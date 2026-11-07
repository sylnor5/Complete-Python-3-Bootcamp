# Bitácora 2: avance y quién actúa ahora

Actualizar al cerrar cada tarea. «Quién» = fundadora, coordinador (Claude) o un agente del equipo
(ver EQUIPO.md).

## Ahora
| Tarea | Quién | Estado |
|---|---|---|
| Mandar el mensaje de WhatsApp a los testers (con el enlace https://thechatradar.com) | fundadora | listo para enviar (dominio en vivo desde el 7-11) |
| Revisar la planilla de línea editorial (borradores/fuentes-postura-revision.csv) | fundadora | pendiente |
| Conectar la línea editorial a la web (datos y página de fuentes) | coordinador | después de la revisión |
| Aprobar la lista de 15 reglas de ChatRadar (ver abajo) y escribir las pruebas automáticas (REGLAS.md + /goal con tope) | fundadora, luego coordinador | lista propuesta |
| Plantilla y reglas generales para proyectos nuevos | sesión «Claude experto» (rama claude/plantilla-proyecto) | en curso |

## Próximo
| Tarea | Quién | Estado |
|---|---|---|
| Decidir si se suaviza la historia de la portada (quitar «de un solo lado» y la cita) o se muestra después de participar (propuesta del psicólogo) | fundadora | sin prisa |
| Revisión de la lista de afirmaciones desde el lado palestino | verificador + revisor humano | pendiente |
| Revisar los disparadores en hebreo de la lista y los textos nuevos | hablante nativo | pendiente |
| Revisar source_origins.json desde los dos lados | verificador | pendiente |
| Al salir en vivo: abrir la sesión «ChatRadar Redes» con el agente chatradar-redes (Instagram primero; propone y la fundadora aprueba; sin respuestas automáticas) | fundadora + coordinador | el día del lanzamiento |
| Página de diagnóstico para probar en teléfonos reales | coordinador + QA | planificado |
| Instrucciones para copiar fuentes en otros chats (además de Gemini) | coordinador | tras feedback de testers |

## Hecho
- 7-11-2026: thechatradar.com en vivo (plan Developer, CNAME, reenvío 301, Let's Encrypt, Force HTTPS). Los datos se conservaron.
- 7-11-2026: frase nueva en la portada (porqué sin anclar), en los 4 idiomas. Mensaje de WhatsApp en hebreo revisado por el psicólogo.
- 7-11-2026: marca TheChatRadar en la web (logo, títulos, textos, imagen para compartir). Mensaje corto para testers en es/en/he en borradores/mensajes-testers.md.
- 7-11-2026: recorrido de la prueba en /admin/stats (6 pasos, errores al enviar, periodos hoy/semana/mes/todo). Anónimo; cuenta desde el 7-11.

## Fechas
- 27-11-2026, 14:00 (Israel): preguntar si se dejan de contar las respuestas a la versión 1 de la pregunta.

## Más adelante
- Donaciones (Open Collective o Ko-fi), después del lanzamiento, con cuentas públicas.
- Jueces de IA de varias empresas, si se decide.
- Manifiesto (borradores/manifiesto.md), Cloudflare, Brevo.

## Lista propuesta de reglas de ChatRadar (pendiente de aprobación)
1. Todo texto visible existe en es/en/fr/he y no está vacío.
2. La pregunta existe en los 4 idiomas y usa «afirma / claims / affirme / טוען».
3. Todas las páginas abren sin error en los 4 idiomas.
4. Sin errores de JavaScript en móvil (390 px) y computadora.
5. Nada se sale del ancho en el móvil.
6. Lado israelí a la izquierda en es/en/fr; en hebreo invertido.
7. Ningún texto para compartir incluye el veredicto o la postura del participante.
8. Sin amarillo/ámbar.
9. Al tocar «Probar en otro chat», el portapapeles tiene la pregunta.
10. Una respuesta con enlace no reconocido se guarda igual.
11. El idioma de la respuesta se detecta bien en los 4 idiomas.
12. El reloj derecho nunca queda vacío si ese chat tiene respuestas.
13. La lista de afirmaciones encuentra lo esperado en las 4 respuestas de prueba.
14. Las sospechosas no cuentan; las negativas se cuentan aparte.
15. Ninguna fuente queda sin grupo de origen.
16. Textos de la web cumplen «textos que suenen humanos» de REGLAS-GENERALES.md.
