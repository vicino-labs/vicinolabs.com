#!/usr/bin/env python3
"""렛지 제품 페이지 그림 만들기 (2026-11-17).

App Store 스크린샷(앱스토어/렛지/screenshots/<언어>/ipad/screenshot-N.png)에서
기기 화면 부분만 잘라 내고, 헤더 그림과 함께 webp로 줄여 /leggii/shots/ 에 둔다.
문구는 웹페이지가 HTML로 쓰므로 그림 위쪽의 제목 띠는 버린다.

한 번만 돌리면 된다: python3 leggii_shots.py
"""
import os
import subprocess
import sys

from PIL import Image

SRC = "/Users/jameslee/App/앱스토어/렛지"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leggii", "shots")
LANGS = ["en", "de", "ko"]
SHOTS = range(1, 10)
BOX = (278, 646, 1784, 2633)  # 기기 테두리 — 모든 장면이 같은 자리
WIDTH = 1100
TILE_W = 720          # 요약 판의 작은 그림
# 장면마다 4:3 으로 잘라 낼 자리(0 = 화면 위, 1 = 아래). 중요한 것이 담긴 높이가
# 장면마다 다르다 — 메트로놈·건반은 화면 아래, Famiglia 목록은 가운데쯤.
TILE_Y = {1: 0.0, 2: 0.92, 3: 1.0, 4: 0.02, 5: 0.10, 6: 0.0, 7: 1.0, 8: 0.22, 9: 0.45}
# 2·3 은 위를 자르면 똑같은 악보로 보인다. 아래를 보여 줘야 필기 도구와
# 재생 막대가 들어가 서로 다른 그림이 된다.


def webp(im, path, width, quality=80):
    im = im.convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, "WEBP", quality=quality, method=6)


def main():
    for lang in LANGS:
        for n in SHOTS:
            src = f"{SRC}/screenshots/{lang}/ipad/screenshot-{n}.png"
            if not os.path.exists(src):
                print("없음:", src, file=sys.stderr)
                continue
            full = Image.open(src).crop(BOX)
            webp(full, f"{OUT}/{lang}/{n}.webp", WIDTH)
            # 요약 판 타일 — 같은 화면에서 4:3 만큼만
            ch = round(full.width * 3 / 4)
            top = round((full.height - ch) * TILE_Y.get(n, 0.1))
            webp(full.crop((0, top, full.width, top + ch)), f"{OUT}/{lang}/t{n}.webp", TILE_W, 78)
        # 첫 그림(hero.webp)은 여기서 만들지 않는다 — leggii_hero.py 가 만든다.
        # 예전엔 스토어 헤더를 그대로 썼는데 2026-11-17 에 다시 만들었다.
    subprocess.run(["du", "-sh", OUT])
    print("ok")


if __name__ == "__main__":
    main()
