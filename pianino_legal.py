"""Pianino 법적 문서 페이지 — vicinolabs.com/pianino/, /pianino/privacy/, /pianino/terms/ (2026-11-07 초안).

leggii_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 pianino_privacy_content.py / pianino_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 운영자 승인 전 초안.
"""
import os

import app_home
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
    # 공통 틀 app_home.page (2026-11-11): 큰 아이콘·언어별 한 줄·공식 스토어 배지
    return app_home.page(key='pianino', name='Pianino · 피아니노', sub="Vicino Labs · Famiglia Vicino", icon="/apps/pianino.png",
                         ledes={'en': 'Piano, metronome and tuner — one concert pitch (A4 415–466 Hz) for keys and tuner, free.', 'de': 'Klavier, Metronom und Stimmgerät – ein Kammerton für Tasten und Stimmgerät, kostenlos.', 'it': 'Pianoforte, metronomo e accordatore: un unico diapason per tasti e accordatore, gratis.', 'ko': '피아노·메트로놈·튜너 — 건반과 튜너가 같은 기준음을 쓰는 무료 앱.'},
                         play='com.vicinolabs.pianino', apple='https://apps.apple.com/app/id6832363954', email=EMAIL, desc='Pianino — piano, metronome and tuner with one shared concert pitch, by Vicino Labs.', canonical="/pianino/")


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
