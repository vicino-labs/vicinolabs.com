"""Caffè Vicino 법적 문서 페이지 — vicinolabs.com/caffevicino/, /caffevicino/privacy/, /caffevicino/terms/ (2026-11-12 초안).

pianino_legal.py와 같은 틀(nomio_legal.legal_page). 한국어·영어·독일어·이탈리아어,
#ko/#en/#de/#it. 본문은 caffevicino_privacy_content.py / caffevicino_terms_content.py. build.py가 실행한다.
Caffè Vicino는 앱이 아니라 유튜브 채널(@caffevicino)이라 스토어 배지 대신 유튜브 단추를 둔다
(app_home.page는 그대로 두고, 여기서 "출시 예정" 자리를 단추로 바꾼다). 본문은 운영자 승인 전 초안.
"""
import os

import app_home
import nomio_legal
from appoggio_privacy_content import EMAIL
from caffevicino_privacy_content import CHANNEL, PRIVACY
from caffevicino_terms_content import TERMS

CAFFEVICINO = {
    "name": "Caffè Vicino",
    "home": "/caffevicino/",
    "mark": "C",
    "mark_bg": "#2A1810",  # 아이콘 에스프레소 브라운
    "mark_img": "/caffevicino/icon.png",  # 최종 아이콘(2026-11-12) 120px
    "langs": [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")],
    "storage": "caffevicino-legal-lang",
}

YT_LABEL = {"ko": "유튜브에서 보기", "en": "Watch on YouTube", "de": "Auf YouTube ansehen", "it": "Guarda su YouTube"}
# 에스프레소 브라운 바탕에 금색 글씨(아이콘 색)
YT_CSS = (".ah .yt{display:inline-block;background:#2A1810;color:#F5CD78;border:1px solid #C78A36;border-radius:99px;"
          "padding:13px 26px;font-weight:600;font-size:15.5px;line-height:1.2;text-decoration:none}"
          ".ah .yt:hover{background:#3B2416}")


def caffevicino_home():
    # 공통 틀 app_home.page: 큰 아이콘·언어별 한 줄. 스토어가 없으므로 "출시 예정" 표시를 유튜브 단추로 바꾼다.
    html = app_home.page(key='caffevicino', name='Caffè Vicino', sub="Vicino Labs · YouTube", icon="/apps/caffevicino.png",
                         ledes={'en': 'Original music for cafés, focus and rest, by Vicino Labs.',
                                'de': 'Eigene Musik für Cafés, zum Konzentrieren und Entspannen, von Vicino Labs.',
                                'it': 'Musica originale per il caffè, la concentrazione e il riposo, di Vicino Labs.',
                                'ko': '카페와 집중, 휴식을 위한 창작 음악. Vicino Labs가 만듭니다.'},
                         email=EMAIL, desc='Caffè Vicino — original music for cafés, focus and rest, a YouTube channel by Vicino Labs.',
                         canonical="/caffevicino/")
    for l, _ in app_home.LANGS:
        soon = f'<span class="soon">Google Play · App Store — {app_home.SOON[l]}</span>'
        assert soon in html, l  # app_home.page가 바뀌면 여기서 알 수 있게
        html = html.replace(soon, f'<a class="yt" href="{CHANNEL}" target="_blank" rel="noopener">{YT_LABEL[l]} →</a>')
    return html.replace("</style>", YT_CSS + "</style>", 1)


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/caffevicino/", caffevicino_home())
    write("/caffevicino/privacy/", nomio_legal.legal_page("/caffevicino/privacy/", PRIVACY, "/caffevicino/terms/", app=CAFFEVICINO))
    write("/caffevicino/terms/", nomio_legal.legal_page("/caffevicino/terms/", TERMS, "/caffevicino/privacy/", app=CAFFEVICINO))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
