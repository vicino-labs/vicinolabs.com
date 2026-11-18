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
# 기기 모서리 반경(원본 픽셀).
#
# 눈으로 맞추면 안 되고, 재서도 모자란다. 처음에 46 으로 두었더니 마스크가
# 기기 모서리보다 훨씬 작아 모서리 바깥 배경이 통째로 남았다. 그다음 원본에서
# 재어 118/70 을 썼는데도 아이폰에 밝은 픽셀이 10여 개 남았다. 테두리가
# 흐려지는 자리 때문에 "재어서 나온 값"이 실제보다 조금 작게 나온다.
#
# 그래서 반경을 조금씩 올려 가며 **모서리 반투명 픽셀 중 밝은 것(밝기 200 초과)
# 개수를 세어** 0 이 되는 값을 찾았다. 아이폰은 120 부터 0 이고, 여유를 두어
# 124 를 쓴다. 아이패드는 70 에서 이미 0 이지만 같은 여유로 74 를 쓴다.
# 조금 더 깎여도 그 자리는 검은 테두리라 눈에 띄지 않는다.
#
# 확인하는 법은 App/brand/기기-그림-기준.md 에 적어 두었다.
IPAD_R = 74
IPHONE_R = 124


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
    """폰이 앞에 크게, 아이패드가 뒤에 작게.

    프로바는 **폰으로 쓰는 앱**이다(대표님 2026-11-18 "프로바는 패드보단
    휴대폰으로 많이 쓰겠지?"). 레슨실에서 폰을 세워 두고 녹음하고, 입시
    영상도 폰으로 찍는다. 아이패드는 집에 와서 넓게 펼쳐 볼 때다.
    렛지와 정반대인 자리라 첫 그림부터 그렇게 보여야 한다.
    """
    pho = device(f"{SRC}/{lang}/iphone/screenshot-1.png", IPHONE, 980, IPHONE_R)
    pad = device(f"{SRC}/{lang}/ipad/screenshot-3.png", IPAD, 740, IPAD_R)
    W, H = 1680, 1120
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    overlap = 110
    x0 = (W - (pho.width + pad.width - overlap)) // 2
    py = (H - pho.height) // 2
    # 줄인 뒤 비율에 맞춰 그림자 반경도 줄인다. 아이패드를 먼저 놓아 뒤로 보낸다.
    place(c, pad, x0 + pho.width - overlap, py + pho.height - pad.height - 60,
          round(IPAD_R * pad.height / (IPAD[3] - IPAD[1])))
    place(c, pho, x0, py, round(IPHONE_R * pho.height / (IPHONE[3] - IPHONE[1])))
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
        # 깊이 보는 장면. 프로바에만 있는 것 둘은 **폰**으로 보여 준다.
        #   dp4 두 녹음 비교 · dp2 AI 연주 점검
        for n in (2, 4):
            crop(lang, ("iphone", n), IPHONE, 620, IPHONE_R).save(
                os.path.join(d, f"dp{n}.webp"), quality=84, method=6)
        # 아이패드는 한 장면만. 넓은 화면에서 목록과 녹음이 나란히 놓이는 자리다.
        # 보관함 그림(5번)이 더 맞지만 기기가 아래로 잘려 있어 1번을 쓴다.
        crop(lang, ("ipad", 1), IPAD, 1100, IPAD_R).save(
            os.path.join(d, "dwide.webp"), quality=84, method=6)
        # 요약 판 타일: 아이폰 네 장면
        for n in (1, 2, 3, 4):
            crop(lang, ("iphone", n), IPHONE, 520, IPHONE_R).save(
                os.path.join(d, f"t{n}.webp"), quality=82, method=6)
        print(lang, "ok")


if __name__ == "__main__":
    build()
