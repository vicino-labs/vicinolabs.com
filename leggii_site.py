#!/usr/bin/env python3
"""렛지(Leggii) 전용 제품 페이지 — vicinolabs.com/leggii/ (2026-11-17).

예전에는 app_home.page()로 찍던 얇은 카드형 소개였다. 대표님 말씀("누가 봐도 한 번에
렛지의 기능들을 이해하고 알 수 있게")대로, 기능마다 스크린샷과 설명이 붙어 스크롤만
해도 앱이 무엇을 해 주는지 알게 되는 제품 페이지로 바꿨다.

- 그림: leggii_shots.py 가 App Store 스크린샷에서 기기 화면만 잘라 /leggii/shots/<lang>/N.webp
  로 만들어 둔 것. 언어를 바꾸면 자바스크립트가 src 를 바꾼다(ko·en·de, 나머지는 en).
- 문구: 앱스토어/렛지/listing-full.md 의 등록 문구를 그대로 따랐다. 앱에 없는 기능은 쓰지 않는다.
- 디자인: 회사 사이트와 같은 고전 종이 느낌(아이보리·와인·금색, Georgia 세리프).
- 가격은 아직 적지 않는다(대표님 결정 사항, HQ 경유). 결제 자리만 비워 두었다.

build.py 가 leggii_legal.py 를 통해 부른다.
"""

SHOT_LANGS = ("ko", "en", "de")  # 스크린샷이 있는 언어
LANGS = [("ko", "한국어"), ("en", "English"), ("de", "Deutsch")]

PLAY = "https://play.google.com/store/apps/details?id=com.vicinolabs.leggii"
APPLE = "https://apps.apple.com/app/id6832925566"
EMAIL = "contact@vicinolabs.com"

CSS = """
:root{--bg:#f5f0e8;--paper:#fffcf6;--ink:#1c1714;--soft:#6b5f56;--faint:#9a8c7f;--line:#e4d9c8;--accent:#6e1a2f;--gold:#a8823f;--goldl:#d9b878;--tint:#efe7da}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#13110f;--paper:#1c1916;--ink:#f1e8da;--soft:#bfb2a2;--faint:#8f8274;--line:#2e2823;--accent:#e2a3b1;--gold:#d4b07a;--goldl:#8a6f45;--tint:#241f1b}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.7;-webkit-font-smoothing:antialiased;
 font-family:Pretendard,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;font-synthesis:none}
html[lang=ko] body{word-break:keep-all}
a{color:var(--accent)}
h1,h2,h3{font-family:"Cormorant Garamond",Georgia,"Times New Roman",serif;font-weight:500;letter-spacing:-.01em;margin:0}
html[lang=ko] h1,html[lang=ko] h2,html[lang=ko] h3{font-family:"Noto Serif KR",Georgia,serif;font-weight:600}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.top{border-bottom:1px solid var(--line);background:var(--bg)}
.top .in{max-width:1080px;margin:0 auto;padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.co{display:inline-flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-family:Georgia,serif;font-size:19px}
.co img{height:26px;width:auto}
.langbar{display:inline-flex;border:1px solid var(--line);border-radius:999px;padding:3px;background:var(--paper)}
.langbar button{border:0;background:transparent;color:var(--soft);font:600 13px/1 inherit;font-family:inherit;padding:8px 14px;border-radius:999px;cursor:pointer}
.langbar button.on{background:var(--ink);color:var(--bg)}

/* 맨 위 */
.hero{text-align:center;padding:44px 0 8px}
.hero .ic{width:92px;height:92px;border-radius:22px;display:block;margin:0 auto 18px;box-shadow:0 22px 44px -20px rgba(60,30,15,.5)}
.hero h1{font-size:clamp(36px,6.4vw,62px);line-height:1.12;margin:0 0 14px}
html[lang=ko] .hero h1{font-size:clamp(30px,5.2vw,50px)}
.kicker{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:600;margin:0 0 14px}
.hero .lede{font-size:clamp(17px,2vw,20px);color:var(--soft);margin:0 auto;max-width:620px;text-wrap:balance}
.shotwide{display:block;width:100%;height:auto;max-width:1000px;margin:30px auto 0;border-radius:16px}
.stores{display:flex;gap:14px;justify-content:center;align-items:center;flex-wrap:wrap;margin:28px 0 0}
.stores a{display:block;line-height:0}
.note{font-size:13.5px;color:var(--faint);margin:14px 0 0}

/* 요약 판 — 여기서 한 번 스크롤에 앱 전체가 들어와야 한다 */
.sum{border-top:1px solid var(--line);padding:clamp(34px,4.4vw,56px) 0 0}
.sum h2{font-size:clamp(24px,3.2vw,34px);margin:0 0 6px}
.sum .sub{color:var(--soft);margin:0 0 26px;font-size:16px}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.tile{background:var(--paper);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
.tile img{display:block;width:100%;height:auto;border-bottom:1px solid var(--line)}
.tile .tx{padding:14px 16px 16px}
.tile h3{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:19px;margin:0 0 3px;line-height:1.25}
html[lang=ko] .tile h3{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:17px}
.tile p{margin:0;color:var(--soft);font-size:14px;line-height:1.5;text-wrap:pretty}
@media(max-width:1000px){.tiles{grid-template-columns:repeat(3,1fr)}}
@media(max-width:720px){.tiles{grid-template-columns:repeat(2,1fr);gap:10px}
.tile .tx{padding:11px 12px 13px}.tile h3{font-size:15.5px}html[lang=ko] .tile h3{font-size:14.5px}.tile p{font-size:12.5px}}

/* 요금 비교표 — 한 화면에서 견주어 보게 */
.ptabwrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.ptab{width:100%;min-width:560px;border-collapse:collapse;font-size:15px;background:var(--paper);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.ptab th,.ptab td{padding:12px 14px;text-align:center;border-bottom:1px solid var(--line)}
.ptab th:first-child,.ptab td:first-child{text-align:left;color:var(--soft);white-space:normal}
.ptab thead th{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:18px;background:var(--tint);color:var(--ink)}
html[lang=ko] .ptab thead th{font-family:"Noto Serif KR",Georgia,serif;font-weight:600;font-size:16px}
.ptab tbody tr:last-child td{border-bottom:0;font-weight:600;color:var(--ink)}
@media(max-width:720px){.ptab{font-size:13.5px;min-width:520px}.ptab th,.ptab td{padding:9px 8px}}

/* 기능 줄 */
.feat{display:grid;grid-template-columns:1fr 1fr;gap:clamp(26px,4vw,56px);align-items:center;padding:clamp(34px,4.4vw,58px) 0;border-top:1px solid var(--line)}
.feat.flip .txt{order:2}
.feat h2{font-size:clamp(26px,3.4vw,38px);line-height:1.2;margin:0 0 14px}
html[lang=ko] .feat h2{font-size:clamp(23px,2.8vw,32px)}
.feat p{color:var(--soft);font-size:16.5px;margin:0 0 16px;text-wrap:pretty}
.feat ul{margin:0;padding:0;list-style:none}
.feat li{position:relative;padding-left:20px;color:var(--soft);font-size:15.5px;margin:7px 0}
.feat li::before{content:"";position:absolute;left:2px;top:.72em;width:6px;height:6px;border-radius:50%;background:var(--goldl)}
.shot{display:block;width:100%;height:auto;border-radius:10px}
@media(max-width:820px){.feat{grid-template-columns:1fr;gap:20px;padding:32px 0}.feat.flip .txt{order:0}.shot{max-width:480px;margin:0 auto}}

/* 요금 */
.plans{border-top:1px solid var(--line);padding:clamp(34px,4.4vw,58px) 0 10px}
.plans h2{font-size:clamp(26px,3.4vw,38px);margin:0 0 10px}
.plans .sub{color:var(--soft);margin:0 0 30px;max-width:620px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(248px,1fr));gap:16px}
.plan{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:24px}
.plan h3{font-size:22px;margin:0 0 4px}
.plan .tagline{color:var(--gold);font-size:13px;font-weight:600;letter-spacing:.04em;margin:0 0 12px}
.plan ul{margin:0;padding:0;list-style:none}
.plan li{position:relative;padding-left:18px;color:var(--soft);font-size:15px;margin:6px 0}
.plan li::before{content:"";position:absolute;left:1px;top:.7em;width:5px;height:5px;border-radius:50%;background:var(--goldl)}

/* 아래 */
.cta{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;border-radius:999px;padding:13px 26px;font-weight:600;font-size:15.5px}
.getit{text-align:center;border-top:1px solid var(--line);margin-top:clamp(28px,3.4vw,44px);padding:clamp(32px,4vw,52px) 0 10px}
.getit h2{font-size:clamp(26px,3.4vw,38px);margin:0 0 10px}
.getit p{color:var(--soft);margin:0 auto;max-width:560px}
.fam{display:inline-block;margin:30px 0 0;font-weight:600;font-size:14.5px;text-decoration:none;border-bottom:1px solid var(--line)}
footer{border-top:1px solid var(--line);margin-top:54px;padding:24px 0 44px;font-size:13.5px;color:var(--soft)}
footer a{color:var(--soft);margin-right:16px}
[data-l]:not(.on){display:none!important}
"""


def badge(lang):
    b = lang if lang in ("ko", "de", "en") else "en"
    return (f'<a href="{PLAY}&amp;hl={lang}" target="_blank" rel="noopener" aria-label="Google Play">'
            f'<img src="/badges/google-play-{b}-nb.png" alt="Google Play" width="162" height="48" '
            f'style="height:48px;width:auto;border-radius:10px;border:1px solid #a6a6a6;box-sizing:border-box"></a>'
            f'<a href="{APPLE}" target="_blank" rel="noopener" aria-label="App Store">'
            f'<img src="/badges/app-store-{b}.svg" alt="App Store" width="144" height="48" style="height:48px;width:auto"></a>')


# ── 문구 ────────────────────────────────────────────────────────────────
# 앱스토어 등록 문구(listing-full.md)를 따랐다. 앱에 실제로 있는 기능만.
T = {
"ko": {
 "title": "렛지 악보: 악보와 레슨 녹음, AI 레슨 노트 | Vicino Labs",
 "desc": "렛지 악보는 아이패드에 맞춰 만든 악보 앱입니다. PDF·사진·IMSLP에서 악보를 가져오고, 레슨과 리허설을 녹음하면 악보가 따라 넘어가며, AI가 지적과 숙제를 정리합니다.",
 "kicker": "Vicino Labs · Famiglia Vicino",
 "h1": "악보 보며 녹음하고,<br>AI로 정리까지",
 "lede": "아이패드에 맞춰 만든 악보 앱입니다. 다시 들을 때 악보가 저절로 따라 넘어가고, AI는 지적과 숙제를 시간·페이지와 함께 적어 둡니다.",
 "note": "아이패드·아이폰·안드로이드 태블릿과 휴대폰에서 씁니다. 기본 기능은 무료입니다.",
 "feats": [
  (1, "악보함", "악보를 한곳에", "PDF를 가져오거나 종이 악보를 카메라로 찍으면, 삐뚤게 찍힌 사진도 반듯하게 펴 줍니다. 제목과 작곡가는 알아서 읽어 냅니다.",
   ["전체 · 최근 본 악보 · 작곡가별로 보기", "즐겨찾기와 폴더", "연주회와 레슨 순서는 셋리스트로", "출판사와 페이지까지 한눈에"]),
  (2, "필기", "연필처럼 적습니다", "펜, 형광펜, 지우개, 올가미로 골라서 옮기기까지. Apple Pencil을 그대로 씁니다.",
   ["셈여림 · 임시표 · 아티큘레이션 · 운지", "반복과 D.C. 같은 음악 기호는 스탬프로", "필기는 페이지마다 그대로 남습니다"]),
  (3, "녹음", "녹음하면 악보가 따라 넘어갑니다", "악보를 펼친 채 단추 하나로 녹음합니다. 화면을 꺼도 계속 녹음하고, 넘긴 페이지가 함께 기록됩니다. 다시 들을 때 그 자리의 악보가 저절로 펼쳐집니다.",
   ["레슨과 리허설을 그대로", "다른 화면이나 백그라운드에서도 재생", "녹음한 자리를 눌러 바로 그 대목으로"]),
  (4, "AI 레슨 분석", "들은 말을 시간과 페이지로", "지적, 핵심, 숙제를 나눠 정리해 드립니다. 외국에서 레슨을 받아 말이 다 들리지 않을 때 특히 도움이 됩니다.",
   ["레슨 노트: 지적 · 핵심 · 숙제", "대화 받아 적기와 번역", "결과를 PDF로 저장해 그 위에 다시 필기", "요청할 때만 돌아가고, 쓸 시간을 먼저 보여 드립니다"]),
  (6, "IMSLP", "판본을 골라서 받습니다", "곡을 검색하면 출판사, 가사 언어, 편곡자, 미리보기를 보고 고를 수 있습니다. 성악가라면 가사 언어가 맞는 판본을, 반주자라면 필요한 조의 악보를 골라 받으세요.",
   ["출판사 · 가사 언어 · 편곡자로 추리기", "받기 전에 미리보기", "받으면 바로 악보함에"]),
  (7, "연습 도구", "메트로놈과 건반을 악보 위에", "악보를 덮지 않고 떠 있습니다. 음을 찾을 때도, 박을 맞출 때도 악보에서 눈을 떼지 않습니다.",
   ["아이패드 가로 화면에서 두 쪽 나란히", "야간 · 세피아 · 어둡게 읽기", "블루투스 페달이나 화면을 눌러 넘기기"]),
  (8, "렛지에게 물어보기", "물어보면 찾아 줍니다", "“토스카 악보 어디 있지?”, “오늘 녹음 분석해 줘”처럼 말하면 바로 찾아 주고 실행 단추까지 띄웁니다.",
   ["악보 찾기 · 녹음 분석 · 설정까지", "앱 쓰는 법도 물어보세요"]),
  (5, "위레가토 아이디와 클라우드", "기기를 바꿔도 그대로", "위레가토 아이디로 로그인하면 Pro와 AI 시간이 모든 기기에서 이어집니다. 로그인하지 않아도 렛지의 기본 기능은 다 쓸 수 있습니다.",
   ["렛지 클라우드(Plus): 악보 · 필기 · 폴더 · 셋리스트 · 녹음을 아이폰과 아이패드에서 똑같이", "자주 안 보는 악보는 클라우드에만 두어 기기 용량 확보", "클라우드를 쓰지 않으면 악보와 녹음은 기기에만 남습니다"]),
  (9, "Famiglia Vicino", "음악가의 하루를 함께 쓰는 앱들", "렛지는 비치노 랩스가 만드는 음악 앱 가족 가운데 하나입니다. 레슨 선생님이나 함께할 연주자를 찾고 있다면 위레가토를 만나 보세요.",
   ["위레가토: 음악 선생님과 연주자 찾기", "피아니노 · 아뽀조 · 프로바 · 끼아베 · 스퀼로"]),
 ],
  "sum_h": "렛지가 해 주는 일",
 "sum_sub": "여덟 가지입니다. 아래에서 셋은 더 자세히 보실 수 있습니다.",
 "tiles": {1: "PDF·카메라·IMSLP에서 가져와 한곳에",
           2: "펜·형광펜·음악 기호 스탬프, Apple Pencil",
           3: "넘긴 페이지가 함께 기록돼 다시 들을 때 따라 넘어갑니다",
           4: "지적·핵심·숙제를 시간과 페이지로",
           6: "출판사·가사 언어·편곡자를 보고 골라 받기",
           7: "악보를 덮지 않고 그 위에 떠 있습니다",
           8: "말로 물으면 찾아 주고 실행 단추까지",
           5: "Pro와 AI 시간, 클라우드가 기기마다 그대로"},
 "ptab_cols": ["", "무료", "7일 체험", "Pro", "Plus"],
 "ptab": [("악보·필기·녹음·메트로놈", "✓", "✓", "✓", "✓"),
          ("Pro 기능 전부", "–", "✓", "✓", "✓"),
          ("위레가토 배너", "있음", "없음", "없음", "없음"),
          ("매월 AI 분석", "–", "30분", "30분", "5시간"),
          ("렛지 클라우드", "–", "–", "–", "10GB · 50GB"),
          ("가격", "무료", "무료", "한 번 구매", "월 3.99유로부터")],
 "plans_h": "요금제",
 "plans_sub": "악보 가져오기, 필기, 녹음, 메트로놈 같은 기본 기능은 무료입니다. AI 분석과 클라우드는 서버 비용이 들어가는 부분이라 요금제로 받습니다.",
 "plans": [
  ("무료", "처음부터", ["악보 가져오기와 카메라 스캔", "필기와 음악 기호 스탬프", "레슨 · 리허설 녹음과 페이지 따라 넘기기", "메트로놈 · 건반 · IMSLP 검색"]),
  ("7일 체험", "가입하면 바로", ["Pro 기능 전부", "AI 30분", "카드 등록 없이"]),
  ("Leggii Pro", "한 번 구매, 평생", ["Pro 기능 전부", "위레가토 배너 없음", "매월 AI 30분", "첫 구매 보너스 60분"]),
  ("Leggii Plus", "월 3.99유로부터", ["Pro 기능 전부", "매월 AI 5시간", "렛지 클라우드 10GB: 월 3.99유로 · 연 39.99유로", "50GB: 월 5.99유로 · 연 59.99유로"]),
 ],
 "plans_note": "Pro 일회성 구매와 AI 시간 충전(5시간 · 15시간, 12개월 사용)은 앱 안에서 하실 수 있습니다. 나라마다 값이 다릅니다.",
 "plans_cta": "여기서 바로 Plus 구독하기", "plans_cta_note": "위레가토 아이디로 가입하고 카드로 결제합니다. 지금은 유럽에서만 받습니다.",
 "get_h": "내려받기",
 "get_p": "아이패드와 아이폰은 App Store에서, 안드로이드는 Google Play에서 받으세요.",
 "fam": "Famiglia Vicino의 다른 앱 보기",
 "privacy": "개인정보처리방침", "terms": "이용약관",
},
"en": {
 "title": "Leggii: sheet music, lesson recordings and AI lesson notes | Vicino Labs",
 "desc": "Leggii is a sheet music app made for the tablet. Import PDFs, photos and IMSLP editions, record your lessons and rehearsals while the score turns with you, and let AI sort out what was said.",
 "kicker": "Vicino Labs · Famiglia Vicino",
 "h1": "Record while you read,<br>let AI take the notes",
 "lede": "A sheet music app made for the tablet. When you listen back the score turns by itself, and the AI writes down the corrections and the homework with times and pages.",
 "note": "For iPad, iPhone and Android tablets and phones. The basics are free.",
 "feats": [
  (1, "Your library", "All your scores in one place", "Import PDFs or photograph paper music with the camera; tilted photos are straightened. Title and composer are recognised for you.",
   ["Browse all, recently opened or by composer", "Favourites and folders", "Setlists for concerts and lessons", "Publisher and page at a glance"]),
  (2, "Annotate", "Mark up scores like with a pencil", "Pen, highlighter, eraser, and a lasso to select and move what you wrote. Apple Pencil works as it should.",
   ["Dynamics, accidentals, articulation, fingering", "Stamps for repeats, D.C. and the rest", "Your ink stays where you put it, page by page"]),
  (3, "Record", "Record, and the score follows", "One tap records while the score is open, and it keeps going with the screen off. Every page turn is saved, so when you listen back the right page opens by itself.",
   ["Lessons and rehearsals as they happened", "Playback continues on other screens and in the background", "Tap a moment to jump straight to that passage"]),
  (4, "AI lesson notes", "What was said, by time and page", "Corrections, key points and homework, sorted out for you. It helps most when you take lessons in a language you are still learning.",
   ["Lesson notes: corrections, key points, homework", "Word-for-word transcript, with translation", "Save the result as a PDF and write on it", "Runs only when you ask, and shows the AI time first"]),
  (6, "IMSLP", "Choose the edition you want", "Search a work and choose by publisher, text language, arranger and preview. Singers can pick the language they sing in, accompanists the key they need.",
   ["Filter by publisher, text language and arranger", "Preview before you download", "Straight into your library"]),
  (7, "Practice tools", "Metronome and keys right on the score", "They float above the music instead of covering it, so you keep your eyes where they belong.",
   ["Two pages side by side on iPad in landscape", "Night, sepia and dimmed reading", "Turn pages with a Bluetooth pedal or a tap"]),
  (8, "Ask Leggii", "Just ask", "Say “Where is my Tosca score?” or “Analyse today's recording” and you get the answer with a button that does it.",
   ["Find scores, analyse recordings, open settings", "It also explains how the app works"]),
  (5, "welegato ID and cloud", "Change device, keep everything", "Sign in with your welegato ID and your Pro and AI time follow you to every device. Without signing in, all of Leggii's basics still work.",
   ["Leggii cloud (Plus): scores, ink, folders, setlists and recordings the same on iPhone and iPad", "Keep rarely used scores in the cloud only and free up space", "Without the cloud, scores and recordings stay on your device"]),
  (9, "Famiglia Vicino", "A family of apps for your musical day", "Leggii is one of the music apps Vicino Labs makes. Looking for a teacher or musicians to play with? Visit welegato.",
   ["welegato: find music teachers and players", "Pianino · Appoggio · Prova · Chiave · Squillo"]),
 ],
  "sum_h": "What Leggii does",
 "sum_sub": "Eight things. Three of them are shown up close below.",
 "tiles": {1: "Bring them in from PDFs, the camera and IMSLP",
           2: "Pen, highlighter, music stamps, Apple Pencil",
           3: "Page turns are saved, so the score follows when you listen back",
           4: "Corrections, key points and homework, by time and page",
           6: "Choose by publisher, text language and arranger",
           7: "They float above the music instead of covering it",
           8: "Ask out loud and get the answer with a button",
           5: "Pro, AI time and the cloud follow you to every device"},
 "ptab_cols": ["", "Free", "7-day trial", "Pro", "Plus"],
 "ptab": [("Scores, ink, recording, metronome", "✓", "✓", "✓", "✓"),
          ("All Pro features", "–", "✓", "✓", "✓"),
          ("welegato banner", "yes", "no", "no", "no"),
          ("AI analysis a month", "–", "30 min", "30 min", "5 hours"),
          ("Leggii cloud", "–", "–", "–", "10 GB · 50 GB"),
          ("Price", "free", "free", "one-time", "from €3.99 a month")],
 "plans_h": "Plans",
 "plans_sub": "Importing scores, annotating, recording and the metronome are free. AI analysis and the cloud cost us server time, so those are what the plans pay for.",
 "plans": [
  ("Free", "from the start", ["Import scores and camera scan", "Annotation and music stamps", "Lesson and rehearsal recording with page turns", "Metronome, keyboard, IMSLP search"]),
  ("7-day trial", "right away", ["Every Pro feature", "30 AI minutes", "No card needed"]),
  ("Leggii Pro", "one-time purchase", ["Every Pro feature", "No welegato banner", "30 AI minutes a month", "60-minute welcome bonus"]),
  ("Leggii Plus", "from €3.99 a month", ["Every Pro feature", "5 hours of AI a month", "Leggii cloud 10 GB: €3.99 a month, €39.99 a year", "50 GB: €5.99 a month, €59.99 a year"]),
 ],
 "plans_note": "The one-time Pro purchase and AI time top-ups (5 and 15 hours, valid 12 months) are available inside the app. Prices differ by country.",
 "plans_cta": "Subscribe to Plus here", "plans_cta_note": "Sign up with a welegato ID and pay by card. For Europe at the moment.",
 "get_h": "Get Leggii",
 "get_p": "On the App Store for iPad and iPhone, on Google Play for Android.",
 "fam": "More apps from Famiglia Vicino",
 "privacy": "Privacy Policy", "terms": "Terms of Service",
},
"de": {
 "title": "Leggii: Noten, Unterrichtsaufnahmen und KI-Notizen | Vicino Labs",
 "desc": "Leggii ist die Noten-App fürs Tablet: PDFs, Fotos und IMSLP-Ausgaben importieren, Unterricht und Proben aufnehmen, während die Noten mitblättern, und die KI fasst das Gesagte zusammen.",
 "kicker": "Vicino Labs · Famiglia Vicino",
 "h1": "Beim Lesen aufnehmen,<br>die KI schreibt mit",
 "lede": "Die Noten-App fürs Tablet. Beim Anhören blättern die Noten von selbst mit, und die KI notiert Korrekturen und Hausaufgaben mit Zeit und Seite.",
 "note": "Für iPad, iPhone sowie Android-Tablets und -Handys. Die Grundfunktionen sind kostenlos.",
 "feats": [
  (1, "Notenschrank", "Alle Noten an einem Ort", "PDFs importieren oder Papiernoten mit der Kamera abfotografieren – schiefe Fotos werden gerade gerichtet. Titel und Komponist werden erkannt.",
   ["Alle, zuletzt geöffnet oder nach Komponist", "Favoriten und Ordner", "Setlists für Konzert und Unterricht", "Verlag und Seite auf einen Blick"]),
  (2, "Notizen", "Schreiben wie mit dem Bleistift", "Stift, Textmarker, Radierer und Lasso zum Auswählen und Verschieben. Der Apple Pencil wird unterstützt.",
   ["Dynamik, Vorzeichen, Artikulation, Fingersatz", "Stempel für Wiederholungen, D.C. und mehr", "Ihre Notizen bleiben Seite für Seite erhalten"]),
  (3, "Aufnahme", "Aufnehmen – die Noten blättern mit", "Ein Tipp nimmt bei geöffneten Noten auf, auch bei ausgeschaltetem Bildschirm. Jedes Umblättern wird mitgespeichert, beim Anhören öffnet sich die richtige Seite von allein.",
   ["Unterricht und Proben, so wie sie waren", "Wiedergabe läuft auf anderen Seiten und im Hintergrund weiter", "Auf eine Stelle tippen und direkt dorthin springen"]),
  (4, "KI-Unterrichtsnotizen", "Das Gesagte nach Zeit und Seite", "Korrekturen, Kernpunkte und Hausaufgaben, sauber sortiert. Besonders hilfreich, wenn der Unterricht in einer Sprache stattfindet, die Sie noch lernen.",
   ["Unterrichtsnotizen: Korrekturen, Kernpunkte, Hausaufgaben", "Mitschrift Wort für Wort, mit Übersetzung", "Ergebnis als PDF speichern und darauf schreiben", "Läuft nur auf Ihren Wunsch und zeigt vorher die KI-Zeit"]),
  (6, "IMSLP", "Die passende Ausgabe wählen", "Werk suchen und nach Verlag, Textsprache, Bearbeiter und Vorschau auswählen. Sängerinnen und Sänger finden die richtige Sprachfassung, Korrepetitoren die gebrauchte Tonart.",
   ["Nach Verlag, Textsprache und Bearbeiter filtern", "Vorschau vor dem Laden", "Direkt in den Notenschrank"]),
  (7, "Zum Üben", "Metronom und Tastatur auf den Noten", "Beides schwebt über den Noten, statt sie zu verdecken – der Blick bleibt, wo er hingehört.",
   ["Zwei Seiten nebeneinander auf dem iPad im Querformat", "Nacht-, Sepia- und gedimmte Ansicht", "Blättern per Bluetooth-Pedal oder Tippen"]),
  (8, "Leggii fragen", "Einfach fragen", "„Wo sind meine Tosca-Noten?“ oder „Analysiere die Aufnahme von heute“ – Sie bekommen die Antwort samt Schaltfläche, die es erledigt.",
   ["Noten finden, Aufnahmen analysieren, Einstellungen öffnen", "Erklärt auch, wie die App funktioniert"]),
  (5, "welegato-ID und Cloud", "Gerät wechseln, alles behalten", "Mit der welegato-ID angemeldet begleiten Sie Pro und KI-Zeit auf jedes Gerät. Ohne Anmeldung funktionieren alle Grundfunktionen von Leggii.",
   ["Leggii Cloud (Plus): Noten, Notizen, Ordner, Setlists und Aufnahmen auf iPhone und iPad gleich", "Selten genutzte Noten nur in der Cloud behalten und Platz sparen", "Ohne Cloud bleiben Noten und Aufnahmen auf Ihrem Gerät"]),
  (9, "Famiglia Vicino", "Apps für den musikalischen Alltag", "Leggii gehört zur Familie der Musik-Apps von Vicino Labs. Sie suchen eine Lehrkraft oder Mitspielende? Schauen Sie bei welegato vorbei.",
   ["welegato: Musiklehrkräfte und Mitspielende finden", "Pianino · Appoggio · Prova · Chiave · Squillo"]),
 ],
  "sum_h": "Das kann Leggii",
 "sum_sub": "Acht Dinge. Drei davon zeigen wir weiter unten genauer.",
 "tiles": {1: "Aus PDFs, von der Kamera und aus IMSLP",
           2: "Stift, Textmarker, Musikstempel, Apple Pencil",
           3: "Das Umblättern wird mitgespeichert und beim Anhören blättern die Noten mit",
           4: "Korrekturen, Kernpunkte und Hausaufgaben nach Zeit und Seite",
           6: "Nach Verlag, Textsprache und Bearbeiter wählen",
           7: "Sie schweben über den Noten, statt sie zu verdecken",
           8: "Einfach fragen und die Antwort kommt samt Schaltfläche",
           5: "Pro, KI-Zeit und Cloud begleiten Sie auf jedes Gerät"},
 "ptab_cols": ["", "Kostenlos", "7 Tage testen", "Pro", "Plus"],
 "ptab": [("Noten, Notizen, Aufnahme, Metronom", "✓", "✓", "✓", "✓"),
          ("Alle Pro-Funktionen", "–", "✓", "✓", "✓"),
          ("welegato-Banner", "ja", "nein", "nein", "nein"),
          ("KI-Analyse im Monat", "–", "30 Min.", "30 Min.", "5 Std."),
          ("Leggii Cloud", "–", "–", "–", "10 GB · 50 GB"),
          ("Preis", "kostenlos", "kostenlos", "Einmalkauf", "ab 3,99 € im Monat")],
 "plans_h": "Tarife",
 "plans_sub": "Noten importieren, hineinschreiben, aufnehmen und das Metronom sind kostenlos. KI-Analyse und Cloud kosten Serverzeit – dafür sind die Tarife da.",
 "plans": [
  ("Kostenlos", "von Anfang an", ["Noten importieren und Kamera-Scan", "Notizen und Musikstempel", "Unterricht und Proben aufnehmen, mit Umblättern", "Metronom, Tastatur, IMSLP-Suche"]),
  ("7 Tage testen", "sofort", ["Alle Pro-Funktionen", "30 KI-Minuten", "Ohne Kreditkarte"]),
  ("Leggii Pro", "einmaliger Kauf", ["Alle Pro-Funktionen", "Kein welegato-Banner", "30 KI-Minuten im Monat", "60 Minuten Willkommensbonus"]),
  ("Leggii Plus", "ab 3,99 € im Monat", ["Alle Pro-Funktionen", "5 Std. KI im Monat", "Leggii Cloud 10 GB: 3,99 € im Monat, 39,99 € im Jahr", "50 GB: 5,99 € im Monat, 59,99 € im Jahr"]),
 ],
 "plans_note": "Den einmaligen Pro-Kauf und KI-Zeit zum Aufladen (5 und 15 Stunden, 12 Monate gültig) gibt es in der App. Die Preise unterscheiden sich je nach Land.",
 "plans_cta": "Plus hier abonnieren", "plans_cta_note": "Mit einer welegato-ID anmelden und per Karte zahlen. Derzeit für Europa.",
 "get_h": "Leggii laden",
 "get_p": "Im App Store für iPad und iPhone, bei Google Play für Android.",
 "fam": "Weitere Apps der Famiglia Vicino",
 "privacy": "Datenschutzerklärung", "terms": "Nutzungsbedingungen",
},
}


def _on(l):
    return " on" if l == "en" else ""


def _feat(l, i, num, kicker, head, body, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    flip = " flip" if i % 2 else ""
    return (f'<div data-l="{l}" class="feat{flip}{_on(l)}">'
            f'<div class="txt"><p class="kicker">{kicker}</p><h2>{head}</h2><p>{body}</p><ul>{lis}</ul></div>'
            f'<div><img class="shot" data-shot="d{num}" src="/leggii/shots/en/d{num}.webp" '
            f'alt="{head}" width="1200" height="936" loading="lazy" decoding="async"></div></div>')


def _plans(l, t):
    cards = "".join(
        f'<div class="plan"><h3>{n}</h3><p class="tagline">{tag}</p><ul>'
        + "".join(f"<li>{b}</li>" for b in bl) + "</ul></div>"
        for n, tag, bl in t["plans"])
    return (f'<div data-l="{l}" class="plans{_on(l)}"><h2>{t["plans_h"]}</h2>'
            f'<p class="sub">{t["plans_sub"]}</p><div class="cards">{cards}</div>'
            f'<p class="note" style="margin-top:18px">{t["plans_note"]}</p>'
            f'<p style="margin:22px 0 0"><a class="cta" href="/leggii/plus/">{t["plans_cta"]} →</a></p>'
            f'<p class="note" style="margin-top:8px">{t["plans_cta_note"]}</p></div>')


SCRIPT = """(function(){var META=__META__;var k="vl-app-lang",L=["ko","en","de"],s=null;
try{s=localStorage.getItem(k)}catch(e){}
var h=(location.hash||"").slice(1),n=(navigator.language||"en").slice(0,2),
l=L.indexOf(h)>=0?h:(L.indexOf(s)>=0?s:(L.indexOf(n)>=0?n:"en"));
function set(x){l=x;document.documentElement.lang=x;
document.querySelectorAll("[data-l]").forEach(function(e){e.classList.toggle("on",e.getAttribute("data-l")===x)});
document.querySelectorAll("[data-set]").forEach(function(b){b.classList.toggle("on",b.getAttribute("data-set")===x)});
document.querySelectorAll("[data-shot]").forEach(function(e){e.src="/leggii/shots/"+x+"/"+e.getAttribute("data-shot")+".webp"});
document.querySelectorAll("[data-hero]").forEach(function(e){e.src="/leggii/shots/"+x+"/hero.webp"});
if(META[x]){document.title=META[x][0];
var m=document.querySelector('meta[name="description"]');if(m)m.setAttribute("content",META[x][1]);
var ot=document.querySelector('meta[property="og:title"]');if(ot)ot.setAttribute("content",META[x][0]);
var od=document.querySelector('meta[property="og:description"]');if(od)od.setAttribute("content",META[x][1]);}
try{localStorage.setItem(k,x)}catch(e){}}
document.querySelectorAll("[data-set]").forEach(function(b){b.addEventListener("click",function(){set(b.getAttribute("data-set"))})});
set(l)})();"""


def _meta_json():
    """언어별 탭 제목과 설명 — 언어를 바꾸면 자바스크립트가 이걸로 바꾼다."""
    import json
    return json.dumps({l: [T[l]["title"], T[l]["desc"]] for l, _ in LANGS}, ensure_ascii=False)


def _tiles(l):
    t = T[l]
    out = []
    for num, kicker, head, body, bullets in t["feats"]:
        if num not in t["tiles"]:
            continue
        out.append(
            f'<div class="tile"><img data-shot="t{num}" src="/leggii/shots/en/t{num}.webp" '
            f'alt="{head}" width="720" height="540" loading="lazy" decoding="async">'
            f'<div class="tx"><h3>{head}</h3><p>{t["tiles"][num]}</p></div></div>')
    return (f'<div data-l="{l}" class="sum{_on(l)}"><h2>{t["sum_h"]}</h2>'
            f'<p class="sub">{t["sum_sub"]}</p><div class="tiles">{"".join(out)}</div></div>')


def _ptab(l):
    t = T[l]
    head = "".join(f"<th>{c}</th>" for c in t["ptab_cols"])
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in t["ptab"])
    return (f'<div data-l="{l}" class="plans{_on(l)}"><h2>{t["plans_h"]}</h2>'
            f'<p class="sub">{t["plans_sub"]}</p>'
            f'<div class="ptabwrap"><table class="ptab"><thead><tr>{head}</tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
            f'<p class="note" style="margin-top:16px">{t["plans_note"]}</p>'
            f'<p style="margin:20px 0 0"><a class="cta" href="/leggii/plus/">{t["plans_cta"]} →</a></p>'
            f'<p class="note" style="margin-top:8px">{t["plans_cta_note"]}</p></div>')


def _meta_json():
    """언어별 탭 제목과 설명 — 언어를 바꾸면 자바스크립트가 이걸로 바꾼다."""
    import json
    return json.dumps({l: [T[l]["title"], T[l]["desc"]] for l, _ in LANGS}, ensure_ascii=False)


# 크게 보여 줄 것 셋 — 남들이 못 하는 것(HQ·대표님 2026-11-17).
# 녹음하면 악보가 따라 넘어감 / AI가 레슨을 정리 / 기기끼리 맞춰짐.
DEEP = (3, 4, 5)


def page():
    buttons = "".join(f'<button type="button" data-set="{l}"{" class=on" if l == "en" else ""}>{n}</button>'
                      for l, n in LANGS)
    hero = "".join(
        f'<div data-l="{l}" class="hero{_on(l)}">'
        f'<img class="ic" src="/apps/leggii.png" srcset="/apps/hi/leggii.png 2x" alt="Leggii" width="92" height="92">'
        f'<p class="kicker">{T[l]["kicker"]}</p><h1>{T[l]["h1"]}</h1>'
        f'<p class="lede">{T[l]["lede"]}</p>'
        f'<div class="stores">{badge(l)}</div><p class="note">{T[l]["note"]}</p>'
        f'<img class="shotwide" data-hero="1" src="/leggii/shots/en/hero.webp" alt="Leggii" '
        f'width="1700" height="956" fetchpriority="high" decoding="async"></div>'
        for l, _ in LANGS)
    tiles = "".join(_tiles(l) for l, _ in LANGS)
    deep = "".join(
        "".join(_feat(l, i, *f) for i, f in enumerate(T[l]["feats"]) if f[0] in DEEP)
        for l, _ in LANGS)
    plans = "".join(_ptab(l) for l, _ in LANGS)
    get = "".join(
        f'<div data-l="{l}" class="getit{_on(l)}"><h2>{T[l]["get_h"]}</h2><p>{T[l]["get_p"]}</p>'
        f'<div class="stores">{badge(l)}</div>'
        f'<a class="fam" href="{"/famiglia/" if l == "de" else f"/{l}/famiglia/"}">{T[l]["fam"]} →</a></div>'
        for l, _ in LANGS)
    foot = "".join(
        f'<p data-l="{l}"{" class=on" if l == "en" else ""} style="margin:0">'
        f'<a href="/leggii/privacy/#{l}">{T[l]["privacy"]}</a>'
        f'<a href="/leggii/terms/#{l}">{T[l]["terms"]}</a>'
        f'<a href="/impressum/">Impressum</a>'
        f'<a href="mailto:{EMAIL}">{EMAIL}</a></p>' for l, _ in LANGS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{T["en"]["title"]}</title>
<meta name="description" content="{T["en"]["desc"]}">
<link rel="canonical" href="https://vicinolabs.com/leggii/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:title" content="{T["en"]["title"]}">
<meta property="og:description" content="{T["en"]["desc"]}">
<meta property="og:image" content="https://vicinolabs.com/leggii/shots/en/hero.webp">
<meta property="og:url" content="https://vicinolabs.com/leggii/"><meta property="og:type" content="website">
<link rel="stylesheet" href="/fonts/fonts-v2.css">
<style>{CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a>
<div class="langbar" role="group" aria-label="Language">{buttons}</div></div></div>
<main class="wrap">
{hero}
{tiles}
{deep}
{plans}
{get}
</main>
<footer><div class="wrap">{foot}<div style="margin-top:10px">© 2026 Vicino Labs</div></div></footer>
<script>{SCRIPT.replace("__META__", _meta_json())}</script>
</body></html>
"""
