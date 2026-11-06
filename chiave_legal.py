"""끼아베(Chiave) 법적 문서 페이지 — vicinolabs.com/chiave/, /chiave/privacy/, /chiave/terms/ (2026-11-06 게시).

leggii_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 chiave_privacy_content.py / chiave_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 2026-11-06 운영자 승인.
"""
import os

import nomio_legal
from appoggio_privacy_content import EMAIL
from chiave_privacy_content import PRIVACY
from chiave_terms_content import TERMS

CHIAVE = {
    "name": "Chiave",
    "home": "/chiave/",
    "mark": "C",
    "mark_bg": "#5A2F57",  # 아이콘 플럼
    "mark_img": "/chiave/icon.png",  # 최종 아이콘(2026-10-28) 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "chiave-legal-lang",
}


def chiave_home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chiave — Vicino Labs</title>
<meta name="description" content="Chiave — write, scan and transpose scores, by Vicino Labs.">
<link rel="canonical" href="https://vicinolabs.com/chiave/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{nomio_legal.CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="page"><div class="mast"><span class="app"><img class="mark" src="{CHIAVE['mark_img']}" alt="" width="30" height="30" style="background:none;border:none">Chiave</span>
<h1>Chiave · 끼아베</h1>
<p class="lede">Write, scan and transpose scores — your scores stay on your device.<br>
Noten schreiben, scannen und transponieren – deine Noten bleiben auf deinem Gerät.<br>
Scrivi, scansiona e trasponi spartiti: i tuoi spartiti restano sul dispositivo.<br>
악보를 쓰고, 스캔하고, 이조하는 앱 — 악보는 기기에만.</p></div>
<div style="padding:26px 0;max-width:720px">
<p>Google Play · App Store — coming soon · demnächst · prossimamente · 출시 예정</p>
<p>Privacy Policy · Datenschutzerklärung · Informativa privacy · 개인정보처리방침: <a href="/chiave/privacy/">vicinolabs.com/chiave/privacy</a><br>
Terms of Service · Nutzungsbedingungen · Termini · 이용약관: <a href="/chiave/terms/">vicinolabs.com/chiave/terms</a><br>
Impressum: <a href="/impressum/">vicinolabs.com/impressum</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></main>
</body></html>
"""


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/chiave/", chiave_home())
    write("/chiave/privacy/", nomio_legal.legal_page("/chiave/privacy/", PRIVACY, "/chiave/terms/", app=CHIAVE))
    write("/chiave/terms/", nomio_legal.legal_page("/chiave/terms/", TERMS, "/chiave/privacy/", app=CHIAVE))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
