"""끼아베(Chiave) 법적 문서 페이지 — vicinolabs.com/chiave/, /chiave/privacy/, /chiave/terms/ (2026-11-06 게시).

leggii_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 chiave_privacy_content.py / chiave_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 2026-11-06 운영자 승인.
"""
import os

import app_home
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
    # 공통 틀 app_home.page (2026-11-11): 큰 아이콘·언어별 한 줄·공식 스토어 배지
    return app_home.page(key='chiave', name='Chiave · 끼아베', sub="Vicino Labs · Famiglia Vicino", icon="/apps/chiave.png",
                         ledes={'en': 'Create and edit scores with pen, photo or sound — transposition included. Your scores stay on your device.', 'de': 'Noten erstellen und bearbeiten – mit Stift, Foto oder Klang, Transponieren inklusive. Deine Noten bleiben auf deinem Gerät.', 'it': 'Crea e modifica spartiti con penna, foto o suono, trasposizione inclusa. I tuoi spartiti restano sul dispositivo.', 'ko': '펜·사진·소리로 악보를 쉽게 만들고 고치는 앱 — 이조도 함께, 악보는 기기에만.'},
                         play=None, apple=None, email=EMAIL, desc='Chiave — create and edit scores with pen, photo or sound, by Vicino Labs.', canonical="/chiave/")


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
