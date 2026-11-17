"""Leggii(렛지 악보) 법적 문서 페이지 — vicinolabs.com/leggii/privacy/, /leggii/terms/ (2026-10-22).

appoggio_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 leggii_privacy_content.py / leggii_terms_content.py. build.py가 실행한다.
"""
import os

import leggii_plus
import leggii_site
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
    # 2026-11-17: 카드형 소개 → 전용 제품 페이지(leggii_site.py). 기능마다 스크린샷.
    return leggii_site.page()


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/leggii/", leggii_home())
    # Plus 구독(홈페이지 직접 결제, 2026-11-17) — leggii_plus.py
    write("/leggii/plus/", leggii_plus.buy_page())
    write("/leggii/plus/danke/", leggii_plus.thanks_page())
    write("/leggii/privacy/", nomio_legal.legal_page("/leggii/privacy/", PRIVACY, "/leggii/terms/", app=LEGGII))
    write("/leggii/terms/", nomio_legal.legal_page("/leggii/terms/", TERMS, "/leggii/privacy/", app=LEGGII))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
