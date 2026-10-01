"""Appoggio 법적 문서 페이지 — vicinolabs.com/appoggio/privacy/, /appoggio/terms/ (2026-10-01).

예전 주소(vicino-labs.github.io/appoggio-privacy)에서 옮겼다. 페이지 틀·글꼴 원칙은
nomio_legal.py와 같다(외부 글꼴·스크립트 없음). 한 페이지에 한국어·영어·독일어·
이탈리아어가 다 있고 위쪽 단추로 바꾼다(#ko/#en/#de/#it, 앱이 언어에 맞춰 연다).
본문은 appoggio_privacy_content.py / appoggio_terms_content.py. build.py가 함께 실행한다.
"""
import os

import nomio_legal
from appoggio_privacy_content import PRIVACY, EMAIL
from appoggio_terms_content import TERMS

APPOGGIO = {
    "name": "Appoggio",
    "home": "/appoggio/",
    "mark": "a.",
    "mark_bg": "#224561",  # 로고 선 색(네이비)
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "appoggio-legal-lang",
}

# 아직 Play 비공개 테스트 중이라 공개 스토어 페이지가 없다(404) — 공개되면
# details?id=app.appoggio.voice 링크를 소개 페이지에 다시 넣는다.


def appoggio_home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Appoggio — Vicino Labs</title>
<meta name="description" content="Appoggio — breathing training for singers, by Vicino Labs.">
<link rel="canonical" href="https://vicinolabs.com/appoggio/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{nomio_legal.CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="page"><div class="mast"><span class="app"><span class="mark" style="background:{APPOGGIO['mark_bg']}">a.</span>Appoggio</span>
<h1>Appoggio</h1>
<p class="lede">Breathing training for singers — the bel canto art of supporting the voice with breath.<br>
Atemtraining für Sängerinnen und Sänger.<br>
L'arte del respiro: allenamento per cantanti.<br>
성악가를 위한 호흡 훈련 — 모든 기능 무료, 기록은 기기에만.</p></div>
<div style="padding:26px 0;max-width:720px">
<p>Privacy Policy · Datenschutzerklärung · Informativa privacy · 개인정보처리방침: <a href="/appoggio/privacy/">vicinolabs.com/appoggio/privacy</a><br>
Terms of Service · Nutzungsbedingungen · Termini · 이용약관: <a href="/appoggio/terms/">vicinolabs.com/appoggio/terms</a><br>
Impressum: <a href="/impressum/">vicinolabs.com/impressum</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></main>
</body></html>
"""


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/appoggio/", appoggio_home())
    write("/appoggio/privacy/", nomio_legal.legal_page("/appoggio/privacy/", PRIVACY, "/appoggio/terms/", app=APPOGGIO))
    write("/appoggio/terms/", nomio_legal.legal_page("/appoggio/terms/", TERMS, "/appoggio/privacy/", app=APPOGGIO))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
