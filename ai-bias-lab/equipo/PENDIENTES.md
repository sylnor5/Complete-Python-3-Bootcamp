# Bitácora 2: avance y quién actúa ahora

Actualizar al cerrar cada tarea. «Quién» = fundadora, coordinador (Claude) o un agente del equipo
(ver EQUIPO.md).

## Ahora
| Tarea | Quién | Estado |
|---|---|---|
| Mandar el mensaje de WhatsApp a los testers | fundadora | listo para enviar |
| Revisar la planilla de línea editorial (borradores/fuentes-postura-revision.csv) | fundadora | pendiente |
| Conectar la línea editorial a la web (datos y página de fuentes) | coordinador | después de la revisión |
| Aprobar la lista de 15 reglas de ChatRadar (ver abajo) y escribir las pruebas automáticas (REGLAS.md + /goal con tope) | fundadora, luego coordinador | lista propuesta |
| Plantilla y reglas generales para proyectos nuevos | sesión «Claude experto» (rama claude/plantilla-proyecto) | en curso |

## Próximo
| Tarea | Quién | Estado |
|---|---|---|
| Revisión de la lista de afirmaciones desde el lado palestino | verificador + revisor humano | pendiente |
| Revisar los disparadores en hebreo de la lista y los textos nuevos | hablante nativo | pendiente |
| Revisar source_origins.json desde los dos lados | verificador | pendiente |
| Pasar al plan de pago y conectar thechatradar.com | fundadora + coordinador | cuando ella decida |
| Página de diagnóstico para probar en teléfonos reales | coordinador + QA | planificado |
| Instrucciones para copiar fuentes en otros chats (además de Gemini) | coordinador | tras feedback de testers |

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
