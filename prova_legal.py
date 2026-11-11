"""프로바(Prova) 법적 문서 페이지 — vicinolabs.com/prova/, /prova/privacy/, /prova/terms/ (2026-11-07 초안).

chiave_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 prova_privacy_content.py / prova_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 운영자 승인 전 초안(아직 push하지 않음).
"""
import os

import app_home
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
    # 공통 틀 app_home.page (2026-11-11): 큰 아이콘·언어별 한 줄·공식 스토어 배지
    return app_home.page(key='prova', name='Prova · 프로바', sub="Vicino Labs · Famiglia Vicino", icon="/apps/prova.png",
                         ledes={'en': 'Record and film your lessons and practice, compare takes, check submission videos — AI analyses the sound.', 'de': 'Unterricht und Üben aufnehmen und filmen, Takes vergleichen, Bewerbungsvideos prüfen – die KI analysiert den Klang.', 'it': "Registra e filma lezioni e studio, confronta le take, controlla i video per audizioni – l'AI analizza il suono.", 'ko': '레슨과 연습을 녹음·녹화하고, 테이크를 비교하고, 제출 영상을 점검하세요 — AI는 소리를 분석합니다.'},
                         play=None, apple=None, email=EMAIL, desc='Prova — lesson and practice recording and filming with AI analysis, by Vicino Labs.', canonical="/prova/")


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
