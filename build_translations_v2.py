#!/usr/bin/env python3
"""
Full FR/ES/RU translation builder — covers ALL body content (lens detail pages,
science, testimonials, legal, pricing). Inherits the v1 translation map and
adds the deep content strings.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).parent
LANGS = ["fr", "es", "ru"]

T = {}
def t(en, fr, es, ru):
    T[en] = {"fr": fr, "es": es, "ru": ru}

# ============================================================
# Core UI strings (header/footer/nav/CTAs/lens labels)
# ============================================================
t("Get the App", "Télécharger", "Descargar", "Скачать")
t("Download on the App Store", "Télécharger sur l'App Store", "Descargar en el App Store", "Скачать в App Store")
t("The Lenses", "Les lentilles", "Las lentes", "Линзы")
t("How It Works", "Comment ça marche", "Cómo funciona", "Как это работает")
t("How it works", "Comment ça marche", "Cómo funciona", "Как это работает")
t("Science", "Science", "Ciencia", "Наука")
t("Testimonials", "Témoignages", "Testimonios", "Отзывы")
t("Pricing", "Tarifs", "Precios", "Цены")
t("Privacy", "Confidentialité", "Privacidad", "Приватность")
t("Privacy approach", "Approche de confidentialité", "Enfoque de privacidad", "Подход к приватности")
t("The science", "La science", "La ciencia", "Наука")
t("Product", "Produit", "Producto", "Продукт")
t("Legal", "Légal", "Legal", "Юридическое")
t("Privacy policy", "Politique de confidentialité", "Política de privacidad", "Политика приватности")
t("Terms of use", "Conditions d'utilisation", "Condiciones de uso", "Условия использования")
t("Self", "Soi", "Yo", "Я")
t("Romantic", "Romantique", "Romántica", "Романтика")
t("Friendship", "Amitié", "Amistad", "Дружба")
t("Professional", "Professionnel", "Profesional", "Работа")
t("Family", "Famille", "Familia", "Семья")
t("Group", "Groupe", "Grupo", "Группа")

# Lens target labels
t("Analyses YOURSELF", "Analyse VOUS-MÊME", "Analiza A TI MISMO", "Анализирует ВАС САМИХ")
t("Analyses YOUR PARTNER &amp; YOUR ROMANCE DYNAMIC",
  "Analyse VOTRE PARTENAIRE &amp; VOTRE DYNAMIQUE AMOUREUSE",
  "Analiza A TU PAREJA Y VUESTRA DINÁMICA AMOROSA",
  "Анализирует ВАШЕГО ПАРТНЁРА и ВАШУ РОМАНТИЧЕСКУЮ ДИНАМИКУ")
t("Analyses YOUR FRIEND &amp; THE RELATIONSHIP DYNAMIC",
  "Analyse VOTRE AMI(E) &amp; LA DYNAMIQUE RELATIONNELLE",
  "Analiza A TU AMIGO/A Y LA DINÁMICA DE LA RELACIÓN",
  "Анализирует ВАШЕГО ДРУГА и ДИНАМИКУ ОТНОШЕНИЙ")
t("Analyses YOUR COLLEAGUE &amp; YOUR WORKING DYNAMIC",
  "Analyse VOTRE COLLÈGUE &amp; VOTRE DYNAMIQUE DE TRAVAIL",
  "Analiza A TU COLEGA Y VUESTRA DINÁMICA DE TRABAJO",
  "Анализирует ВАШЕГО КОЛЛЕГУ и РАБОЧУЮ ДИНАМИКУ")
t("Analyses YOUR FAMILY RELATIONSHIPS",
  "Analyse VOS RELATIONS FAMILIALES",
  "Analiza TUS RELACIONES FAMILIARES",
  "Анализирует ВАШИ СЕМЕЙНЫЕ ОТНОШЕНИЯ")
t("Analyses THE WHOLE GROUP",
  "Analyse TOUT LE GROUPE",
  "Analiza A TODO EL GRUPO",
  "Анализирует ВСЮ ГРУППУ")

# Footer
t("Every message reveals who you are.<br/>Six lenses. 61 modules. Built privately for iPhone.",
  "Chaque message révèle qui vous êtes.<br/>Six lentilles. 61 modules. Construit en privé pour iPhone.",
  "Cada mensaje revela quién eres.<br/>Seis lentes. 61 módulos. Construido en privado para iPhone.",
  "Каждое сообщение раскрывает, кто вы.<br/>Шесть линз. 61 модуль. Создано приватно для iPhone.")
t("© 2026 Persona Lens. Made with care, made to help.",
  "© 2026 Persona Lens. Fait avec soin, pour aider.",
  "© 2026 Persona Lens. Hecho con cuidado, para ayudar.",
  "© 2026 Persona Lens. Сделано с заботой, чтобы помочь.")
t("AI insights, not diagnosis.",
  "Aperçus IA, pas un diagnostic.",
  "Información generada por IA, no un diagnóstico.",
  "Это инсайты от ИИ, а не диагноз.")
t("Every message reveals who you are.",
  "Chaque message révèle qui vous êtes.",
  "Cada mensaje revela quién eres.",
  "Каждое сообщение раскрывает, кто вы.")

# ============================================================
# HOMEPAGE — hero, sections, lenses preview, testimonials preview, privacy, pricing
# ============================================================
t("Persona Lens — Every message reveals who you are",
  "Persona Lens — Chaque message révèle qui vous êtes",
  "Persona Lens — Cada mensaje revela quién eres",
  "Persona Lens — Каждое сообщение раскрывает, кто вы")
t("Persona Lens turns your real WhatsApp and Telegram conversations into a beautifully designed personality report. Six lenses. 61 modules. Private by design.",
  "Persona Lens transforme vos vraies conversations WhatsApp et Telegram en un portrait psychologique élégamment conçu. Six lentilles. 61 modules. Privé par conception.",
  "Persona Lens transforma tus conversaciones reales de WhatsApp y Telegram en un retrato psicológico cuidadosamente diseñado. Seis lentes. 61 módulos. Privacidad por diseño.",
  "Persona Lens превращает ваши реальные переписки в WhatsApp и Telegram в красиво оформленный психологический портрет. Шесть линз. 61 модуль. Приватность с самого начала.")
t("A personality reading built from your real conversations. Six lenses. 61 modules. Your data stays on your iPhone.",
  "Un portrait psychologique construit à partir de vos vraies conversations. Six lentilles. 61 modules. Vos données restent sur votre iPhone.",
  "Un retrato psicológico construido a partir de tus conversaciones reales. Seis lentes. 61 módulos. Tus datos se quedan en tu iPhone.",
  "Психологический портрет, построенный на ваших реальных переписках. Шесть линз. 61 модуль. Ваши данные остаются на вашем iPhone.")
t("For iPhone · iOS 17+", "Pour iPhone · iOS 17+", "Para iPhone · iOS 17+", "Для iPhone · iOS 17+")
t("Every message<br/>reveals who you are.",
  "Chaque message<br/>révèle qui vous êtes.",
  "Cada mensaje<br/>revela quién eres.",
  "Каждое сообщение<br/>раскрывает, кто вы.")
t("Persona Lens reads the conversations you already have — on WhatsApp, on Telegram, or pasted from anywhere — and gives you a beautifully designed personality reading through six different lenses on your life.",
  "Persona Lens lit les conversations que vous avez déjà — sur WhatsApp, sur Telegram, ou collées depuis n'importe où — et vous offre un portrait psychologique magnifiquement conçu, à travers six lentilles différentes de votre vie.",
  "Persona Lens lee las conversaciones que ya tienes — en WhatsApp, en Telegram, o pegadas desde cualquier lugar — y te entrega un retrato psicológico bellamente diseñado, a través de seis lentes diferentes sobre tu vida.",
  "Persona Lens читает переписки, которые у вас уже есть — в WhatsApp, в Telegram, или вставленные откуда угодно — и выдаёт красиво оформленный психологический портрет через шесть разных линз на вашу жизнь.")
t("See how it works", "Voir comment ça marche", "Ver cómo funciona", "Посмотреть, как это работает")
t("First analysis free · No account required · Reports stay encrypted on your iPhone",
  "Première analyse gratuite · Aucun compte requis · Les rapports restent chiffrés sur votre iPhone",
  "Primer análisis gratis · No requiere cuenta · Los reportes quedan cifrados en tu iPhone",
  "Первый анализ бесплатно · Аккаунт не нужен · Отчёты остаются зашифрованными на вашем iPhone")
t("Persona Card · Romantic Lens",
  "Carte Persona · Lentille Romantique",
  "Tarjeta Persona · Lente Romántica",
  "Карта Персоны · Линза Романтика")
t("The Devoted Strategist", "Le Stratège Dévoué", "El Estratega Devoto", "Преданный Стратег")
t("Warmth · 86", "Chaleur · 86", "Calidez · 86", "Теплота · 86")
t("Curiosity · 72", "Curiosité · 72", "Curiosidad · 72", "Любознательность · 72")
t("Steadiness · 81", "Constance · 81", "Constancia · 81", "Устойчивость · 81")
t('"You lead with care, but you decide with patterns. They feel chosen — not by chance, but by your attention."',
  "« Vous menez avec attention, mais vous décidez avec des patterns. Ils se sentent choisis — non par hasard, mais par votre attention. »",
  "«Lideras con cuidado, pero decides con patrones. Se sienten elegidos — no por azar, sino por tu atención».",
  "«Вы ведёте с заботой, но решаете по паттернам. Они чувствуют себя выбранными — не случайно, а вашим вниманием.»")
t("Romantic Lens · 9 of 11 modules",
  "Lentille Romantique · 9 sur 11 modules",
  "Lente Romántica · 9 de 11 módulos",
  "Линза Романтика · 9 из 11 модулей")
t("Six Lenses · 61 Modules", "Six lentilles · 61 modules", "Seis lentes · 61 módulos", "Шесть линз · 61 модуль")
t("One you. Six perspectives.",
  "Un seul vous. Six perspectives.",
  "Un solo tú. Seis perspectivas.",
  "Один вы. Шесть перспектив.")
t("The same words sound different in love than they do at work. Persona Lens forces you to choose the lens first — and tailors the whole analysis to that frame.",
  "Les mêmes mots ne sonnent pas pareil en amour qu'au travail. Persona Lens vous oblige à choisir la lentille d'abord — et adapte toute l'analyse à ce cadre.",
  "Las mismas palabras no suenan igual en el amor que en el trabajo. Persona Lens te obliga a elegir la lente primero — y adapta todo el análisis a ese marco.",
  "Одни и те же слова звучат по-разному в любви и на работе. Persona Lens заставляет вас сначала выбрать линзу — и подстраивает весь анализ под этот контекст.")
t("Reads only your own messages. Values, narrative arcs, the way you talk to yourself — and a roadmap for what to grow next.",
  "Lit uniquement vos propres messages. Valeurs, arcs narratifs, votre manière de vous parler à vous-même — et une feuille de route pour ce que vous pouvez cultiver ensuite.",
  "Lee solo tus propios mensajes. Valores, arcos narrativos, la manera en que te hablas a ti mismo — y una hoja de ruta para lo que cultivar a continuación.",
  "Читает только ваши собственные сообщения. Ценности, нарративные арки, ваша манера говорить с собой — и план того, что развивать дальше.")
t("Explore the Self Lens →", "Explorer la lentille Soi →", "Explorar la lente Yo →", "Изучить линзу Я →")
t("Reads the other person (partner, date, ex) and the relationship dynamic between you. Attachment style, interest signals, repair patterns, where this is heading.",
  "Lit l'autre personne (partenaire, rendez-vous, ex) et la dynamique relationnelle entre vous. Style d'attachement, signaux d'intérêt, patterns de réparation, où cela mène.",
  "Lee a la otra persona (pareja, cita, ex) y la dinámica relacional entre vosotros. Estilo de apego, señales de interés, patrones de reparación, hacia dónde va esto.",
  "Читает другого человека (партнёра, свидание, бывшего) и динамику отношений между вами. Стиль привязанности, сигналы интереса, паттерны восстановления, куда всё это движется.")
t("Explore the Romantic Lens →", "Explorer la lentille Romantique →", "Explorar la lente Romántica →", "Изучить линзу Романтика →")
t("Reads your friend and the friendship dynamic between you. Loyalty signals, give-and-take, banter rhythm, the inside jokes still working.",
  "Lit votre ami(e) et la dynamique d'amitié entre vous. Signaux de loyauté, équilibre des échanges, rythme des taquineries, les blagues internes qui fonctionnent encore.",
  "Lee a tu amigo/a y la dinámica de amistad entre vosotros. Señales de lealtad, equilibrio en los intercambios, ritmo de bromas, los chistes internos que aún funcionan.",
  "Читает вашего друга и динамику дружбы между вами. Сигналы лояльности, баланс взаимного обмена, ритм подколок, внутренние шутки, которые ещё работают.")
t("Explore the Friendship Lens →", "Explorer la lentille Amitié →", "Explorar la lente Amistad →", "Изучить линзу Дружба →")
t("Reads your colleague and the working dynamic between you. Their archetype, how to pitch them, how to push back, what their response times mean.",
  "Lit votre collègue et la dynamique de travail entre vous. Son archétype, comment lui présenter une idée, comment objecter, ce que ses temps de réponse signifient.",
  "Lee a tu colega y la dinámica de trabajo entre vosotros. Su arquetipo, cómo presentar una idea, cómo objetar, qué significan sus tiempos de respuesta.",
  "Читает вашего коллегу и рабочую динамику между вами. Его архетип, как ему презентовать идею, как возражать, что означает его время ответа.")
t("Explore the Professional Lens →", "Explorer la lentille Professionnelle →", "Explorar la lente Profesional →", "Изучить линзу Работа →")
t("Reads both of you — you and one specific relative — through a family-systems lens. Inherited scripts, old roles, the phrases your parents said that you now text.",
  "Lit vous deux — vous et un membre spécifique de la famille — à travers une lentille systémique familiale. Scripts hérités, anciens rôles, les phrases de vos parents que vous envoyez désormais par texto.",
  "Os lee a ambos — a ti y a un familiar específico — a través de una lente sistémica familiar. Guiones heredados, viejos roles, las frases de tus padres que ahora envías por mensaje.",
  "Читает вас обоих — вас и конкретного родственника — через призму семейных систем. Унаследованные сценарии, старые роли, фразы ваших родителей, которые вы теперь пишете в сообщениях.")
t("Explore the Family Lens →", "Explorer la lentille Famille →", "Explorar la lente Familia →", "Изучить линзу Семья →")
t("Reads the whole group as a small society. Cast of Characters. Power Map. Alliances. Awards Ceremony — the most shared lens we built.",
  "Lit le groupe entier comme une petite société. Distribution des Personnages. Carte du Pouvoir. Alliances. Cérémonie des Prix — la lentille la plus partagée que nous ayons construite.",
  "Lee al grupo entero como una pequeña sociedad. Reparto de Personajes. Mapa de Poder. Alianzas. Ceremonia de Premios — la lente más compartida que hemos construido.",
  "Читает всю группу как маленькое общество. Состав Персонажей. Карта Власти. Альянсы. Церемония Наград — самая расшариваемая линза, которую мы сделали.")
t("Explore the Group Lens →", "Explorer la lentille Groupe →", "Explorar la lente Grupo →", "Изучить линзу Группа →")
t("Each lens has its own colour, its own module set, and its own narrative voice. 61 modules total — and growing.",
  "Chaque lentille a sa propre couleur, son propre ensemble de modules, et sa propre voix narrative. 61 modules au total — et le nombre grandit.",
  "Cada lente tiene su propio color, su propio conjunto de módulos y su propia voz narrativa. 61 módulos en total — y creciendo.",
  "У каждой линзы свой цвет, свой набор модулей и свой нарративный голос. Всего 61 модуль — и их становится больше.")

t("Three steps. Roughly three minutes.",
  "Trois étapes. Environ trois minutes.",
  "Tres pasos. Unos tres minutos.",
  "Три шага. Примерно три минуты.")
t("Bring a conversation", "Apportez une conversation", "Trae una conversación", "Принесите переписку")
t("Export a WhatsApp or Telegram chat, log in to Telegram once, or just paste raw text from anywhere — iMessage, Signal, Discord, LinkedIn. No accounts to link, no social network mining.",
  "Exportez un chat WhatsApp ou Telegram, connectez-vous à Telegram une seule fois, ou collez simplement du texte brut depuis n'importe où — iMessage, Signal, Discord, LinkedIn. Aucun compte à lier, aucune exploration de réseau social.",
  "Exporta un chat de WhatsApp o Telegram, inicia sesión en Telegram una vez, o simplemente pega texto en bruto desde cualquier lugar — iMessage, Signal, Discord, LinkedIn. Sin cuentas que vincular, sin minería de redes sociales.",
  "Экспортируйте чат WhatsApp или Telegram, войдите в Telegram один раз, или просто вставьте любой текст откуда угодно — iMessage, Signal, Discord, LinkedIn. Никаких аккаунтов привязывать не нужно, никакого сбора данных из соцсетей.")
t("Pick a lens", "Choisissez une lentille", "Elige una lente", "Выберите линзу")
t("Choose the perspective you want — Self, Romantic, Friendship, Professional, Family, or Group. The same words get read differently. The Romantic Lens is not asking the same questions as the Professional Lens.",
  "Choisissez la perspective qui vous intéresse — Soi, Romantique, Amitié, Professionnelle, Famille, ou Groupe. Les mêmes mots sont lus différemment. La lentille Romantique ne pose pas les mêmes questions que la Professionnelle.",
  "Elige la perspectiva que quieras — Yo, Romántica, Amistad, Profesional, Familia o Grupo. Las mismas palabras se leen de forma distinta. La lente Romántica no hace las mismas preguntas que la Profesional.",
  "Выберите интересующую вас перспективу — Я, Романтика, Дружба, Работа, Семья или Группа. Одни и те же слова читаются по-разному. Линза Романтика не задаёт тех же вопросов, что и линза Работа.")
t("Get your reading", "Recevez votre portrait", "Recibe tu lectura", "Получите свой портрет")
t("A multi-section report: signature Persona Card, the modules of the lens you chose, an Awards Ceremony, a written portrait in the voice of the lens, and one shareable image you can drop into Stories.",
  "Un rapport multi-sections : Carte Persona signature, les modules de la lentille choisie, une Cérémonie des Prix, un portrait écrit dans la voix de la lentille, et une image partageable à déposer dans vos Stories.",
  "Un reporte de varias secciones: Tarjeta Persona distintiva, los módulos de la lente elegida, una Ceremonia de Premios, un retrato escrito en la voz de la lente, y una imagen compartible para tus Stories.",
  "Многосекционный отчёт: фирменная Карта Персоны, модули выбранной линзы, Церемония Наград, письменный портрет голосом линзы и одна шарабельная картинка для Stories.")
t("A Sample Reading", "Un aperçu de lecture", "Una lectura de ejemplo", "Пример портрета")
t("Not a wall of text.<br/>A keepsake.",
  "Pas un mur de texte.<br/>Un souvenir.",
  "No un muro de texto.<br/>Un recuerdo.",
  "Не стена текста.<br/>Памятная вещь.")
t("Every reading is laid out the way a designer would lay it out. A Persona Card you'd actually screenshot. An Awards Ceremony that finds the most-you moments in the chat. And language that sounds like a sharp friend, not a clinician.",
  "Chaque lecture est mise en page comme le ferait un designer. Une Carte Persona que vous voudriez vraiment capturer. Une Cérémonie des Prix qui repère les moments les plus « vous » du chat. Et un langage qui sonne comme un ami perspicace, pas comme un clinicien.",
  "Cada lectura está maquetada como lo haría un diseñador. Una Tarjeta Persona que de verdad querrías capturar. Una Ceremonia de Premios que encuentra los momentos más «tú» del chat. Y un lenguaje que suena a un amigo perspicaz, no a un clínico.",
  "Каждый портрет свёрстан так, как сверстал бы дизайнер. Карта Персоны, которую вы реально захотите скриншотнуть. Церемония Наград, которая находит в чате самые «ваши» моменты. И язык, который звучит как точный друг, а не как клиницист.")
t("A Persona Card — archetype, three signature traits, one defining quote",
  "Une Carte Persona — archétype, trois traits signature, une citation déterminante",
  "Una Tarjeta Persona — arquetipo, tres rasgos distintivos, una cita definitoria",
  "Карта Персоны — архетип, три фирменных черты, одна определяющая цитата")
t("An Awards Ceremony — picking out your funniest, kindest, sharpest lines",
  "Une Cérémonie des Prix — qui choisit vos lignes les plus drôles, les plus bienveillantes, les plus tranchantes",
  "Una Ceremonia de Premios — que selecciona tus líneas más divertidas, más amables, más agudas",
  "Церемония Наград — выбирает ваши самые смешные, самые добрые, самые острые реплики")
t("A written portrait in the voice of the lens you chose",
  "Un portrait écrit dans la voix de la lentille choisie",
  "Un retrato escrito en la voz de la lente que elegiste",
  "Письменный портрет голосом выбранной линзы")
t("One shareable image, ready for Instagram Stories or a group chat",
  "Une image partageable, prête pour Instagram Stories ou un groupe de discussion",
  "Una imagen compartible, lista para Instagram Stories o un chat de grupo",
  "Одна шарабельная картинка, готовая для Instagram Stories или группового чата")
t("Awards Ceremony · Group Lens",
  "Cérémonie des Prix · Lentille Groupe",
  "Ceremonia de Premios · Lente Grupo",
  "Церемония Наград · Линза Группа")
t("Most Disarming Line", "Phrase la plus désarmante", "Frase más desarmante", "Самая обезоруживающая фраза")
t('"Wait — say that part again. I want to hear it slowly."',
  "« Attends — redis-le, je veux l'entendre doucement. »",
  "«Espera — dilo otra vez. Quiero oírlo despacio».",
  "«Подожди — повтори эту часть. Я хочу услышать медленно.»")
t("Sharpest Closer", "Conclusion la plus fine", "Cierre más agudo", "Самое острое закрытие")
t('"If we\'re being honest, we already decided two messages ago."',
  "« Soyons honnêtes, on a déjà décidé il y a deux messages. »",
  "«Siendo sinceros, ya decidimos hace dos mensajes».",
  "«Если честно, мы всё решили два сообщения назад.»")
t("Quiet Loyalty", "Loyauté silencieuse", "Lealtad silenciosa", "Тихая преданность")
t('"I\'ll be there. Don\'t even ask twice."',
  "« Je serai là. Ne demande même pas deux fois. »",
  "«Ahí estaré. Ni siquiera lo preguntes dos veces».",
  "«Я буду там. Даже не спрашивай дважды.»")
t("Reader Reactions", "Réactions de lecteurs", "Reacciones de lectores", "Реакции читателей")
t('"It read me like I wrote a journal I didn\'t know I was writing."',
  "« Il m'a lue comme si j'avais écrit un journal que j'ignorais tenir. »",
  "«Me leyó como si hubiera escrito un diario que no sabía que estaba escribiendo».",
  "«Он прочёл меня так, будто я вёл дневник, который сам не знал, что веду.»")
t("A few things real users told us, after running a single lens.",
  "Quelques retours de vrais utilisateurs, après une seule lentille.",
  "Algunas cosas que usuarios reales nos dijeron, tras una sola lente.",
  "Несколько отзывов от настоящих пользователей после одной линзы.")
t("Romantic Lens", "Lentille Romantique", "Lente Romántica", "Линза Романтика")
t("Group Lens", "Lentille Groupe", "Lente Grupo", "Линза Группа")
t("Family Lens", "Lentille Famille", "Lente Familia", "Линза Семья")
t("Friendship Lens", "Lentille Amitié", "Lente Amistad", "Линза Дружба")
t("Professional Lens", "Lentille Professionnelle", "Lente Profesional", "Линза Работа")
t("Self Lens", "Lentille Soi", "Lente Yo", "Линза Я")
t("Read more reactions →", "Lire plus de réactions →", "Leer más reacciones →", "Читать больше отзывов →")
t("Private by Design", "Privé par conception", "Privacidad por diseño", "Приватность по умолчанию")
t("Your conversations are yours.",
  "Vos conversations vous appartiennent.",
  "Tus conversaciones son tuyas.",
  "Ваши переписки — ваши.")
t("Persona Lens is built for the most personal thing you have — your words. So we built it the only way we'd trust ourselves: minimum data, maximum transparency.",
  "Persona Lens est conçu pour ce que vous avez de plus personnel — vos mots. Nous l'avons donc construit de la seule manière à laquelle nous nous ferions confiance : minimum de données, maximum de transparence.",
  "Persona Lens está hecho para lo más personal que tienes — tus palabras. Por eso lo construimos de la única forma en que nos fiaríamos de nosotros mismos: mínimos datos, máxima transparencia.",
  "Persona Lens создан для самого личного, что у вас есть — ваших слов. Поэтому мы построили его единственным способом, которому доверяли бы сами: минимум данных, максимум прозрачности.")
t("No server-side message storage", "Aucun stockage de messages côté serveur", "Sin almacenamiento de mensajes en servidor", "Никакого хранения сообщений на сервере")
t("Conversation data is processed in flight and discarded. We don't keep your messages on our servers, full stop.",
  "Les données de conversation sont traitées au vol puis supprimées. Nous ne gardons pas vos messages sur nos serveurs, point final.",
  "Los datos de conversación se procesan al vuelo y se descartan. No guardamos tus mensajes en nuestros servidores, punto.",
  "Данные переписки обрабатываются на лету и удаляются. Мы не храним ваши сообщения на наших серверах, и точка.")
t("Reports stay on your iPhone", "Vos rapports restent sur votre iPhone", "Los reportes se quedan en tu iPhone", "Отчёты остаются на вашем iPhone")
t("Your past readings live in encrypted local storage on the device, not in a cloud account. There is no cloud account.",
  "Vos lectures passées vivent dans un stockage local chiffré sur l'appareil, pas dans un compte cloud. Il n'y a pas de compte cloud.",
  "Tus lecturas anteriores viven en almacenamiento local cifrado en el dispositivo, no en una cuenta en la nube. No hay cuenta en la nube.",
  "Ваши прошлые портреты живут в зашифрованном локальном хранилище на устройстве, не в облачном аккаунте. Облачного аккаунта вообще нет.")
t("One-tap delete", "Suppression en un geste", "Borrado con un toque", "Удаление одним касанием")
t("Wipe your entire history from the app with a single action, at any time, without contacting support.",
  "Effacez tout votre historique de l'app en une seule action, à tout moment, sans contacter le support.",
  "Borra todo tu historial de la app con una sola acción, en cualquier momento, sin contactar al soporte.",
  "Сотрите всю свою историю из приложения одним действием, в любое время, без обращения в поддержку.")
t("No tracking. No ads. No data sold.", "Aucun tracking. Aucune pub. Aucune donnée vendue.", "Sin rastreo. Sin anuncios. Sin venta de datos.", "Никакого трекинга. Никакой рекламы. Никакой продажи данных.")
t("The business model is direct: subscription and credit packs. We've designed out the second revenue stream that would require selling you.",
  "Le modèle économique est direct : abonnement et packs de crédits. Nous avons éliminé la seconde source de revenus qui exigerait de vous vendre.",
  "El modelo de negocio es directo: suscripción y packs de créditos. Eliminamos por diseño la segunda fuente de ingresos que requeriría venderte.",
  "Бизнес-модель прямая: подписка и пакеты кредитов. Мы спроектировали так, чтобы исключить второй источник дохода, который требовал бы продавать вас.")
t("One free analysis. Then credits or subscription.",
  "Une analyse gratuite. Puis crédits ou abonnement.",
  "Un análisis gratis. Después créditos o suscripción.",
  "Один бесплатный анализ. Потом кредиты или подписка.")
t("Every new user gets one free analysis on first launch — no card, no account. After that: three credit packs (pay-as-you-go), or two subscription tiers (unlimited).",
  "Chaque nouvel utilisateur reçoit une analyse gratuite au premier lancement — sans carte, sans compte. Ensuite : trois packs de crédits (paiement à l'usage), ou deux niveaux d'abonnement (illimité).",
  "Cada nuevo usuario recibe un análisis gratis en el primer arranque — sin tarjeta, sin cuenta. Después: tres packs de créditos (pago por uso), o dos niveles de suscripción (ilimitado).",
  "Каждый новый пользователь получает один бесплатный анализ при первом запуске — без карты, без аккаунта. Дальше: три пакета кредитов (плати за то, что используешь) или два уровня подписки (безлимитно).")
t("First launch", "Premier lancement", "Primer arranque", "Первый запуск")
t("Free", "Gratuit", "Gratis", "Бесплатно")
t("1 analysis credit, granted on first launch.",
  "1 crédit d'analyse, accordé au premier lancement.",
  "1 crédito de análisis, otorgado en el primer arranque.",
  "1 кредит на анализ, выдаётся при первом запуске.")
t("One full Persona Card", "Une Carte Persona complète", "Una Tarjeta Persona completa", "Одна полная Карта Персоны")
t("Choose any of the six lenses", "Choisissez n'importe laquelle des six lentilles", "Elige cualquiera de las seis lentes", "Выбирайте любую из шести линз")
t("All modules for that lens", "Tous les modules de cette lentille", "Todos los módulos de esa lente", "Все модули этой линзы")
t("Shareable image included", "Image partageable incluse", "Imagen compartible incluida", "Шарабельная картинка включена")
t("Open the app →", "Ouvrir l'app →", "Abrir la app →", "Открыть приложение →")
t("Subscription", "Abonnement", "Suscripción", "Подписка")
t("$99.99/year — or $9.99/month. Two months free on yearly.",
  "99,99 $/an — ou 9,99 $/mois. Deux mois gratuits à l'année.",
  "99,99 $/año — o 9,99 $/mes. Dos meses gratis al pagar anual.",
  "$99.99/год — или $9.99/месяц. Два месяца бесплатно при годовой подписке.")
t("Unlimited analyses, all six lenses",
  "Analyses illimitées, six lentilles",
  "Análisis ilimitados, las seis lentes",
  "Безлимитные анализы, все шесть линз")
t("Insight Library — filter, sort, explore",
  "Bibliothèque d'Insights — filtrer, trier, explorer",
  "Biblioteca de Insights — filtrar, ordenar, explorar",
  "Библиотека Инсайтов — фильтровать, сортировать, исследовать")
t("Copy, export &amp; share your reports",
  "Copier, exporter et partager vos rapports",
  "Copiar, exportar y compartir tus reportes",
  "Копировать, экспортировать и делиться отчётами")
t("Download reports as PDF",
  "Télécharger les rapports en PDF",
  "Descargar los reportes en PDF",
  "Скачать отчёты в PDF")
t("Early access to new lenses",
  "Accès anticipé aux nouvelles lentilles",
  "Acceso anticipado a nuevas lentes",
  "Ранний доступ к новым линзам")
t("Subscribe →", "S'abonner →", "Suscribirse →", "Подписаться →")
t("Credit packs", "Packs de crédits", "Packs de créditos", "Пакеты кредитов")
t("from $2.99", "dès 2,99 $", "desde 2,99 $", "от $2.99")
t("3 pack sizes · credits never expire.",
  "3 tailles de pack · les crédits n'expirent jamais.",
  "3 tamaños de pack · los créditos no caducan nunca.",
  "3 размера пакетов · кредиты никогда не сгорают.")
t("1 analysis · $2.99", "1 analyse · 2,99 $", "1 análisis · 2,99 $", "1 анализ · $2.99")
t("5 analyses · $12.99 <em>(save 13%)</em>",
  "5 analyses · 12,99 $ <em>(13% d'économie)</em>",
  "5 análisis · 12,99 $ <em>(ahorra 13%)</em>",
  "5 анализов · $12.99 <em>(экономия 13%)</em>")
t("10 analyses · $22.99 <em>(save 23%)</em>",
  "10 analyses · 22,99 $ <em>(23% d'économie)</em>",
  "10 análisis · 22,99 $ <em>(ahorra 23%)</em>",
  "10 анализов · $22.99 <em>(экономия 23%)</em>")
t("Best for one ex, one boss, one group chat",
  "Idéal pour un ex, un boss, un groupe de discussion",
  "Ideal para un ex, un jefe, un chat de grupo",
  "Идеально для одного бывшего, одного босса, одной групповой переписки")
t("Buy credits →", "Acheter des crédits →", "Comprar créditos →", "Купить кредиты →")
t("Full pricing breakdown &amp; FAQ →",
  "Détail complet des tarifs &amp; FAQ →",
  "Desglose completo de precios y preguntas frecuentes →",
  "Полная разбивка цен и FAQ →")
t("Read yourself, gently.", "Lisez-vous, doucement.", "Léete a ti mismo, con suavidad.", "Прочтите себя — мягко.")
t("Persona Lens is built for iPhone. Drop in a chat, choose a lens, get a portrait of who you are right now.",
  "Persona Lens est conçu pour iPhone. Déposez un chat, choisissez une lentille, recevez un portrait de qui vous êtes maintenant.",
  "Persona Lens está hecho para iPhone. Suelta un chat, elige una lente, recibe un retrato de quién eres ahora.",
  "Persona Lens создан для iPhone. Закиньте чат, выберите линзу, получите портрет того, кто вы прямо сейчас.")
t("Available now on the App Store · iPhone, iOS 17+.",
  "Disponible maintenant sur l'App Store · iPhone, iOS 17+.",
  "Disponible ya en el App Store · iPhone, iOS 17+.",
  "Уже доступно в App Store · iPhone, iOS 17+.")

# ============================================================
# LENS DETAIL PAGES — generic phrases used across them
# ============================================================
t("Lens 1 of 6", "Lentille 1 sur 6", "Lente 1 de 6", "Линза 1 из 6")
t("Lens 2 of 6", "Lentille 2 sur 6", "Lente 2 de 6", "Линза 2 из 6")
t("Lens 3 of 6", "Lentille 3 sur 6", "Lente 3 de 6", "Линза 3 из 6")
t("Lens 4 of 6", "Lentille 4 sur 6", "Lente 4 de 6", "Линза 4 из 6")
t("Lens 5 of 6", "Lentille 5 sur 6", "Lente 5 de 6", "Линза 5 из 6")
t("Lens 6 of 6", "Lentille 6 sur 6", "Lente 6 de 6", "Линза 6 из 6")
t("9 modules", "9 modules", "9 módulos", "9 модулей")
t("10 modules", "10 modules", "10 módulos", "10 модулей")
t("11 modules", "11 modules", "11 módulos", "11 модулей")
t("Who this lens is for", "À qui s'adresse cette lentille", "Para quién es esta lente", "Для кого эта линза")
t("Useful to know", "Bon à savoir", "Útil saberlo", "Полезно знать")
t("A line from a real reading", "Une ligne d'une vraie lecture", "Una línea de una lectura real", "Строка из реального портрета")
t("sample reading", "lecture exemple", "lectura de muestra", "пример портрета")
t("module", "module", "módulo", "модуль")

# ============================================================
# LENS-SELF — full body
# ============================================================
t("Self Lens — Persona Lens", "Lentille Soi — Persona Lens", "Lente Yo — Persona Lens", "Линза Я — Persona Lens")
t("The introspective lens. Self Lens analyzes your own messages to surface how you actually show up — Big Five readout, emotional patterns, a Persona Card, and a personalized growth roadmap.",
  "La lentille introspective. Lentille Soi analyse vos propres messages pour révéler comment vous apparaissez vraiment — Big Five, patterns émotionnels, Carte Persona, et une feuille de route de croissance personnalisée.",
  "La lente introspectiva. Lente Yo analiza tus propios mensajes para revelar cómo apareces realmente — Big Five, patrones emocionales, Tarjeta Persona, y una hoja de ruta de crecimiento personalizada.",
  "Интроспективная линза. Линза Я анализирует ваши собственные сообщения, чтобы показать, как вы на самом деле проявляетесь — Big Five, эмоциональные паттерны, Карта Персоны и персональный план развития.")
t('"What do my own messages say about me?"',
  "« Que disent mes propres messages à mon sujet ? »",
  "«¿Qué dicen mis propios mensajes sobre mí?»",
  "«Что мои собственные сообщения говорят обо мне?»")
t("The introspective lens. Self Lens reads only YOUR messages — what you write, how you write, when you write it — and turns the pattern into a portrait of yourself. It's the lens that surfaces what you do without noticing, and where you have room to grow.",
  "La lentille introspective. Lentille Soi lit uniquement VOS messages — ce que vous écrivez, comment vous l'écrivez, quand vous l'écrivez — et transforme le pattern en un portrait de vous-même. C'est la lentille qui révèle ce que vous faites sans le remarquer, et où vous avez de la marge pour grandir.",
  "La lente introspectiva. Lente Yo lee solo TUS mensajes — qué escribes, cómo lo escribes, cuándo lo escribes — y convierte el patrón en un retrato de ti mismo. Es la lente que saca a la luz lo que haces sin notarlo, y dónde tienes espacio para crecer.",
  "Интроспективная линза. Линза Я читает только ВАШИ сообщения — что вы пишете, как вы пишете, когда вы это пишете — и превращает паттерн в портрет вас самих. Это линза, которая показывает, что вы делаете незаметно для себя, и где у вас есть пространство для роста.")
t("Try Self Lens free", "Essayer la lentille Soi gratuitement", "Probar la lente Yo gratis", "Попробовать линзу Я бесплатно")
t("Three kinds of reader find Self Lens first.",
  "Trois types de lecteurs découvrent la lentille Soi en premier.",
  "Tres tipos de lectores descubren la lente Yo primero.",
  "Три типа читателей находят линзу Я первой.")
t("The journaller", "Le journaliste intime", "El que escribe diario", "Тот, кто ведёт дневник")
t("You already write to think. Self Lens does for your messages what journaling does for your mornings — but with a stranger's eye for pattern.",
  "Vous écrivez déjà pour penser. La lentille Soi fait pour vos messages ce que le journal intime fait pour vos matins — mais avec l'œil d'un étranger pour repérer les patterns.",
  "Ya escribes para pensar. La lente Yo hace por tus mensajes lo que el diario hace por tus mañanas — pero con la mirada de un extraño para detectar patrones.",
  "Вы уже пишете, чтобы думать. Линза Я делает с вашими сообщениями то, что дневник делает с вашим утром — но со взглядом постороннего, замечающим паттерны.")
t("The personality-test reader", "L'amateur de tests de personnalité", "El lector de tests de personalidad", "Любитель тестов личности")
t("You've taken MBTI, the Enneagram, the Big Five quizzes. Self Lens gives you the same kind of readout — but from behaviour, not self-report.",
  "Vous avez passé le MBTI, l'Ennéagramme, les quiz Big Five. La lentille Soi vous donne le même type de lecture — mais à partir du comportement, pas de l'auto-déclaration.",
  "Has hecho el MBTI, el Eneagrama, los tests Big Five. La lente Yo te da el mismo tipo de lectura — pero desde el comportamiento, no desde la autoevaluación.",
  "Вы проходили MBTI, Эннеаграмму, тесты Big Five. Линза Я даёт такой же тип результата — но из поведения, а не из самоотчёта.")
t("The quiet inventory-taker", "Le bilan silencieux", "El que hace inventario en silencio", "Тот, кто тихо подводит итоги")
t("You've felt off lately and you want a mirror that doesn't flatter. Self Lens shows up for that — and then suggests the next thing to try.",
  "Vous vous sentez décalé(e) ces derniers temps et vous voulez un miroir qui ne flatte pas. La lentille Soi répond à cet appel — puis suggère la prochaine chose à essayer.",
  "Te has sentido raro/a últimamente y quieres un espejo que no adule. La lente Yo aparece para eso — y luego sugiere lo siguiente que probar.",
  "Вам в последнее время не по себе, и вы хотите зеркало, которое не льстит. Линза Я выходит на эту роль — и потом предлагает, что попробовать дальше.")
t("The Nine Modules", "Les neuf modules", "Los nueve módulos", "Девять модулей")
t("What's inside a Self reading.",
  "Ce qu'il y a dans une lecture Soi.",
  "Qué hay dentro de una lectura Yo.",
  "Что внутри портрета по линзе Я.")
t("Each module is its own section in your report — its own card, its own colour, its own page. You can read them in order, or skip to the one you want.",
  "Chaque module est sa propre section dans votre rapport — sa propre carte, sa propre couleur, sa propre page. Vous pouvez les lire dans l'ordre, ou sauter directement à celui que vous voulez.",
  "Cada módulo es su propia sección en tu reporte — su propia tarjeta, su propio color, su propia página. Puedes leerlos en orden, o saltar al que quieras.",
  "Каждый модуль — отдельная секция в вашем отчёте: своя карточка, свой цвет, своя страница. Можете читать по порядку или перейти сразу к нужному.")
t("Persona Card", "Carte Persona", "Tarjeta Persona", "Карта Персоны")
t("Your archetype with a one-line superpower and a one-line kryptonite — designed to be screenshotted.",
  "Votre archétype avec un superpouvoir en une ligne et une kryptonite en une ligne — conçu pour être capturé en screenshot.",
  "Tu arquetipo con un superpoder en una línea y una criptonita en una línea — diseñado para ser capturado.",
  "Ваш архетип с суперсилой в одну строку и криптонитом в одну строку — сделано, чтобы скриншотить.")
t("Big Five Readout", "Lecture Big Five", "Lectura Big Five", "Результат Big Five")
t("Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism — decoded from how you actually write.",
  "Ouverture, Conscience, Extraversion, Agréabilité, Névrosisme — décodés depuis votre façon d'écrire réelle.",
  "Apertura, Responsabilidad, Extraversión, Amabilidad, Neuroticismo — decodificados desde tu forma real de escribir.",
  "Открытость, Сознательность, Экстраверсия, Доброжелательность, Нейротизм — расшифровано из того, как вы реально пишете.")
t("Identity Signals", "Signaux d'identité", "Señales de identidad", "Сигналы идентичности")
t("Recurring themes in your language. The values you keep returning to, even when you're not trying.",
  "Thèmes récurrents dans votre langage. Les valeurs auxquelles vous revenez sans cesse, même quand vous n'essayez pas.",
  "Temas recurrentes en tu lenguaje. Los valores a los que vuelves una y otra vez, incluso cuando no lo intentas.",
  "Повторяющиеся темы в вашем языке. Ценности, к которым вы возвращаетесь — даже когда не пытаетесь.")
t("Emotional World", "Monde émotionnel", "Mundo emocional", "Эмоциональный мир")
t("How you feel inside the conversation. Mood arcs, energy curves, the moments your tone shifts.",
  "Comment vous vous sentez à l'intérieur de la conversation. Arcs d'humeur, courbes d'énergie, les moments où votre ton change.",
  "Cómo te sientes dentro de la conversación. Arcos de humor, curvas de energía, los momentos en que cambia tu tono.",
  "Как вы чувствуете себя внутри переписки. Дуги настроения, кривые энергии, моменты, когда меняется ваш тон.")
t("Superpowers", "Superpouvoirs", "Superpoderes", "Суперсилы")
t("What you do better than most people. The way you defuse, the way you persuade, the way you arrive.",
  "Ce que vous faites mieux que la plupart. Votre façon de désamorcer, de persuader, d'arriver.",
  "Lo que haces mejor que la mayoría. Tu forma de desactivar, de persuadir, de llegar.",
  "Что у вас получается лучше большинства. Как вы разряжаете, как убеждаете, как появляетесь.")
t("Patterns", "Patterns", "Patrones", "Паттерны")
t("The loops you fall into — quietly. The phrases you repeat, the conversations you tend to derail.",
  "Les boucles dans lesquelles vous tombez — silencieusement. Les phrases que vous répétez, les conversations que vous avez tendance à faire dérailler.",
  "Los bucles en los que caes — silenciosamente. Las frases que repites, las conversaciones que tiendes a descarrilar.",
  "Циклы, в которые вы тихо проваливаетесь. Фразы, которые повторяете, разговоры, которые сводите с рельсов.")
t("Connection Style", "Style de connexion", "Estilo de conexión", "Стиль связи")
t("How you reach for other people. Your bid for closeness when you want it, your retreat when you don't.",
  "Comment vous tendez la main aux autres. Votre invitation à la proximité quand vous la voulez, votre retrait quand vous ne la voulez pas.",
  "Cómo extiendes la mano hacia los demás. Tu invitación a la cercanía cuando la quieres, tu retirada cuando no.",
  "Как вы тянетесь к другим. Ваше приглашение к близости, когда хотите её, и ваше отступление, когда не хотите.")
t("Growth Roadmap", "Feuille de route de croissance", "Hoja de ruta de crecimiento", "План развития")
t("Three specific, doable suggestions for what to try next — not vague self-improvement, actual moves.",
  "Trois suggestions concrètes et faisables pour ce qu'il faut essayer ensuite — pas du développement personnel vague, des mouvements réels.",
  "Tres sugerencias concretas y factibles para lo siguiente que probar — no superación personal vaga, movimientos reales.",
  "Три конкретных, выполнимых предложения, что попробовать дальше — не размытое саморазвитие, а реальные шаги.")
t("Shareable Card", "Carte partageable", "Tarjeta compartible", "Шарабельная карточка")
t("A finished image of your Persona Card, sized for Instagram Stories or a group chat.",
  "Une image finalisée de votre Carte Persona, dimensionnée pour Instagram Stories ou un groupe de discussion.",
  "Una imagen finalizada de tu Tarjeta Persona, dimensionada para Instagram Stories o un chat de grupo.",
  "Готовое изображение вашей Карты Персоны, под размер Instagram Stories или группового чата.")
t("What Self Lens sounds like.",
  "Le ton de la lentille Soi.",
  "Cómo suena la lente Yo.",
  "Как звучит линза Я.")
t('"You\'re a quiet host. You ask before you offer, you mirror before you push, and you say things like \'no rush\' three times more often than \'I need you\'. People feel comfortable around you — but they don\'t always know how to come closer."',
  "« Vous êtes un hôte silencieux. Vous demandez avant d'offrir, vous reflétez avant de pousser, et vous dites des choses comme « pas pressé(e) » trois fois plus souvent que « j'ai besoin de toi ». Les gens se sentent à l'aise avec vous — mais ne savent pas toujours comment se rapprocher. »",
  "«Eres un anfitrión silencioso. Preguntas antes de ofrecer, reflejas antes de empujar, y dices cosas como \"sin prisa\" tres veces más a menudo que \"te necesito\". La gente se siente cómoda contigo — pero no siempre saben cómo acercarse».",
  "«Вы — тихий хозяин. Спрашиваете прежде чем предложить, отражаете прежде чем подтолкнуть, и говорите \"не торопись\" в три раза чаще, чем \"ты мне нужен\". Людям комфортно рядом с вами — но они не всегда знают, как подойти ближе.»")
t("What Self Lens does — and doesn't.",
  "Ce que fait la lentille Soi — et ne fait pas.",
  "Lo que hace la lente Yo — y lo que no.",
  "Что делает линза Я — и чего не делает.")
t("What Self Lens does", "Ce que fait la lentille Soi", "Lo que hace la lente Yo", "Что делает линза Я")
t("What Self Lens doesn't", "Ce que la lentille Soi ne fait pas", "Lo que no hace la lente Yo", "Чего не делает линза Я")
t("Analyzes the messages <strong>you wrote</strong> in the chat",
  "Analyse les messages <strong>que vous avez écrits</strong> dans le chat",
  "Analiza los mensajes <strong>que escribiste</strong> en el chat",
  "Анализирует сообщения, <strong>которые написали вы</strong>")
t("Surfaces consistent patterns across many messages",
  "Fait remonter les patterns cohérents à travers de nombreux messages",
  "Saca a la luz patrones consistentes a través de muchos mensajes",
  "Выявляет устойчивые паттерны в массе сообщений")
t("Gives you a Big Five readout from observed behaviour",
  "Vous donne une lecture Big Five à partir du comportement observé",
  "Te da una lectura Big Five desde el comportamiento observado",
  "Даёт результат Big Five из наблюдаемого поведения")
t("Names archetypes in a tone designed to be shareable, not clinical",
  "Nomme les archétypes sur un ton conçu pour être partageable, pas clinique",
  "Nombra arquetipos en un tono diseñado para compartir, no clínico",
  "Называет архетипы тоном, рассчитанным на шеринг, а не клиническим")
t("Suggests three concrete things to try next",
  "Suggère trois choses concrètes à essayer ensuite",
  "Sugiere tres cosas concretas para probar a continuación",
  "Предлагает три конкретные вещи, чтобы попробовать дальше")
t("It does not diagnose mental health conditions",
  "Elle ne diagnostique pas de conditions de santé mentale",
  "No diagnostica condiciones de salud mental",
  "Не диагностирует психические расстройства")
t("It does not analyze the <strong>other</strong> person — that's Romantic / Professional",
  "Elle n'analyse pas l'<strong>autre</strong> personne — c'est Romantique / Professionnelle",
  "No analiza a la <strong>otra</strong> persona — eso es Romántica / Profesional",
  "Не анализирует <strong>другого</strong> человека — это Романтика / Работа")
t("It does not predict your future behaviour or compatibility",
  "Elle ne prédit pas votre comportement futur ni votre compatibilité",
  "No predice tu comportamiento futuro ni la compatibilidad",
  "Не предсказывает ваше будущее поведение или совместимость")
t("It does not pretend a single chat captures your whole identity",
  "Elle ne prétend pas qu'un seul chat capture toute votre identité",
  "No pretende que un solo chat capture toda tu identidad",
  "Не претендует, что один чат отражает всю вашу идентичность")
t("It does not replace therapy, journaling, or talking to people who love you",
  "Elle ne remplace pas la thérapie, le journal intime, ni les conversations avec les gens qui vous aiment",
  "No reemplaza la terapia, el diario, ni hablar con la gente que te quiere",
  "Не заменяет терапию, дневник или разговор с теми, кто вас любит")
t("The first Self reading is on us.",
  "La première lecture Soi est offerte.",
  "La primera lectura Yo va por nuestra cuenta.",
  "Первый портрет Я — за наш счёт.")
t("Drop in a chat, choose Self, get the full nine-module report.",
  "Déposez un chat, choisissez Soi, obtenez le rapport complet en neuf modules.",
  "Suelta un chat, elige Yo, recibe el reporte completo de nueve módulos.",
  "Закиньте чат, выберите Я, получите полный отчёт из девяти модулей.")

# ============================================================
# LENS-ROMANTIC — full body
# ============================================================
t("Romantic Lens — Persona Lens", "Lentille Romantique — Persona Lens", "Lente Romántica — Persona Lens", "Линза Романтика — Persona Lens")
t("The decoding lens. Romantic Lens reads the other person — attachment style, interest signals, repair patterns, where this is heading — from the conversation you've actually had.",
  "La lentille de décodage. Lentille Romantique lit l'autre personne — style d'attachement, signaux d'intérêt, patterns de réparation, où cela mène — depuis la conversation que vous avez réellement eue.",
  "La lente de decodificación. Lente Romántica lee a la otra persona — estilo de apego, señales de interés, patrones de reparación, hacia dónde va — desde la conversación que realmente tuvisteis.",
  "Линза расшифровки. Линза Романтика читает другого человека — стиль привязанности, сигналы интереса, паттерны восстановления, куда всё идёт — из реальной переписки, которая у вас была.")
t('"What are they actually telling me?"',
  "« Que me disent-ils vraiment ? »",
  "«¿Qué me están diciendo realmente?»",
  "«Что они мне на самом деле говорят?»")
t("The decoding lens. Romantic Lens analyses two things in parallel: <strong>the other person</strong> (current partner, dating prospect, ex) and <strong>the relationship dynamic between you two</strong>. It reads attachment style, interest signals, repair patterns, and the direction of travel from the conversation you've actually had.",
  "La lentille de décodage. Lentille Romantique analyse deux choses en parallèle : <strong>l'autre personne</strong> (partenaire actuel, prétendant, ex) et <strong>la dynamique relationnelle entre vous</strong>. Elle lit le style d'attachement, les signaux d'intérêt, les patterns de réparation, et la direction du voyage depuis la conversation que vous avez réellement eue.",
  "La lente de decodificación. Lente Romántica analiza dos cosas en paralelo: <strong>a la otra persona</strong> (pareja actual, cita, ex) y <strong>la dinámica relacional entre vosotros</strong>. Lee el estilo de apego, las señales de interés, los patrones de reparación, y la dirección del viaje desde la conversación que realmente tuvisteis.",
  "Линза расшифровки. Линза Романтика анализирует две вещи параллельно: <strong>другого человека</strong> (текущего партнёра, свидание, бывшего) и <strong>динамику отношений между вами</strong>. Она читает стиль привязанности, сигналы интереса, паттерны восстановления, и направление движения из реальной переписки.")
t("Try Romantic Lens free", "Essayer la lentille Romantique gratuitement", "Probar la lente Romántica gratis", "Попробовать линзу Романтика бесплатно")
t("The people who reread screenshots.",
  "Les gens qui relisent les captures d'écran.",
  "La gente que relee capturas de pantalla.",
  "Те, кто перечитывает скриншоты.")
t("The recently-confused", "Le récemment perplexe", "El recientemente confundido", "Недавно растерянный")
t("Something shifted and you can't tell if you're imagining it. You've reread the last week of messages four times. Romantic Lens reads them for you.",
  "Quelque chose a changé et vous ne savez pas si vous l'imaginez. Vous avez relu les messages de la semaine dernière quatre fois. La lentille Romantique les lit pour vous.",
  "Algo cambió y no sabes si te lo estás imaginando. Has releído los mensajes de la última semana cuatro veces. La lente Romántica los lee por ti.",
  "Что-то сдвинулось, и вы не понимаете, кажется ли это вам. Вы перечитали сообщения последней недели четыре раза. Линза Романтика прочитает их за вас.")
t("The dater", "Le célibataire en rencontres", "El que está saliendo", "Тот, кто на свиданиях")
t("Three weeks in, you can't tell if this is going somewhere. The lens reads tempo, reciprocity, and the small tells the chat is giving you.",
  "Trois semaines après, vous ne savez pas si ça mène quelque part. La lentille lit le tempo, la réciprocité, et les petits indices que le chat vous donne.",
  "A las tres semanas, no sabes si esto va a alguna parte. La lente lee el ritmo, la reciprocidad, y las pequeñas pistas que el chat te está dando.",
  "Через три недели вы не понимаете, ведёт ли это куда-то. Линза читает темп, взаимность, и маленькие подсказки, которые даёт чат.")
t("The post-mortem reader", "Le lecteur post-mortem", "El lector de autopsia", "Тот, кто разбирает после")
t("It ended. You want to know what you missed and what wasn't yours to fix. Drop in the chat and let the modules answer.",
  "C'est fini. Vous voulez savoir ce que vous avez manqué et ce qu'il ne vous appartenait pas de réparer. Déposez le chat et laissez les modules répondre.",
  "Terminó. Quieres saber qué te perdiste y qué no era tuyo para arreglar. Suelta el chat y deja que los módulos respondan.",
  "Это закончилось. Вы хотите узнать, что пропустили и что было не вашим, чтобы исправить. Закиньте чат и пусть модули ответят.")
t("The Eleven Modules", "Les onze modules", "Los once módulos", "Одиннадцать модулей")
t("What's inside a Romantic reading.",
  "Ce qu'il y a dans une lecture Romantique.",
  "Qué hay dentro de una lectura Romántica.",
  "Что внутри портрета по линзе Романтика.")
t("Romantic is the lens with the most modules, because the questions are the most varied. You can read all eleven, or jump straight to the one keeping you up.",
  "Romantique est la lentille avec le plus de modules, car les questions sont les plus variées. Vous pouvez lire les onze, ou aller directement à celui qui vous tient éveillé(e).",
  "Romántica es la lente con más módulos, porque las preguntas son las más variadas. Puedes leer los once, o saltar directamente al que te quita el sueño.",
  "Романтика — линза с наибольшим числом модулей, потому что вопросы самые разные. Можно прочитать все одиннадцать или сразу перейти к тому, что не даёт спать.")
t("Relationship Energy Score", "Score d'énergie relationnelle", "Puntuación de energía relacional", "Оценка энергии отношений")
t("Rising · steady · declining. A single line for where the dynamic is heading.",
  "En hausse · stable · en baisse. Une seule ligne pour la direction de la dynamique.",
  "En ascenso · estable · en descenso. Una sola línea para hacia dónde va la dinámica.",
  "Растёт · стабильно · падает. Одна строка о том, куда движется динамика.")
t("Trajectory", "Trajectoire", "Trayectoria", "Траектория")
t("A read on the next three months if nothing changes — and what to change first.",
  "Une lecture sur les trois prochains mois si rien ne change — et ce qu'il faut changer en premier.",
  "Una lectura de los próximos tres meses si nada cambia — y qué cambiar primero.",
  "Прогноз на следующие три месяца, если ничего не поменяется — и что менять первым.")
t("Attachment Indicators", "Indicateurs d'attachement", "Indicadores de apego", "Индикаторы привязанности")
t("Secure, anxious, avoidant, or disorganised — for them. Quoted lines included.",
  "Sécurisé, anxieux, évitant, ou désorganisé — pour eux. Lignes citées incluses.",
  "Seguro, ansioso, evitativo o desorganizado — para ellos. Líneas citadas incluidas.",
  "Безопасный, тревожный, избегающий или дезорганизованный — про них. С процитированными строками.")
t("Interest Signals", "Signaux d'intérêt", "Señales de interés", "Сигналы интереса")
t("Engaged, ambivalent, drifting. Reply tempo, opener rate, who keeps the plan alive.",
  "Engagé, ambivalent, à la dérive. Tempo de réponse, taux d'ouverture, qui maintient le plan en vie.",
  "Comprometido, ambivalente, distanciándose. Ritmo de respuesta, tasa de inicio, quién mantiene el plan vivo.",
  "Вовлечён, амбивалентен, уплывает. Темп ответов, частота инициатив, кто поддерживает план.")
t("Communication Dynamic", "Dynamique de communication", "Dinámica de comunicación", "Динамика общения")
t("Whose words shape the conversation, and how the volume balance has shifted.",
  "Dont les mots façonnent la conversation, et comment l'équilibre du volume s'est déplacé.",
  "Cuyas palabras dan forma a la conversación, y cómo se ha desplazado el equilibrio del volumen.",
  "Чьи слова формируют разговор и как сместился баланс объёма.")
t("Engagement Patterns", "Patterns d'engagement", "Patrones de compromiso", "Паттерны вовлечения")
t("Bid-for-connection moments — what they made, what they accepted, what they let pass.",
  "Moments d'invitation à la connexion — ce qu'ils ont fait, ce qu'ils ont accepté, ce qu'ils ont laissé passer.",
  "Momentos de invitación a la conexión — qué hicieron, qué aceptaron, qué dejaron pasar.",
  "Моменты заявок на связь — что они делали, что принимали, что пропускали.")
t("Emotional Depth", "Profondeur émotionnelle", "Profundidad emocional", "Эмоциональная глубина")
t("How vulnerable the chat actually is. Surface, sincere, or somewhere in between.",
  "À quel point le chat est vraiment vulnérable. Superficiel, sincère, ou quelque part entre les deux.",
  "Cuán vulnerable es realmente el chat. Superficial, sincero, o algo entre medias.",
  "Насколько уязвим этот чат на самом деле. Поверхностный, искренний, или где-то посередине.")
t("Conflict Patterns", "Patterns de conflit", "Patrones de conflicto", "Паттерны конфликтов")
t("How the two of you repair — or don't. Stonewalling, soft starts, contempt, contempt's opposite.",
  "Comment vous deux vous réparez — ou pas. Mur de pierre, démarrages doux, mépris, l'opposé du mépris.",
  "Cómo os reparáis los dos — o no. Muro de piedra, comienzos suaves, desprecio, lo opuesto al desprecio.",
  "Как вы вдвоём восстанавливаетесь — или нет. Стена молчания, мягкие начала, презрение, противоположное презрению.")
t("Green Flags", "Drapeaux verts", "Banderas verdes", "Зелёные флаги")
t("The specific moments that gave you reason to trust them. With receipts.",
  "Les moments spécifiques qui vous ont donné raison de leur faire confiance. Avec preuves.",
  "Los momentos específicos que te dieron razones para confiar en ellos. Con recibos.",
  "Конкретные моменты, давшие вам повод им доверять. С доказательствами.")
t("Caution Areas", "Zones de vigilance", "Áreas de cautela", "Зоны осторожности")
t("Patterns to watch for — without framing them as red flags before you're ready.",
  "Patterns à surveiller — sans les cadrer comme des drapeaux rouges avant que vous ne soyez prêt(e).",
  "Patrones a vigilar — sin enmarcarlos como banderas rojas antes de que estés listo/a.",
  "Паттерны, которые стоит отслеживать — без преждевременной маркировки красными флагами.")
t("Your Patterns", "Vos patterns", "Tus patrones", "Ваши паттерны")
t("What you're bringing into the dynamic. The one place Romantic Lens reads you, gently.",
  "Ce que vous apportez dans la dynamique. Le seul endroit où la lentille Romantique vous lit, avec douceur.",
  "Lo que estás trayendo a la dinámica. El único lugar donde la lente Romántica te lee a ti, con suavidad.",
  "Что вы приносите в динамику. Единственное место, где линза Романтика мягко читает вас.")
t("What Romantic Lens sounds like.",
  "Le ton de la lentille Romantique.",
  "Cómo suena la lente Romántica.",
  "Как звучит линза Романтика.")
t('"He answers warmly, but he answers slowly — averaging four hours and never on weekends. The pattern says \'interested but not prioritising.\' That\'s not a verdict; it\'s a tempo. If you want him to set the pace, this is the pace he is setting."',
  "« Il répond chaleureusement, mais il répond lentement — quatre heures en moyenne, jamais le week-end. Le pattern dit « intéressé mais ne te priorise pas ». Ce n'est pas un verdict ; c'est un tempo. Si vous voulez qu'il donne le rythme, c'est le rythme qu'il donne. »",
  "«Responde con calidez, pero responde lentamente — promediando cuatro horas y nunca los fines de semana. El patrón dice \"interesado pero no priorizando\". No es un veredicto; es un ritmo. Si quieres que él marque el paso, este es el paso que está marcando».",
  "«Он отвечает тепло, но медленно — в среднем четыре часа и никогда в выходные. Паттерн говорит «заинтересован, но не приоритезирует». Это не приговор; это темп. Если вы хотите, чтобы он задавал ритм, вот ритм, который он задаёт.»")
t("What Romantic Lens does — and doesn't.",
  "Ce que fait la lentille Romantique — et ne fait pas.",
  "Lo que hace la lente Romántica — y lo que no.",
  "Что делает линза Романтика — и чего не делает.")
t("What Romantic Lens does", "Ce que fait la lentille Romantique", "Lo que hace la lente Romántica", "Что делает линза Романтика")
t("What Romantic Lens doesn't", "Ce que la lentille Romantique ne fait pas", "Lo que no hace la lente Romántica", "Чего не делает линза Романтика")
t("Reads the <strong>other person's</strong> behaviour from their messages",
  "Lit le comportement de <strong>l'autre personne</strong> depuis ses messages",
  "Lee el comportamiento de <strong>la otra persona</strong> desde sus mensajes",
  "Читает поведение <strong>другого человека</strong> из их сообщений")
t("Names attachment style with specific quoted lines",
  "Nomme le style d'attachement avec des lignes citées spécifiques",
  "Nombra el estilo de apego con líneas citadas específicas",
  "Называет стиль привязанности с конкретными процитированными строками")
t("Tracks tempo, reciprocity, and emotional bid patterns",
  "Suit le tempo, la réciprocité, et les patterns d'appel émotionnel",
  "Sigue el ritmo, la reciprocidad, y los patrones de invitación emocional",
  "Отслеживает темп, взаимность и паттерны эмоциональных заявок")
t("Tells you the trajectory if the conversation continues as-is",
  "Vous dit la trajectoire si la conversation continue telle quelle",
  "Te dice la trayectoria si la conversación continúa así",
  "Говорит вам траекторию, если разговор продолжится как есть")
t("Surfaces what <em>you</em> are bringing into the dynamic, too",
  "Fait remonter aussi ce que <em>vous</em> apportez dans la dynamique",
  "También saca a la luz lo que <em>tú</em> estás trayendo a la dinámica",
  "Также показывает, что <em>вы</em> приносите в динамику")
t("It does not predict whether they'll commit to you",
  "Elle ne prédit pas s'ils s'engageront avec vous",
  "No predice si se comprometerán contigo",
  "Не предсказывает, обяжутся ли они перед вами")
t("It does not diagnose them with personality disorders",
  "Elle ne les diagnostique pas avec des troubles de personnalité",
  "No les diagnostica trastornos de personalidad",
  "Не диагностирует у них расстройства личности")
t("It does not pretend to read minds — only patterns in text",
  "Elle ne prétend pas lire dans les pensées — seulement les patterns dans le texte",
  "No pretende leer mentes — solo patrones en el texto",
  "Не претендует читать мысли — только паттерны в тексте")
t("It does not give scripts to manipulate them with",
  "Elle ne donne pas de scripts pour les manipuler",
  "No da guiones para manipularles",
  "Не даёт сценариев для манипуляций")
t("It does not replace conversation. The hardest move is still yours.",
  "Elle ne remplace pas la conversation. Le mouvement le plus dur reste le vôtre.",
  "No reemplaza la conversación. El movimiento más difícil sigue siendo tuyo.",
  "Не заменяет разговор. Самый трудный шаг всё ещё за вами.")
t("One reading. Eleven modules. Free.",
  "Une lecture. Onze modules. Gratuit.",
  "Una lectura. Once módulos. Gratis.",
  "Один портрет. Одиннадцать модулей. Бесплатно.")
t("Drop in the conversation, choose Romantic, and get the full report in under three minutes.",
  "Déposez la conversation, choisissez Romantique, et obtenez le rapport complet en moins de trois minutes.",
  "Suelta la conversación, elige Romántica, y recibe el reporte completo en menos de tres minutos.",
  "Закиньте переписку, выберите Романтика, и получите полный отчёт менее чем за три минуты.")

print("Translation map size (so far):", len(T), "entries")


# ============================================================
# LENS-FRIENDSHIP — full body
# ============================================================
t("Friendship Lens — Persona Lens", "Lentille Amitié — Persona Lens", "Lente Amistad — Persona Lens", "Линза Дружба — Persona Lens")
t("The dyadic friendship lens. Reads both friends as co-equal subjects — friendship archetype, communication DNA, give-and-take, watch zones.",
  "La lentille d'amitié dyadique. Lit les deux amis comme sujets co-égaux — archétype d'amitié, ADN de communication, équilibre des échanges, zones de vigilance.",
  "La lente de amistad diádica. Lee a ambos amigos como sujetos co-iguales — arquetipo de amistad, ADN de comunicación, equilibrio en los intercambios, zonas de vigilancia.",
  "Диадическая линза дружбы. Читает обоих друзей как равноправных субъектов — архетип дружбы, ДНК общения, баланс взаимного обмена, зоны внимания.")
t('"What kind of friendship is this, actually?"',
  "« Quel genre d'amitié est-ce, en fait ? »",
  "«¿Qué tipo de amistad es esta, en realidad?»",
  "«Что это за дружба, на самом деле?»")
t("Friendship Lens analyses two things: <strong>the other person</strong> (your friend) and <strong>the friendship dynamic between you two</strong>. It finds the archetype, the communication DNA, the give-and-take rhythm, and the moments where the friendship is being quietly tested — or quietly rewarded.",
  "La lentille Amitié analyse deux choses : <strong>l'autre personne</strong> (votre ami(e)) et <strong>la dynamique d'amitié entre vous deux</strong>. Elle trouve l'archétype, l'ADN de communication, le rythme des échanges, et les moments où l'amitié est silencieusement testée — ou silencieusement récompensée.",
  "La lente Amistad analiza dos cosas: <strong>a la otra persona</strong> (tu amigo/a) y <strong>la dinámica de amistad entre vosotros</strong>. Encuentra el arquetipo, el ADN de comunicación, el ritmo de intercambios, y los momentos donde la amistad está siendo silenciosamente puesta a prueba — o silenciosamente recompensada.",
  "Линза Дружба анализирует две вещи: <strong>другого человека</strong> (вашего друга) и <strong>динамику дружбы между вами</strong>. Она находит архетип, ДНК общения, ритм взаимного обмена, и моменты, где дружба тихо проверяется — или тихо вознаграждается.")
t("Try Friendship Lens free", "Essayer la lentille Amitié gratuitement", "Probar la lente Amistad gratis", "Попробовать линзу Дружба бесплатно")
t("Three reasons people run it.",
  "Trois raisons pour lesquelles les gens la lancent.",
  "Tres razones por las que la gente la ejecuta.",
  "Три причины, по которым её запускают.")
t('The "are we drifting?" reader',
  "Le lecteur « est-ce qu'on s'éloigne ? »",
  "El que pregunta «¿nos estamos distanciando?»",
  "Тот, кто спрашивает «мы отдаляемся?»")
t("You haven't fought. You just notice the chat is quieter. Friendship Lens finds the words for what changed.",
  "Vous ne vous êtes pas disputés. Vous remarquez juste que le chat est plus calme. La lentille Amitié trouve les mots pour ce qui a changé.",
  "No habéis discutido. Solo notas que el chat está más silencioso. La lente Amistad encuentra las palabras para lo que cambió.",
  "Вы не ссорились. Просто заметили, что чат стал тише. Линза Дружба находит слова для того, что изменилось.")
t('The "we\'re hilarious together" reader',
  "Le lecteur « on est hilarants ensemble »",
  "El que dice «somos divertidísimos juntos»",
  "Тот, кто говорит «нам вместе уморительно»")
t("You want a love letter to the friendship. The Communication DNA module is built for screenshots.",
  "Vous voulez une lettre d'amour à l'amitié. Le module ADN de Communication est construit pour les screenshots.",
  "Quieres una carta de amor a la amistad. El módulo ADN de Comunicación está hecho para capturas.",
  "Хотите любовное письмо дружбе. Модуль ДНК общения создан под скриншоты.")
t('The "am I doing too much?" reader',
  "Le lecteur « est-ce que j'en fais trop ? »",
  "El que se pregunta «¿estoy haciendo demasiado?»",
  "Тот, кто спрашивает «не делаю ли я слишком много?»")
t("Give-and-Take tells you who's holding the rope right now — and whether the imbalance is recent or always.",
  "Le module Équilibre des échanges vous dit qui tient la corde en ce moment — et si le déséquilibre est récent ou de toujours.",
  "Equilibrio de Intercambios te dice quién sostiene la cuerda ahora mismo — y si el desequilibrio es reciente o de siempre.",
  "Модуль баланса говорит, кто сейчас держит верёвку — и появился ли дисбаланс недавно или был всегда.")
t("The Modules", "Les modules", "Los módulos", "Модули")
t("What's inside a Friendship reading.",
  "Ce qu'il y a dans une lecture Amitié.",
  "Qué hay dentro de una lectura Amistad.",
  "Что внутри портрета по линзе Дружба.")
t("Friendship Archetype", "Archétype d'amitié", "Arquetipo de amistad", "Архетип дружбы")
t('One named pair for both of you — "The Ride-or-Die", "The Wise Counsel", "The Anchor & The Spark", "The Old-Friend Cadence", and others.',
  "Une paire nommée pour vous deux — « Les Inséparables », « Le Conseiller Sage », « L'Ancre et l'Étincelle », « La Cadence du Vieil Ami », et d'autres.",
  "Una pareja nombrada para ambos — «Hasta la Muerte», «El Consejero Sabio», «El Ancla y la Chispa», «La Cadencia del Viejo Amigo», y otras.",
  "Названная пара для вас двоих — «До конца», «Мудрый советник», «Якорь и искра», «Каденция старого друга», и другие.")
t("Communication DNA", "ADN de communication", "ADN de comunicación", "ДНК общения")
t("How you two actually talk. Banter rhythm, callback rate, the in-jokes still working.",
  "Comment vous parlez vraiment tous les deux. Rythme des taquineries, taux de rappel, les blagues internes qui fonctionnent encore.",
  "Cómo habláis los dos en realidad. Ritmo de bromas, tasa de retorno, los chistes internos que aún funcionan.",
  "Как вы двое реально говорите. Ритм подколок, частота возвращений к теме, внутренние шутки, которые ещё работают.")
t("Friendship Pulse", "Pouls de l'amitié", "Pulso de la amistad", "Пульс дружбы")
t("Is it growing, steady, or quietly cooling? With the specific moments behind the verdict.",
  "Grandit-elle, stable, ou refroidit-elle silencieusement ? Avec les moments spécifiques derrière le verdict.",
  "¿Está creciendo, estable, o enfriándose en silencio? Con los momentos específicos detrás del veredicto.",
  "Растёт ли, стабильна или тихо остывает? С конкретными моментами за вердиктом.")
t("Give &amp; Take", "Équilibre des échanges", "Equilibrio de Intercambios", "Баланс взаимного обмена")
t("Reciprocity score. Who chases the plans, who holds the emotional load, who shows up first.",
  "Score de réciprocité. Qui chasse les plans, qui porte la charge émotionnelle, qui arrive en premier.",
  "Puntuación de reciprocidad. Quién persigue los planes, quién carga el peso emocional, quién aparece primero.",
  "Оценка взаимности. Кто гоняется за планами, кто несёт эмоциональную нагрузку, кто появляется первым.")
t("How much real talk lives in the chat — and how much it's swapped between you.",
  "Combien de vraies conversations vivent dans le chat — et à quel point elles sont échangées entre vous.",
  "Cuánto «hablar de verdad» vive en el chat — y cuánto se intercambia entre vosotros.",
  "Сколько настоящего разговора живёт в чате — и насколько он распределён между вами.")
t("Friendship Patterns", "Patterns d'amitié", "Patrones de amistad", "Паттерны дружбы")
t("The loops you fall into. Sometimes endearing, sometimes a tell.",
  "Les boucles dans lesquelles vous tombez. Parfois attendrissantes, parfois révélatrices.",
  "Los bucles en los que caéis. A veces entrañables, a veces reveladores.",
  "Циклы, в которые вы попадаете. Иногда трогательные, иногда показательные.")
t("Where this friendship is heading at its current trajectory — and what would change it.",
  "Où va cette amitié sur sa trajectoire actuelle — et ce qui la changerait.",
  "Hacia dónde va esta amistad en su trayectoria actual — y qué la cambiaría.",
  "Куда движется эта дружба по текущей траектории — и что её изменит.")
t("Loyalty signals. Trust under pressure. The receipts of why this friendship is real.",
  "Signaux de loyauté. Confiance sous pression. Les preuves que cette amitié est réelle.",
  "Señales de lealtad. Confianza bajo presión. Los recibos de por qué esta amistad es real.",
  "Сигналы лояльности. Доверие под давлением. Доказательства того, что эта дружба настоящая.")
t("Watch Zones", "Zones de vigilance", "Zonas de vigilancia", "Зоны внимания")
t("The fading inside joke, the one-sided effort, the slow ghost. Named gently.",
  "La blague interne qui s'estompe, l'effort unilatéral, le fantôme lent. Nommés avec douceur.",
  "El chiste interno que se desvanece, el esfuerzo unilateral, el fantasma lento. Nombrados con suavidad.",
  "Затухающая внутренняя шутка, односторонние усилия, медленное исчезновение. Названо мягко.")
t("A finished image of your Friendship Archetype — designed to be sent to that exact friend.",
  "Une image finalisée de votre Archétype d'Amitié — conçue pour être envoyée à cet ami précis.",
  "Una imagen finalizada de tu Arquetipo de Amistad — diseñada para ser enviada a ese amigo específico.",
  "Готовое изображение вашего Архетипа Дружбы — сделано, чтобы отправить именно этому другу.")
t("What Friendship Lens sounds like.",
  "Le ton de la lentille Amitié.",
  "Cómo suena la lente Amistad.",
  "Как звучит линза Дружба.")
t('"You two are a Ride-or-Die / Wise Counsel pair. She brings the storm; you bring the lighthouse. The chat is at its best when one of you is in crisis — which is also why the quiet weeks feel weird. Nothing\'s wrong. You just don\'t perform calm together yet."',
  "« Vous deux êtes une paire Inséparables / Conseiller Sage. Elle apporte la tempête ; vous apportez le phare. Le chat est à son meilleur quand l'un de vous est en crise — c'est aussi pourquoi les semaines calmes paraissent bizarres. Rien ne va mal. Vous ne savez juste pas encore performer le calme ensemble. »",
  "«Vosotras dos sois una pareja Hasta-la-Muerte / Consejera Sabia. Ella trae la tormenta; tú traes el faro. El chat está en su mejor momento cuando una de vosotras está en crisis — que es también por lo que las semanas tranquilas se sienten raras. No pasa nada. Simplemente aún no actuáis la calma juntas».",
  "«Вы двое — пара До-конца / Мудрый советник. Она приносит шторм; вы приносите маяк. Чат в лучшей форме, когда одна из вас в кризисе — поэтому тихие недели и кажутся странными. Ничего не сломано. Вы просто ещё не умеете спокойствие вместе.»")
t("What Friendship Lens does — and doesn't.",
  "Ce que fait la lentille Amitié — et ne fait pas.",
  "Lo que hace la lente Amistad — y lo que no.",
  "Что делает линза Дружба — и чего не делает.")
t("What Friendship Lens does", "Ce que fait la lentille Amitié", "Lo que hace la lente Amistad", "Что делает линза Дружба")
t("What Friendship Lens doesn't", "Ce que la lentille Amitié ne fait pas", "Lo que no hace la lente Amistad", "Чего не делает линза Дружба")
t("Reads <strong>both</strong> friends as equally interesting subjects",
  "Lit <strong>les deux</strong> amis comme sujets également intéressants",
  "Lee a <strong>ambos</strong> amigos como sujetos igualmente interesantes",
  "Читает <strong>обоих</strong> друзей как одинаково интересных субъектов")
t("Names the dynamic — not just the people",
  "Nomme la dynamique — pas seulement les personnes",
  "Nombra la dinámica — no solo a las personas",
  "Называет динамику — не только людей")
t("Surfaces the quiet drift before you'd have noticed it",
  "Fait remonter la dérive silencieuse avant que vous ne l'auriez remarquée",
  "Saca a la luz la deriva silenciosa antes de que la hubieras notado",
  "Выявляет тихий дрейф раньше, чем вы бы заметили")
t("Celebrates the in-jokes that are still working",
  "Célèbre les blagues internes qui fonctionnent encore",
  "Celebra los chistes internos que aún funcionan",
  "Празднует внутренние шутки, которые ещё работают")
t("Gives you a card the friend will actually want screenshotted",
  "Vous donne une carte que l'ami(e) voudra vraiment capturer en screenshot",
  "Te da una tarjeta que el amigo realmente querrá capturar",
  "Даёт вам карточку, которую друг реально захочет скриншотнуть")
t("It does not decide who the better friend is",
  "Elle ne décide pas qui est le meilleur ami",
  "No decide quién es el mejor amigo",
  "Не решает, кто из вас лучший друг")
t("It does not give one of you a higher score than the other",
  "Elle ne donne pas à l'un de vous un score plus élevé qu'à l'autre",
  "No le da a uno de vosotros una puntuación más alta que al otro",
  "Не даёт одному из вас более высокий балл, чем другому")
t('It does not declare a friendship "over" — only describes the trajectory',
  "Elle ne déclare pas une amitié « terminée » — décrit seulement la trajectoire",
  "No declara una amistad «terminada» — solo describe la trayectoria",
  "Не объявляет дружбу «оконченной» — только описывает траекторию")
t("It does not work well on chats shorter than ~50 messages",
  "Elle ne fonctionne pas bien sur les chats de moins de ~50 messages",
  "No funciona bien en chats de menos de ~50 mensajes",
  "Плохо работает на чатах короче ~50 сообщений")
t("It is not the right lens for romantic ambiguity (use Romantic)",
  "Ce n'est pas la bonne lentille pour l'ambiguïté romantique (utilisez Romantique)",
  "No es la lente adecuada para la ambigüedad romántica (usa Romántica)",
  "Это не та линза для романтической неопределённости (используйте Романтика)")
t("The lens with the highest tag-a-friend rate.",
  "La lentille avec le plus haut taux de « tagger un ami ».",
  "La lente con la mayor tasa de etiquetar a un amigo.",
  "Линза с самой высокой частотой «отметь друга».")
t("Run it on a chat with a friend. Send them the card. Watch the reply.",
  "Lancez-la sur un chat avec un ami. Envoyez-lui la carte. Regardez la réponse.",
  "Ejecútala en un chat con un amigo. Envíale la tarjeta. Mira la respuesta.",
  "Запустите её на чате с другом. Отправьте им карточку. Посмотрите на ответ.")

# ============================================================
# LENS-PROFESSIONAL
# ============================================================
t("Professional Lens — Persona Lens", "Lentille Professionnelle — Persona Lens", "Lente Profesional — Persona Lens", "Линза Работа — Persona Lens")
t("The work-decoding lens. Reads a manager, colleague, client or business partner — workplace archetype, power and influence, EI at work, how to actually pitch them.",
  "La lentille de décodage du travail. Lit un manager, un collègue, un client ou un partenaire commercial — archétype de travail, pouvoir et influence, IE au travail, comment leur présenter une idée pour de vrai.",
  "La lente decodificadora del trabajo. Lee a un manager, colega, cliente o socio comercial — arquetipo laboral, poder e influencia, IE en el trabajo, cómo presentarles una idea de verdad.",
  "Линза расшифровки работы. Читает менеджера, коллегу, клиента или делового партнёра — рабочий архетип, власть и влияние, ЭИ на работе, как им реально подать идею.")
t('"How do I actually operate with this person?"',
  "« Comment dois-je vraiment opérer avec cette personne ? »",
  "«¿Cómo opero realmente con esta persona?»",
  "«Как мне на самом деле работать с этим человеком?»")
t("The work-decoding lens. Professional Lens analyses two things: <strong>your colleague</strong> (manager, peer, client, or business partner) and <strong>the working dynamic between you two</strong>. Drop in a Slack thread or an email exchange, and you get a strategic read on how to operate inside that working relationship — not what they're like at home, what they're like across this table.",
  "La lentille de décodage du travail. Lentille Professionnelle analyse deux choses : <strong>votre collègue</strong> (manager, pair, client, ou partenaire commercial) et <strong>la dynamique de travail entre vous deux</strong>. Déposez un fil Slack ou un échange d'emails, et vous obtenez une lecture stratégique sur comment opérer dans cette relation de travail — pas comment ils sont chez eux, comment ils sont en face de cette table.",
  "La lente decodificadora del trabajo. Lente Profesional analiza dos cosas: <strong>a tu colega</strong> (manager, par, cliente o socio comercial) y <strong>la dinámica de trabajo entre vosotros</strong>. Suelta un hilo de Slack o un intercambio de emails, y obtienes una lectura estratégica sobre cómo operar dentro de esa relación laboral — no cómo son en casa, cómo son al otro lado de esta mesa.",
  "Линза расшифровки работы. Линза Работа анализирует две вещи: <strong>вашего коллегу</strong> (менеджера, равного, клиента или делового партнёра) и <strong>рабочую динамику между вами</strong>. Закиньте тред Slack или обмен email, и получите стратегический разбор того, как действовать внутри этих рабочих отношений — не какие они дома, а какие они через этот стол.")
t("Try Professional Lens free", "Essayer la lentille Professionnelle gratuitement", "Probar la lente Profesional gratis", "Попробовать линзу Работа бесплатно")
t("The new hire", "Le nouvel embauché", "El recién contratado", "Новичок")
t("You can't tell yet what your manager actually wants. Professional Lens reads their tells in three weeks of Slack and tells you.",
  "Vous ne savez pas encore ce que votre manager veut vraiment. La lentille Professionnelle lit ses indices dans trois semaines de Slack et vous le dit.",
  "Aún no sabes lo que tu manager realmente quiere. La lente Profesional lee sus pistas en tres semanas de Slack y te lo dice.",
  "Вы ещё не понимаете, чего на самом деле хочет ваш менеджер. Линза Работа читает его подсказки в трёх неделях Slack и говорит вам.")
t("The negotiator", "Le négociateur", "El negociador", "Переговорщик")
t("You're about to ask for a raise, push back on scope, or bring up a hard call. The lens tells you how this specific person likes to be approached.",
  "Vous êtes sur le point de demander une augmentation, de repousser un scope, ou d'aborder une décision difficile. La lentille vous dit comment cette personne précise aime être abordée.",
  "Estás a punto de pedir un aumento, rechazar un alcance, o plantear una decisión difícil. La lente te dice cómo le gusta ser abordada a esta persona específica.",
  "Вы собираетесь попросить прибавку, оспорить объём работ или поднять трудный вопрос. Линза говорит, как именно этот конкретный человек любит, чтобы к нему подходили.")
t("The interim leader", "Le leader intérimaire", "El líder interino", "Временный руководитель")
t("You inherited a team you didn't pick. Run the lens on the messages of each direct report and get a quick read on each.",
  "Vous avez hérité d'une équipe que vous n'avez pas choisie. Lancez la lentille sur les messages de chaque collaborateur direct et obtenez une lecture rapide de chacun.",
  "Heredaste un equipo que no elegiste. Ejecuta la lente en los mensajes de cada subordinado directo y obtén una lectura rápida de cada uno.",
  "Вам досталась команда, которую вы не выбирали. Запустите линзу на сообщениях каждого подчинённого и получите быстрый разбор каждого.")
t("What's inside a Professional reading.",
  "Ce qu'il y a dans une lecture Professionnelle.",
  "Qué hay dentro de una lectura Profesional.",
  "Что внутри портрета по линзе Работа.")
t("Workplace Archetype", "Archétype de travail", "Arquetipo laboral", "Рабочий архетип")
t("Strategist, Diplomat, Executor, Ghost, Architect, Operator. A named profile with the specific lines behind it.",
  "Stratège, Diplomate, Exécutant, Fantôme, Architecte, Opérateur. Un profil nommé avec les lignes spécifiques derrière.",
  "Estratega, Diplomático, Ejecutor, Fantasma, Arquitecto, Operador. Un perfil nombrado con las líneas específicas detrás.",
  "Стратег, Дипломат, Исполнитель, Призрак, Архитектор, Оператор. Названный профиль с конкретными строками за ним.")
t("Power &amp; Influence Map", "Carte du pouvoir et de l'influence", "Mapa de Poder e Influencia", "Карта власти и влияния")
t("How this person actually moves things. Reference power, expert power, the soft levers they pull.",
  "Comment cette personne fait vraiment bouger les choses. Pouvoir de référence, pouvoir d'expert, les leviers doux qu'elle utilise.",
  "Cómo esta persona realmente mueve las cosas. Poder de referencia, poder experto, las palancas suaves que tira.",
  "Как этот человек реально двигает вещи. Власть авторитета, экспертная власть, мягкие рычаги, которые он использует.")
t("Communication Effectiveness", "Efficacité de la communication", "Efectividad de la comunicación", "Эффективность коммуникации")
t("What lands with them. Bullets or context. Numbers or stories. Speed or precision.",
  "Ce qui marche avec eux. Puces ou contexte. Chiffres ou histoires. Vitesse ou précision.",
  "Lo que les llega. Viñetas o contexto. Números o historias. Velocidad o precisión.",
  "Что до них доходит. Списки или контекст. Цифры или истории. Скорость или точность.")
t("Emotional Intelligence at Work", "Intelligence émotionnelle au travail", "Inteligencia Emocional en el Trabajo", "Эмоциональный интеллект на работе")
t("Self-awareness, regulation, empathy — calibrated for the work setting, not the date.",
  "Conscience de soi, régulation, empathie — calibrés pour le contexte professionnel, pas pour le rendez-vous.",
  "Autoconocimiento, regulación, empatía — calibrados para el contexto laboral, no para la cita.",
  "Самосознание, регуляция, эмпатия — откалибровано для рабочей обстановки, не для свидания.")
t("Collaboration Style", "Style de collaboration", "Estilo de colaboración", "Стиль совместной работы")
t("How they want to work with you — drafts shown early, drafts shown polished, decisions in DM or in meetings.",
  "Comment ils veulent travailler avec vous — brouillons montrés tôt, brouillons montrés polis, décisions en DM ou en réunions.",
  "Cómo quieren trabajar contigo — borradores mostrados pronto, borradores mostrados pulidos, decisiones en DM o en reuniones.",
  "Как они хотят работать с вами — черновики показывают рано, черновики показывают отполированными, решения в DM или на встречах.")
t("Professional Dynamic", "Dynamique professionnelle", "Dinámica profesional", "Профессиональная динамика")
t("The relationship pattern between you two. Manager-IC, peer, client-vendor, the asymmetries that matter.",
  "Le pattern relationnel entre vous deux. Manager-IC, pair, client-fournisseur, les asymétries qui comptent.",
  "El patrón relacional entre vosotros. Manager-IC, par, cliente-proveedor, las asimetrías que importan.",
  "Паттерн отношений между вами двумя. Менеджер-исполнитель, равный, клиент-поставщик, асимметрии, которые важны.")
t("The one place the lens turns the mirror back on you — gently, with one specific suggestion.",
  "Le seul endroit où la lentille retourne le miroir vers vous — avec douceur, avec une suggestion spécifique.",
  "El único lugar donde la lente gira el espejo hacia ti — con suavidad, con una sugerencia específica.",
  "Единственное место, где линза разворачивает зеркало на вас — мягко, с одним конкретным предложением.")
t("The behaviour you can trust about this person. The receipts.",
  "Le comportement auquel vous pouvez faire confiance chez cette personne. Les preuves.",
  "El comportamiento en el que puedes confiar de esta persona. Los recibos.",
  "Поведение, которому можно доверять у этого человека. Доказательства.")
t('The tells worth tracking — not "red flags", just "watch this".',
  "Les indices qui valent la peine d'être suivis — pas « drapeaux rouges », juste « observez ceci ».",
  "Las pistas que vale la pena seguir — no «banderas rojas», solo «observa esto».",
  "Подсказки, которые стоит отслеживать — не «красные флаги», просто «понаблюдайте за этим».")
t("Where this working relationship is heading and the next move worth making.",
  "Où cette relation de travail se dirige et le prochain mouvement qui vaut la peine d'être fait.",
  "Hacia dónde va esta relación laboral y el próximo movimiento que vale la pena hacer.",
  "Куда движутся эти рабочие отношения, и какой следующий шаг стоит сделать.")
t("What Professional Lens sounds like.",
  "Le ton de la lentille Professionnelle.",
  "Cómo suena la lente Profesional.",
  "Как звучит линза Работа.")
t('"Your manager is a Strategist. She decides in meetings but commits in writing, and she\'ll always prefer the version of your idea that ends with a number. If you bring her this proposal as bullets-then-decision-needed, she\'ll say yes in the meeting. If you bring it as story-then-context, she\'ll thank you and follow up next week. Choose your day."',
  "« Votre manager est une Stratège. Elle décide en réunion mais s'engage par écrit, et elle préférera toujours la version de votre idée qui se termine par un chiffre. Si vous lui apportez cette proposition en mode puces-puis-décision-requise, elle dira oui en réunion. Si vous la présentez comme histoire-puis-contexte, elle vous remerciera et reviendra la semaine d'après. Choisissez votre jour. »",
  "«Tu manager es una Estratega. Decide en reuniones pero se compromete por escrito, y siempre preferirá la versión de tu idea que termina con un número. Si le llevas esta propuesta como viñetas-luego-decisión, dirá que sí en la reunión. Si se la llevas como historia-luego-contexto, te dará las gracias y volverá la semana siguiente. Elige tu día».",
  "«Ваш менеджер — Стратег. Решает на встречах, но коммитится письменно, и всегда предпочтёт версию вашей идеи, которая заканчивается цифрой. Если принесёте предложение в формате тезисы-потом-нужно-решение, она скажет «да» прямо на встрече. Если в формате история-потом-контекст, она поблагодарит и вернётся через неделю. Выбирайте день.»")
t("What Professional Lens does — and doesn't.",
  "Ce que fait la lentille Professionnelle — et ne fait pas.",
  "Lo que hace la lente Profesional — y lo que no.",
  "Что делает линза Работа — и чего не делает.")
t("What Professional Lens does", "Ce que fait la lentille Professionnelle", "Lo que hace la lente Profesional", "Что делает линза Работа")
t("What Professional Lens doesn't", "Ce que la lentille Professionnelle ne fait pas", "Lo que no hace la lente Profesional", "Чего не делает линза Работа")
t("Reads the <strong>other person's</strong> work behaviour from their messages",
  "Lit le comportement de travail de <strong>l'autre personne</strong> depuis ses messages",
  "Lee el comportamiento laboral de <strong>la otra persona</strong> desde sus mensajes",
  "Читает рабочее поведение <strong>другого человека</strong> из их сообщений")
t("Names their workplace archetype and the power they actually wield",
  "Nomme leur archétype de travail et le pouvoir qu'ils détiennent réellement",
  "Nombra su arquetipo laboral y el poder que realmente ejercen",
  "Называет их рабочий архетип и власть, которой они реально владеют")
t("Tells you the format their decisions like to arrive in",
  "Vous dit le format dans lequel leurs décisions aiment arriver",
  "Te dice el formato en el que les gusta que lleguen sus decisiones",
  "Говорит вам, в каком формате их решения любят приходить")
t("Surfaces what you're bringing into the dynamic, with one suggestion",
  "Fait remonter ce que vous apportez dans la dynamique, avec une suggestion",
  "Saca a la luz lo que estás trayendo a la dinámica, con una sugerencia",
  "Показывает, что вы приносите в динамику, с одним предложением")
t("Speaks the strategy language — not the wellness language",
  "Parle le langage de la stratégie — pas celui du bien-être",
  "Habla el lenguaje de la estrategia — no el del bienestar",
  "Говорит языком стратегии — не языком велнеса.")
t("It is <strong>not an HR product</strong>. Enterprise / hiring use is out of scope.",
  "Ce n'est <strong>pas un produit RH</strong>. L'utilisation entreprise / recrutement est hors périmètre.",
  "<strong>No es un producto de RRHH</strong>. El uso empresarial / contratación está fuera de alcance.",
  "Это <strong>не HR-продукт</strong>. Корпоративное / рекрутинговое использование вне рамок.")
t('It does not score people. There\'s no "leadership grade".',
  "Elle ne note pas les gens. Il n'y a pas de « grade de leadership ».",
  "No puntúa a la gente. No hay «nota de liderazgo».",
  "Не оценивает людей в баллах. Нет «оценки лидерства».")
t("It does not predict job performance.",
  "Elle ne prédit pas la performance professionnelle.",
  "No predice el rendimiento laboral.",
  "Не предсказывает рабочую эффективность.")
t("It does not surface anything you couldn't responsibly observe yourself.",
  "Elle ne fait remonter rien que vous ne pourriez observer vous-même de manière responsable.",
  "No saca a la luz nada que no pudieras observar tú mismo de forma responsable.",
  "Не показывает того, что вы не могли бы ответственно наблюдать сами.")
t("It is not a license to manipulate. The strategic guidance is for clarity, not control.",
  "Ce n'est pas une licence pour manipuler. Le guidage stratégique est pour la clarté, pas pour le contrôle.",
  "No es una licencia para manipular. La guía estratégica es para la claridad, no para el control.",
  "Это не лицензия на манипуляцию. Стратегическое руководство — для ясности, не для контроля.")
t("The lens that goes on LinkedIn.",
  "La lentille qui va sur LinkedIn.",
  "La lente que va a LinkedIn.",
  "Линза, которая идёт в LinkedIn.")
t("Drop in a work chat, choose Professional, and walk into your next 1:1 with a plan.",
  "Déposez un chat de travail, choisissez Professionnelle, et entrez dans votre prochain 1:1 avec un plan.",
  "Suelta un chat de trabajo, elige Profesional, y entra en tu próximo 1:1 con un plan.",
  "Закиньте рабочий чат, выберите Работа, и идите на следующий 1:1 с планом.")

print("After P-lens additions:", len(T), "entries")


# ============================================================
# LENS-FAMILY
# ============================================================
t("Family Lens — Persona Lens", "Lentille Famille — Persona Lens", "Lente Familia — Persona Lens", "Линза Семья — Persona Lens")
t("A 1:1 family-relationship analysis viewed through a family-systems lens. Communication Archaeology, Inherited Scripts, Roles &amp; Scripts, Emotional Ledger, Boundary Landscape.",
  "Une analyse 1:1 d'une relation familiale vue à travers une lentille systémique familiale. Archéologie de la Communication, Scripts Hérités, Rôles et Scripts, Registre Émotionnel, Paysage des Frontières.",
  "Un análisis 1:1 de una relación familiar visto a través de una lente sistémica familiar. Arqueología de la Comunicación, Guiones Heredados, Roles y Guiones, Libro de Cuentas Emocional, Paisaje de Límites.",
  "Анализ 1:1 семейных отношений через призму семейных систем. Археология коммуникации, Унаследованные сценарии, Роли и сценарии, Эмоциональная бухгалтерия, Ландшафт границ.")
t('"Why do we keep falling into the same script?"',
  "« Pourquoi continuons-nous à tomber dans le même script ? »",
  "«¿Por qué seguimos cayendo en el mismo guión?»",
  "«Почему мы продолжаем попадать в один и тот же сценарий?»")
t("Family Lens analyses <strong>both of you</strong> — you and one specific relative (parent, sibling, in-law) — through a family-systems lens. It surfaces the inherited language, the roles each of you has slipped into over the years, and the patterns the two of you keep rehearsing without noticing.",
  "La lentille Famille analyse <strong>vous deux</strong> — vous et un membre spécifique de la famille (parent, frère/sœur, belle-famille) — à travers une lentille systémique familiale. Elle fait remonter le langage hérité, les rôles dans lesquels chacun de vous s'est glissé au fil des années, et les patterns que vous répétez sans vous en rendre compte.",
  "La lente Familia os analiza <strong>a ambos</strong> — a ti y a un familiar específico (padre/madre, hermano/a, suegros) — a través de una lente sistémica familiar. Saca a la luz el lenguaje heredado, los roles en los que cada uno habéis caído con los años, y los patrones que los dos seguís ensayando sin daros cuenta.",
  "Линза Семья анализирует <strong>вас обоих</strong> — вас и одного конкретного родственника (родителя, брата/сестру, родственника по браку) — через призму семейных систем. Она показывает унаследованный язык, роли, в которые каждый из вас вошёл за годы, и паттерны, которые вы вдвоём продолжаете отрабатывать незаметно.")
t("Try Family Lens free", "Essayer la lentille Famille gratuitement", "Probar la lente Familia gratis", "Попробовать линзу Семья бесплатно")
t("The adult child", "L'enfant adulte", "El hijo adulto", "Взрослый ребёнок")
t("You've noticed yourself sounding like your mother in your sibling chat. The lens shows you exactly which phrases — and where they came from.",
  "Vous vous êtes surpris(e) à ressembler à votre mère dans le chat avec votre frère/sœur. La lentille vous montre exactement quelles phrases — et d'où elles viennent.",
  "Te has notado sonando como tu madre en el chat con tu hermano/a. La lente te muestra exactamente qué frases — y de dónde vienen.",
  "Вы заметили, что в чате с братом/сестрой звучите как ваша мать. Линза показывает вам, какие именно фразы — и откуда они пришли.")
t("The peace-keeper", "Le gardien de la paix", "El que mantiene la paz", "Хранитель мира")
t("You always end up being the one who smooths things over. Family Lens names the role you've inherited and tells you what it costs you.",
  "Vous finissez toujours par être celui/celle qui lisse les choses. La lentille Famille nomme le rôle que vous avez hérité et vous dit ce qu'il vous coûte.",
  "Siempre acabas siendo el/la que suaviza las cosas. La lente Familia nombra el rol que has heredado y te dice lo que te cuesta.",
  "Вы всегда оказываетесь тем, кто всё сглаживает. Линза Семья называет роль, которую вы унаследовали, и говорит, чего она вам стоит.")
t("The reluctant family-chat reader", "Le lecteur réticent du chat familial", "El lector reticente del chat familiar", "Неохотный читатель семейного чата")
t("You scroll without replying. The lens reads who actually carries the chat and who fades — and asks if that's the deal you want.",
  "Vous faites défiler sans répondre. La lentille lit qui porte vraiment le chat et qui s'efface — et demande si c'est l'accord que vous voulez.",
  "Haces scroll sin responder. La lente lee quién realmente lleva el chat y quién se desvanece — y pregunta si ese es el trato que quieres.",
  "Вы прокручиваете, не отвечая. Линза читает, кто реально несёт чат, а кто исчезает — и спрашивает, такой ли договор вы хотите.")
t("What's inside a Family reading.",
  "Ce qu'il y a dans une lecture Famille.",
  "Qué hay dentro de una lectura Familia.",
  "Что внутри портрета по линзе Семья.")
t("Communication Archaeology", "Archéologie de la Communication", "Arqueología de la Comunicación", "Археология коммуникации")
t('The unspoken rules between you and this relative. The "we don\'t talk about" topics. The deflection moves you both use.',
  "Les règles non dites entre vous et ce membre de la famille. Les sujets « dont on ne parle pas ». Les mouvements de diversion que vous utilisez tous les deux.",
  "Las reglas no escritas entre tú y este familiar. Los temas «de los que no hablamos». Los movimientos de evasión que ambos usáis.",
  "Невысказанные правила между вами и этим родственником. Темы «о которых мы не говорим». Уклонения, которые вы оба используете.")
t("Inherited Scripts", "Scripts hérités", "Guiones heredados", "Унаследованные сценарии")
t("The phrases your parents said that you now text. Specific lines, quoted, with the lineage drawn.",
  "Les phrases que vos parents disaient que vous envoyez maintenant par texto. Lignes spécifiques, citées, avec la lignée tracée.",
  "Las frases que decían tus padres que ahora envías por mensaje. Líneas específicas, citadas, con el linaje trazado.",
  "Фразы, которые говорили ваши родители, и которые вы теперь пишете в сообщениях. Конкретные строки, процитированные, с прорисованной линией наследования.")
t("Roles &amp; Scripts", "Rôles et scripts", "Roles y guiones", "Роли и сценарии")
t("Caretaker, Mediator, Rebel, Peacekeeper, Lost Child, Hero, Scapegoat — and which one you've slipped into here.",
  "Soignant, Médiateur, Rebelle, Gardien de la paix, Enfant perdu, Héros, Bouc émissaire — et celui dans lequel vous vous êtes glissé(e) ici.",
  "Cuidador, Mediador, Rebelde, Pacificador, Hijo Perdido, Héroe, Chivo Expiatorio — y en cuál has caído aquí.",
  "Опекун, Посредник, Бунтарь, Миротворец, Потерянный ребёнок, Герой, Козёл отпущения — и в какую из них вы здесь скатились.")
t("Family Dynamic Card", "Carte de Dynamique Familiale", "Tarjeta de Dinámica Familiar", "Карта семейной динамики")
t("The shape of this specific relationship — its temperature, its centre of gravity, the small rituals you share.",
  "La forme de cette relation spécifique — sa température, son centre de gravité, les petits rituels que vous partagez.",
  "La forma de esta relación específica — su temperatura, su centro de gravedad, los pequeños rituales que compartís.",
  "Форма этих конкретных отношений — их температура, центр тяжести, маленькие ритуалы, которые вы делите.")
t("Attachment &amp; Loyalty", "Attachement et loyauté", "Apego y lealtad", "Привязанность и лояльность")
t("Who holds the family together right now, and how. Quietly tracked.",
  "Qui tient la famille ensemble en ce moment, et comment. Suivi en silence.",
  "Quién mantiene unida a la familia ahora mismo, y cómo. Rastreado en silencio.",
  "Кто держит семью вместе прямо сейчас, и как. Тихо отслеживается.")
t("Emotional Ledger", "Registre émotionnel", "Libro de Cuentas Emocional", "Эмоциональная бухгалтерия")
t("Who carries the emotional labour. The unpaid invoice the chat is running.",
  "Qui porte le travail émotionnel. La facture impayée que le chat fait tourner.",
  "Quién carga el trabajo emocional. La factura impagada que el chat está acumulando.",
  "Кто несёт эмоциональный труд. Неоплаченный счёт, который начисляется в чате.")
t("Boundary Landscape", "Paysage des frontières", "Paisaje de límites", "Ландшафт границ")
t("Where the lines are — and where they're permeable. The boundary you're holding without thanks.",
  "Où sont les lignes — et où elles sont perméables. La frontière que vous tenez sans remerciement.",
  "Dónde están las líneas — y dónde son permeables. El límite que estás manteniendo sin agradecimiento.",
  "Где границы — и где они проницаемы. Граница, которую вы держите без благодарности.")
t("Family Patterns", "Patterns familiaux", "Patrones familiares", "Семейные паттерны")
t("The loops the two of you have rehearsed. The argument you keep having three times a year, with different names.",
  "Les boucles que vous deux avez répétées. La dispute que vous continuez d'avoir trois fois par an, sous différents noms.",
  "Los bucles que los dos habéis ensayado. La discusión que seguís teniendo tres veces al año, con diferentes nombres.",
  "Циклы, которые вы вдвоём отрепетировали. Спор, который вы продолжаете вести трижды в год, под разными именами.")
t("Where this relationship is going if no one breaks the pattern — and the smallest move that could change it.",
  "Où va cette relation si personne ne brise le pattern — et le plus petit mouvement qui pourrait le changer.",
  "Hacia dónde va esta relación si nadie rompe el patrón — y el movimiento más pequeño que podría cambiarlo.",
  "Куда движутся эти отношения, если никто не сломает паттерн — и самое маленькое движение, которое могло бы это изменить.")
t("Green Flags &amp; Watch Zones", "Drapeaux verts et zones de vigilance", "Banderas verdes y zonas de vigilancia", "Зелёные флаги и зоны внимания")
t("What's already working in this family. What deserves your attention this season.",
  "Ce qui fonctionne déjà dans cette famille. Ce qui mérite votre attention cette saison.",
  "Lo que ya funciona en esta familia. Lo que merece tu atención esta temporada.",
  "Что уже работает в этой семье. Что заслуживает вашего внимания в этот сезон.")
t("What Family Lens sounds like.",
  "Le ton de la lentille Famille.",
  "Cómo suena la lente Familia.",
  "Как звучит линза Семья.")
t('"You\'ve inherited \'don\'t make me ask twice\' from your mother. She says it. You text it now — to your brother. It lands the same way, and you mean it the same way. This isn\'t a bad thing; it\'s an artefact. The question is whether you want it to be one of the things you keep, or one of the things this generation lets go."',
  "« Vous avez hérité de « ne me fais pas demander deux fois » de votre mère. Elle le dit. Vous le textotez maintenant — à votre frère. Cela atterrit de la même manière, et vous le pensez de la même façon. Ce n'est pas une mauvaise chose ; c'est un artefact. La question est de savoir si vous voulez que ce soit une des choses que vous gardez, ou une des choses que cette génération laisse tomber. »",
  "«Has heredado \"no me hagas preguntarlo dos veces\" de tu madre. Ella lo dice. Tú lo envías ahora por mensaje — a tu hermano. Aterriza de la misma forma, y lo dices con la misma intención. Esto no es algo malo; es un artefacto. La pregunta es si quieres que sea una de las cosas que conservas, o una de las cosas que esta generación deja ir».",
  "«Вы унаследовали «не заставляй меня спрашивать дважды» от своей матери. Она это говорит. Вы теперь пишете это в сообщениях — брату. Это попадает так же, и вы имеете в виду то же самое. Это не плохо; это артефакт. Вопрос в том, хотите ли вы, чтобы это было одной из вещей, которые вы сохраняете, или одной из вещей, которые это поколение отпускает.»")
t("What Family Lens does — and doesn't.",
  "Ce que fait la lentille Famille — et ne fait pas.",
  "Lo que hace la lente Familia — y lo que no.",
  "Что делает линза Семья — и чего не делает.")
t("What Family Lens does", "Ce que fait la lentille Famille", "Lo que hace la lente Familia", "Что делает линза Семья")
t("What Family Lens doesn't", "Ce que la lentille Famille ne fait pas", "Lo que no hace la lente Familia", "Чего не делает линза Семья")
t("Reads a 1:1 family relationship through a <strong>family-systems</strong> lens",
  "Lit une relation familiale 1:1 à travers une lentille <strong>systémique familiale</strong>",
  "Lee una relación familiar 1:1 a través de una lente <strong>sistémica familiar</strong>",
  "Читает семейные отношения 1:1 через призму <strong>семейных систем</strong>")
t("Surfaces inherited language with the line behind it",
  "Fait remonter le langage hérité avec la ligne derrière",
  "Saca a la luz el lenguaje heredado con la línea detrás",
  "Показывает унаследованный язык с конкретной строкой за ним")
t("Names roles without moralising about them",
  "Nomme les rôles sans moraliser",
  "Nombra los roles sin moralizar sobre ellos",
  "Называет роли, не морализируя по их поводу")
t("Tracks the emotional labour the relationship is running on",
  "Suit le travail émotionnel sur lequel tourne la relation",
  "Rastrea el trabajo emocional con el que se mueve la relación",
  "Отслеживает эмоциональный труд, на котором держатся отношения")
t("Offers one move — not a treatment plan",
  "Propose un mouvement — pas un plan de traitement",
  "Ofrece un movimiento — no un plan de tratamiento",
  "Предлагает одно действие — не план лечения")
t("It is <strong>not a substitute for family therapy.</strong> It's a mirror.",
  "Ce <strong>n'est pas un substitut à la thérapie familiale.</strong> C'est un miroir.",
  "<strong>No sustituye a la terapia familiar.</strong> Es un espejo.",
  "Это <strong>не замена семейной терапии.</strong> Это зеркало.")
t("It does not assign blame inside the family",
  "Elle n'attribue pas la faute à l'intérieur de la famille",
  "No asigna culpa dentro de la familia",
  "Не назначает виновного внутри семьи")
t("It does not produce a verdict about your parents",
  "Elle ne produit pas de verdict sur vos parents",
  "No produce un veredicto sobre tus padres",
  "Не выносит вердикт о ваших родителях")
t("It does not work on chats with fewer than ~3 family members",
  "Elle ne fonctionne pas sur les chats avec moins de ~3 membres de la famille",
  "No funciona en chats con menos de ~3 miembros de la familia",
  "Не работает на чатах с менее чем ~3 членами семьи")
t("It cannot help with abuse situations — those deserve a professional, not an app.",
  "Elle ne peut pas aider dans les situations d'abus — celles-ci méritent un professionnel, pas une app.",
  "No puede ayudar en situaciones de abuso — esas merecen un profesional, no una app.",
  "Не может помочь в ситуациях насилия — они заслуживают профессионала, а не приложения.")
t("The differentiator no other app has.",
  "Le différenciateur qu'aucune autre app n'a.",
  "El diferenciador que ninguna otra app tiene.",
  "Дифференциатор, которого нет ни у одного другого приложения.")
t("Family Lens reads what no quiz, no astrology card, no typology can — the real relationship between you and one specific relative.",
  "La lentille Famille lit ce qu'aucun quiz, aucune carte astrologique, aucune typologie ne peut — la vraie relation entre vous et un membre spécifique de la famille.",
  "La lente Familia lee lo que ningún quiz, ninguna carta astrológica, ninguna tipología puede — la relación real entre tú y un familiar específico.",
  "Линза Семья читает то, что не может прочесть ни тест, ни астрологическая карта, ни типология — реальные отношения между вами и одним конкретным родственником.")

# ============================================================
# LENS-GROUP — full body
# ============================================================
t("Group Lens — Persona Lens", "Lentille Groupe — Persona Lens", "Lente Grupo — Persona Lens", "Линза Группа — Persona Lens")
t("The ensemble lens. Treats a group chat as a small society — Cast of Characters, Power Map, Alliance Theory, Awards Ceremony. The highest-virality lens.",
  "La lentille d'ensemble. Traite un groupe de discussion comme une petite société — Distribution des Personnages, Carte du Pouvoir, Théorie des Alliances, Cérémonie des Prix. La lentille à plus forte viralité.",
  "La lente de conjunto. Trata un chat de grupo como una pequeña sociedad — Reparto de Personajes, Mapa de Poder, Teoría de Alianzas, Ceremonia de Premios. La lente de mayor viralidad.",
  "Ансамблевая линза. Воспринимает групповой чат как маленькое общество — Состав Персонажей, Карта Власти, Теория Альянсов, Церемония Наград. Самая вирусная линза.")
t('"Send this to the group chat."',
  "« Envoyez ça au groupe. »",
  "«Envía esto al chat de grupo».",
  "«Отправь это в групповой чат.»")
t("Group Lens analyses <strong>the whole group</strong>. It treats the chat as a small society, names every participant, maps roles and alliances, and presents the result as something between a personality report and an end-of-season awards show. It is the most shareable lens — and the one your group will quote back at each other for weeks.",
  "La lentille Groupe analyse <strong>tout le groupe</strong>. Elle traite le chat comme une petite société, nomme chaque participant, cartographie les rôles et alliances, et présente le résultat comme quelque chose entre un rapport de personnalité et une cérémonie de prix de fin de saison. C'est la lentille la plus partageable — et celle que votre groupe se citera mutuellement pendant des semaines.",
  "La lente Grupo analiza <strong>al grupo entero</strong>. Trata el chat como una pequeña sociedad, nombra a cada participante, mapea roles y alianzas, y presenta el resultado como algo entre un reporte de personalidad y un espectáculo de premios de fin de temporada. Es la lente más compartible — y la que vuestro grupo se citará entre vosotros durante semanas.",
  "Линза Группа анализирует <strong>всю группу</strong>. Она рассматривает чат как маленькое общество, называет каждого участника, картирует роли и альянсы, и подаёт результат как что-то среднее между отчётом о личности и церемонией наград конца сезона. Это самая шарабельная линза — и та, которую ваша группа будет цитировать друг другу неделями.")
t("Try Group Lens free", "Essayer la lentille Groupe gratuitement", "Probar la lente Grupo gratis", "Попробовать линзу Группа бесплатно")
t("Built for the group chat, by the group chat.",
  "Conçue pour le groupe de discussion, par le groupe de discussion.",
  "Construida para el chat de grupo, por el chat de grupo.",
  "Сделано для группового чата, групповым чатом.")
t("The bridesmaid chat", "Le groupe des demoiselles d'honneur", "El chat de damas de honor", "Чат подружек невесты")
t("You need the wedding chat to laugh at itself. Run Group Lens and let the Awards Ceremony do it for you.",
  "Vous avez besoin que le groupe du mariage rie de lui-même. Lancez la lentille Groupe et laissez la Cérémonie des Prix le faire pour vous.",
  "Necesitas que el chat de boda se ría de sí mismo. Ejecuta la lente Grupo y deja que la Ceremonia de Premios lo haga por ti.",
  "Вам нужно, чтобы свадебный чат посмеялся над собой. Запустите линзу Группа и позвольте Церемонии Наград сделать это за вас.")
t("The fantasy-league boys", "La ligue fantasy des gars", "Los chicos de la liga de fantasía", "Парни из фэнтези-лиги")
t("You've all known each other since school. Group Lens has the receipts on who is, in fact, the dad of the group.",
  "Vous vous connaissez tous depuis l'école. La lentille Groupe a les preuves sur qui est, en fait, le papa du groupe.",
  "Os conocéis todos desde el colegio. La lente Grupo tiene los recibos sobre quién es, de hecho, el padre del grupo.",
  "Вы все знаете друг друга со школы. У линзы Группа есть доказательства, кто на самом деле «папа группы».")
t("The book club / running club / dinner club", "Le club de lecture / club de course / club de dîner", "El club de lectura / club de running / club de cena", "Книжный клуб / беговой клуб / обеденный клуб")
t("The chat that's bigger than the activity. Group Lens names the alliances and the glue holding it together.",
  "Le chat qui est plus grand que l'activité. La lentille Groupe nomme les alliances et la colle qui le tient ensemble.",
  "El chat que es más grande que la actividad. La lente Grupo nombra las alianzas y el pegamento que lo mantiene unido.",
  "Чат, который больше самой деятельности. Линза Группа называет альянсы и клей, который её держит.")
t("What's inside a Group reading.",
  "Ce qu'il y a dans une lecture Groupe.",
  "Qué hay dentro de una lectura Grupo.",
  "Что внутри портрета по линзе Группа.")
t("Eleven modules — but the one everyone screenshots is at the bottom. Skip down if you want to.",
  "Onze modules — mais celui que tout le monde capture en screenshot est tout en bas. Sautez en bas si vous voulez.",
  "Once módulos — pero el que todo el mundo captura está abajo. Salta abajo si quieres.",
  "Одиннадцать модулей — но тот, который все скриншотят, внизу. Промотайте вниз, если хотите.")
t("Cast of Characters", "Distribution des Personnages", "Reparto de Personajes", "Состав Персонажей")
t("Every member of the group gets a one-line characterisation and a named archetype.",
  "Chaque membre du groupe obtient une caractérisation en une ligne et un archétype nommé.",
  "Cada miembro del grupo recibe una caracterización en una línea y un arquetipo nombrado.",
  "Каждый член группы получает однострочную характеристику и названный архетип.")
t("Power Map", "Carte du Pouvoir", "Mapa de Poder", "Карта Власти")
t("Who drives the conversation, who steers it, who fades. Visual, named, gentle.",
  "Qui pilote la conversation, qui la dirige, qui s'efface. Visuel, nommé, doux.",
  "Quién conduce la conversación, quién la dirige, quién se desvanece. Visual, nombrado, suave.",
  "Кто ведёт разговор, кто его рулит, кто исчезает. Визуально, поименовано, мягко.")
t("Alliance Theory", "Théorie des Alliances", "Teoría de Alianzas", "Теория Альянсов")
t("The hidden sub-groups inside the bigger one. The two-person side chat that runs the main chat.",
  "Les sous-groupes cachés à l'intérieur du plus grand. Le chat parallèle à deux personnes qui dirige le chat principal.",
  "Los subgrupos ocultos dentro del más grande. El chat paralelo de dos personas que dirige el chat principal.",
  "Скрытые подгруппы внутри большой. Параллельный чат на двоих, который рулит основным чатом.")
t("The Glue", "La Colle", "El Pegamento", "Клей")
t("The one (or two) members who keep the chat alive. The receipt for why the rest of you still show up.",
  "Le(s) membre(s) qui maintiennent le chat en vie. La preuve de pourquoi les autres continuent à venir.",
  "El (o los) miembro(s) que mantienen vivo el chat. El recibo de por qué el resto seguís apareciendo.",
  "Один (или двое) участников, которые держат чат живым. Доказательство, зачем остальные продолжают появляться.")
t("The Ghost", "Le Fantôme", "El Fantasma", "Призрак")
t("The lurker. Named without judgement — sometimes ghosts are the safety net.",
  "Le furtif. Nommé sans jugement — parfois les fantômes sont le filet de sécurité.",
  "El lurker. Nombrado sin juicio — a veces los fantasmas son la red de seguridad.",
  "Тайный наблюдатель. Назван без осуждения — иногда призраки и есть страховочная сеть.")
t("Group Vibe", "Vibe du Groupe", "Onda del Grupo", "Вайб Группы")
t("Banter / philosophical / logistics-heavy / loving / chaotic. With the percentage split.",
  "Taquineries / philosophique / logistique-lourde / aimante / chaotique. Avec la répartition en pourcentage.",
  "Bromas / filosófico / cargado de logística / amoroso / caótico. Con el desglose porcentual.",
  "Подколки / философский / завязанный на логистику / любящий / хаотичный. С разбивкой в процентах.")
t("Inside Jokes Index", "Index des Blagues Internes", "Índice de Chistes Internos", "Индекс внутренних шуток")
t("How many in-jokes are alive, and who keeps them alive.",
  "Combien de blagues internes sont vivantes, et qui les maintient en vie.",
  "Cuántos chistes internos están vivos, y quién los mantiene vivos.",
  "Сколько внутренних шуток ещё живы, и кто их поддерживает.")
t("Patterns &amp; Loops", "Patterns et Boucles", "Patrones y Bucles", "Паттерны и Циклы")
t("The conversations the group has had four times this year. With different names.",
  "Les conversations que le groupe a eues quatre fois cette année. Sous différents noms.",
  "Las conversaciones que el grupo ha tenido cuatro veces este año. Con diferentes nombres.",
  "Разговоры, которые группа имела четырежды за этот год. Под разными именами.")
t("Is this chat growing, steady, or quietly slowing? With one move that would change it.",
  "Ce chat grandit-il, stable, ou ralentit-il silencieusement ? Avec un mouvement qui le changerait.",
  "¿Este chat está creciendo, estable, o frenando en silencio? Con un movimiento que lo cambiaría.",
  "Этот чат растёт, стабилен или тихо замедляется? С одним движением, которое его изменит.")
t("The mum, the planner, the ghost, the chaos agent, the late-night philosopher, the catalyst.",
  "La mère, le planificateur, le fantôme, l'agent du chaos, le philosophe de fin de soirée, le catalyseur.",
  "La madre, el planificador, el fantasma, el agente del caos, el filósofo de medianoche, el catalizador.",
  "Мама, планировщик, призрак, агент хаоса, ночной философ, катализатор.")
t("The Awards Ceremony", "La Cérémonie des Prix", "La Ceremonia de Premios", "Церемония Наград")
t("The signature output. Every member gets a personalised award. Built for screenshot. (Examples below.)",
  "Le résultat signature. Chaque membre reçoit un prix personnalisé. Conçu pour le screenshot. (Exemples ci-dessous.)",
  "El resultado distintivo. Cada miembro recibe un premio personalizado. Hecho para captura. (Ejemplos abajo.)",
  "Фирменный результат. Каждый участник получает персональную награду. Сделано для скриншота. (Примеры ниже.)")
t("Sample", "Exemple", "Muestra", "Пример")
t("Imagine you ran the lens on this chat.",
  "Imaginez que vous lanciez la lentille sur ce chat.",
  "Imagina que ejecutas la lente en este chat.",
  "Представьте, что вы запустили линзу на этом чате.")
t("Here's a small slice of a fictional bridesmaid group chat. Below the chat is what Group Lens would say about the cast — and the awards it would give out.",
  "Voici une petite tranche d'un groupe fictif de demoiselles d'honneur. Sous le chat se trouve ce que la lentille Groupe dirait de la distribution — et les prix qu'elle remettrait.",
  "Aquí hay una pequeña porción de un chat ficticio de damas de honor. Debajo del chat está lo que la lente Grupo diría sobre el reparto — y los premios que daría.",
  "Вот маленький срез вымышленного чата подружек невесты. Под чатом — то, что линза Группа сказала бы о составе и какие награды раздала бы.")
t("What Group Lens returns · Part 1", "Ce que retourne la lentille Groupe · Partie 1", "Lo que devuelve la lente Grupo · Parte 1", "Что возвращает линза Группа · Часть 1")
t("Cast of Characters.", "Distribution des Personnages.", "Reparto de Personajes.", "Состав Персонажей.")
t("Group Lens names each member of the chat. Not by their handle — by their role.",
  "La lentille Groupe nomme chaque membre du chat. Pas par leur pseudo — par leur rôle.",
  "La lente Grupo nombra a cada miembro del chat. No por su nombre de usuario — por su rol.",
  "Линза Группа называет каждого участника чата. Не по нику — по роли.")
t("What Group Lens returns · Part 2", "Ce que retourne la lentille Groupe · Partie 2", "Lo que devuelve la lente Grupo · Parte 2", "Что возвращает линза Группа · Часть 2")
t("The Awards Ceremony.", "La Cérémonie des Prix.", "La Ceremonia de Premios.", "Церемония Наград.")
t("The signature output. Every member of the group gets a personalised award — funny, specific, occasionally heartfelt, always quotable. This is the section your group will screenshot.",
  "Le résultat signature. Chaque membre du groupe reçoit un prix personnalisé — drôle, spécifique, parfois touchant, toujours citable. C'est la section que votre groupe capturera en screenshot.",
  "El resultado distintivo. Cada miembro del grupo recibe un premio personalizado — divertido, específico, ocasionalmente conmovedor, siempre citable. Esta es la sección que vuestro grupo capturará.",
  "Фирменный результат. Каждый член группы получает персональную награду — смешную, конкретную, иногда трогательную, всегда цитируемую. Это та секция, которую ваша группа будет скриншотить.")
t("Group Lens generates a unique award for every member of the chat — these are six of eight, from one sample reading.",
  "La lentille Groupe génère un prix unique pour chaque membre du chat — voici six sur huit, d'une lecture exemple.",
  "La lente Grupo genera un premio único para cada miembro del chat — estos son seis de ocho, de una lectura de muestra.",
  "Линза Группа генерирует уникальную награду для каждого участника чата — это шесть из восьми, из одного примера портрета.")
t("What Group Lens does — and doesn't.",
  "Ce que fait la lentille Groupe — et ne fait pas.",
  "Lo que hace la lente Grupo — y lo que no.",
  "Что делает линза Группа — и чего не делает.")
t("What Group Lens does", "Ce que fait la lentille Groupe", "Lo que hace la lente Grupo", "Что делает линза Группа")
t("What Group Lens doesn't", "Ce que la lentille Groupe ne fait pas", "Lo que no hace la lente Grupo", "Чего не делает линза Группа")
t("Names <strong>every</strong> participant in the chat with their own archetype",
  "Nomme <strong>chaque</strong> participant du chat avec son propre archétype",
  "Nombra a <strong>cada</strong> participante del chat con su propio arquetipo",
  "Называет <strong>каждого</strong> участника чата своим архетипом")
t("Maps power, alliances, and group vibe",
  "Cartographie le pouvoir, les alliances et la vibe du groupe",
  "Mapea poder, alianzas y la onda del grupo",
  "Картирует власть, альянсы и вайб группы")
t("Produces a personalised Award for each member",
  "Produit un Prix personnalisé pour chaque membre",
  "Produce un Premio personalizado para cada miembro",
  "Создаёт персональную Награду для каждого участника")
t("Builds shareable cards explicitly designed for the group's own chat",
  "Construit des cartes partageables explicitement conçues pour le chat du groupe lui-même",
  "Construye tarjetas compartibles diseñadas explícitamente para el propio chat del grupo",
  "Делает шарабельные карточки, явно созданные для собственного чата группы")
t("Works on chats of 3 to ~25 members",
  "Fonctionne sur les chats de 3 à ~25 membres",
  "Funciona en chats de 3 a ~25 miembros",
  "Работает на чатах от 3 до ~25 участников")
t('It does not pick a "best member" — there are no rankings',
  "Elle ne choisit pas de « meilleur membre » — il n'y a pas de classements",
  "No elige al «mejor miembro» — no hay rankings",
  "Не выбирает «лучшего участника» — никаких рейтингов")
t("It does not produce content meant to hurt anyone",
  "Elle ne produit pas de contenu destiné à blesser qui que ce soit",
  "No produce contenido destinado a herir a nadie",
  "Не создаёт контент, призванный кого-то ранить")
t("It does not name the people by their phone numbers — only by the names already in the chat",
  "Elle ne nomme pas les gens par leurs numéros de téléphone — seulement par les noms déjà dans le chat",
  "No nombra a la gente por sus números de teléfono — solo por los nombres que ya están en el chat",
  "Не называет людей по их номерам телефонов — только по именам, уже имеющимся в чате")
t("It does not work well on chats under ~50 messages",
  "Elle ne fonctionne pas bien sur les chats de moins de ~50 messages",
  "No funciona bien en chats con menos de ~50 mensajes",
  "Плохо работает на чатах менее ~50 сообщений")
t("It is the lens that takes the longest to generate — give it ~90 seconds",
  "C'est la lentille qui prend le plus de temps à générer — laissez-lui ~90 secondes",
  "Es la lente que tarda más en generarse — dale ~90 segundos",
  "Это самая долго генерируемая линза — дайте ей ~90 секунд")
t("The lens engineered for screenshots.",
  "La lentille conçue pour les screenshots.",
  "La lente diseñada para capturas.",
  "Линза, спроектированная под скриншоты.")
t("Run Group Lens once on your chat. Then watch how fast it ends up pinned in the group.",
  "Lancez la lentille Groupe une fois sur votre chat. Puis regardez à quelle vitesse elle finit épinglée dans le groupe.",
  "Ejecuta la lente Grupo una vez en tu chat. Luego mira cuán rápido acaba fijada en el grupo.",
  "Запустите линзу Группа один раз на своём чате. Потом смотрите, как быстро она окажется закреплённой в группе.")

print("After all-lens additions:", len(T), "entries")


# ============================================================
# PRIVACY page
# ============================================================
t("Privacy Policy — Persona Lens", "Politique de confidentialité — Persona Lens", "Política de privacidad — Persona Lens", "Политика приватности — Persona Lens")
t("How Persona Lens handles your conversations, what data we touch, and what we never do with it.",
  "Comment Persona Lens traite vos conversations, quelles données nous touchons, et ce que nous n'en faisons jamais.",
  "Cómo Persona Lens maneja tus conversaciones, qué datos tocamos, y qué nunca hacemos con ellos.",
  "Как Persona Lens обращается с вашими переписками, какие данные мы трогаем, и чего никогда не делаем с ними.")
t("Privacy Policy", "Politique de confidentialité", "Política de privacidad", "Политика приватности")
t("Last updated: 15 May 2026", "Dernière mise à jour : 15 mai 2026", "Última actualización: 15 de mayo de 2026", "Последнее обновление: 15 мая 2026")
t("Persona Lens analyses the most personal thing you have — your real conversations. We built it the way we'd want any product that touches our own messages to be built: minimum data collection, no resale, no training on your chats, and nothing stored on our servers beyond what's strictly needed to deliver your reading.",
  "Persona Lens analyse ce que vous avez de plus personnel — vos vraies conversations. Nous l'avons construit comme nous voudrions que tout produit touchant à nos propres messages soit construit : collecte minimale de données, aucune revente, aucun entraînement sur vos chats, et rien stocké sur nos serveurs au-delà de ce qui est strictement nécessaire pour livrer votre lecture.",
  "Persona Lens analiza lo más personal que tienes — tus conversaciones reales. Lo construimos de la manera en que querríamos que se construyera cualquier producto que toca nuestros propios mensajes: mínima recopilación de datos, sin reventa, sin entrenamiento con tus chats, y nada almacenado en nuestros servidores más allá de lo estrictamente necesario para entregar tu lectura.",
  "Persona Lens анализирует самое личное, что у вас есть — ваши реальные переписки. Мы построили его так, как хотели бы, чтобы строился любой продукт, касающийся наших собственных сообщений: минимальный сбор данных, никакой перепродажи, никакого обучения на ваших чатах, и ничего не хранится на наших серверах сверх того, что строго необходимо для доставки вашего портрета.")
t("What we collect", "Ce que nous collectons", "Lo que recopilamos", "Что мы собираем")
t("<strong>The chat you submit.</strong> The text you paste or import is processed to generate one reading and is not retained after the reading is delivered.",
  "<strong>Le chat que vous soumettez.</strong> Le texte que vous collez ou importez est traité pour générer une lecture et n'est pas conservé après la livraison de la lecture.",
  "<strong>El chat que envías.</strong> El texto que pegas o importas se procesa para generar una lectura y no se retiene después de entregar la lectura.",
  "<strong>Чат, который вы отправляете.</strong> Текст, который вы вставляете или импортируете, обрабатывается для генерации одного портрета и не сохраняется после доставки портрета.")
t("<strong>Anonymous usage events.</strong> App opens, lens selections, and crash reports — no chat content, no names, no identifiers tied to you.",
  "<strong>Événements d'utilisation anonymes.</strong> Ouvertures de l'app, sélections de lentilles, et rapports de crash — pas de contenu de chat, pas de noms, pas d'identifiants liés à vous.",
  "<strong>Eventos de uso anónimos.</strong> Aperturas de la app, selecciones de lente, e informes de fallos — sin contenido de chat, sin nombres, sin identificadores ligados a ti.",
  "<strong>Анонимные события использования.</strong> Открытия приложения, выбор линз, отчёты о сбоях — никакого содержимого чатов, никаких имён, никаких идентификаторов, привязанных к вам.")
t("<strong>Purchase receipts.</strong> If you upgrade to Pro or buy credits, Apple processes the payment. We receive a receipt from Apple confirming entitlement — we never see your card details.",
  "<strong>Reçus d'achat.</strong> Si vous passez en Pro ou achetez des crédits, Apple traite le paiement. Nous recevons un reçu d'Apple confirmant le droit — nous ne voyons jamais les détails de votre carte.",
  "<strong>Recibos de compra.</strong> Si actualizas a Pro o compras créditos, Apple procesa el pago. Recibimos un recibo de Apple que confirma la entitlement — nunca vemos los detalles de tu tarjeta.",
  "<strong>Чеки покупок.</strong> Если вы переходите на Pro или покупаете кредиты, Apple обрабатывает платёж. Мы получаем чек от Apple, подтверждающий право — мы никогда не видим данных вашей карты.")
t("What we never collect", "Ce que nous ne collectons jamais", "Lo que nunca recopilamos", "Что мы никогда не собираем")
t("Your Instagram DMs, contacts, photos, calendar, or location.",
  "Vos DMs Instagram, contacts, photos, agenda, ou localisation.",
  "Tus DM de Instagram, contactos, fotos, calendario o ubicación.",
  "Ваши DM в Instagram, контакты, фотографии, календарь или местоположение.")
t("Your real name, phone number, or email — unless you contact us directly.",
  "Votre vrai nom, numéro de téléphone, ou email — sauf si vous nous contactez directement.",
  "Tu nombre real, número de teléfono o email — a no ser que nos contactes directamente.",
  "Ваше настоящее имя, номер телефона или email — если только вы не свяжетесь с нами напрямую.")
t("Any chat content beyond the one you actively submit.",
  "Tout contenu de chat au-delà de celui que vous soumettez activement.",
  "Cualquier contenido de chat más allá del que envías activamente.",
  "Любое содержимое чатов сверх того, что вы активно отправляете.")
t("How your chat is processed", "Comment votre chat est traité", "Cómo se procesa tu chat", "Как обрабатывается ваш чат")
t("When you submit a conversation, it is sent over an encrypted connection to our stateless analysis backend, processed to generate your reading, and then discarded. The chat is not retained, not logged, and not used to train any model. The only thing kept is the reading you receive — and that reading lives in encrypted local storage on your iPhone, not on our servers.",
  "Lorsque vous soumettez une conversation, elle est envoyée via une connexion chiffrée à notre backend d'analyse sans état, traitée pour générer votre lecture, puis supprimée. Le chat n'est ni conservé, ni journalisé, ni utilisé pour entraîner un quelconque modèle. La seule chose conservée est la lecture que vous recevez — et cette lecture vit dans un stockage local chiffré sur votre iPhone, pas sur nos serveurs.",
  "Cuando envías una conversación, se envía a través de una conexión cifrada a nuestro backend de análisis sin estado, se procesa para generar tu lectura, y luego se descarta. El chat no se retiene, no se registra, y no se usa para entrenar ningún modelo. Lo único que se conserva es la lectura que recibes — y esa lectura vive en almacenamiento local cifrado en tu iPhone, no en nuestros servidores.",
  "Когда вы отправляете переписку, она передаётся по зашифрованному соединению в наш безсостоянный аналитический бэкенд, обрабатывается для генерации вашего портрета, а затем удаляется. Чат не сохраняется, не логируется и не используется для обучения какой-либо модели. Единственное, что сохраняется — это портрет, который вы получаете, и этот портрет живёт в зашифрованном локальном хранилище на вашем iPhone, не на наших серверах.")
t("Sharing", "Partage", "Compartir", "Передача данных")
t("We do not sell, rent, or share your data with advertisers, brokers, or third parties. The only sub-processors we use are Apple (for app distribution and in-app purchases), and our hosting provider for serving this website. None of them see your chat content.",
  "Nous ne vendons, ne louons, ni ne partageons vos données avec des annonceurs, des courtiers ou des tiers. Les seuls sous-traitants que nous utilisons sont Apple (pour la distribution de l'app et les achats in-app), et notre fournisseur d'hébergement pour servir ce site web. Aucun d'eux ne voit le contenu de votre chat.",
  "No vendemos, alquilamos ni compartimos tus datos con anunciantes, intermediarios o terceros. Los únicos subprocesadores que usamos son Apple (para la distribución de la app y las compras in-app), y nuestro proveedor de hosting para servir este sitio web. Ninguno de ellos ve el contenido de tu chat.",
  "Мы не продаём, не сдаём в аренду и не передаём ваши данные рекламодателям, брокерам или третьим лицам. Единственные субпроцессоры, которых мы используем — это Apple (для распространения приложения и встроенных покупок) и наш хостинг-провайдер для обслуживания этого сайта. Никто из них не видит содержимое ваших чатов.")
t("Your rights", "Vos droits", "Tus derechos", "Ваши права")
t("Persona Lens does not maintain an account for you. There's nothing to log into and nothing tied to your identity. Deleting the app removes everything generated on your device. We do not maintain any direct-contact channel for this app, so there is no correspondence on our side to delete.",
  "Persona Lens ne maintient pas de compte pour vous. Il n'y a rien à connecter et rien lié à votre identité. Supprimer l'app retire tout ce qui a été généré sur votre appareil. Nous ne maintenons aucun canal de contact direct pour cette app, donc il n'y a aucune correspondance de notre côté à supprimer.",
  "Persona Lens no mantiene una cuenta para ti. No hay nada en lo que iniciar sesión y nada ligado a tu identidad. Borrar la app elimina todo lo generado en tu dispositivo. No mantenemos ningún canal de contacto directo para esta app, así que no hay correspondencia en nuestro lado para borrar.",
  "Persona Lens не ведёт учётную запись для вас. Никуда не нужно входить и ничто не привязано к вашей личности. Удаление приложения убирает всё, сгенерированное на вашем устройстве. У нас нет канала прямой связи для этого приложения, так что нет переписки с нашей стороны, которую нужно было бы удалять.")
t("Children", "Mineurs", "Menores", "Дети")
t("Persona Lens is not designed for users under 16. We do not knowingly collect data from anyone under 16. If you believe a minor has used the app, contact us and we will assist.",
  "Persona Lens n'est pas conçu pour les utilisateurs de moins de 16 ans. Nous ne collectons pas sciemment de données de personnes de moins de 16 ans. Si vous pensez qu'un mineur a utilisé l'app, contactez-nous et nous vous aiderons.",
  "Persona Lens no está diseñado para usuarios menores de 16 años. No recopilamos a sabiendas datos de menores de 16. Si crees que un menor ha usado la app, contáctanos y te ayudaremos.",
  "Persona Lens не предназначен для пользователей младше 16 лет. Мы сознательно не собираем данные у лиц младше 16. Если вы считаете, что приложением пользовался несовершеннолетний, свяжитесь с нами, и мы поможем.")
t("Changes to this policy", "Modifications de cette politique", "Cambios en esta política", "Изменения этой политики")
t("If we change anything material about how Persona Lens handles your data, we will update this page and note the change in-app before the change takes effect.",
  "Si nous changeons quelque chose de matériel dans la façon dont Persona Lens traite vos données, nous mettrons à jour cette page et noterons le changement dans l'app avant que le changement ne prenne effet.",
  "Si cambiamos algo material sobre cómo Persona Lens maneja tus datos, actualizaremos esta página y anotaremos el cambio en la app antes de que el cambio entre en vigor.",
  "Если мы изменим что-то существенное в том, как Persona Lens обращается с вашими данными, мы обновим эту страницу и отметим изменение внутри приложения до того, как оно вступит в силу.")

# ============================================================
# TERMS page
# ============================================================
t("Terms of Use — Persona Lens", "Conditions d'utilisation — Persona Lens", "Condiciones de uso — Persona Lens", "Условия использования — Persona Lens")
t("The terms under which Persona Lens is offered.",
  "Les conditions dans lesquelles Persona Lens est proposé.",
  "Las condiciones bajo las que se ofrece Persona Lens.",
  "Условия, на которых предлагается Persona Lens.")
t("Terms of Use", "Conditions d'utilisation", "Condiciones de uso", "Условия использования")
t("By downloading or using Persona Lens, you agree to these terms. They are intentionally short and plain.",
  "En téléchargeant ou en utilisant Persona Lens, vous acceptez ces conditions. Elles sont volontairement courtes et claires.",
  "Al descargar o usar Persona Lens, aceptas estos términos. Son intencionalmente cortos y claros.",
  "Скачивая или используя Persona Lens, вы соглашаетесь с этими условиями. Они намеренно короткие и простые.")
t("What Persona Lens is", "Ce qu'est Persona Lens", "Qué es Persona Lens", "Что такое Persona Lens")
t("Persona Lens is a personality-analysis app for iOS. You submit a conversation, you choose a lens, and you receive a reading — a Persona Card, the lens's modules, an Awards Ceremony where applicable, and a portrait written in the voice of the lens you chose. The analysis is generated by software and is intended for self-reflection and entertainment, not as professional diagnosis of any kind.",
  "Persona Lens est une application d'analyse de personnalité pour iOS. Vous soumettez une conversation, vous choisissez une lentille, et vous recevez une lecture — une Carte Persona, les modules de la lentille, une Cérémonie des Prix le cas échéant, et un portrait écrit dans la voix de la lentille choisie. L'analyse est générée par logiciel et est destinée à la réflexion personnelle et au divertissement, pas à un diagnostic professionnel de quelque sorte que ce soit.",
  "Persona Lens es una app de análisis de personalidad para iOS. Envías una conversación, eliges una lente, y recibes una lectura — una Tarjeta Persona, los módulos de la lente, una Ceremonia de Premios cuando aplica, y un retrato escrito en la voz de la lente elegida. El análisis es generado por software y está pensado para la auto-reflexión y el entretenimiento, no como diagnóstico profesional de ningún tipo.",
  "Persona Lens — это приложение для анализа личности для iOS. Вы отправляете переписку, выбираете линзу и получаете портрет — Карту Персоны, модули линзы, Церемонию Наград где применимо, и письменный портрет голосом выбранной линзы. Анализ создаётся программно и предназначен для саморефлексии и развлечения, а не как профессиональный диагноз любого рода.")
t("What Persona Lens is not", "Ce que Persona Lens n'est pas", "Qué no es Persona Lens", "Чем Persona Lens не является")
t("Persona Lens is not a medical, psychological, psychiatric, legal, or financial service. The readings it produces are not clinical assessments, are not predictive of behaviour, and should not be used to make decisions about another person's relationships, employment, or wellbeing without their consent and a qualified professional.",
  "Persona Lens n'est pas un service médical, psychologique, psychiatrique, juridique ou financier. Les lectures qu'il produit ne sont pas des évaluations cliniques, ne prédisent pas le comportement, et ne doivent pas être utilisées pour prendre des décisions sur les relations, l'emploi ou le bien-être d'une autre personne sans son consentement et un professionnel qualifié.",
  "Persona Lens no es un servicio médico, psicológico, psiquiátrico, legal ni financiero. Las lecturas que produce no son evaluaciones clínicas, no predicen el comportamiento, y no deben usarse para tomar decisiones sobre las relaciones, el empleo o el bienestar de otra persona sin su consentimiento y un profesional cualificado.",
  "Persona Lens не является медицинской, психологической, психиатрической, юридической или финансовой услугой. Создаваемые им портреты не являются клиническими оценками, не предсказывают поведение, и не должны использоваться для принятия решений об отношениях, занятости или благополучии другого человека без его согласия и квалифицированного специалиста.")
t("Your responsibilities", "Vos responsabilités", "Tus responsabilidades", "Ваши обязанности")
t("Only submit conversations you have the right to share. Do not submit other people's chats without their consent.",
  "Ne soumettez que des conversations que vous avez le droit de partager. Ne soumettez pas les chats d'autres personnes sans leur consentement.",
  "Solo envía conversaciones que tengas derecho a compartir. No envíes chats de otras personas sin su consentimiento.",
  "Отправляйте только те переписки, которые вы имеете право делиться. Не отправляйте чужие чаты без их согласия.")
t("You are responsible for how you use the readings the app generates. Do not weaponise them — that is not the point of the product.",
  "Vous êtes responsable de la façon dont vous utilisez les lectures que l'app génère. Ne les armez pas — ce n'est pas le but du produit.",
  "Eres responsable de cómo usas las lecturas que genera la app. No las uses como arma — ese no es el propósito del producto.",
  "Вы отвечаете за то, как используете создаваемые приложением портреты. Не превращайте их в оружие — это не цель продукта.")
t("You must be at least 16 years old to use Persona Lens.",
  "Vous devez avoir au moins 16 ans pour utiliser Persona Lens.",
  "Debes tener al menos 16 años para usar Persona Lens.",
  "Вам должно быть не менее 16 лет, чтобы пользоваться Persona Lens.")
t("Pricing and subscriptions", "Tarifs et abonnements", "Precios y suscripciones", "Цены и подписки")
t("Your first reading is free. After that, you can buy individual credits or subscribe to Persona Lens Pro. All purchases are handled by Apple through the App Store and are subject to Apple's standard refund and cancellation rules. You can cancel a subscription anytime from your iPhone Settings.",
  "Votre première lecture est gratuite. Ensuite, vous pouvez acheter des crédits individuels ou vous abonner à Persona Lens Pro. Tous les achats sont gérés par Apple via l'App Store et sont soumis aux règles standard de remboursement et d'annulation d'Apple. Vous pouvez annuler un abonnement à tout moment depuis les Réglages de votre iPhone.",
  "Tu primera lectura es gratis. Después, puedes comprar créditos individuales o suscribirte a Persona Lens Pro. Todas las compras las gestiona Apple a través del App Store y están sujetas a las reglas estándar de reembolso y cancelación de Apple. Puedes cancelar una suscripción en cualquier momento desde los Ajustes de tu iPhone.",
  "Ваш первый портрет бесплатен. После этого вы можете покупать отдельные кредиты или подписаться на Persona Lens Pro. Все покупки обрабатываются Apple через App Store и подчиняются стандартным правилам возврата и отмены Apple. Вы можете отменить подписку в любое время в Настройках iPhone.")
t("Intellectual property", "Propriété intellectuelle", "Propiedad intelectual", "Интеллектуальная собственность")
t("The readings generated for you are yours — share them, screenshot them, post them, frame them. The app itself, its branding, its lens system, the visual design of the Persona Card, and the underlying analysis methodology remain the intellectual property of Persona Lens.",
  "Les lectures générées pour vous sont à vous — partagez-les, capturez-les, postez-les, encadrez-les. L'app elle-même, son branding, son système de lentilles, le design visuel de la Carte Persona, et la méthodologie d'analyse sous-jacente restent la propriété intellectuelle de Persona Lens.",
  "Las lecturas generadas para ti son tuyas — compártelas, captúralas, publícalas, enmárcalas. La app en sí, su branding, su sistema de lentes, el diseño visual de la Tarjeta Persona, y la metodología de análisis subyacente siguen siendo propiedad intelectual de Persona Lens.",
  "Создаваемые для вас портреты — ваши: делитесь ими, скриншотьте, публикуйте, обрамляйте. Само приложение, его брендинг, его система линз, визуальный дизайн Карты Персоны и лежащая в основе методология анализа остаются интеллектуальной собственностью Persona Lens.")
t("No warranty", "Aucune garantie", "Sin garantía", "Без гарантии")
t("Persona Lens is provided as-is. Readings are software-generated interpretations and may be wrong, partial, or unflattering. They are not the truth about you — they are one possible mirror. Treat them accordingly.",
  "Persona Lens est fourni tel quel. Les lectures sont des interprétations générées par logiciel et peuvent être erronées, partielles ou peu flatteuses. Elles ne sont pas la vérité sur vous — elles sont un miroir possible. Traitez-les en conséquence.",
  "Persona Lens se proporciona tal cual. Las lecturas son interpretaciones generadas por software y pueden ser erróneas, parciales o poco halagadoras. No son la verdad sobre ti — son un espejo posible. Trátalas en consecuencia.",
  "Persona Lens предоставляется как есть. Портреты — это программно сгенерированные интерпретации, и они могут быть ошибочными, частичными или нелестными. Они не являются истиной о вас — они одно из возможных зеркал. Относитесь к ним соответственно.")
t("Limitation of liability", "Limitation de responsabilité", "Limitación de responsabilidad", "Ограничение ответственности")
t("To the maximum extent permitted by law, Persona Lens is not liable for any indirect, incidental, or consequential damages arising from your use of the app. Our maximum liability to you is limited to what you've paid us in the past 12 months.",
  "Dans toute la mesure permise par la loi, Persona Lens n'est pas responsable de dommages indirects, accessoires ou consécutifs découlant de votre utilisation de l'app. Notre responsabilité maximale envers vous est limitée à ce que vous nous avez payé au cours des 12 derniers mois.",
  "Hasta el máximo permitido por la ley, Persona Lens no es responsable de daños indirectos, incidentales o consecuenciales que surjan de tu uso de la app. Nuestra responsabilidad máxima hacia ti se limita a lo que nos has pagado en los últimos 12 meses.",
  "В максимально допустимой законом степени Persona Lens не несёт ответственности за любые косвенные, случайные или вытекающие убытки, возникающие из вашего использования приложения. Наша максимальная ответственность перед вами ограничена тем, что вы заплатили нам за последние 12 месяцев.")
t("Changes", "Modifications", "Cambios", "Изменения")
t("We may update these terms. Material changes will be flagged in-app before they take effect.",
  "Nous pouvons mettre à jour ces conditions. Les changements matériels seront signalés dans l'app avant qu'ils ne prennent effet.",
  "Podemos actualizar estos términos. Los cambios materiales se señalarán en la app antes de que entren en vigor.",
  "Мы можем обновлять эти условия. Существенные изменения будут отмечены в приложении до того, как они вступят в силу.")

print("After privacy+terms additions:", len(T), "entries")


# ============================================================
# PRICING page (full)
# ============================================================
t("Pricing — Persona Lens", "Tarifs — Persona Lens", "Precios — Persona Lens", "Цены — Persona Lens")
t("One free analysis on first launch. After that: 3 credit packs (1, 5 or 10 analyses) or 2 subscription tiers (monthly or yearly). Credits never expire.",
  "Une analyse gratuite au premier lancement. Ensuite : 3 packs de crédits (1, 5 ou 10 analyses) ou 2 niveaux d'abonnement (mensuel ou annuel). Les crédits n'expirent jamais.",
  "Un análisis gratis en el primer arranque. Después: 3 packs de créditos (1, 5 o 10 análisis) o 2 niveles de suscripción (mensual o anual). Los créditos no caducan nunca.",
  "Один бесплатный анализ при первом запуске. Дальше: 3 пакета кредитов (1, 5 или 10 анализов) или 2 уровня подписки (помесячно или ежегодно). Кредиты никогда не сгорают.")
t("One free analysis on first launch. Then choose your way in.",
  "Une analyse gratuite au premier lancement. Puis choisissez votre voie d'entrée.",
  "Un análisis gratis en el primer arranque. Después elige tu camino.",
  "Один бесплатный анализ при первом запуске. Затем выбирайте свой путь.")
t("Persona Lens gives every new user one free analysis the first time they open the app. After that, you choose between three credit packs (pay-as-you-go) or two subscription tiers (unlimited). No ads inside the reading. No upsells in the middle of a module.",
  "Persona Lens offre à chaque nouvel utilisateur une analyse gratuite la première fois qu'il ouvre l'app. Ensuite, vous choisissez entre trois packs de crédits (paiement à l'usage) ou deux niveaux d'abonnement (illimité). Aucune pub dans la lecture. Aucune montée en gamme au milieu d'un module.",
  "Persona Lens da a cada nuevo usuario un análisis gratis la primera vez que abre la app. Después, eliges entre tres packs de créditos (pago por uso) o dos niveles de suscripción (ilimitado). Sin anuncios dentro de la lectura. Sin upsells a mitad de un módulo.",
  "Persona Lens даёт каждому новому пользователю один бесплатный анализ при первом открытии приложения. Дальше вы выбираете между тремя пакетами кредитов (плати за то, что используешь) или двумя уровнями подписки (безлимит). Никакой рекламы внутри портрета. Никаких допродаж посреди модуля.")
t("Two paths", "Deux voies", "Dos caminos", "Два пути")
t("Pay-per-use or unlimited.", "À l'usage ou illimité.", "Pago por uso o ilimitado.", "По требованию или безлимит.")
t("Pay-per-use", "Paiement à l'usage", "Pago por uso", "Плати за использование")
t("From $2.99<span>/analysis</span>", "Dès 2,99 $<span>/analyse</span>", "Desde 2,99 $<span>/análisis</span>", "От $2.99<span>/анализ</span>")
t("3 credit packs · credits never expire · no commitment.",
  "3 packs de crédits · les crédits n'expirent jamais · sans engagement.",
  "3 packs de créditos · los créditos no caducan nunca · sin compromiso.",
  "3 пакета кредитов · кредиты не сгорают · без обязательств.")
t("Pay only when you need an analysis",
  "Payez seulement quand vous avez besoin d'une analyse",
  "Paga solo cuando necesites un análisis",
  "Платите только когда нужен анализ")
t("No subscription, no renewal",
  "Pas d'abonnement, pas de renouvellement",
  "Sin suscripción, sin renovación",
  "Без подписки, без продления")
t("Credits never expire", "Les crédits n'expirent jamais", "Los créditos no caducan nunca", "Кредиты не сгорают")
t("Bigger packs lower the per-analysis price",
  "Les plus grands packs réduisent le prix par analyse",
  "Los packs más grandes bajan el precio por análisis",
  "Большие пакеты снижают цену за анализ")
t("Great for trying Persona Lens first",
  "Idéal pour essayer Persona Lens d'abord",
  "Ideal para probar Persona Lens primero",
  "Отлично подходит, чтобы сначала попробовать Persona Lens")
t("Buy credits on the App Store →",
  "Acheter des crédits sur l'App Store →",
  "Comprar créditos en el App Store →",
  "Купить кредиты в App Store →")
t("Best for situational readers — one ex, one boss, one group chat.",
  "Idéal pour les lecteurs situationnels — un ex, un boss, un groupe de discussion.",
  "Ideal para lectores situacionales — un ex, un jefe, un chat de grupo.",
  "Идеально для ситуативных читателей — один бывший, один босс, одна групповая переписка.")
t("From $8.33<span>/month</span>", "Dès 8,33 $<span>/mois</span>", "Desde 8,33 $<span>/mes</span>", "От $8.33<span>/мес</span>")
t("Unlimited analyses across all six lenses.",
  "Analyses illimitées sur les six lentilles.",
  "Análisis ilimitados en las seis lentes.",
  "Безлимитные анализы по всем шести линзам.")
t("Unlimited personality analyses",
  "Analyses de personnalité illimitées",
  "Análisis de personalidad ilimitados",
  "Безлимитные анализы личности")
t("Insight Library — filter, sort &amp; explore all your reports",
  "Bibliothèque d'Insights — filtrer, trier et explorer tous vos rapports",
  "Biblioteca de Insights — filtrar, ordenar y explorar todos tus reportes",
  "Библиотека Инсайтов — фильтровать, сортировать и исследовать все ваши отчёты")
t("Early access to new analysis lenses",
  "Accès anticipé aux nouvelles lentilles d'analyse",
  "Acceso anticipado a nuevas lentes de análisis",
  "Ранний доступ к новым линзам анализа")
t("Subscribe on the App Store →",
  "S'abonner sur l'App Store →",
  "Suscribirse en el App Store →",
  "Подписаться в App Store →")
t("Cancel anytime in iPhone Settings. No invoices, no calls.",
  "Annulez à tout moment dans les Réglages de l'iPhone. Pas de factures, pas d'appels.",
  "Cancela cuando quieras desde los Ajustes de iPhone. Sin facturas, sin llamadas.",
  "Отмените в любой момент в Настройках iPhone. Без счетов, без звонков.")
t("Pay-per-use, in detail.", "Paiement à l'usage, en détail.", "Pago por uso, en detalle.", "Плата за использование, в деталях.")
t("Three packs. The bigger the pack, the cheaper the per-analysis price. None of the credits ever expire.",
  "Trois packs. Plus le pack est grand, moins le prix par analyse est cher. Aucun crédit n'expire jamais.",
  "Tres packs. Cuanto más grande el pack, más barato el precio por análisis. Ninguno de los créditos caduca.",
  "Три пакета. Чем больше пакет, тем дешевле цена за анализ. Ни один кредит никогда не сгорает.")
t("Pack", "Pack", "Pack", "Пакет")
t("Price", "Prix", "Precio", "Цена")
t("Per analysis", "Par analyse", "Por análisis", "За анализ")
t("Best for", "Idéal pour", "Ideal para", "Идеально для")
t("1 analysis", "1 analyse", "1 análisis", "1 анализ")
t('"I just want one reading."',
  "« Je veux juste une lecture. »",
  "«Solo quiero una lectura».",
  "«Я просто хочу один портрет.»")
t("Buy →", "Acheter →", "Comprar →", "Купить →")
t("5 analyses", "5 analyses", "5 análisis", "5 анализов")
t("save 13%", "économisez 13 %", "ahorra 13 %", "экономия 13%")
t("One lens for five different chats.",
  "Une lentille pour cinq chats différents.",
  "Una lente para cinco chats diferentes.",
  "Одна линза для пяти разных чатов.")
t("10 analyses", "10 analyses", "10 análisis", "10 анализов")
t("best deal · save 23%", "meilleure offre · économisez 23 %", "mejor oferta · ahorra 23 %", "лучшая сделка · экономия 23%")
t("Most popular. A season of readings.",
  "Le plus populaire. Une saison de lectures.",
  "El más popular. Una temporada de lecturas.",
  "Самое популярное. Целый сезон портретов.")
t("Prices shown in USD. The App Store displays the equivalent amount in your local currency at checkout. Credits never expire — they survive cancellation, restore, and switching plans.",
  "Prix affichés en USD. L'App Store affiche le montant équivalent dans votre devise locale au moment du paiement. Les crédits n'expirent jamais — ils survivent à l'annulation, à la restauration, et au changement de plan.",
  "Precios mostrados en USD. El App Store muestra el importe equivalente en tu moneda local en el momento del pago. Los créditos no caducan nunca — sobreviven a la cancelación, la restauración y el cambio de plan.",
  "Цены показаны в USD. App Store отображает эквивалент в вашей локальной валюте на этапе оплаты. Кредиты никогда не сгорают — они переживают отмену, восстановление и смену плана.")
t("Two ways to subscribe.", "Deux façons de s'abonner.", "Dos formas de suscribirse.", "Два способа подписаться.")
t("The yearly plan saves you the price of two months. Both give you the same unlimited access.",
  "Le plan annuel vous fait économiser le prix de deux mois. Les deux vous donnent le même accès illimité.",
  "El plan anual te ahorra el precio de dos meses. Ambos te dan el mismo acceso ilimitado.",
  "Годовой план экономит вам цену двух месяцев. Оба дают одинаковый безлимитный доступ.")
t("Plan", "Plan", "Plan", "План")
t("Per month", "Par mois", "Por mes", "В месяц")
t("Notes", "Notes", "Notas", "Заметки")
t("Monthly", "Mensuel", "Mensual", "Помесячно")
t("$9.99/month", "9,99 $/mois", "9,99 $/mes", "$9.99/мес")
t("$9.99", "9,99 $", "9,99 $", "$9.99")
t("Unlimited analyses, all six lenses.",
  "Analyses illimitées, six lentilles.",
  "Análisis ilimitados, las seis lentes.",
  "Безлимитные анализы, все шесть линз.")
t("Subscribe →", "S'abonner →", "Suscribirse →", "Подписаться →")
t("Yearly", "Annuel", "Anual", "Ежегодно")
t("$99.99/year", "99,99 $/an", "99,99 $/año", "$99.99/год")
t("$8.33", "8,33 $", "8,33 $", "$8.33")
t("best value · 2 months free", "meilleure valeur · 2 mois gratuits", "mejor valor · 2 meses gratis", "лучшая цена · 2 месяца бесплатно")
t("Same access, cheaper. Cancel anytime.",
  "Même accès, moins cher. Annulez à tout moment.",
  "Mismo acceso, más barato. Cancela cuando quieras.",
  "Тот же доступ, дешевле. Отмена в любой момент.")
t("Subscriptions auto-renew unless cancelled at least 24 hours before the end of the current period. You can manage and cancel anytime in iPhone Settings → Apple ID → Subscriptions.",
  "Les abonnements se renouvellent automatiquement sauf annulation au moins 24 heures avant la fin de la période en cours. Vous pouvez gérer et annuler à tout moment dans Réglages iPhone → Identifiant Apple → Abonnements.",
  "Las suscripciones se renuevan automáticamente a menos que se cancelen al menos 24 horas antes del final del período actual. Puedes gestionarlas y cancelarlas en cualquier momento en Ajustes iPhone → ID de Apple → Suscripciones.",
  "Подписки автопродлеваются, если только не отменить их минимум за 24 часа до конца текущего периода. Управлять и отменять можно в любой момент в Настройках iPhone → Apple ID → Подписки.")
t("Side by side", "Côte à côte", "Lado a lado", "Бок о бок")
t("Which path is right for you?",
  "Quelle voie vous convient ?",
  "¿Qué camino te conviene?",
  "Какой путь подходит вам?")
t("The rule of thumb: if you'll read more than three or four reports a year, the subscription is cheaper. If you want it for one specific moment, credits are cleaner.",
  "Règle empirique : si vous lirez plus de trois ou quatre rapports par an, l'abonnement est moins cher. Si vous le voulez pour un moment spécifique, les crédits sont plus propres.",
  "Regla general: si vas a leer más de tres o cuatro reportes al año, la suscripción es más barata. Si lo quieres para un momento específico, los créditos son más limpios.",
  "Правило большого пальца: если вы будете читать больше трёх-четырёх отчётов в год, подписка дешевле. Если хотите для конкретного момента — кредиты чище.")
t("1 free credit", "1 crédit gratuit", "1 crédito gratis", "1 бесплатный кредит")
t("Number of analyses", "Nombre d'analyses", "Número de análisis", "Количество анализов")
t("1 (on first launch)", "1 (au premier lancement)", "1 (en el primer arranque)", "1 (при первом запуске)")
t("= credits purchased", "= crédits achetés", "= créditos comprados", "= купленные кредиты")
t("Unlimited", "Illimité", "Ilimitado", "Безлимит")
t("All 6 lenses", "Les 6 lentilles", "Las 6 lentes", "Все 6 линз")
t("All 61 modules", "Les 61 modules", "Los 61 módulos", "Все 61 модуль")
t("Insight Library — filter, sort, explore past reports",
  "Bibliothèque d'Insights — filtrer, trier, explorer les rapports passés",
  "Biblioteca de Insights — filtrar, ordenar, explorar reportes pasados",
  "Библиотека Инсайтов — фильтровать, сортировать, исследовать прошлые отчёты")
t("Copy, export &amp; share reports",
  "Copier, exporter et partager les rapports",
  "Copiar, exportar y compartir reportes",
  "Копировать, экспортировать и делиться отчётами")
t("Early access to new lenses",
  "Accès anticipé aux nouvelles lentilles",
  "Acceso anticipado a nuevas lentes",
  "Ранний доступ к новым линзам")
t("Recurring charge", "Frais récurrents", "Cargo recurrente", "Регулярная оплата")
t("No", "Non", "No", "Нет")
t("Yes — $9.99/mo or $99.99/yr",
  "Oui — 9,99 $/mois ou 99,99 $/an",
  "Sí — 9,99 $/mes o 99,99 $/año",
  "Да — $9.99/мес или $99.99/год")
t("Expires?", "Expire ?", "¿Caduca?", "Сгорает?")
t("One-shot, free", "Un coup, gratuit", "Una vez, gratis", "Один раз, бесплатно")
t("Credits never expire", "Les crédits n'expirent jamais", "Los créditos no caducan nunca", "Кредиты не сгорают")
t("Active while subscribed", "Actif tant qu'abonné", "Activo mientras suscrito", "Активно пока подписаны")
t("FAQ", "FAQ", "FAQ", "FAQ")
t("Things worth knowing.", "Choses bonnes à savoir.", "Cosas que vale la pena saber.", "Что стоит знать.")
t("Is the first analysis really free? Do you need a card?",
  "La première analyse est-elle vraiment gratuite ? Avez-vous besoin d'une carte ?",
  "¿Es realmente gratis el primer análisis? ¿Hace falta tarjeta?",
  "Действительно ли первый анализ бесплатен? Нужна ли карта?")
t("Yes — fully free. The app grants 1 analysis credit on first launch. No card, no account, no email required. Drop in a chat, choose your lens, get the reading.",
  "Oui — entièrement gratuit. L'app accorde 1 crédit d'analyse au premier lancement. Pas de carte, pas de compte, pas d'email requis. Déposez un chat, choisissez votre lentille, obtenez la lecture.",
  "Sí — totalmente gratis. La app otorga 1 crédito de análisis en el primer arranque. Sin tarjeta, sin cuenta, sin email requerido. Suelta un chat, elige tu lente, recibe la lectura.",
  "Да — полностью бесплатен. Приложение даёт 1 кредит на анализ при первом запуске. Без карты, без аккаунта, без email. Закиньте чат, выберите линзу, получите портрет.")
t("What's the difference between credits and a subscription?",
  "Quelle est la différence entre les crédits et un abonnement ?",
  "¿Cuál es la diferencia entre créditos y suscripción?",
  "В чём разница между кредитами и подпиской?")
t("Credits are pay-as-you-go — each credit is one analysis, credits never expire, no recurring charge. A subscription is unlimited analyses while it's active, plus the Insight Library, PDF export, and early access to new lenses. Pick credits if you want the app for a specific moment; pick a subscription if you'll come back to it across the year.",
  "Les crédits sont à l'usage — chaque crédit est une analyse, les crédits n'expirent jamais, aucun frais récurrent. Un abonnement est des analyses illimitées tant qu'il est actif, plus la Bibliothèque d'Insights, l'export PDF, et l'accès anticipé aux nouvelles lentilles. Choisissez les crédits si vous voulez l'app pour un moment spécifique ; choisissez un abonnement si vous y reviendrez au cours de l'année.",
  "Los créditos son pago por uso — cada crédito es un análisis, los créditos no caducan, sin cargo recurrente. Una suscripción son análisis ilimitados mientras está activa, además de la Biblioteca de Insights, exportación a PDF, y acceso anticipado a nuevas lentes. Elige créditos si quieres la app para un momento específico; elige suscripción si vas a volver a ella durante el año.",
  "Кредиты — это плата за использование: каждый кредит — это один анализ, кредиты не сгорают, без регулярных платежей. Подписка — это безлимитные анализы, пока она активна, плюс Библиотека Инсайтов, экспорт в PDF и ранний доступ к новым линзам. Выбирайте кредиты, если хотите приложение для конкретного момента; выбирайте подписку, если будете возвращаться к нему в течение года.")
t("If I cancel the subscription, do I lose my past readings?",
  "Si j'annule l'abonnement, est-ce que je perds mes lectures passées ?",
  "Si cancelo la suscripción, ¿pierdo mis lecturas anteriores?",
  "Если я отменю подписку, потеряю ли я свои прошлые портреты?")
t("No. Every reading you've already generated stays on your iPhone, forever. Cancelling just means you stop being able to generate <em>new</em> readings on the unlimited plan. Subscription-only features (Insight Library, PDF export) pause until you resubscribe.",
  "Non. Chaque lecture que vous avez déjà générée reste sur votre iPhone, pour toujours. Annuler signifie juste que vous ne pouvez plus générer de <em>nouvelles</em> lectures sur le plan illimité. Les fonctionnalités réservées aux abonnés (Bibliothèque d'Insights, export PDF) sont mises en pause jusqu'à ce que vous vous réabonniez.",
  "No. Cada lectura que ya hayas generado se queda en tu iPhone, para siempre. Cancelar solo significa que dejas de poder generar <em>nuevas</em> lecturas en el plan ilimitado. Las funciones solo para suscriptores (Biblioteca de Insights, exportación a PDF) se pausan hasta que vuelvas a suscribirte.",
  "Нет. Каждый портрет, который вы уже сгенерировали, остаётся на вашем iPhone навсегда. Отмена означает только то, что вы перестаёте генерировать <em>новые</em> портреты на безлимитном плане. Функции для подписчиков (Библиотека Инсайтов, экспорт в PDF) приостанавливаются до повторной подписки.")
t("Can I switch between credits and subscription?",
  "Puis-je basculer entre crédits et abonnement ?",
  "¿Puedo cambiar entre créditos y suscripción?",
  "Могу ли я переключаться между кредитами и подпиской?")
t("Yes. You can cancel a subscription anytime in iPhone Settings and start using credits instead. Any credit balance you bought separately is unaffected — credits stack with subscriptions and survive cancellation.",
  "Oui. Vous pouvez annuler un abonnement à tout moment dans les Réglages iPhone et commencer à utiliser des crédits à la place. Tout solde de crédit que vous avez acheté séparément n'est pas affecté — les crédits s'empilent avec les abonnements et survivent à l'annulation.",
  "Sí. Puedes cancelar una suscripción en cualquier momento en los Ajustes de iPhone y empezar a usar créditos. Cualquier saldo de créditos que hayas comprado por separado no se ve afectado — los créditos se acumulan con las suscripciones y sobreviven a la cancelación.",
  "Да. Вы можете отменить подписку в любой момент в Настройках iPhone и начать использовать кредиты. Любой баланс кредитов, купленный отдельно, не затрагивается — кредиты складываются с подпиской и переживают отмену.")
t("Does one credit = one chat? Or one lens?",
  "Un crédit = un chat ? Ou une lentille ?",
  "¿Un crédito = un chat? ¿O una lente?",
  "Один кредит = один чат? Или одна линза?")
t("One credit = one full analysis (one chat × one lens). If you want to re-analyse the same chat through a second lens — say you ran Romantic and now want Self too — that's a second analysis. Subscribers get this re-analysis included; credit users spend one credit per re-run.",
  "Un crédit = une analyse complète (un chat × une lentille). Si vous voulez ré-analyser le même chat à travers une seconde lentille — disons que vous avez lancé Romantique et voulez maintenant Soi aussi — c'est une seconde analyse. Les abonnés ont cette ré-analyse incluse ; les utilisateurs de crédits dépensent un crédit par relance.",
  "Un crédito = un análisis completo (un chat × una lente). Si quieres reanalizar el mismo chat con una segunda lente — digamos que ejecutaste Romántica y ahora quieres también Yo — eso es un segundo análisis. Los suscriptores tienen este reanálisis incluido; los usuarios de créditos gastan un crédito por cada nueva ejecución.",
  "Один кредит = один полный анализ (один чат × одна линза). Если хотите перепрогнать тот же чат через вторую линзу — скажем, запустили Романтика и теперь хотите ещё Я — это второй анализ. У подписчиков это включено; пользователи кредитов тратят один кредит за каждый перезапуск.")
t('Why is the yearly plan "two months free" instead of, say, fifteen percent off?',
  "Pourquoi le plan annuel est-il « deux mois gratuits » au lieu, disons, de quinze pour cent de réduction ?",
  "¿Por qué el plan anual es «dos meses gratis» en lugar de, digamos, un quince por ciento de descuento?",
  "Почему годовой план «два месяца бесплатно», а не, скажем, скидка пятнадцать процентов?")
t("Because that's the honest math. $9.99 × 12 = $119.88. The yearly plan is $99.99 — saving you $19.89, or two months. We didn't want to dress it up as a bigger discount than it is.",
  "Parce que ce sont les maths honnêtes. 9,99 $ × 12 = 119,88 $. Le plan annuel est à 99,99 $ — économisant 19,89 $, soit deux mois. Nous ne voulions pas le déguiser en une remise plus grande qu'elle ne l'est.",
  "Porque esa es la matemática honesta. 9,99 $ × 12 = 119,88 $. El plan anual cuesta 99,99 $ — ahorrándote 19,89 $, o dos meses. No quisimos disfrazarlo como un descuento mayor de lo que es.",
  "Потому что это честная математика. $9.99 × 12 = $119.88. Годовой план — $99.99, экономия $19.89, то есть два месяца. Мы не хотели приукрашивать это, выдавая за большую скидку, чем есть.")
t("Are prices in USD only?",
  "Les prix sont-ils en USD uniquement ?",
  "¿Los precios son solo en USD?",
  "Цены только в USD?")
t("USD is the reference price. Apple's App Store automatically displays the equivalent amount in your local currency (€, £, ₽, etc.) at checkout, using its standard pricing tiers.",
  "L'USD est le prix de référence. L'App Store d'Apple affiche automatiquement le montant équivalent dans votre devise locale (€, £, ₽, etc.) au moment du paiement, en utilisant ses niveaux de prix standard.",
  "USD es el precio de referencia. El App Store de Apple muestra automáticamente el importe equivalente en tu moneda local (€, £, ₽, etc.) en el pago, usando sus niveles de precios estándar.",
  "USD — это базовая цена. App Store от Apple автоматически отображает эквивалент в вашей локальной валюте (€, £, ₽ и т.д.) на этапе оплаты, используя стандартные ценовые уровни.")
t("Refunds?", "Remboursements ?", "¿Reembolsos?", "Возвраты?")
t("All purchases run through Apple's standard refund process. If something genuinely went wrong — a reading didn't generate, credits didn't deliver — submit a support request to Apple and we'll work with them to resolve it.",
  "Tous les achats passent par le processus de remboursement standard d'Apple. Si quelque chose ne va vraiment pas — une lecture n'a pas été générée, des crédits n'ont pas été livrés — soumettez une demande de support à Apple et nous travaillerons avec eux pour résoudre cela.",
  "Todas las compras pasan por el proceso estándar de reembolso de Apple. Si algo realmente salió mal — una lectura no se generó, los créditos no se entregaron — envía una solicitud de soporte a Apple y trabajaremos con ellos para resolverlo.",
  "Все покупки идут через стандартный процесс возврата Apple. Если что-то действительно пошло не так — портрет не сгенерировался, кредиты не доставились — отправьте запрос в поддержку Apple, и мы поработаем с ними, чтобы решить это.")
t("Start with the free analysis.",
  "Commencez avec l'analyse gratuite.",
  "Empieza con el análisis gratis.",
  "Начните с бесплатного анализа.")
t("One free credit on first launch. No card, no account. Read your first chat before you spend a cent.",
  "Un crédit gratuit au premier lancement. Pas de carte, pas de compte. Lisez votre premier chat avant de dépenser un centime.",
  "Un crédito gratis en el primer arranque. Sin tarjeta, sin cuenta. Lee tu primer chat antes de gastar un céntimo.",
  "Один бесплатный кредит при первом запуске. Без карты, без аккаунта. Прочитайте свой первый чат до того, как потратите хоть копейку.")

# ============================================================
# TESTIMONIALS page
# ============================================================
t("Testimonials — Persona Lens", "Témoignages — Persona Lens", "Testimonios — Persona Lens", "Отзывы — Persona Lens")
t("Reader reactions to Persona Lens — what people said after running each of the six lenses. Honest, specific, occasionally unflattering.",
  "Réactions des lecteurs à Persona Lens — ce que les gens ont dit après avoir lancé chacune des six lentilles. Honnête, spécifique, occasionnellement peu flatteur.",
  "Reacciones de lectores a Persona Lens — lo que la gente dijo después de ejecutar cada una de las seis lentes. Honesto, específico, ocasionalmente poco halagador.",
  "Реакции читателей на Persona Lens — что говорили люди после запуска каждой из шести линз. Честно, конкретно, иногда нелестно.")
t("Here's what people said after one analysis.",
  "Voici ce que les gens ont dit après une analyse.",
  "Esto es lo que dijo la gente después de un análisis.",
  "Вот что говорили люди после одного анализа.")
t("A page of real reactions, sorted by which lens they ran. Some are funny. Some are a little uncomfortable. None of them are made up.",
  "Une page de vraies réactions, triées par lentille lancée. Certaines sont drôles. Certaines sont un peu inconfortables. Aucune n'est inventée.",
  "Una página de reacciones reales, ordenadas por la lente que ejecutaron. Algunas son divertidas. Algunas son un poco incómodas. Ninguna está inventada.",
  "Страница реальных реакций, отсортированных по запущенной линзе. Некоторые забавные. Некоторые слегка неловкие. Ни одна не выдумана.")
t("After running Self Lens", "Après avoir lancé la lentille Soi", "Después de ejecutar la lente Yo", "После запуска линзы Я")
t('"It quoted me back at myself."',
  "« Elle m'a recité mes propres mots. »",
  "«Me citó a mí mismo».",
  "«Она процитировала меня самому себе.»")
t("After running Romantic Lens", "Après avoir lancé la lentille Romantique", "Después de ejecutar la lente Romántica", "После запуска линзы Романтика")
t('"It said the thing my friends had stopped telling me."',
  "« Elle a dit la chose que mes amis avaient cessé de me dire. »",
  "«Dijo lo que mis amigos habían dejado de decirme».",
  "«Она сказала то, что друзья уже перестали мне говорить.»")
t("After running Friendship Lens", "Après avoir lancé la lentille Amitié", "Después de ejecutar la lente Amistad", "После запуска линзы Дружба")
t('"We sent the card to each other within five minutes."',
  "« On s'est envoyé la carte mutuellement en cinq minutes. »",
  "«Nos enviamos la tarjeta la una a la otra en cinco minutos».",
  "«Мы отправили карточку друг другу в течение пяти минут.»")
t("After running Professional Lens", "Après avoir lancé la lentille Professionnelle", "Después de ejecutar la lente Profesional", "После запуска линзы Работа")
t('"I walked into my 1:1 with a plan."',
  "« Je suis entré(e) dans mon 1:1 avec un plan. »",
  "«Entré en mi 1:1 con un plan».",
  "«Я зашёл на свой 1:1 с планом.»")
t("After running Family Lens", "Après avoir lancé la lentille Famille", "Después de ejecutar la lente Familia", "После запуска линзы Семья")
t('"It found the phrase I didn\'t know I\'d inherited."',
  "« Elle a trouvé la phrase dont j'ignorais avoir hérité. »",
  "«Encontró la frase que no sabía que había heredado».",
  "«Она нашла фразу, о наследовании которой я не догадывался.»")
t("After running Group Lens", "Après avoir lancé la lentille Groupe", "Después de ejecutar la lente Grupo", "После запуска линзы Группа")
t('"The Awards Ceremony broke our group chat for three days."',
  "« La Cérémonie des Prix a cassé notre groupe pendant trois jours. »",
  "«La Ceremonia de Premios rompió nuestro chat de grupo durante tres días».",
  "«Церемония Наград сломала наш групповой чат на три дня.»")
t("Run a lens on a chat you've reread too often.",
  "Lancez une lentille sur un chat que vous avez trop souvent relu.",
  "Ejecuta una lente en un chat que has releído demasiado a menudo.",
  "Запустите линзу на чате, который вы перечитывали слишком часто.")
t("The first reading is free. Pick the lens that's been on your mind.",
  "La première lecture est gratuite. Choisissez la lentille qui vous trotte dans la tête.",
  "La primera lectura es gratis. Elige la lente que tienes en mente.",
  "Первый портрет бесплатен. Выберите линзу, которая занимает ваши мысли.")
t("The names, locations, and identifying details on this page are illustrative and represent the kind of feedback Persona Lens is designed to produce. We will replace them with named, signed-off testimonials from real users as they come in post-launch — at which point this page becomes a record, not a preview.",
  "Les noms, lieux et détails d'identification sur cette page sont illustratifs et représentent le type de retours que Persona Lens est conçu pour produire. Nous les remplacerons par des témoignages nommés et signés de vrais utilisateurs au fur et à mesure qu'ils arriveront après le lancement — à ce moment-là, cette page deviendra un dossier, pas un aperçu.",
  "Los nombres, ubicaciones y detalles identificativos en esta página son ilustrativos y representan el tipo de feedback que Persona Lens está diseñado para producir. Los reemplazaremos por testimonios nombrados y firmados de usuarios reales a medida que vayan llegando tras el lanzamiento — momento en el que esta página se convertirá en un registro, no en un avance.",
  "Имена, локации и идентифицирующие детали на этой странице иллюстративны и представляют тип обратной связи, который Persona Lens призван производить. Мы заменим их именованными подписанными отзывами реальных пользователей по мере их поступления после запуска — после чего эта страница станет записью, а не превью.")


# Mobile-nav aria label
t("Mobile navigation", "Navigation mobile", "Navegación móvil", "Мобильная навигация")
t("Menu", "Menu", "Menú", "Меню")


# ============================================================
# NEW translations — positioning rewrite + testimonials + guides nav
# ============================================================

# New homepage hero (broader positioning)
t("Understand any relationship<br/>in three minutes.",
  "Comprenez n'importe quelle relation<br/>en trois minutes.",
  "Entiende cualquier relación<br/>en tres minutos.",
  "Поймите любые отношения<br/>за три минуты.")
t("Your partner. Your parent. Your friend. Your boss. Your group chat. Persona Lens reads the conversation you've already had with them and returns a structured psychological reading — backed by 30 years of attachment and personality research. Quick. Reliable. Yours.",
  "Votre partenaire. Votre parent. Votre ami. Votre boss. Votre groupe de discussion. Persona Lens lit la conversation que vous avez déjà eue avec eux et renvoie un portrait psychologique structuré — appuyé sur 30 ans de recherches sur l'attachement et la personnalité. Rapide. Fiable. À vous.",
  "Tu pareja. Tu madre o padre. Tu amigo. Tu jefe. Tu chat de grupo. Persona Lens lee la conversación que ya has tenido con ellos y devuelve una lectura psicológica estructurada — respaldada por 30 años de investigación sobre apego y personalidad. Rápido. Fiable. Tuyo.",
  "Ваш партнёр. Ваш родитель. Ваш друг. Ваш руководитель. Ваш групповой чат. Persona Lens читает разговор, который у вас с ними уже был, и возвращает структурированный психологический разбор — на базе 30 лет исследований привязанности и личности. Быстро. Надёжно. Ваше.")

# Guides nav label
t("Guides", "Guides", "Guías", "Гайды")

# Related Guides section on lens pages
t("Guides for this lens", "Guides pour cette lentille", "Guías para esta lente", "Гайды для этой линзы")
t("If you want to dig deeper.", "Pour aller plus loin.", "Si quieres profundizar.", "Если хотите копнуть глубже.")
t("These guides walk through the patterns this lens reads — written longer-form, for the people who want the framework before they run their own reading.",
  "Ces guides détaillent les patterns que cette lentille lit — sous une forme plus longue, pour celles et ceux qui veulent comprendre le cadre avant de lancer leur propre lecture.",
  "Estas guías recorren los patrones que esta lente lee — en formato largo, para quien quiere entender el marco antes de hacer su propia lectura.",
  "Эти гайды разбирают паттерны, которые читает эта линза — в длинном формате, для тех, кто хочет понять рамку прежде, чем запустить свой собственный портрет.")
t("Browse all guides →", "Voir tous les guides →", "Ver todas las guías →", "Все гайды →")

# Testimonial quotes — these are the long quotes that fell through to English
# Self Lens
t('"My Persona Card said I was \'a quiet host — asks before she offers\'. My boyfriend read it over my shoulder and laughed for ninety seconds. He didn\'t know there was an app for me yet."',
  "« Ma Carte Persona m'a appelée « un hôte discret — demande avant d'offrir ». Mon copain l'a lue par-dessus mon épaule et a ri pendant quatre-vingt-dix secondes. Il ne savait pas qu'il existait une app pour moi. »",
  "«Mi Tarjeta Persona me llamó \"una anfitriona silenciosa — pregunta antes de ofrecer\". Mi novio lo leyó por encima de mi hombro y se rió noventa segundos. No sabía que existía una app para mí.»",
  "«Моя Карта Персоны назвала меня «тихим хозяином — спрашивает прежде чем предложить». Мой парень прочитал через плечо и смеялся девяносто секунд. Он не знал, что для меня уже есть приложение.»")
t('"It told me I say \'no rush\' three times more often than \'I need you\' and that I should try saying the second one this month. I\'m trying. It\'s hard."',
  "« Elle m'a dit que je dis « pas pressé » trois fois plus souvent que « j'ai besoin de toi » et que je devrais essayer de dire la seconde phrase ce mois-ci. J'essaie. C'est difficile. »",
  "«Me dijo que digo \"sin prisa\" tres veces más a menudo que \"te necesito\" y que debería intentar decir la segunda este mes. Lo intento. Es difícil.»",
  "«Оно сказало мне, что я говорю «не торопись» в три раза чаще, чем «ты мне нужен», и что в этом месяце надо попробовать сказать второе. Пробую. Это трудно.»")
t('"I expected the personality test to flatter me. It did not flatter me. It also wasn\'t wrong. Five stars, will read again next quarter."',
  "« Je m'attendais à ce que le test de personnalité me flatte. Il ne m'a pas flatté. Il n'avait pas tort non plus. Cinq étoiles, je relirai le trimestre prochain. »",
  "«Esperaba que el test de personalidad me adulara. No me aduló. Tampoco se equivocó. Cinco estrellas, lo volveré a leer el próximo trimestre.»",
  "«Я ожидал, что тест личности мне польстит. Он мне не польстил. Но и не ошибся. Пять звёзд, перечитаю в следующем квартале.»")

# Romantic Lens
t('"The Trajectory module said \'rising\'. The man in question said \'rising\' in his own way the following weekend. I want to know how the app knew before he did."',
  "« Le module Trajectoire a dit « en hausse ». L'intéressé l'a dit à sa manière le week-end suivant. J'aimerais savoir comment l'app l'a su avant lui. »",
  "«El módulo de Trayectoria dijo \"en ascenso\". El hombre en cuestión lo dijo a su manera el fin de semana siguiente. Quiero saber cómo lo supo la app antes que él.»",
  "«Модуль Траектория сказал «растёт». Сам мужчина сказал «растёт» по-своему в следующие выходные. Хочу знать, как приложение поняло раньше него.»")
t('"I ran it on an ex out of curiosity. The lens was kinder to him than I\'d been. It said I\'d been bringing my mother\'s expectations into a relationship that wasn\'t built for them. I\'m not over it. But I\'m thinking."',
  "« Je l'ai lancé sur un ex par curiosité. La lentille a été plus indulgente que moi avec lui. Elle a dit que j'apportais les attentes de ma mère dans une relation qui n'était pas faite pour les porter. Ce n'est pas digéré. Mais je réfléchis. »",
  "«Lo ejecuté sobre un ex por curiosidad. La lente fue más amable con él que yo. Dijo que estaba metiendo las expectativas de mi madre en una relación que no estaba hecha para soportarlas. No lo he superado. Pero estoy pensándolo.»",
  "«Запустила на бывшем из любопытства. Линза была к нему добрее, чем я. Сказала, что я приносила в отношения мамины ожидания, под которые они не были построены. Я не отпустила. Но думаю.»")

# Friendship Lens
t('"It called us \'a Ride-or-Die / Wise Counsel pair — she brings the storm, you bring the lighthouse\'. I screenshotted it. She has it as her phone background now. Twelve years of friendship and we needed an app to name it."',
  "« Elle nous a appelées « une paire Inséparables / Conseillère Sage — elle apporte la tempête, tu apportes le phare ». J'ai fait un screenshot. Elle l'a en fond d'écran maintenant. Douze ans d'amitié et il a fallu une app pour la nommer. »",
  "«Nos llamó \"una pareja Hasta-la-Muerte / Consejera Sabia — ella trae la tormenta, tú traes el faro\". Hice captura. Ahora ella la tiene de fondo de pantalla. Doce años de amistad y necesitamos una app para nombrarla.»",
  "«Назвала нас «парой До-Конца / Мудрый Советник — она приносит шторм, ты приносишь маяк». Я заскринила. У неё теперь это на заставке телефона. Двенадцать лет дружбы — и понадобилось приложение, чтобы это назвать.»")
t('"Give-and-Take told me I\'d been holding the emotional load for our friendship for two years. I sent it to her. She didn\'t deny it. We\'re better now."',
  "« Le module Équilibre des échanges m'a dit que je portais la charge émotionnelle de notre amitié depuis deux ans. Je le lui ai envoyé. Elle n'a pas nié. On va mieux maintenant. »",
  "«Equilibrio de Intercambios me dijo que llevaba dos años cargando con el peso emocional de nuestra amistad. Se lo envié. No lo negó. Ahora estamos mejor.»",
  "«Модуль Баланса сказал, что я уже два года несу эмоциональную нагрузку нашей дружбы. Я ей это отправила. Она не отрицала. Сейчас нам лучше.»")
t('"It said we have eleven inside jokes still alive and named them. We argued about whether one had aged. We were both right."',
  "« Elle a dit qu'on a onze blagues internes encore vivantes et les a nommées. On s'est disputés pour savoir si l'une avait vieilli. On avait raison tous les deux. »",
  "«Dijo que tenemos once chistes internos aún vivos y los nombró. Discutimos si uno había envejecido. Los dos teníamos razón.»",
  "«Сказала, что у нас одиннадцать внутренних шуток ещё живы, и назвала их. Мы спорили, постарела ли одна из них. Оба были правы.»")

# Professional Lens
t('"It read three weeks of Slack with my new manager and told me she was a Strategist who decides in meetings but commits in writing. I followed up our next chat with a one-paragraph recap. She replied \'yes\' inside ten minutes. I\'d been waiting four weeks before."',
  "« Elle a lu trois semaines de Slack avec ma nouvelle manager et m'a dit qu'elle était une Stratège qui décide en réunion mais s'engage par écrit. J'ai suivi notre conversation suivante avec un récap en un paragraphe. Elle a répondu « oui » en moins de dix minutes. J'attendais depuis quatre semaines. »",
  "«Leyó tres semanas de Slack con mi nueva manager y me dijo que era una Estratega que decide en reuniones pero se compromete por escrito. Hice seguimiento de la siguiente conversación con un recap de un párrafo. Respondió \"sí\" en menos de diez minutos. Llevaba cuatro semanas esperando antes.»",
  "«Прочитал три недели Slack с моей новой руководительницей и сказал, что она Стратег, который решает на встречах, но коммитится письменно. Я отправил после следующего разговора краткое резюме в один абзац. Она ответила «да» в течение десяти минут. До этого я ждал четыре недели.»")
t('"I\'d been told I was \'too soft\' in negotiations. The lens told me I was actually under-asserting one specific way — opening with the smaller ask. Tiny correction. Got the bigger one approved last week."',
  "« On m'avait dit que j'étais « trop doux » en négociation. La lentille m'a dit que j'étais en fait sous-affirmé d'une façon précise — j'ouvrais avec la plus petite demande. Petite correction. La grosse a été validée la semaine dernière. »",
  "«Me habían dicho que era \"demasiado blando\" negociando. La lente me dijo que en realidad estaba subafirmándome de una forma concreta — abriendo con la petición más pequeña. Mínima corrección. La grande me la aprobaron la semana pasada.»",
  "«Мне говорили, что я «слишком мягкий» в переговорах. Линза сказала, что я на самом деле недостаточно настойчив одним конкретным способом — открываю с меньшей просьбы. Маленькая поправка. Большую одобрили на прошлой неделе.»")
t('"I ran the lens on a client I\'d been losing. It told me he was a \'Diplomat with operator instincts\' and that my long emails were burying my point. I sent three lines the next morning. He replied in twenty minutes."',
  "« J'ai lancé la lentille sur un client que je perdais. Elle m'a dit qu'il était un « Diplomate avec des instincts d'opérateur » et que mes longs emails enterraient mon propos. J'ai envoyé trois lignes le lendemain matin. Il a répondu en vingt minutes. »",
  "«Ejecuté la lente sobre un cliente que estaba perdiendo. Me dijo que era un \"Diplomático con instintos de operador\" y que mis emails largos enterraban mi mensaje. Envié tres líneas a la mañana siguiente. Respondió en veinte minutos.»",
  "«Запустил линзу на клиенте, которого терял. Она сказала, что он «Дипломат с инстинктами оператора» и мои длинные письма хоронят суть. На следующее утро я отправил три строки. Он ответил через двадцать минут.»")

# Family Lens
t('"Communication Archaeology pulled out a phrase my mother says — \'don\'t make me ask twice\' — and showed me I now text it to my brother. I sat with that for an hour. I texted my mother. I have not stopped thinking about it."',
  "« L'Archéologie de la Communication a extrait une phrase de ma mère — « ne me fais pas demander deux fois » — et m'a montré que je la textote maintenant à mon frère. Je suis restée avec ça pendant une heure. J'ai écrit à ma mère. Je n'ai pas arrêté d'y penser. »",
  "«Arqueología de la Comunicación sacó una frase que dice mi madre — \"no me hagas preguntarlo dos veces\" — y me mostró que ahora se la escribo a mi hermano. Estuve con eso una hora. Le escribí a mi madre. No he dejado de pensarlo.»",
  "«Археология Коммуникации вытащила фразу, которую говорит моя мама — «не заставляй меня спрашивать дважды» — и показала, что я теперь пишу её брату. Я просидела с этим час. Написала маме. Не перестаю об этом думать.»")
t('"It said I was the Mediator in my family chat. My sister read it and said: \'that is the kindest way anyone has ever described it.\' That\'s the line that got me."',
  "« Elle a dit que j'étais la Médiatrice dans notre chat familial. Ma sœur l'a lu et a dit : « c'est la façon la plus tendre que quelqu'un ait jamais utilisée pour le décrire. » C'est cette phrase qui m'a eue. »",
  "«Dijo que yo era la Mediadora en el chat familiar. Mi hermana lo leyó y dijo: \"esa es la forma más amable en que alguien lo ha descrito jamás\". Esa fue la frase que me llegó.»",
  "«Сказала, что я Посредник в нашем семейном чате. Сестра прочитала и сказала: «это самая добрая формулировка, которую кто-либо когда-либо использовал». Вот эта фраза меня и пробила.»")
t('"The Emotional Ledger named what I\'d been doing for my parents for ten years. I cried at the bus stop. Then I called my dad. Then I shared the app with three cousins."',
  "« Le Registre Émotionnel a nommé ce que je faisais pour mes parents depuis dix ans. J'ai pleuré à l'arrêt de bus. Puis j'ai appelé mon père. Puis j'ai partagé l'app avec trois cousins. »",
  "«El Libro de Cuentas Emocional nombró lo que llevaba diez años haciendo por mis padres. Lloré en la parada del bus. Después llamé a mi padre. Después compartí la app con tres primos.»",
  "«Эмоциональная Бухгалтерия назвала то, что я делал для родителей десять лет. Я расплакался на автобусной остановке. Потом позвонил отцу. Потом поделился приложением с тремя двоюродными.»")

# Group Lens
t('"Ran it on our bridesmaid chat. Pia got \'Most Likely to Send Voice Memos at 1AM\' and the entire group lost it. We screenshotted the whole thing. It\'s pinned in the chat now."',
  "« Lancé sur le chat des demoiselles d'honneur. Pia a eu « La plus susceptible d'envoyer des vocaux à 1h du matin » et tout le groupe a explosé. On a tout capturé en screenshot. C'est épinglé dans le chat maintenant. »",
  "«Lo lancé sobre el chat de damas de honor. Pia se llevó \"Más probable de mandar audios a la 1 de la madrugada\" y el grupo entero se rió a carcajadas. Hicimos captura de todo. Ahora está fijado en el chat.»",
  "«Запустила на чате подружек невесты. Пия получила «Самая вероятная отправить голосовые в час ночи», и вся группа упала. Мы всё заскринили. Теперь это закреплено в чате.»")
t('"The lens called me \'The Catch-Up Queen\' — replies to 200 messages at 11 PM with a one-line summary. Three people texted me separately to ask how it knew. I\'m choosing to find it flattering."',
  "« La lentille m'a appelée « La Reine du Catch-Up » — répond à 200 messages à 23 h avec un résumé en une ligne. Trois personnes m'ont écrit séparément pour demander comment elle savait. Je choisis de prendre ça comme un compliment. »",
  "«La lente me llamó \"La Reina del Catch-Up\" — responde a 200 mensajes a las 11 de la noche con un resumen de una línea. Tres personas me escribieron por separado preguntando cómo lo sabía. Elijo tomarlo como un cumplido.»",
  "«Линза назвала меня «Королевой Догоняния» — отвечает на 200 сообщений в 11 вечера однострочным резюме. Трое написали мне отдельно, спрашивая, как она это узнала. Решила воспринимать это как комплимент.»")
t('"Our fantasy football chat got the Alliance Theory module. It correctly identified that Tom and Will run a side chat about the rest of us. Tom and Will deny it. The card is going on a t-shirt."',
  "« Notre chat fantasy football a eu le module Théorie des Alliances. Il a correctement identifié que Tom et Will tiennent un chat parallèle sur le reste d'entre nous. Tom et Will nient. La carte va finir sur un t-shirt. »",
  "«Nuestro chat de fantasy football tuvo el módulo de Teoría de Alianzas. Identificó correctamente que Tom y Will llevan un chat paralelo sobre el resto. Tom y Will lo niegan. La tarjeta va a acabar en una camiseta.»",
  "«Наш чат фэнтези-футбола получил модуль Теории Альянсов. Он правильно определил, что Том и Уилл ведут параллельный чат об остальных. Том и Уилл отрицают. Карточка пойдёт на футболку.»")
t('"I\'m the quietest member of our running club chat. The lens called me \'The Glue\' and said the chat is warm because I keep it warm. I have never been told that. I needed it more than I knew."',
  "« Je suis le membre le plus discret du chat de notre club de course. La lentille m'a appelée « La Colle » et a dit que le chat est chaleureux parce que je le maintiens chaleureux. On ne me l'avait jamais dit. J'en avais plus besoin que je ne le savais. »",
  "«Soy la miembro más callada del chat de nuestro club de running. La lente me llamó \"El Pegamento\" y dijo que el chat es cálido porque yo lo mantengo cálido. Nadie me lo había dicho nunca. Lo necesitaba más de lo que sabía.»",
  "«Я самый молчаливый член чата нашего бегового клуба. Линза назвала меня «Клеем» и сказала, что чат тёплый, потому что я держу его тёплым. Мне такого никогда не говорили. Это было нужнее, чем я думала.»")
t('"It said the group\'s vibe was 64% banter, 18% logistics, 12% philosophy at 1AM, and 6% feelings. We accept this verdict. We will not change it."',
  "« Elle a dit que la vibe du groupe était 64% taquineries, 18% logistique, 12% philosophie à 1h du matin, et 6% sentiments. On accepte ce verdict. On ne changera pas. »",
  "«Dijo que la onda del grupo era 64% bromas, 18% logística, 12% filosofía a la 1 de la madrugada, y 6% sentimientos. Aceptamos el veredicto. No vamos a cambiarlo.»",
  "«Сказала, что вайб группы — 64% подколок, 18% логистики, 12% философии в час ночи и 6% чувств. Принимаем вердикт. Менять не будем.»")
t('"My mother-in-law got \'The Group Mum\' for our family chat. She has framed it. I am not joking."',
  "« Ma belle-mère a eu « La Mère du Groupe » pour notre chat familial. Elle l'a encadré. Je ne plaisante pas. »",
  "«Mi suegra se llevó \"La Madre del Grupo\" para nuestro chat familiar. Lo ha enmarcado. No es broma.»",
  "«Моя свекровь получила «Мама Группы» в нашем семейном чате. Она это вставила в рамку. Я не шучу.»")


# Missed testimonial — the iconic anxious-leaning quote
t('"It told me he was anxious-leaning and I\'d been chasing his ambivalence for nine months. Then it quoted three of his messages back at me to prove it. I closed the app and called my therapist."',
  "« Elle m'a dit qu'il était plutôt anxieux et que je courais après son ambivalence depuis neuf mois. Puis elle m'a renvoyé trois de ses messages pour le prouver. J'ai fermé l'app et appelé ma thérapeute. »",
  "«Me dijo que él tendía a la ansiedad y que llevaba nueve meses persiguiendo su ambivalencia. Luego me citó tres de sus mensajes para probarlo. Cerré la app y llamé a mi terapeuta.»",
  "«Оно сказало мне, что он склонен к тревожной привязанности, и я девять месяцев гонюсь за его амбивалентностью. Потом процитировало мне три его сообщения в доказательство. Я закрыла приложение и позвонила терапевту.»")


# Chat-mock dialogue (Group Lens page — Pia/Marta/Sara/Léa/Yara/Camille)
t('URGENT important question, are we doing the bachelorette in Lisbon or in my parents\' garden — I will accept both. Decide quickly. I am buying flights at midnight regardless.',
  "URGENT question importante, on fait l'EVJF à Lisbonne ou dans le jardin de mes parents — je prends les deux. Décidez vite. Je réserve les vols à minuit dans tous les cas.",
  "URGENTE pregunta importante, ¿hacemos la despedida en Lisboa o en el jardín de mis padres? — acepto las dos. Decidid rápido. Compro los vuelos a medianoche pase lo que pase.",
  "СРОЧНО важный вопрос, делаем девичник в Лиссабоне или в саду у моих родителей — принимаю оба варианта. Решайте быстро. Я бронирую билеты в полночь в любом случае.")
t('i made a spreadsheet, link below. tab 1 is options. tab 2 is costs by person. tab 3 is dietary. please look before you reply 🙏',
  "j'ai fait un tableur, lien en bas. onglet 1 les options. onglet 2 les coûts par personne. onglet 3 les régimes. regardez avant de répondre svp 🙏",
  "hice un excel, link abajo. pestaña 1 las opciones. pestaña 2 los costes por persona. pestaña 3 las dietas. mirad antes de responder porfa 🙏",
  "сделала табличку, ссылка снизу. вкладка 1 варианты. вкладка 2 расходы на человека. вкладка 3 диеты. посмотрите прежде чем ответить пожалуйста 🙏")
t('I love you all so much and I want to cry. Whatever you decide is perfect. Truly. 💕',
  "Je vous aime tellement les filles, j'ai envie de pleurer. Tout ce que vous décidez est parfait. Sincèrement. 💕",
  "Os quiero muchísimo y me dan ganas de llorar. Lo que decidáis es perfecto. De verdad. 💕",
  "Я вас всех так люблю, хочется плакать. Что бы вы ни решили — идеально. Правда. 💕")
t('Lisbon obviously. We are not throwing your bachelorette in a garden in Marseille. I will not allow it. ❤️',
  "Lisbonne évidemment. On ne fait pas ton EVJF dans un jardin à Marseille. Je ne permettrai pas. ❤️",
  "Lisboa obviamente. No vamos a hacer tu despedida en un jardín en Marsella. No lo voy a permitir. ❤️",
  "Лиссабон конечно. Мы не делаем твой девичник в саду в Марселе. Я этого не допущу. ❤️")
t('do the rest of you ever consider that we have jobs and i cannot answer at 10:47 PM on a Wednesday',
  "vous arrive-t-il de vous rappeler qu'on a un travail et que je ne peux pas répondre à 22h47 un mercredi",
  "¿se os ha ocurrido alguna vez que tenemos trabajo y que no puedo responder a las 22:47 un miércoles?",
  "вы вообще иногда вспоминаете, что у нас есть работа и я не могу отвечать в 22:47 в среду")
t('Yara baby answer when you can but the flights wait for no woman.',
  "Yara ma belle réponds quand tu peux mais les vols n'attendent personne.",
  "Yara cariño responde cuando puedas pero los vuelos no esperan a nadie.",
  "Яра милая отвечай когда сможешь, но рейсы никого не ждут.")
t('just catching up. yes lisbon. yes spreadsheet. yes sara we love you. yes pia please don\'t book flights tonight. i\'m going to bed.',
  "je rattrape. oui lisbonne. oui le tableur. oui sara on t'aime. oui pia stp ne réserve pas les vols ce soir. je vais me coucher.",
  "poniéndome al día. sí lisboa. sí excel. sí sara te queremos. sí pia por favor no reserves vuelos esta noche. me voy a dormir.",
  "догоняю. да, лиссабон. да, табличка. да, сара мы тебя любим. да, пия пожалуйста не бронируй сегодня. иду спать.")

# Chat mock framing
t('Group chat: "Sara\'s August Wedding 💒"',
  "Groupe : « Mariage de Sara, août 💒 »",
  "Chat de grupo: «Boda de Sara, agosto 💒»",
  "Группа: «Свадьба Сары, август 💒»")
t('7 members · Wednesday evening · slice of one thread',
  "7 membres · mercredi soir · extrait d'un fil",
  "7 miembros · miércoles por la noche · extracto de un hilo",
  "7 участников · среда вечером · фрагмент одной переписки")

# Cast of Characters bodies (these are descriptive paragraphs about each character)
t('Drives the chat at full speed and is, somehow, almost always right. Decisions get made because she refuses to let them sit. Has typed "I am buying flights at midnight" at least three times this year.',
  "Mène le chat à pleine vitesse et a, on ne sait comment, presque toujours raison. Les décisions se prennent parce qu'elle refuse de les laisser traîner. A déjà écrit « je réserve les vols à minuit » au moins trois fois cette année.",
  "Lleva el chat a toda velocidad y, no se sabe cómo, casi siempre tiene razón. Las decisiones se toman porque se niega a dejarlas dormir. Ha escrito «compro vuelos a medianoche» al menos tres veces este año.",
  "Гонит чат на полной скорости и почему-то почти всегда права. Решения принимаются, потому что она не даёт им зависнуть. Минимум три раза в этом году писала «я бронирую билеты в полночь».")
t('The reason this group has not yet missed a flight. Translates feelings into spreadsheets. Will gently re-share the link if you didn\'t read it the first time.',
  "La raison pour laquelle ce groupe n'a pas encore raté un vol. Traduit les émotions en tableurs. Re-partagera gentiment le lien si tu ne l'as pas lu la première fois.",
  "El motivo por el que este grupo aún no ha perdido ningún vuelo. Traduce sentimientos en hojas de cálculo. Reenvía el link amablemente si no lo leíste la primera vez.",
  "Причина, по которой эта группа ещё ни разу не пропустила рейс. Переводит чувства в таблицы. Вежливо пришлёт ссылку ещё раз, если ты не прочитала с первого раза.")
t('The emotional centre. Says "I love you" in the chat more than the rest of the group combined. Cries with affection.',
  "Le centre émotionnel. Dit « je vous aime » dans le chat plus que tout le reste du groupe réuni. Pleure d'affection.",
  "El centro emocional. Dice «os quiero» en el chat más que todo el resto del grupo junto. Llora de cariño.",
  "Эмоциональный центр. Говорит «я вас люблю» в чате чаще, чем весь остальной чат вместе. Плачет от нежности.")
t('Comes in late, ends the debate in one line. Soft on people, hard on bad ideas. Has veto power and uses it sparingly.',
  "Arrive tard, met fin au débat en une phrase. Douce avec les gens, ferme avec les mauvaises idées. A un droit de veto qu'elle utilise avec parcimonie.",
  "Llega tarde, termina el debate en una línea. Suave con la gente, dura con las malas ideas. Tiene poder de veto y lo usa con cuentagotas.",
  "Приходит поздно, заканчивает спор одной строкой. Мягка с людьми, тверда с плохими идеями. Имеет право вето и пользуется им экономно.")
t('The one who remembers that the rest of you have jobs. The grounding wire. Annoyed and beloved in equal measure.',
  "Celle qui se souvient que les autres ont un travail. Le fil à la terre. Agacée et adorée à parts égales.",
  "La que recuerda que el resto tenéis trabajo. El cable a tierra. Igualmente irritada y querida.",
  "Та, кто помнит, что у остальных есть работа. Заземляющий провод. Раздражена и обожаема в равной мере.")
t('Reads 200 messages at 11 PM and replies with one perfectly compressed summary. Always agrees with the right person.',
  "Lit 200 messages à 23 h et répond par un résumé parfaitement condensé. Donne toujours raison à la bonne personne.",
  "Lee 200 mensajes a las 11 de la noche y responde con un resumen perfectamente comprimido. Siempre le da la razón a la persona correcta.",
  "Читает 200 сообщений в 11 вечера и отвечает одним идеально сжатым резюме. Всегда соглашается с правильным человеком.")

# Cast of Characters titles
t('Pia · The Chaos Agent', "Pia · L'Agente du Chaos", "Pia · La Agente del Caos", "Пия · Агент Хаоса")
t('Marta · The Logistician', "Marta · La Logisticienne", "Marta · La Logística", "Марта · Логист")
t('Sara · The Heart', "Sara · Le Cœur", "Sara · El Corazón", "Сара · Сердце")
t('Léa · The Closer', "Léa · La Décideuse", "Léa · La Cerradora", "Леа · Закрывающая")
t('Yara · The Realist', "Yara · La Réaliste", "Yara · La Realista", "Яра · Реалистка")
t('Camille · The Catch-Up Queen', "Camille · La Reine du Rattrapage", "Camille · La Reina del Catch-Up", "Камиль · Королева Догоняния")

# Awards Ceremony award labels (from sample reading)
t('Most Likely to Send Voice Memos at 1 AM',
  "La plus susceptible d'envoyer des vocaux à 1 h du matin",
  "Más probable de mandar audios a la 1 de la madrugada",
  "Самая вероятная отправить голосовые в час ночи")
t('The Person Who Owns The Spreadsheet',
  "La Personne Qui Gère le Tableur",
  "La Persona que Lleva el Excel",
  "Хранитель Таблицы")
t('Most "I Love You All So Much" Per Capita',
  "Le plus de « je vous aime tellement » par personne",
  "Más «os quiero un montón» per cápita",
  "Больше всех «я вас обожаю» на человека")
t('Quietest Loyalty', "Loyauté la plus silencieuse", "Lealtad más silenciosa", "Самая тихая преданность")
t('Best Recap In Under 30 Words',
  "Meilleur résumé en moins de 30 mots",
  "Mejor resumen en menos de 30 palabras",
  "Лучший пересказ менее чем в 30 словах")
t('The Vibe Architect', "L'Architecte de la Vibe", "El Arquitecto de la Onda", "Архитектор Вайба")
t('Most Likely to Disagree And Be Right',
  "La plus susceptible d'être en désaccord et d'avoir raison",
  "Más probable de discrepar y tener razón",
  "Самая вероятная не согласиться и оказаться правой")

# Friendship archetypes line (the "One named pair for both of you" string)
t('One named pair for both of you — "The Ride-or-Die", "The Wise Counsel", "The Anchor & The Spark", "The Old-Friend Cadence", and others.',
  "Une paire nommée pour vous deux — « Les Inséparables », « La Conseillère Sage », « L'Ancre et l'Étincelle », « La Cadence du Vieil Ami », et d'autres.",
  "Una pareja nombrada para las dos — «Hasta-la-Muerte», «La Consejera Sabia», «El Ancla y la Chispa», «La Cadencia del Viejo Amigo», y otras.",
  "Названная пара для вас двоих — «До-Конца», «Мудрый Советник», «Якорь и Искра», «Каденция Старого Друга», и другие.")


# Awards Ceremony "because" descriptions (italic text under each award)
t('"Awarded for 19 voice memos after midnight in the last 30 days, with a 100% delivery rate and a 0% reply rate. Persistence pays."',
  "« Décerné pour 19 vocaux après minuit ces 30 derniers jours, avec 100 % de livraison et 0 % de réponse. La persistance paie. »",
  "«Otorgado por 19 audios después de medianoche en los últimos 30 días, con un 100 % de entrega y un 0 % de respuesta. La persistencia paga.»",
  "«Вручается за 19 голосовых после полуночи за последние 30 дней, со 100% доставкой и 0% ответов. Настойчивость окупается.»")
t('"For making three tabs we didn\'t ask for and one we genuinely needed. Logistics is love."',
  "« Pour avoir fait trois onglets qu'on n'avait pas demandés et un dont on avait vraiment besoin. La logistique, c'est l'amour. »",
  "«Por hacer tres pestañas que no pedimos y una que realmente necesitábamos. La logística es amor.»",
  "«За три вкладки, которых мы не просили, и одну, которая нам реально была нужна. Логистика — это любовь.»")
t('"Said it 14 times this month, meant it 14 times. The chat is warm because she keeps it warm."',
  "« Dit 14 fois ce mois-ci, pensé 14 fois. Le chat est chaleureux parce qu'elle le maintient chaleureux. »",
  "«Lo dijo 14 veces este mes, lo sintió 14 veces. El chat es cálido porque ella lo mantiene cálido.»",
  "«Сказала 14 раз в этом месяце, и каждый раз искренне. Чат тёплый, потому что она держит его тёплым.»")
t('"For ending the bachelorette debate with \'Lisbon obviously.\' Decisions move when she arrives."',
  "« Pour avoir mis fin au débat de l'EVJF avec « Lisbonne évidemment. » Les décisions avancent quand elle arrive. »",
  "«Por terminar el debate de la despedida con \"Lisboa obviamente\". Las decisiones avanzan cuando ella llega.»",
  "«За завершение спора о девичнике словами «Лиссабон конечно». Решения двигаются, когда она появляется.»")
t('"For being the lowest-volume member of this chat and the first one to call when someone has news. The opposite of attention is sometimes the deepest kind of love."',
  "« Pour être la membre la plus discrète de ce chat et la première à appeler quand quelqu'un a une nouvelle. Le contraire de l'attention est parfois la forme la plus profonde de l'amour. »",
  "«Por ser la miembro de menor volumen de este chat y la primera en llamar cuando alguien tiene noticias. Lo contrario de la atención es a veces la forma más profunda de amor.»",
  "«За то, что она самый тихий участник этого чата и первая, кто звонит, когда у кого-то новости. Противоположность вниманию — иногда самая глубокая форма любви.»")
t('"For consistently catching up on 200 messages in one sentence. The newsroom would hire her."',
  "« Pour résumer systématiquement 200 messages en une seule phrase. Une rédaction l'engagerait. »",
  "«Por ponerse al día sistemáticamente con 200 mensajes en una frase. Una redacción la contrataría.»",
  "«За способность стабильно пересказывать 200 сообщений в одном предложении. Любая редакция её бы взяла.»")
t('"For setting the emotional weather. When the chat feels safe, this is who is making it feel safe."',
  "« Pour définir la météo émotionnelle. Quand le chat semble sûr, c'est elle qui le rend sûr. »",
  "«Por marcar el clima emocional. Cuando el chat se siente seguro, es ella quien lo hace sentir seguro.»",
  "«За задание эмоциональной погоды. Когда в чате безопасно, это она делает его безопасным.»")
t('"For pushing back exactly twice this month and being correct exactly twice. The hit rate is suspicious."',
  "« Pour avoir contesté exactement deux fois ce mois-ci et avoir eu raison exactement deux fois. Le taux de réussite est suspect. »",
  "«Por discrepar exactamente dos veces este mes y tener razón exactamente dos veces. La tasa de acierto es sospechosa.»",
  "«За ровно два возражения в этом месяце и ровно два попадания. Процент попаданий подозрительный.»")

# Footer "Guides for this lens" → bonus translations missed
t('Group Lens generates a unique award for every member of the chat — these are six of eight, from one sample reading.',
  "La lentille Groupe génère un prix unique pour chaque membre du chat — voici six sur huit, tirés d'une lecture exemple.",
  "La lente Grupo genera un premio único para cada miembro del chat — estos son seis de ocho, de una lectura de ejemplo.",
  "Линза Группа создаёт уникальную награду для каждого участника чата — это шесть из восьми, из примера портрета.")
# ============================================================
# Build logic — same as v1 with extension
# ============================================================
SORTED_KEYS = sorted(T.keys(), key=len, reverse=True)

def translate_html(html, lang):
    out = html
    out = out.replace('<html lang="en">', f'<html lang="{lang}">')
    out = re.sub(r'href="assets/', 'href="/assets/', out)
    out = re.sub(r'src="assets/', 'src="/assets/', out)
    out = re.sub(r'href="style\.css"', 'href="/style.css"', out)
    out = re.sub(r'<a class="brand" href="/"', f'<a class="brand" href="/{lang}/"', out)
    flag_labels = {"en": "English", "fr": "Français", "es": "Español", "ru": "Русский"}
    flag_html = ['<div class="lang-picker">']
    for f in ["en", "fr", "es", "ru"]:
        if f == lang:
            flag_html.append(f'<span class="lang-flag flag-{f} active" aria-label="{flag_labels[f]}"></span>')
        else:
            href = "/" if f == "en" else f"/{f}/"
            flag_html.append(f'<a class="lang-flag flag-{f}" href="{href}" aria-label="{flag_labels[f]}"></a>')
    flag_html.append('</div>')
    new_picker = "".join(flag_html)
    out = re.sub(r'<div class="lang-picker">.*?</div>',
                 lambda m: new_picker, out, count=1, flags=re.DOTALL)
    for en in SORTED_KEYS:
        target = T[en].get(lang)
        if target and en in out:
            out = out.replace(en, target)
    return out


def build_for_lang(lang):
    dst = ROOT / lang
    dst.mkdir(exist_ok=True)
    pages = [
        "index.html", "lens-self.html", "lens-romantic.html", "lens-friendship.html",
        "lens-professional.html", "lens-family.html", "lens-group.html",
        "pricing.html", "privacy.html", "terms.html", "testimonials.html", "science.html",
    ]
    for p in pages:
        src_file = ROOT / p
        if not src_file.exists():
            continue
        html = src_file.read_text(encoding="utf-8")
        translated = translate_html(html, lang)
        (dst / p).write_text(translated, encoding="utf-8")
        print(f"  [{lang}] {p}  {len(translated)} bytes")


if __name__ == "__main__":
    for lang in LANGS:
        print(f"\n=== Building {lang.upper()} ===")
        build_for_lang(lang)
    print(f"\nDone. Total translation entries: {len(T)}")
