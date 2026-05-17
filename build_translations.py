#!/usr/bin/env python3
"""
Build full French, Spanish, and Russian translations of the Persona Lens website.
Reads English source files, applies translations + path adjustments, writes to fr/, es/, ru/.
"""
import os
import re
import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
LANGS = ["fr", "es", "ru"]

# Shared UI strings — translated for header, footer, nav, buttons
UI = {
    "fr": {
        "brand_link_home": "/fr/",
        "get_app": "Télécharger",
        "lenses": "Les lentilles",
        "how": "Comment ça marche",
        "science": "Science",
        "testimonials": "Témoignages",
        "pricing": "Tarifs",
        "privacy_nav": "Confidentialité",
        "footer_lenses": "Les lentilles",
        "footer_product": "Produit",
        "footer_legal": "Légal",
        "self": "Soi",
        "romantic": "Romantique",
        "friendship": "Amitié",
        "professional": "Professionnel",
        "family": "Famille",
        "group": "Groupe",
        "how_it_works": "Comment ça marche",
        "privacy_policy": "Politique de confidentialité",
        "terms_of_use": "Conditions d'utilisation",
        "footer_tag": "Chaque message révèle qui vous êtes.<br/>Six lentilles. 61 modules. Construit en privé pour iPhone.",
        "footer_copyright": "© 2026 Persona Lens. Fait avec soin, pour aider.",
        "footer_disclaimer": "Aperçus IA, pas un diagnostic.",
        "the_science": "La science",
        "privacy_approach": "Approche de confidentialité",
        "download_app_store": "Télécharger sur l'App Store",
        "back_to_home": "← Retour à l'accueil",
    },
    "es": {
        "brand_link_home": "/es/",
        "get_app": "Descargar",
        "lenses": "Las lentes",
        "how": "Cómo funciona",
        "science": "Ciencia",
        "testimonials": "Testimonios",
        "pricing": "Precios",
        "privacy_nav": "Privacidad",
        "footer_lenses": "Las lentes",
        "footer_product": "Producto",
        "footer_legal": "Legal",
        "self": "Yo",
        "romantic": "Romántica",
        "friendship": "Amistad",
        "professional": "Profesional",
        "family": "Familia",
        "group": "Grupo",
        "how_it_works": "Cómo funciona",
        "privacy_policy": "Política de privacidad",
        "terms_of_use": "Condiciones de uso",
        "footer_tag": "Cada mensaje revela quién eres.<br/>Seis lentes. 61 módulos. Construido en privado para iPhone.",
        "footer_copyright": "© 2026 Persona Lens. Hecho con cuidado, para ayudar.",
        "footer_disclaimer": "Información generada por IA, no un diagnóstico.",
        "the_science": "La ciencia",
        "privacy_approach": "Enfoque de privacidad",
        "download_app_store": "Descargar en el App Store",
        "back_to_home": "← Volver al inicio",
    },
    "ru": {
        "brand_link_home": "/ru/",
        "get_app": "Скачать",
        "lenses": "Линзы",
        "how": "Как это работает",
        "science": "Наука",
        "testimonials": "Отзывы",
        "pricing": "Цены",
        "privacy_nav": "Приватность",
        "footer_lenses": "Линзы",
        "footer_product": "Продукт",
        "footer_legal": "Юридическое",
        "self": "Я",
        "romantic": "Романтика",
        "friendship": "Дружба",
        "professional": "Работа",
        "family": "Семья",
        "group": "Группа",
        "how_it_works": "Как это работает",
        "privacy_policy": "Политика приватности",
        "terms_of_use": "Условия использования",
        "footer_tag": "Каждое сообщение раскрывает, кто вы.<br/>Шесть линз. 61 модуль. Создано приватно для iPhone.",
        "footer_copyright": "© 2026 Persona Lens. Сделано с заботой, чтобы помочь.",
        "footer_disclaimer": "Это инсайты от ИИ, а не диагноз.",
        "the_science": "Наука",
        "privacy_approach": "Подход к приватности",
        "download_app_store": "Скачать в App Store",
        "back_to_home": "← Вернуться на главную",
    },
}

# Lens-specific helper labels used on multiple pages
LENS_TARGETS = {
    "fr": {
        "self": "Analyse VOUS-MÊME",
        "romantic": "Analyse VOTRE PARTENAIRE &amp; VOTRE DYNAMIQUE AMOUREUSE",
        "friendship": "Analyse VOTRE AMI(E) &amp; LA DYNAMIQUE RELATIONNELLE",
        "professional": "Analyse VOTRE COLLÈGUE &amp; VOTRE DYNAMIQUE DE TRAVAIL",
        "family": "Analyse VOS RELATIONS FAMILIALES",
        "group": "Analyse TOUT LE GROUPE",
    },
    "es": {
        "self": "Analiza A TI MISMO",
        "romantic": "Analiza A TU PAREJA Y VUESTRA DINÁMICA AMOROSA",
        "friendship": "Analiza A TU AMIGO/A Y LA DINÁMICA DE LA RELACIÓN",
        "professional": "Analiza A TU COLEGA Y VUESTRA DINÁMICA DE TRABAJO",
        "family": "Analiza TUS RELACIONES FAMILIARES",
        "group": "Analiza A TODO EL GRUPO",
    },
    "ru": {
        "self": "Анализирует ВАС САМИХ",
        "romantic": "Анализирует ВАШЕГО ПАРТНЁРА и ВАШУ РОМАНТИЧЕСКУЮ ДИНАМИКУ",
        "friendship": "Анализирует ВАШЕГО ДРУГА и ДИНАМИКУ ОТНОШЕНИЙ",
        "professional": "Анализирует ВАШЕГО КОЛЛЕГУ и РАБОЧУЮ ДИНАМИКУ",
        "family": "Анализирует ВАШИ СЕМЕЙНЫЕ ОТНОШЕНИЯ",
        "group": "Анализирует ВСЮ ГРУППУ",
    },
}


# ============================================================
# Translation map: English source string → {fr, es, ru} target
# ============================================================
T = {}

def t(en, fr, es, ru):
    T[en] = {"fr": fr, "es": es, "ru": ru}

# Common headings / button labels / phrases (shared across pages)
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

# Lens target labels (the small uppercase labels above each lens name)
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

# Hero copy
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
t("For iPhone · iOS 17+",
  "Pour iPhone · iOS 17+",
  "Para iPhone · iOS 17+",
  "Для iPhone · iOS 17+")
t("Every message<br/>reveals who you are.",
  "Chaque message<br/>révèle qui vous êtes.",
  "Cada mensaje<br/>revela quién eres.",
  "Каждое сообщение<br/>раскрывает, кто вы.")
t("Persona Lens reads the conversations you already have — on WhatsApp, on Telegram, or pasted from anywhere — and gives you a beautifully designed personality reading through six different lenses on your life.",
  "Persona Lens lit les conversations que vous avez déjà — sur WhatsApp, sur Telegram, ou collées depuis n'importe où — et vous offre un portrait psychologique magnifiquement conçu, à travers six lentilles différentes de votre vie.",
  "Persona Lens lee las conversaciones que ya tienes — en WhatsApp, en Telegram, o pegadas desde cualquier lugar — y te entrega un retrato psicológico bellamente diseñado, a través de seis lentes diferentes sobre tu vida.",
  "Persona Lens читает переписки, которые у вас уже есть — в WhatsApp, в Telegram, или вставленные откуда угодно — и выдаёт красиво оформленный психологический портрет через шесть разных линз на вашу жизнь.")
t("See how it works",
  "Voir comment ça marche",
  "Ver cómo funciona",
  "Посмотреть, как это работает")
t("First analysis free · No account required · Reports stay encrypted on your iPhone",
  "Première analyse gratuite · Aucun compte requis · Les rapports restent chiffrés sur votre iPhone",
  "Primer análisis gratis · No requiere cuenta · Los reportes quedan cifrados en tu iPhone",
  "Первый анализ бесплатно · Аккаунт не нужен · Отчёты остаются зашифрованными на вашем iPhone")
t("Persona Card · Romantic Lens",
  "Carte Persona · Lentille Romantique",
  "Tarjeta Persona · Lente Romántica",
  "Карта Персоны · Линза Романтика")
t("The Devoted Strategist",
  "Le Stratège Dévoué",
  "El Estratega Devoto",
  "Преданный Стратег")
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

# Lens section
t("Six Lenses · 61 Modules",
  "Six lentilles · 61 modules",
  "Seis lentes · 61 módulos",
  "Шесть линз · 61 модуль")
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

# HOW IT WORKS
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

# SAMPLE
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

# Testimonials preview
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
t('"It told me he was anxious-leaning and I\'d been chasing his ambivalence for nine months. Then it quoted three of his messages back at me to prove it. I closed the app and called my therapist."',
  "« Il m'a dit qu'il était plutôt anxieux et que je courais après son ambivalence depuis neuf mois. Puis il m'a renvoyé trois de ses messages pour le prouver. J'ai fermé l'app et appelé ma thérapeute. »",
  "«Me dijo que él tendía a la ansiedad y que yo llevaba nueve meses persiguiendo su ambivalencia. Luego me citó tres de sus mensajes para probarlo. Cerré la app y llamé a mi terapeuta».",
  "«Он сказал, что он склонен к тревожной привязанности, а я девять месяцев гонюсь за его амбивалентностью. Потом процитировал мне три его сообщения в доказательство. Я закрыла приложение и позвонила терапевту.»")
t('"Ran it on our bridesmaid chat. The Awards Ceremony nailed every one of us. Pia got \'Most Likely to Send Voice Memos at 1AM\' and the entire group lost it. We screenshotted the whole thing."',
  "« Lancé sur le chat de mes demoiselles d'honneur. La Cérémonie des Prix a clouée chacune de nous. Pia a eu « La plus susceptible d'envoyer des vocaux à 1h du matin » et tout le groupe a éclaté. On a tout capturé en screenshot. »",
  "«Lo corrí en el chat de mis damas de honor. La Ceremonia de Premios clavó a cada una. Pia se llevó \"Más probable de mandar audios a la 1 de la madrugada\" y el grupo entero se rió a carcajadas. Hicimos screenshot de todo».",
  "«Запустила на чате подружек невесты. Церемония Наград прибила каждую из нас. Пия получила «Самая вероятная отправить голосовые в час ночи», и вся группа повалилась со смеху. Мы заскринили всё.»")
t('"Communication Archaeology pulled out a phrase my mother says — \'don\'t make me ask twice\' — and showed me I now text it to my brother. I sat with that for an hour."',
  "« L'Archéologie de la Communication a sorti une phrase que dit ma mère — « ne me fais pas demander deux fois » — et m'a montré que je la textote maintenant à mon frère. Je suis restée avec ça pendant une heure. »",
  "«Arqueología de la Comunicación sacó una frase que dice mi madre — \"no me hagas preguntarlo dos veces\" — y me mostró que ahora se la mando a mi hermano por mensaje. Me quedé con eso una hora».",
  "«Археология Коммуникации вытащила фразу, которую говорит моя мама — «не заставляй меня спрашивать дважды» — и показала, что я теперь пишу её брату. Я просидела с этим час.»")
t("Lyon · 28", "Lyon · 28 ans", "Lyon · 28", "Лион · 28")
t("Madrid · 31", "Madrid · 31 ans", "Madrid · 31", "Мадрид · 31")
t("Tbilisi · 34", "Tbilissi · 34 ans", "Tiflis · 34", "Тбилиси · 34")
t("Read more reactions →", "Lire plus de réactions →", "Leer más reacciones →", "Читать больше отзывов →")

# PRIVACY block
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

# Pricing preview
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

# DOWNLOAD
t("Read yourself, gently.", "Lisez-vous, doucement.", "Léete a ti mismo, con suavidad.", "Прочтите себя — мягко.")
t("Persona Lens is built for iPhone. Drop in a chat, choose a lens, get a portrait of who you are right now.",
  "Persona Lens est conçu pour iPhone. Déposez un chat, choisissez une lentille, recevez un portrait de qui vous êtes maintenant.",
  "Persona Lens está hecho para iPhone. Suelta un chat, elige una lente, recibe un retrato de quién eres ahora.",
  "Persona Lens создан для iPhone. Закиньте чат, выберите линзу, получите портрет того, кто вы прямо сейчас.")
t("Available now on the App Store · iPhone, iOS 17+.",
  "Disponible maintenant sur l'App Store · iPhone, iOS 17+.",
  "Disponible ya en el App Store · iPhone, iOS 17+.",
  "Уже доступно в App Store · iPhone, iOS 17+.")

# Subtitle: pricing dollar value (the price-amount $8.33/month)
t("$8.33", "8,33 $", "8,33 $", "$8.33")
t("/month", "/mois", "/mes", "/мес")

print("Translation map size:", len(T), "entries")


# ============================================================
# Build logic
# ============================================================

# Sort translation keys by length descending — longer strings get replaced first,
# so substring matches don't clobber larger phrases.
SORTED_KEYS = sorted(T.keys(), key=len, reverse=True)


def translate_html(html: str, lang: str) -> str:
    """Apply all translations + path adjustments + language picker update for `lang`."""
    out = html

    # 1. <html lang="en"> → <html lang="fr|es|ru">
    out = out.replace('<html lang="en">', f'<html lang="{lang}">')

    # 2. Path adjustments (relative → absolute /)
    out = re.sub(r'href="assets/', 'href="/assets/', out)
    out = re.sub(r'src="assets/', 'src="/assets/', out)
    out = re.sub(r'href="style\.css"', 'href="/style.css"', out)

    # 3. Brand link → /lang/
    out = re.sub(r'<a class="brand" href="/"', f'<a class="brand" href="/{lang}/"', out)

    # 4. Language picker: rebuild it cleanly
    flags = ["en", "fr", "es", "ru"]
    flag_labels = {"en": "English", "fr": "Français", "es": "Español", "ru": "Русский"}
    flag_html = ['<div class="lang-picker">']
    for f in flags:
        if f == lang:
            flag_html.append(f'<span class="lang-flag flag-{f} active" aria-label="{flag_labels[f]}"></span>')
        else:
            href = "/" if f == "en" else f"/{f}/"
            flag_html.append(f'<a class="lang-flag flag-{f}" href="{href}" aria-label="{flag_labels[f]}"></a>')
    flag_html.append('</div>')
    new_picker = "".join(flag_html)
    # Replace the entire lang-picker block
    out = re.sub(
        r'<div class="lang-picker">.*?</div>',
        lambda m: new_picker,
        out,
        count=1,
        flags=re.DOTALL,
    )

    # 5. Apply translation dictionary (longest keys first)
    for en in SORTED_KEYS:
        target = T[en].get(lang)
        if not target:
            continue
        if en in out:
            out = out.replace(en, target)

    return out


def build_for_lang(lang: str):
    src_dir = ROOT
    dst_dir = ROOT / lang
    dst_dir.mkdir(exist_ok=True)
    pages = [
        "index.html",
        "lens-self.html",
        "lens-romantic.html",
        "lens-friendship.html",
        "lens-professional.html",
        "lens-family.html",
        "lens-group.html",
        "pricing.html",
        "privacy.html",
        "terms.html",
        "testimonials.html",
        "science.html",
    ]
    for page in pages:
        src = src_dir / page
        if not src.exists():
            print(f"  skip missing {page}")
            continue
        html = src.read_text(encoding="utf-8")
        translated = translate_html(html, lang)
        dst = dst_dir / page
        dst.write_text(translated, encoding="utf-8")
        print(f"  [{lang}] wrote {page} ({len(translated)} bytes)")


if __name__ == "__main__":
    for lang in LANGS:
        print(f"\n=== Building {lang.upper()} ===")
        build_for_lang(lang)
    print("\nDone.")
