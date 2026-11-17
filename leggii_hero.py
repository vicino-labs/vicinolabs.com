#!/usr/bin/env python3
"""렛지 제품 페이지 첫 그림(hero) 만들기 — 2026-11-17 (대표님 지시로 다시 만듦).

예전 그림의 문제: 아이패드 앱이라고 써 놓고 그림엔 아이폰만 셋, 가장 중요한
악보 화면이 가장 작게 잘려 있었고, 그림 안에 로고와 제목이 또 들어 있었다.

새 모양
  * 아이패드 가로 화면을 크게. 악보 두 쪽이 펼쳐진 모습이 주인공.
  * 아이폰 한 대만 곁들인다("태블릿도 휴대폰도 된다"는 그림 하나로 충분).
  * 그림 안에 글자를 넣지 않는다. 제목은 페이지가 말한다.
  * 기기 바닥이 잘리지 않게 다 보이도록.

재료는 렛지 저장소의 골든 이미지(기기 틀 없는 순수 화면):
  test_screenshots/goldens/ipad/<lang>-3.png    2752×2064  가로, 악보 두 쪽 + 녹음
  test_screenshots/goldens/iphone/<lang>-1.png  1320×2868  세로, 악보함

python3 leggii_hero.py 로 다시 만든다.
"""
import os

from PIL import Image, ImageDraw, ImageFilter

GOLD = "/Users/jameslee/App/leggii/test_screenshots/goldens"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leggii", "shots")
LANGS = ("ko", "en", "de")

W, H = 2400, 1350
BG = (245, 240, 232)          # 사이트 바탕 --bg
GLOW = (253, 250, 245)        # 가운데를 아주 살짝 밝게
FRAME = (28, 26, 24)          # 기기 테두리
EDGE = (62, 58, 54)           # 테두리 안쪽 얇은 선

PAD_W, PAD_BEZEL, PAD_R = 1560, 26, 42       # 아이패드 전체 너비·테·모서리
PHONE_W, PHONE_BEZEL, PHONE_R = 372, 17, 40  # 아이폰


def shadow(size, box, radius, blur, alpha, offset):
    """기기 아래에 깔 부드러운 그림자."""
    lay = Image.new("L", size, 0)
    d = ImageDraw.Draw(lay)
    x0, y0, x1, y1 = box
    d.rounded_rectangle((x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]),
                        radius=radius, fill=alpha)
    return lay.filter(ImageFilter.GaussianBlur(blur))


def device(canvas, shot, box, bezel, radius):
    """기기 하나를 그린다 — 테두리, 화면, 모서리 둥글리기."""
    x0, y0, x1, y1 = box
    sh = shadow(canvas.size, box, radius, blur=46, alpha=72, offset=(0, 26))
    canvas.paste(Image.new("RGB", canvas.size, (92, 72, 52)), (0, 0), sh)

    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle(box, radius=radius, fill=FRAME)
    d.rounded_rectangle(box, radius=radius, outline=EDGE, width=2)

    sx0, sy0 = x0 + bezel, y0 + bezel
    sw, sh_ = (x1 - x0) - 2 * bezel, (y1 - y0) - 2 * bezel
    screen = shot.convert("RGB").resize((sw, sh_), Image.LANCZOS)
    mask = Image.new("L", (sw, sh_), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, sw - 1, sh_ - 1), radius=max(radius - bezel, 8), fill=255)
    canvas.paste(screen, (sx0, sy0), mask)


def build(lang):
    pad_shot = Image.open(f"{GOLD}/ipad/{lang}-3.png")
    phone_shot = Image.open(f"{GOLD}/iphone/{lang}-1.png")

    canvas = Image.new("RGB", (W, H), BG)
    # 가운데를 아주 살짝 밝게 — 기기가 떠 보이지 않게 바탕에 깊이를 준다
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W * 0.08, -H * 0.5, W * 0.92, H * 1.25), fill=150)
    canvas.paste(Image.new("RGB", (W, H), GLOW), (0, 0), glow.filter(ImageFilter.GaussianBlur(220)))

    # 아이패드 — 가운데, 바닥까지 보이게
    ratio = pad_shot.height / pad_shot.width
    pw = PAD_W
    ph = round((pw - 2 * PAD_BEZEL) * ratio) + 2 * PAD_BEZEL
    px0 = 640
    py0 = (H - ph) // 2 - 10
    device(canvas, pad_shot, (px0, py0, px0 + pw, py0 + ph), PAD_BEZEL, PAD_R)

    # 아이폰 — 왼쪽 앞, 아이패드 테두리에 살짝 겹치게
    pr = phone_shot.height / phone_shot.width
    fw = PHONE_W
    fh = round((fw - 2 * PHONE_BEZEL) * pr) + 2 * PHONE_BEZEL
    fx0 = 336
    fy0 = py0 + ph - fh + 44          # 아이패드보다 조금 아래 = 앞에 있는 느낌
    device(canvas, phone_shot, (fx0, fy0, fx0 + fw, fy0 + fh), PHONE_BEZEL, PHONE_R)

    out = f"{OUT}/{lang}/hero.webp"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    canvas.resize((1700, round(1700 * H / W)), Image.LANCZOS).save(out, "WEBP", quality=84, method=6)
    print(lang, out, os.path.getsize(out) // 1024, "KB")


# 크게 보여 줄 장면 셋 — 가로 아이패드 한 대만. 세로 그림보다 낮아서
# 페이지가 짧아지고, 첫 그림과 결이 같다(2026-11-17 구조 정리).
DEEP = (3, 4, 5)


def deep(lang, num):
    shot = Image.open(f"{GOLD}/ipad/{lang}-{num}.png")
    bezel, radius, m = 22, 34, 54
    sw = 1120
    sh_ = round(sw * shot.height / shot.width)
    cw, ch = sw + 2 * bezel + 2 * m, sh_ + 2 * bezel + 2 * m
    canvas = Image.new("RGB", (cw, ch), BG)
    device(canvas, shot, (m, m, cw - m, ch - m), bezel, radius)
    out = f"{OUT}/{lang}/d{num}.webp"
    canvas.resize((1200, round(1200 * ch / cw)), Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
    return canvas.size


if __name__ == "__main__":
    for l in LANGS:
        build(l)
        for n in DEEP:
            deep(l, n)
        print(l, "깊은 그림", DEEP)
