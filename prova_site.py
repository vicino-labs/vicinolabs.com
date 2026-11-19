"""프로바 소개 페이지 — vicinolabs.com/prova/ (2026-11-18).

예전에는 app_home.page() 로 찍던 얇은 카드였다. 대표님 지시로 렛지처럼
한 번 훑으면 앱이 무엇을 하는지 알 수 있는 페이지로 바꾼다.

Play 는 2026-11-18 프로덕션으로 나갔고 iOS 는 심사 중이다. 스토어 배지는 STORES 가
True 가 될 때만 나온다. 출시하면 그 한 줄만 바꾸면 된다.

CSS 는 leggii_site 의 것을 그대로 쓴다. 같은 사이트의 같은 자리이고,
거기서 고친 것들(그림 height:auto, 한국어 줄바꿈, 문단으로 흐르게)이
여기에도 그대로 필요하다.

문구는 claude-handoff/문구지침.md 를 따랐다. 특히 '파는 자리' 규칙 —
우리 사정을 팔지 않고, 무료를 앞세우지 않고, 가능성이 아니라 장면으로.

  python3 prova_shots.py   # 그림(스토어 스크린샷에서 기기만 잘라낸다)
  python3 build.py
"""
import json

import leggii_site

EMAIL = "contact@vicinolabs.com"
LANGS = [("ko", "한국어"), ("en", "English"), ("de", "Deutsch")]

# 출시하면 True. 그때까지는 "곧 나옵니다" 한 줄만 보인다.
STORES = True
PLAY = "https://play.google.com/store/apps/details?id=com.vicinolabs.prova"
APPLE = ""   # 출시 때 App Store 주소

# 깊이 보는 장면은 **프로바에만 있는 것**으로 채운다(대표님 2026-11-18
# "그런 차별이 없으면 렛지만 사면 되지 프로바가 쓸모없어져").
# 레슨 녹음과 AI 레슨 노트는 렛지에도 있다. 그건 여덟 칸 요약에 두고
# 여기에는 연습 비교(4)와 AI 연주 점검(2)만 둔다. 촬영은 화면 그림이
# 오는 대로 넣는다.
#
# 9 는 그 둘 뒤에 붙는 "넓은 화면" 장면이다. 번호가 아니라 자리표다.
DEEP = (4, 2, 9)

# 장면마다 어떤 기기로 보여 줄지. **프로바는 폰으로 쓰는 앱이다**
# (대표님 2026-11-18 "프로바는 패드보단 휴대폰으로 많이 쓰겠지?").
# 레슨실에서 폰을 세워 두고 녹음하고, 입시 영상도 폰으로 찍는다.
# 렛지가 "태블릿 기본"인 것과 정반대 자리라, 셋 다 아이패드로 두면
# "이건 패드 앱인가" 로 읽힌다. 아이패드는 **거드는 자리** 하나만 둔다.
#   (파일이름, 덧붙일 class, 폭, 높이)
SHOT = {
    4: ("dp4", " ph", 617, 1308),
    2: ("dp2", " ph", 617, 1308),
    9: ("dwide", "", 1098, 1447),
}

# 요금 카드 CSS 는 렛지 것을 그대로 쓴다(leggii_site.PLANS_CSS).
CSS = leggii_site.CSS + leggii_site.PLANS_CSS + """
/* 요약 판: 그림이 있는 칸과 글만 있는 칸이 섞인다. 늘리지 않고 칸마다
   제 높이를 갖게 둔다. 안 그러면 글만 있는 칸이 같은 줄의 그림 칸 높이에
   맞춰 늘어나 아래가 500px 넘게 비어 보인다(2026-11-18). */
.tiles{align-items:start}
/* 요약 판에서 카드 테두리와 배경을 걷어낸다.
   카드 배경(--paper, 거의 흰색)과 페이지 배경(상아색)이 다르면, 색을 어디에
   칠하든 둘이 만나는 자리에 선이 생긴다. 그림 뒤를 페이지색으로 바꿨더니
   이번에는 카드 테두리가 그림 둘레를 두르는 선으로 보였다
   (대표님 2026-11-18 "바깥 라인도").
   그래서 상자를 아예 없앤다. 기기가 페이지 위에 바로 놓이므로 경계가 생길
   자리가 없다. 첫 화면과 깊이 보는 장면이 이미 그 모양이고 거기는 깔끔했다. */
.tile{background:none;border:0;border-radius:0;overflow:visible}
.tile img{background:none;border-bottom:0}
/* 히어로 폰에는 기기 둘레에 부드러운 그림자가 구워져 있다. 요약 판과 깊이
   보는 장면의 기기에도 같은 그림자를 준다. drop-shadow 는 그림의 투명한
   모서리를 따라가므로 둥근 테두리 모양 그대로 떨어진다(2026-11-18). */
.tile img,.feat .shot{filter:drop-shadow(0 10px 18px rgba(60,35,18,.28))}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .tile img,
  :root:not([data-theme="light"]) .feat .shot{filter:drop-shadow(0 10px 20px rgba(0,0,0,.55))}}
.tile .tx{padding:14px 2px 0}
/* 아래 줄: 거드는 설명들. 작게 두어 위의 장면들과 무게를 가른다.
   두 줄 사이를 벌린다. 30px 은 격자 줄 간격 16px 의 두 배도 안 돼서 여덟
   칸이 한 덩어리로 읽혔다(대표님 2026-11-18 "여기 줄이 너무 붙어있다").
   56px 은 이 페이지가 쓰는 간격 그대로다 — 요약 판 위가 56, 깊이 보는
   장면 안쪽이 58. 줄 간격(16)은 그대로 두고 아래 줄에만 위 여백을 준다.
   줄 간격을 키우면 폭이 좁아져 칸이 세 줄, 두 줄로 접힐 때 그 사이까지
   같이 벌어진다. 좁은 폭에서는 줄 간격이 10까지 내려가니 함께 줄인다. */
.tiles.more{margin-top:56px}
/* 글 칸 바로 밑에 구분선이 붙어 있었다(대표님 2026-11-18 "글 밑에 줄이 너무
   붙어있다"). 요약 판은 아래 여백이 0 인데 바로 다음 장면이 border-top 을
   달고 온다. 그래서 "보내기 전에 점검해요" 다음 줄이 곧장 선이었다.
   렛지에서는 마지막 줄이 테두리 있는 카드라 눈에 안 띄었다. 여기는 상자를
   걷어낸 글이라 선이 글에 달라붙는다. 선 아래가 58(장면 안쪽 여백)이니
   위도 그만큼 띄운다. */
.sum{padding-bottom:56px}
@media(max-width:1000px){.tiles.more{margin-top:40px}}
@media(max-width:720px){.tiles.more{margin-top:28px}}
.tiles.more .tx{padding:0 2px}
.tiles.more h3{font-size:16px}
html[lang=ko] .tiles.more h3{font-size:15px}
.tiles.more p{font-size:13.5px}
@media(max-width:720px){.tile .tx{padding:10px 2px 0}}
.soon{display:inline-block;margin:26px 0 0;padding:9px 16px;border-radius:999px;
border:1px solid var(--line);background:var(--paper);color:var(--soft);font-size:14px}
/* 깊이 보는 장면: 글과 그림의 높이 차이를 줄인다.
   반반(492:492)에 가운데 정렬이라 짧은 글 위아래가 206px 씩 비었다
   (대표님 2026-11-18 "여백"). 정렬만 바꾸면 빈자리가 위아래로 옮겨갈 뿐이라
   높이 차이 자체를 줄인다. 글 칸을 좁혀 자연스럽게 길어지게 하고(글줄
   길이도 같이 나아진다), 그림은 넓히되 높이를 눌러 둔다. */
.feat{grid-template-columns:minmax(0,0.78fr) minmax(0,1.22fr)}
.feat .pic{display:flex;justify-content:center}
/* 폭으로 누른다. 높이로 누르면서 width:auto 를 주면 그림의 비율 상자가
   사라져 불러오기 전 크기가 0x0 이 되고, 그러면 lazy 가 영영 안 걸린다
   (2026-11-18 에 그렇게 만들었다가 그림이 아예 안 나왔다). */
.feat .shot{width:100%;height:auto;max-width:370px}
/* 폰은 세로로 길다(2.12:1). 아이패드와 같은 폭을 주면 높이가 780px 이 넘어
   글(약 350px)과 다시 벌어진다. 폰만 더 좁게 눌러 높이를 맞춘다.
   240 이면 높이 508: 글이 330~361 이니 위아래가 74~89 로 남는다. */
.feat .shot.ph{max-width:240px}
/* 좌우 번갈아 놓기. 렛지 CSS 의 .flip 은 .txt 를 집는데 이 페이지의 글 칸은
   .tx 라 여태 걸리지 않았다(가운데 장면도 그림이 오른쪽에 있었다).
   칸 너비도 함께 뒤집어야 글 칸이 넓어지지 않는다. */
.feat.flip{grid-template-columns:minmax(0,1.22fr) minmax(0,0.78fr)}
.feat.flip .tx{order:2}
@media(max-width:820px){.feat{grid-template-columns:1fr}
.feat .shot{max-width:460px}
.feat .shot.ph{max-width:300px}}

.pri{max-width:980px;margin:52px auto 0;padding:24px 26px;border:1px solid var(--line);
border-radius:16px;background:var(--paper);display:grid;grid-template-columns:1fr 1fr;gap:26px}
@media(max-width:720px){.pri{grid-template-columns:1fr;gap:22px}}
.pri h2{font-size:clamp(19px,2vw,23px);margin:0 0 10px}
.pri p{margin:0;color:var(--soft);font-size:15.5px}
"""

T = {
"ko": {
 # 사람이 하는 일은 **"함께 틀다/듣다"** 다(대표님 2026-11-18 "지난번 녹음과
 # 함께 들어보세요, 두 녹음을 함께 틀면"). "나란히"는 옆에 놓는다는 말이라
 # 기능을 가리킬 때는 맞지만 동작 자리에서는 틀리다. 영어와 독일어는 이미
 # side by side / nebeneinander(이름)와 play together / zusammen abspielen
 # (동작)으로 나눠 쓰고 있었고 한국어만 한 말로 뭉개고 있었다. 한국어에서
 # 기능을 가리키는 말은 칸 이름 "두 녹음 비교"이니 본문에 "나란히"는 없다.
 #
 # "지난번"만 쓰지 않고 "지난번 녹음"으로 쓴다. 무엇과 견주는지 분명해진다.
 # 권하는 자리는 ~어요가 아니라 ~세요다("들어보세요").
 #
 # 말투는 **앱을 따른다**(대표님 2026-11-18 "주로 학생들이 많을 것 같으니
 # 어요~체로 바꾸면? 좀 친근한 모드로"). 프로바 앱 한국어 문자열은 ~어요가
 # 133개, ~습니다가 21개(거의 오류 메시지)다. 사이트에서 읽고 앱을 받았는데
 # 말투가 바뀌면 어긋난다. 약관과 방침은 그대로 ~습니다다.
 "title": "프로바: 연습 비교와 제출 영상, AI 연주 점검 | Vicino Labs",
 "desc": "같은 구간을 여러 번 녹음해 지난번 녹음과 함께 들어보고, 제출 영상은 보내기 전에 점검해요. AI가 음정·박자·템포·셈여림을 마디와 시간으로 짚어 줘요.",
 "kicker": "VICINO LABS · FAMIGLIA VICINO",
 "h1": "AI가 내 연주를 듣고 짚어 줘요",
 "lede": "같은 구간을 여러 번 녹음하면 1번째, 2번째로 번호가 붙어요. 지난번 녹음과 함께 들어보세요. 제출 영상은 카메라로 찍어 두고 보내기 전에 점검해요.",
 "soon": "iOS는 심사 중이에요. 안드로이드는 Google Play에서 받으세요.",
 "tiles": [
  ("레슨과 리허설", "선생님 시범과 지적, 지휘자의 지시까지 소리로 또는 영상으로"),
  ("AI 레슨 노트", "짚어 주신 곳, 칭찬, 숙제가 시간과 함께 적혀요"),
  ("제출 영상", "오디션·콩쿠르 영상을 0.6·1·2배 줌으로 찍고 보내기 전에 점검해요"),
  ("연습 녹음", "같은 구간을 여러 번 녹음하면 1번째, 2번째로 번호가 붙어요"),
  ("두 녹음 비교", "지난번 녹음과 함께 틀어 무엇이 달라졌는지 봐요"),
  ("AI 연주 점검", "음정·박자·템포·음색·셈여림·프레이징을 마디와 시간으로"),
  ("녹음하는 동안", "안드로이드에서는 방해 금지를 켜고, 끝나면 되돌려요"),
  ("내 성부와 기준음", "성부와 악기, 기준음을 정해 두면 AI가 그 기준으로 들어요")],
 "feats": [
  (3, "AI 레슨 노트", "레슨이 끝나면 벌써 적혀 있어요",
   "한 시간 넘는 레슨은 앞부분부터 잊혀요. 녹음해 두고 AI 분석을 누르면 선생님이 하신 말씀, 고쳐 주신 곳, 칭찬, 숙제가 시간 순서로 정리돼요.",
   ["시간을 누르면 그 부분부터 다시 들려요",
    "리허설에서는 지휘자와 코치의 지시만 역할별로 적어요",
    "외국어로 받은 레슨도 적어 둬요"]),
  (4, "연습 녹음", "지난번 녹음과 함께 들어보세요",
   "같은 구간을 여러 번 녹음하면 1번째, 2번째로 번호가 붙어요. 두 녹음을 함께 틀면 무엇이 달라졌는지 귀로 바로 알아요.",
   ["같은 곡·구간에 녹음이 둘 이상 쌓이면 비교 탭이 열려요",
    "곡과 구간별로 모여 있어요",
    "별표를 달아 두면 중요한 녹음만 모아 봐요",
    "파형 위의 점을 누르면 그 자리부터 들려요"]),
  (2, "AI 연주 점검", "잘된 곳과 다듬을 곳을 짚어 줘요",
   "AI가 음정, 박자, 템포, 음색, 셈여림, 프레이징, 호흡, 발음을 마디와 시간으로 짚어 줘요. 초록은 잘된 곳, 주황은 연습할 곳이에요.",
   ["성부와 기준음(440·442·443Hz)을 정해 두면 그 기준으로 들어요",
    "쓰는 시간을 미리 알려 주고, 분석이 실패하면 깎지 않아요",
    "영상은 크게 보면서 그 자리의 메모를 함께 봐요"]),
  (9, "넓은 화면", "아이패드에서는 양쪽으로 펼쳐 봐요",
   "녹음은 폰으로 해요. 레슨실에 들고 가는 것도, 입시 영상을 찍는 것도 폰이에요. 집에 와서 아이패드로 열면 왼쪽에 목록, 오른쪽에 열린 녹음이 놓여요.",
   ["보관함이 곡과 구간별로 묶여요",
    "파형 위에 AI가 짚은 자리가 점으로 떠요. 누르면 그 자리부터 들려요",
    "펼친 폴더블 폰도 같아요. 접으면 보던 녹음이 그대로 남아요"])],
 # 요금제 (2026-11-19). 값은 두 스토어와 같다(HQ 확정 2026-11-12).
 # 월 AI 분 수는 서버 leggii_ai_config.monthly_minutes_prova 의 sub=600 을
 # 그대로 옮긴 것이다. 10GB 와 50GB 의 AI 시간은 같고 클라우드만 다르다.
 "cards": [
  ('무료', '', '@free', '', ['녹음과 녹화', '듣고 두 녹음 함께 틀기', '곡과 구간별 보관함'], '로그인 없이 써요'),
  ('Plus', '구독 · 2개월 무료', '@p10m', '@p10y', ['+ 무료의 모든 기능', 'AI 레슨 노트와 AI 연주 점검 매월 10시간', '클라우드 10GB'], '@p10mo'),
  ('Plus 50GB', '영상이 쌓이면', '@p50m', '@p50y', ['+ Plus의 모든 기능', '클라우드 50GB', 'AI 시간은 10시간으로 같아요'], '@p50mo')],
 "trial": '위레가토 아이디로 처음 로그인하면 AI 30분을 7일 동안 무료로 써 보실 수 있어요',
 "plans_h": "요금제",
 "plans_sub": "녹음과 녹화, 듣기와 비교는 로그인 없이 써요. Plus는 AI와 클라우드예요.",
 "plans_value": "매월 AI 10시간은 한 시간짜리 레슨 열 번 분량이에요. 클라우드 10GB에는 녹음이 100시간 넘게 들어가요. 영상은 자리를 많이 차지해서, 영상이 많으면 50GB가 편해요.",
 "plans_punch": "레슨 한 번 값이면 Plus를 일 년 써요.",
 "plans_cta": "여기서 바로 시작하기",
 "pri_h": "녹음은 이 기기에 남아요",
 "pri_p": "녹음과 영상은 기기에 저장돼요. AI 분석에는 소리만 보내고, 분석이 끝나면 지워요. 영상의 화면은 보내지 않아요.",
 "con_h": "녹음하기 전에",
 "con_p": "레슨을 녹음할 때는 선생님과 함께 녹음되는 분들의 동의를 먼저 받아 주세요. 18세 미만이면 보호자 동의도 필요해요. 앱이 녹음을 시작하기 전에 확인해요.",
 "get_h": "내려받기",
 "get_p": "녹음과 듣기, 비교는 로그인 없이 써요. AI 분석과 클라우드는 위레가토 아이디로 로그인해서 써요. 처음 로그인하면 AI 30분을 7일 동안 무료로 드려요.",
 "fam": "앱들이 함께 일하는 방법",
 "privacy": "개인정보처리방침", "terms": "이용약관",
},
"en": {
 "title": "Prova: compare your runs, film auditions, AI on your playing | Vicino Labs",
 "desc": "Record the same passage again and play it beside last time. Film the audition video and check it. The AI marks intonation, rhythm, tempo and dynamics by bar and by time.",
 "kicker": "VICINO LABS · FAMIGLIA VICINO",
 "h1": "The AI listens to your playing",
 "lede": "Record the same passage again and it is numbered Run 1, Run 2, then play two of them together. Film the audition video and check it before you send it.",
 "soon": "In review on iOS. On Android, get it on Google Play.",
 "tiles": [
  ("Lessons and rehearsals", "What your teacher plays and corrects, and what the conductor asks for, in sound or on video"),
  ("AI lesson notes", "The corrections, the praise and the homework, each with its time"),
  ("Audition videos", "Film at 0.6×, 1× or 2× and check the video before you send it"),
  ("Practice runs", "Record the same passage again and it is numbered: Run 1, Run 2"),
  ("Two runs side by side", "Play them together and hear what changed"),
  ("AI listens to the playing", "Intonation, rhythm, tempo, tone, dynamics and phrasing, by bar and by time"),
  ("While you record", "On Android it turns on Do Not Disturb and puts it back afterwards"),
  ("Your part and your pitch", "Set the voice or instrument and the reference pitch and the AI judges by that")],
 "feats": [
  (3, "AI lesson notes", "The lesson ends and it is already written up",
   "An hour of teaching fades from the beginning. Record it, press analyse, and what your teacher said, corrected and praised, and the homework, are in the order they came.",
   ["Tap a time and that passage plays again",
    "In a rehearsal it lists only what the conductor or coach said, by role",
    "A lesson in another language is written down too"]),
  (4, "Practice runs", "Hear last time and this time together",
   "Record the same passage again and it is numbered: Run 1, Run 2. Play two of them together and your ear tells you what changed.",
   ["Two or more takes of a piece and passage, and the compare tab opens",
    "Gathered by piece and by passage",
    "Star the ones that matter and see only those",
    "Tap a mark on the waveform and it plays from there"]),
  (2, "The AI listens to the playing", "What went well and what to work on",
   "The AI marks intonation, rhythm, tempo, tone, dynamics, phrasing, breathing and diction by bar and by time. Green went well, orange is to work on.",
   ["Set your part and your pitch (440, 442, 443 Hz) and it judges by that",
    "It tells you the minutes before it starts, and charges nothing if it fails",
    "Watch the video large with the notes for that moment beside it"]),
  (9, "A wide screen", "On an iPad it opens out to both sides",
   "The recording happens on the phone. The phone is what goes to the lesson, and what films the audition. Open it on the iPad at home and the list sits on the left, the take on the right.",
   ["The library groups takes by piece and by passage",
    "The AI's marks sit as dots above the waveform; tap one and it plays from there",
    "An unfolded foldable is the same. Fold it shut and the open take stays"])],
 "cards": [
  ('Free', '', '@free', '', ['Recording and video', 'Playing two recordings together', 'Library by piece and passage'], 'No account needed'),
  ('Plus', 'Subscription · 2 months free', '@p10m', '@p10y', ['+ Everything in Free', 'AI lesson notes and AI performance check, 10 hours a month', '10 GB cloud'], '@p10mo'),
  ('Plus 50 GB', 'When the videos pile up', '@p50m', '@p50y', ['+ Everything in Plus', '50 GB cloud', 'The same 10 hours of AI'], '@p50mo')],
 "trial": 'Your first sign-in with a welegato ID opens 30 AI minutes for seven days',
 "plans_h": "Plans",
 "plans_sub": "Recording, filming, listening and comparing need no account. Plus is the AI and the cloud.",
 "plans_value": "Ten hours of AI a month is ten one-hour lessons. 10 GB holds over a hundred hours of recordings. Video fills it much faster, so 50 GB is the easier one if you film a lot.",
 "plans_punch": "A year of Plus costs about one lesson.",
 "plans_cta": "Get Plus",
 "pri_h": "The recordings stay on your device",
 "pri_p": "Recordings and videos are kept on the device. Only the sound goes out for the AI analysis, and it is deleted when the analysis is done. The picture never leaves the device.",
 "con_h": "Before you record",
 "con_p": "Ask the teacher, and everyone else who will be recorded, before you record a lesson. For anyone under 18 a parent has to agree as well. Prova asks you to confirm this before it starts.",
 "get_h": "Get Prova",
 "get_p": "Recording, listening and comparing need no account. The AI analysis and the cloud work when you sign in with your welegato ID. Your first sign-in opens 30 AI minutes for seven days.",
 "fam": "How the apps work together",
 "privacy": "Privacy", "terms": "Terms",
},
"de": {
 "title": "Prova: Durchläufe vergleichen, Videos prüfen, KI zum Spiel | Vicino Labs",
 "desc": "Dieselbe Stelle noch einmal aufnehmen und neben die letzte legen. Das Bewerbungsvideo filmen und prüfen. Die KI markiert Intonation, Rhythmus, Tempo und Dynamik nach Takt und Zeit.",
 "kicker": "VICINO LABS · FAMIGLIA VICINO",
 "h1": "Die KI hört Ihr Spiel",
 "lede": "Dieselbe Stelle noch einmal aufnehmen, Durchlauf 1, Durchlauf 2, und beide zusammen abspielen. Das Bewerbungsvideo filmen und vor dem Abschicken prüfen.",
 "soon": "Bei Apple in Prüfung. Für Android bei Google Play.",
 "tiles": [
  ("Unterricht und Proben", "Was die Lehrkraft vormacht und korrigiert und was der Dirigent verlangt, als Ton oder Video"),
  ("KI-Notizen zur Stunde", "Korrekturen, Lob und Hausaufgaben, jeweils mit der Zeit"),
  ("Bewerbungsvideos", "Mit 0,6×, 1× oder 2× filmen und das Video vor dem Abschicken prüfen"),
  ("Übe-Aufnahmen", "Dieselbe Stelle noch einmal, und sie wird nummeriert: Durchlauf 1, Durchlauf 2"),
  ("Zwei Aufnahmen nebeneinander", "Zusammen abspielen und hören, was sich geändert hat"),
  ("Die KI hört das Spiel", "Intonation, Rhythmus, Tempo, Klang, Dynamik und Phrasierung, nach Takt und Zeit"),
  ("Während der Aufnahme", "Unter Android wird „Nicht stören“ eingeschaltet und danach zurückgestellt"),
  ("Ihre Stimme, Ihr Kammerton", "Stimmlage oder Instrument und Kammerton einstellen, danach urteilt die KI")],
 "feats": [
  (3, "KI-Notizen zur Stunde", "Die Stunde ist vorbei und steht schon da",
   "Nach einer Stunde Unterricht verblasst der Anfang zuerst. Nehmen Sie auf, tippen Sie auf Analysieren, und was gesagt, korrigiert und gelobt wurde und was aufgegeben ist, steht in der Reihenfolge da, in der es kam.",
   ["Ein Tippen auf die Zeit, und die Stelle läuft wieder",
    "Bei einer Probe steht nur, was Dirigent oder Coach gesagt hat, nach Rolle",
    "Auch eine Stunde in einer anderen Sprache wird mitgeschrieben"]),
  (4, "Übe-Aufnahmen", "Das letzte Mal und dieses Mal zusammen hören",
   "Dieselbe Stelle noch einmal aufnehmen, und sie wird nummeriert: Durchlauf 1, Durchlauf 2. Zwei Aufnahmen zusammen abspielen, und das Ohr merkt sofort, was sich geändert hat.",
   ["Zwei Aufnahmen zu Stück und Stelle, und der Vergleich öffnet sich",
    "Nach Stück und Stelle gesammelt",
    "Wichtige mit einem Stern markieren und nur diese sehen",
    "Auf eine Marke in der Wellenform tippen, und es läuft von dort"]),
  (2, "Die KI hört das Spiel", "Was gelungen ist und woran Sie arbeiten",
   "Die KI markiert Intonation, Rhythmus, Tempo, Klang, Dynamik, Phrasierung, Atem und Aussprache nach Takt und Zeit. Grün ist gelungen, Orange ist zum Üben.",
   ["Stimmlage und Kammerton (440, 442, 443 Hz) einstellen, danach urteilt sie",
    "Die Minuten stehen vorher da, und bei einem Fehlschlag wird nichts abgezogen",
    "Das Video groß ansehen, daneben die Notizen zu dieser Stelle"]),
  (9, "Großer Bildschirm", "Auf dem iPad klappt es nach beiden Seiten auf",
   "Aufgenommen wird mit dem Telefon. Das Telefon geht mit in die Stunde, und es filmt das Vorspiel. Zu Hause auf dem iPad geöffnet, steht links die Liste und rechts die offene Aufnahme.",
   ["Das Archiv gruppiert nach Stück und Stelle",
    "Die Marken der KI sitzen als Punkte über der Wellenform; ein Tippen, und es läuft von dort",
    "Ein aufgeklapptes Foldable genauso. Zugeklappt bleibt die offene Aufnahme stehen"])],
 "cards": [
  ('Gratis', '', '@free', '', ['Aufnehmen und filmen', 'Zwei Aufnahmen zusammen abspielen', 'Archiv nach Stück und Stelle'], 'Ohne Konto'),
  ('Plus', 'Abo · 2 Monate geschenkt', '@p10m', '@p10y', ['+ Alles aus Gratis', 'KI-Unterrichtsnotizen und KI-Spielanalyse, 10 Stunden im Monat', '10 GB Cloud'], '@p10mo'),
  ('Plus 50 GB', 'Wenn die Videos sich häufen', '@p50m', '@p50y', ['+ Alles aus Plus', '50 GB Cloud', 'Dieselben 10 KI-Stunden'], '@p50mo')],
 "trial": 'Die erste Anmeldung mit der welegato-ID öffnet 30 KI-Minuten für sieben Tage',
 "plans_h": "Tarife",
 "plans_sub": "Aufnehmen, filmen, anhören und vergleichen brauchen kein Konto. Plus sind die KI und die Cloud.",
 "plans_value": "Zehn KI-Stunden im Monat sind zehn Unterrichtsstunden. In 10 GB passen über hundert Stunden Aufnahmen. Videos füllen sie viel schneller. Wer viel filmt, fährt mit 50 GB leichter.",
 "plans_punch": "Ein Jahr Plus kostet so viel wie eine Unterrichtsstunde.",
 "plans_cta": "Plus starten",
 "pri_h": "Die Aufnahmen bleiben auf Ihrem Gerät",
 "pri_p": "Aufnahmen und Videos liegen auf dem Gerät. Für die KI-Analyse geht nur der Ton hinaus, und er wird nach der Analyse gelöscht. Das Bild verlässt das Gerät nicht.",
 "con_h": "Vor der Aufnahme",
 "con_p": "Holen Sie vor einer Aufnahme in der Stunde das Einverständnis der Lehrkraft und aller ein, die mit aufgenommen werden. Bei unter 18-Jährigen muss auch ein Elternteil einverstanden sein. Prova fragt vor dem Start danach.",
 "get_h": "Prova laden",
 "get_p": "Aufnehmen, Anhören und Vergleichen brauchen kein Konto. Die KI-Analyse und die Cloud nutzen Sie mit Ihrer welegato-ID. Die erste Anmeldung öffnet 30 KI-Minuten für sieben Tage.",
 "fam": "Wie die Apps zusammenarbeiten",
 "privacy": "Datenschutz", "terms": "Nutzungsbedingungen",
},
}

SCRIPT = """(function(){var META=__META__,PRICE=__REGION__;
/* 값은 읽는 말이 아니라 사는 곳이 정한다. 시간대로 어림잡는다.
   틀려도 스토어에 들어가면 맞는 값이 보이고, 그 줄도 적어 두었다. */
function region(){try{var z=Intl.DateTimeFormat().resolvedOptions().timeZone||"";
if(z==="Asia/Seoul")return "kr";
if(/^Europe\\//.test(z))return ["Europe/Moscow","Europe/Istanbul","Europe/Kyiv","Europe/Kiev",
"Europe/Minsk","Europe/Simferopol","Europe/Volgograd","Europe/Samara","Europe/Saratov",
"Europe/Astrakhan","Europe/Ulyanovsk","Europe/Kirov"].indexOf(z)<0?"eu":"xx";
if(["Atlantic/Reykjavik","Atlantic/Canary","Atlantic/Madeira","Atlantic/Azores","Atlantic/Faroe"].indexOf(z)>=0)return "eu";
return "xx"}catch(e){return "xx"}}
var RG=region();
var KEY="vl-app-lang",langs=["ko","en","de"];
/* 차례: 주소 뒤의 #ko/#en/#de → 전에 고른 언어 → 브라우저 언어.
   회사 사이트에서 읽던 언어가 주소에 실려 온다. 브라우저가 한국어라도
   독일어로 읽고 있었다면 독일어가 맞다(대표님 2026-11-19). */
function pick(){var h=(location.hash||"").slice(1);
if(langs.indexOf(h)>=0)return h;
try{var s=localStorage.getItem(KEY);if(s&&langs.indexOf(s)>=0)return s}catch(e){}
var l=(navigator.languages||[navigator.language||"en"]);
for(var i=0;i<l.length;i++){var c=String(l[i]).toLowerCase().split("-")[0];
if(langs.indexOf(c)>=0)return c}return "en"}
function set(x){var m=META[x]||META.en;
document.documentElement.lang=x;
document.title=m.t;
var d=document.querySelector('meta[name=description]');if(d)d.content=m.d;
var ot=document.querySelector('meta[property="og:title"]');if(ot)ot.content=m.t;
var od=document.querySelector('meta[property="og:description"]');if(od)od.content=m.d;
document.querySelectorAll("[data-l]").forEach(function(e){e.classList.toggle("on",e.getAttribute("data-l")===x)});
document.querySelectorAll("[data-set]").forEach(function(b){b.classList.toggle("on",b.getAttribute("data-set")===x)});
/* 화면 그림도 그 언어로 */
document.querySelectorAll("[data-hero]").forEach(function(e){e.src="/prova/shots/"+x+"/hero.webp"});
document.querySelectorAll("[data-shot]").forEach(function(e){e.src="/prova/shots/"+x+"/"+e.getAttribute("data-shot")+".webp"});
document.querySelectorAll("[data-tile]").forEach(function(e){e.src="/prova/shots/"+x+"/"+e.getAttribute("data-tile")+".webp"});
var pp=(PRICE[x]||{})[RG];
if(pp){document.querySelectorAll("[data-pp]").forEach(function(e){e.textContent=pp[+e.getAttribute("data-pp")]||""});
document.querySelectorAll("[data-pricenote]").forEach(function(e){e.textContent=pp[6]});
document.querySelectorAll("[data-pricecta]").forEach(function(e){e.textContent=pp[8]})}
try{localStorage.setItem(KEY,x)}catch(e){}}
document.addEventListener("click",function(e){var b=e.target.closest("[data-set]");
if(b){set(b.getAttribute("data-set"))}});
set(pick());})();"""



# 가격은 읽는 말이 아니라 사는 곳이 정한다(렛지 페이지와 같은 규칙,
# 대표님 2026-11-17). 유럽에 사는 한국인 음악가가 우리 핵심 고객이라
# 언어로 고르면 그 사람에게 한국 값이 보인다. 시간대로 지역을 어림잡고,
# 모르는 지역에는 값을 적지 않는다. 틀린 값보다 안 적는 게 낫다.
#
# 자리: (10GB 큰 값, 10GB 작은 값, 10GB 아래 줄, 50GB 큰 값, 50GB 작은 값,
#        50GB 아래 줄, 값 설명 한 줄)
# 큰 값은 연간을 열두 달로 나눈 값이다(49,99/12 = 4,17). 연간을 앞에
# 세우는 것은 렛지에서 정한 방식이다(2026-11-19).
REGION = {
 "ko": {
  "eu": ("월 4,17 €", "연 49,99 €, 1년에 한 번 결제", "월간은 월 4,99 €",
         "월 5,83 €", "연 69,99 €, 1년에 한 번 결제", "월간은 월 6,99 €",
         "값은 스토어와 같아요. 여기서 바로 결제하셔도 되고, 앱 스토어·구글 플레이에서 구독하셔도 돼요."),
  "kr": ("월 5,750원", "연 69,000원, 1년에 한 번 결제", "월간은 월 6,900원",
         "월 8,250원", "연 99,000원, 1년에 한 번 결제", "월간은 월 9,900원",
         "한국 가격이에요. 결제는 앱 스토어·구글 플레이에서 해요."),
  "xx": ("스토어에서 구독", "", "", "스토어에서 구독", "", "",
         "나라마다 값이 달라서 스토어에서 확인하실 수 있어요."),
 },
 "en": {
  "eu": ("€4.17/mo", "€49.99 billed once a year", "or €4.99/mo billed monthly",
         "€5.83/mo", "€69.99 billed once a year", "or €6.99/mo billed monthly",
         "The same price as in the stores. Pay here, or subscribe on the App Store or Google Play."),
  "kr": ("₩5,750/mo", "₩69,000 billed once a year", "or ₩6,900/mo billed monthly",
         "₩8,250/mo", "₩99,000 billed once a year", "or ₩9,900/mo billed monthly",
         "Prices for Korea. You pay in the App Store or on Google Play."),
  "xx": ("In the store", "", "", "In the store", "", "",
         "Prices differ by country, and the store shows yours."),
 },
 "de": {
  "eu": ("4,17 €/Monat", "49,99 € einmal im Jahr", "oder 4,99 €/Monat bei monatlicher Zahlung",
         "5,83 €/Monat", "69,99 € einmal im Jahr", "oder 6,99 €/Monat bei monatlicher Zahlung",
         "Derselbe Preis wie in den Stores. Sie können hier zahlen oder im App Store bzw. bei Google Play abonnieren."),
  "kr": ("5.750 ₩/Monat", "69.000 ₩ einmal im Jahr", "oder 6.900 ₩/Monat bei monatlicher Zahlung",
         "8.250 ₩/Monat", "99.000 ₩ einmal im Jahr", "oder 9.900 ₩/Monat bei monatlicher Zahlung",
         "Preise für Korea. Bezahlt wird im App Store oder bei Google Play."),
  "xx": ("Im Store", "", "", "Im Store", "", "",
         "Die Preise unterscheiden sich je nach Land, der Store zeigt Ihren."),
 },
}
PRICE_SLOT = {"@p10m": 0, "@p10y": 1, "@p10mo": 2, "@p50m": 3, "@p50y": 4, "@p50mo": 5,
              "@free": 7}

# 7번 자리: 무료 칸의 값. 유럽에서 "0원"이 "월 4,17 €" 옆에 서면
# 어긋나 보여서 이것도 지역에 맞춘다.
# 8번 자리: 단추 아래 줄. 홈페이지 결제는 유럽만이라 지역마다 달라야 한다.
# 유럽 밖에서 단추를 눌렀다가 "유럽에서만 받아요"를 보는 것보다 먼저 아는 게 낫다.
CTA_NOTE = {
 "ko": {"eu": "위레가토 아이디로 가입하고 카드로 결제해요.",
        "kr": "홈페이지 결제는 유럽에서만 돼요. 한국에서는 위 값으로 앱 스토어·구글 플레이에서 구독해 주세요.",
        "xx": "홈페이지 결제는 지금 유럽에서만 돼요. 다른 곳에서는 앱 스토어·구글 플레이에서 구독해 주세요."},
 "en": {"eu": "Sign up with a welegato ID and pay by card.",
        "kr": "Website payment is for Europe only. In Korea please subscribe on the App Store or Google Play at the prices above.",
        "xx": "Website payment is for Europe at the moment. Elsewhere please subscribe on the App Store or Google Play."},
 "de": {"eu": "Mit einer welegato-ID anmelden und per Karte zahlen.",
        "kr": "Über die Webseite zahlen geht nur in Europa. In Korea bitte im App Store oder bei Google Play zu den Preisen oben abonnieren.",
        "xx": "Über die Webseite zahlen geht derzeit nur in Europa. Sonst bitte im App Store oder bei Google Play abonnieren."},
}

FREE = {"ko": {"eu": "0 €", "kr": "0원", "xx": "무료"}, "en": {"eu": "€0", "kr": "₩0", "xx": "Free"}, "de": {"eu": "0 €", "kr": "0 ₩", "xx": "Kostenlos"}}
for _l, _rs in REGION.items():
    for _rg in _rs:
        _rs[_rg] = _rs[_rg] + (FREE[_l][_rg], CTA_NOTE[_l][_rg])



def _plans(l):
    """요금제 카드 셋. 값은 자바스크립트가 지역에 맞게 채운다."""
    t = T[l]
    out = []
    for i, (name, tag, pr, pr2, bullets, foot) in enumerate(t["cards"]):
        def cell(v, cls):
            if v in PRICE_SLOT:
                return f'<div class="{cls}" data-pp="{PRICE_SLOT[v]}"></div>'
            return f'<div class="{cls}">{v}</div>' if v else f'<div class="{cls}"></div>'
        lis = "".join(f'<li class="up">{b}</li>' if b.startswith("+ ") else f"<li>{b}</li>"
                      for b in bullets)
        out.append(f'<div class="pcard{" hi" if i == 1 else ""}"><h3>{name}</h3>'
                   f'<div class="tag">{tag}</div>'
                   + cell(pr, "pr") + cell(pr2, "pr2")
                   + f"<ul>{lis}</ul>"
                   + (cell(foot, "foot") if foot else "")
                   + "</div>")
    return (f'<section data-l="{l}" class="plans{_on(l)}"><h2>{t["plans_h"]}</h2>'
            f'<p class="sub">{t["plans_sub"]}</p>'
            f'<div class="pcards">{"".join(out)}</div>'
            f'<p class="note trial">{t["trial"]}</p>'
            f'<p class="value">{t["plans_value"]}</p>'
            f'<p class="punch">{t["plans_punch"]}</p>'
            f'<p class="note" style="margin-top:10px" data-pricenote></p>'
            f'<p style="margin:20px 0 0"><a class="cta" href="/prova/plus/">{t["plans_cta"]} \u2192</a></p>'
            f'<p class="note" style="margin-top:10px" data-pricecta></p></section>')


def _on(l):
    return " on" if l == "en" else ""


def _meta_json():
    return json.dumps({l: {"t": T[l]["title"], "d": T[l]["desc"]} for l, _ in LANGS},
                      ensure_ascii=False)


def _stores(l):
    """스토어 배지. 렛지 페이지와 같은 그림·크기를 쓴다.

    App Store 는 아직 심사 중이라 APPLE 이 비어 있고, 그동안은 Play 만
    나온다. 승인되면 APPLE 에 번호만 넣으면 배지가 하나 더 붙는다.
    """
    if not STORES:
        return f'<p class="soon">{T[l]["soon"]}</p>'
    b = l if l in ("ko", "de", "en") else "en"
    out = [f'<a href="{PLAY}&amp;hl={l}" target="_blank" rel="noopener" aria-label="Google Play">'
           f'<img src="/badges/google-play-{b}-nb.png" alt="Google Play" width="162" height="48" '
           f'style="height:48px;width:auto;border-radius:10px;border:1px solid #a6a6a6;box-sizing:border-box"></a>']
    if APPLE:
        out.append(f'<a href="https://apps.apple.com/app/id{APPLE}" target="_blank" rel="noopener" aria-label="App Store">'
                   f'<img src="/badges/app-store-{b}.svg" alt="App Store" width="144" height="48" style="height:48px;width:auto"></a>')
    return '<div class="stores">' + "".join(out) + "</div>"


# 요약 판 칸마다 어느 화면 그림을 붙일지. 칸 차례(0부터)에 맞춘다.
# 아이폰 스토어 그림: 1 홈 · 2 AI 연주 점검 · 3 AI 레슨 노트 · 4 두 녹음 비교
#                    5 보관함(다크, 기기가 아래로 잘려 있어 안 쓴다) · 6 Famiglia
# "제출 영상"(2번 칸)과 "연습 녹음"(3번 칸)은 아직 맞는 그림이 없다.
# 프로바 세션에 촬영 화면을 부탁해 두었고, 오면 여기에 넣는다.
TILE_IMG = {0: 1, 1: 3, 4: 4, 5: 2}


def _tiles(l):
    """요약 판. 그림 있는 칸과 글만 있는 칸을 **따로 묶는다**.

    2026-11-18: 한 격자에 섞었더니 같은 줄에서 한쪽은 594px, 한쪽은 98px 이라
    옆이 휑하게 비었다(대표님 "제출영상, 연습녹음은 왜저래?"). 늘리면 아래가
    500px 비고 안 늘리면 옆이 빈다. 섞은 것 자체가 원인이라 나눈다.

    아래 줄에 남는 것들은 성격도 다르다. "녹음하는 동안", "내 성부와 기준음"은
    거드는 설명이지 보여 줄 장면이 아니다. 작게 두는 편이 글의 무게에도 맞다.
    촬영 화면이 오면 "제출 영상"이 위로 올라간다.
    """
    big, small = [], []
    for i, (head, body) in enumerate(T[l]["tiles"]):
        n = TILE_IMG.get(i)
        if n:
            big.append(f'<div class="tile">'
                       f'<img class="shot" data-tile="t{n}" src="/prova/shots/en/t{n}.webp" '
                       f'alt="" width="517" height="1097" loading="lazy" decoding="async">'
                       f'<div class="tx"><h3>{head}</h3><p>{body}</p></div></div>')
        else:
            small.append(f'<div class="tile"><div class="tx"><h3>{head}</h3><p>{body}</p></div></div>')
    return (f'<section data-l="{l}" class="sum{_on(l)}">'
            f'<div class="tiles">{"".join(big)}</div>'
            f'<div class="tiles more">{"".join(small)}</div></section>')


def _shot(num, head):
    name, cls, w, h = SHOT[num]
    return (f'<img class="shot{cls}" data-shot="{name}" src="/prova/shots/en/{name}.webp" '
            f'alt="{head}" width="{w}" height="{h}" loading="lazy" decoding="async">')


def _feat(l, i, num, kicker, head, body, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    flip = " flip" if i % 2 else ""
    return (f'<section data-l="{l}" class="feat{flip}{_on(l)}">'
            f'<div class="tx"><p class="kicker">{kicker}</p><h2>{head}</h2>'
            f'<p>{body}</p><ul>{lis}</ul></div>'
            f'<div class="pic">{_shot(num, head)}</div></section>')


def page():
    buttons = "".join(f'<button type="button" data-set="{l}"{" class=on" if l == "en" else ""}>{n}</button>'
                      for l, n in LANGS)
    hero = "".join(
        f'<div data-l="{l}" class="hero{_on(l)}">'
        f'<img class="ic" src="/apps/prova.png" srcset="/apps/hi/prova.png 2x" alt="Prova" width="92" height="92">'
        f'<p class="kicker">{T[l]["kicker"]}</p><h1>{T[l]["h1"]}</h1>'
        f'<p class="lede">{T[l]["lede"]}</p>'
        f'{_stores(l)}'
        f'<img class="shotwide" data-hero="1" src="/prova/shots/en/hero.webp" alt="Prova" '
        f'width="1680" height="1120" fetchpriority="high" decoding="async"></div>'
        for l, _ in LANGS)
    tiles = "".join(_tiles(l) for l, _ in LANGS)
    deep = "".join(
        "".join(_feat(l, i, *f)
                for i, f in enumerate(x for x in T[l]["feats"] if x[0] in DEEP))
        for l, _ in LANGS)
    plans = "".join(_plans(l) for l, _ in LANGS)
    pri = "".join(
        f'<section data-l="{l}" class="pri{_on(l)}">'
        f'<div><h2>{T[l]["pri_h"]}</h2><p>{T[l]["pri_p"]}</p></div>'
        f'<div><h2>{T[l]["con_h"]}</h2><p>{T[l]["con_p"]}</p></div></section>'
        for l, _ in LANGS)
    get = "".join(
        # 제목을 빼 둔다. 바로 아래 스토어 배지가 "여기서 받으세요"라는
        # 뜻이라 "내려받기"를 또 적으면 같은 말을 두 번 한다
        # (대표님 2026-11-18 "없어도 배지 있으니 다 알지").
        f'<div data-l="{l}" class="getit{_on(l)}"><p>{T[l]["get_p"]}</p>'
        f'{_stores(l)}'
        f'<a class="fam" href="{"/famiglia/" if l == "de" else f"/{l}/famiglia/"}">{T[l]["fam"]} →</a></div>'
        for l, _ in LANGS)
    foot = "".join(
        f'<p data-l="{l}"{" class=on" if l == "en" else ""} style="margin:0">'
        f'<a href="/prova/privacy/#{l}">{T[l]["privacy"]}</a>'
        f'<a href="/prova/terms/#{l}">{T[l]["terms"]}</a>'
        f'<a href="/impressum/">Impressum</a>'
        f'<a href="mailto:{EMAIL}">{EMAIL}</a></p>' for l, _ in LANGS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{T["en"]["title"]}</title>
<meta name="description" content="{T["en"]["desc"]}">
<link rel="canonical" href="https://vicinolabs.com/prova/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:title" content="{T["en"]["title"]}">
<meta property="og:description" content="{T["en"]["desc"]}">
<meta property="og:image" content="https://vicinolabs.com/prova/shots/en/hero.webp">
<meta property="og:url" content="https://vicinolabs.com/prova/"><meta property="og:type" content="website">
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
{pri}
{get}
</main>
<footer><div class="wrap">{foot}<div style="margin-top:10px">© 2026 Vicino Labs</div></div></footer>
<script>{SCRIPT.replace("__META__", _meta_json()).replace("__REGION__", json.dumps(REGION, ensure_ascii=False))}</script>
</body></html>
"""
