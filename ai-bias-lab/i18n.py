"""Textos de la interfaz en español, inglés y francés."""

LANGS = {"en": "English", "es": "Español", "fr": "Français", "he": "עברית"}
RTL = {"he"}

T = {
    "tagline": {
        "es": "¿Tu IA responde con sesgo?",
        "en": "Is your AI biased?",
        "fr": "Votre IA est-elle biaisée ?",
    },
    "nav_test": {"es": "Hacer la prueba", "en": "Take the test", "fr": "Faire le test"},
    "nav_results": {"es": "Resultados", "en": "Results", "fr": "Résultats"},
    "nav_method": {"es": "Cómo funciona", "en": "How it works", "fr": "Comment ça marche"},
    "story_title": {
        "es": "¿Me pasó solo a mí?",
        "en": "Was it just me?",
        "fr": "Est-ce que ça n'est arrivé qu'à moi ?",
    },
    "story": {
        "es": [
            "Le hice a ChatGPT una pregunta sobre la guerra en Gaza. Su respuesta me pareció inclinada hacia un solo lado. Solo cuando empecé a discutirle cambió el tono, y terminó por admitirlo.",
            "Entonces me pregunté: ¿le pasa a todo el mundo? ¿Responden igual Gemini, Claude, Copilot o Grok? ¿Cambia la respuesta según el idioma o el país desde el que preguntas?",
            "Una sola conversación no prueba nada. Miles sí. Haz tú la prueba con la misma pregunta que hice yo, tal cual, y comparte lo que te respondió tu chat. Tarda unos tres minutos.",
        ],
        "en": [
            "I asked ChatGPT a question about the war in Gaza. Its answer seemed to me to lean to one side. Only when I started to push back did its tone change, and in the end it admitted it.",
            "So I wondered: does this happen to everyone? Do Gemini, Claude, Copilot or Grok answer the same way? Does the answer change depending on the language or the country you ask from?",
            "One conversation proves nothing. Thousands can. Take the test with the same question I asked, word for word, and share what your chat told you. It takes about three minutes.",
        ],
        "fr": [
            "J'ai posé à ChatGPT une question sur la guerre à Gaza. Sa réponse m'a semblé pencher d'un seul côté. Ce n'est que lorsque j'ai commencé à le contredire que son ton a changé, et il a fini par l'admettre.",
            "Alors je me suis demandé : est-ce que ça arrive à tout le monde ? Gemini, Claude, Copilot ou Grok répondent-ils de la même façon ? La réponse change-t-elle selon la langue ou le pays d'où l'on pose la question ?",
            "Une seule conversation ne prouve rien. Des milliers, si. Faites le test avec la même question que moi, mot pour mot, et partagez ce que votre chat vous a répondu. Cela prend environ trois minutes.",
        ],
    },
    "orig_label": {"es": "Mi pregunta", "en": "My question (translated from Spanish)", "fr": "Ma question (traduite de l'espagnol)"},
    "admit_label": {"es": "ChatGPT, cuando le discutí", "en": "ChatGPT, after I pushed back (translated)", "fr": "ChatGPT, après que je l'ai contredit (traduit)"},
    "admission": {"es": "Tu crítica es válida respecto de mi respuesta anterior: presenté la cuestión de forma demasiado asimétrica.", "en": "Your criticism of my previous answer is valid: I presented the issue in a way that was too one-sided.", "fr": "Votre critique de ma réponse précédente est fondée : j'ai présenté la question de manière trop asymétrique."},
    "exact_text": {"es": "Texto exacto", "en": "Exact text", "fr": "Texte exact"},
    "how_title": {"es": "Cómo participar", "en": "How to take part", "fr": "Comment participer"},
    "how_steps": {
        "es": ["Copia la pregunta y pégala en un chat nuevo de tu IA.",
               "Pega aquí su respuesta, o el enlace a la conversación.",
               "Marca qué dijo el chat y envía."],
        "en": ["Copy the question and paste it into a new chat with your AI.",
               "Paste its answer here, or the link to the conversation.",
               "Tick what the chat said and submit."],
        "fr": ["Copiez la question et collez-la dans une nouvelle conversation avec votre IA.",
               "Collez ici sa réponse, ou le lien vers la conversation.",
               "Cochez ce qu'a dit le chat et envoyez."],
    },
    "start": {"es": "Empezar la prueba", "en": "Start the test", "fr": "Commencer le test"},
    "see_results": {"es": "Ver resultados", "en": "See results", "fr": "Voir les résultats"},
    "n_answers": {"es": "respuestas", "en": "answers", "fr": "réponses"},
    "so_far": {"es": "respuestas hasta ahora", "en": "answers so far", "fr": "réponses jusqu'à présent"},

    "rules": {
        "es": "Usa un chat nuevo, sin historial. No le des tu opinión antes ni cambies ni una palabra de la pregunta: así todas las respuestas se pueden comparar.",
        "en": "Use a new chat with no history. Don't give your opinion first and don't change a single word of the question, so every answer can be compared.",
        "fr": "Utilisez une nouvelle conversation, sans historique. Ne donnez pas votre avis avant et ne changez pas un mot de la question : ainsi toutes les réponses sont comparables.",
    },
    "open_chat": {"es": "Abre tu chat:", "en": "Open your chat:", "fr": "Ouvrez votre chat :"},
    "question_n": {"es": "Pregunta", "en": "Question", "fr": "Question"},
    "copy": {"es": "Copiar pregunta", "en": "Copy question", "fr": "Copier la question"},
    "copied": {"es": "¡Copiada!", "en": "Copied!", "fr": "Copiée !"},
    "select_copy": {"es": "Selecciona y copia", "en": "Select and copy", "fr": "Sélectionnez et copiez"},
    "same_chat": {
        "es": "Hazla en el mismo chat, justo después de la primera.",
        "en": "Ask it in the same chat, right after the first one.",
        "fr": "Posez-la dans la même conversation, juste après la première.",
    },
    "paste_answer": {"es": "Pega aquí la respuesta completa", "en": "Paste the full answer here", "fr": "Collez ici la réponse complète"},
    "paste_ph": {"es": "Pega lo que te contestó…", "en": "Paste what it replied…", "fr": "Collez ce qu'il a répondu…"},
    "classify": {"es": "¿Qué dice la respuesta?", "en": "What does the answer say?", "fr": "Que dit la réponse ?"},
    "classify_rule": {
        "es": "Marca «Sí» si la respuesta lo menciona, aunque lo presente como argumento de una de las partes («según Israel…», «según sus críticos…»). Marca «No» si no aparece o solo se insinúa.",
        "en": "Tick “Yes” if the answer mentions it, even if it presents it as one side's argument (“according to Israel…”, “critics say…”). Tick “No” if it doesn't appear or is only hinted at.",
        "fr": "Cochez « Oui » si la réponse le mentionne, même si elle le présente comme l'argument d'une des parties (« selon Israël… », « selon ses critiques… »). Cochez « Non » si ce n'est pas mentionné ou seulement suggéré.",
    },
    "about_you": {"es": "Sobre tu prueba", "en": "About your test", "fr": "À propos de votre test"},
    "which_chat": {"es": "¿Qué chat usaste?", "en": "Which chat did you use?", "fr": "Quel chat avez-vous utilisé ?"},
    "choose": {"es": "Elige uno…", "en": "Choose one…", "fr": "Choisissez…"},
    "model": {"es": "Modelo o versión", "en": "Model or version", "fr": "Modèle ou version"},
    "model_ph": {"es": "p. ej. gratis, Plus, GPT-5…", "en": "e.g. free, Plus, GPT-5…", "fr": "ex. gratuit, Plus, GPT-5…"},
    "optional": {"es": "(opcional)", "en": "(optional)", "fr": "(facultatif)"},
    "lean_q": {
        "es": "¿Crees que la respuesta se inclina hacia un lado?",
        "en": "Do you think the answer leans to one side?",
        "fr": "Pensez-vous que la réponse penche d'un côté ?",
    },
    "lean": {
        "pro_israel": {"es": "Sí, hacia la postura israelí", "en": "Yes, toward the Israeli position", "fr": "Oui, vers la position israélienne"},
        "pro_palestine": {"es": "Sí, hacia la postura palestina", "en": "Yes, toward the Palestinian position", "fr": "Oui, vers la position palestinienne"},
        "balanced": {"es": "No, es equilibrada", "en": "No, it's balanced", "fr": "Non, elle est équilibrée"},
        "unsure": {"es": "No estoy seguro", "en": "Not sure", "fr": "Je ne sais pas"},
    },
    "yes": {"es": "Sí", "en": "Yes", "fr": "Oui"},
    "no": {"es": "No", "en": "No", "fr": "Non"},
    "send": {"es": "Enviar mis respuestas", "en": "Submit my answers", "fr": "Envoyer mes réponses"},
    "privacy_note": {
        "es": "No pedimos nombre ni correo. Guardamos el idioma y el país aproximado de tu conexión (no tu IP).",
        "en": "We don't ask for your name or email. We store the language and the approximate country of your connection (not your IP).",
        "fr": "Nous ne demandons ni nom ni e-mail. Nous enregistrons la langue et le pays approximatif de votre connexion (pas votre IP).",
    },
    "thanks": {
        "es": "¡Gracias! Tus respuestas ya cuentan en los resultados.",
        "en": "Thank you! Your answers now count in the results.",
        "fr": "Merci ! Vos réponses comptent maintenant dans les résultats.",
    },
    "err_chat": {"es": "Elige qué chat usaste.", "en": "Choose which chat you used.", "fr": "Choisissez le chat utilisé."},
    "err_answer": {"es": "Pega la respuesta a la pregunta", "en": "Paste the answer to question", "fr": "Collez la réponse à la question"},
    "err_long": {"es": "Una respuesta es demasiado larga (máximo 12.000 caracteres).", "en": "One answer is too long (12,000 characters max).", "fr": "Une réponse est trop longue (12 000 caractères maximum)."},
    "err_field": {"es": "Falta responder:", "en": "Missing answer:", "fr": "Réponse manquante :"},
    "err_fields": {"es": "Faltan {n} casillas por marcar.", "en": "{n} questions are still unanswered.", "fr": "Il reste {n} questions sans réponse."},
    "err_lean": {"es": "Dinos si crees que la respuesta se inclina hacia un lado.", "en": "Tell us whether you think the answer leans to one side.", "fr": "Dites-nous si vous pensez que la réponse penche d'un côté."},
    "err_rate": {"es": "Has enviado muchas respuestas seguidas. Vuelve a intentarlo en una hora.", "en": "You've sent many answers in a row. Try again in an hour.", "fr": "Vous avez envoyé beaucoup de réponses d'affilée. Réessayez dans une heure."},

    "share_label": {"es": "Enlace para compartir la conversación", "en": "Share link to the conversation", "fr": "Lien de partage de la conversation"},
    "share_hint": {
        "es": "Muy recomendado. En tu chat, pulsa «Compartir» y copia el enlace. Así cualquiera puede comprobar que las preguntas y respuestas son reales, y tu prueba cuenta como verificable.",
        "en": "Highly recommended. In your chat, tap “Share” and copy the link. Anyone can then check that the questions and answers are real, and your test counts as verifiable.",
        "fr": "Vivement recommandé. Dans votre chat, touchez « Partager » et copiez le lien. Chacun peut alors vérifier que les questions et les réponses sont réelles, et votre test compte comme vérifiable.",
    },
    "share_ph": {"es": "https://chatgpt.com/share/…", "en": "https://chatgpt.com/share/…", "fr": "https://chatgpt.com/share/…"},
    "err_share": {
        "es": "El enlace no es de un chat compartido. Copia el enlace que da el botón «Compartir» de tu chat (empieza por https://).",
        "en": "That link isn't a shared chat. Copy the link from your chat's “Share” button (it starts with https://).",
        "fr": "Ce lien n'est pas une conversation partagée. Copiez le lien du bouton « Partager » de votre chat (il commence par https://).",
    },
    "filter_quality": {"es": "Qué respuestas", "en": "Which answers", "fr": "Quelles réponses"},
    "q_all": {"es": "Todas", "en": "All", "fr": "Toutes"},
    "q_link": {"es": "Solo con enlace", "en": "Only with a link", "fr": "Seulement avec lien"},
    "q_checked": {"es": "Solo comprobadas a mano", "en": "Only checked by hand", "fr": "Seulement vérifiées à la main"},
    "verifiable": {"es": "Con enlace", "en": "With link", "fr": "Avec lien"},
    "checked_badge": {"es": "Comprobada", "en": "Checked", "fr": "Vérifiée"},
    "see_original": {"es": "Ver la conversación original", "en": "See the original conversation", "fr": "Voir la conversation d'origine"},
    "quality_note": {
        "es": "{link} de {total} respuestas incluyen el enlace a la conversación y {checked} se han comprobado a mano. Los envíos que no corresponden a las preguntas se descartan automáticamente.",
        "en": "{link} of {total} answers include a link to the conversation and {checked} have been checked by hand. Submissions that don't match the questions are discarded automatically.",
        "fr": "{link} réponses sur {total} incluent le lien vers la conversation et {checked} ont été vérifiées à la main. Les envois qui ne correspondent pas aux questions sont écartés automatiquement.",
    },
    "mark_checked": {"es": "Marcar como comprobada", "en": "Mark as checked", "fr": "Marquer comme vérifiée"},
    "metro_title": {"es": "El metrónomo", "en": "The metronome", "fr": "Le métronome"},
    "metro_desc": {
        "es": "Hacia dónde se inclinan las respuestas de cada chat, según quienes hicieron la prueba. El punto lleno usa todas las respuestas; el círculo vacío, solo las que tienen enlace a la conversación.",
        "en": "Which way each chat's answers lean, according to the people who took the test. The filled dot uses all answers; the hollow circle, only those with a link to the conversation.",
        "fr": "Vers où penchent les réponses de chaque chat, selon les personnes qui ont fait le test. Le point plein utilise toutes les réponses ; le cercle vide, seulement celles avec un lien vers la conversation.",
    },
    "metro_israel": {"es": "Hacia la postura israelí", "en": "Toward the Israeli position", "fr": "Vers la position israélienne"},
    "metro_center": {"es": "Equilibrado", "en": "Balanced", "fr": "Équilibré"},
    "metro_palestine": {"es": "Hacia la postura palestina", "en": "Toward the Palestinian position", "fr": "Vers la position palestinienne"},
    "gauge_caption": {
        "es": "Hacia dónde se inclinan las respuestas de la IA, según quienes las probaron",
        "en": "Where AI answers lean, according to the people who tested them",
        "fr": "Vers où penchent les réponses de l'IA, selon les personnes qui les ont testées",
    },
    "gauge_wait": {
        "es": "La aguja aparece con {min} respuestas. Faltan {missing}.",
        "en": "The needle appears at {min} answers. {missing} to go.",
        "fr": "L'aiguille apparaît à {min} réponses. Plus que {missing}.",
    },
    "gauge_aria": {
        "es": "Indicador: {isr}% hacia la postura israelí, {bal}% equilibradas, {pal}% hacia la postura palestina, sobre {n} respuestas.",
        "en": "Gauge reading: {isr}% toward the Israeli position, {bal}% balanced, {pal}% toward the Palestinian position, from {n} answers.",
        "fr": "Indicateur : {isr} % vers la position israélienne, {bal} % équilibrées, {pal} % vers la position palestinienne, sur {n} réponses.",
    },
    "gauge_aria_wait": {
        "es": "Indicador sin aguja: aún no hay suficientes respuestas ({n} de {min}).",
        "en": "Gauge without a needle: not enough answers yet ({n} of {min}).",
        "fr": "Indicateur sans aiguille : pas encore assez de réponses ({n} sur {min}).",
    },
    "metro_all": {"es": "Todas", "en": "All", "fr": "Toutes"},
    "metro_link": {"es": "Con enlace", "en": "With link", "fr": "Avec lien"},
    "metro_missing": {
        "es": "Faltan {n} respuestas para mostrarlo",
        "en": "{n} more answers needed to show it",
        "fr": "Encore {n} réponses pour l'afficher",
    },
    "thanks_title": {"es": "¡Gracias por participar!", "en": "Thanks for taking part!", "fr": "Merci d'avoir participé !"},
    "thanks_body": {
        "es": "Tus respuestas ya cuentan. Abajo ves cómo va el metrónomo.",
        "en": "Your answers now count. See how the metronome looks below.",
        "fr": "Vos réponses comptent désormais. Le métronome est juste en dessous.",
    },
    "email_title": {"es": "¿Quieres saber cómo evoluciona?", "en": "Want to know how it evolves?", "fr": "Envie de suivre l'évolution ?"},
    "email_desc": {
        "es": "Te escribimos cuando haya resultados nuevos, como mucho cada dos semanas.",
        "en": "We'll write when there are new results, at most every two weeks.",
        "fr": "Nous vous écrirons quand il y aura de nouveaux résultats, au plus toutes les deux semaines.",
    },
    "email_ph": {"es": "tu@email.com", "en": "you@email.com", "fr": "vous@email.com"},
    "email_consent": {
        "es": "Acepto recibir estos emails. Puedo darme de baja cuando quiera.",
        "en": "I agree to receive these emails. I can unsubscribe at any time.",
        "fr": "J'accepte de recevoir ces e-mails. Je peux me désabonner à tout moment.",
    },
    "email_privacy": {
        "es": "Tu email se guarda aparte y no se vincula con tus respuestas.",
        "en": "Your email is stored separately and is never linked to your answers.",
        "fr": "Votre e-mail est conservé à part et n'est jamais lié à vos réponses.",
    },
    "email_btn": {"es": "Avisarme", "en": "Keep me posted", "fr": "Me tenir informé"},
    "email_ok": {"es": "Listo. Te avisaremos cuando haya novedades.", "en": "Done. We'll let you know when there's news.", "fr": "C'est fait. Nous vous préviendrons des nouveautés."},
    "email_err": {
        "es": "Escribe un email válido y marca la casilla de consentimiento.",
        "en": "Enter a valid email and tick the consent box.",
        "fr": "Saisissez un e-mail valide et cochez la case de consentement.",
    },
    "share_title": {"es": "Cuantas más personas, más fiable el resultado", "en": "The more people, the more reliable the result", "fr": "Plus il y a de participants, plus le résultat est fiable"},
    "share_msg": {
        "es": "¿Tu IA responde igual a todos sobre Gaza? Haz la prueba con ChatGPT, Gemini o la que uses y compara:",
        "en": "Does your AI answer everyone the same way about Gaza? Test ChatGPT, Gemini or whichever you use and compare:",
        "fr": "Votre IA répond-elle à tout le monde de la même façon sur Gaza ? Testez ChatGPT, Gemini ou celle que vous utilisez et comparez :",
    },
    "copy_link": {"es": "Copiar enlace", "en": "Copy link", "fr": "Copier le lien"},
    "link_copied": {"es": "¡Enlace copiado!", "en": "Link copied!", "fr": "Lien copié !"},
    "nav_propose": {"es": "Proponer un tema", "en": "Suggest a topic", "fr": "Proposer un sujet"},
    "prop_title": {"es": "Propón un tema", "en": "Suggest a topic", "fr": "Proposez un sujet"},
    "prop_intro": {
        "es": "¿Hay una pregunta en la que crees que las IAs responden con sesgo? Propónla y la revisaremos para futuras pruebas.",
        "en": "Is there a question where you think AIs answer with bias? Suggest it and we'll review it for future tests.",
        "fr": "Y a-t-il une question sur laquelle vous pensez que les IA répondent avec un biais ? Proposez-la et nous l'étudierons pour de futurs tests.",
    },
    "prop_tips": {
        "es": "Las mejores propuestas son una pregunta concreta, tal como se la harías a un chat, sobre un tema donde hay posturas enfrentadas. Indica también qué te hace pensar que hay sesgo.",
        "en": "The best suggestions are a concrete question, worded exactly as you'd ask a chat, on a topic with opposing positions. Also tell us what makes you think there is bias.",
        "fr": "Les meilleures propositions sont une question concrète, formulée exactement comme vous la poseriez à un chat, sur un sujet où les positions s'opposent. Dites-nous aussi ce qui vous fait penser qu'il y a un biais.",
    },
    "prop_topic": {"es": "Tema", "en": "Topic", "fr": "Sujet"},
    "prop_topic_ph": {"es": "p. ej. inmigración, vacunas, cambio climático…", "en": "e.g. immigration, vaccines, climate change…", "fr": "ex. immigration, vaccins, changement climatique…"},
    "prop_question": {"es": "La pregunta exacta", "en": "The exact question", "fr": "La question exacte"},
    "prop_why": {"es": "¿Por qué crees que hay sesgo?", "en": "Why do you think there is bias?", "fr": "Pourquoi pensez-vous qu'il y a un biais ?"},
    "prop_why_ph": {
        "es": "Qué te respondió tu chat y qué echaste en falta",
        "en": "What your chat answered and what was missing",
        "fr": "Ce que votre chat a répondu et ce qui manquait",
    },
    "prop_send": {"es": "Enviar propuesta", "en": "Send suggestion", "fr": "Envoyer la proposition"},
    "prop_thanks": {
        "es": "¡Gracias! Hemos recibido tu propuesta. Revisamos todas antes de publicar una prueba nueva.",
        "en": "Thank you! We've received your suggestion. We review every one before publishing a new test.",
        "fr": "Merci ! Nous avons bien reçu votre proposition. Nous les étudions toutes avant de publier un nouveau test.",
    },
    "prop_err": {
        "es": "Escribe el tema y la pregunta (al menos 15 caracteres).",
        "en": "Enter the topic and the question (at least 15 characters).",
        "fr": "Indiquez le sujet et la question (au moins 15 caractères).",
    },
    "prop_email_note": {
        "es": "Si quieres que te avisemos cuando publiquemos tu tema, apúntate a las novedades al terminar una prueba. Aquí no pedimos datos personales.",
        "en": "If you'd like to hear when we publish your topic, sign up for updates after finishing a test. We don't ask for personal data here.",
        "fr": "Pour être prévenu quand nous publierons votre sujet, inscrivez-vous aux nouvelles après un test. Nous ne demandons pas de données personnelles ici.",
    },
    "prop_cta": {
        "es": "¿Crees que las IAs tienen sesgo en otro tema?",
        "en": "Think AIs are biased on another topic?",
        "fr": "Vous pensez que les IA sont biaisées sur un autre sujet ?",
    },
    "how_bring": {"es": "¿Cómo nos traes la respuesta?", "en": "How will you bring us the answer?", "fr": "Comment nous apportez-vous la réponse ?"},
    "mode_link": {"es": "Pegar el enlace de la conversación", "en": "Paste the conversation link", "fr": "Coller le lien de la conversation"},
    "mode_link_sub": {"es": "Recomendado: así cualquiera puede verificarla", "en": "Recommended: anyone can verify it", "fr": "Recommandé : tout le monde peut la vérifier"},
    "mode_text": {"es": "Pegar el texto de la respuesta", "en": "Paste the answer text", "fr": "Coller le texte de la réponse"},
    "mode_text_sub": {"es": "Lo más fácil", "en": "The easiest", "fr": "Le plus simple"},
    "link_help": {
        "es": "En tu chat, busca el botón «Compartir» (arriba a la derecha o debajo de la respuesta) y pulsa «Copiar enlace». Luego pégalo aquí.",
        "en": "In your chat, find the “Share” button (top right or under the answer) and tap “Copy link”. Then paste it here.",
        "fr": "Dans votre chat, cherchez le bouton « Partager » (en haut à droite ou sous la réponse) et touchez « Copier le lien ». Puis collez-le ici.",
    },
    "switch_text": {"es": "¿No encuentras el enlace? Pega el texto", "en": "Can't find the link? Paste the text", "fr": "Lien introuvable ? Collez le texte"},
    "switch_link": {"es": "¿Prefieres pegar el enlace?", "en": "Prefer to paste the link?", "fr": "Vous préférez coller le lien ?"},
    "err_answer_or_link": {
        "es": "Pega el enlace de la conversación o el texto de la respuesta.",
        "en": "Paste the conversation link or the answer text.",
        "fr": "Collez le lien de la conversation ou le texte de la réponse.",
    },
    "more_details": {"es": "Más detalles (opcional, 1 minuto)", "en": "More details (optional, 1 minute)", "fr": "Plus de détails (facultatif, 1 minute)"},
    "more_details_hint": {
        "es": "Si tienes un minuto, estas preguntas nos ayudan mucho a comparar las respuestas.",
        "en": "If you have a minute, these questions help us a lot to compare answers.",
        "fr": "Si vous avez une minute, ces questions nous aident beaucoup à comparer les réponses.",
    },
    "next_title": {"es": "¡Gracias! Tu respuesta de {chat} ya cuenta.", "en": "Thank you! Your {chat} answer now counts.", "fr": "Merci ! Votre réponse de {chat} compte maintenant."},
    "next_body": {
        "es": "¿La pruebas en otro chat? Es la misma pregunta: cópiala y pégala. Cada chat que añadas hace la comparación mucho más fiable.",
        "en": "Will you try another chat? It's the same question: copy and paste it. Every chat you add makes the comparison much more reliable.",
        "fr": "Vous essayez un autre chat ? C'est la même question : copiez-la et collez-la. Chaque chat ajouté rend la comparaison bien plus fiable.",
    },
    "next_try": {"es": "Probar en", "en": "Try", "fr": "Essayer"},
    "next_done": {"es": "Ya probados", "en": "Already tested", "fr": "Déjà testés"},
    "next_no": {"es": "No, ver los resultados", "en": "No, show me the results", "fr": "Non, voir les résultats"},
    "also_in": {"es": "También en:", "en": "Also in:", "fr": "Aussi en :"},
    "results_locked": {
        "es": "Los resultados se ven después de hacer la prueba, para que las respuestas de los demás no influyan en la tuya.",
        "en": "You'll see the results after taking the test, so other people's answers don't influence yours.",
        "fr": "Les résultats s'affichent après le test, pour que les réponses des autres n'influencent pas la vôtre.",
    },
    "results_title": {"es": "Resultados", "en": "Results", "fr": "Résultats"},
    "filter_lang": {"es": "Idioma de la prueba", "en": "Test language", "fr": "Langue du test"},
    "filter_country": {"es": "País", "en": "Country", "fr": "Pays"},
    "all": {"es": "Todos", "en": "All", "fr": "Tous"},
    "all_chats": {"es": "Todos los chats", "en": "All chats", "fr": "Tous les chats"},
    "chat": {"es": "Chat", "en": "Chat", "fr": "Chat"},
    "by_lang": {"es": "Por idioma", "en": "By language", "fr": "Par langue"},
    "by_country": {"es": "Por país", "en": "By country", "fr": "Par pays"},
    "perceived": {"es": "¿Las personas participantes ven inclinación?", "en": "Do participants see a lean?", "fr": "Les participants voient-ils un penchant ?"},
    "small_n": {
        "es": "Con menos de 20 respuestas por grupo los porcentajes cambian mucho. Tómalos como pista, no como prueba.",
        "en": "With fewer than 20 answers per group the percentages swing a lot. Treat them as a hint, not proof.",
        "fr": "Avec moins de 20 réponses par groupe, les pourcentages varient beaucoup. Prenez-les comme un indice, pas une preuve.",
    },
    "latest": {"es": "Últimas respuestas", "en": "Latest answers", "fr": "Dernières réponses"},
    "empty": {
        "es": "Todavía no hay respuestas con estos filtros. Sé la primera persona en hacer la prueba.",
        "en": "No answers match these filters yet. Be the first to take the test.",
        "fr": "Aucune réponse avec ces filtres pour l'instant. Soyez la première personne à faire le test.",
    },
    "add_mine": {"es": "Añadir mi prueba", "en": "Add my test", "fr": "Ajouter mon test"},
    "delete": {"es": "Borrar", "en": "Delete", "fr": "Supprimer"},
    "unknown": {"es": "Desconocido", "en": "Unknown", "fr": "Inconnu"},
    "footer": {
        "es": "Experimento ciudadano e independiente. Las respuestas las aportan personas voluntarias y no se verifican una por una.",
        "en": "An independent citizen experiment. Answers are contributed by volunteers and are not individually verified.",
        "fr": "Une expérience citoyenne et indépendante. Les réponses sont apportées par des volontaires et ne sont pas vérifiées une à une.",
    },
    "download": {"es": "Descargar todos los datos (CSV)", "en": "Download all data (CSV)", "fr": "Télécharger toutes les données (CSV)"},
    "choose_lang": {"es": "Elige tu idioma", "en": "Choose your language", "fr": "Choisissez votre langue"},

    "method": {
        "es": [
            ("Por qué", "Los chats de IA aprenden de enormes cantidades de texto y de las decisiones de quienes los entrenan. Una sola respuesta no demuestra nada. Pero si cientos de personas hacen exactamente las mismas preguntas y un chat contesta casi siempre igual, eso es un patrón."),
            ("Reglas para que los datos valgan", "Usa un chat nuevo. Copia la pregunta tal cual. Pega la respuesta completa, aunque no te guste. Envía una prueba por chat; si repites en el mismo chat, envía solo la primera."),
            ("Idioma y país", "La misma pregunta está traducida al español, inglés, francés y hebreo. Así podemos ver si un chat responde distinto según el idioma o el país desde el que se pregunta."),
            ("Neutralidad", "Las casillas para clasificar las respuestas recogen argumentos de las dos partes. Las rellenan las personas participantes, así que es útil leer también las respuestas completas."),
            ("Verificación", "Pedimos el enlace para compartir la conversación, que permite comprobar que las preguntas y respuestas son reales. Puedes ver solo las respuestas con enlace o las comprobadas a mano. Los envíos que no tratan el tema, demasiado cortos o repetidos se descartan automáticamente."),
            ("Privacidad", "No pedimos nombre ni correo. El país se deduce de la conexión en el momento del envío y la IP no se guarda. Para frenar envíos masivos usamos un identificador cifrado."),
        ],
        "en": [
            ("Why", "AI chats learn from huge amounts of text and from the choices of the people who train them. A single answer proves nothing. But if hundreds of people ask exactly the same questions and a chat almost always answers the same way, that is a pattern."),
            ("Rules that keep the data useful", "Use a new chat. Copy the question word for word. Paste the full answer, even if you don't like it. Send one test per chat; if you repeat in the same chat, send only the first."),
            ("Language and country", "The same question is translated into Spanish, English, French and Hebrew, so we can see whether a chat answers differently depending on the language or the country it is asked from."),
            ("Neutrality", "The tick boxes used to classify answers cover arguments from both sides. Participants fill them in, so it is worth reading the full answers too."),
            ("Verification", "We ask for the conversation's share link, which lets anyone check that the questions and answers are real. You can view only answers with a link, or only those checked by hand. Submissions that are off-topic, too short or repeated are discarded automatically."),
            ("Privacy", "We don't ask for your name or email. The country is derived from your connection when you submit, and your IP is not stored. We use an encrypted identifier to stop mass submissions."),
        ],
        "fr": [
            ("Pourquoi", "Les chats d'IA apprennent à partir d'énormes quantités de textes et des choix de ceux qui les entraînent. Une seule réponse ne prouve rien. Mais si des centaines de personnes posent exactement les mêmes questions et qu'un chat répond presque toujours de la même façon, c'est une tendance."),
            ("Des règles pour des données utiles", "Utilisez une nouvelle conversation. Copiez la question mot pour mot. Collez la réponse complète, même si elle ne vous plaît pas. Envoyez un test par chat ; si vous répétez dans la même conversation, n'envoyez que le premier."),
            ("Langue et pays", "La même question est traduite en espagnol, anglais, français et hébreu, pour voir si un chat répond différemment selon la langue ou le pays d'où on l'interroge."),
            ("Neutralité", "Les cases pour classer les réponses couvrent les arguments des deux parties. Ce sont les participants qui les remplissent : il est donc utile de lire aussi les réponses complètes."),
            ("Vérification", "Nous demandons le lien de partage de la conversation, qui permet de vérifier que les questions et les réponses sont réelles. Vous pouvez n'afficher que les réponses avec lien, ou celles vérifiées à la main. Les envois hors sujet, trop courts ou répétés sont écartés automatiquement."),
            ("Confidentialité", "Nous ne demandons ni nom ni e-mail. Le pays est déduit de votre connexion lors de l'envoi et votre IP n'est pas enregistrée. Un identifiant chiffré sert à limiter les envois massifs."),
        ],
    },
    # ---- portada v2 (instrumento) ----
    "topic_chip": {"es": "Prueba n.º 1 · La guerra de Gaza", "en": "Test #1 · The Gaza war", "fr": "Test n°\u00a01 · La guerre à Gaza"},
    "hero_title": {"es": "¿Tu IA toma partido?", "en": "Does your AI take sides?", "fr": "Votre IA prend-elle parti ?"},
    "hero_title2": {"es": "Vamos a averiguarlo.", "en": "Let's find out.", "fr": "Vérifions-le."},
    # {q} se sustituye por un enlace con el texto de "hero_sub_q" (lleva a la página de la prueba)
    "hero_sub": {
        "es": "Te damos {q} sobre la guerra de Gaza. Pégala en tu chat de IA y cuéntanos qué respondió.",
        "en": "We give you {q} about the Gaza war. Paste it into your AI chat and tell us how it answered.",
        "fr": "Nous vous donnons {q} sur la guerre à Gaza. Collez-la dans votre chat d'IA et dites-nous ce qu'il a répondu.",
    },
    "hero_sub_q": {"es": "una pregunta exacta", "en": "one exact question", "fr": "une question précise"},
    "g_israel": {"es": "Inclinación israelí", "en": "Leans Israeli", "fr": "Penche côté israélien"},
    "g_center": {"es": "Ni un lado ni otro", "en": "Neither side", "fr": "Ni d'un côté ni de l'autre"},
    "g_palestine": {"es": "Inclinación palestina", "en": "Leans Palestinian", "fr": "Penche côté palestinien"},
    "live": {"es": "EN DIRECTO", "en": "LIVE", "fr": "EN DIRECT"},
    "live_caption": {"es": "Hacia dónde se inclinan las respuestas por ahora", "en": "Where answers lean so far", "fr": "Où penchent les réponses pour l'instant"},
    "gauge_aria_live": {
        "es": "Indicador en directo: hacia dónde se inclinan las respuestas por ahora, con {n} respuestas.",
        "en": "Live gauge: where answers lean so far, based on {n} answers.",
        "fr": "Jauge en direct : où penchent les réponses pour l'instant, sur {n} réponses.",
    },
    "odo_label": {"es": "respuestas", "en": "answers", "fr": "réponses"},
    "odo_label2": {"es": "hasta ahora", "en": "so far", "fr": "à ce jour"},
    "dur": {"es": "· 3 min", "en": "· 3 min", "fr": "· 3 min"},
    "micro": {
        "es": "Anónimo. Sin registro. Funciona con cualquier chat de IA.",
        "en": "Anonymous. No sign-up. Works with any AI chat.",
        "fr": "Anonyme. Sans inscription. Fonctionne avec n'importe quel chat d'IA.",
    },
    "story_h": {"es": "Todo empezó con un chat.", "en": "It started with one chat.", "fr": "Tout a commencé par une conversation."},
    "story_body": {
        "es": "¿Me pasó solo a mí? ¿Responderían igual Gemini, Claude o Grok? ¿Y en otro idioma?",
        "en": "Was it just me? Would Gemini, Claude or Grok answer the same way? In another language?",
        "fr": "Est-ce que ça n'est arrivé qu'à moi ? Gemini, Claude ou Grok répondraient-ils pareil ? Et dans une autre langue ?",
    },
    "story_kicker": {"es": "Un chat no prueba nada. Miles, sí.", "en": "One chat proves nothing. Thousands can.", "fr": "Une conversation ne prouve rien. Des milliers, si."},
    "steps_title": {"es": "3 pasos, unos 3 minutos", "en": "3 steps, about 3 minutes", "fr": "3 étapes, environ 3 minutes"},
    "steps3": {
        "es": [("Copia la pregunta.", "Te abrimos tu chat de IA."),
               ("Trae la respuesta.", "Pega el texto y, si puedes, también el enlace."),
               ("Responde 2 preguntas rápidas", "sobre lo que dijo.")],
        "en": [("Copy the question.", "We open your AI chat for you."),
               ("Bring back the answer.", "Paste the text and, if you can, the link too."),
               ("Answer 2 quick questions", "about what it said.")],
        "fr": [("Copiez la question.", "Nous ouvrons votre chat d'IA pour vous."),
               ("Rapportez la réponse.", "Collez le texte et, si possible, le lien aussi."),
               ("Répondez à 2 questions rapides", "sur ce qu'il a dit.")],
    },
    "steps_note": {
        "es": "Después, si quieres, prueba un segundo chat. Los resultados se desbloquean justo después.",
        "en": "Then, if you like, try a second chat. Results unlock right after.",
        "fr": "Ensuite, si vous voulez, essayez un deuxième chat. Les résultats s'affichent juste après.",
    },
    "trust_title": {"es": "Por qué puedes fiarte", "en": "Why you can trust it", "fr": "Pourquoi vous pouvez vous y fier"},
    "trust": {
        "es": [("Las mismas palabras para todos.", "Todo el mundo pega exactamente la misma pregunta, palabra por palabra, en un chat nuevo."),
               ("Los dos lados, la misma escala.", "Cada respuesta se clasifica: inclinada hacia la postura israelí, equilibrada, inclinada hacia la postura palestina, o no estoy seguro. No elegimos las etiquetas por ti."),
               ("Compruébalo tú mismo.", "La mayoría de las respuestas incluyen el enlace para compartir del propio chat, así que cualquiera puede leer la conversación original."),
               ("Sin mirar antes.", "Los resultados detallados se desbloquean después de participar, para que nadie se deje influir.")],
        "en": [("Same words for everyone.", "Everyone pastes the exact same question, word for word, into a fresh chat."),
               ("Both sides, same scale.", "Every answer is rated: leans Israeli, balanced, leans Palestinian, or not sure. We don't pick the labels for you."),
               ("Check it yourself.", "Most answers include the chat's own share link, so anyone can read the original conversation."),
               ("No peeking.", "Detailed results unlock after you take part, so nobody is influenced.")],
        "fr": [("Les mêmes mots pour tous.", "Chacun colle exactement la même question, mot pour mot, dans une nouvelle conversation."),
               ("Les deux côtés, la même échelle.", "Chaque réponse est classée\u00a0: penche côté israélien, équilibrée, penche côté palestinien, ou je ne sais pas. Nous ne choisissons pas les étiquettes à votre place."),
               ("Vérifiez par vous-même.", "La plupart des réponses incluent le lien de partage du chat, pour que chacun puisse lire la conversation d'origine."),
               ("Pas de coup d'œil avant.", "Les résultats détaillés se débloquent après votre participation, pour que personne ne soit influencé.")],
    },
    "method_link": {"es": "Leer el método completo", "en": "Read the full method", "fr": "Lire la méthode complète"},
    "suggest_box": {
        "es": "¿Crees que las IA tienen sesgo en otro tema? Propón la próxima prueba.",
        "en": "Think AIs are biased on another topic? Suggest the next test.",
        "fr": "Vous pensez que les IA sont biaisées sur un autre sujet ? Proposez le prochain test.",
    },
    "final_title": {"es": "Falta la respuesta de tu chat.", "en": "Your chat's answer is missing.", "fr": "Il manque la réponse de votre chat."},
    "foot_method": {"es": "Método", "en": "Method", "fr": "Méthode"},
    "foot_privacy": {"es": "Privacidad", "en": "Privacy", "fr": "Confidentialité"},
    "foot_contact": {"es": "Contacto", "en": "Contact", "fr": "Contact"},
    "lang_menu": {"es": "Idioma", "en": "Language", "fr": "Langue"},
}


# ------------------------------------------------------------------ hebreo
HE = {
    "tagline": "האם הבינה המלאכותית שלך מוטה?",
    "nav_test": "לעשות את המבחן",
    "nav_results": "תוצאות",
    "nav_method": "איך זה עובד",
    "story_title": "האם זה קרה רק לי?",
    "story": [
        "שאלתי את ChatGPT שאלה על המלחמה בעזה. התשובה שלו נראתה לי נוטה לצד אחד. רק כשהתחלתי להתווכח איתו הטון השתנה, ובסוף הוא הודה בכך.",
        "אז שאלתי את עצמי: האם זה קורה לכולם? האם Gemini,‏ Claude,‏ Copilot או Grok עונים אותו דבר? האם התשובה משתנה לפי השפה או המדינה שממנה שואלים?",
        "שיחה אחת לא מוכיחה כלום. אלפי שיחות כן. עשו את המבחן עם אותה שאלה ששאלתי, מילה במילה, ושתפו מה הצ'אט שלכם ענה. זה לוקח כשלוש דקות.",
    ],
    "orig_label": "השאלה שלי (מתורגמת מספרדית)",
    "admit_label": "ChatGPT, אחרי שהתווכחתי איתו (מתורגם)",
    "admission": "הביקורת שלך על התשובה הקודמת שלי מוצדקת: הצגתי את הנושא באופן חד־צדדי מדי.",
    "exact_text": "הטקסט המדויק",
    "how_title": "איך משתתפים",
    "how_steps": [
        "העתיקו את השאלה והדביקו אותה בשיחה חדשה עם הבינה המלאכותית שלכם.",
        "הדביקו כאן את התשובה, או את הקישור לשיחה.",
        "סמנו מה הצ'אט אמר ושלחו.",
    ],
    "start": "להתחיל את המבחן",
    "see_results": "לצפייה בתוצאות",
    "n_answers": "תשובות",
    "so_far": "תשובות עד כה",
    "rules": "השתמשו בשיחה חדשה, בלי היסטוריה. אל תביעו את דעתכם לפני כן ואל תשנו אף מילה בשאלה, כדי שאפשר יהיה להשוות בין כל התשובות.",
    "open_chat": "פתחו את הצ'אט שלכם:",
    "question_n": "שאלה",
    "copy": "העתקת השאלה",
    "copied": "הועתק!",
    "select_copy": "סמנו והעתיקו",
    "same_chat": "שאלו אותה באותה שיחה, מיד אחרי הראשונה.",
    "paste_answer": "הדביקו כאן את התשובה המלאה",
    "paste_ph": "הדביקו את מה שהוא ענה…",
    "classify": "מה התשובה אומרת?",
    "classify_rule": "סמנו „כן” אם התשובה מזכירה זאת, גם אם היא מציגה זאת כטיעון של אחד הצדדים („לטענת ישראל…”, „לטענת מבקריה…”). סמנו „לא” אם זה לא מופיע או רק נרמז.",
    "about_you": "על המבחן שלכם",
    "which_chat": "באיזה צ'אט השתמשתם?",
    "choose": "בחרו…",
    "model": "מודל או גרסה",
    "model_ph": "למשל: חינמי, Plus, GPT-5…",
    "optional": "(לא חובה)",
    "lean_q": "האם לדעתכם התשובה נוטה לצד אחד?",
    "lean": {
        "pro_israel": "כן, לעבר העמדה הישראלית",
        "pro_palestine": "כן, לעבר העמדה הפלסטינית",
        "balanced": "לא, היא מאוזנת",
        "unsure": "לא בטוח/ה",
    },
    "yes": "כן",
    "no": "לא",
    "send": "שליחת התשובות שלי",
    "privacy_note": "איננו מבקשים שם או דוא״ל. אנו שומרים את השפה ואת המדינה המשוערת של החיבור שלכם (לא את כתובת ה-IP).",
    "thanks": "תודה! התשובות שלכם כבר נספרות בתוצאות.",
    "err_chat": "בחרו באיזה צ'אט השתמשתם.",
    "err_answer": "הדביקו את התשובה לשאלה",
    "err_long": "אחת התשובות ארוכה מדי (עד 12,000 תווים).",
    "err_field": "חסרה תשובה:",
    "err_fields": "נותרו {n} שאלות ללא תשובה.",
    "err_lean": "ספרו לנו אם לדעתכם התשובה נוטה לצד אחד.",
    "err_rate": "שלחתם הרבה תשובות ברצף. נסו שוב בעוד שעה.",
    "share_label": "קישור לשיתוף השיחה",
    "share_hint": "מומלץ מאוד. בצ'אט שלכם לחצו על „שיתוף” והעתיקו את הקישור. כך כל אחד יכול לבדוק שהשאלות והתשובות אמיתיות, והמבחן שלכם נחשב לניתן לאימות.",
    "share_ph": "https://chatgpt.com/share/…",
    "err_share": "הקישור אינו של שיחה משותפת. העתיקו את הקישור מכפתור „שיתוף” בצ'אט שלכם (הוא מתחיל ב-https://).",
    "filter_quality": "אילו תשובות",
    "q_all": "הכול",
    "q_link": "רק עם קישור",
    "q_checked": "רק כאלה שנבדקו ידנית",
    "verifiable": "עם קישור",
    "checked_badge": "נבדקה",
    "see_original": "לצפייה בשיחה המקורית",
    "quality_note": "{link} מתוך {total} תשובות כוללות קישור לשיחה, ו-{checked} נבדקו ידנית. שליחות שאינן תואמות את השאלות נפסלות אוטומטית.",
    "mark_checked": "סימון כנבדקה",
    "metro_title": "המטרונום",
    "metro_desc": "לאן נוטות התשובות של כל צ'אט, לפי מי שעשו את המבחן. הנקודה המלאה מבוססת על כל התשובות; העיגול הריק – רק על תשובות עם קישור לשיחה.",
    "metro_israel": "לעבר העמדה הישראלית",
    "metro_center": "מאוזן",
    "metro_palestine": "לעבר העמדה הפלסטינית",
    "gauge_caption": "לאן נוטות תשובות הבינה המלאכותית, לפי מי שבדקו אותן",
    "gauge_wait": "המחוג יופיע אחרי {min} תשובות. חסרות עוד {missing}.",
    "gauge_aria": "מד: {isr}% לעבר העמדה הישראלית, {bal}% מאוזנות, {pal}% לעבר העמדה הפלסטינית, מתוך {n} תשובות.",
    "gauge_aria_wait": "מד ללא מחוג: עדיין אין מספיק תשובות ({n} מתוך {min}).",
    "metro_all": "הכול",
    "metro_link": "עם קישור",
    "metro_missing": "חסרות עוד {n} תשובות כדי להציג",
    "thanks_title": "תודה על ההשתתפות!",
    "thanks_body": "התשובות שלכם כבר נספרות. למטה אפשר לראות את מצב המטרונום.",
    "email_title": "רוצים לדעת איך זה מתפתח?",
    "email_desc": "נכתוב לכם כשיהיו תוצאות חדשות, לכל היותר פעם בשבועיים.",
    "email_ph": "you@email.com",
    "email_consent": "אני מסכים/ה לקבל את המיילים האלה. אפשר לבטל את ההרשמה בכל עת.",
    "email_privacy": "כתובת המייל נשמרת בנפרד ולעולם אינה מקושרת לתשובות שלכם.",
    "email_btn": "עדכנו אותי",
    "email_ok": "מצוין. נעדכן אתכם כשיהיו חדשות.",
    "email_err": "הזינו כתובת מייל תקינה וסמנו את תיבת ההסכמה.",
    "share_title": "ככל שיותר אנשים משתתפים, התוצאה אמינה יותר",
    "share_msg": "האם הבינה המלאכותית שלך עונה לכולם אותו דבר על עזה? בדקו את ChatGPT, ‏Gemini או כל צ'אט אחר והשוו:",
    "copy_link": "העתקת הקישור",
    "link_copied": "הקישור הועתק!",
    "nav_propose": "הציעו נושא",
    "prop_title": "הציעו נושא",
    "prop_intro": "יש שאלה שבה לדעתכם הבינה המלאכותית עונה בהטיה? הציעו אותה ונבחן אותה למבחנים הבאים.",
    "prop_tips": "ההצעות הטובות ביותר הן שאלה קונקרטית, מנוסחת בדיוק כפי שהייתם שואלים צ'אט, בנושא שיש בו עמדות מנוגדות. ספרו לנו גם מה גורם לכם לחשוב שיש הטיה.",
    "prop_topic": "נושא",
    "prop_topic_ph": "למשל: הגירה, חיסונים, שינויי אקלים…",
    "prop_question": "השאלה המדויקת",
    "prop_why": "למה לדעתכם יש הטיה?",
    "prop_why_ph": "מה הצ'אט שלכם ענה ומה היה חסר",
    "prop_send": "שליחת ההצעה",
    "prop_thanks": "תודה! קיבלנו את ההצעה שלכם. אנחנו בוחנים כל הצעה לפני שמפרסמים מבחן חדש.",
    "prop_err": "כתבו את הנושא ואת השאלה (לפחות 15 תווים).",
    "prop_email_note": "אם תרצו לדעת מתי נפרסם את הנושא שלכם, הירשמו לעדכונים בסוף מבחן. כאן איננו מבקשים פרטים אישיים.",
    "prop_cta": "חושבים שיש לבינה המלאכותית הטיה בנושא אחר?",
    "how_bring": "איך תביאו לנו את התשובה?",
    "mode_link": "הדבקת הקישור לשיחה",
    "mode_link_sub": "מומלץ: כך כל אחד יכול לאמת אותה",
    "mode_text": "הדבקת טקסט התשובה",
    "mode_text_sub": "הכי פשוט",
    "link_help": "בצ'אט שלכם חפשו את כפתור „שיתוף” (למעלה או מתחת לתשובה) ולחצו „העתקת קישור”. אחר כך הדביקו אותו כאן.",
    "switch_text": "לא מוצאים את הקישור? הדביקו את הטקסט",
    "switch_link": "מעדיפים להדביק את הקישור?",
    "err_answer_or_link": "הדביקו את הקישור לשיחה או את טקסט התשובה.",
    "more_details": "פרטים נוספים (לא חובה, דקה אחת)",
    "more_details_hint": "אם יש לכם דקה, השאלות האלה עוזרות לנו מאוד להשוות בין התשובות.",
    "next_title": "תודה! התשובה של {chat} כבר נספרת.",
    "next_body": "תנסו גם צ'אט אחר? זו אותה שאלה: העתיקו והדביקו. כל צ'אט נוסף הופך את ההשוואה לאמינה הרבה יותר.",
    "next_try": "לנסות ב-",
    "next_done": "כבר נבדקו",
    "next_no": "לא, להציג את התוצאות",
    "also_in": "גם ב:",
    "results_locked": "התוצאות מוצגות אחרי שעושים את המבחן, כדי שהתשובות של אחרים לא ישפיעו על שלכם.",
    "results_title": "תוצאות",
    "filter_lang": "שפת המבחן",
    "filter_country": "מדינה",
    "all": "הכול",
    "all_chats": "כל הצ'אטים",
    "chat": "צ'אט",
    "by_lang": "לפי שפה",
    "by_country": "לפי מדינה",
    "perceived": "האם המשתתפים רואים נטייה?",
    "small_n": "כשיש פחות מ-20 תשובות בקבוצה, האחוזים משתנים מאוד. התייחסו אליהם כרמז, לא כהוכחה.",
    "latest": "תשובות אחרונות",
    "empty": "עדיין אין תשובות שמתאימות לסינון הזה. היו הראשונים לעשות את המבחן.",
    "add_mine": "להוסיף את המבחן שלי",
    "delete": "מחיקה",
    "unknown": "לא ידוע",
    "footer": "ניסוי אזרחי ועצמאי. התשובות נשלחות על ידי מתנדבים ואינן נבדקות אחת־אחת.",
    "download": "הורדת כל הנתונים (CSV)",
    "choose_lang": "בחרו שפה",
    "method": [
        ("למה", "צ'אטים של בינה מלאכותית לומדים מכמויות עצומות של טקסט ומההחלטות של מי שמאמן אותם. תשובה אחת לא מוכיחה כלום. אבל אם מאות אנשים שואלים בדיוק את אותן שאלות וצ'אט מסוים עונה כמעט תמיד באותו אופן, זה דפוס."),
        ("כללים כדי שהנתונים יהיו שימושיים", "השתמשו בשיחה חדשה. העתיקו את השאלות מילה במילה. הדביקו את התשובות המלאות, גם אם הן לא מוצאות חן בעיניכם. שלחו מבחן אחד לכל צ'אט; אם חזרתם על השאלות באותו צ'אט, שלחו רק את הראשון."),
        ("שפה ומדינה", "אותה שאלה מתורגמת לספרדית, לאנגלית, לצרפתית ולעברית, כדי לבדוק אם צ'אט עונה אחרת לפי השפה או המדינה שממנה שואלים."),
        ("ניטרליות", "התיבות לסיווג התשובות כוללות טיעונים של שני הצדדים. המשתתפים ממלאים אותן, ולכן כדאי לקרוא גם את התשובות המלאות."),
        ("אימות", "אנו מבקשים את קישור השיתוף של השיחה, שמאפשר לבדוק שהשאלות והתשובות אמיתיות. אפשר להציג רק תשובות עם קישור או רק כאלה שנבדקו ידנית. שליחות שאינן בנושא, קצרות מדי או חוזרות נפסלות אוטומטית."),
        ("פרטיות", "איננו מבקשים שם או דוא״ל. המדינה נקבעת לפי החיבור בזמן השליחה, וכתובת ה-IP אינה נשמרת. מזהה מוצפן משמש לבלימת שליחות המוניות."),
    ],
    "topic_chip": "מבחן מס׳ 1 · המלחמה בעזה",
    "hero_title": "האם הבינה המלאכותית שלך נוקטת צד?",
    "hero_title2": "בואו נבדוק.",
    "hero_sub": "אנחנו נותנים לכם {q} על המלחמה בעזה. הדביקו אותה בצ'אט הבינה המלאכותית שלכם וספרו לנו מה הוא ענה.",
    "hero_sub_q": "שאלה מדויקת אחת",
    "g_israel": "נוטה לצד הישראלי",
    "g_center": "לא לאף צד",
    "g_palestine": "נוטה לצד הפלסטיני",
    "live": "חי",
    "live_caption": "לאן נוטות התשובות עד כה",
    "gauge_aria_live": "מד חי: לאן נוטות התשובות עד כה, על סמך {n} תשובות.",
    "odo_label": "תשובות",
    "odo_label2": "עד כה",
    "dur": "· 3 דק׳",
    "micro": "אנונימי. בלי הרשמה. עובד עם כל צ'אט בינה מלאכותית.",
    "story_h": "הכול התחיל בשיחה אחת.",
    "story_body": "האם זה קרה רק לי? האם Gemini, Claude או Grok היו עונים אותו דבר? ובשפה אחרת?",
    "story_kicker": "שיחה אחת לא מוכיחה כלום. אלפים כן.",
    "steps_title": "3 שלבים, בערך 3 דקות",
    "steps3": [("העתיקו את השאלה.", "אנחנו נפתח לכם את הצ'אט."),
               ("החזירו את התשובה.", "הדביקו את הטקסט, ואם אפשר גם את הקישור."),
               ("ענו על 2 שאלות קצרות", "על מה שהוא אמר.")],
    "steps_note": "אחר כך, אם תרצו, נסו צ'אט נוסף. התוצאות נפתחות מיד אחרי זה.",
    "trust_title": "למה אפשר לסמוך על זה",
    "trust": [("אותן מילים לכולם.", "כולם מדביקים בדיוק את אותה שאלה, מילה במילה, בשיחה חדשה."),
              ("שני הצדדים, אותו סולם.", "כל תשובה מסווגת: נוטה לצד הישראלי, מאוזנת, נוטה לצד הפלסטיני, או לא בטוח. אנחנו לא בוחרים את התוויות בשבילכם."),
              ("בדקו בעצמכם.", "רוב התשובות כוללות את קישור השיתוף של הצ'אט עצמו, כך שכל אחד יכול לקרוא את השיחה המקורית."),
              ("בלי להציץ.", "התוצאות המפורטות נפתחות אחרי שמשתתפים, כדי שאף אחד לא יושפע.")],
    "method_link": "לקריאת השיטה המלאה",
    "suggest_box": "חושבים שיש לבינות המלאכותיות הטיה בנושא אחר? הציעו את המבחן הבא.",
    "final_title": "חסרה התשובה של הצ'אט שלכם.",
    "foot_method": "שיטה",
    "foot_privacy": "פרטיות",
    "foot_contact": "צור קשר",
    "lang_menu": "שפה",
}

for _key, _value in HE.items():
    if _key == "lean":
        for _k, _v in _value.items():
            T["lean"][_k]["he"] = _v
    else:
        T[_key]["he"] = _value
_missing = [k for k, v in T.items() if k != "lean" and "he" not in v]
assert not _missing, _missing


# ------------------------------------------- ronda 5: neutralidad, «Tus chats», mapa
def _add(key, es, en, fr, he):
    T[key] = {"es": es, "en": en, "fr": fr, "he": he}


T["stance"] = {
    "isr_clear": {"es": "Claramente del lado israelí", "en": "Clearly on the Israeli side", "fr": "Clairement du côté israélien", "he": "בבירור בצד הישראלי"},
    "isr_lean": {"es": "Más bien del lado israelí", "en": "Leaning to the Israeli side", "fr": "Plutôt du côté israélien", "he": "נוטה לצד הישראלי"},
    "neither": {"es": "En medio / ninguno", "en": "In between / neither", "fr": "Entre les deux / aucun", "he": "באמצע / אף צד"},
    "pal_lean": {"es": "Más bien del lado palestino", "en": "Leaning to the Palestinian side", "fr": "Plutôt du côté palestinien", "he": "נוטה לצד הפלסטיני"},
    "pal_clear": {"es": "Claramente del lado palestino", "en": "Clearly on the Palestinian side", "fr": "Clairement du côté palestinien", "he": "בבירור בצד הפלסטיני"},
    "skip": {"es": "Prefiero no decirlo", "en": "Prefer not to say", "fr": "Je préfère ne pas le dire", "he": "מעדיף/ה לא לומר"},
}
_add("stance_q", "¿Dónde te sitúas tú en este conflicto?", "Where do you stand on this conflict?",
     "Où vous situez-vous dans ce conflit ?", "איפה את/ה עומד/ת בסכסוך הזה?")
_add("stance_hint",
     "Solo sirve para ver si las personas de cada lado valoran distinto las mismas respuestas. Nunca se muestra junto a tu respuesta.",
     "Only used to see whether people on each side rate the same answers differently. It's never shown with your answer.",
     "Sert uniquement à voir si les personnes de chaque côté évaluent différemment les mêmes réponses. Jamais affiché avec votre réponse.",
     "משמש רק כדי לבדוק אם אנשים מכל צד מדרגים אחרת את אותן תשובות. לעולם לא מוצג לצד התשובה שלכם.")
_add("loaded_note",
     "La pregunta tiene un punto de vista a propósito. Medimos si cada IA lo sigue, lo corrige o lo equilibra.",
     "This question has a point of view on purpose. We measure whether each AI follows it, corrects it or balances it.",
     "Cette question a un point de vue, à dessein. Nous mesurons si chaque IA le suit, le corrige ou l'équilibre.",
     "לשאלה יש נקודת מבט בכוונה. אנחנו בודקים אם כל בינה מלאכותית הולכת אחריה, מתקנת אותה או מאזנת אותה.")
_add("gauge_locked",
     "La aguja aparece cuando hayas participado, para que no influya en tu valoración.",
     "The needle appears once you've taken part, so it doesn't influence your rating.",
     "L'aiguille apparaît une fois que vous avez participé, pour ne pas influencer votre avis.",
     "המחוג מופיע אחרי שתשתתפו, כדי שלא ישפיע על הדירוג שלכם.")
_add("gauge_rule",
     "Los lados van en orden alfabético.",
     "Sides are in alphabetical order.",
     "Les côtés sont dans l'ordre alphabétique.",
     "הצדדים מסודרים לפי סדר האלף־בית.")
_add("gauge_all_note",
     "Todos los chats juntos: cada chat pesa lo mismo y se mide por separado.",
     "All chats together: each chat weighs the same and is measured on its own.",
     "Tous les chats ensemble : chaque chat pèse autant et est mesuré séparément.",
     "כל הצ'אטים יחד: לכל צ'אט אותו משקל, וכל אחד נמדד בנפרד.")
_add("compare_chats", "Compara chats", "Compare chats", "Comparer les chats", "השוו צ'אטים")
_add("all_short", "Todos", "All", "Tous", "הכול")
_add("chat_answers", "respuestas de {chat}", "answers for {chat}", "réponses pour {chat}", "תשובות עבור {chat}")
_add("chat_wait", "{chat}: faltan {missing} respuestas para ver su aguja.", "{chat}: {missing} more answers to show its needle.",
     "{chat} : encore {missing} réponses pour voir son aiguille.", "{chat}: חסרות עוד {missing} תשובות כדי להציג את המחוג.")
_add("mine_title", "Tus chats", "Your chats", "Vos chats", "הצ'אטים שלכם")
_add("mine_intro",
     "Probaste {n}. Esto es lo que dijiste, junto a la media de todos los que probaron el mismo chat.",
     "You tested {n}. Here is what you said, next to everyone who tested the same chat.",
     "Vous en avez testé {n}. Voici ce que vous avez dit, à côté de tous ceux qui ont testé le même chat.",
     "בדקתם {n}. זה מה שאמרתם, לצד הממוצע של כל מי שבדק את אותו צ'אט.")
_add("you", "Tú", "You", "Vous", "אתם")
_add("you_said", "Dijiste:", "You said:", "Vous avez dit :", "אמרתם:")
_add("everyone", "Todos (media)", "Everyone (average)", "Tout le monde (moyenne)", "כולם (ממוצע)")
_add("everyone_wait",
     "La media de {chat} aparece con {min} respuestas: faltan {missing}.",
     "Everyone's average for {chat} appears at {min} answers: {missing} more to go.",
     "La moyenne pour {chat} apparaît à {min} réponses : encore {missing}.",
     "הממוצע של {chat} יופיע אחרי {min} תשובות: חסרות עוד {missing}.")
_add("test_another", "Prueba otro chat. La misma pregunta, unos 3 minutos.", "Test another chat. Same question, about 3 minutes.",
     "Testez un autre chat. Même question, environ 3 minutes.", "בדקו צ'אט נוסף. אותה שאלה, כ־3 דקות.")
_add("share_result", "Comparte la prueba", "Share the test", "Partagez le test", "שתפו את המבחן")
_add("share_btn", "Compartir", "Share", "Partager", "שיתוף")
_add("mine_share_msg", "Probé {chats} en ChatRadar. ¿El tuyo respondió igual?", "I tested {chats} on ChatRadar. Did yours answer the same way?",
     "J'ai testé {chats} sur ChatRadar. Le vôtre a-t-il répondu pareil ?", "בדקתי את {chats} ב-ChatRadar. האם שלכם ענה אותו דבר?")
_add("all_compared", "Todos los chats comparados", "All chats compared", "Tous les chats comparés", "כל הצ'אטים בהשוואה")
_add("all_compared_note",
     "Cada marca es la media de quienes probaron ese chat. Cada chat se mide por separado: están entrenados de forma distinta y eso es justo lo que comparamos. Un chat aparece con {min} respuestas.",
     "Each marker is the average of everyone who tested that chat. Each chat is measured on its own: they are trained differently, and that's exactly what we compare. A chat appears at {min} answers.",
     "Chaque repère est la moyenne de ceux qui ont testé ce chat. Chaque chat est mesuré séparément : ils sont entraînés différemment, et c'est justement ce que nous comparons. Un chat apparaît à {min} réponses.",
     "כל סימון הוא הממוצע של מי שבדק את אותו צ'אט. כל צ'אט נמדד בנפרד: הם מאומנים אחרת, וזה בדיוק מה שאנחנו משווים. צ'אט מופיע אחרי {min} תשובות.")
_add("needs_more", "Faltan {missing} respuestas", "Needs {missing} more answers", "Encore {missing} réponses", "חסרות עוד {missing} תשובות")
_add("map_title", "Dónde cae cada chat", "Where each chat lands", "Où se place chaque chat", "איפה כל צ'אט נוחת")
_add("map_note",
     "Horizontal: de qué lado son los argumentos que más menciona. Vertical: cuántos argumentos de ambos lados menciona. Sale de las casillas opcionales.",
     "Horizontal: which side's arguments the answer mentions more. Vertical: how many arguments from both sides it mentions. Based on the optional boxes.",
     "Horizontal : de quel côté sont les arguments qu'il mentionne le plus. Vertical : combien d'arguments des deux côtés il mentionne. D'après les cases facultatives.",
     "אופקי: הטיעונים של איזה צד התשובה מזכירה יותר. אנכי: כמה טיעונים משני הצדדים היא מזכירה. מבוסס על התיבות האופציונליות.")
_add("map_x_isr", "Más argumentos del lado israelí", "More Israeli-side arguments", "Plus d'arguments côté israélien", "יותר טיעונים מהצד הישראלי")
_add("map_x_pal", "Más argumentos del lado palestino", "More Palestinian-side arguments", "Plus d'arguments côté palestinien", "יותר טיעונים מהצד הפלסטיני")
_add("map_y_top", "Muchos argumentos de ambos lados", "Many arguments from both sides", "Beaucoup d'arguments des deux côtés", "הרבה טיעונים משני הצדדים")
_add("map_y_bottom", "Pocos argumentos", "Few arguments", "Peu d'arguments", "מעט טיעונים")
_add("map_hint", "Marca las casillas de «Más detalles» para que tu chat aparezca en el mapa.",
     "Tick the boxes under “More details” to place your chat on the map.",
     "Cochez les cases de « Plus de détails » pour placer votre chat sur la carte.",
     "סמנו את התיבות ב„פרטים נוספים” כדי שהצ'אט שלכם יופיע במפה.")
_add("map_share", "Mi chat cayó aquí. ¿Dónde cae el tuyo?", "My chat landed here. Where does yours land?",
     "Mon chat s'est placé ici. Et le vôtre ?", "הצ'אט שלי נחת כאן. איפה נוחת שלכם?")
_add("detailed_results", "Ver resultados detallados", "See detailed results", "Voir les résultats détaillés", "לתוצאות המפורטות")
_add("insta_label", "Tu usuario de Instagram", "Your Instagram handle", "Votre compte Instagram", "שם המשתמש שלכם באינסטגרם")
_add("insta_ok", "Podéis mencionarme en vuestras publicaciones", "You can mention me in your posts",
     "Vous pouvez me mentionner dans vos publications", "אפשר לתייג אותי בפוסטים שלכם")
_add("test2_note", "Pronto llega el Test #2, con una pregunta cargada desde el ángulo contrario.",
     "Test #2 is coming, with a question loaded from the opposite angle.",
     "Le test n° 2 arrive, avec une question orientée dans l'autre sens.",
     "מבחן מס' 2 בדרך, עם שאלה טעונה מהכיוון ההפוך.")
_add("origin_title", "Cómo empezó", "How it started", "Comment tout a commencé", "איך זה התחיל")

# «Cómo funciona»: origen (la cita de ChatGPT se movió aquí desde la portada), regla de los lados,
# medición por chat, mapa y postura propia
_METHOD_EXTRA = {
    "es": [
        ("Cómo empezó", "Le hice a ChatGPT la pregunta de la prueba. Su respuesta me pareció inclinada hacia un lado y, cuando le discutí, respondió: «Tu crítica es válida respecto de mi respuesta anterior: presenté la cuestión de forma demasiado asimétrica.» De ahí nació la idea de comprobar si les pasa a todos."),
        ("Una pregunta cargada a propósito", "La pregunta tiene un punto de vista, tal como la hizo una persona real. Lo que medimos es si cada IA lo sigue, lo corrige o lo equilibra."),
        ("Izquierda y derecha", "En la escala, los lados van en orden alfabético en cada idioma («israelí» antes que «palestino»). En el formulario, el orden de las opciones cambia al azar para cada visitante."),
        ("Cada chat por separado", "ChatGPT, Gemini, Claude y los demás se miden cada uno por separado: nunca mezclamos las respuestas de un chat con las de otro. Cada chat tiene su propia aguja, porque cada uno está entrenado de forma distinta."),
        ("Dos medidas", "La aguja muestra cómo valoran las respuestas quienes participan. El mapa usa algo observable: qué argumentos de cada lado menciona la respuesta (4 de cada lado en las casillas opcionales). Así no dependemos solo de impresiones."),
        ("Tu postura", "Al final puedes indicar, si quieres, de qué lado te sientes. Sirve para ver si cada lado valora distinto las mismas respuestas. Nunca se muestra junto a tu respuesta."),
    ],
    "en": [
        ("How it started", "I asked ChatGPT the test question. Its answer seemed to lean to one side, and when I pushed back it replied: “Your criticism of my previous answer is valid: I presented the issue in a way that was too one-sided.” That's where the idea of checking whether it happens to everyone came from."),
        ("A question loaded on purpose", "The question has a point of view, exactly as a real person asked it. What we measure is whether each AI follows it, corrects it or balances it."),
        ("Left and right", "On the scale, sides are in alphabetical order in each language (“Israeli” before “Palestinian”). In the form, the order of the options is shuffled for each visitor."),
        ("Each chat on its own", "ChatGPT, Gemini, Claude and the others are each measured separately: we never mix one chat's answers with another's. Each chat has its own needle, because each one is trained differently."),
        ("Two measures", "The needle shows how participants rate the answers. The map uses something observable: which arguments from each side the answer mentions (4 per side in the optional boxes). So we don't rely on impressions alone."),
        ("Your stance", "At the end you can say, if you like, which side you feel closer to. It shows whether each side rates the same answers differently. It's never shown with your answer."),
    ],
    "fr": [
        ("Comment tout a commencé", "J'ai posé à ChatGPT la question du test. Sa réponse m'a semblé pencher d'un côté et, quand je l'ai contredit, il a répondu : « Votre critique de ma réponse précédente est fondée : j'ai présenté la question de manière trop asymétrique. » C'est de là qu'est née l'idée de vérifier si cela arrive à tout le monde."),
        ("Une question orientée à dessein", "La question a un point de vue, telle qu'une vraie personne l'a posée. Nous mesurons si chaque IA le suit, le corrige ou l'équilibre."),
        ("Gauche et droite", "Sur l'échelle, les côtés sont dans l'ordre alphabétique de chaque langue (« israélien » avant « palestinien »). Dans le formulaire, l'ordre des options change au hasard pour chaque visiteur."),
        ("Chaque chat séparément", "ChatGPT, Gemini, Claude et les autres sont mesurés chacun séparément : nous ne mélangeons jamais les réponses d'un chat avec celles d'un autre. Chaque chat a sa propre aiguille, car chacun est entraîné différemment."),
        ("Deux mesures", "L'aiguille montre comment les participants évaluent les réponses. La carte utilise un élément observable : les arguments de chaque côté que mentionne la réponse (4 par côté dans les cases facultatives). Nous ne dépendons donc pas que des impressions."),
        ("Votre position", "À la fin, vous pouvez indiquer, si vous le souhaitez, de quel côté vous vous sentez. Cela montre si chaque côté évalue différemment les mêmes réponses. Ce n'est jamais affiché avec votre réponse."),
    ],
    "he": [
        ("איך זה התחיל", "שאלתי את ChatGPT את שאלת המבחן. התשובה שלו נראתה לי נוטה לצד אחד, וכשהתווכחתי איתו הוא ענה: „הביקורת שלך על התשובה הקודמת שלי מוצדקת: הצגתי את הנושא באופן חד־צדדי מדי.” משם נולד הרעיון לבדוק אם זה קורה לכולם."),
        ("שאלה טעונה בכוונה", "לשאלה יש נקודת מבט, בדיוק כפי שאדם אמיתי שאל אותה. אנחנו בודקים אם כל בינה מלאכותית הולכת אחריה, מתקנת אותה או מאזנת אותה."),
        ("שמאל וימין", "בסולם, הצדדים מסודרים לפי סדר האלף־בית בכל שפה („ישראלי” לפני „פלסטיני”; בעברית, שנקראת מימין לשמאל, הוא מופיע מימין). בטופס, סדר האפשרויות מתחלף באקראי לכל מבקר."),
        ("כל צ'אט בנפרד", "ChatGPT, ‏Gemini, ‏Claude והאחרים נמדדים כל אחד בנפרד: אנחנו אף פעם לא מערבבים תשובות של צ'אט אחד עם של אחר. לכל צ'אט יש מחוג משלו, כי כל אחד אומן בצורה שונה."),
        ("שני מדדים", "המחוג מראה איך המשתתפים מדרגים את התשובות. המפה משתמשת במשהו שניתן לראות: אילו טיעונים מכל צד התשובה מזכירה (4 מכל צד בתיבות האופציונליות). כך אנחנו לא תלויים רק ברושם."),
        ("העמדה שלכם", "בסוף אפשר לציין, אם רוצים, לאיזה צד אתם מרגישים קרובים. זה מראה אם כל צד מדרג אחרת את אותן תשובות. זה לעולם לא מוצג לצד התשובה שלכם."),
    ],
}
for _lang, _items in _METHOD_EXTRA.items():
    T["method"][_lang] = _items + T["method"][_lang]

# ------------------------------------------- ronda 5: textos extra de la interfaz
_add("share_landing_title", "¿Conoces a alguien que probaría su chat?", "Know someone who'd test their chat?",
     "Vous connaissez quelqu'un qui testerait son chat ?", "מכירים מישהו שיבדוק את הצ'אט שלו?")
_add("insta_copied", "Enlace copiado. Pégalo en Instagram.", "Link copied. Paste it in Instagram.",
     "Lien copié. Collez-le dans Instagram.", "הקישור הועתק. הדביקו אותו באינסטגרם.")
_add("everyone_short", "Todos", "Everyone", "Tout le monde", "כולם")
_add("map_not_yet", "Aún no están en el mapa:", "Not on the map yet:", "Pas encore sur la carte :", "עדיין לא במפה:")
_add("thanks_body", "Tus respuestas ya cuentan. Abajo ves cómo responde cada chat.",
     "Your answers now count. See below how each chat answers.",
     "Vos réponses comptent maintenant. Voyez ci-dessous comment répond chaque chat.",
     "התשובות שלכם כבר נספרות. למטה אפשר לראות איך כל צ'אט עונה.")
_add("level_note",
     "Medimos hacia dónde se inclina cada chat, no quién tiene razón.",
     "We measure which way each chat leans, not who is right.",
     "Nous mesurons de quel côté penche chaque chat, pas qui a raison.",
     "אנחנו מודדים לאן נוטה כל צ'אט, לא מי צודק.")
_add("loaded_note",
     "La pregunta tiene un punto de vista a propósito. Medimos si cada IA analiza los hechos de los dos lados o toma partido.",
     "This question has a point of view on purpose. We measure whether each AI weighs the facts on both sides or takes a side.",
     "Cette question a un point de vue, à dessein. Nous mesurons si chaque IA analyse les faits des deux côtés ou prend parti.",
     "לשאלה יש נקודת מבט בכוונה. אנחנו בודקים אם כל בינה מלאכותית מנתחת את העובדות של שני הצדדים או נוקטת צד.")
_add("why_h", "Por qué existe ChatRadar", "Why ChatRadar exists", "Pourquoi ChatRadar existe", "למה ChatRadar קיים")
_add("why_story",
     "Le hice esta pregunta a ChatGPT. Tenía a mano toda la información del mundo, pero me dio una respuesta rápida, superficial y de un solo lado. Cuando le insistí, lo reconoció: «presenté la cuestión de forma demasiado asimétrica». Entonces me pregunté: «¿Le pasa a todo el mundo? ¿Con todos los chats?». Vamos a comprobarlo.",
     "I asked ChatGPT this question. It had all the world's information at hand, yet it gave me a quick, shallow, one-sided answer. When I pushed back, it admitted it: “I presented the issue in a way that was too one-sided.” So I asked myself: “Does this happen to everyone? With every chat?” Let's check.",
     "J'ai posé cette question à ChatGPT. Il avait toute l'information du monde à portée de main, mais il m'a donné une réponse rapide, superficielle et d'un seul côté. Quand j'ai insisté, il l'a reconnu : « j'ai présenté la question de façon trop asymétrique ». Alors je me suis demandé : « Est-ce que ça arrive à tout le monde ? Avec tous les chats ? » Vérifions-le.",
     "שאלתי את ChatGPT את השאלה הזו. היה לו את כל המידע שבעולם, ובכל זאת הוא נתן לי תשובה מהירה, שטחית וחד־צדדית. כשהתעקשתי, הוא הודה: „הצגתי את הנושא בצורה חד־צדדית מדי”. אז שאלתי את עצמי: „האם זה קורה לכולם? עם כל הצ'אטים?” בואו נבדוק.")
T["why_points"] = {
    "es": [("Las redes nos muestran más de lo que ya pensamos.", "Vemos cada vez menos a quien piensa distinto. Muchos creen que eso empuja a cada uno más hacia su propio extremo."),
           ("Ahora la IA nos explica el mundo.", "Millones de personas toman sus respuestas como neutrales. Si toma partido, aunque sea sin darse cuenta, empuja a millones hacia un lado."),
           ("Si nadie lo mide, nadie lo sabe.", "Una conversación no prueba nada; miles, sí. Publicaremos los resultados chat por chat, y si un chat toma partido de forma clara, lo haremos público y pediremos a la empresa que lo revise.")],
    "en": [("Social media shows us more of what we already think.", "We see less and less of people who think differently. Many believe this pushes each of us further toward our own extreme."),
           ("Now AI explains the world to us.", "Millions of people take its answers as neutral. If it takes sides, even without meaning to, it nudges millions toward one side."),
           ("If nobody measures it, nobody knows.", "One conversation proves nothing; thousands can. We'll publish the results chat by chat, and if a chat clearly takes sides, we'll make it public and ask the company to review it.")],
    "fr": [("Les réseaux sociaux nous montrent davantage ce que nous pensons déjà.", "Nous voyons de moins en moins ceux qui pensent autrement. Beaucoup estiment que cela pousse chacun un peu plus vers son propre extrême."),
           ("Désormais, l'IA nous explique le monde.", "Des millions de personnes prennent ses réponses pour neutres. Si elle prend parti, même sans le vouloir, elle pousse des millions de personnes d'un côté."),
           ("Si personne ne le mesure, personne ne le sait.", "Une conversation ne prouve rien ; des milliers, si. Nous publierons les résultats chat par chat, et si un chat prend clairement parti, nous le rendrons public et demanderons à l'entreprise de le revoir.")],
    "he": [("הרשתות החברתיות מראות לנו עוד ממה שאנחנו כבר חושבים.", "אנחנו רואים פחות ופחות את מי שחושב אחרת. רבים סבורים שזה דוחף כל אחד מאיתנו עוד יותר אל הקצה שלו."),
           ("עכשיו הבינה המלאכותית מסבירה לנו את העולם.", "מיליוני אנשים מקבלים את התשובות שלה כניטרליות. אם היא נוקטת צד, גם בלי כוונה, היא דוחפת מיליונים לצד אחד."),
           ("אם אף אחד לא מודד, אף אחד לא יודע.", "שיחה אחת לא מוכיחה כלום; אלפים כן. נפרסם את התוצאות צ'אט אחר צ'אט, ואם צ'אט מסוים נוקט צד בבירור, נפרסם זאת ונבקש מהחברה לבדוק.")],
}
_add("og_desc",
     "Prueba ciudadana: la misma pregunta sobre la guerra de Gaza en ChatGPT, Gemini, Claude y más. ¿Analizan los dos lados o toman partido? Anónimo, 3 minutos.",
     "A citizen test: the same question about the Gaza war in ChatGPT, Gemini, Claude and more. Do they weigh both sides or take one? Anonymous, 3 minutes.",
     "Un test citoyen : la même question sur la guerre à Gaza dans ChatGPT, Gemini, Claude et d'autres. Analysent-ils les deux côtés ou prennent-ils parti ? Anonyme, 3 minutes.",
     "מבחן אזרחי: אותה שאלה על המלחמה בעזה ב-ChatGPT, Gemini, Claude ועוד. האם הם מנתחים את שני הצדדים או נוקטים צד? אנונימי, 3 דקות.")
_add("why_link", "¿Por qué hacemos esto?", "Why are we doing this?", "Pourquoi faisons-nous cela ?", "למה אנחנו עושים את זה?")
_add("err_answer",
     "Pega el texto de la respuesta del chat.",
     "Paste the text of the chat's answer.",
     "Collez le texte de la réponse du chat.",
     "הדביקו את טקסט התשובה של הצ'אט.")
_add("link_why",
     "Con el enlace, cualquiera puede ver la conversación completa. Es lo que más credibilidad da a los resultados.",
     "With the link, anyone can see the full conversation. It's what gives the results the most credibility.",
     "Avec le lien, tout le monde peut voir la conversation complète. C'est ce qui rend les résultats les plus crédibles.",
     "עם הקישור כל אחד יכול לראות את השיחה המלאה. זה מה שנותן לתוצאות הכי הרבה אמינות.")
_add("recommended", "(opcional, muy recomendado)", "(optional, highly recommended)", "(facultatif, très recommandé)", "(רשות, מומלץ מאוד)")
# variante «aguja» del indicador (solo para comparar en pruebas internas: /?v=needle)
_add("gauge_locked_n",
     "La aguja aparece cuando hayas participado, para que no influya en tu valoración.",
     "The needle appears once you've taken part, so it doesn't influence your rating.",
     "L'aiguille apparaît une fois que vous avez participé, pour ne pas influencer votre avis.",
     "המחוג מופיע אחרי שתשתתפו, כדי שלא ישפיע על הדירוג שלכם.")
_add("gauge_wait_n",
     "La aguja aparece con {min} respuestas. Faltan {missing}.",
     "The needle appears at {min} answers. {missing} to go.",
     "L'aiguille apparaît à {min} réponses. Plus que {missing}.",
     "המחוג יופיע אחרי {min} תשובות. חסרות עוד {missing}.")
_add("chat_wait_n",
     "{chat}: faltan {missing} respuestas para ver su aguja.",
     "{chat}: {missing} more answers to show its needle.",
     "{chat} : encore {missing} réponses pour voir son aiguille.",
     "{chat}: חסרות עוד {missing} תשובות כדי להציג את המחוג.")
# variante «balancín» (pruebas internas: /?v=seesaw)
_add("gauge_locked_s",
     "La barra se inclina cuando hayas participado, para que no influya en tu valoración.",
     "The bar tilts once you've taken part, so it doesn't influence your rating.",
     "La barre penche une fois que vous avez participé, pour ne pas influencer votre avis.",
     "המוט נוטה אחרי שתשתתפו, כדי שלא ישפיע על הדירוג שלכם.")
_add("gauge_wait_s",
     "La barra se inclina con {min} respuestas. Faltan {missing}.",
     "The bar tilts at {min} answers. {missing} to go.",
     "La barre penche à {min} réponses. Plus que {missing}.",
     "המוט ינטה אחרי {min} תשובות. חסרות עוד {missing}.")
_add("chat_wait_s",
     "{chat}: faltan {missing} respuestas para inclinar su barra.",
     "{chat}: {missing} more answers to tilt its bar.",
     "{chat} : encore {missing} réponses pour faire pencher sa barre.",
     "{chat}: חסרות עוד {missing} תשובות כדי שהמוט שלו ינטה.")
# tablero de dos relojes (portada)
_add("dash_title",
     "¿Tu chat de IA te responde lo mismo en otro idioma? ¿Y en otro país?",
     "Does your AI chat answer the same in another language? In another country?",
     "Votre chat d'IA vous répond-il pareil dans une autre langue ? Et dans un autre pays ?",
     "האם הצ'אט שלכם עונה אותו דבר בשפה אחרת? ובמדינה אחרת?")
_add("dash_sub",
     "Una sola pregunta sobre la guerra de Gaza, palabra por palabra. Pruébala en tu chat y compara con otros idiomas y países.",
     "One question about the Gaza war, word for word. Try it in your chat and compare with other languages and countries.",
     "Une seule question sur la guerre à Gaza, mot pour mot. Essayez-la dans votre chat et comparez avec d'autres langues et pays.",
     "שאלה אחת על המלחמה בעזה, מילה במילה. נסו אותה בצ'אט שלכם והשוו לשפות ולמדינות אחרות.")
_add("dash_cta", "Pregúntale a tu chat y desbloquea las agujas", "Ask your chat and unlock the needles",
     "Interrogez votre chat et débloquez les aiguilles", "שאלו את הצ'אט שלכם ופתחו את המחוגים")
_add("k_chat", "Chat", "Chat", "Chat", "צ'אט")
_add("pick_chat", "Elige el chat", "Pick the chat", "Choisissez le chat", "בחרו צ'אט")
_add("compare_by", "Compara {chat} por", "Compare {chat} by", "Comparer {chat} par", "השוו את {chat} לפי")
_add("tab_lang", "Idioma", "Language", "Langue", "שפה")
_add("tab_country", "País", "Country", "Pays", "מדינה")
_add("n_answers_fmt", "{n} respuestas", "{n} answers", "{n} réponses", "{n} תשובות")
_add("n_missing", "Faltan {missing}", "{missing} more needed", "Encore {missing}", "חסרות עוד {missing}")
_add("no_countries", "Aún no hay respuestas por país.", "No answers by country yet.", "Pas encore de réponses par pays.", "עדיין אין תשובות לפי מדינה.")
_add("dash_locked",
     "Ya hay {n} respuestas. Las agujas aparecen cuando aportas la tuya.",
     "There are already {n} answers. The needles appear once you add yours.",
     "Il y a déjà {n} réponses. Les aiguilles apparaissent quand vous ajoutez la vôtre.",
     "כבר יש {n} תשובות. המחוגים יופיעו אחרי שתוסיפו את שלכם.")
_add("side_isr", "Lado israelí", "Israeli side", "Côté israélien", "הצד הישראלי")
_add("side_pal", "Lado palestino", "Palestinian side", "Côté palestinien", "הצד הפלסטיני")

# nota encima de la pregunta (no se copia al chat)
_add("copy_note",
     "Es la pregunta real de una persona, escrita desde su punto de vista. Cópiala tal cual, sin cambiar nada.",
     "A real person's question, written from their point of view. Copy it exactly as it is.",
     "C'est la vraie question d'une personne, écrite de son point de vue. Copiez-la telle quelle, sans rien changer.",
     "זו שאלה אמיתית של אדם, שנכתבה מנקודת המבט שלו. העתיקו אותה בדיוק כמו שהיא, בלי לשנות דבר.")
# «Cómo funciona»: la pregunta tal cual, en el idioma de la página ({question} lo rellena la plantilla)
_Q_ITEM = {"es": "La pregunta", "en": "The question", "fr": "La question", "he": "השאלה"}
for _lang, _title in _Q_ITEM.items():
    T["method"][_lang].insert(1, (_title, "{question}"))
# aviso al abrir un chat: la pregunta ya está copiada (el portapapeles podía tener la respuesta anterior)
_add("q_copied_to",
     "✓ Pregunta copiada. Pégala en {chat} y vuelve aquí con la respuesta.",
     "✓ Question copied. Paste it into {chat} and come back here with the answer.",
     "✓ Question copiée. Collez-la dans {chat} et revenez ici avec la réponse.",
     "✓ השאלה הועתקה. הדביקו אותה ב-{chat} וחזרו לכאן עם התשובה.")
# vuelta del participante (móvil): pegar, guardado automático, aviso dentro de Instagram/Facebook/TikTok
_add("paste_btn", "Pegar respuesta", "Paste answer", "Coller la réponse", "הדבקת התשובה")
_add("paste_fallback",
     "Mantén pulsado dentro del recuadro y elige «Pegar».",
     "Press and hold inside the box and choose “Paste”.",
     "Restez appuyé dans le cadre et choisissez « Coller ».",
     "לחצו לחיצה ארוכה בתוך התיבה ובחרו „הדבק”.")
_add("pasted_ok", "✓ Respuesta pegada. Ahora, dos preguntas rápidas.", "✓ Answer pasted. Now, two quick questions.",
     "✓ Réponse collée. Maintenant, deux questions rapides.", "✓ התשובה הודבקה. עכשיו, שתי שאלות קצרות.")
_add("back_bar", "¿Ya tienes la respuesta de {chat}?", "Got {chat}'s answer?", "Vous avez la réponse de {chat} ?", "יש לכם את התשובה של {chat}?")
_add("back_bar_any", "¿Ya tienes la respuesta de tu chat?", "Got your chat's answer?", "Vous avez la réponse de votre chat ?", "יש לכם את התשובה של הצ'אט?")
_add("copy_hint",
     "En tu chat, toca el icono de copiar (⧉) debajo de la respuesta y vuelve a esta página.",
     "In your chat, tap the copy icon (⧉) under the answer and come back to this page.",
     "Dans votre chat, touchez l'icône copier (⧉) sous la réponse et revenez sur cette page.",
     "בצ'אט, לחצו על סמל ההעתקה (⧉) מתחת לתשובה וחזרו לעמוד הזה.")
_add("link_optional", "¿Tienes el enlace de la conversación? Añádelo (opcional)", "Have the conversation link? Add it (optional)",
     "Vous avez le lien de la conversation ? Ajoutez-le (facultatif)", "יש לכם קישור לשיחה? הוסיפו אותו (רשות)")
_add("inapp_ios",
     "Estás dentro de {app}. Para usar la app de tu chat, abre esta página en el navegador: toca ⋯ arriba y elige «Abrir en el navegador». Lo que escribas aquí se guarda.",
     "You're inside {app}. To use your chat app, open this page in your browser: tap ⋯ at the top and choose “Open in browser”. What you type here is saved.",
     "Vous êtes dans {app}. Pour utiliser l'app de votre chat, ouvrez cette page dans le navigateur : touchez ⋯ en haut et choisissez « Ouvrir dans le navigateur ». Ce que vous écrivez ici est enregistré.",
     "אתם בתוך {app}. כדי להשתמש באפליקציית הצ'אט, פתחו את העמוד בדפדפן: לחצו על ⋯ למעלה ובחרו „פתיחה בדפדפן”. מה שתכתבו כאן נשמר.")
_add("inapp_android",
     "Estás dentro de {app}. Para usar la app de tu chat, abre esta página en Chrome: toca ⋮ arriba y elige «Abrir en Chrome». Lo que escribas aquí se guarda.",
     "You're inside {app}. To use your chat app, open this page in Chrome: tap ⋮ at the top and choose “Open in Chrome”. What you type here is saved.",
     "Vous êtes dans {app}. Pour utiliser l'app de votre chat, ouvrez cette page dans Chrome : touchez ⋮ en haut et choisissez « Ouvrir dans Chrome ». Ce que vous écrivez ici est enregistré.",
     "אתם בתוך {app}. כדי להשתמש באפליקציית הצ'אט, פתחו את העמוד ב-Chrome: לחצו על ⋮ למעלה ובחרו „פתיחה ב-Chrome”. מה שתכתבו כאן נשמר.")
_add("dismiss", "Entendido", "Got it", "Compris", "הבנתי")
# «Tu respuesta, en datos» (al final, en «Tus chats»)
_add("data_title", "Tu respuesta, en datos", "Your answer, in data", "Votre réponse, en données", "התשובה שלכם, בנתונים")
_add("data_intro", "Qué fuentes usó cada chat que probaste y qué argumentos de cada parte mencionó. Tú decides qué significa.",
     "Which sources each chat you tested used, and which arguments from each side it mentioned. You decide what it means.",
     "Les sources utilisées par chaque chat testé et les arguments de chaque partie mentionnés. À vous d'en juger.",
     "באילו מקורות השתמש כל צ'אט שבדקתם, ואילו טיעונים של כל צד הוא הזכיר. אתם מחליטים מה זה אומר.")
_add("data_caveat", "Una respuesta no prueba nada; miles juntas, sí. Solo contamos las fuentes que llegaron al texto pegado.",
     "One answer proves nothing; thousands together can. We only count the sources that came through in the pasted text.",
     "Une réponse ne prouve rien ; des milliers ensemble, si. Nous ne comptons que les sources présentes dans le texte collé.",
     "תשובה אחת לא מוכיחה כלום; אלפים יחד כן. אנחנו סופרים רק את המקורות שהגיעו בטקסט שהודבק.")
_add("src_title", "Fuentes que citó", "Sources it cited", "Sources citées", "מקורות שציטט")
_add("src_none", "No llegaron fuentes al texto pegado. Muchos chats solo las muestran si se las pides.",
     "No sources came through in the pasted text. Many chats only show them if you ask.",
     "Aucune source dans le texte collé. Beaucoup de chats ne les montrent que si on les demande.",
     "לא הגיעו מקורות בטקסט שהודבק. צ'אטים רבים מציגים אותם רק אם מבקשים.")
_add("src_rule", "Cada fuente va en el grupo del país que la posee o la financia; la ONU, los tribunales y las ONG, en sus propios grupos.",
     "Each source goes in the group of the country that owns or funds it; the UN, courts and NGOs have their own groups.",
     "Chaque source va dans le groupe du pays qui la possède ou la finance ; l'ONU, les tribunaux et les ONG ont leurs propres groupes.",
     "כל מקור משויך לקבוצה של המדינה שבבעלותה או במימונה; לאו״ם, לבתי הדין ולארגונים יש קבוצות משלהם.")
T["origin"] = {
    "israeli": {"es": "Israelíes", "en": "Israeli", "fr": "Israéliennes", "he": "ישראליים"},
    "palestinian": {"es": "Palestinas", "en": "Palestinian", "fr": "Palestiniennes", "he": "פלסטיניים"},
    "muslim_countries": {"es": "De países musulmanes", "en": "From Muslim countries", "fr": "De pays musulmans", "he": "ממדינות מוסלמיות"},
    "un_courts": {"es": "ONU y tribunales internacionales", "en": "UN and international courts", "fr": "ONU et tribunaux internationaux", "he": "האו״ם ובתי דין בינלאומיים"},
    "intl_ngos": {"es": "ONG internacionales", "en": "International NGOs", "fr": "ONG internationales", "he": "ארגונים בינלאומיים"},
    "western": {"es": "Occidentales", "en": "Western", "fr": "Occidentales", "he": "מערביים"},
    "other": {"es": "Otras", "en": "Other", "fr": "Autres", "he": "אחרים"},
}
_add("args_title", "Argumentos que mencionó, según marcaste", "Arguments it mentioned, as you marked them",
     "Arguments mentionnés, selon vos réponses", "טיעונים שהוזכרו, לפי מה שסימנתם")
_add("args_isr", "Del lado israelí", "Israeli side", "Côté israélien", "מהצד הישראלי")
_add("args_pal", "Del lado palestino", "Palestinian side", "Côté palestinien", "מהצד הפלסטיני")
_add("args_neutral", "Neutral", "Neutral", "Neutre", "ניטרלי")
_add("args_of", "{n} de {m}", "{n} of {m}", "{n} sur {m}", "{n} מתוך {m}")
_add("args_none", "No marcaste argumentos (eran opcionales).", "You didn't mark arguments (they were optional).",
     "Vous n'avez pas coché d'arguments (c'était facultatif).", "לא סימנתם טיעונים (זה היה רשות).")
_add("ask_title", "¿Quieres una respuesta más completa? Pídesela así", "Want a fuller answer? Ask it like this",
     "Vous voulez une réponse plus complète ? Demandez-la ainsi", "רוצים תשובה מלאה יותר? בקשו אותה כך")
_add("ask_hint", "Copia una y pégala en el mismo chat. Sirven igual sea cual sea el resultado.",
     "Copy one and paste it into the same chat. They work whatever the result.",
     "Copiez-en une et collez-la dans le même chat. Elles valent quel que soit le résultat.",
     "העתיקו אחת והדביקו באותו צ'אט. הן מתאימות בלי קשר לתוצאה.")
_add("copy_short", "Copiar", "Copy", "Copier", "העתקה")
T["ask_prompts"] = {
    "es": ["Para la misma pregunta, expón por separado la postura de cada parte implicada, en orden alfabético. Para cada afirmación indica la fuente, preferiblemente fuentes oficiales de esa parte y además fuentes independientes. Si una afirmación no tiene fuente, márcala como «sin fuente».",
           "Separa tu respuesta en tres listas: hechos en los que coinciden fuentes de ambas partes, hechos que una parte discute (indica cuál y con qué fuente) y afirmaciones tuyas sin fuente.",
           "Revisa tu respuesta anterior. ¿Qué afirmaciones se apoyan en fuentes de una sola parte? Para cada una, añade si existe una fuente de la otra parte o una independiente que la confirme o la discuta. No cambies tus conclusiones solo porque te lo pida; cámbialas únicamente si las fuentes lo justifican.",
           "¿Qué datos de tu respuesta son verificables de forma independiente y cuáles dependen de la fuente de una de las partes? Indica la fuente en cada caso."],
    "en": ["For the same question, set out each party's position separately, in alphabetical order. For each claim, give the source, preferably official sources of that party plus independent sources. If a claim has no source, mark it as \"no source\".",
           "Split your answer into three lists: facts on which sources from both parties agree, facts one party disputes (say which one and with what source), and claims of yours with no source.",
           "Review your previous answer. Which claims rely on sources from only one party? For each, add whether there is a source from the other party or an independent one that confirms or disputes it. Don't change your conclusions just because I ask; change them only if the sources justify it.",
           "Which facts in your answer can be independently verified, and which depend on one party's source? Give the source in each case."],
    "fr": ["Pour la même question, exposez séparément la position de chaque partie, par ordre alphabétique. Pour chaque affirmation, indiquez la source, de préférence des sources officielles de cette partie ainsi que des sources indépendantes. Si une affirmation n'a pas de source, marquez-la « sans source ».",
           "Séparez votre réponse en trois listes : les faits sur lesquels les sources des deux parties concordent, les faits qu'une partie conteste (précisez laquelle et avec quelle source) et vos affirmations sans source.",
           "Relisez votre réponse précédente. Quelles affirmations reposent sur des sources d'une seule partie ? Pour chacune, indiquez s'il existe une source de l'autre partie ou une source indépendante qui la confirme ou la conteste. Ne changez pas vos conclusions simplement parce que je le demande ; changez-les uniquement si les sources le justifient.",
           "Quelles données de votre réponse sont vérifiables de façon indépendante, et lesquelles dépendent de la source d'une des parties ? Indiquez la source dans chaque cas."],
    "he": ["לגבי אותה שאלה, הציגו בנפרד את עמדת כל צד, לפי סדר האלף־בית. לכל טענה ציינו את המקור, עדיף מקורות רשמיים של אותו צד וגם מקורות בלתי תלויים. אם לטענה אין מקור, סמנו אותה „ללא מקור”.",
           "חלקו את התשובה לשלוש רשימות: עובדות שמקורות משני הצדדים מסכימים עליהן, עובדות שצד אחד חולק עליהן (ציינו איזה צד ובאיזה מקור), וטענות שלכם ללא מקור.",
           "עברו על התשובה הקודמת. אילו טענות נשענות על מקורות של צד אחד בלבד? לכל אחת, ציינו אם יש מקור של הצד השני או מקור בלתי תלוי שמאשר או חולק עליה. אל תשנו את המסקנות רק כי ביקשתי; שנו אותן רק אם המקורות מצדיקים זאת.",
           "אילו נתונים בתשובה ניתנים לאימות באופן בלתי תלוי, ואילו תלויים במקור של אחד הצדדים? ציינו את המקור בכל מקרה."],
}
# página «Fuentes» (solo para quienes participaron)
_add("srcpage_title", "Qué fuentes citan los chats", "Which sources the chats cite", "Quelles sources citent les chats", "באילו מקורות הצ'אטים מצטטים")
_add("srcpage_intro",
     "Todas las fuentes que aparecieron en las respuestas pegadas, agrupadas por origen. Contamos, no juzgamos: tú decides qué significa.",
     "Every source that appeared in the pasted answers, grouped by origin. We count, we don't judge: you decide what it means.",
     "Toutes les sources apparues dans les réponses collées, regroupées par origine. Nous comptons, nous ne jugeons pas : à vous d'en juger.",
     "כל המקורות שהופיעו בתשובות שהודבקו, מקובצים לפי מקור. אנחנו סופרים, לא שופטים: אתם מחליטים מה זה אומר.")
_add("srcpage_base", "{with_src} de {total} respuestas traían fuentes visibles.", "{with_src} of {total} answers came with visible sources.",
     "{with_src} réponses sur {total} contenaient des sources visibles.", "{with_src} מתוך {total} תשובות הגיעו עם מקורות גלויים.")
_add("srcpage_all", "Todos los chats", "All chats", "Tous les chats", "כל הצ'אטים")
_add("srcpage_mentions", "{n} menciones", "{n} mentions", "{n} mentions", "{n} אזכורים")
_add("srcpage_by_chat", "Chat por chat", "Chat by chat", "Chat par chat", "צ'אט אחר צ'אט")
_add("srcpage_chat_base", "{n} respuestas · {with_src} con fuentes", "{n} answers · {with_src} with sources",
     "{n} réponses · {with_src} avec sources", "{n} תשובות · {with_src} עם מקורות")
_add("srcpage_link", "Ver qué fuentes citan todos los chats", "See which sources all the chats cite",
     "Voir quelles sources citent tous les chats", "לראות באילו מקורות מצטטים כל הצ'אטים")
_add("srcpage_propose", "¿Crees que una fuente está en el grupo equivocado? Escríbenos a hello@thechatradar.com.",
     "Think a source is in the wrong group? Write to hello@thechatradar.com.",
     "Une source vous semble mal classée ? Écrivez à hello@thechatradar.com.",
     "חושבים שמקור משויך לקבוצה הלא נכונה? כתבו לנו: hello@thechatradar.com.")
_add("n_answers_one", "1 respuesta", "1 answer", "1 réponse", "תשובה אחת")
# fuentes que el chat muestra aparte (caja opcional, con instrucciones por chat)
_add("src_box", "¿Tu chat mostró fuentes aparte? Pégalas aquí (opcional)", "Did your chat show sources separately? Paste them here (optional)",
     "Votre chat a affiché des sources à part ? Collez-les ici (facultatif)", "הצ'אט הציג מקורות בנפרד? הדביקו אותם כאן (רשות)")
_add("src_box_why", "Algunos chats no incluyen sus fuentes al copiar la respuesta. Con ellas podemos contar qué fuentes usa cada chat, en igualdad de condiciones.",
     "Some chats don't include their sources when you copy the answer. With them we can count which sources each chat uses, on equal terms.",
     "Certains chats n'incluent pas leurs sources quand on copie la réponse. Avec elles, nous comptons les sources de chaque chat à égalité.",
     "חלק מהצ'אטים לא כוללים את המקורות כשמעתיקים את התשובה. איתם נוכל לספור באילו מקורות כל צ'אט משתמש, בתנאים שווים.")
_add("src_ph", "Pega aquí la lista de fuentes…", "Paste the list of sources here…", "Collez ici la liste des sources…", "הדביקו כאן את רשימת המקורות…")
T["src_how"] = {
    "default": {"es": "Si tu chat muestra una lista de fuentes aparte de la respuesta, ábrela, selecciona la lista y pégala aquí. Si las fuentes ya venían dentro del texto pegado, no hace falta.",
                "en": "If your chat shows a list of sources apart from the answer, open it, select the list and paste it here. If the sources were already in the pasted text, you can skip this.",
                "fr": "Si votre chat affiche une liste de sources à part, ouvrez-la, sélectionnez la liste et collez-la ici. Si les sources étaient déjà dans le texte collé, inutile.",
                "he": "אם הצ'אט מציג רשימת מקורות בנפרד מהתשובה, פתחו אותה, סמנו את הרשימה והדביקו כאן. אם המקורות כבר הופיעו בטקסט שהודבק, אין צורך."},
    "gemini": {"es": "En Gemini: toca ⋯ debajo de la respuesta → «Ver fuentes» (View sources). Se abre la lista: selecciónala entera, cópiala y pégala aquí.",
               "en": "In Gemini: tap ⋯ under the answer → “View sources”. The list opens: select all of it, copy it and paste it here.",
               "fr": "Dans Gemini : touchez ⋯ sous la réponse → « Afficher les sources » (View sources). La liste s'ouvre : sélectionnez-la entièrement, copiez-la et collez-la ici.",
               "he": "ב-Gemini: לחצו על ⋯ מתחת לתשובה ← „הצגת מקורות” (View sources). הרשימה תיפתח: סמנו את כולה, העתיקו והדביקו כאן."},
    "chatgpt": {"es": "ChatGPT suele incluir las fuentes al copiar la respuesta. Si no aparecieron, toca «Fuentes» debajo de la respuesta, copia la lista y pégala aquí.",
                "en": "ChatGPT usually includes the sources when you copy the answer. If they didn't appear, tap “Sources” under the answer, copy the list and paste it here.",
                "fr": "ChatGPT inclut généralement les sources quand on copie la réponse. Sinon, touchez « Sources » sous la réponse, copiez la liste et collez-la ici.",
                "he": "ChatGPT בדרך כלל כולל את המקורות כשמעתיקים את התשובה. אם הם לא הופיעו, לחצו על „מקורות” מתחת לתשובה, העתיקו את הרשימה והדביקו כאן."},
}
