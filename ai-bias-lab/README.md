# AI Bias Lab

Web para un experimento ciudadano: cada persona hace **la misma pregunta** en su chat de IA preferido
(ChatGPT, Claude, Gemini, Copilot, Meta AI, Grok, DeepSeek, Le Chat, Perplexity…), pega la respuesta y la
clasifica. La web agrega las respuestas por chat para ver si alguna IA muestra sesgos (de género, políticos,
de origen…).

## Qué incluye

- **Portada** con las preguntas disponibles y cuántas respuestas lleva cada una.
- **Página de pregunta**: botón para copiar el texto exacto, enlaces a cada chat y formulario
  (chat usado, modelo, país, respuesta completa, clasificación y si la persona percibe sesgo).
- **Resultados**: tablas comparando chats (porcentaje por opción, con la media de todos), percepción de sesgo
  y las últimas 50 respuestas.
- **Exportación** de todos los datos en `/export.csv`.
- Antispam básico: campo trampa para bots y máximo de envíos por hora por conexión (la IP se guarda cifrada, nunca en claro).
- Moderación: define `ADMIN_TOKEN` y abre `/q/<id>/resultados?token=TU_TOKEN` para ver botones de borrar.

## Cambiar o añadir preguntas

Edita `questions.json`. Cada pregunta tiene:

```json
{
  "id": "identificador-en-la-url",
  "title": "Título corto",
  "topic": "Género | Política | Origen | …",
  "prompt": "Texto exacto que la gente copiará en su chat",
  "why": "Explicación de qué patrón indicaría sesgo",
  "fields": [
    {"id": "campo", "label": "Pregunta para clasificar la respuesta", "options": ["A", "B", "C"]}
  ]
}
```

Los `fields` son la clave: convierten respuestas de texto libre en datos comparables entre chats.
No cambies las `options` de una pregunta que ya tiene respuestas; crea una pregunta nueva.

## Ejecutar en local

```bash
cd ai-bias-lab
pip install -r requirements.txt
python app.py            # http://127.0.0.1:5000
```

## Publicarla en internet

Cualquier hosting de Python sirve (Render, Railway, Fly.io, PythonAnywhere…). Comando de arranque:

```bash
gunicorn app:app
```

Variables de entorno:

| Variable       | Para qué                                                    |
|----------------|-------------------------------------------------------------|
| `SECRET_KEY`   | Obligatoria en producción: una cadena larga y aleatoria.    |
| `DATABASE`     | Ruta del fichero SQLite (ponlo en un disco persistente).    |
| `ADMIN_TOKEN`  | Activa la moderación (borrar respuestas).                   |
| `MAX_PER_HOUR` | Envíos máximos por conexión y hora (por defecto 10).        |

Ojo: en hostings con disco efímero (p. ej. el plan gratuito de Render) SQLite se borra al reiniciar.
Usa un disco persistente o PythonAnywhere, que guarda los ficheros.
