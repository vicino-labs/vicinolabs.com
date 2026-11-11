"""Appoggio 법적 문서 페이지 — vicinolabs.com/appoggio/privacy/, /appoggio/terms/ (2026-10-01).

예전 주소(vicino-labs.github.io/appoggio-privacy)에서 옮겼다. 페이지 틀·글꼴 원칙은
nomio_legal.py와 같다(외부 글꼴·스크립트 없음). 한 페이지에 한국어·영어·독일어·
이탈리아어가 다 있고 위쪽 단추로 바꾼다(#ko/#en/#de/#it, 앱이 언어에 맞춰 연다).
본문은 appoggio_privacy_content.py / appoggio_terms_content.py. build.py가 함께 실행한다.
"""
import os

import app_home
import nomio_legal
from appoggio_privacy_content import PRIVACY, EMAIL
from appoggio_terms_content import TERMS

APPOGGIO = {
    "name": "Appoggio",
    "home": "/appoggio/",
    "mark": "a.",
    "mark_bg": "#16233d",  # 앱 아이콘 미드나잇(2026-10-28 시리즈)
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "appoggio-legal-lang",
}

# 2026-10 조직 계정(Vicino Labs)에서 새 앱으로 공개 (예전 개인 계정 app.appoggio.voice는 게시 중단).
PLAY_URL = "https://play.google.com/store/apps/details?id=com.vicinolabs.appoggio"


def appoggio_home():
    # 공통 틀 app_home.page (2026-11-11): 큰 아이콘·언어별 한 줄·공식 스토어 배지
    return app_home.page(key='appoggio', name='Appoggio · 아뽀조', sub="Vicino Labs · Famiglia Vicino", icon="/apps/appoggio.png",
                         ledes={'en': 'Breathing training for singers — the bel canto art of supporting the voice with breath.', 'de': 'Atemtraining für Sängerinnen und Sänger.', 'it': "L'arte del respiro: allenamento per cantanti.", 'ko': '성악가를 위한 호흡 훈련 — 모든 기능 무료, 기록은 기기에만.'},
                         play='com.vicinolabs.appoggio', apple='https://apps.apple.com/app/id6832364161', email=EMAIL, desc='Appoggio — breathing training for singers, by Vicino Labs.', canonical="/appoggio/")


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/appoggio/", appoggio_home())
    write("/appoggio/privacy/", nomio_legal.legal_page("/appoggio/privacy/", PRIVACY, "/appoggio/terms/", app=APPOGGIO))
    write("/appoggio/terms/", nomio_legal.legal_page("/appoggio/terms/", TERMS, "/appoggio/privacy/", app=APPOGGIO))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
