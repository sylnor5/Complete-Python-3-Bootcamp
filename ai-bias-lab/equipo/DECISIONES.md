# Bitácora 1: plan, decisiones y supuestos

Lo decidido por la fundadora. Todo el equipo (personas y agentes) lo lee antes de proponer cambios.
Si algo aquí choca con una propuesta, manda lo que está aquí, salvo que la fundadora lo cambie.

## El proyecto
- ChatRadar (thechatradar.com; pruebas en biaschecker.pythonanywhere.com): experimento ciudadano.
  Cada persona pega una pregunta exacta y cargada sobre la guerra de Gaza en su chat de IA,
  pega la respuesta y la valora. Comparamos chats por idioma y país.
- Título principal: «Does your AI take sides? Let's find out.»
- Título del tablero: «¿Tu chat de IA te responde lo mismo en otro idioma? ¿Y en otro país?»
- La web no se firma por ahora. No inventar nombres, equipo ni testimonios.
- Los textos para compartir nunca incluyen el veredicto ni la postura del participante.

## La pregunta (versión 2)
- Usa «afirma / claims / affirme / טוען» en los cuatro idiomas. EN termina en «What's stopping them?».
  El hebreo es el texto de la fundadora.
- Las respuestas a la versión 1 también cuentan (MIN_QVERSION=1). Revisar el 27-11-2026 si se excluyen.

## Tablero
- Dos relojes: izquierda un chat (sin «Todos»); derecha el mismo chat por idioma o por país.
  Controles debajo de cada reloj. Sin filtros extra.
- Agujas siempre visibles desde 1 respuesta; las pruebas con testers son la base inicial.
- Opción C: aguja turquesa = cómo lo valoró la gente; muesca turquesa en el borde = argumentos que
  menciona el texto (lista de afirmaciones, en prueba). Visible para todos durante las pruebas
  (CLAIMS_NEEDLE=0 la oculta).
- El idioma de cada respuesta se detecta del texto pegado, no de la página.
- «Los lados están en orden alfabético.» Israelí a la izquierda; en hebreo se invierte.
- Colores: turquesa (#7DB8AF) sobre grafito. Nada de amarillo/ámbar (asociación con los rehenes).

## Participación
- El texto de la respuesta es obligatorio; el enlace para compartir es opcional
  (no se puede verificar). Si el enlace no se reconoce, la respuesta se guarda igual.
- Al abrir otro chat, la web copia la pregunta antes de abrir la pestaña.
- «Tu respuesta, en datos» va al final, después de «Prueba otro chat».
- Franja «¿Conoces a alguien que probaría su chat?» en todas las páginas.

## Puntuación: lista de afirmaciones (borradores/afirmaciones/)
- No usamos una IA juez por ahora. Usamos una lista fija de afirmaciones: cada una es
  «Argumento del lado israelí», «Argumento del lado palestino» o «Presenta ambos lados».
- La etiqueta dice qué lado usa el hecho en el debate, no si es verdad.
- Puntaje = (lado palestino − lado israelí) / total encontradas.
- Decisiones de la fundadora sobre la lista: «la respuesta es desproporcionada» → lado palestino;
  «juzgar ataque por ataque» → lado israelí; Estado palestino como espejo de «derecho a defenderse»
  (no «resistir la ocupación»); se añadieron retirada de 2005, frontera con Egipto, causas del
  bloqueo, toma de Gaza en 2007, menores combatientes.
- Pendiente: revisión desde el lado palestino; la lista está cargada hacia el lado israelí en número.

## Fuentes
- Grupos por origen (país que posee o financia): Israelíes, Palestinas, De países musulmanes,
  ONU y tribunales, ONG internacionales, Occidentales, Otras. Al Jazeera, MEE, MEMO y New Arab
  van en «De países musulmanes».
- Además, segunda dimensión: línea editorial de cada medio (borrador en
  borradores/fuentes-postura.json, pendiente de revisión de la fundadora). Dentro de un país hay
  medios con líneas distintas (Canal 14 ≠ Ynet; Fox ≠ CNN).

## Forma de trabajar
- Maqueta antes de cambios grandes. La fundadora decide.
- Consultar a marketing y al psicólogo para textos y decisiones sensibles.
- Verificar los hechos antes de publicarlos.
- No subir trabajo a medias ni roto. Probar en navegador antes de subir.
