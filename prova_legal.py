"""프로바(Prova) 법적 문서 페이지 — vicinolabs.com/prova/, /prova/privacy/, /prova/terms/ (2026-11-07 초안).

chiave_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 prova_privacy_content.py / prova_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 링크 대신 "coming soon". 본문은 운영자 승인 전 초안(아직 push하지 않음).
"""
import os

import app_home
import nomio_legal
import prova_site
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
    # 2026-11-18: 얇은 카드(app_home.page) → 전용 소개 페이지(prova_site.py).
    # 대표님 지시 "렛지처럼 한 번에 무엇을 하는 앱인지 알게".
    return prova_site.page()


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
