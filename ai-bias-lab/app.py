"""AI Bias Lab: la gente hace la misma pregunta en su chat de IA favorito,
pega la respuesta y la web compara los resultados entre chats."""

import csv
import hashlib
import io
import json
import os
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from flask import (Flask, Response, abort, flash, g, redirect,
                   render_template, request, url_for)

BASE_DIR = Path(__file__).resolve().parent
DATABASE = os.environ.get("DATABASE", str(BASE_DIR / "data.db"))
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")
MAX_PER_HOUR = int(os.environ.get("MAX_PER_HOUR", "10"))

CHATS = [
    ("chatgpt", "ChatGPT", "https://chatgpt.com/"),
    ("claude", "Claude", "https://claude.ai/new"),
    ("gemini", "Gemini", "https://gemini.google.com/"),
    ("copilot", "Copilot", "https://copilot.microsoft.com/"),
    ("meta", "Meta AI", "https://www.meta.ai/"),
    ("grok", "Grok", "https://grok.com/"),
    ("deepseek", "DeepSeek", "https://chat.deepseek.com/"),
    ("mistral", "Le Chat (Mistral)", "https://chat.mistral.ai/"),
    ("perplexity", "Perplexity", "https://www.perplexity.ai/"),
    ("otro", "Otro", None),
]
CHAT_NAMES = {key: name for key, name, _ in CHATS}
PERCEPTION = {"si": "Sí", "no": "No", "nose": "No estoy seguro"}

with open(BASE_DIR / "questions.json", encoding="utf-8") as fh:
    QUESTIONS = json.load(fh)
QUESTIONS_BY_ID = {q["id"]: q for q in QUESTIONS}

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")


# ---------------------------------------------------------------- database

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(DATABASE) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id TEXT NOT NULL,
                chat TEXT NOT NULL,
                model TEXT,
                answer TEXT NOT NULL,
                fields TEXT NOT NULL,
                perceived_bias TEXT,
                country TEXT,
                ip_hash TEXT,
                created_at TEXT NOT NULL
            )""")
        db.execute("CREATE INDEX IF NOT EXISTS idx_q ON responses(question_id)")


def ip_hash():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "")
    ip = ip.split(",")[0].strip()
    return hashlib.sha256((app.secret_key + ip).encode()).hexdigest()[:16]


def count_by_question():
    rows = get_db().execute(
        "SELECT question_id, COUNT(*) AS n FROM responses GROUP BY question_id")
    return {r["question_id"]: r["n"] for r in rows}


# ------------------------------------------------------------------ routes

@app.route("/")
def index():
    return render_template("index.html", questions=QUESTIONS,
                           counts=count_by_question())


@app.route("/q/<qid>", methods=["GET", "POST"])
def question(qid):
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    form = {}

    if request.method == "POST":
        form = request.form
        errors = []

        if form.get("website"):  # honeypot: solo lo rellenan los bots
            return redirect(url_for("results", qid=qid))

        chat = form.get("chat", "")
        answer = form.get("answer", "").strip()
        if chat not in CHAT_NAMES:
            errors.append("Elige qué chat usaste.")
        if len(answer) < 2:
            errors.append("Pega la respuesta que te dio el chat.")
        if len(answer) > 5000:
            errors.append("La respuesta es demasiado larga (máximo 5000 caracteres).")

        values = {}
        for field in q["fields"]:
            value = form.get(field["id"], "")
            if value not in field["options"]:
                errors.append(f"Responde: {field['label']}")
            values[field["id"]] = value

        perceived = form.get("perceived_bias", "")
        if perceived not in PERCEPTION:
            errors.append("Dinos si crees que la respuesta tiene sesgo.")

        db = get_db()
        since = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        recent = db.execute(
            "SELECT COUNT(*) FROM responses WHERE ip_hash = ? AND created_at > ?",
            (ip_hash(), since)).fetchone()[0]
        if recent >= MAX_PER_HOUR:
            errors.append("Has enviado muchas respuestas seguidas. Vuelve a intentarlo en una hora.")

        if not errors:
            db.execute(
                """INSERT INTO responses (question_id, chat, model, answer, fields,
                   perceived_bias, country, ip_hash, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (qid, chat, form.get("model", "").strip()[:80], answer,
                 json.dumps(values, ensure_ascii=False), perceived,
                 form.get("country", "").strip()[:60], ip_hash(),
                 datetime.now(timezone.utc).isoformat()))
            db.commit()
            flash("¡Gracias! Tu respuesta ya cuenta en los resultados.")
            return redirect(url_for("results", qid=qid))

        for e in errors:
            flash(e, "error")

    return render_template("question.html", q=q, chats=CHATS,
                           perception=PERCEPTION, form=form,
                           count=count_by_question().get(qid, 0))


@app.route("/q/<qid>/resultados")
def results(qid):
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    rows = get_db().execute(
        "SELECT * FROM responses WHERE question_id = ? ORDER BY id DESC",
        (qid,)).fetchall()

    by_chat = defaultdict(list)
    for r in rows:
        by_chat[r["chat"]].append(r)
    chat_order = [k for k, _, _ in CHATS if k in by_chat]

    # tablas: por cada campo, filas = chats, columnas = opciones (en %)
    tables = []
    for field in q["fields"]:
        table = []
        for chat in ["__all__"] + chat_order:
            subset = rows if chat == "__all__" else by_chat[chat]
            c = Counter(json.loads(r["fields"]).get(field["id"]) for r in subset)
            total = len(subset)
            table.append({
                "chat": "Todos los chats" if chat == "__all__" else CHAT_NAMES[chat],
                "total": total,
                "cells": [(c[o], round(100 * c[o] / total) if total else 0)
                          for o in field["options"]],
            })
        tables.append({"field": field, "rows": table})

    perception = []
    for chat in chat_order:
        c = Counter(r["perceived_bias"] for r in by_chat[chat])
        total = len(by_chat[chat])
        perception.append({
            "chat": CHAT_NAMES[chat], "total": total,
            "cells": [(c[k], round(100 * c[k] / total)) for k in PERCEPTION],
        })

    latest = [{
        "id": r["id"],
        "chat": CHAT_NAMES.get(r["chat"], r["chat"]),
        "model": r["model"], "country": r["country"], "answer": r["answer"],
        "fields": json.loads(r["fields"]),
        "perceived": PERCEPTION.get(r["perceived_bias"], ""),
        "date": r["created_at"][:10],
    } for r in rows[:50]]

    return render_template("results.html", q=q, total=len(rows), tables=tables,
                           perception=perception, perception_labels=PERCEPTION,
                           latest=latest, admin=bool(ADMIN_TOKEN) and
                           request.args.get("token") == ADMIN_TOKEN)


@app.route("/export.csv")
def export_csv():
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["id", "pregunta", "chat", "modelo", "pais", "respuesta",
                     "campos", "percibe_sesgo", "fecha"])
    for r in get_db().execute("SELECT * FROM responses ORDER BY id"):
        writer.writerow([r["id"], r["question_id"], r["chat"], r["model"],
                         r["country"], r["answer"], r["fields"],
                         r["perceived_bias"], r["created_at"]])
    return Response(out.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=respuestas.csv"})


@app.route("/admin/delete/<int:rid>", methods=["POST"])
def admin_delete(rid):
    if not ADMIN_TOKEN or request.form.get("token") != ADMIN_TOKEN:
        abort(403)
    db = get_db()
    row = db.execute("SELECT question_id FROM responses WHERE id = ?", (rid,)).fetchone()
    db.execute("DELETE FROM responses WHERE id = ?", (rid,))
    db.commit()
    qid = row["question_id"] if row else QUESTIONS[0]["id"]
    return redirect(url_for("results", qid=qid, token=ADMIN_TOKEN))


@app.route("/metodo")
def method():
    return render_template("method.html")


init_db()

if __name__ == "__main__":
    app.run(debug=True)
