"""Famiglia Vicino 포트폴리오 화면 v2 (2026-11-11, 사용자 결정: 시안 A+B 섞은 판 "이대로 올려봐").
연주회 프로그램북 구성 + 진짜 악보 같은 총보(famiglia_score.py). 음원은 사이트에 안 올림(대표님 2026-11-11), _draft/audio 에만 있음.
문구 대부분은 famiglia.T(8개 언어)를 그대로 쓰고, 새로 생긴 문구만 아래 NEW 에 둔다.
옛 화면(famiglia.body)은 famiglia.py 에 그대로 남아 있다(되돌릴 때 build.py 한 줄)."""
import famiglia as F
import famiglia_score as FS

ROWS = ["welegato", "leggii", "chiave", "appoggio", "squillo", "pianino", "prova"]
TEMPO = {"find": "Andante", "prepare": "Moderato", "warmup": "Adagio", "practise": "Allegro", "reflect": "Tranquillo"}
STAGE_APPS = {"find": ["welegato"], "prepare": ["leggii", "chiave"], "warmup": ["appoggio", "squillo"], "practise": ["pianino"], "reflect": ["prova"]}
PROG = [("Prima parte", ["find", "prepare"]), ("Intervallo", ["warmup"]),
        ("Seconda parte", ["practise", "reflect"])]

NEW = {
    "ko": dict(subt="음악가의 일주일을 위한 일곱 곡", part="총보", score_h="일곱 개의 성부, 하나의 음악.",
               intro="총보에서 악기마다 자기 줄이 있듯, 앱마다 맡은 마디가 있어요. 마디마다 주인공이 바뀌고, 다른 앱들은 곁에서 받쳐 줘요.",
               hint="와인색 음표가 그 마디의 주인공이에요.", swipe="옆으로 밀어서 보세요.", listen="들어 보기", pause="멈추기",
               sub="교향곡 9번 4악장 「환희의 송가」 · 일곱 개의 앱을 위한 편곡", stages=["찾기", "준비하기", "몸 풀기", "연습하기", "돌아보기"],
               dc="다시 처음으로 — 다음 레슨", label="베토벤 「환희의 송가」 총보: 여덟 마디 동안 일곱 개의 앱이 차례로 주제를 이어받아요",
               notes="프로그램 노트", parts=["1부 · 찾고, 준비하고", "쉬는 시간 · 숨 고르기", "2부 · 연습하고, 돌아보고"],
               when=["찾는 날", "악보를 펼치는 밤", "내 키가 아닐 때", "숨부터", "목을 깨우는 아침", "피아노 없는 방에서", "레슨이 끝난 뒤"],
               free="무료 입장"),
    "en": dict(subt="Seven pieces for a musician's week", part="Full score", score_h="Seven voices, one piece of music.",
               intro="Just as every instrument has its own line in a score, every app has its own bars. In each bar a different app takes the lead while the others accompany.",
               hint="Wine-red notes mark the lead in each bar.", swipe="Swipe sideways to see it all.", listen="Listen", pause="Pause",
               sub="Symphony No. 9, finale: “Ode to Joy” · arranged for seven apps", stages=["Find", "Prepare", "Warm up", "Practise", "Reflect"],
               dc="Da capo — on to the next lesson", label="Full score of Beethoven’s Ode to Joy: over eight bars the seven apps pass the theme from one to the next",
               notes="Programme notes", parts=["Part one · find and prepare", "Interval · catch your breath", "Part two · practise and reflect"],
               when=["the day you search", "the evening with your scores", "when the key is wrong", "breath first", "the morning warm-up",
                     "in a room without a piano", "after the lesson"],
               free="Free admission"),
    "de": dict(subt="Sieben Stücke für eine Musikerwoche", part="Partitur", score_h="Sieben Stimmen, eine Musik.",
               intro="Wie jedes Instrument in der Partitur seine eigene Zeile hat, hat jede App ihre eigenen Takte. In jedem Takt führt eine andere App, die anderen begleiten.",
               hint="Die weinroten Noten zeigen, wer im Takt führt.", swipe="Zum Ansehen seitlich wischen.", listen="Anhören", pause="Pause",
               sub="9. Sinfonie, Finale: „An die Freude“ · für sieben Apps gesetzt", stages=["Finden", "Vorbereiten", "Einsingen", "Üben", "Rückblick"],
               dc="Da capo — zur nächsten Stunde", label="Partitur von Famiglia Vicino: ein Stück in fünf Takten, in jedem Takt führt eine andere App",
               notes="Programmheft", parts=["Erster Teil · finden und vorbereiten", "Pause · durchatmen", "Zweiter Teil · üben und zurückblicken"],
               when=["der Tag der Suche", "der Abend über den Noten", "wenn die Tonart nicht passt", "zuerst der Atem", "das Einsingen am Morgen",
                     "im Raum ohne Klavier", "nach dem Unterricht"],
               free="Eintritt frei"),
    "it": dict(subt="Sette brani per la settimana di un musicista", part="", score_h="Sette voci, una sola musica.",
               intro="Come ogni strumento ha il suo rigo nella partitura, ogni app ha le sue battute. In ogni battuta un'app diversa guida, le altre accompagnano.",
               hint="Le note color vino indicano chi guida la battuta.", swipe="Scorri di lato per vederla tutta.", listen="Ascolta", pause="Pausa",
               sub="Sinfonia n. 9, finale: «Inno alla gioia» · per sette app", stages=["Trovare", "Preparare", "Riscaldarsi", "Studiare", "Riascoltare"],
               dc="Da capo — alla prossima lezione", label="Partitura di Famiglia Vicino: un brano di cinque battute in cui ogni battuta è guidata da un'app diversa",
               notes="", parts=["trovare e preparare", "riprendere fiato", "studiare e riascoltare"],
               when=["il giorno della ricerca", "la sera sugli spartiti", "quando la tonalità non va", "prima il respiro", "il vocalizzo del mattino",
                     "in una stanza senza pianoforte", "dopo la lezione"],
               free=""),
    "fr": dict(subt="Sept pièces pour la semaine d'un musicien", part="Conducteur", score_h="Sept voix, une seule musique.",
               intro="Comme chaque instrument a sa portée dans le conducteur, chaque app a ses mesures. À chaque mesure, une app différente mène et les autres accompagnent.",
               hint="Les notes lie-de-vin indiquent qui mène la mesure.", swipe="Faites défiler sur le côté.", listen="Écouter", pause="Pause",
               sub="Symphonie nº 9, finale : « Ode à la joie » · arrangée pour sept apps", stages=["Trouver", "Préparer", "Échauffement", "Travailler", "Réécouter"],
               dc="Da capo — vers la prochaine leçon", label="Conducteur de Famiglia Vicino : une pièce de cinq mesures où une app différente mène chaque mesure",
               notes="Notes de programme", parts=["Première partie · trouver et préparer", "Entracte · reprendre son souffle",
                                                  "Deuxième partie · travailler et réécouter"],
               when=["le jour où l'on cherche", "le soir sur les partitions", "quand la tonalité ne va pas", "d'abord le souffle",
                     "l'échauffement du matin", "dans une pièce sans piano", "après la leçon"],
               free="Entrée libre"),
    "zh": dict(subt="为音乐人一周而作的七首曲子", part="总谱", score_h="七个声部，一首音乐。",
               intro="就像总谱里每件乐器都有自己的一行，每个应用也有属于自己的小节。每一小节由不同的应用领奏，其他应用在旁伴奏。",
               hint="酒红色的音符是该小节的主角。", swipe="左右滑动查看。", listen="试听", pause="暂停",
               sub="第九交响曲终乐章《欢乐颂》· 为七个应用改编", stages=["寻找", "准备", "热身", "练习", "回顾"],
               dc="从头再来——下一堂课", label="Famiglia Vicino 总谱：五小节的乐曲，每一小节由不同的应用领奏",
               notes="节目说明", parts=["上半场 · 寻找与准备", "中场休息 · 调整呼吸", "下半场 · 练习与回顾"],
               when=["寻找的那天", "翻开乐谱的夜晚", "调不合适的时候", "先从呼吸开始", "清晨开嗓", "没有钢琴的房间里", "下课之后"],
               free="免费入场"),
    "es": dict(subt="Siete piezas para la semana de un músico", part="", score_h="Siete voces, una sola música.",
               intro="Como cada instrumento tiene su pentagrama en la partitura, cada app tiene sus compases. En cada compás lidera una app distinta y las demás acompañan.",
               hint="Las notas color vino marcan quién lleva la voz en cada compás.", swipe="Desliza hacia el lado para verla entera.",
               listen="Escuchar", pause="Pausa",
               sub="Sinfonía n.º 9, final: «Oda a la alegría» · arreglo para siete apps", stages=["Buscar", "Preparar", "Calentar", "Practicar", "Repasar"],
               dc="Da capo — a la próxima clase", label="Partitura de Famiglia Vicino: una pieza de cinco compases en la que cada compás lo lidera una app distinta",
               notes="Notas al programa", parts=["Primera parte · buscar y preparar", "Intermedio · tomar aire", "Segunda parte · practicar y repasar"],
               when=["el día de buscar", "la noche con las partituras", "cuando el tono no encaja", "primero la respiración",
                     "el calentamiento de la mañana", "en una sala sin piano", "después de la clase"],
               free="Entrada libre"),
    "ru": dict(subt="Семь пьес для недели музыканта", part="Партитура", score_h="Семь голосов — одна музыка.",
               intro="Как у каждого инструмента в партитуре своя строка, у каждого приложения свои такты. В каждом такте ведёт другое приложение, остальные аккомпанируют.",
               hint="Ноты винного цвета — ведущий голос такта.", swipe="Прокрутите вбок.", listen="Слушать", pause="Пауза",
               sub="Симфония № 9, финал: «Ода к радости» · переложение для семи приложений", stages=["Найти", "Подготовить", "Распеться", "Заниматься", "Разобрать"],
               dc="Da capo — к следующему уроку", label="Партитура Famiglia Vicino: пьеса из пяти тактов, в каждом такте ведёт другое приложение",
               notes="Аннотация", parts=["Первое отделение · найти и подготовить", "Антракт · перевести дух", "Второе отделение · заниматься и разбирать"],
               when=["день поиска", "вечер над нотами", "когда тональность не та", "сначала дыхание", "утренняя распевка",
                     "в комнате без рояля", "после урока"],
               free="Вход свободный"),
}


def _lab(lat, local):
    return f'<p class="lab">{lat}{" · " + local if local else ""}</p>'


def _links(k, t, lang):
    L = F.LINKS[k]; out = []
    info = F.I.welegato_url(lang) if L["info"] == "WELEGATO" else L["info"]
    ext = ' target="_blank" rel="noopener"'
    if info:
        out.append(f'<a href="{info}"{ext if info.startswith("http") else ""}>{t["info"]}</a>')
    if L["play"]:
        out.append(f'<a href="https://play.google.com/store/apps/details?id={L["play"]}&amp;hl={lang}"{ext}>Google Play</a>')
    if L["apple"]:
        out.append(f'<a href="{L["apple"].replace("{lang}", lang)}"{ext}>App Store</a>')
    return " · ".join(out) or f'<span class="soon">{t["soon"]}</span>'


def body(lang, soon_keys):
    t = F.T[lang]; n = NEW[lang]; N = t["names"]
    svg = FS.score_svg(N, n["stages"], n["sub"], n["dc"], n["label"])
    # 프로그램: 악장(빠르기말이 제목, 단계는 부제목, 물음·설명) + 오른쪽에 그 악장의 앱 아이콘 (시안 A 내용, 2026-11-11 사용자)
    def icon(k):
        L = F.LINKS[k]; info = F.I.welegato_url(lang) if L["info"] == "WELEGATO" else L["info"]
        href = info or (f"https://play.google.com/store/apps/details?id={L['play']}&amp;hl={lang}" if L["play"] else "")
        tgt = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        inner = f'<img src="/apps/{k}.png" alt="" loading="lazy"><figcaption>{N[k]}</figcaption>'
        return f'<a class="ic{" solo" if k == "welegato" else ""}" href="{href}"{tgt}>{inner}</a>' if href else f'<span class="ic">{inner}</span>'
    def mov(no, tempo, h, q, d, keys, tag=""):
        qq = f'<p class="q">{q}</p>' if q else ""
        return (f'<li class="mov"><span class="no">{no}</span><div class="mb"><p class="tm">{tempo}</p><h3>{h}{tag}</h3>{qq}'
                f'<p class="d">{d}</p></div><div class="ics">{"".join(icon(k) for k in keys)}</div></li>')
    prog, no = [], 0
    for (lat, stages), sub in zip(PROG, n["parts"]):
        prog.append(f'<li class="part"><span>{lat}</span><small>{sub}</small></li>')
        for st in stages:
            no += 1; h, q, d = t["stages"][st]
            tag = f'<span class="tag">{t["warmup_tag"]}</span>' if st == "warmup" else ""
            prog.append(mov(no, TEMPO[st], h, q, d, STAGE_APPS[st], tag))
    prog.append(mov("D.C.", "Ancora", t["loop_h"], "", t["loop"], ["welegato"]))
    ids = ("s", "t", "a")
    who = ("".join(f'<input type="radio" name="fv2r" id="fv2r-{r}"{" checked" if r == "s" else ""}>' for r in ids)
           + '<div class="tabs" role="tablist">' + "".join(f'<label for="fv2r-{r}">{nm}</label>' for r, nm in zip(ids, t["roles"])) + "</div>"
           + "".join(f'<ul class="p p-{r}">' + "".join(f'<li><img src="/apps/{k}.png" alt="" loading="lazy"><div><b>{N[k]}</b>'
                                                     f'<span>{t["scen"][k][i]}</span></div></li>' for k in ROWS) + "</ul>"
                     for i, r in enumerate(ids)))
    glue = "".join(f'<div><i>{"①②③"[i]}</i><b>{h}</b><span>{d}</span></div>' for i, (h, d) in enumerate(t["glue"]))
    fonts = "/fonts/fonts-v2.css" if lang in ("ko", "zh") else "/fonts/fonts-v2-latin.css"
    lead = t["lead"].replace('<br class="w">', " ")
    return f'''<link rel="stylesheet" href="{fonts}"><style>{CSS}</style><div class="fv2">
<div class="cover"><div class="frame"><p class="pre">Vicino Labs presenta</p><h1>Famiglia<br>Vicino</h1><div class="orn">❦</div>
<p class="subt">{n["subt"]}</p><p class="season">Stagione 2026 · Frankfurt — Seoul</p></div></div>
<section class="partitura">{_lab("Partitura", n["part"])}<h2>{n["score_h"]}</h2><p class="intro">{n["intro"]}</p>
<div class="sheet"><div class="scroll">{svg}</div></div>
<p class="hint"><span class="m">{n["swipe"]} </span>{n["hint"]}</p></section>
<section class="notes">{_lab("Note di sala", n["notes"])}<h2>{t["h1"]}</h2>
<p class="lead1"><span class="drop">{lead}</span></p></section>
<section class="prog">{_lab("Programma", "")}<ol>{"".join(prog)}</ol></section>
<section class="night"><p class="k">{t["quote_kicker"]}</p><blockquote>{t["quote"]}</blockquote>
<svg class="nslur" viewBox="0 0 600 60" aria-hidden="true"><path d="M10 50 Q 300 -20 590 50 Q 300 -14 10 50Z"/></svg><p>{t["quote_text"]}</p></section>
<section class="who">{_lab("Tutti", "")}<h2>{t["who_h"]}</h2><div class="roles">{who}</div></section>
<section class="glue"><h2>{t["glue_h"]}</h2><div class="g3">{glue}</div></section>
<section class="ticket"><div class="stub">{_lab("Ingresso libero", n["free"])}<h2>{t["end_h"]}</h2>
<a class="btn" href="{t["end_href2"]}" target="_blank" rel="noopener">{t["end_btn2"]}</a></div><div class="tear"><span>N° 2026</span><b>W.L</b></div></section>
</div>'''


CSS = """
@font-face{font-family:"Bravura Score";src:url(/fonts/bravura/bravura-score.woff) format("woff");font-display:block}
.fv2{font-family:Pretendard,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.75}
html[lang=ko] .fv2,html[lang=zh] .fv2{word-break:keep-all}
.fv2 h1,.fv2 h2,.fv2 h3{text-wrap:balance}
.fv2 .cover{display:grid;place-items:center;padding:56px 0 20px}
.fv2 .frame{border:1px solid var(--ink);outline:1px solid var(--ink);outline-offset:6px;padding:64px 56px;text-align:center;max-width:560px;width:100%;background:var(--paper)}
.fv2 .pre{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:20px;margin:0 0 22px;color:var(--soft)}
.fv2 .cover h1{font-family:"Cormorant Garamond",Georgia,serif!important;font-weight:500;font-style:italic!important;font-size:clamp(60px,11vw,116px);line-height:.92;margin:0;letter-spacing:-.02em}
.fv2 .orn{color:var(--accent);font-size:28px;margin:20px 0 10px}
.fv2 .subt{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:19px;margin:0}
html:not([lang=ko]):not([lang=zh]) .fv2 .subt{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:23px;font-weight:500}
.fv2 .season{font-size:12.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin:28px 0 0;font-weight:600}
.fv2 .lab{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:22px;color:var(--accent);margin:0 0 16px;text-align:center}
.fv2 .lab:before,.fv2 .lab:after{content:"—";color:var(--line);margin:0 14px}
.fv2 section{padding:100px 0 0}
.fv2 h2{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-style:normal;font-size:clamp(28px,4vw,40px);line-height:1.3;text-align:center;margin:0 0 36px}
html:not([lang=ko]):not([lang=zh]) .fv2 h2{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:500;font-size:clamp(34px,4.6vw,48px);line-height:1.15}
.fv2 .partitura h2{margin-bottom:14px}
.fv2 .partitura .intro{margin-bottom:34px}
.fv2 .intro{max-width:640px;margin:0 auto 26px;text-align:center;color:var(--soft);text-wrap:balance}
.fv2 .sheet{background:#fffdf8;border:1px solid #e2d6c3;padding:22px 20px 14px;box-shadow:0 40px 70px -40px rgba(60,35,15,.45),8px 8px 0 -1px #ebe2d2,8px 8px 0 0 #e2d6c3;margin:0 -60px}
.fv2 .scroll{overflow-x:auto}
.fv2 .score{display:block;width:100%;min-width:900px;height:auto}
.fv2 .score .mus{font-family:"Bravura Score";font-size:32px;fill:#1b1612}
.fv2 .score .dyn{font-size:30px}
.fv2 .score .st{stroke:#3a322b}.fv2 .score .ln{stroke:#1b1612}
.fv2 .score .thick,.fv2 .score .dt,.fv2 .score .beam{fill:#1b1612}
.fv2 .score .slur{fill:#1b1612;stroke:#1b1612;stroke-width:.4}
.fv2 .score .brk{stroke:#1b1612;stroke-width:4.5}.fv2 .score .brkc{stroke:#1b1612;stroke-width:2;fill:none}
.fv2 .score .ttl{font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:600;font-size:34px;fill:#1b1612}
.fv2 .score .sub{font-family:"Noto Serif KR","Cormorant Garamond",serif;font-weight:600;font-size:13px;fill:#6c6157;letter-spacing:.04em}
.fv2 .score .comp{font-family:"Cormorant Garamond",serif;font-weight:600;font-size:18px;fill:#1b1612;letter-spacing:.06em}
.fv2 .score .comp2{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:13px;fill:#6c6157}
.fv2 .score .pn{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:14px;fill:#1b1612}
.fv2 .score .pn.big{font-size:16px;fill:#6e1a2f}
.fv2 .score .pn2{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:14px;fill:#a8823f}.fv2 .score .pf{font-size:15px;fill:#6e1a2f}
.fv2 .score .reh{fill:none;stroke:#1b1612;stroke-width:1.3}
.fv2 .score .rehl{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:16px;fill:#1b1612}
.fv2 .score .tempo{font-family:"Cormorant Garamond",serif;font-weight:700;font-size:19px;fill:#1b1612}
.fv2 .score .stg{font-family:"Noto Serif KR","Cormorant Garamond",serif;font-weight:600;font-size:11.5px;fill:#a8823f}
.fv2 .score .mark{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:15px;fill:#6e1a2f}
.fv2 .score .dc{font-family:"Noto Serif KR","Cormorant Garamond",serif;font-weight:600;font-size:16px;fill:#6e1a2f}
.fv2 .score .lyr{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:14px;fill:#1b1612}
.fv2 .score .hl .lyr{fill:#8a1d3a}
.fv2 .score .pg{font-family:"Cormorant Garamond",serif;font-size:14px;fill:#a39484}
.fv2 .score .band{fill:#d4b57a;fill-opacity:.16}
.fv2 .score .hl .mus{fill:#8a1d3a}.fv2 .score .hl .ln{stroke:#8a1d3a;stroke-width:1.5}.fv2 .score .hl .beam,.fv2 .score .hl .slur{fill:#8a1d3a;stroke:#8a1d3a}
.fv2 .hint{text-align:center;font-size:13px;color:var(--faint);margin:20px 0 0}.fv2 .hint .m{display:none}
.fv2 .prog ol{list-style:none;margin:0 auto;padding:0;max-width:860px;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink)}
.fv2 .part{text-align:center;padding:34px 0 10px}.fv2 .part span{display:block;font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:30px}
.fv2 .part small{color:var(--gold);letter-spacing:.08em;font-size:13px}
.fv2 .night{margin:100px calc(50% - 50vw) 0;padding:110px 24px 120px;background:radial-gradient(ellipse at 50% 0%,#3a1320 0,#1a0d12 70%);color:#f2e6d6;text-align:center}
.fv2 .night .k{font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:#d4b57a;font-weight:700;margin:0 0 16px}
.fv2 .night blockquote{margin:0;font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:clamp(34px,5.4vw,58px);line-height:1.2;color:#fbf1e4}
html:not([lang=ko]):not([lang=zh]) .fv2 .night blockquote{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:500}
.fv2 .nslur{display:block;width:min(500px,80%);margin:8px auto 22px}.fv2 .nslur path{fill:#d4b57a}
.fv2 .night p:last-child{max-width:600px;margin:0 auto;color:#cdbba7}
.fv2 .ticket{display:grid;grid-template-columns:1fr 140px;margin-top:40px;filter:drop-shadow(0 20px 30px rgba(60,30,10,.18))}
.fv2 .stub{background:#6e1a2f;color:#f6eadb;padding:44px 40px;border-radius:14px 0 0 14px;text-align:center}
.fv2 .stub h2{color:#fff;margin:0 0 10px}.fv2 .stub .lab{color:#e3c58e}.fv2 .stub .lab:before,.fv2 .stub .lab:after{color:rgba(255,255,255,.25)}
.fv2 .stub p{color:#e7d3c3;margin:0 0 22px}
.fv2 .tear{background:#5a1426;border-left:2px dashed rgba(255,255,255,.35);border-radius:0 14px 14px 0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#e3c58e;gap:8px}
.fv2 .tear span{writing-mode:vertical-rl;letter-spacing:.3em;font-size:12px}.fv2 .tear b{font-family:"Cormorant Garamond",serif;font-size:34px;font-style:italic}
.fv2 .btn{display:inline-block;background:#f6eadb;color:#6e1a2f;text-decoration:none;padding:12px 28px;border-radius:99px;font-weight:700}
html,body{overflow-x:clip}
.fv2 .lead1{max-width:760px;margin:0 auto;color:var(--soft);font-size:17px;text-align:center;text-wrap:balance}
.fv2 .mov{display:grid;grid-template-columns:44px 1fr auto;gap:22px;align-items:center;padding:28px 0;border-top:1px solid var(--line)}
.fv2 .part+.mov{border-top:0}
.fv2 .no{font-family:"Cormorant Garamond",serif;font-size:24px;color:var(--gold);text-align:right;align-self:start;padding-top:6px}
.fv2 .tm{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:600;font-size:38px;line-height:1;color:var(--accent);margin:0 0 8px}
.fv2 .mov h3{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-style:normal;font-size:19px;margin:0 0 4px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.fv2 .tag{font-family:Pretendard,sans-serif;font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--gold);border:1px solid var(--gold);border-radius:99px;padding:1px 9px}
.fv2 .mov .q{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;color:var(--gold);margin:0 0 4px;font-size:15px}
.fv2 .mov .d{margin:0;color:var(--soft);font-size:15px;max-width:560px;text-wrap:pretty}
.fv2 .ics{display:flex;gap:14px;justify-content:flex-end}
.fv2 .ic{display:block;text-align:center;text-decoration:none;color:var(--soft);font-size:12.5px;font-weight:600;width:78px}
.fv2 .ic img{width:64px;height:64px;border-radius:16px;display:block;margin:0 auto 6px;box-shadow:0 12px 24px -12px rgba(60,30,15,.5);transition:transform .2s}
.fv2 a.ic:hover img{transform:translateY(-3px)}
.fv2 .ic.solo img{box-shadow:0 0 0 6px rgba(184,50,79,.08),0 0 26px 4px rgba(184,50,79,.22),0 12px 24px -12px rgba(60,30,15,.5)}
.fv2 .ic figcaption{display:block}
.fv2 .who h2,.fv2 .glue h2{margin-bottom:22px}
.fv2 .roles{max-width:860px;margin:0 auto;text-align:center}
.fv2 .roles input{position:absolute;opacity:0;pointer-events:none}
.fv2 .tabs{display:inline-flex;border:1px solid var(--line);border-radius:99px;padding:4px;background:var(--paper);margin:0 0 22px}
.fv2 .tabs label{cursor:pointer;padding:8px 22px;border-radius:99px;font-weight:600;color:var(--soft);font-size:15px}
#fv2r-s:checked~.tabs [for=fv2r-s],#fv2r-t:checked~.tabs [for=fv2r-t],#fv2r-a:checked~.tabs [for=fv2r-a]{background:var(--accent);color:#fbf1e4}
.fv2 .p{display:none;list-style:none;margin:0;padding:0;columns:2;column-gap:40px;text-align:left}
#fv2r-s:checked~.p-s,#fv2r-t:checked~.p-t,#fv2r-a:checked~.p-a{display:block}
.fv2 .p li{break-inside:avoid;display:flex;gap:14px;padding:14px 0;border-top:1px solid var(--line)}
.fv2 .p img{width:40px;height:40px;border-radius:10px;flex:none}
.fv2 .p b{display:block;font-family:"Noto Serif KR",Georgia,serif;font-weight:600}.fv2 .p span{color:var(--soft);font-size:14.5px}
.fv2 .g3{display:grid;grid-template-columns:repeat(3,1fr);max-width:860px;margin:0 auto;border-top:2px solid var(--ink)}
.fv2 .g3 div{padding:22px 22px 4px 0}.fv2 .g3 div+div{padding-left:22px;border-left:1px solid var(--line)}
.fv2 .g3 i{font-style:normal;color:var(--gold);font-size:20px}.fv2 .g3 b{display:block;font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:18px;margin:4px 0}
.fv2 .g3 span{color:var(--soft);font-size:14.5px}
.fv2 .drop:first-letter{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:1.6em;color:var(--accent)}
@media(max-width:1180px){.fv2 .sheet{margin:0 -10px}}
@media(max-width:700px){.fv2 .frame{padding:46px 22px}
.fv2 .mov{grid-template-columns:30px 1fr;gap:10px 14px}.fv2 .ics{grid-column:2;justify-content:flex-start}.fv2 .tm{font-size:32px}
.fv2 .p{columns:1}.fv2 .g3{grid-template-columns:1fr}.fv2 .g3 div+div{padding-left:0;border-left:0;border-top:1px solid var(--line)}.fv2 .ticket{grid-template-columns:1fr 64px}.fv2 .stub{padding:34px 22px}
.fv2 .hint .m{display:inline;color:var(--gold)}.fv2 .sheet{padding:14px 8px}.fv2 section{padding-top:72px}}
"""
