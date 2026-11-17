#!/usr/bin/env python3
"""'녹음하면 악보가 따라 넘어갑니다' 짧은 영상 — leggii/shots/follow.mp4 (2026-11-17).

렛지 세션이 뽑은 프레임(goldens/frames/01..12.png, 2752×2064 가로, 기기 틀 없음)을
첫 그림과 같은 기기 틀에 끼워 넣고 이어 붙인다. 틀을 씌우는 이유는 멈춤 그림
(poster = d3.webp)과 이어져야 하기 때문이다. 둘이 다르면 재생이 시작되는 순간
그림이 튄다.

01–06 이 1–2쪽 펼친 면, 07–12 가 3–4쪽. 13–15(5쪽)는 오른쪽이 비어 반복이
어색해지므로 쓰지 않는다. 12에서 01로 돌아간다.

소리는 없다. 쪽이 넘어가는 순간(06→07)만 조금 빠르게, 넘어간 뒤에는 조금
머물게 해서 실제로 보는 느낌에 가깝게 한다.

python3 leggii_follow.py
"""
import os
import subprocess
import tempfile

from PIL import Image

import leggii_hero as H

FRAMES = "/Users/jameslee/App/leggii/test_screenshots/goldens/frames"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leggii", "shots", "follow.mp4")
USE = list(range(1, 13))          # 01–12
WIDTH = 1200                      # 멈춤 그림(d3.webp)과 같은 너비

# 프레임마다 머무는 시간(초). 넘어가기 직전은 짧게, 넘어간 직후는 길게.
HOLD = {6: 0.42, 7: 0.85, 12: 0.80}
DEFAULT_HOLD = 0.55


def framed(path):
    """첫 그림과 같은 기기 틀에 화면을 끼운다(leggii_hero.deep 과 같은 치수)."""
    shot = Image.open(path)
    bezel, radius, m = 22, 34, 54
    sw = 1120
    sh = round(sw * shot.height / shot.width)
    cw, ch = sw + 2 * bezel + 2 * m, sh + 2 * bezel + 2 * m
    canvas = Image.new("RGB", (cw, ch), H.BG)
    H.device(canvas, shot, (m, m, cw - m, ch - m), bezel, radius)
    return canvas.resize((WIDTH, round(WIDTH * ch / cw)), Image.LANCZOS)


def main():
    with tempfile.TemporaryDirectory(prefix="leggii-follow-") as tmp:
        lines = []
        for n in USE:
            src = f"{FRAMES}/{n:02d}.png"
            if not os.path.exists(src):
                raise SystemExit(f"프레임이 없다: {src}")
            dst = f"{tmp}/{n:02d}.png"
            framed(src).save(dst)
            hold = HOLD.get(n, DEFAULT_HOLD)
            lines.append(f"file '{dst}'\nduration {hold}")
        # concat 데모서는 마지막 그림을 한 번 더 적어야 끝까지 보여 준다
        lines.append(f"file '{tmp}/{USE[-1]:02d}.png'")
        listing = f"{tmp}/list.txt"
        open(listing, "w").write("\n".join(lines) + "\n")

        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "concat", "-safe", "0", "-i", listing,
            "-vf", "fps=15,format=yuv420p",
            "-c:v", "libx264", "-preset", "veryslow", "-crf", "30",
            "-movflags", "+faststart", "-an",
            OUT,
        ], check=True)
    secs = sum(HOLD.get(n, DEFAULT_HOLD) for n in USE)
    print(f"{OUT}  {os.path.getsize(OUT) // 1024} KB  {secs:.1f}초  {len(USE)}장")


if __name__ == "__main__":
    main()
