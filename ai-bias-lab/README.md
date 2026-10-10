# ChatRadar — thechatradar.com

Experimento ciudadano: cada persona hace **las mismas preguntas** en su chat de IA preferido
(ChatGPT, Gemini, Claude, Copilot, Grok, Meta AI, DeepSeek, Le Chat, Perplexity…), pega las respuestas y las
clasifica. La web compara los resultados **por chat, por idioma y por país** para ver si hay sesgos sistemáticos.

La primera prueba es la pregunta sobre Gaza que originó el proyecto (una sola pregunta, igual para todos), en español, inglés, francés y hebreo (la web se muestra de derecha a izquierda en hebreo).

## Recorrido

1. `/` — la persona elige idioma (español, English, français, עברית).
2. `/<idioma>/` — portada con la historia del proyecto y cómo participar.
3. `/<idioma>/q/gaza` — copia la pregunta en un chat nuevo, pega la respuesta, marca qué dijo el chat y si
   cree que se inclina hacia un lado.
4. `/<idioma>/q/gaza/results` — resultados con filtros por idioma y país:
   - percepción de inclinación por chat, por idioma y por país;
   - una tabla por cada casilla (conclusión, argumentos mencionados u omitidos) comparando chats;
   - las últimas respuestas completas.
5. `/export.csv?token=ADMIN_TOKEN` — todos los datos (solo para ti), una columna por casilla, para analizarlos en Excel o Python.

## Metrónomo, email y compartir

- **Metrónomo** (arriba de los resultados): una barra por chat que va de «hacia la postura israelí» a
  «hacia la postura palestina», con «equilibrado» en el centro. La posición sale de lo que marcaron quienes
  participaron (-1, 0, +1; «no estoy seguro» no cuenta). Punto lleno = todas las respuestas; círculo vacío =
  solo las que tienen enlace. Un chat no aparece hasta tener `MIN_METRO` respuestas (ahora 1 para las pruebas internas; volver a 20 antes del lanzamiento).
  Respeta los filtros de idioma, país y tipo de respuesta.
- **Tras enviar**, la persona llega al metrónomo con un panel de agradecimiento que ofrece:
  - **email opcional** con casilla de consentimiento. Se guarda en otra tabla (`subscribers`), sin ningún
    vínculo con las respuestas y solo con la fecha (sin hora), para que no se pueda cruzar con un envío.
    Exporta la lista en `/admin/subscribers.csv?token=ADMIN_TOKEN`. Si defines `BREVO_API_KEY` y
    `BREVO_LIST_ID`, cada alta se envía además a esa lista de Brevo (activa allí la doble confirmación y
    usa Brevo para mandar los correos y gestionar las bajas);
  - **botones para compartir** (WhatsApp, X, Facebook, LinkedIn, Telegram, copiar enlace) con un mensaje
    en el idioma de la persona y el enlace a `PUBLIC_URL` (por defecto `https://thechatradar.com`).

## Propuestas de temas nuevos

`/<idioma>/propose` deja que cualquiera proponga un tema y la pregunta exacta en la que cree que las IAs
tienen sesgo, con el motivo. No pide datos personales. Las propuestas **no se publican**: las revisas en
`/admin/proposals?token=ADMIN_TOKEN` (con descarga en CSV y botón de borrar). Para lanzar una prueba
nueva a partir de una propuesta, añádela a `questions.json` con sus traducciones y casillas.

## Protección contra respuestas falsas

- **Enlace para compartir (opcional, muy recomendado).** La persona pega el enlace «Compartir» de su chat
  (ChatGPT, Claude, Gemini, Copilot, Grok, Meta AI, DeepSeek, Le Chat, Perplexity). Solo se aceptan
  enlaces `https://` de esos dominios. En resultados se puede filtrar «solo con enlace».
- **Descarte automático.** No cuentan en los resultados los envíos con alguna respuesta de menos de 150
  caracteres, sin ninguna palabra clave del tema (lista `keywords` en `questions.json`, en los 4 idiomas),
  con la misma respuesta repetida en varias preguntas (si una prueba tiene más de una) o idénticos a un envío anterior. A quien envía no se le avisa,
  para no enseñar cómo saltarse el filtro.
- **Comprobación a mano.** Con `?token=ADMIN_TOKEN` en la página de resultados ves también los descartados
  y puedes marcar cualquier respuesta como «comprobada» (tras abrir su enlace) o borrarla. Hay un filtro
  «solo comprobadas a mano».
- El CSV incluye `share_url`, `checked` y `flags` para analizar con o sin los dudosos.

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
| `PUBLIC_URL`   | Dirección pública para compartir (por defecto thechatradar.com). |
| `MIN_METRO`    | Respuestas mínimas por chat para mostrar su burbuja (ahora 1; volver a 20 antes del lanzamiento). |
| `BREVO_API_KEY`, `BREVO_LIST_ID` | Opcional: enviar los emails a una lista de Brevo. |

En hostings con disco efímero (p. ej. el plan gratuito de Render) SQLite se borra al reiniciar.
Usa un disco persistente o PythonAnywhere, que guarda los ficheros.
