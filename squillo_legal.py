"""스퀼로(Squillo) 법적 문서 페이지 — vicinolabs.com/squillo/, /squillo/privacy/, /squillo/terms/ (2026-11-26 초안).

chiave_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 squillo_privacy_content.py / squillo_terms_content.py. build.py가 실행한다.
아직 출시 전이라 스토어 배지 대신 "출시 예정". 본문은 운영자 승인 전 초안(페이지에 초안 표시).
/squillo/ 는 지원 페이지 역할(문의 메일, 방침·약관 링크).
"""
import os

import app_home
import nomio_legal
from appoggio_privacy_content import EMAIL
from squillo_privacy_content import PRIVACY
from squillo_terms_content import TERMS

SQUILLO = {
    "name": "Squillo",
    "home": "/squillo/",
    "mark": "S",
    "mark_bg": "#B4532F",  # 아이콘 테라코타
    "mark_img": "/squillo/icon.png",  # 아이콘 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "squillo-legal-lang",
}


def squillo_home():
    return app_home.page(key='squillo', name={'ko': '스퀼로(Squillo)', 'en': 'Squillo', 'de': 'Squillo', 'it': 'Squillo'}, sub="Vicino Labs · Famiglia Vicino", icon="/apps/squillo.png",
                         ledes={'en': 'Vocal warm-ups and studies for singers, with piano accompaniment set to your voice and concert pitch.',
                                'de': 'Einsingen und Etüden für Sängerinnen und Sänger, mit Klavierbegleitung passend zu Stimmlage und Kammerton.',
                                'it': 'Vocalizzi e studi per cantanti, con accompagnamento al pianoforte adatto al tuo registro e al diapason.',
                                'ko': '성악가를 위한 발성 연습과 연습곡. 내 성부와 기준음에 맞춘 피아노 반주로 연습합니다.'},
                         play=None, apple=None, email=EMAIL, desc='Squillo: vocal warm-ups and studies for singers, by Vicino Labs.', canonical="/squillo/")


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/squillo/", squillo_home())
    write("/squillo/privacy/", nomio_legal.legal_page("/squillo/privacy/", PRIVACY, "/squillo/terms/", app=SQUILLO))
    write("/squillo/terms/", nomio_legal.legal_page("/squillo/terms/", TERMS, "/squillo/privacy/", app=SQUILLO))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
