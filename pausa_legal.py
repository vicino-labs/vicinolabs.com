"""파우사(Pausa) 법적 문서 페이지: vicinolabs.com/pausa/, /pausa/privacy/, /pausa/terms/ (2026-11-12 초안).

prova_legal.py와 같은 틀(nomio_legal.legal_page, app_home.page). 한국어·영어·독일어·이탈리아어, #ko/#en/#de/#it.
본문은 pausa_privacy_content.py / pausa_terms_content.py. 운영자 승인 전 초안이며 시행일은 비워 둠.
아직 build.py에 연결하지 않았다(다른 세션 작업 중). 출시 전이라 스토어 링크 대신 "출시 예정".
아이콘 /pausa/icon.png 확정(2026-11-13). 위레가토 통합 아이디 로그인을 넣으면 두 문서를 반드시 고쳐야 한다.
"""
import os

import app_home
import nomio_legal
from appoggio_privacy_content import EMAIL
from pausa_privacy_content import PRIVACY
from pausa_terms_content import TERMS

PAUSA = {
    "name": "Pausa",
    "home": "/pausa/",
    "mark": "P",
    "mark_bg": "#3B2A20",  # 에스프레소
    "mark_img": "/pausa/icon.png",  # 최종 아이콘(2026-11-13) 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "pausa-legal-lang",
}


def pausa_home():
    return app_home.page(key='pausa', name='Pausa · 파우사', sub="Vicino Labs · Famiglia Vicino", icon="/apps/pausa.png",
                         ledes={'en': 'For the café, reading, desk work and bedtime: mix music with rain, fireplace, café murmur and wind into a sound of your own.',
                                'de': 'Fürs Café, zum Lesen, für die Arbeit am Schreibtisch und vor dem Schlafen: Musik mit Regen, Kaminfeuer, Cafégeräuschen und Wind zu deinem eigenen Klang mischen.',
                                'it': 'Per il bar, la lettura, il lavoro alla scrivania e la sera prima di dormire: mescola musica, pioggia, camino, brusio del caffè e vento nel tuo sottofondo.',
                                'ko': '카페에서, 책 읽을 때, 일할 때, 잠들기 전에. 음악에 빗소리, 장작불, 카페 소음, 바람을 섞어 나만의 소리를 만들어 보세요.'},
                         play=None, apple=None, email=EMAIL, desc='Pausa: soundscapes for the café, reading, desk work and bedtime, by Vicino Labs.', canonical="/pausa/")


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/pausa/", pausa_home())
    write("/pausa/privacy/", nomio_legal.legal_page("/pausa/privacy/", PRIVACY, "/pausa/terms/", app=PAUSA))
    write("/pausa/terms/", nomio_legal.legal_page("/pausa/terms/", TERMS, "/pausa/privacy/", app=PAUSA))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
