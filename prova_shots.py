"""프로바 소개 페이지 그림 (2026-11-18).

스토어 스크린샷(App/앱스토어/프로바)에서 **기기 부분만** 잘라 쓴다. 스토어
그림에는 위에 홍보 문구가 얹혀 있어 그대로 쓰면 글이 두 번 나온다.

기기 테두리 자리는 재서 찾았다(모든 장면이 같은 자리다).
  아이패드 (352, 860)-(1711, 2648)   1359×1788
  아이폰   (168, 704)-(1037, 2538)    870×1835

배경은 투명하게 둔다. 사이트가 밝은 때와 어두운 때 둘 다 쓰므로
상아색을 구워 넣으면 어두운 화면에서 흰 덩어리가 된다.

  python3 prova_shots.py
"""
import os

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/Users/jameslee/App/앱스토어/프로바"
OUT = os.path.join(HERE, "prova", "shots")
LANGS = ("ko", "en", "de")

IPAD = (352, 860, 1711, 2648)
IPHONE = (168, 704, 1037, 2538)
# 기기 모서리 반경(원본 픽셀). 재서 찾았다 — 아이폰 118, 아이패드 70.
# 46 으로 두었더니 마스크가 기기의 둥근 모서리보다 작아, 모서리 바깥의
# 밝은 배경이 그림 안에 남아 흰 테처럼 보였다(2026-11-18).
IPAD_R = 70
IPHONE_R = 118


INSET = 4            # 기기 가장자리 안쪽으로 잘라 들어가는 픽셀 수


def device(path, box, height, radius):
    """기기만 잘라 둥근 모서리로 다듬고 [height] 높이로 줄인다.

    가장자리를 [INSET] 만큼 안쪽에서 자른다. 원본에서 기기 테두리와 밝은
    배경이 만나는 줄은 이미 두 색이 섞인 밝은 픽셀이라, 거기서 알파만
    깎으면 **색은 밝은 채로 남아** 상아색 페이지 위에서 흰 테처럼 보인다
    (대표님 2026-11-18 "모서리 깎은자리에 배경 색이 달라서 보기 안좋음").
    섞인 줄을 아예 잘라내면 남는 가장자리가 순수한 검은 테두리라,
    마스크가 만드는 경계도 검정에서 투명으로 곱게 넘어간다.
    """
    box = (box[0] + INSET, box[1] + INSET, box[2] - INSET, box[3] - INSET)
    im = Image.open(path).convert("RGB").crop(box)
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), max(1, radius - INSET), fill=255)
    out = Image.new("RGBA", (w, h))
    out.paste(im, (0, 0), mask)
    k = height / h
    return out.resize((max(1, round(w * k)), height), Image.LANCZOS)


def shadow(size, radius, blur=34, spread=16, alpha=110):
    """기기 뒤에 깔 부드러운 그림자."""
    w, h = size
    pad = blur * 2 + spread
    s = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(s).rounded_rectangle(
        (pad, pad, pad + w - 1, pad + h - 1), radius, fill=(60, 35, 18, alpha))
    return s.filter(ImageFilter.GaussianBlur(blur)), pad


def place(canvas, dev, x, y, radius):
    sh, pad = shadow(dev.size, radius)
    canvas.alpha_composite(sh, (x - pad, y - pad + 22))
    canvas.alpha_composite(dev, (x, y))


def hero(lang):
    """아이패드 옆에 아이폰. 가로로 넓은 첫 그림."""
    pad = device(f"{SRC}/{lang}/ipad/screenshot-2.png", IPAD, 1000, IPAD_R)
    pho = device(f"{SRC}/{lang}/iphone/screenshot-3.png", IPHONE, 700, IPHONE_R)
    W, H = 1680, 1120
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = (W - pad.width) // 2 + 150
    # 줄인 뒤 비율에 맞춰 그림자 반경도 줄인다
    place(c, pad, px, (H - pad.height) // 2, round(IPAD_R * pad.height / (IPAD[3] - IPAD[1])))
    place(c, pho, px - pho.width + 60, H - pho.height - 60,
          round(IPHONE_R * pho.height / (IPHONE[3] - IPHONE[1])))
    return c


def crop(lang, which, box, width, radius):
    """기기 한 대를 [width] 너비로. 세로는 원래 비율대로."""
    h = round(width * (box[3] - box[1]) / (box[2] - box[0]))
    return device(f"{SRC}/{lang}/{which[0]}/screenshot-{which[1]}.png", box, h, radius)


def build():
    for lang in LANGS:
        d = os.path.join(OUT, lang)
        os.makedirs(d, exist_ok=True)
        hero(lang).save(os.path.join(d, "hero.webp"), quality=86, method=6)
        # 깊이 보는 세 장면: 2 AI 연주 점검 · 3 AI 레슨 노트 · 4 두 녹음 비교
        for n in (2, 3, 4):
            crop(lang, ("ipad", n), IPAD, 1100, IPAD_R).save(
                os.path.join(d, f"d{n}.webp"), quality=84, method=6)
        # 요약 판 타일: 아이폰 네 장면
        for n in (1, 2, 3, 4):
            crop(lang, ("iphone", n), IPHONE, 520, IPHONE_R).save(
                os.path.join(d, f"t{n}.webp"), quality=82, method=6)
        print(lang, "ok")


if __name__ == "__main__":
    build()
