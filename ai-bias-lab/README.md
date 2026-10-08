# AI Bias Lab

Experimento ciudadano: cada persona hace **las mismas preguntas** en su chat de IA preferido
(ChatGPT, Gemini, Claude, Copilot, Grok, Meta AI, DeepSeek, Le Chat, Perplexity…), pega las respuestas y las
clasifica. La web compara los resultados **por chat, por idioma y por país** para ver si hay sesgos sistemáticos.

La primera prueba son las dos preguntas sobre Gaza que originaron el proyecto, en español, inglés, francés y hebreo (la web se muestra de derecha a izquierda en hebreo).

## Recorrido

1. `/` — la persona elige idioma (español, English, français, עברית).
2. `/<idioma>/` — portada con la historia del proyecto y cómo participar.
3. `/<idioma>/q/gaza` — copia la pregunta 1 en un chat nuevo, pega la respuesta; hace la pregunta 2 en el
   mismo chat y pega la respuesta; marca qué dijo el chat y si cree que se inclina hacia un lado.
4. `/<idioma>/q/gaza/results` — resultados con filtros por idioma y país:
   - percepción de inclinación por chat, por idioma y por país;
   - una tabla por cada casilla (conclusión, argumentos mencionados u omitidos) comparando chats;
   - las últimas respuestas completas.
5. `/export.csv` — todos los datos, una columna por casilla, para analizarlos en Excel o Python.

## País de cada participante

La web guarda el **país aproximado** de la conexión, nunca la IP. Lo obtiene así, por orden:

1. Cabeceras que añaden algunos proxies: `CF-IPCountry` (Cloudflare), `X-Vercel-IP-Country`, etc.
   Si pones la web detrás de Cloudflare (gratis), funciona sin hacer nada más.
2. Si no hay cabecera, una base de datos GeoIP local. Descarga el fichero gratuito
   **IP to Country Lite** de DB-IP en formato `.mmdb` (https://db-ip.com/db/download/ip-to-country-lite),
   guárdalo como `geoip.mmdb` en esta carpeta (o indica su ruta con `GEOIP_DB`) y actualízalo cada mes.
   Su licencia (CC BY 4.0) pide citar a DB-IP: añade «IP geolocation by DB-IP» en el pie si lo usas.
3. Si no hay ninguna de las dos, el país queda como «Desconocido».

La página «Cómo funciona» lo explica a las personas participantes. En la UE esto es obligatorio.

## Cambiar o añadir preguntas

Edita `questions.json`. Cada prueba tiene textos en `es`, `en`, `fr` y `he` y una lista de `steps` (preguntas que
se hacen en el mismo chat, una tras otra). Cada paso tiene `fields`, las casillas para clasificar la respuesta:

- con `"type": "yesno"` → casilla Sí / No;
- con `"options"` → una opción entre varias.

No cambies los `id` de campos u opciones que ya tienen respuestas: rompería la comparación. Para cambios
grandes, crea una prueba nueva con otro `id`. Los textos de la interfaz están en `i18n.py`.

## Ejecutar en local

```bash
cd ai-bias-lab
pip install -r requirements.txt
python app.py            # http://127.0.0.1:5000
```

## Publicarla en internet

Cualquier hosting de Python sirve (PythonAnywhere, Render, Railway, Fly.io…). Comando de arranque:

```bash
gunicorn app:app
```

| Variable       | Para qué                                                    |
|----------------|-------------------------------------------------------------|
| `SECRET_KEY`   | Obligatoria en producción: una cadena larga y aleatoria.    |
| `DATABASE`     | Ruta del fichero SQLite (en un disco persistente).          |
| `ADMIN_TOKEN`  | Activa la moderación: abre `/es/q/gaza/results?token=…`.    |
| `GEOIP_DB`     | Ruta del fichero `.mmdb` (por defecto `geoip.mmdb`).        |
| `MAX_PER_HOUR` | Envíos máximos por conexión y hora (por defecto 10).        |

En hostings con disco efímero (p. ej. el plan gratuito de Render) SQLite se borra al reiniciar.
Usa un disco persistente o PythonAnywhere, que guarda los ficheros.
