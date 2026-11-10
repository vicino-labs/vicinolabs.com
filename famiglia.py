"""Famiglia Vicino 포트폴리오 화면(2026-11-10, 사용자 요청: 모든 앱의 관계를 한눈에,
"딱 보면 다 필요하겠구나" 느끼게). /famiglia/ (de), /en/famiglia/, /ko/famiglia/.

흐름: 레슨 한 번의 길(찾기 → 준비 → 몸 풀기 → 연습 → 녹음·돌아보기 → 다음 레슨)에 앱을 얹는다.
앱 사이에 실제로 없는 연동은 쓰지 않는다(위레가토 아이디는 렛지부터 차례로).

통합 구독(하나만 구독하면 모든 앱): 아직 계획 단계 — SHOW_BUNDLE 이 False 면 숨김.
가격·이름이 정해지면 BUNDLE 문구를 고치고 True 로(가격은 HQ·사용자 승인 뒤).
"""
import math

SHOW_BUNDLE = False

# 단계별 앱(앱 키는 /apps/<key>.png 아이콘 이름)
STAGES = [
    ("find", ["welegato"]),
    ("prepare", ["leggii", "chiave"]),
    ("warmup", ["appoggio", "squillo"]),
    ("practise", ["pianino"]),
    ("reflect", ["prova"]),
]
RING = ["welegato", "leggii", "chiave", "appoggio", "squillo", "pianino", "prova"]
# 누구에게: 2 = 꼭, 1 = 성악 선생님만
WHO = {
    "welegato": (2, 2, 2), "leggii": (2, 2, 2), "chiave": (2, 2, 2), "appoggio": (2, 0, 1),
    "squillo": (2, 0, 1), "pianino": (2, 2, 2), "prova": (2, 2, 2),
}

# 앱 정보 배지 아이콘(지구) — 스토어 배지와 같은 높이의 검은 배지(2026-11-10 사용자 요청)
GLOBE = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="#fff" stroke-width="1.6">'
         '<circle cx="12" cy="12" r="9.2"/><ellipse cx="12" cy="12" rx="4" ry="9.2"/><path d="M3 12h18M4.6 7.2h14.8M4.6 16.8h14.8"/></svg>')

LINKS = {
    "welegato": {"info": "WELEGATO",
                 "play": "app.welegato.welegato", "apple": "https://welegato.com/ios/?lang={lang}"},  # 나라별 스토어로 보내는 주소
    "leggii": {"info": "/leggii/", "play": "com.vicinolabs.leggii", "apple": None},
    "chiave": {"info": "/chiave/", "play": None, "apple": None},
    "appoggio": {"info": "/appoggio/", "play": "com.vicinolabs.appoggio", "apple": "https://apps.apple.com/app/id6832364161"},
    "squillo": {"info": None, "play": None, "apple": None},
    "pianino": {"info": "/pianino/", "play": "com.vicinolabs.pianino", "apple": "https://apps.apple.com/app/id6832363954"},
    "prova": {"info": "/prova/", "play": None, "apple": None},
}

T = {'de': {'path': '/famiglia/',
        'home': '/',
        'title': 'Famiglia Vicino — so arbeiten unsere Musik-Apps zusammen',
        'desc': 'Sieben Apps, ein Musikerleben: Lehrer finden, Noten vorbereiten, einsingen, üben, aufnehmen. So greifen welegato, Leggii, '
                'Chiave, Appoggio, Squillo, Pianino und Prova ineinander.',
        'names': {'welegato': 'welegato',
                  'leggii': 'Leggii',
                  'chiave': 'Chiave',
                  'appoggio': 'Appoggio',
                  'squillo': 'Squillo',
                  'pianino': 'Pianino',
                  'prova': 'Prova'},
        'kicker': 'Famiglia Vicino',
        'h1': 'Für <em>jeden</em> Moment<br>Ihres Musikerlebens.',
        'lead': 'Der Tag, an dem Sie eine Lehrerin suchen. Der Abend über den Noten. Der letzte Atemzug vor dem Auftritt. Sieben Apps, '
                'jede für einen Moment — einzeln hilfreich, zusammen ein Ganzes.',
        'center': 'Ihre<br>Musik',
        'soon': 'Bald',
        'journey_h': 'Eine Unterrichtswoche, Schritt für Schritt',
        'journey_sub': 'Für jeden Moment, in dem es hakt, gibt es eine App.',
        'stages': {'find': ('Finden',
                            'Neu in der Stadt und auf Lehrersuche?',
                            'Finden Sie auf welegato Lehrkräfte, Korrepetitoren und Ensembles in Ihrer Nähe. Schreiben Sie in Ihrer '
                            'Sprache — der Chat übersetzt für beide Seiten.'),
                   'prepare': ('Vorbereiten',
                               'Die Arie liegt eine Terz zu hoch?',
                               'Ihre Noten liegen in Leggii auf dem Tablet, mit allen Eintragungen aus dem Unterricht. Passt die Tonart '
                               'nicht, genügt ein Foto: Chiave transponiert in Ihre Lage.'),
                   'warmup': ('Einsingen',
                              'Die Stimme ist noch nicht wach?',
                              'Mit Appoggio zuerst den Atem aufbauen, dann mit Squillo zur Klavierbegleitung einsingen.'),
                   'practise': ('Üben',
                                'Intonation üben, aber kein Klavier in der Nähe?',
                                'Pianino vereint Klavier, Metronom und Stimmgerät. Stellen Sie einfach Ihren Kammerton ein — 443 Hz wie im '
                                'Orchester oder 415 Hz für Barockmusik.'),
                   'reflect': ('Aufnehmen und auswerten',
                               'Was hat die Lehrerin noch mal gesagt?',
                               'Nehmen Sie Unterricht und Üben mit Prova auf. Die KI fasst zusammen, was gut lief und woran Sie als '
                               'Nächstes arbeiten.')},
        'warmup_tag': 'für Sängerinnen und Sänger',
        'loop_h': 'Und dann: die nächste Stunde',
        'loop': 'Mit allem, was Sie in der Woche erarbeitet haben, zurück in den Unterricht. Und wenn Sie eine neue Lehrerin, einen Coach '
                'oder eine Bühne suchen, öffnet welegato die nächste Tür. So bleibt die Musik legato — ohne Unterbrechung.',
        'who_h': 'Wer braucht was?',
        'who_sub': 'Ob Gesang, Instrument oder Unterricht — kaum ein Feld bleibt leer.',
        'who_cols': ('Sängerinnen und Sänger', 'Instrumentalisten', 'Lehrkräfte'),
        'who_half': 'für Gesangslehrkräfte',
        'glue_h': 'Einzeln stark, zusammen besser',
        'glue': [('Eine ID für alles',
                  'Mit einer welegato-ID müssen Sie sich nicht in jeder App neu registrieren. Leggii macht den Anfang, die anderen '
                  'folgen.'),
                 ('Gleiche Handschrift',
                  'Jede App bedient sich gleich, spricht dieselben Sprachen und stimmt, wo gestimmt wird, im selben Bereich von a′ = 415 '
                  'bis 466 Hz.'),
                 ('Kostenlos starten', 'Alle Apps sind kostenlos nutzbar, vieles ganz ohne Konto. Extras nur, wenn Sie sie brauchen.')],
        'bundle_kicker': 'Bald',
        'bundle_h': 'Ein Abo für alles',
        'bundle': 'Bald gibt es ein gemeinsames Abo: einmal abschließen, und alle Extras aller Famiglia-Vicino-Apps sind freigeschaltet.',
        'all_h': 'Alle Apps ansehen',
        'all_btn': 'Zur App-Übersicht',
        'all_href': '/#apps',
        'langs': 'Sprache',
        'quote_kicker': 'we + legato',
        'quote': 'Spielen wir legato?',
        'quote_text': 'Wie beim Legato, wo die Töne ohne Unterbrechung ineinanderfließen,<br class="w"> verbinden die Apps von Famiglia '
                      'Vicino jeden Moment Ihres Musikerlebens —<br class="w"> ohne Bruch, von einer Stunde zur nächsten.',
        'quote_src': 'aus welegato',
        'end_h': 'Dann spielen wir legato.',
        'end_btn2': 'welegato öffnen',
        'end_href2': 'https://welegato.com/',
        'apps_h': 'Alle Apps auf einen Blick',
        'apps_sub': 'Infos und Downloads für jede App.',
        'info': 'Mehr erfahren',
        'apple_soon': 'App Store bald',
        'd': {'welegato': 'Musiklehrkräfte, Korrepetitoren und Musiker in Europa und Korea finden — mit automatischer Übersetzung im Chat.',
              'leggii': 'Die einfache Noten-App: PDF-Noten, Notizen, IMSLP-Suche, Metronom, Unterrichtsaufnahmen und KI-Notizen.',
              'chiave': 'Noten fotografieren und in jede Tonart transponieren.',
              'appoggio': 'Atemtraining für Sängerinnen und Sänger — kostenlos, ohne Konto.',
              'squillo': 'Tägliche Stimm- und Einsingübungen für Sängerinnen und Sänger.',
              'pianino': 'Klavier, Metronom und Stimmgerät in einer App — mit einstellbarem Kammerton.',
              'prova': 'Unterricht und Üben aufnehmen, mit KI-Auswertung der Aufnahme.'},
        'info_top': 'Mehr erfahren',
        'info_main': 'App-Info'},
 'en': {'path': '/en/famiglia/',
        'home': '/en/',
        'title': 'Famiglia Vicino — how our music apps work together',
        'desc': 'Seven apps, one musical life: find a teacher, prepare your scores, warm up, practise, record. How welegato, Leggii, '
                'Chiave, Appoggio, Squillo, Pianino and Prova fit together.',
        'names': {'welegato': 'welegato',
                  'leggii': 'Leggii',
                  'chiave': 'Chiave',
                  'appoggio': 'Appoggio',
                  'squillo': 'Squillo',
                  'pianino': 'Pianino',
                  'prova': 'Prova'},
        'kicker': 'Famiglia Vicino',
        'h1': 'For <em>every</em> moment<br>of your musical life.',
        'lead': 'The day you look for a teacher. The evening over your scores. The last breath before you walk on stage. Seven apps, each '
                'for one moment — useful on their own, whole together.',
        'center': 'Your<br>music',
        'soon': 'Soon',
        'journey_h': 'A lesson week, step by step',
        'journey_sub': "Whenever you get stuck, there's an app for that moment.",
        'stages': {'find': ('Find',
                            'New in town and looking for a teacher?',
                            'Find teachers, accompanists and ensembles near you on welegato. Write in your own language — the chat '
                            'translates for both sides.'),
                   'prepare': ('Prepare',
                               'The aria sits a third too high?',
                               'Your scores live in Leggii on your tablet, with every marking from your lessons. Wrong key? One photo is '
                               'enough — Chiave transposes it into your range.'),
                   'warmup': ('Warm up',
                              'Voice not awake yet?',
                              'Build your breath with Appoggio first, then warm up to piano accompaniment in Squillo.'),
                   'practise': ('Practise',
                                'Need to check your pitch, but no piano around?',
                                'Pianino puts piano, metronome and tuner in one app. Just set your pitch — 443 Hz like the orchestra or '
                                '415 Hz for Baroque music.'),
                   'reflect': ('Record and reflect',
                               'What did your teacher say again?',
                               'Record lessons and practice with Prova. The AI sums up what went well and what to work on next.')},
        'warmup_tag': 'for singers',
        'loop_h': 'And then: the next lesson',
        'loop': 'Take everything you built this week back to your lesson. And when you need a new teacher, coach or stage, welegato opens '
                "the next door. That's how music stays legato.",
        'who_h': 'Who needs what?',
        'who_sub': 'Voice, instrument or teaching — hardly a box stays empty.',
        'who_cols': ('Singers', 'Instrumentalists', 'Teachers'),
        'who_half': 'for voice teachers',
        'glue_h': 'Strong alone, better together',
        'glue': [('One ID for everything',
                  "With one welegato ID you don't have to sign up again in every app. Leggii comes first, the others follow."),
                 ('One handwriting',
                  'Every app works the same way, speaks the same languages and, wherever there is tuning, tunes within the same A4 = '
                  '415–466 Hz.'),
                 ('Free to start', 'Every app is free to use, much of it without an account. Extras only when you need them.')],
        'bundle_kicker': 'Soon',
        'bundle_h': 'One subscription for everything',
        'bundle': 'A shared subscription is on its way: subscribe once and unlock the extras of every Famiglia Vicino app.',
        'all_h': 'See all apps',
        'all_btn': 'Go to the app overview',
        'all_href': '/en/#apps',
        'langs': 'Language',
        'quote_kicker': 'we + legato',
        'quote': 'Shall we play legato?',
        'quote_text': 'Like legato, where notes flow on without a break,<br class="w"> the Famiglia Vicino apps connect every moment of '
                      'your musical life —<br class="w"> seamlessly, from one lesson to the next.',
        'quote_src': 'from welegato',
        'end_h': "Then let's play legato.",
        'end_btn2': 'Open welegato',
        'end_href2': 'https://welegato.com/en/',
        'apps_h': 'All apps at a glance',
        'apps_sub': 'Details and downloads for every app.',
        'info': 'Learn more',
        'apple_soon': 'App Store soon',
        'd': {'welegato': 'Find music teachers, accompanists and musicians in Europe and Korea — with automatic chat translation.',
              'leggii': 'A simple sheet music reader: PDF scores, notes, IMSLP search, a metronome, lesson recordings and AI lesson notes.',
              'chiave': 'Photograph sheet music and transpose it into any key.',
              'appoggio': 'Breathing training for singers — free, no sign-up.',
              'squillo': 'Daily vocal exercises and warm-ups for singers.',
              'pianino': 'Piano, metronome and tuner in one app — with adjustable concert pitch.',
              'prova': 'Record lessons and practice, with AI feedback on the recording.'},
        'info_top': 'Learn more',
        'info_main': 'App info'},
 'ko': {'path': '/ko/famiglia/',
        'home': '/en/',
        'title': 'Famiglia Vicino — 음악 앱들이 함께 일하는 방법',
        'desc': '앱 일곱 개, 음악 생활 하나: 선생님 찾기, 악보 준비, 몸 풀기, 연습, 녹음. 위레가토·렛지·끼아베·아뽀조·스퀼로·피아니노·프로바가 이렇게 이어져요.',
        'names': {'welegato': '위레가토',
                  'leggii': '렛지',
                  'chiave': '끼아베',
                  'appoggio': '아뽀조',
                  'squillo': '스퀼로',
                  'pianino': '피아니노',
                  'prova': '프로바'},
        'kicker': 'Famiglia Vicino',
        'h1': '음악가의 하루,<br>그 <em>모든</em> 순간에.',
        'lead': '선생님을 찾는 날, 악보를 펼치는 밤, 무대에 오르기 전 마지막 호흡까지.<br class="w"> 일곱 개의 앱이 각자 한 순간을 맡아요.<br class="w"> 하나씩 써도 좋지만, 함께 쓰면 비로소 하나의 '
                '흐름이 돼요.',
        'center': '나의<br>음악',
        'soon': '곧 출시',
        'journey_h': '레슨 일주일, 이렇게 흘러가요',
        'journey_sub': '막히는 순간마다 꺼내 쓰는 앱이 있어요.',
        'stages': {'find': ('찾기', '새 도시에서 선생님을 찾고 있나요?', '가까운 선생님·반주자·앙상블을 위레가토에서 찾으세요. 현지 언어가 서툴러도 괜찮아요. 채팅이 서로의 언어로 번역해 줘요.'),
                   'prepare': ('준비하기',
                               '아리아가 3도 높게 쓰여 있나요?',
                               '악보는 렛지에 담아 태블릿으로. 레슨에서 적어 둔 표시도 그대로 남아요. 키가 맞지 않으면 사진 한 장이면 돼요. 끼아베가 내 음역으로 옮겨 줘요.'),
                   'warmup': ('몸 풀기', '목이 아직 덜 깨어났나요?', '아뽀조로 호흡 훈련하고, 스퀼로의 피아노 반주에 맞춰 발성 연습해요.'),
                   'practise': ('연습하기',
                                '피아노 없이 음정을 잡아야 하나요?',
                                '피아니노 하나에 피아노·메트로놈·튜너가 다 있어요. 오케스트라에서 쓰는 443Hz도, 바로크 음악의 415Hz도 원하는 기준음으로 맞춰 쓸 수 있어요.'),
                   'reflect': ('녹음하고 돌아보기', '레슨에서 들은 말, 벌써 흐릿한가요?', '프로바로 레슨과 연습을 녹음하세요. AI가 잘된 점과 다음에 연습할 점을 정리해 줘요.')},
        'warmup_tag': '성악가를 위해',
        'loop_h': '그리고 다시, 다음 레슨',
        'loop': '한 주 동안 쌓은 것을 들고 다시 레슨으로. 새 선생님, 코치, 무대가 필요해지면 위레가토가 다음 문을 열어요. 음악은 그렇게 끊기지 않고 이어져요.',
        'who_h': '누구에게 무엇이 필요할까요?',
        'who_sub': '성악가든 연주자든 선생님이든, 비어 있는 칸이 거의 없어요.',
        'who_cols': ('성악가', '기악 연주자', '선생님'),
        'who_half': '성악 선생님에게',
        'glue_h': '따로 또 같이',
        'glue': [('아이디 하나로', '위레가토 아이디 하나면 앱마다 새로 가입하지 않아도 돼요. 렛지부터 시작해 차례로 이어져요.'),
                 ('같은 손길', '어느 앱을 열어도 사용법과 언어가 같고, 음을 맞추는 앱은 모두 같은 기준음 범위(A4 415~466Hz)를 써요.'),
                 ('무료로 시작', '모든 앱은 무료로 시작할 수 있고, 많은 기능은 가입 없이도 돼요. 추가 기능은 필요할 때만.')],
        'bundle_kicker': '곧',
        'bundle_h': '구독 하나로 전부',
        'bundle': '공동 구독을 준비하고 있어요. 한 번만 구독하면 Famiglia Vicino 모든 앱의 추가 기능이 열려요.',
        'all_h': '모든 앱 보기',
        'all_btn': '앱 목록으로',
        'all_href': '/en/#apps',
        'langs': '언어',
        'quote_kicker': 'we + legato',
        'quote': '우리 레가토 할까요?',
        'quote_text': '음을 끊지 않고 이어 연주하는 레가토처럼,<br class="w"> Famiglia Vicino의 앱들은 음악가의 하루를 끊김 없이 이어요.<br class="w"> 한 레슨에서 다음 레슨까지.',
        'quote_src': '위레가토에서',
        'end_h': '이제, 함께 레가토 해요.',
        'end_btn2': '위레가토 열기',
        'end_href2': 'https://welegato.com/ko/',
        'apps_h': '앱 바로가기',
        'apps_sub': '앱마다 자세한 정보와 다운로드 링크를 모았어요.',
        'info': '앱 정보',
        'apple_soon': 'App Store 곧 출시',
        'd': {'welegato': '유럽과 한국에서 음악 선생님·반주자·연주자를 찾는 앱. 채팅은 자동으로 번역돼요.',
              'leggii': '쉬운 악보 앱: PDF 악보, 메모, IMSLP 검색, 메트로놈, 레슨 녹음과 AI 노트.',
              'chiave': '악보를 사진으로 찍어 원하는 키로 옮겨요.',
              'appoggio': '성악가를 위한 호흡 훈련 — 무료, 가입 없이.',
              'squillo': '성악가를 위한 매일의 발성 연습.',
              'pianino': '피아노·메트로놈·튜너를 한 앱에. 기준음을 맞춰 쓸 수 있어요.',
              'prova': '레슨과 연습을 녹음하면 AI가 녹음을 분석해 줘요.'},
        'info_top': '자세히 보기',
        'info_main': '앱 정보'}}

# ── 8개 언어(2026-11-10) — site_i18n.py 에서 합친다 ──
import site_i18n as I
WHO = {k: (2, 2, 2) for k in RING}  # 학생·선생님·반주자 모두(사용자: 각각 앱이 셋 모두에게 필요)
T["ko"]["lead"] = ('선생님을 찾는 날, 악보를 펼치는 밤, 무대에 오르기 전 마지막 호흡까지.<br class="w"> '
                   '학생에게도, 선생님에게도, 반주자에게도 — 일곱 개의 앱이 각자 한 순간을 맡아요.<br class="w"> '
                   '하나씩 써도 좋지만, 함께 쓰면 비로소 하나의 흐름이 돼요.')
for _l in I.LANGS:
    if _l not in T:
        _b = dict(T["en"]); _b.update(I.FAM_MORE[_l])
        _b["stages"] = {**T["en"]["stages"], **I.FAM_MORE[_l]["stages"]}
        _b["names"] = dict(T["en"]["names"])
        T[_l] = _b
    _t = T[_l]
    _t["path"] = I.fam_path(_l); _t["home"] = I.home_path(_l)
    _t["end_href2"] = I.welegato_url(_l); _t["all_href"] = I.home_path(_l) + "#apps"
    _t["stages"] = dict(_t["stages"]); _t["stages"]["prepare"] = I.PREP[_l]
    _t["who_h"], _t["who_sub"] = I.WHO_H[_l]
    _t["who_cols"] = I.ROLES[_l]; _t["roles"] = I.ROLES[_l]; _t["scen"] = I.SCEN[_l]
    for _k in ("lead", "journey_sub", "loop", "who_sub", "apps_sub", "quote_text", "d", "scen", "glue"):
        _t[_k] = I.nb(_t[_k])
    # 스퀼로 연습곡(2026-11-10 사용자: 콘코네는 한국 입시에 꼭 필요) — 지금은 파노프카만, 콘코네·바카이는 곧
    _h, _q, _a = _t["stages"]["warmup"]; _t["stages"]["warmup"] = (_h, _q, _a + " " + I.STUDI[_l])
    _t["d"] = dict(_t["d"]); _t["d"]["squillo"] = _t["d"]["squillo"] + " " + I.STUDI[_l]
    _t["stages"] = {k: (I.nb(h), I.nb(q), I.nb(a)) for k, (h, q, a) in _t["stages"].items()}
    _t["quote"] = I.nb(_t["quote"]); _t["loop_h"] = I.nb(_t["loop_h"])
    if _l not in ("ko", "zh"):  # 서양어 제목은 강제 줄바꿈 대신 균형 줄바꿈(끝 낱말 홀로 남지 않게)
        _t["h1"] = I.nb(_t["h1"].replace("<br>", " "), pair=13)

CSS = """
html[lang=ko] body{word-break:keep-all}
main h1,main h2,main h3,.fam-quote p,.fam-quote blockquote,.lead,.sub,.fam-body p,.fam-card p,.fam-glue span,.fam-loop p{text-wrap:balance}
.fam-body p,.fam-card p,.fam-glue span{text-wrap:pretty}
@media(max-width:820px){br.w{display:none}}
body{font-family:Pretendard,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-synthesis:none}
main h1,main h2,main h3,.fam-ring .center,.fam-num,.fam-glue b{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-style:italic;font-weight:500}
html[lang=ko] main h1,html[lang=ko] main h2,html[lang=ko] main h3,html[lang=ko] .fam-glue b{font-weight:600;letter-spacing:-.01em}
main h1{font-size:clamp(40px,6.4vw,68px);line-height:1.05}
html[lang=ko] main h1{font-size:clamp(34px,5.4vw,56px);line-height:1.2}
main h2{font-size:clamp(30px,4vw,40px)}
html[lang=ko] main h2{font-size:clamp(25px,3.3vw,33px)}
.fam-body h3{font-size:28px}
html[lang=ko] .fam-body h3{font-size:23px}
.fam-body .fam-q{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-style:italic;font-size:21px;color:var(--accent)!important;margin:0 0 6px!important;line-height:1.3}
html[lang=ko] .fam-body .fam-q{font-size:17px;font-weight:600}
html[lang=ko] main h1,html[lang=ko] main h2,html[lang=ko] main h3,html[lang=ko] .fam-glue b,html[lang=ko] .fam-body .fam-q{font-family:"Noto Serif KR",Georgia,serif;font-style:normal}
.fam-ring .node.big{width:26%;z-index:2;font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-style:italic;font-size:clamp(16px,2vw,19px);color:var(--accent);line-height:1.15}
html[lang=ko] .fam-ring .node.big{font-family:"Noto Serif KR",Georgia,serif;font-style:normal;font-weight:600}
.fam-ring .node.big img{box-shadow:0 10px 28px rgba(110,26,47,.38)}
.fam-ring .node.big small{display:block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-style:normal;font-weight:600;font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-top:2px}
.fam-ring .hub img{width:100%;height:auto;border-radius:22%;box-shadow:0 10px 28px rgba(110,26,47,.35);display:block;margin-bottom:6px}
.fam-ring .hub{position:absolute;left:50%;top:50%;width:30%;transform:translate(-50%,-46%);text-align:center;font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-style:italic;font-size:clamp(17px,2.2vw,21px);color:var(--accent);line-height:1.2}
html[lang=ko] .fam-ring .hub{font-family:"Noto Serif KR",Georgia,serif;font-style:normal;font-weight:600}
html[lang=ko] main h1 em{font-style:normal}
.fam-hero{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding:64px 0 56px}
.fam-ring{position:relative;width:100%;max-width:420px;margin-top:20px!important;aspect-ratio:1;margin:0 auto}
.fam-ring svg{position:absolute;inset:0;width:100%;height:100%}
.fam-ring .node{position:absolute;width:17%;transform:translate(-50%,-50%);text-align:center;font-size:12px;color:var(--soft);line-height:1.25}
.fam-ring .node img{width:100%;height:auto;border-radius:22%;box-shadow:0 6px 16px rgba(40,25,15,.18);display:block;margin-bottom:5px}
.fam-ring .center{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-family:Georgia,"Times New Roman",serif;font-style:italic;font-size:clamp(20px,3vw,27px);text-align:center;color:var(--accent);line-height:1.15}
.fam-langs{font-size:13px;color:var(--soft);margin-top:22px}.fam-langs a{margin-right:12px;font-weight:600;text-decoration:none}
.fam-steps{list-style:none;margin:0;padding:0;position:relative}
.fam-steps:before{content:"";position:absolute;left:27px;top:30px;bottom:30px;width:2px;background:linear-gradient(var(--goldl),var(--line))}
.fam-step{position:relative;display:grid;grid-template-columns:56px 1fr;gap:20px;padding:0 0 26px}
.fam-num{width:56px;height:56px;border-radius:50%;background:var(--paper);border:2px solid var(--goldl);display:flex;align-items:center;justify-content:center;font-family:Georgia,"Times New Roman",serif;font-size:20px;color:var(--gold);position:relative;z-index:1}
.fam-body{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:20px 22px;display:grid;grid-template-columns:minmax(150px,220px) 1fr;gap:6px 26px;align-items:start}
.fam-body h3{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:23px;margin:0 0 10px}
.fam-tag{display:inline-block;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--gold);margin:-6px 0 10px}
.fam-apps{display:flex;flex-wrap:wrap;gap:14px}
.fam-app{display:flex;align-items:center;gap:9px;font-size:15px;font-weight:600}
.fam-app img{width:40px;height:40px;border-radius:10px;box-shadow:0 3px 9px rgba(40,25,15,.15)}
.fam-app .soon{margin-left:2px}
.fam-body p{margin:0;color:var(--soft);font-size:15.5px}
.fam-loop .fam-num{background:var(--accent);border-color:var(--accent);color:var(--bg);font-size:26px}
.fam-loop .fam-body{border-style:dashed;border-color:var(--goldl)}
.fam-who{width:100%;border-collapse:collapse;background:var(--paper);border:1px solid var(--line);border-radius:18px;overflow:hidden;font-size:15px}
.fam-who th,.fam-who td{padding:12px 14px;border-bottom:1px solid var(--line);text-align:center}
.fam-who tr:last-child td{border-bottom:0}
.fam-who th{font-weight:600;font-size:13px;color:var(--soft)}
.fam-who td:first-child,.fam-who th:first-child{text-align:left}
.fam-who td:first-child{display:flex;align-items:center;gap:10px;font-weight:600}
.fam-who td:first-child img{width:30px;height:30px;border-radius:8px}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--accent)}
.dot.half{background:linear-gradient(90deg,var(--accent) 50%,transparent 50%);border:1.5px solid var(--accent);width:13px;height:13px}
.fam-legend{font-size:13px;color:var(--soft);margin-top:10px;display:flex;align-items:center;gap:8px}
.fam-glue{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.fam-glue div{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:22px}
.fam-glue b{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:20px;display:block;margin-bottom:6px}
.fam-glue span{color:var(--soft);font-size:15px}
.fam-bundle{margin-top:8px;border-radius:22px;padding:36px 32px;background:var(--accent);color:#fbf3e8;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center}
.fam-bundle h2{color:#fff}.fam-bundle p{margin:6px 0 0;color:#f1dfd0;max-width:560px}
.fam-bundle .kicker{color:#e9c98f;margin-bottom:8px}
.fam-bundle .stack{display:flex}.fam-bundle .stack img{width:44px;height:44px;border-radius:11px;border:2px solid var(--accent);margin-left:-12px;box-shadow:0 4px 10px rgba(0,0,0,.25)}
.fam-all{text-align:center;padding:48px 0 8px}
.fam-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.fam-card{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:20px;display:flex;gap:16px;align-items:flex-start}
.fam-card .icon{width:64px;height:64px;border-radius:15px;flex:none;box-shadow:0 5px 14px rgba(40,25,15,.16)}
.fam-card h3{font-size:24px;margin:0;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
html[lang=ko] .fam-card h3{font-size:20px}
.fam-card p{margin:4px 0 12px;color:var(--soft);font-size:15px}
.fam-links{display:flex;flex-wrap:wrap;align-items:center;gap:10px 12px}
.fam-links a.badge{display:inline-flex;align-items:center;justify-content:center;width:136px;height:40px;box-sizing:border-box;background:#000;border:1px solid #a6a6a6;border-radius:8px;overflow:hidden;line-height:1;text-decoration:none;color:#fff}
.fam-links a.badge img{height:38px;width:auto;max-width:134px;display:block}
.fam-links a.badge.gp img{height:34px}
.fam-links a.badge.info{gap:8px;padding:0 10px}
.fam-links a.badge.info span{display:flex;flex-direction:column;gap:2px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:15px;font-weight:600;letter-spacing:-.01em}
.fam-links a.badge.info small{font-size:9px;font-weight:500;letter-spacing:.02em}
.fam-links .later{font-size:12px;color:var(--faint)}
@media(max-width:820px){.fam-cards{grid-template-columns:1fr}}
.fam-all a.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}
.fam-quote{text-align:center;max-width:720px;margin:0 auto;padding:30px 0 64px}
.fam-quote blockquote{margin:0 0 14px;font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-style:italic;font-weight:500;font-size:clamp(36px,5.6vw,58px);line-height:1.1;color:var(--accent)}
.fam-quote blockquote:before{content:"“";color:var(--goldl);margin-right:.06em}.fam-quote blockquote:after{content:"”";color:var(--goldl);margin-left:.06em}
.fam-quote p{color:var(--soft);font-size:clamp(16px,1.8vw,18px);margin:0}
.fam-quote p.kicker{font-size:12px;color:var(--gold);margin:0 0 12px}
html[lang=ko] .fam-quote blockquote{font-family:"Noto Serif KR",Georgia,serif;font-style:normal;font-weight:600;font-size:clamp(30px,4.6vw,46px)}
.fam-ring .hub small{display:block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-style:normal;font-weight:600;font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-top:2px}
.fam-all a.btn{display:inline-block;margin-top:14px;background:var(--ink);color:var(--bg);text-decoration:none;padding:11px 22px;border-radius:99px;font-weight:600;font-size:15px}
@media(max-width:820px){.fam-hero{grid-template-columns:1fr;padding:44px 0 36px}.fam-body{grid-template-columns:1fr}.fam-glue{grid-template-columns:1fr}.fam-bundle{grid-template-columns:1fr;padding:28px 22px}}
@media(max-width:520px){.fam-step{grid-template-columns:40px 1fr;gap:12px}.fam-num{width:40px;height:40px;font-size:16px}.fam-steps:before{left:19px}.fam-loop .fam-num{font-size:20px}.fam-body{padding:16px}.fam-who th,.fam-who td{padding:10px 6px}.fam-who td:first-child img{width:24px;height:24px}.fam-who td:first-child{gap:6px;font-size:14px}.fam-ring .node{font-size:10.5px}}
.fam-roles{position:relative}.fam-roles input{position:absolute;opacity:0;pointer-events:none}
.fam-tabs{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 16px}
.fam-tabs label{cursor:pointer;padding:9px 18px;border-radius:99px;border:1px solid var(--line);background:var(--paper);font-weight:600;font-size:15px;color:var(--soft)}
#role-s:checked~.fam-tabs label[for=role-s],#role-t:checked~.fam-tabs label[for=role-t],#role-a:checked~.fam-tabs label[for=role-a]{background:var(--accent);border-color:var(--accent);color:#fbf3e8}
#role-s:focus-visible~.fam-tabs label[for=role-s],#role-t:focus-visible~.fam-tabs label[for=role-t],#role-a:focus-visible~.fam-tabs label[for=role-a]{outline:2px solid var(--gold);outline-offset:2px}
.fam-role{display:none;list-style:none;margin:0;padding:0;background:var(--paper);border:1px solid var(--line);border-radius:18px;overflow:hidden}
#role-s:checked~.p-s,#role-t:checked~.p-t,#role-a:checked~.p-a{display:block}
.fam-role li{display:flex;gap:14px;align-items:flex-start;padding:14px 18px;border-top:1px solid var(--line)}.fam-role li:first-child{border-top:0}
.fam-role img{width:40px;height:40px;border-radius:10px;flex:none;box-shadow:0 3px 9px rgba(40,25,15,.15)}
.fam-role b{display:block;font-size:15.5px;margin-bottom:2px}.fam-role span{color:var(--soft);font-size:15px;text-wrap:pretty}
.fam-role b .soon{margin-left:6px;vertical-align:1px}
html[lang=zh] main h1,html[lang=zh] main h2,html[lang=zh] main h3,html[lang=zh] .fam-glue b,html[lang=zh] .fam-body .fam-q,html[lang=zh] .fam-quote blockquote,html[lang=zh] .fam-ring .center{font-family:"Noto Serif KR","Songti SC","Noto Serif SC",serif;font-style:normal;font-weight:600}
html[lang=zh] main h1{font-size:clamp(34px,5.4vw,56px);line-height:1.2}html[lang=zh] main h1 em{font-style:normal}
html[lang=zh] body{word-break:normal;line-break:strict}
"""


def _soon(key, t, soon_keys):
    return f' <span class="soon">{t["soon"]}</span>' if key in soon_keys else ""


def ring(t, soon_keys):
    # 2026-11-10 사용자: 동그라미는 그대로, 위레가토만 둘레 맨 위에서 크게(가운데 허브보다 이게 낫다).
    n = len(RING)
    nodes = []
    for i, k in enumerate(RING):
        a = -math.pi / 2 + 2 * math.pi * i / n
        x = 50 + 38 * math.cos(a)
        y = 50 + 38 * math.sin(a)
        mark = " ·" if k in soon_keys else ""
        if k == "welegato":
            nodes.append(f'<div class="node big" style="left:{x:.1f}%;top:{y:.1f}%"><img src="/apps/{k}.png" alt="">'
                         f'{t["names"][k]}<small>we + legato</small></div>')
        else:
            nodes.append(f'<div class="node" style="left:{x:.1f}%;top:{y:.1f}%"><img src="/apps/{k}.png" alt="">{t["names"][k]}{mark}</div>')
    # 화살표가 도는 원(흐름이 다시 처음으로 이어진다는 뜻) — 위레가토에서 출발
    svg = ('<svg viewBox="0 0 100 100" aria-hidden="true"><defs><marker id="ah" viewBox="0 0 10 10" refX="5" refY="5" '
           'markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--goldl)"/></marker>'
           '<radialGradient id="glow"><stop offset="0" stop-color="#b8324f" stop-opacity=".22"/><stop offset="1" stop-color="#b8324f" stop-opacity="0"/></radialGradient></defs>'
           '<circle cx="50" cy="12" r="17" fill="url(#glow)"/>'
           '<circle cx="50" cy="50" r="38" fill="none" stroke="var(--goldl)" stroke-width=".5" stroke-dasharray="1.2 1.6"/>'
           '<path d="M 66 15.5 A 38 38 0 0 1 75 22" fill="none" stroke="var(--goldl)" stroke-width=".7" marker-end="url(#ah)"/></svg>')
    return f'<div class="fam-ring" role="img" aria-label="Famiglia Vicino">{svg}{"".join(nodes)}<div class="center">{t["center"]}</div></div>'


def body(lang, soon_keys):
    t = T[lang]
    langs = "".join(f'<a href="{T[l]["path"]}" hreflang="{l}" lang="{l}">{I.LANG_NAMES[l]}</a>' for l in I.LANGS if l != lang)
    hero = (f'<div class="fam-hero"><div><p class="kicker">{t["kicker"]}</p><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>'
            f'</div>{ring(t, soon_keys)}</div>')
    steps = []
    for i, (key, apps) in enumerate(STAGES, 1):
        h, q, d = t["stages"][key]
        tag = f'<span class="fam-tag">{t["warmup_tag"]}</span>' if key == "warmup" else ""
        chips = "".join(f'<span class="fam-app"><img src="/apps/{a}.png" alt="">{t["names"][a]}{_soon(a, t, soon_keys)}</span>' for a in apps)
        steps.append(f'<li class="fam-step"><div class="fam-num">{i:02d}</div><div class="fam-body"><div><h3>{h}</h3>{tag}'
                     f'<div class="fam-apps">{chips}</div></div><div><p class="fam-q">{q}</p><p>{d}</p></div></div></li>')
    steps.append(f'<li class="fam-step fam-loop"><div class="fam-num">↻</div><div class="fam-body"><div><h3>{t["loop_h"]}</h3>'
                 f'<div class="fam-apps"><span class="fam-app"><img src="/apps/welegato.png" alt="">{t["names"]["welegato"]}</span></div></div>'
                 f'<p>{t["loop"]}</p></div></li>')
    quote = (f'<div class="fam-quote"><p class="kicker">{t["quote_kicker"]}</p><blockquote>{t["quote"]}</blockquote>'
             f'<p>{t["quote_text"]}</p></div>')
    journey = (f'<section><h2>{t["journey_h"]}</h2><p class="sub">{t["journey_sub"]}</p>'
               f'<ol class="fam-steps">{"".join(steps)}</ol></section>')
    # 학생·선생님·반주자 탭(스크립트 없이 radio) — 앱마다 그 사람에게 필요한 상황
    ids = ("s", "t", "a")
    radios = "".join(f'<input type="radio" name="fam-role" id="role-{r}"{" checked" if r == "s" else ""}>' for r in ids)
    tabs = "".join(f'<label for="role-{r}">{name}</label>' for r, name in zip(ids, t["roles"]))
    panels = []
    for n, r in enumerate(ids):
        rows = "".join(f'<li><img src="/apps/{k}.png" alt=""><div><b>{t["names"][k]}{_soon(k, t, soon_keys)}</b><span>{t["scen"][k][n]}</span></div></li>' for k in RING)
        panels.append(f'<ul class="fam-role p-{r}">{rows}</ul>')
    who = (f'<section id="who"><h2>{t["who_h"]}</h2><p class="sub">{t["who_sub"]}</p>'
           f'<div class="fam-roles">{radios}<div class="fam-tabs">{tabs}</div>{"".join(panels)}</div></section>')
    glue = "".join(f"<div><b>{h}</b><span>{d}</span></div>" for h, d in t["glue"])
    glue = f'<section><h2>{t["glue_h"]}</h2><p class="sub"></p><div class="fam-glue">{glue}</div></section>'
    bundle = ""
    if SHOW_BUNDLE:
        stack = "".join(f'<img src="/apps/{k}.png" alt="">' for k in RING)
        bundle = (f'<section><div class="fam-bundle"><div><p class="kicker">{t["bundle_kicker"]}</p><h2>{t["bundle_h"]}</h2>'
                  f'<p>{t["bundle"]}</p></div><div class="stack">{stack}</div></div></section>')
    ext = ' target="_blank" rel="noopener"'
    blang = lang if lang in ("de", "en", "ko") else "en"
    cards = []
    for k in RING:
        L = LINKS[k]
        links = []
        info = I.welegato_url(lang) if L["info"] == "WELEGATO" else L["info"]
        if info:
            links.append(f'<a class="badge info" href="{info}"{ext if info.startswith("http") else ""}>{GLOBE}'
                         f'<span><small>{t["info_top"]}</small>{t["info_main"]}</span></a>')
        if L["play"]:
            links.append(f'<a class="badge gp" href="https://play.google.com/store/apps/details?id={L["play"]}&amp;hl={lang}"{ext}>'
                         f'<img src="/badges/google-play-{blang}-nb.png" alt="Google Play" height="38" loading="lazy"></a>')
        if L["apple"]:
            links.append(f'<a class="badge" href="{L["apple"].replace("{lang}", lang)}"{ext}>'
                         f'<img src="/badges/app-store-{blang}-nb.svg" alt="App Store" height="38" loading="lazy"></a>')
        elif L["play"]:
            links.append(f'<span class="later">{t["apple_soon"]}</span>')
        cards.append(f'<div class="fam-card"><img class="icon" src="/apps/{k}.png" alt=""><div><h3>{t["names"][k]}{_soon(k, t, soon_keys)}</h3>'
                     f'<p>{t["d"][k]}</p><div class="fam-links">{"".join(links)}</div></div></div>')
    apps = (f'<section id="apps"><h2>{t["apps_h"]}</h2><p class="sub">{t["apps_sub"]}</p>'
            f'<div class="fam-cards">{"".join(cards)}</div></section>')
    all_ = (f'<div class="fam-all"><p class="kicker">we + legato</p><h2>{t["end_h"]}</h2>'
            f'<a class="btn" href="{t["end_href2"]}" target="_blank" rel="noopener">{t["end_btn2"]}</a></div>')
    # 글꼴(2026-11-10): 위레가토 홈페이지와 같은 파일을 사이트 안에서(외부 불러오기 없음)
    fonts = "/fonts/fonts-v2.css" if lang in ("ko", "zh") else "/fonts/fonts-v2-latin.css"
    return f'<link rel="stylesheet" href="{fonts}"><style>{CSS}</style>{hero}{quote}{journey}{who}{glue}{bundle}{apps}{all_}'
