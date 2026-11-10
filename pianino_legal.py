"""Pianino 법적 문서 페이지 — vicinolabs.com/pianino/, /pianino/privacy/, /pianino/terms/ (2026-11-07 초안).

leggii_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 pianino_privacy_content.py / pianino_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 운영자 승인 전 초안.
"""
import os

import nomio_legal
from appoggio_privacy_content import EMAIL
from pianino_privacy_content import PRIVACY
from pianino_terms_content import TERMS

PIANINO = {
    "name": "Pianino",
    "home": "/pianino/",
    "mark": "P",
    "mark_bg": "#0F5A3C",  # 아이콘 에메랄드
    "mark_img": "/pianino/icon.png",  # 최종 아이콘(2026-11-07) 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "pianino-legal-lang",
}


def pianino_home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pianino — Vicino Labs</title>
<meta name="description" content="Pianino — piano, metronome and tuner with one shared concert pitch, by Vicino Labs.">
<link rel="canonical" href="https://vicinolabs.com/pianino/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{nomio_legal.CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="page"><div class="mast"><span class="app"><img class="mark" src="{PIANINO['mark_img']}" alt="" width="30" height="30" style="background:none;border:none">Pianino</span>
<h1>Pianino · 피아니노</h1>
<p class="lede">Piano, metronome and tuner — one concert pitch (A4 415–466 Hz) for keys and tuner, free.<br>
Klavier, Metronom und Stimmgerät – ein Kammerton für Tasten und Stimmgerät, kostenlos.<br>
Pianoforte, metronomo e accordatore: un unico diapason per tasti e accordatore, gratis.<br>
피아노·메트로놈·튜너 — 건반과 튜너가 같은 기준음을 쓰는 무료 앱.</p></div>
<div style="padding:26px 0;max-width:720px">
<p><a href="https://play.google.com/store/apps/details?id=com.vicinolabs.pianino" target="_blank" rel="noopener">Google Play →</a> · <a href="https://apps.apple.com/app/id6832363954" target="_blank" rel="noopener">App Store →</a></p>
<p>Privacy Policy · Datenschutzerklärung · Informativa privacy · 개인정보처리방침: <a href="/pianino/privacy/">vicinolabs.com/pianino/privacy</a><br>
Terms of Service · Nutzungsbedingungen · Termini · 이용약관: <a href="/pianino/terms/">vicinolabs.com/pianino/terms</a><br>
Impressum: <a href="/impressum/">vicinolabs.com/impressum</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></main>
</body></html>
"""


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/pianino/", pianino_home())
    write("/pianino/privacy/", nomio_legal.legal_page("/pianino/privacy/", PRIVACY, "/pianino/terms/", app=PIANINO))
    write("/pianino/terms/", nomio_legal.legal_page("/pianino/terms/", TERMS, "/pianino/privacy/", app=PIANINO))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
