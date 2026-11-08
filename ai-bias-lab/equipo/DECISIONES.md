# Bitácora 1: plan, decisiones y supuestos

Lo decidido por la fundadora. Todo el equipo (personas y agentes) lo lee antes de proponer cambios.
Si algo aquí choca con una propuesta, manda lo que está aquí, salvo que la fundadora lo cambie.

## El proyecto
- Marca: **TheChatRadar** (opción B, 7-11-2026), igual que el dominio, para que nadie escriba
  chatradar.com (es de otra persona). En mensajes y redes, escribir siempre «thechatradar.com» completo.
- ChatRadar (thechatradar.com; pruebas en biaschecker.pythonanywhere.com): experimento ciudadano.
  Cada persona pega una pregunta exacta y cargada sobre la guerra de Gaza en su chat de IA,
  pega la respuesta y la valora. Comparamos chats por idioma y país.
- Título principal: «Does your AI take sides? Let's find out.»
- Título del tablero: «¿Tu chat de IA te responde lo mismo en otro idioma? ¿Y en otro país?»
- Portada: encima del botón «Empezar» va la frase «Queremos saber si los chats de IA responden
  igual a todo el mundo. Tú lo compruebas.» (7-11-2026). Explica el porqué sin anclar. La historia
  completa sigue más abajo. «My question» sin «(translated from Spanish)».
- Las respuestas de los testers se quedan: no se borra nada (con 500 respuestas no pesan).
- La web no se firma por ahora. No inventar nombres, equipo ni testimonios.
- Los textos para compartir nunca incluyen el veredicto ni la postura del participante.

## Servidor y dominio
- PythonAnywhere, plan Developer (10 USD/mes, una web). La web se renombró de
  biaschecker.pythonanywhere.com a www.thechatradar.com (7-11-2026); la dirección vieja ya no sirve.
- GoDaddy: CNAME www → webapp-3239598.pythonanywhere.com; thechatradar.com reenvía (301) a
  https://www.thechatradar.com.
- Comando para actualizar la web:
  cd ~/Complete-Python-3-Bootcamp && git pull && touch /var/www/www_thechatradar_com_wsgi.py
- Copias en el servidor: ~/wsgi-copia.py y ~/data-copia.db (7-11-2026).

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
- Sin límite de una respuesta por chat: la fundadora quiere poder mandar el mismo chat en varios
  idiomas. Límite solo por conexión: 10 por hora. Se rechaza el mismo texto exacto dos veces.
- Sospechosas (no cuentan): menos de 150 caracteres, fuera de tema (sin palabras clave), duplicadas.
- Si el chat se niega a contestar, no se descarta: se cuenta aparte («se negó a responder»), sin mover agujas.
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

## Redes sociales (borradores/redes/)
- Instagram: nombre visible «TheChatRadar»; usuario @thechatradar. Cuenta creada (7-11-2026).
- Acceso (7-11-2026, cambia la regla anterior): Claude puede entrar en la cuenta para preparar
  perfil y borradores, siempre desde el navegador de la fundadora (sin compartir la contraseña).
  Publicar, programar o responder solo con su autorización explícita, cada vez.
- Pie de los posts: un solo idioma por post, rotando entre es/en/fr/he. Más adelante, elegir
  según los países del público (7-11-2026).
- La cita de ChatGPT, cuando se use, va en el idioma del post, sin indicar que es traducción
  (8-11-2026).
- Árabe: por ahora no (ni en posts ni en la web). La biografía va solo en inglés (7-11-2026).
- La historia de la portada (la conversación con ChatGPT) puede usarse en redes como gancho
  narrativo. Los posts deben atraer y dar curiosidad, sin tomar partido ni dar veredicto (7-11-2026).

## Forma de trabajar
- Dos sesiones: «ChatRadar Live» lleva la web en vivo y el código; «TheChatRadar Redes» lleva
  redes sociales y solo escribe en borradores/redes/ (7-11-2026).
- Maqueta antes de cambios grandes. La fundadora decide.
- Consultar a marketing y al psicólogo para textos y decisiones sensibles.
- Verificar los hechos antes de publicarlos.
- No subir trabajo a medias ni roto. Probar en navegador antes de subir.
