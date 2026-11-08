"""Leggii(렛지 악보) 법적 문서 페이지 — vicinolabs.com/leggii/privacy/, /leggii/terms/ (2026-10-22).

appoggio_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 leggii_privacy_content.py / leggii_terms_content.py. build.py가 실행한다.
"""
import os

import nomio_legal
from appoggio_privacy_content import EMAIL
from leggii_privacy_content import PRIVACY
from leggii_terms_content import TERMS

LEGGII = {
    "name": "Leggii",
    "home": "/leggii/",
    "mark": "L",
    "mark_bg": "#2a2c30",  # 아이콘 차콜
    "mark_img": "/leggii/icon.png",  # 최종 아이콘(올리브, 2026-11-08) 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "leggii-legal-lang",
}

PLAY_URL = "https://play.google.com/store/apps/details?id=com.vicinolabs.leggii"


def leggii_home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Leggii — Vicino Labs</title>
<meta name="description" content="Leggii — a simple sheet music reader for musicians, by Vicino Labs.">
<link rel="canonical" href="https://vicinolabs.com/leggii/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{nomio_legal.CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="page"><div class="mast"><span class="app"><img class="mark" src="{LEGGII['mark_img']}" alt="" width="30" height="30" style="background:none;border:none">Leggii</span>
<h1>Leggii · 렛지 악보</h1>
<p class="lede">A simple sheet music reader for musicians — PDF scores, notes, IMSLP search, metronome, lesson recordings and AI lesson notes.<br>
Die einfache Noten-App für Musikerinnen und Musiker – mit Unterrichtsaufnahmen und KI-Notizen.<br>
Il leggio digitale semplice per musicisti, con registrazioni e note AI delle lezioni.<br>
음악가를 위한 간편한 악보 앱 — 레슨 녹음과 AI 레슨 노트까지, 기본 기능 무료, 악보는 기기에만.</p></div>
<div style="padding:26px 0;max-width:720px">
<p><a href="{PLAY_URL}" target="_blank" rel="noopener">Google Play →</a></p>
<p>Privacy Policy · Datenschutzerklärung · Informativa privacy · 개인정보처리방침: <a href="/leggii/privacy/">vicinolabs.com/leggii/privacy</a><br>
Terms of Service · Nutzungsbedingungen · Termini · 이용약관: <a href="/leggii/terms/">vicinolabs.com/leggii/terms</a><br>
Impressum: <a href="/impressum/">vicinolabs.com/impressum</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></main>
</body></html>
"""


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/leggii/", leggii_home())
    write("/leggii/privacy/", nomio_legal.legal_page("/leggii/privacy/", PRIVACY, "/leggii/terms/", app=LEGGII))
    write("/leggii/terms/", nomio_legal.legal_page("/leggii/terms/", TERMS, "/leggii/privacy/", app=LEGGII))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
