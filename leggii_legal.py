"""Leggii(렛지 악보) 법적 문서 페이지 — vicinolabs.com/leggii/privacy/, /leggii/terms/ (2026-10-22).

appoggio_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 leggii_privacy_content.py / leggii_terms_content.py. build.py가 실행한다.
"""
import os

import app_home
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
    # 공통 틀 app_home.page (2026-11-11): 큰 아이콘·언어별 한 줄·공식 스토어 배지
    return app_home.page(key='leggii', name='Leggii · 렛지 악보', sub="Vicino Labs · Famiglia Vicino", icon="/apps/leggii.png",
                         ledes={'en': 'A simple sheet music reader for musicians — PDF scores, notes, IMSLP search, metronome, lesson recordings and AI lesson notes.', 'de': 'Die einfache Noten-App für Musikerinnen und Musiker – mit Unterrichtsaufnahmen und KI-Notizen.', 'it': 'Il leggio digitale semplice per musicisti, con registrazioni e note AI delle lezioni.', 'ko': '음악가를 위한 간편한 악보 앱 — 레슨 녹음과 AI 레슨 노트까지, 기본 기능 무료, 악보는 기기에만.'},
                         play='com.vicinolabs.leggii', apple='https://apps.apple.com/app/id6832925566', email=EMAIL, desc='Leggii — a simple sheet music reader for musicians, by Vicino Labs.', canonical="/leggii/")


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
