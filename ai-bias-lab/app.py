"""ChatRadar (thechatradar.com): la gente hace las mismas preguntas en su chat de IA favorito,
pega las respuestas y la web compara los resultados por chat, idioma y país."""

import csv
import hashlib
import io
import json
import os
import re
import sqlite3
import unicodedata
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse
from pathlib import Path

from flask import (Flask, Response, abort, flash, g, redirect,
                   render_template, request, session, url_for)

from i18n import LANGS, RTL, T

BASE_DIR = Path(__file__).resolve().parent
DATABASE = os.environ.get("DATABASE", str(BASE_DIR / "data.db"))
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")
MAX_PER_HOUR = int(os.environ.get("MAX_PER_HOUR", "10"))
GEOIP_DB = os.environ.get("GEOIP_DB", str(BASE_DIR / "geoip.mmdb"))
MAX_ANSWER = 12000
MIN_METRO = int(os.environ.get("MIN_METRO", "20"))  # respuestas mínimas para mostrar un chat
PUBLIC_URL = os.environ.get("PUBLIC_URL", "https://thechatradar.com").rstrip("/")
BREVO_API_KEY = os.environ.get("BREVO_API_KEY", "")
BREVO_LIST_ID = os.environ.get("BREVO_LIST_ID", "")

CHATS = [
    ("chatgpt", "ChatGPT", "https://chatgpt.com/"),
    ("gemini", "Gemini", "https://gemini.google.com/"),
    ("claude", "Claude", "https://claude.ai/new"),
    ("copilot", "Copilot", "https://copilot.microsoft.com/"),
    ("grok", "Grok", "https://grok.com/"),
    ("meta", "Meta AI", "https://www.meta.ai/"),
    ("deepseek", "DeepSeek", "https://chat.deepseek.com/"),
    ("mistral", "Le Chat (Mistral)", "https://chat.mistral.ai/"),
    ("perplexity", "Perplexity", "https://www.perplexity.ai/"),
    ("otro", "Otro / Other / Autre / אחר", None),
]
CHAT_NAMES = {key: name for key, name, _ in CHATS}

# Dominios desde los que los chats publican conversaciones compartidas.
SHARE_HOSTS = {
    "chatgpt.com", "chat.openai.com", "claude.ai", "g.co", "gemini.google.com",
    "copilot.microsoft.com", "grok.com", "x.com", "www.meta.ai", "meta.ai",
    "chat.deepseek.com", "chat.mistral.ai", "www.perplexity.ai", "perplexity.ai",
}
MIN_ANSWER = 150  # una respuesta real a estas preguntas es mucho más larga
LEAN_KEYS = list(T["lean"])

with open(BASE_DIR / "questions.json", encoding="utf-8") as fh:
    QUESTIONS = json.load(fh)
QUESTIONS_BY_ID = {q["id"]: q for q in QUESTIONS}


def all_fields(q):
    for step in q["steps"]:
        yield from step["fields"]


def field_options(field):
    """Opciones de un campo como lista de (id, {idioma: texto})."""
    if field.get("type") == "yesno":
        return [("yes", T["yes"]), ("no", T["no"])]
    return [(o["id"], o["label"]) for o in field["options"]]


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")


# ------------------------------------------------------------ idioma y país

@app.url_value_preprocessor
def pull_lang(_endpoint, values):
    if values and "lang" in values:
        lang = values.pop("lang")
        if lang not in LANGS:
            abort(404)
        g.lang = lang


@app.url_defaults
def add_lang(endpoint, values):
    if "lang" not in values and app.url_map.is_endpoint_expecting(endpoint, "lang"):
        values["lang"] = g.get("lang", "en")


@app.context_processor
def inject_helpers():
    lang = g.get("lang", "en")

    def fix(text):  # en francés, espacio no separable antes de ? ! : ;
        if lang == "fr" and isinstance(text, str):
            for mark in "?!:;":
                text = text.replace(" " + mark, "\u00a0" + mark)
        return text

    def t(key):
        value = T[key]
        value = value[lang] if isinstance(value, dict) and lang in value else value
        return [fix(v) for v in value] if isinstance(value, list) and value and isinstance(value[0], str) else fix(value)

    def tr(obj):  # texto multilingüe de questions.json
        return fix(obj.get(lang) or obj.get("en") or next(iter(obj.values())))

    return {"t": t, "tr": tr, "lang": lang, "langs": LANGS, "T": T,
            "flag": flag, "rtl": RTL, "dir": "rtl" if lang in RTL else "ltr",
            "geoip_credit": os.path.exists(GEOIP_DB)}


def flag(code):
    if not code or len(code) != 2 or not code.isalpha():
        return "🏳️"
    return "".join(chr(0x1F1E6 + ord(ch) - ord("A")) for ch in code.upper())


def client_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "")
    return ip.split(",")[0].strip()


_geo_reader = None


def detect_country():
    """País aproximado (código ISO de 2 letras) a partir de la conexión.

    Primero mira las cabeceras que añaden algunos proxies (Cloudflare, Vercel…);
    si no hay, consulta una base GeoIP local (fichero .mmdb) si existe."""
    for header in ("CF-IPCountry", "X-Vercel-IP-Country", "X-Country-Code",
                   "X-AppEngine-Country"):
        code = request.headers.get(header, "").strip().upper()
        if len(code) == 2 and code.isalpha() and code != "XX":
            return code

    global _geo_reader
    if _geo_reader is None:
        try:
            import maxminddb
            _geo_reader = maxminddb.open_database(GEOIP_DB)
        except Exception:  # sin librería o sin fichero: no detectamos
            _geo_reader = False
    if _geo_reader:
        try:
            rec = _geo_reader.get(client_ip()) or {}
            code = (rec.get("country") or {}).get("iso_code", "")
            return code.upper() if code else ""
        except ValueError:
            return ""
    return ""


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
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id TEXT NOT NULL,
                lang TEXT NOT NULL,
                country TEXT,
                chat TEXT NOT NULL,
                model TEXT,
                answers TEXT NOT NULL,
                fields TEXT NOT NULL,
                lean TEXT,
                ip_hash TEXT,
                created_at TEXT NOT NULL
            )""")
        db.execute("CREATE INDEX IF NOT EXISTS idx_sub_q ON submissions(question_id)")
        # emails: tabla aparte y sin ningún vínculo con las respuestas
        db.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                email TEXT PRIMARY KEY,
                lang TEXT NOT NULL,
                consent_date TEXT NOT NULL
            )""")
        db.execute("""
            CREATE TABLE IF NOT EXISTS proposals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lang TEXT NOT NULL,
                country TEXT,
                topic TEXT NOT NULL,
                question TEXT NOT NULL,
                why TEXT,
                ip_hash TEXT,
                created_at TEXT NOT NULL
            )""")
        cols = {r[1] for r in db.execute("PRAGMA table_info(submissions)")}
        for col, kind in [("share_url", "TEXT"), ("flags", "TEXT DEFAULT ''"),
                          ("answers_hash", "TEXT"), ("checked", "INTEGER DEFAULT 0")]:
            if col not in cols:
                db.execute(f"ALTER TABLE submissions ADD COLUMN {col} {kind}")


def normalize(text):
    text = unicodedata.normalize("NFKD", text.lower())
    return " ".join("".join(ch for ch in text if not unicodedata.combining(ch)).split())


def valid_share_url(url):
    try:
        parsed = urlparse(url)
    except ValueError:
        return False
    return parsed.scheme == "https" and parsed.hostname in SHARE_HOSTS and len(parsed.path) > 1


def quality_flags(q, answers, answers_hash, share_url, db):
    """Señales de que un envío no corresponde a las preguntas. No se muestran a quien
    envía (sería una guía para engañar); los envíos marcados no cuentan en los resultados."""
    flags = []
    keywords = [normalize(k) for k in q.get("keywords", [])]
    for i, text in enumerate(answers, start=1):
        if share_url and not text:
            continue  # solo enlace: se comprueba abriéndolo, no por el texto
        norm = normalize(text)
        if len(text) < MIN_ANSWER:
            flags.append(f"short{i}")
        if keywords and not any(k in norm for k in keywords):
            flags.append(f"offtopic{i}")
    if len(answers) > 1 and len({normalize(a) for a in answers}) < len(answers):
        flags.append("same_text")
    if any(answers) and db.execute(
            "SELECT 1 FROM submissions WHERE answers_hash = ? LIMIT 1", (answers_hash,)).fetchone():
        flags.append("duplicate")
    elif share_url and db.execute(
            "SELECT 1 FROM submissions WHERE share_url = ? LIMIT 1", (share_url,)).fetchone():
        flags.append("duplicate")
    return flags


def ip_hash():
    return hashlib.sha256((app.secret_key + client_ip()).encode()).hexdigest()[:16]


def count_by_question():
    rows = get_db().execute(
        "SELECT question_id, COUNT(*) AS n FROM submissions GROUP BY question_id")
    return {r["question_id"]: r["n"] for r in rows}


def distribution(rows, key_fn, keys):
    total = len(rows)
    c = Counter(key_fn(r) for r in rows)
    return total, [(c[k], round(100 * c[k] / total) if total else 0) for k in keys]


# ------------------------------------------------------------------ routes

@app.route("/")
def landing():
    g.lang = "en"  # la portada principal es en inglés; el menú permite cambiar de idioma
    return index()


@app.route("/<lang>/")
def index():
    q = QUESTIONS[0]
    rows = [r for r in get_db().execute(
        "SELECT lean, flags FROM submissions WHERE question_id = ?", (q["id"],)) if not r["flags"]]
    # gauge = {"ok": bool, "n": respuestas con postura, "pos": 0-100 (0 = postura israelí,
    #          50 = equilibrado, 100 = postura palestina), "pct": {...}, "missing": cuántas faltan}
    return render_template("index.html", questions=QUESTIONS,
                           counts=count_by_question(), gauge=lean_score(rows),
                           total_valid=len(rows), min_metro=MIN_METRO)


@app.route("/<lang>/q/<qid>", methods=["GET", "POST"])
def question(qid):
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    lang = g.lang
    form = {}

    if request.method == "POST":
        form = request.form
        errors = []

        if form.get("website"):  # honeypot: solo lo rellenan los bots
            return redirect(url_for("results", qid=qid))

        chat = form.get("chat", "")
        if chat not in CHAT_NAMES:
            errors.append(T["err_chat"][lang])

        share_url = form.get("share_url", "").strip()[:500]
        if share_url and not valid_share_url(share_url):
            errors.append(T["err_share"][lang])

        # basta con el enlace a la conversación o con el texto de la respuesta
        answers = []
        for i, _step in enumerate(q["steps"], start=1):
            text = form.get(f"answer{i}", "").strip()
            if len(text) > MAX_ANSWER:
                errors.append(T["err_long"][lang])
            answers.append(text)
        if not share_url and any(len(a) < 2 for a in answers):
            errors.append(T["err_answer_or_link"][lang])

        values, missing = {}, []
        for field in all_fields(q):
            value = form.get(field["id"], "")
            if value not in [k for k, _ in field_options(field)]:
                value = ""
                if field.get("required"):
                    missing.append(field["label"][lang])
            values[field["id"]] = value
        if len(missing) == 1:
            errors.append(f"{T['err_field'][lang]} {missing[0]}")
        elif missing:
            errors.append(T["err_fields"][lang].format(n=len(missing)))

        lean = form.get("lean", "")
        if lean not in LEAN_KEYS:
            errors.append(T["err_lean"][lang])

        db = get_db()
        since = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        recent = db.execute(
            "SELECT COUNT(*) FROM submissions WHERE ip_hash = ? AND created_at > ?",
            (ip_hash(), since)).fetchone()[0]
        if recent >= MAX_PER_HOUR:
            errors.append(T["err_rate"][lang])

        if not errors:
            answers_hash = hashlib.sha256(
                "\n".join(normalize(a) for a in answers).encode()).hexdigest()
            flags = quality_flags(q, answers, answers_hash, share_url, db)
            db.execute(
                """INSERT INTO submissions (question_id, lang, country, chat, model,
                   answers, fields, lean, ip_hash, created_at,
                   share_url, flags, answers_hash, checked)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)""",
                (qid, lang, detect_country(), chat, form.get("model", "").strip()[:80],
                 json.dumps(answers, ensure_ascii=False),
                 json.dumps(values, ensure_ascii=False), lean, ip_hash(),
                 datetime.now(timezone.utc).isoformat(),
                 share_url or None, ",".join(flags), answers_hash))
            db.commit()
            done = session.get("done", {})
            done[qid] = sorted(set(done.get(qid, [])) | {chat})
            session["done"] = done
            session["just_sent"] = qid
            return redirect(url_for("next_chat", qid=qid, chat=chat))

        for e in errors:
            flash(e, "error")

    if request.method == "GET" and request.args.get("chat") in CHAT_NAMES:
        form = {"chat": request.args["chat"]}
    return render_template("question.html", q=q, chats=CHATS, form=form,
                           field_options=field_options,
                           count=count_by_question().get(qid, 0))


@app.route("/<lang>/q/<qid>/next")
def next_chat(qid):
    """Tras enviar: invitar a probar la misma pregunta en otro chat antes de ver resultados."""
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    done = session.get("done", {}).get(qid, [])
    last = request.args.get("chat", "")
    others = [(k, n, l) for k, n, l in CHATS if l and k not in done and k != last]
    return render_template("next.html", q=q, others=others,
                           done=[CHAT_NAMES[c] for c in done if c in CHAT_NAMES],
                           last=CHAT_NAMES.get(last, ""))


@app.route("/<lang>/q/<qid>/results")
def results(qid):
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    lang = g.lang
    every = get_db().execute(
        "SELECT * FROM submissions WHERE question_id = ? ORDER BY id DESC",
        (qid,)).fetchall()

    admin = bool(ADMIN_TOKEN) and request.args.get("token") == ADMIN_TOKEN
    flagged = [r for r in every if r["flags"]]
    every = [r for r in every if not r["flags"]]  # los sospechosos no cuentan

    f_lang = request.args.get("l", "")
    f_country = request.args.get("c", "")
    f_quality = request.args.get("v", "")
    rows = [r for r in every
            if (not f_lang or r["lang"] == f_lang)
            and (not f_country or (r["country"] or "") == f_country)
            and (f_quality != "link" or r["share_url"])
            and (f_quality != "checked" or r["checked"])]
    n_link = sum(1 for r in every if r["share_url"])
    n_checked = sum(1 for r in every if r["checked"])
    countries = Counter(r["country"] or "" for r in every).most_common()

    by_chat = defaultdict(list)
    for r in rows:
        by_chat[r["chat"]].append(r)
    chat_order = [k for k, _, _ in CHATS if k in by_chat]
    metronome = [dict(chat=CHAT_NAMES[c], all=lean_score(by_chat[c]),
                      link=lean_score([r for r in by_chat[c] if r["share_url"]]))
                 for c in chat_order]
    metronome.insert(0, dict(chat=T["all_chats"][lang], all=lean_score(rows),
                             link=lean_score([r for r in rows if r["share_url"]])))
    parsed = {r["id"]: json.loads(r["fields"]) for r in rows + flagged}

    tables = []
    for field in all_fields(q):
        opts = field_options(field)
        keys = [k for k, _ in opts]
        table = []
        for chat in [None] + chat_order:
            subset = [r for r in (rows if chat is None else by_chat[chat])
                      if parsed[r["id"]].get(field["id"])]  # los campos opcionales sin marcar no cuentan
            total, cells = distribution(
                subset, lambda r: parsed[r["id"]].get(field["id"]), keys)
            table.append({"name": T["all_chats"][lang] if chat is None else CHAT_NAMES[chat],
                          "total": total, "cells": cells})
        tables.append({"label": field["label"][lang],
                       "options": [label[lang] for _, label in opts], "rows": table})

    def lean_rows(groups):
        out = []
        for name, subset in groups:
            total, cells = distribution(subset, lambda r: r["lean"], LEAN_KEYS)
            out.append({"name": name, "total": total, "cells": cells})
        return out

    by_lang = defaultdict(list)
    by_country = defaultdict(list)
    for r in rows:
        by_lang[r["lang"]].append(r)
        by_country[r["country"] or ""].append(r)
    lean_tables = [
        (T["chat"][lang], lean_rows([(CHAT_NAMES[c], by_chat[c]) for c in chat_order])),
        (T["by_lang"][lang], lean_rows([(LANGS[l], by_lang[l]) for l in LANGS if l in by_lang])),
        (T["by_country"][lang], lean_rows(
            [(f"{flag(c)} {c or T['unknown'][lang]}", s)
             for c, s in sorted(by_country.items(), key=lambda kv: -len(kv[1]))[:15]])),
    ]

    labels = {f["id"]: {k: v[lang] for k, v in field_options(f)} for f in all_fields(q)}
    choice_fields = {f["id"] for f in all_fields(q) if f.get("type") != "yesno"}
    latest = [{
        "id": r["id"], "chat": CHAT_NAMES.get(r["chat"], r["chat"]),
        "model": r["model"], "lang": LANGS.get(r["lang"], r["lang"]),
        "country": r["country"], "answers": json.loads(r["answers"]),
        "lean": T["lean"].get(r["lean"], {}).get(lang, ""),
        "share_url": r["share_url"], "checked": r["checked"], "flags": r["flags"],
        "tags": [labels[f][v] for f, v in parsed[r["id"]].items()
                 if f in choice_fields and v in labels[f]],
        "date": r["created_at"][:10],
    } for r in (rows[:30] + (flagged[:50] if admin else []))]

    return render_template(
        "results.html", q=q, total=len(rows), grand_total=len(every),
        tables=tables, lean_tables=lean_tables, latest=latest,
        countries=countries,
        f_lang=f_lang, f_country=f_country, f_quality=f_quality,
        n_link=n_link, n_checked=n_checked, n_flagged=len(flagged), admin=admin,
        metronome=metronome, min_metro=MIN_METRO,
        just_sent=session.pop("just_sent", None) == qid, share_url=public_home_url(),
        subscribed=request.args.get("sub") == "1")


@app.route("/admin/check/<int:rid>", methods=["POST"])
def admin_check(rid):
    if not ADMIN_TOKEN or request.form.get("token") != ADMIN_TOKEN:
        abort(403)
    db = get_db()
    row = db.execute("SELECT question_id FROM submissions WHERE id = ?", (rid,)).fetchone()
    # comprobada a mano: cuenta aunque el filtro automático la hubiera marcado
    db.execute("UPDATE submissions SET checked = 1, flags = '' WHERE id = ?", (rid,))
    db.commit()
    qid = row["question_id"] if row else QUESTIONS[0]["id"]
    return redirect(url_for("results", lang="es", qid=qid, token=ADMIN_TOKEN))


@app.route("/<lang>/propose", methods=["GET", "POST"])
def propose():
    lang = g.lang
    form = {}
    if request.method == "POST":
        form = request.form
        if form.get("website"):  # honeypot
            return redirect(url_for("propose"))
        topic = form.get("topic", "").strip()[:120]
        question_text = form.get("question", "").strip()[:2000]
        why = form.get("why", "").strip()[:3000]
        db = get_db()
        since = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        recent = db.execute("SELECT COUNT(*) FROM proposals WHERE ip_hash = ? AND created_at > ?",
                            (ip_hash(), since)).fetchone()[0]
        if len(topic) < 2 or len(question_text) < 15:
            flash(T["prop_err"][lang], "error")
        elif recent >= MAX_PER_HOUR:
            flash(T["err_rate"][lang], "error")
        else:
            db.execute(
                "INSERT INTO proposals (lang, country, topic, question, why, ip_hash, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (lang, detect_country(), topic, question_text, why, ip_hash(),
                 datetime.now(timezone.utc).isoformat()))
            db.commit()
            flash(T["prop_thanks"][lang])
            return redirect(url_for("propose"))
    return render_template("propose.html", form=form)


@app.route("/admin/proposals")
def admin_proposals():
    if not ADMIN_TOKEN or request.args.get("token") != ADMIN_TOKEN:
        abort(403)
    rows = get_db().execute("SELECT * FROM proposals ORDER BY id DESC").fetchall()
    if request.args.get("format") == "csv":
        out = io.StringIO()
        writer = csv.writer(out)
        writer.writerow(["id", "lang", "country", "topic", "question", "why", "created_at"])
        for r in rows:
            writer.writerow([r["id"], r["lang"], r["country"], r["topic"], r["question"],
                             r["why"], r["created_at"]])
        return Response("\ufeff" + out.getvalue(), mimetype="text/csv",
                        headers={"Content-Disposition": "attachment; filename=proposals.csv"})
    g.lang = "es"
    return render_template("admin_proposals.html", rows=rows, token=ADMIN_TOKEN)


@app.route("/admin/proposals/<int:pid>/delete", methods=["POST"])
def admin_delete_proposal(pid):
    if not ADMIN_TOKEN or request.form.get("token") != ADMIN_TOKEN:
        abort(403)
    db = get_db()
    db.execute("DELETE FROM proposals WHERE id = ?", (pid,))
    db.commit()
    return redirect(url_for("admin_proposals", token=ADMIN_TOKEN))


@app.route("/<lang>/method")
def method():
    return render_template("method.html")


def lean_score(rows):
    """Posición en el metrónomo según lo que marcaron quienes participaron:
    -1 = hacia la postura israelí, 0 = equilibrada, +1 = hacia la postura palestina.
    «No estoy seguro» no cuenta para la posición."""
    c = Counter(r["lean"] for r in rows)
    n = c["pro_israel"] + c["balanced"] + c["pro_palestine"]
    if n < MIN_METRO:
        return {"ok": False, "n": n, "missing": MIN_METRO - n}
    score = (c["pro_palestine"] - c["pro_israel"]) / n
    return {"ok": True, "n": n, "pos": round(50 + 50 * score, 1),
            "pct": {k: round(100 * c[k] / n) for k in ("pro_israel", "balanced", "pro_palestine")}}


def public_home_url():
    root = PUBLIC_URL or request.url_root.rstrip("/")
    return f"{root}/{g.lang}/"


def push_to_brevo(email, lang):
    """Da de alta el contacto en la lista de Brevo, si está configurada."""
    if not (BREVO_API_KEY and BREVO_LIST_ID):
        return
    body = json.dumps({"email": email, "listIds": [int(BREVO_LIST_ID)],
                       "attributes": {"LANGUAGE": lang}, "updateEnabled": True}).encode()
    req = urllib.request.Request(
        "https://api.brevo.com/v3/contacts", data=body, method="POST",
        headers={"api-key": BREVO_API_KEY, "Content-Type": "application/json",
                 "Accept": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=5).close()
    except Exception as exc:  # el email queda guardado igualmente en la base local
        app.logger.warning("Brevo: %s", exc)


@app.route("/<lang>/subscribe", methods=["POST"])
def subscribe():
    lang = g.lang
    qid = request.form.get("qid") if request.form.get("qid") in QUESTIONS_BY_ID else QUESTIONS[0]["id"]
    email = request.form.get("email", "").strip().lower()[:200]
    if request.form.get("website"):  # honeypot
        return redirect(url_for("results", qid=qid))
    if not request.form.get("consent") or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        flash(T["email_err"][lang], "error")
        session["just_sent"] = qid  # vuelve a mostrar el panel
        return redirect(url_for("results", qid=qid) + "#thanks")
    db = get_db()
    # solo la fecha, sin hora: así no se puede cruzar con el momento de un envío
    db.execute("INSERT OR IGNORE INTO subscribers (email, lang, consent_date) VALUES (?, ?, ?)",
               (email, lang, datetime.now(timezone.utc).date().isoformat()))
    db.commit()
    push_to_brevo(email, lang)
    return redirect(url_for("results", qid=qid, sub=1) + "#thanks")


@app.route("/admin/subscribers.csv")
def admin_subscribers():
    if not ADMIN_TOKEN or request.args.get("token") != ADMIN_TOKEN:
        abort(403)
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["email", "lang", "consent_date"])
    for r in get_db().execute("SELECT email, lang, consent_date FROM subscribers ORDER BY consent_date"):
        writer.writerow(list(r))
    return Response("\ufeff" + out.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=subscribers.csv"})


@app.route("/export.csv")
def export_csv():
    out = io.StringIO()
    writer = csv.writer(out)
    field_ids = [f["id"] for q in QUESTIONS for f in all_fields(q)]
    n_steps = max(len(q["steps"]) for q in QUESTIONS)
    writer.writerow(["id", "question", "lang", "country", "chat", "model",
                     *[f"answer{i}" for i in range(1, n_steps + 1)], *field_ids, "lean", "share_url",
                     "checked", "flags", "created_at"])
    for r in get_db().execute("SELECT * FROM submissions ORDER BY id"):
        answers = (json.loads(r["answers"]) + [""] * n_steps)[:n_steps]
        fields = json.loads(r["fields"])
        writer.writerow([r["id"], r["question_id"], r["lang"], r["country"],
                         r["chat"], r["model"], *answers,
                         *[fields.get(f, "") for f in field_ids],
                         r["lean"], r["share_url"] or "", r["checked"],
                         r["flags"] or "", r["created_at"]])
    return Response("﻿" + out.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=ai-bias-lab.csv"})


@app.route("/admin/delete/<int:rid>", methods=["POST"])
def admin_delete(rid):
    if not ADMIN_TOKEN or request.form.get("token") != ADMIN_TOKEN:
        abort(403)
    db = get_db()
    row = db.execute("SELECT question_id FROM submissions WHERE id = ?", (rid,)).fetchone()
    db.execute("DELETE FROM submissions WHERE id = ?", (rid,))
    db.commit()
    qid = row["question_id"] if row else QUESTIONS[0]["id"]
    return redirect(url_for("results", lang="es", qid=qid, token=ADMIN_TOKEN))


init_db()

if __name__ == "__main__":
    app.run(debug=True)
