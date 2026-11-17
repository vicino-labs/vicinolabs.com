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
HDR_WIDTH = 1700


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
            webp(Image.open(src).crop(BOX), f"{OUT}/{lang}/{n}.webp", WIDTH)
        hdr = f"{SRC}/header/{lang}/leggii-header-v1-{lang}.png"
        if os.path.exists(hdr):
            webp(Image.open(hdr), f"{OUT}/{lang}/hero.webp", HDR_WIDTH, 82)
    subprocess.run(["du", "-sh", OUT])
    print("ok")


if __name__ == "__main__":
    main()
