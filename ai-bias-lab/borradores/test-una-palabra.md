# Idea: ¿cambia la respuesta por una sola palabra? (borrador, pendiente de diseñar)

> Idea del 17 de octubre de 2026. Surgió al cambiar «Hamás dice» por «Hamás afirma» en la pregunta (en inglés «says» por «claims», en hebreo «אומר» por «טוען»).

## Qué mide

Si una sola palabra de la pregunta cambia la respuesta del chat. Es un **efecto de encuadre**:
- «dice» presenta la cifra como un dato;
- «afirma» o «claims» sugiere que hay que dudar de ella.

Si cambia, demuestra lo frágil que es la «neutralidad» de estos chats.

## Cómo podría funcionar

1. Dos versiones de la pregunta, idénticas salvo por esa palabra: «dice» y «afirma».
2. La web sortea qué versión recibe cada participante. Lo decide el sorteo, no la persona.
3. Se compara, chat por chat:
   - la conclusión;
   - la inclinación;
   - la casilla «¿Dice que la cifra viene de Hamás o duda de ella?» (q1_source).

## Cuidados

- Las dos versiones deben ser equivalentes en los cuatro idiomas.
- No mezclar los resultados con la prueba principal: cada respuesta guarda su versión de la pregunta (`qversion`).
- Hacen falta bastantes respuestas por grupo, porque el sorteo divide la muestra en dos.
- Se puede combinar con la prueba de complacencia (`test-complacencia.md`) o hacer por separado.
