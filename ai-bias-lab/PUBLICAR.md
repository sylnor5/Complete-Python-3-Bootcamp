# Publicar ChatRadar en thechatradar.com

Guía paso a paso con PythonAnywhere (servidor) y GoDaddy (dominio).
Donde pone `USUARIO`, escribe tu nombre de usuario de PythonAnywhere.

---

## 1. Crear la cuenta en PythonAnywhere

1. Entra en https://www.pythonanywhere.com y crea una cuenta.
   El nombre de usuario aparece en las rutas, así que elige uno corto (por ejemplo `chatradar`).
2. Puedes empezar con la cuenta gratuita para probar: la web funcionará en `USUARIO.pythonanywhere.com`.
3. Para usar **thechatradar.com** necesitas un plan de pago (el más barato basta). Puedes subir de plan
   en cualquier momento desde **Account**, sin perder nada.

## 2. Descargar la web en el servidor

En PythonAnywhere abre **Consoles → Bash** y pega estos comandos, uno por uno:

```bash
git clone -b claude/stoic-thompson-i6esto https://github.com/sylnor5/Complete-Python-3-Bootcamp.git
cd Complete-Python-3-Bootcamp/ai-bias-lab
mkvirtualenv chatradar --python=python3.11
pip install -r requirements.txt
mkdir -p ~/chatradar-data
```

Si `python3.11` da error, prueba con `python3.10` o `python3.12`.
Si GitHub te pide usuario y contraseña, el repositorio es privado: hazlo público o pide ayuda para usar un token.

Ahora genera dos claves secretas (ejecuta la línea dos veces y **guarda los dos resultados**):

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

- La primera será tu `SECRET_KEY`.
- La segunda será tu `ADMIN_TOKEN`: la clave para entrar a moderar. No la compartas con nadie.

## 3. Detectar el país (base de datos gratuita)

En la misma consola:

```bash
cd ~/Complete-Python-3-Bootcamp/ai-bias-lab
wget -O geoip.mmdb.gz "https://download.db-ip.com/free/dbip-country-lite-$(date +%Y-%m).mmdb.gz"
gunzip -f geoip.mmdb.gz
ls -lh geoip.mmdb
```

Si el último comando muestra un archivo de varios MB, está bien. Repítelo una vez al mes para actualizarlo.
(Si el `wget` falla, descárgalo desde https://db-ip.com/db/download/ip-to-country-lite en formato MMDB y
súbelo con la pestaña **Files** a esa carpeta con el nombre `geoip.mmdb`.)

## 4. Crear la web

1. Ve a la pestaña **Web → Add a new web app**.
2. Dominio:
   - con cuenta gratuita: acepta `USUARIO.pythonanywhere.com`;
   - con cuenta de pago: escribe `www.thechatradar.com`.
3. Elige **Manual configuration** (no "Flask") y la misma versión de Python del paso 2.
4. En la página de la web, rellena:
   - **Source code:** `/home/USUARIO/Complete-Python-3-Bootcamp/ai-bias-lab`
   - **Virtualenv:** `/home/USUARIO/.virtualenvs/chatradar`
5. En **Static files** añade una línea:
   - URL: `/static/`
   - Directory: `/home/USUARIO/Complete-Python-3-Bootcamp/ai-bias-lab/static`
6. Activa **Force HTTPS**.
7. Haz clic en el enlace del **WSGI configuration file**, borra todo su contenido y pega esto
   (cambiando `USUARIO` y las dos claves):

```python
import os
import sys

path = "/home/USUARIO/Complete-Python-3-Bootcamp/ai-bias-lab"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ["SECRET_KEY"] = "PEGA_AQUI_LA_PRIMERA_CLAVE"
os.environ["ADMIN_TOKEN"] = "PEGA_AQUI_LA_SEGUNDA_CLAVE"
os.environ["DATABASE"] = "/home/USUARIO/chatradar-data/data.db"
os.environ["PUBLIC_URL"] = "https://www.thechatradar.com"

from app import app as application
```

8. Guarda y pulsa el botón verde **Reload**.
9. Abre la dirección de tu web. Deberías ver la pantalla de elegir idioma.

Si algo falla, mira el **Error log** en la pestaña Web y envíame las últimas líneas.

## 5. Conectar thechatradar.com (cuenta de pago)

1. En PythonAnywhere, pestaña **Web**, aparece un valor **CNAME** parecido a `webapp-123456.pythonanywhere.com`. Cópialo.
2. En GoDaddy: **My Products → thechatradar.com → DNS**.
   - Si existe un registro `CNAME` con nombre `www`, edítalo; si no, añade uno:
     - Type: `CNAME` · Name: `www` · Value: el valor copiado · TTL: 1 hora.
   - Si hay un registro `A` con nombre `@` que apunte a un "parking" de GoDaddy, no pasa nada; lo resolvemos con el reenvío.
3. En GoDaddy, en la misma página del dominio, busca **Forwarding** (reenvío) y reenvía
   `thechatradar.com` a `https://www.thechatradar.com`, tipo **Permanent (301)**.
   Así funciona tanto con «www» como sin él.
4. Espera entre 15 minutos y unas horas a que se propague.
5. Vuelve a PythonAnywhere, pestaña **Web**, sección **HTTPS certificate**: elige
   **Auto-renewing Let's Encrypt certificate**. Pulsa **Reload**.

## 6. Comprobar que todo funciona

- `https://www.thechatradar.com` → elegir idioma.
- Haz una prueba completa tú misma (con respuestas reales y el enlace de compartir).
- Resultados de moderación: `https://www.thechatradar.com/es/q/gaza/results?token=TU_ADMIN_TOKEN`
- Propuestas de temas: `https://www.thechatradar.com/admin/proposals?token=TU_ADMIN_TOKEN`
- Emails apuntados: `https://www.thechatradar.com/admin/subscribers.csv?token=TU_ADMIN_TOKEN`

## 7. Actualizar la web cuando haya cambios

En la consola Bash de PythonAnywhere:

```bash
cd ~/Complete-Python-3-Bootcamp
git pull
workon chatradar
pip install -r ai-bias-lab/requirements.txt
```

Y luego **Reload** en la pestaña Web. Los datos (`~/chatradar-data/data.db`) no se tocan.

## 8. Copias de seguridad

Una vez por semana descarga `https://www.thechatradar.com/export.csv` (todas las respuestas) y la lista de
emails. O descarga directamente el archivo `chatradar-data/data.db` desde la pestaña **Files**.

## Más adelante (opcional)

- **Cloudflare** (gratis): protección contra ataques y picos de tráfico, y país detectado sin archivo GeoIP.
  Implica cambiar los "nameservers" de GoDaddy a Cloudflare. Lo hacemos cuando la web ya funcione.
- **Brevo** (emails de novedades): crea la cuenta y una lista, y añade al archivo WSGI
  `os.environ["BREVO_API_KEY"] = "..."` y `os.environ["BREVO_LIST_ID"] = "..."`.
- **Correo hola@thechatradar.com** gratis que llegue a tu Gmail: Cloudflare Email Routing.
