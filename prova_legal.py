"""프로바(Prova) 법적 문서 페이지 — vicinolabs.com/prova/, /prova/privacy/, /prova/terms/ (2026-11-07 초안).

chiave_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 prova_privacy_content.py / prova_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 운영자 승인 전 초안(아직 push하지 않음).
"""
import os

import nomio_legal
from appoggio_privacy_content import EMAIL
from prova_privacy_content import PRIVACY
from prova_terms_content import TERMS

PROVA = {
    "name": "Prova",
    "home": "/prova/",
    "mark": "P",
    "mark_bg": "#1B4590",  # 아이콘 로열 블루
    "mark_img": "/prova/icon.png",  # 최종 아이콘(2026-10-28) 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "prova-legal-lang",
}


def prova_home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prova — Vicino Labs</title>
<meta name="description" content="Prova — lesson and practice recording and filming with AI analysis, by Vicino Labs.">
<link rel="canonical" href="https://vicinolabs.com/prova/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{nomio_legal.CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="page"><div class="mast"><span class="app"><img class="mark" src="{PROVA['mark_img']}" alt="" width="30" height="30" style="background:none;border:none">Prova</span>
<h1>Prova · 프로바</h1>
<p class="lede">Record and film your lessons and practice, compare takes, check submission videos — AI analyses the sound.<br>
Unterricht und Üben aufnehmen und filmen, Takes vergleichen, Bewerbungsvideos prüfen – die KI analysiert den Klang.<br>
Registra e filma lezioni e studio, confronta le take, controlla i video per audizioni – l'AI analizza il suono.<br>
레슨과 연습을 녹음·녹화하고, 테이크를 비교하고, 제출 영상을 점검하세요 — AI는 소리를 분석합니다.</p></div>
<div style="padding:26px 0;max-width:720px">
<p>Google Play · App Store — coming soon · demnächst · prossimamente · 출시 예정</p>
<p>Privacy Policy · Datenschutzerklärung · Informativa privacy · 개인정보처리방침: <a href="/prova/privacy/">vicinolabs.com/prova/privacy</a><br>
Terms of Service · Nutzungsbedingungen · Termini · 이용약관: <a href="/prova/terms/">vicinolabs.com/prova/terms</a><br>
Impressum: <a href="/impressum/">vicinolabs.com/impressum</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></main>
</body></html>
"""


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/prova/", prova_home())
    write("/prova/privacy/", nomio_legal.legal_page("/prova/privacy/", PRIVACY, "/prova/terms/", app=PROVA))
    write("/prova/terms/", nomio_legal.legal_page("/prova/terms/", TERMS, "/prova/privacy/", app=PROVA))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
