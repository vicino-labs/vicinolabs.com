"""프로바 소개 페이지 — vicinolabs.com/prova/ (2026-11-18).

예전에는 app_home.page() 로 찍던 얇은 카드였다. 대표님 지시로 렛지처럼
한 번 훑으면 앱이 무엇을 하는지 알 수 있는 페이지로 바꾼다.

아직 출시 전이다(iOS 심사 중, Play 내부 테스트). 스토어 배지는 STORES 가
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
# 오는 대로 세 번째로 넣는다.
DEEP = (4, 2)

CSS = leggii_site.CSS + """
.soon{display:inline-block;margin:26px 0 0;padding:9px 16px;border-radius:999px;
border:1px solid var(--line);background:var(--paper);color:var(--soft);font-size:14px}
.pri{max-width:980px;margin:52px auto 0;padding:24px 26px;border:1px solid var(--line);
border-radius:16px;background:var(--paper);display:grid;grid-template-columns:1fr 1fr;gap:26px}
@media(max-width:720px){.pri{grid-template-columns:1fr;gap:22px}}
.pri h2{font-size:clamp(19px,2vw,23px);margin:0 0 10px}
.pri p{margin:0;color:var(--soft);font-size:15.5px}
"""

T = {
"ko": {
 "title": "프로바: 연습 비교와 제출 영상, AI 연주 점검 | Vicino Labs",
 "desc": "같은 구간을 여러 번 녹음해 지난번과 나란히 견주고, 제출 영상을 찍어 점검합니다. AI가 음정·박자·템포·셈여림을 마디와 시간으로 짚어 줍니다.",
 "kicker": "VICINO LABS · FAMIGLIA VICINO",
 "h1": "AI가 내 연주를 듣고 짚어 줍니다",
 "lede": "같은 구간을 여러 번 녹음하면 1번째, 2번째로 번호가 붙고, 지난번과 나란히 틀어 봅니다. 제출 영상은 카메라로 찍어 보내기 전에 점검합니다.",
 "soon": "iOS 심사 중입니다. 안드로이드는 내부 테스트 중입니다.",
 "tiles": [
  ("레슨과 리허설", "선생님 시범과 지적, 지휘자의 지시까지 소리로 또는 영상으로"),
  ("AI 레슨 노트", "짚어 주신 곳, 칭찬, 숙제가 시간과 함께 적힙니다"),
  ("제출 영상", "오디션·콩쿠르 영상을 0.6·1·2배 줌으로 찍고 보내기 전에 점검합니다"),
  ("연습 녹음", "같은 구간을 여러 번 녹음하면 1번째, 2번째로 번호가 붙습니다"),
  ("두 녹음 비교", "지난번과 나란히 틀어 무엇이 달라졌는지 봅니다"),
  ("AI 연주 점검", "음정·박자·템포·음색·셈여림·프레이징을 마디와 시간으로"),
  ("녹음하는 동안", "안드로이드에서는 방해 금지를 켜고, 끝나면 되돌립니다"),
  ("내 성부와 기준음", "성부와 악기, 기준음을 정해 두면 AI가 그에 맞춰 봅니다")],
 "feats": [
  (3, "AI 레슨 노트", "레슨이 끝나면 적혀 있습니다",
   "한 시간 넘는 레슨은 앞부분부터 잊힙니다. 녹음해 두고 AI 분석을 누르면 선생님이 하신 말씀, 고쳐 주신 곳, 칭찬, 숙제가 시간 순서로 정리됩니다.",
   ["시간을 누르면 그 부분부터 다시 들립니다",
    "리허설에서는 지휘자와 코치의 지시만 역할별로 적습니다",
    "외국어로 받은 레슨도 적어 둡니다"]),
  (4, "연습 녹음", "지난번과 나란히 들어 봅니다",
   "같은 구간을 여러 번 녹음하면 1번째, 2번째로 번호가 붙습니다. 두 녹음을 나란히 틀면 무엇이 달라졌는지 귀로 바로 압니다.",
   ["곡과 구간별로 모여 있습니다",
    "파형 위의 점을 누르면 그 자리부터 들립니다"]),
  (2, "AI 연주 점검", "잘된 곳과 다듬을 곳을 짚습니다",
   "AI가 음정, 박자, 템포, 음색, 셈여림, 프레이징, 호흡, 발음을 마디와 시간으로 짚어 줍니다. 초록은 잘된 곳, 주황은 연습할 곳입니다.",
   ["성부와 기준음(440·442·443Hz)을 정해 두면 그에 맞춰 봅니다",
    "영상은 크게 보면서 그 자리의 메모를 함께 봅니다"])],
 "pri_h": "녹음은 이 기기에 남습니다",
 "pri_p": "녹음과 영상은 기기에 저장됩니다. AI 분석에는 소리만 보내고, 분석이 끝나면 지웁니다. 영상의 화면은 보내지 않습니다.",
 "con_h": "녹음하기 전에",
 "con_p": "레슨을 녹음할 때는 선생님과 함께 녹음되는 분들의 동의를 먼저 받아 주세요. 18세 미만이면 보호자의 동의도 필요합니다. 앱이 녹음을 시작하기 전에 확인합니다.",
 "get_h": "내려받기",
 "get_p": "녹음과 듣기, 비교는 로그인 없이 씁니다. AI 분석과 클라우드는 위레가토 아이디로 로그인해서 씁니다. 처음 로그인하시면 AI 30분이 7일 동안 열립니다.",
 "fam": "앱들이 함께 일하는 방법",
 "privacy": "개인정보처리방침", "terms": "이용약관",
},
"en": {
 "title": "Prova: compare your runs, film auditions, AI on your playing | Vicino Labs",
 "desc": "Record the same passage again and play it beside last time. Film the audition video and check it. The AI marks intonation, rhythm, tempo and dynamics by bar and by time.",
 "kicker": "VICINO LABS · FAMIGLIA VICINO",
 "h1": "The AI listens to your playing",
 "lede": "Record the same passage again and it is numbered Run 1, Run 2, then play two of them together. Film the audition video and check it before you send it.",
 "soon": "In review on iOS. In internal testing on Android.",
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
   ["Gathered by piece and by passage",
    "Tap a mark on the waveform and it plays from there"]),
  (2, "The AI listens to the playing", "What went well and what to work on",
   "The AI marks intonation, rhythm, tempo, tone, dynamics, phrasing, breathing and diction by bar and by time. Green went well, orange is to work on.",
   ["Set your part and your pitch (440, 442, 443 Hz) and it judges by that",
    "Watch the video large with the notes for that moment beside it"])],
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
 "soon": "Bei Apple in Prüfung. Bei Android im internen Test.",
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
   ["Nach Stück und Stelle gesammelt",
    "Auf eine Marke in der Wellenform tippen, und es läuft von dort"]),
  (2, "Die KI hört das Spiel", "Was gelungen ist und woran Sie arbeiten",
   "Die KI markiert Intonation, Rhythmus, Tempo, Klang, Dynamik, Phrasierung, Atem und Aussprache nach Takt und Zeit. Grün ist gelungen, Orange ist zum Üben.",
   ["Stimmlage und Kammerton (440, 442, 443 Hz) einstellen, danach urteilt sie",
    "Das Video groß ansehen, daneben die Notizen zu dieser Stelle"])],
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

SCRIPT = """(function(){var META=__META__;
var KEY="vl-app-lang",langs=["ko","en","de"];
function pick(){try{var s=localStorage.getItem(KEY);if(s&&langs.indexOf(s)>=0)return s}catch(e){}
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
try{localStorage.setItem(KEY,x)}catch(e){}}
document.addEventListener("click",function(e){var b=e.target.closest("[data-set]");
if(b){set(b.getAttribute("data-set"))}});
set(pick());})();"""


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


def _tiles(l):
    """요약 판: 여덟 칸, 글만.

    2026-11-18: 앞 네 칸에 아이폰 그림을 넣었다가 뺐다. 스토어 스크린샷의
    아이폰은 **기기 아래가 화면 밖으로 잘려 있어서**, 잘라 쓰면 폰이 중간에서
    뚝 끊겨 보인다(대표님 지적). 아이패드 그림은 아래까지 온전해서 깊이
    보는 세 장면에는 그대로 쓴다. 프로바 세션에 기기 테두리 없는 순수
    화면 캡처와 촬영 화면을 부탁해 두었다. 받으면 여기에 다시 넣는다.
    """
    cells = []
    for head, body in T[l]["tiles"]:
        cells.append(f'<div class="tile"><div class="tx"><h3>{head}</h3><p>{body}</p></div></div>')
    return (f'<section data-l="{l}" class="sum{_on(l)}">'
            f'<div class="tiles">{"".join(cells)}</div></section>')


def _feat(l, i, num, kicker, head, body, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    flip = " flip" if i % 2 else ""
    return (f'<section data-l="{l}" class="feat{flip}{_on(l)}">'
            f'<div class="tx"><p class="kicker">{kicker}</p><h2>{head}</h2>'
            f'<p>{body}</p><ul>{lis}</ul></div>'
            f'<div class="pic"><img class="shot" data-shot="d{num}" src="/prova/shots/en/d{num}.webp" '
            f'alt="{head}" width="1100" height="1447" loading="lazy" decoding="async"></div></section>')


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
    pri = "".join(
        f'<section data-l="{l}" class="pri{_on(l)}">'
        f'<div><h2>{T[l]["pri_h"]}</h2><p>{T[l]["pri_p"]}</p></div>'
        f'<div><h2>{T[l]["con_h"]}</h2><p>{T[l]["con_p"]}</p></div></section>'
        for l, _ in LANGS)
    get = "".join(
        f'<div data-l="{l}" class="getit{_on(l)}"><h2>{T[l]["get_h"]}</h2><p>{T[l]["get_p"]}</p>'
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
{pri}
{get}
</main>
<footer><div class="wrap">{foot}<div style="margin-top:10px">© 2026 Vicino Labs</div></div></footer>
<script>{SCRIPT.replace("__META__", _meta_json())}</script>
</body></html>
"""
