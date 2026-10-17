"""ChatRadar (thechatradar.com): la gente hace las mismas preguntas en su chat de IA favorito,
pega las respuestas y la web compara los resultados por chat, idioma y país."""

import csv
import hashlib
import io
import json
import os
import random
import re
import sqlite3
import unicodedata
import urllib.request
from urllib.parse import urlparse
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
MIN_METRO = int(os.environ.get("MIN_METRO", "1"))  # respuestas mínimas para mostrar un chat.
# Decisión del proyecto: con 1 respuesta ya se ve la aguja, y las agujas de la portada se ven
# sin haber participado. Las pruebas con personas reales quedan como base inicial de datos.
# (Para volver a ocultarlas hasta participar: PREVIEW_NEEDLES=0.)
PREVIEW_NEEDLES = os.environ.get("PREVIEW_NEEDLES", "1") == "1"
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
    "chatgpt.com", "chat.openai.com", "claude.ai", "g.co", "gemini.google.com", "share.gemini.google",
    "copilot.microsoft.com", "grok.com", "x.com", "www.meta.ai", "meta.ai",
    "chat.deepseek.com", "chat.mistral.ai", "www.perplexity.ai", "perplexity.ai",
}
MIN_ANSWER = 150  # una respuesta real a estas preguntas es mucho más larga
LEAN_KEYS = list(T["lean"])
STANCE_KEYS = list(T["stance"])  # postura propia, opcional
SHARE_NETS = ("whatsapp", "instagram", "facebook", "x", "telegram", "linkedin", "copy", "native")

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
            "geoip_credit": os.path.exists(GEOIP_DB), "public_url": site_root()}


_STOP = {
    "es": " el la los las que de del y en es por una con para como pero sus fue han ha se ".split(),
    "en": " the and of to is that in for with as are was have has it this by not ".split(),
    "fr": " le la les des et est que une pour dans pas qui sur avec il a du au ".split(),
}


def answer_lang(text, fallback):
    """Idioma en que respondió el chat (el de la pregunta que se le hizo), no el de la página.
    Si no está claro, el idioma de la página."""
    if len(re.findall(r"[\u0590-\u05FF]", text or "")) > 30:
        return "he"
    words = re.findall(r"[a-zà-ÿ']+", (text or "").lower())
    score = {k: sum(1 for w in words if w in v) for k, v in _STOP.items()}
    best = sorted(score, key=score.get, reverse=True)
    if score[best[0]] >= 8 and score[best[0]] >= 1.5 * score[best[1]]:
        return best[0]
    return fallback


def row_lang(r):
    return (r["alang"] if "alang" in r.keys() else None) or r["lang"]


# Lista de afirmaciones (borrador, pendiente de revisión por ambos lados). Por ahora solo la ve
# la administración: segunda aguja en la portada y detalle por respuesta en resultados.
CLAIMS_FILE = BASE_DIR / "borradores" / "afirmaciones" / "catalogo-afirmaciones.json"
try:
    with open(CLAIMS_FILE, encoding="utf-8") as fh:
        CLAIMS = json.load(fh)["claims"]
except (OSError, ValueError, KeyError):
    CLAIMS = []
# cuando aparece la versión con los dos lados, no se cuentan además sus mitades
CLAIM_SUPERSEDES = {"disengagement_both_views": {"gaza_disengagement_2005", "occupation_context"}}


def _norm(text):
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch)).lower()
    for a, b in (("’", "'"), ("‘", "'"), ("´", "'"), ("״", '"'), ("“", '"'), ("”", '"')):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text)


_CLAIM_CACHE = {}


def claims_in(text):
    """Afirmaciones de la lista que aparecen en el texto: [(id, side)]."""
    key = hashlib.sha1((text or "").encode("utf-8")).hexdigest()
    if key in _CLAIM_CACHE:
        return _CLAIM_CACHE[key]
    t, found = _norm(text), []
    for c in CLAIMS:
        for trig in (x for ts in c["triggers"].values() for x in ts):
            hit = re.search(_norm(trig[3:]), t) if trig.startswith("re:") else _norm(trig) in t
            if hit:
                found.append((c["id"], c["side"]))
                break
    drop = set().union(*(CLAIM_SUPERSEDES.get(i, set()) for i, _ in found)) if found else set()
    found = [x for x in found if x[0] not in drop]
    _CLAIM_CACHE[key] = found
    return found


def claims_pos(rs):
    """Posición 0-100 según la lista: (lado palestino − lado israelí) / total de afirmaciones.
    Media de las respuestas que tienen alguna afirmación."""
    vals = []
    for r in rs:
        found = claims_in(" ".join(json.loads(r["answers"] or "[]")))
        if found:
            isr = sum(1 for _, sd in found if sd == "israeli")
            pal = sum(1 for _, sd in found if sd == "palestinian")
            vals.append((pal - isr) / len(found))
    return (round(50 + 50 * sum(vals) / len(vals), 1) if vals else None), len(vals)


_URL_RE = re.compile(r"https?://[^\s)\]>\"'<]+", re.I)


ORIGIN_GROUPS = ["israeli", "palestinian", "muslim_countries", "un_courts", "intl_ngos", "western", "other"]
with open(BASE_DIR / "source_origins.json", encoding="utf-8") as fh:
    _origins = json.load(fh)
ORIGIN_OF = {dom: grp for grp in ORIGIN_GROUPS if grp != "other" for dom in _origins.get(grp, [])}
SOURCE_ALIASES = _origins.get("aliases", {})  # nombre con que un chat muestra la fuente → dominio


def source_origin(domain):
    """Grupo de origen de una fuente (por el país que la posee o financia, o por organización
    internacional). Se busca el dominio y, si no está, sus dominios padres. Sin clasificar: «other»."""
    parts = domain.split(".")
    for i in range(len(parts) - 1):
        grp = ORIGIN_OF.get(".".join(parts[i:]))
        if grp:
            return grp
    return "other"


def source_names(text):
    """Fuentes pegadas aparte (p. ej. la ventana «Sources» de Gemini, que da nombres y no direcciones):
    una línea que es el nombre de un medio u organización conocido, o un título que termina en
    « - Nombre» o « | Nombre». Se devuelven sus dominios."""
    found = []
    for line in (text or "").splitlines():
        low = re.sub(r"\s+", " ", line).strip().lower()
        if not low:
            continue
        for name, dom in SOURCE_ALIASES.items():
            if low == name or low.endswith((" - " + name, " | " + name, " – " + name)):
                if dom not in found:
                    found.append(dom)
                break
    return found


def source_domains(text, extra=""):
    """Dominios de las fuentes que el chat incluyó en su respuesta, sin repetir y en orden.
    ChatGPT copia cada fuente como icono de Google (…/s2/favicons?domain=https://www.reuters.com…):
    de esos se toma el dominio de la fuente, no el de Google. Se guarda solo el dominio, sin la ruta."""
    found = []
    for url in _URL_RE.findall((text or "") + "\n" + (extra or "")):
        url = url.rstrip(".,;:")
        m = re.search(r"[?&]domain=(?:https?://)?([^&/\s]+)", url)
        host = m.group(1) if m else urlparse(url).hostname or ""
        host = host.lower().strip("\\").removeprefix("www.")  # el texto copiado a veces trae «\&»
        if host and "." in host and host not in found:
            found.append(host)
    for dom in source_names(extra):
        if dom not in found:
            found.append(dom)
    return found


@app.template_filter("clean_answer")
def clean_answer(text):
    """Al mostrar una respuesta pegada, quita los iconos de fuentes que algunos chats copian como
    imágenes en Markdown (![](https://…favicons…)). El texto guardado no cambia."""
    return re.sub(r"!\[[^\]]*\]\([^)]*\)\s*", "", text or "")


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
            # formato MaxMind/DB-IP oficial ({"country": {"iso_code"}}) o el de ip-location-db ({"country_code"})
            code = (rec.get("country") or {}).get("iso_code", "") or rec.get("country_code", "")
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
                          ("answers_hash", "TEXT"), ("checked", "INTEGER DEFAULT 0"),
                          ("stance", "TEXT"), ("order_flip", "INTEGER"), ("qversion", "INTEGER"),
                          ("sources", "TEXT"), ("sources_text", "TEXT"), ("alang", "TEXT")]:
            if col not in cols:
                db.execute(f"ALTER TABLE submissions ADD COLUMN {col} {kind}")
                if col == "sources":  # rellenar las respuestas que ya estaban guardadas
                    for rid, answers in db.execute("SELECT id, answers FROM submissions").fetchall():
                        doms = source_domains(" ".join(json.loads(answers or "[]")))
                        db.execute("UPDATE submissions SET sources = ? WHERE id = ?", (",".join(doms), rid))
                if col == "alang":  # idioma de las respuestas ya guardadas
                    for rid, answers, plang in db.execute("SELECT id, answers, lang FROM submissions").fetchall():
                        db.execute("UPDATE submissions SET alang = ? WHERE id = ?",
                                   (answer_lang(" ".join(json.loads(answers or "[]")), plang), rid))
        sub_cols = {r[1] for r in db.execute("PRAGMA table_info(subscribers)")}
        if "instagram" not in sub_cols:
            db.execute("ALTER TABLE subscribers ADD COLUMN instagram TEXT")
        # contadores anónimos: de qué red llegan visitas y en qué botón de compartir se pulsa
        db.execute("""
            CREATE TABLE IF NOT EXISTS counters (
                day TEXT NOT NULL, kind TEXT NOT NULL, name TEXT NOT NULL,
                n INTEGER NOT NULL DEFAULT 0, PRIMARY KEY (day, kind, name)
            )""")


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


def bump(kind, name):
    db = get_db()
    day = datetime.now(timezone.utc).date().isoformat()
    db.execute("INSERT INTO counters (day, kind, name, n) VALUES (?, ?, ?, 1) "
               "ON CONFLICT(day, kind, name) DO UPDATE SET n = n + 1", (day, kind, name))
    db.commit()


def valid_rows(qid):
    """Envíos que cuentan: sin señales de calidad y respondidos con la versión vigente de la
    pregunta (las respuestas a otra redacción no se mezclan; las antiguas no tienen versión = 1)."""
    version = QUESTIONS_BY_ID[qid].get("version", 1) if qid in QUESTIONS_BY_ID else 1
    return [r for r in get_db().execute(
        "SELECT * FROM submissions WHERE question_id = ?", (qid,))
        if not r["flags"] and (r["qversion"] or 1) == version]


def group_by_chat(rows):
    by_chat = defaultdict(list)
    for r in rows:
        by_chat[r["chat"]].append(r)
    return by_chat


def chats_scores(rows):
    """Aguja de cada chat por separado (nunca se mezclan respuestas de chats distintos)."""
    by_chat = group_by_chat(rows)
    return {k: dict(key=k, name=n, score=lean_score(by_chat.get(k, [])), total=len(by_chat.get(k, [])))
            for k, n, _ in CHATS}


def overall_score(scores):
    """«Todos los chats»: media de las agujas de cada chat, cada chat pesa lo mismo."""
    ok = [s["score"] for s in scores.values() if s["score"]["ok"]]
    if not ok:
        best = max((s["score"]["n"] for s in scores.values()), default=0)
        return {"ok": False, "n": best, "missing": max(MIN_METRO - best, 0), "chats": 0}
    return {"ok": True, "pos": round(sum(x["pos"] for x in ok) / len(ok), 1),
            "n": sum(x["n"] for x in ok), "chats": len(ok)}


def side_fields(q):
    isr = [f["id"] for f in all_fields(q) if f.get("side") == "israeli"]
    pal = [f["id"] for f in all_fields(q) if f.get("side") == "palestinian"]
    return isr, pal


def argument_point(q, rows):
    """Posición en el mapa de dos ejes a partir de las casillas observables:
    x = 0 (solo menciona argumentos del lado israelí) … 50 (los mismos de cada lado) … 100 (solo del palestino);
    y = 0-100, cuántos de los argumentos de ambos lados menciona (completitud)."""
    isr, pal = side_fields(q)
    xs, ys = [], []
    for r in rows:
        f = json.loads(r["fields"])
        if not any(f.get(k) for k in isr + pal):
            continue  # no rellenó las casillas opcionales
        a = sum(f.get(k) == "yes" for k in isr)
        b = sum(f.get(k) == "yes" for k in pal)
        xs.append(50 + 50 * (b - a) / (a + b) if a + b else 50)
        ys.append(100 * (a + b) / (len(isr) + len(pal)))
    n = len(xs)
    if n < MIN_METRO:
        return {"ok": False, "n": n, "missing": MIN_METRO - n}
    return {"ok": True, "n": n, "x": round(sum(xs) / n, 1), "y": round(sum(ys) / n, 1)}


# ------------------------------------------------------------------ routes

@app.route("/")
def landing():
    g.lang = "en"  # la portada principal es en inglés; el menú permite cambiar de idioma
    return index()


@app.route("/<lang>/")
def index():
    q = QUESTIONS[0]
    src = request.args.get("from", "")
    if src in SHARE_NETS:
        bump("visit_from", src)
    rows = valid_rows(q["id"])
    scores = chats_scores(rows)
    # Tablero de dos relojes. Las agujas solo se ven después de participar (para no anclar
    # la opinión); antes solo van los contadores: ni siquiera se envían las posiciones.
    unlocked = bool(session.get("done", {}).get(q["id"]))
    tested = session.get("done", {}).get(q["id"]) or []
    if ADMIN_TOKEN and request.args.get("token") == ADMIN_TOKEN:
        session["admin"] = True
    elif request.args.get("token") == "salir":
        session.pop("admin", None)
    admin = bool(ADMIN_TOKEN) and session.get("admin", False)
    return render_template("index.html", questions=QUESTIONS, q=q, counts=count_by_question(),
                           dash=dashboard_data(rows, unlocked or PREVIEW_NEEDLES, tested, admin), unlocked=unlocked,
                           admin=admin,
                           preview=PREVIEW_NEEDLES and not unlocked,
                           share_url=public_home_url(), total_valid=len(rows), min_metro=MIN_METRO)


def dashboard_data(rows, show, tested, admin=False):
    """Reloj izquierdo: cada chat por separado. Reloj derecho: ese chat por idioma o por país.
    pos: 0 = postura israelí, 50 = ni un lado ni otro, 100 = postura palestina."""
    def gauge(rs):
        sc = lean_score(rs)
        out = {"n": sc["n"], "pos": sc["pos"] if (show and sc["ok"]) else None,
               "missing": sc.get("missing", 0)}
        if admin:
            out["apos"], out["an"] = claims_pos(rs)
        return out
    by_chat = group_by_chat(rows)
    chats = []
    for key, name, _ in CHATS:
        if key == "otro":
            continue
        rs = by_chat.get(key, [])
        langs = [dict(code=c, label=LANGS[c], **gauge([r for r in rs if row_lang(r) == c])) for c in LANGS]
        per_country = Counter(r["country"] for r in rs if r["country"] and len(r["country"]) == 2)
        countries = [dict(code=c, label=c, **gauge([r for r in rs if r["country"] == c]))
                     for c, _ in per_country.most_common(8)]
        chats.append(dict(key=key, name=name, langs=langs, countries=countries, **gauge(rs)))
    first = next((c["key"] for c in chats if c["key"] in tested), None) \
        or max(chats, key=lambda c: c["n"])["key"]
    return {"chats": chats, "first": first}


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
        sources_text = form.get("sources_text", "").strip()[:6000]  # fuentes que el chat mostró aparte (opcional)
        if share_url and not valid_share_url(share_url):
            errors.append(T["err_share"][lang])

        # basta con el enlace a la conversación o con el texto de la respuesta
        answers = []
        for i, _step in enumerate(q["steps"], start=1):
            text = form.get(f"answer{i}", "").strip()
            if len(text) > MAX_ANSWER:
                errors.append(T["err_long"][lang])
            answers.append(text)
        if any(len(a) < 2 for a in answers):  # el texto es obligatorio; el enlace, opcional
            errors.append(T["err_answer"][lang])

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
        stance = form.get("stance", "")
        stance = stance if stance in STANCE_KEYS else None

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
            cur = db.execute(
                """INSERT INTO submissions (question_id, lang, country, chat, model,
                   answers, fields, lean, ip_hash, created_at,
                   share_url, flags, answers_hash, checked, stance, order_flip, qversion, sources, sources_text, alang)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?, ?)""",
                (qid, lang, detect_country(), chat, form.get("model", "").strip()[:80],
                 json.dumps(answers, ensure_ascii=False),
                 json.dumps(values, ensure_ascii=False), lean, ip_hash(),
                 datetime.now(timezone.utc).isoformat(),
                 share_url or None, ",".join(flags), answers_hash,
                 stance, int(bool(session.get("flip"))), q.get("version", 1),
                 ",".join(source_domains(" ".join(answers), sources_text)), sources_text or None,
                 answer_lang(" ".join(answers), lang)))
            db.commit()
            done = session.get("done", {})
            done[qid] = sorted(set(done.get(qid, [])) | {chat})
            session["done"] = done
            mine = session.get("mine", {})
            mine.setdefault(qid, {})[chat] = lean  # para «Tus chats»: lo que dijo esta persona
            session["mine"] = mine
            subs = session.get("subs", {})  # para «Tu respuesta, en datos»: qué envío es de esta persona
            subs.setdefault(qid, {})[chat] = cur.lastrowid
            session["subs"] = subs
            session["just_sent"] = qid
            return redirect(url_for("next_chat", qid=qid, chat=chat))

        for e in errors:
            flash(e, "error")

    copied_to = None
    if request.method == "GET" and request.args.get("chat") in CHAT_NAMES:
        form = {"chat": request.args["chat"]}
        if request.args.get("copied"):  # viene de «Probar otro chat»: la pregunta ya se copió
            copied_to = CHAT_NAMES[request.args["chat"]]
    # orden de las dos posturas al azar por visitante (fijo durante su visita), para que
    # el orden no influya; «equilibrada» y «no estoy seguro» siempre al final
    if "flip" not in session:
        session["flip"] = random.random() < 0.5
    sides = ["pro_palestine", "pro_israel"] if session["flip"] else ["pro_israel", "pro_palestine"]
    stance_order = (["pal_clear", "pal_lean", "neither", "isr_lean", "isr_clear"] if session["flip"]
                    else ["isr_clear", "isr_lean", "neither", "pal_lean", "pal_clear"]) + ["skip"]
    return render_template("question.html", q=q, chats=CHATS, form=form,
                           lean_order=sides + ["balanced", "unsure"], stance_order=stance_order,
                           field_options=field_options, copied_to=copied_to,
                           count=count_by_question().get(qid, 0))


@app.route("/<lang>/q/<qid>/next")
def next_chat(qid):
    """Tras enviar: invitar a probar la misma pregunta en otro chat antes de ver resultados."""
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    done = session.get("done", {}).get(qid, [])
    last = request.args.get("chat", "")
    others = [(k, n, l) for k, n, l in CHATS if l and k not in done and k != last]
    return render_template("next.html", q=q, others=others, prompt=q["steps"][0]["prompt"],
                           done=[CHAT_NAMES[c] for c in done if c in CHAT_NAMES],
                           last=CHAT_NAMES.get(last, ""))


@app.route("/<lang>/q/<qid>/mine")
def mine(qid):
    """«Tus chats»: lo que dijo esta persona de cada chat que probó, frente a la media de ese chat,
    y la comparación de todos los chats (aguja y mapa de dos ejes)."""
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    lang = g.lang
    done = session.get("done", {}).get(qid, [])
    if not done:
        flash(T["results_locked"][lang])
        return redirect(url_for("question", qid=qid))
    my = session.get("mine", {}).get(qid, {})
    rows = valid_rows(qid)
    scores = chats_scores(rows)
    by_chat = group_by_chat(rows)
    cards = [dict(key=c, name=CHAT_NAMES[c], said=my.get(c), everyone=scores[c]["score"],
                  total=scores[c]["total"]) for c in done if c in CHAT_NAMES]
    untested = [(k, n, l) for k, n, l in CHATS if l and k not in done]
    compare = sorted(scores.values(), key=lambda s: (not s["score"]["ok"], -s["total"]))
    points = [dict(key=k, name=n, mine=k in done, point=argument_point(q, by_chat.get(k, [])))
              for k, n, _ in CHATS]
    names = [CHAT_NAMES[c] for c in done if c in CHAT_NAMES]
    share_text = T["mine_share_msg"][lang].format(chats=" & ".join(names))
    in_data = answer_data(q, session.get("subs", {}).get(qid, {}))
    return render_template("mine.html", q=q, cards=cards, untested=untested, compare=compare,
                           points=points, overall=overall_score(scores), min_metro=MIN_METRO,
                           share_text=share_text, share_url=public_home_url(),
                           just_sent=session.pop("just_sent", None) == qid, in_data=in_data,
                           origin_groups=ORIGIN_GROUPS, subscribed=request.args.get("sub") == "1")


def answer_data(q, subs):
    """«Tu respuesta, en datos»: solo cosas contables de cada respuesta de esta persona.
    Fuentes por origen (las que llegaron al texto pegado) y argumentos de cada lado según sus casillas."""
    sides = {s: [f["id"] for f in all_fields(q) if f.get("side") == s] for s in ("israeli", "palestinian", "neutral")}
    out = []
    for chat, sid in subs.items():
        r = get_db().execute("SELECT * FROM submissions WHERE id = ?", (sid,)).fetchone()
        if not r or chat not in CHAT_NAMES:
            continue
        doms = [d for d in (r["sources"] or "").split(",") if d]
        groups = {g: [d for d in doms if source_origin(d) == g] for g in ORIGIN_GROUPS}
        vals = json.loads(r["fields"] or "{}")
        args = {s: (sum(vals.get(f) == "yes" for f in ids), len(ids)) for s, ids in sides.items()}
        out.append(dict(chat=chat, name=CHAT_NAMES[chat], sources=doms, groups=groups, args=args,
                        marked=any(vals.get(f) in ("yes", "no") for ids in sides.values() for f in ids)))
    return out


@app.route("/<lang>/q/<qid>/sources")
def sources(qid):
    """Fuentes citadas en todas las respuestas válidas, agrupadas por origen, en total y chat por chat.
    Solo para quienes participaron (como los resultados)."""
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    is_admin = bool(ADMIN_TOKEN) and request.args.get("token") == ADMIN_TOKEN
    if not is_admin and not session.get("done", {}).get(qid):
        flash(T["results_locked"][g.lang])
        return redirect(url_for("question", qid=qid))
    rows = valid_rows(qid)

    def tally(rs):
        per_group = {grp: Counter() for grp in ORIGIN_GROUPS}
        with_src = 0
        for r in rs:
            doms = [d for d in (r["sources"] or "").split(",") if d]
            with_src += bool(doms)
            for d in doms:
                per_group[source_origin(d)][d] += 1
        return dict(n=len(rs), with_src=with_src,
                    groups={grp: dict(total=sum(c.values()), top=c.most_common(12)) for grp, c in per_group.items()})

    by_chat = group_by_chat(rows)
    chats = [dict(key=k, name=n, **tally(by_chat.get(k, []))) for k, n, _ in CHATS if by_chat.get(k)]
    return render_template("sources.html", q=q, overall=tally(rows), chats=chats, origin_groups=ORIGIN_GROUPS)


@app.route("/<lang>/share/<net>", methods=["POST"])
def share_click(net):
    if net in SHARE_NETS:
        bump("share_click", net)
    return ("", 204)


@app.route("/admin/stats")
def admin_stats():
    if not ADMIN_TOKEN or request.args.get("token") != ADMIN_TOKEN:
        abort(403)
    rows = get_db().execute(
        "SELECT kind, name, SUM(n) AS n FROM counters GROUP BY kind, name ORDER BY kind, n DESC").fetchall()
    stances = get_db().execute(
        "SELECT COALESCE(stance, '—') AS stance, lean, COUNT(*) AS n FROM submissions "
        "WHERE flags = '' OR flags IS NULL GROUP BY stance, lean ORDER BY stance").fetchall()
    g.lang = "es"
    return render_template("admin_stats.html", rows=rows, stances=stances, token=ADMIN_TOKEN)


@app.route("/<lang>/q/<qid>/results")
def results(qid):
    q = QUESTIONS_BY_ID.get(qid) or abort(404)
    lang = g.lang
    is_admin = bool(ADMIN_TOKEN) and request.args.get("token") == ADMIN_TOKEN
    # los resultados solo se ven después de participar, para no influir en las respuestas
    if not is_admin and not session.get("done", {}).get(qid):
        flash(T["results_locked"][lang])
        return redirect(url_for("question", qid=qid))
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
            if (not f_lang or row_lang(r) == f_lang)
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
        by_lang[row_lang(r)].append(r)
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
        "model": r["model"], "lang": LANGS.get(row_lang(r), row_lang(r)),
        "country": r["country"], "answers": json.loads(r["answers"]),
        "lean": T["lean"].get(r["lean"], {}).get(lang, ""),
        "share_url": r["share_url"], "checked": r["checked"], "flags": r["flags"],
        "tags": [labels[f][v] for f, v in parsed[r["id"]].items()
                 if f in choice_fields and v in labels[f]],
        "date": r["created_at"][:10],
        "claims": claims_detail(r, lang) if admin else None,
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


def claims_detail(r, lang):
    found = claims_in(" ".join(json.loads(r["answers"] or "[]")))
    text = {c["id"]: c["text"].get(lang) or c["text"]["en"] for c in CLAIMS}
    groups = {sd: [text[i] for i, s2 in found if s2 == sd] for sd in ("israeli", "palestinian", "balanced")}
    n = len(found)
    score = (len(groups["palestinian"]) - len(groups["israeli"])) / n if n else None
    return {"groups": groups, "n": n, "pos": round(50 + 50 * score) if n else None}


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
    return render_template("method.html", question=QUESTIONS[0]["steps"][0]["prompt"])


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


def site_root():
    """PUBLIC_URL si la visita llega por ese dominio; si no, la dirección por la que llegó
    (así los enlaces para compartir funcionan en biaschecker.pythonanywhere.com antes de conectar el dominio)."""
    host = urlparse(PUBLIC_URL).netloc
    if not host or request.host in (host, host.removeprefix("www.")) or "www." + request.host == host:
        return PUBLIC_URL or request.url_root.rstrip("/")
    return "https://" + request.host


def public_home_url():
    root = site_root()
    return f"{root}/" if g.lang == "en" else f"{root}/{g.lang}/"


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
        return redirect(url_for("mine", qid=qid))
    if not request.form.get("consent") or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        flash(T["email_err"][lang], "error")
        session["just_sent"] = qid  # vuelve a mostrar el panel
        return redirect(url_for("mine", qid=qid) + "#thanks")
    db = get_db()
    # solo la fecha, sin hora: así no se puede cruzar con el momento de un envío
    insta = request.form.get("instagram", "").strip().lstrip("@")[:40]
    insta = insta if re.fullmatch(r"[A-Za-z0-9._]{1,30}", insta or "") and request.form.get("insta_ok") else None
    db.execute("INSERT INTO subscribers (email, lang, consent_date, instagram) VALUES (?, ?, ?, ?) "
               "ON CONFLICT(email) DO UPDATE SET instagram = COALESCE(excluded.instagram, subscribers.instagram)",
               (email, lang, datetime.now(timezone.utc).date().isoformat(), insta))
    db.commit()
    push_to_brevo(email, lang)
    return redirect(url_for("mine", qid=qid, sub=1) + "#thanks")


@app.route("/admin/subscribers.csv")
def admin_subscribers():
    if not ADMIN_TOKEN or request.args.get("token") != ADMIN_TOKEN:
        abort(403)
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["email", "lang", "consent_date", "instagram"])
    for r in get_db().execute(
            "SELECT email, lang, consent_date, instagram FROM subscribers ORDER BY consent_date"):
        writer.writerow(list(r))
    return Response("\ufeff" + out.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=subscribers.csv"})


@app.route("/export.csv")
def export_csv():
    if not ADMIN_TOKEN or request.args.get("token") != ADMIN_TOKEN:
        abort(403)  # solo para ti: /export.csv?token=ADMIN_TOKEN
    out = io.StringIO()
    writer = csv.writer(out)
    field_ids = [f["id"] for q in QUESTIONS for f in all_fields(q)]
    n_steps = max(len(q["steps"]) for q in QUESTIONS)
    writer.writerow(["id", "question", "page_lang", "answer_lang", "country", "chat", "model",
                     *[f"answer{i}" for i in range(1, n_steps + 1)], *field_ids, "lean", "stance", "order_flip", "share_url",
                     "checked", "flags", "created_at", "question_version", "sources", "sources_text"])
    for r in get_db().execute("SELECT * FROM submissions ORDER BY id"):
        answers = (json.loads(r["answers"]) + [""] * n_steps)[:n_steps]
        fields = json.loads(r["fields"])
        writer.writerow([r["id"], r["question_id"], r["lang"], row_lang(r), r["country"],
                         r["chat"], r["model"], *answers,
                         *[fields.get(f, "") for f in field_ids],
                         r["lean"], r["stance"] or "", r["order_flip"], r["share_url"] or "", r["checked"],
                         r["flags"] or "", r["created_at"], r["qversion"] or 1, r["sources"] or "", r["sources_text"] or ""])
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
