"""Famiglia Vicino 총보(2026-11-11) — 진짜 악보처럼 그리는 SVG. Bravura(SMuFL, OFL) 글꼴을
/fonts/bravura/bravura-score.woff 로 쓴다(필요한 글리프만). 곡: 베토벤 교향곡 9번 4악장 「환희의 송가」
주제 앞 8마디(라장조 4/4, 가사 실러). 마디마다 주인공 앱(와인색 + 금빛 바탕)이 바뀌고 나머지는 받친다.
같은 곡의 음원(사이트에는 안 올림): _draft/audio/make_midi.py + render.swift (A4 = 443 Hz)."""

SP = 8.0
NB = 8                     # 마디 수
STAGE_BARS = [0, 2, 4, 6, 7]  # 연습 기호 A–E 가 붙는 마디
MUSIC = []                 # 마지막으로 그린 곡(음원 만들 때 씀)
FS = SP * 4  # Bravura font-size

G = {  # SMuFL 글리프
    "gClef": "", "fClef": "", "t4": "", "brace": "",
    "nhBlack": "", "nhHalf": "", "nhWhole": "",
    "rWhole": "", "rHalf": "", "rQuarter": "",
    "fermata": "", "breath": "", "dot": "",
    "p": "", "pp": "", "mp": "", "mf": "", "f": "",
    "rptL": "", "rptR": "",
    "sharp": "\ue262", "flagUp": "\ue240", "flagDown": "\ue241",
}
STEPS = {"C": 0, "D": 1, "E": 2, "F": 3, "G": 4, "A": 5, "B": 6}
REF = {"treble": 4 * 7 + 2, "bass": 2 * 7 + 4}  # 맨 아래 줄: E4 / G2


def step(pitch, clef):
    return int(pitch[1]) * 7 + STEPS[pitch[0]] - REF[clef]


class Score:
    def __init__(self, width=1000):
        self.W = width
        self.o = []

    def t(self, x, y, s, cls="mus", extra=""):
        self.o.append(f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}"{extra}>{s}</text>')

    def line(self, x1, y1, x2, y2, w=1.0, cls="ln"):
        self.o.append(f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="{w}"/>')

    def staff(self, x1, x2, top):
        for i in range(5):
            self.line(x1, top + i * SP, x2, top + i * SP, 0.9, "st")

    def note_y(self, top, pitch, clef):
        return top + 4 * SP - step(pitch, clef) * SP / 2

    def ledgers(self, x, top, s):
        w = 1.18 * SP
        k = -2
        while k >= s:
            self.line(x - 0.35 * SP, top + 4 * SP - k * SP / 2, x + w + 0.35 * SP, top + 4 * SP - k * SP / 2, 1.1)
            k -= 2
        k = 10
        while k <= s:
            self.line(x - 0.35 * SP, top + 4 * SP - k * SP / 2, x + w + 0.35 * SP, top + 4 * SP - k * SP / 2, 1.1)
            k += 2

    def chord(self, x, top, clef, pitches, dur, stem=None, stemless=False):
        """dur: 1=온, 2=2분, 4=4분. 같은 기둥의 화음. 돌려줌: (머리 y들, 기둥 방향)"""
        ss = [step(p, clef) for p in pitches]
        ys = [top + 4 * SP - s * SP / 2 for s in ss]
        head = {1: G["nhWhole"], 2: G["nhHalf"], 4: G["nhBlack"]}[dur]
        for s, y in zip(ss, ys):
            self.ledgers(x, top, s)
            self.t(x, y, head)
        up = stem if stem is not None else (sum(ss) / len(ss) < 4)
        if dur > 1 and not stemless:
            w = 1.18 * SP
            if up:
                xs = x + w - 0.07 * SP
                self.line(xs, max(ys) - 0.15 * SP, xs, min(ys) - 3.5 * SP, 1.2)
            else:
                xs = x + 0.07 * SP
                self.line(xs, min(ys) + 0.15 * SP, xs, max(ys) + 3.5 * SP, 1.2)
        return ys, up

    def slur(self, x1, y1, x2, y2, above=True, h=None):
        d = -1 if above else 1
        h = h or min(22, 6 + (x2 - x1) * 0.08)
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2 + d * h
        my2 = my - d * 1.6
        self.o.append(f'<path class="slur" d="M{x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {mx:.1f} {my2:.1f} {x1:.1f} {y1:.1f}Z"/>')

    def svg(self, h, label):
        return (f'<svg class="score" viewBox="0 0 {self.W} {h:.0f}" role="img" aria-label="{label}">'
                + "".join(self.o) + "</svg>")


def score_svg(names, stages, subtitle, dc, label):
    # ---------------- 총보 ----------------
    S = Score(1240)
    X0, XN = 170, 1216          # 오선 시작·끝
    XM = 258                   # 첫 마디 시작(음자리표·조표·박자표 뒤)
    # (키, 음자리표, 묶음) — 묶음: solo / brace / bracket / single
    PARTS = [("welegato", "treble", "solo"), ("leggii", "treble", "brace"), ("chiave", "bass", "brace"),
             ("appoggio", "treble", "bracket"), ("squillo", "bass", "bracket"),
             ("pianino", "treble", "single"), ("prova", "treble", "single")]
    GAP = {"solo": 92, "brace": 70, "bracket": 92, "single": 78}
    tops, y = [], 168
    for i, (k, c, g) in enumerate(PARTS):
        tops.append(y)
        nxt = PARTS[i + 1][2] if i + 1 < len(PARTS) else None
        y += (66 if g == "brace" else 86) if (nxt == g and g in ("brace", "bracket")) else GAP[g] + 6
    H = tops[-1] + 4 * SP + 84
    TOP0, BOT = tops[0], tops[-1] + 4 * SP

    # ---- 곡: L. van Beethoven, 교향곡 9번 op. 125 4악장 「환희의 송가」 주제 앞 8마디(그대로). 라장조 4/4.
    # 조표(F#·C#)가 붙으므로 음 이름은 글자만 쓴다(F = F#, C = C#). 화성 D | D A | D | A | D | D A | D | A7 D
    # 주제가 성부를 건너간다: Violino(1–2) → Pianoforte(3–4) → Baritono(5) → Soprano(6) → Oboe(7) → Flauto(8, 모두 함께 맺음).
    # 가사는 실러 원문(Freude, schöner Götterfunken … Heiligtum). 베토벤·실러 모두 저작권 만료.
    global MUSIC
    ACTIVE = {j: set() for j in range(NB)}
    MUSIC = []
    def play(j, i, clef, notes, **k):
        k.setdefault("slur", False)
        ACTIVE[j].add(i); MUSIC.append((j, i, clef, notes, k))
    Q = lambda *ps: [([p], 1) for p in ps]
    LYR1, LYR2, LYR3 = ["Freu-", "de,", "schö-", "ner"], ["Göt-", "ter-", "fun-", "ken,"], ["Hei-", "lig-", "tum!"]
    # A 찾기 — 주인공 Violino (주제 1–2마디)
    play(0, 0, "treble", Q("F5", "F5", "G5", "A5"), dyn="p", feat=True)
    play(1, 0, "treble", Q("A5", "G5", "F5", "E5"), feat=True)
    play(0, 1, "treble", [("r", 1), (["D4", "F4"], 1), (["D4", "F4"], 1), (["D4", "F4"], 1)], dyn="pp")
    play(0, 2, "bass", [(["D3"], 2), (["A2"], 2)])
    play(1, 1, "treble", [(["D4", "F4"], 2), (["C4", "E4", "G4"], 2)])
    play(1, 2, "bass", [(["D3"], 2), (["A2"], 2)])
    # B 준비하기 — 주인공 Pianoforte 두 손 (주제 3–4마디)
    play(2, 1, "treble", Q("D5", "D5", "E5", "F5"), dyn="mp", feat=True)
    play(2, 2, "bass", Q("D3", "F3", "A3", "F3"), feat=True)
    play(3, 1, "treble", [(["F5"], 1.5), (["E5"], 0.5), (["E5"], 2)], feat=True)
    play(3, 2, "bass", Q("A2", "C3", "E3", "C3"), feat=True)
    play(2, 0, "treble", [(["A4"], 4)], dyn="pp")
    play(3, 0, "treble", [(["C5"], 4)])
    # C 몸 풀기 — 주인공 Baritono, 이어서 Soprano (주제 1–2마디를 노래로)
    play(4, 4, "bass", Q("F3", "F3", "G3", "A3"), dyn="mf", feat=True, lyr=LYR1)
    play(4, 1, "treble", [("r", 1), (["F4", "A4"], 1), (["F4", "A4"], 1), (["F4", "A4"], 1)], dyn="pp")
    play(4, 2, "bass", [(["D3"], 2), (["A2"], 2)])
    play(5, 3, "treble", Q("A4", "G4", "F4", "E4"), dyn="mf", feat=True, lyr=LYR2)
    play(5, 4, "bass", Q("F3", "E3", "D3", "C3"), lyr=LYR2)
    play(5, 1, "treble", [(["D4", "F4"], 2), (["C4", "E4", "G4"], 2)])
    play(5, 2, "bass", [(["D3"], 2), (["A2"], 2)])
    # D 연습하기 — 주인공 Oboe (주제 7마디)
    play(6, 5, "treble", Q("D5", "D5", "E5", "F5"), dyn="mf", feat=True)
    play(6, 0, "treble", [(["A4"], 4)], dyn="pp")
    play(6, 1, "treble", [("r", 1), (["F4", "A4"], 1), (["F4", "A4"], 1), (["F4", "A4"], 1)])
    play(6, 2, "bass", [(["D3"], 2), (["A2"], 2)])
    # E 돌아보기 — 주인공 Flauto (주제 8마디), 모두 함께 라장조로 맺음
    play(7, 6, "treble", [(["E5"], 1.5), (["D5"], 0.5), (["D5"], 2)], dyn="p", feat=True, fermata_last=True)
    play(7, 0, "treble", [(["A4"], 4)], fermata_last=True)
    play(7, 3, "treble", [(["G4"], 1.5), (["F4"], 0.5), (["F4"], 2)], fermata_last=True, lyr=LYR3)
    play(7, 4, "bass", [(["E3"], 1.5), (["C3"], 0.5), (["D3"], 2)], fermata_last=True, lyr=LYR3)
    play(7, 5, "treble", [(["C5"], 2), (["A4"], 2)], fermata_last=True)
    play(7, 1, "treble", [(["C4", "E4", "G4"], 2), (["D4", "F4", "A4"], 2)], fermata_last=True)
    play(7, 2, "bass", [(["A2"], 2), (["D3"], 2)], fermata_last=True)

    # 마디 폭: 음표가 많은 마디는 넓게. 같은 박자는 모든 성부에서 세로로 맞춤
    def onsets(j):
        ons = {0.0}
        for (jj, i, clef, notes, kw) in MUSIC:
            if jj != j: continue
            b = 0.0
            for _, beats in notes:
                ons.add(b); b += beats
        return sorted(ons) + [4.0]
    WT = []
    for j in range(NB):
        o = onsets(j)
        WT.append([max(0.9, o[n + 1] - o[n]) ** 0.45 for n in range(len(o) - 1)])
    tot = [sum(w) + 0.9 + (1.4 if j == NB - 1 else 0) for j, w in enumerate(WT)]  # +1.2: 마디 앞뒤 여백
    MWJ = [(XN - XM) * x / sum(tot) for x in tot]
    BX = [XM]
    for w in MWJ: BX.append(BX[-1] + w)

    # 머리말(제목·부제·작곡가 자리)
    S.t(620, 46, "An die Freude", "ttl", ' text-anchor="middle"')
    S.t(620, 74, subtitle, "sub", ' text-anchor="middle"')
    S.t(XN, 100, "Ludwig van Beethoven", "comp", ' text-anchor="end"')
    S.t(XN, 117, "Sinfonia n. 9, op. 125 · testo di F. Schiller", "comp2", ' text-anchor="end"')
    S.t(22, 117, "per la Famiglia Vicino", "comp2")

    # 오선·음자리표·박자표·이름 (악기 이름은 실제 총보처럼 이탈리아어)
    INST = {"welegato": "Violino", "appoggio": "Soprano", "squillo": "Baritono", "pianino": "Oboe", "prova": "Flauto"}
    for (k, c, g), top in zip(PARTS, tops):
        S.staff(X0, XN, top)
        S.t(X0 + 6, top + (3 if c == "treble" else 1) * SP, G["gClef" if c == "treble" else "fClef"])
        for n, st in enumerate((8, 5) if c == "treble" else (6, 3)):  # 조표 F#·C#
            S.t(X0 + 34 + n * 10, top + 4 * SP - st * SP / 2, G["sharp"])
        S.t(X0 + 60, top + 1 * SP, G["t4"]); S.t(X0 + 60, top + 3 * SP, G["t4"])
        big = k == "welegato"
        isz = 34 if big else 26
        ix = 22
        if big:
            S.o.append(f'<circle cx="{ix + isz / 2:.1f}" cy="{top + 2 * SP:.1f}" r="{isz * .95:.1f}" fill="url(#wglow)"/>')
        S.o.append(f'<image href="/apps/{k}.png" x="{ix}" y="{top + 2 * SP - isz / 2:.1f}" width="{isz}" height="{isz}"/>')
        nx = X0 - 30 + (0 if g not in ("brace", "bracket") else -6)
        inst = INST.get(k)
        S.t(nx, top + 2 * SP + (0 if inst else 5), names[k], "pn" + (" big" if big else ""), ' text-anchor="end"')
        if inst:
            S.t(nx, top + 2 * SP + 15, inst, "pn2", ' text-anchor="end"')
    S.t(X0 - 36, (tops[1] + tops[2] + 4 * SP) / 2 + 5, "Pianoforte", "pn2 pf", ' text-anchor="end"')

    S.line(X0, TOP0, X0, BOT, 1.4)
    b0, b1 = tops[1], tops[2] + 4 * SP
    sc = (b1 - b0) / FS
    S.o.append(f'<text class="mus" transform="translate({X0 - 16:.1f} {b1:.1f}) scale({min(sc, 1.5):.3f} {sc:.3f})" x="0" y="0">{G["brace"]}</text>')
    k0, k1 = tops[3], tops[4] + 4 * SP
    S.o.append(f'<path class="brk" d="M{X0 - 9} {k0 - 6} V{k1 + 6}"/>'
               f'<path class="brkc" d="M{X0 - 11} {k0 - 7} q 9 -1 15 -9 M{X0 - 11} {k1 + 7} q 9 1 15 9"/>')

    groups = [[0], [1, 2], [3, 4], [5], [6]]
    for j in range(1, NB + 1):
        x = BX[j]
        for gidx in groups:
            ya, yb = tops[gidx[0]], tops[gidx[-1]] + 4 * SP
            if j < NB:
                S.line(x, ya, x, yb, 1.1)
            else:
                S.line(x - 9, ya, x - 9, yb, 1.1)
                S.o.append(f'<rect class="thick" x="{x - 4.5:.1f}" y="{ya:.1f}" width="4.5" height="{yb - ya:.1f}"/>')
                for i in gidx:
                    S.o.append(f'<circle class="dt" cx="{x - 16:.1f}" cy="{tops[i] + 1.5 * SP:.1f}" r="2"/>'
                               f'<circle class="dt" cx="{x - 16:.1f}" cy="{tops[i] + 2.5 * SP:.1f}" r="2"/>')

    # 빠르기는 맨 앞에 한 번(실제 악보처럼), 마디마다 연습 기호 + 그 순간
    S.t(XM - 82, TOP0 - 62, "Allegro assai", "tempo")
    for j, L, ko in zip(STAGE_BARS, "ABCDE", stages):
        x = BX[j] + 4
        S.o.append(f'<rect class="reh" x="{x:.1f}" y="{TOP0 - 46:.1f}" width="19" height="19" rx="1"/>')
        S.t(x + 9.5, TOP0 - 31.5, L, "rehl", ' text-anchor="middle"')
        S.t(x + 26, TOP0 - 32, ko, "stg")

    PAD = 18
    XMAP = {}
    def bx(j, beat):
        return XMAP[j][beat]

    def build_xmap(music):
        for j in range(NB):
            o = onsets(j); unit = MWJ[j] / tot[j]
            x = BX[j] + unit * 0.75; XMAP[j] = {}
            for n, on in enumerate(o[:-1]):
                XMAP[j][on] = x; x += unit * WT[j][n]

    def head_code(beats):
        return {4: 1, 3: 2, 2: 2, 1.5: 4, 1: 4, 0.5: 4}[beats]

    def phrase(j, i, clef, notes, dyn=None, slur=True, fermata_last=False, feat=False, down=False, lyr=None):
        start = len(S.o)
        """notes: [(음 목록 또는 'r', 박자 수)] — 박자 4·3(점2분)·2·1.5(점4분)·1·0.5(8분, 이웃끼리 묶음)."""
        top = tops[i]; beat = 0; ext = []; eighths = []
        def flush():
            if not eighths:
                return
            ss = [sum(step(p, clef) for p in ps) / len(ps) for (_, _, ps) in eighths]
            up = (sum(ss) / len(ss) < 4) and not down
            w = 1.18 * SP
            pts = []
            for (x, ys, ps) in eighths:
                sx = x + w - 0.07 * SP if up else x + 0.07 * SP
                sy = (min(ys) - 3.5 * SP) if up else (max(ys) + 3.5 * SP)
                pts.append([sx, sy])
            # 기울기는 작게, 가장 바깥 기둥 끝에 맞춤
            if up:
                m = min(p[1] for p in pts); y0, y1 = m, m - min(6, max(-6, (pts[0][1] - pts[-1][1]) / 3))
            else:
                m = max(p[1] for p in pts); y0, y1 = m, m - min(6, max(-6, (pts[0][1] - pts[-1][1]) / 3))
            if len(eighths) == 1:
                (x, ys, ps), (sx, sy) = eighths[0], pts[0]
                S.line(sx, (max(ys) - 0.15 * SP) if up else (min(ys) + 0.15 * SP), sx, sy, 1.2)
                S.t(sx - 0.6, sy, G["flagUp" if up else "flagDown"])
                ext.append((x, min(ys), max(ys), min(min(ys), sy), max(max(ys), sy), up))
                eighths.clear(); return
            x0, xe = pts[0][0], pts[-1][0]
            for (x, ys, ps), (sx, _) in zip(eighths, pts):
                by = y0 + (y1 - y0) * ((sx - x0) / (xe - x0) if xe > x0 else 0)
                S.line(sx, (max(ys) - 0.15 * SP) if up else (min(ys) + 0.15 * SP), sx, by, 1.2)
            th = 0.5 * SP * (1 if up else -1)
            S.o.append(f'<path class="beam" d="M{x0 - 0.6:.1f} {y0:.1f} L{xe + 0.6:.1f} {y1:.1f} L{xe + 0.6:.1f} {y1 + th:.1f} L{x0 - 0.6:.1f} {y0 + th:.1f}Z"/>')
            for (x, ys, ps), (sx, _) in zip(eighths, pts):
                by = y0 + (y1 - y0) * ((sx - x0) / (xe - x0) if xe > x0 else 0)
                ext.append((x, min(ys), max(ys), min(min(ys), by), max(max(ys), by), up))
            eighths.clear()
        for item, beats in notes:
            x = bx(j, float(beat)) + (10 if beats == 4 else 0)
            if item == "r":
                flush()
                g = {1: G["rQuarter"], 0.5: "", 2: G["rHalf"]}[beats]
                S.t(x + 2, top + 2 * SP, g)
            elif beats == 0.5:
                ys = [S.note_y(top, p, clef) for p in item]
                S.chord(x, top, clef, item, 4, stemless=True)
                eighths.append((x, ys, item))
            else:
                flush()
                ys, up = S.chord(x, top, clef, item, head_code(beats), stem=(False if down else None))
                hasstem = beats < 4
                hi = min(ys) - (3.5 * SP if (up and hasstem) else 0)
                lo = max(ys) + (3.5 * SP if (not up and hasstem) else 0)
                if beats in (3, 1.5):  # 점
                    for p, yy in zip(item, ys):
                        on_line = step(p, clef) % 2 == 0
                        S.t(x + 1.18 * SP + 4, yy - (SP / 2 if on_line else 0), G["dot"])
                ext.append((x, min(ys), max(ys), hi, lo, up))
            beat += beats
        flush()
        ext.sort(key=lambda e: e[0])
        if slur and len(ext) > 1:
            def end(e, first):
                x, ymin, ymax, hi, lo, up = e
                if up:   # 기둥이 위: 기둥 끝 옆
                    return (x + 1.18 * SP + (3 if first else -1), hi - 3)
                return (x + 0.6 * SP, ymin - 7)
            (x1, y1), (x2, y2) = end(ext[0], True), end(ext[-1], False)
            clear = min(e[3] for e in ext[1:-1]) - 8 if len(ext) > 2 else min(y1, y2)
            h = max(7, (y1 + y2) / 2 - clear + 3)
            S.slur(x1, y1, x2, y2, above=True, h=h)
        if fermata_last:
            e = ext[-1]
            S.t(e[0] + 1, min(e[3], top) - 8, G["fermata"])
        if lyr:
            heads = [e for e in ext]
            ly = max(top + 4 * SP + 17, max(e[4] for e in heads) + 13)
            for n, (e, syl) in enumerate(zip(heads, lyr)):
                cx = e[0] + 0.59 * SP
                S.t(cx, ly, syl.rstrip('-'), 'lyr', ' text-anchor="middle"')
                if syl.endswith('-') and n + 1 < len(heads):
                    S.t((cx + heads[n + 1][0] + 0.59 * SP) / 2, ly, '-', 'lyr', ' text-anchor="middle"')
        if dyn and lyr:
            S.t(ext[0][0] - 2, min(top, min(e[3] for e in ext)) - 9, G[dyn], 'mus dyn')
        elif dyn:
            nxt = tops[i + 1] if i + 1 < len(tops) else top + 120
            lowest = max(e[4] for e in ext)
            dy = max(top + 4 * SP + 17, lowest + 21)
            dy = min(dy, nxt - 12)
            S.t(ext[0][0] - 2, dy, G[dyn], "mus dyn")
        if feat:
            S.o[start:] = [f'<g class="hl">'] + S.o[start:] + ['</g>']
        return ext

    build_xmap(MUSIC)
    BANDS = {(j, i) for (j, i, c, n, k) in MUSIC if k.get("feat")}
    for (j, i) in BANDS:
        S.o.insert(1, f'<rect class="band" x="{BX[j] + 3:.1f}" y="{tops[i] - 14:.1f}" width="{MWJ[j] - 6:.1f}" height="{4 * SP + 28:.1f}" rx="6"/>')
    for (j, i, clef, notes, k) in MUSIC:
        phrase(j, i, clef, notes, **k)
    S.t(BX[6] + 6, tops[5] - 26, "a′ = 443 Hz", "mark")

    # 쉬는 마디: 온쉼표(넷째 줄에 매달림), 마디 가운데
    for j in range(NB):
        for i, (k, c, g) in enumerate(PARTS):
            if i in ACTIVE[j]:
                continue
            S.t(BX[j] + MWJ[j] / 2 - 6, tops[i] + 1 * SP, G["rWhole"])

    S.t(XN, BOT + 58, dc, "dc", ' text-anchor="end"')
    S.t(X0 - 150, BOT + 58, "1", "pg")
    S.o.insert(0, '<defs><radialGradient id="wglow"><stop offset="0" stop-color="#b8324f" stop-opacity=".30"/>'
                  '<stop offset="1" stop-color="#b8324f" stop-opacity="0"/></radialGradient></defs>')
    return S.svg(H, label)
