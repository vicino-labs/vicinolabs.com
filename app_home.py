"""앱 소개 페이지 공통 틀 — vicinolabs.com/<앱>/ (2026-11-11, 사용자: "링크 들어간 앱 사이트들 손 좀 봐서 구글·애플 링크 아이콘").
Famiglia 화면에서 아이콘을 누르면 오는 곳. 큰 아이콘 + 이름 + 언어별 한 줄(고른 언어만 보임) + 공식 스토어 배지
(/badges, 언어별: ko·de·en, 나머지는 en) + 개인정보·약관·Impressum. 출시 전 스토어는 "출시 예정" 표시.
각 앱 *_legal.py 의 *_home() 이 이 함수를 부른다."""
import nomio_legal

LANGS = [("ko", "한국어"), ("en", "English"), ("de", "Deutsch"), ("it", "Italiano")]
FAM = {"ko": "/ko/famiglia/", "en": "/en/famiglia/", "de": "/famiglia/", "it": "/it/famiglia/"}
SOON = {"ko": "출시 예정", "en": "Coming soon", "de": "Demnächst", "it": "Prossimamente"}
FAMT = {"ko": "Famiglia Vicino의 다른 앱 보기", "en": "More apps from Famiglia Vicino",
        "de": "Weitere Apps der Famiglia Vicino", "it": "Altre app della Famiglia Vicino"}
LEGAL = {"ko": ("개인정보처리방침", "이용약관"), "en": ("Privacy Policy", "Terms of Service"),
         "de": ("Datenschutzerklärung", "Nutzungsbedingungen"), "it": ("Informativa privacy", "Termini")}

CSS = """
.ah{max-width:720px;margin:0 auto;padding:64px 20px 40px;text-align:center}
.ah .ic{width:132px;height:132px;border-radius:30px;display:block;margin:0 auto 26px;box-shadow:0 26px 50px -22px rgba(60,30,15,.55)}
.ah h1{font-family:Georgia,"Times New Roman",serif;font-weight:500;font-size:clamp(34px,6vw,50px);line-height:1.15;margin:0 0 6px}
.ah .sub{color:var(--gold);font-size:15px;letter-spacing:.04em;margin:0 0 22px}
.ah .langs{display:inline-flex;border:1px solid var(--line);border-radius:99px;padding:3px;background:var(--paper);margin:0 0 20px}
.ah .langs button{border:0;background:none;color:var(--soft);font:600 13px/1 inherit;font-family:inherit;padding:8px 14px;border-radius:99px;cursor:pointer}
.ah .langs button.on{background:var(--ink);color:var(--bg)}
.ah .lede{font-size:18px;color:var(--soft);margin:0 auto 30px;max-width:560px;text-wrap:balance}

.ah .stores{display:flex;gap:14px;justify-content:center;align-items:center;flex-wrap:wrap;min-height:52px}
.ah .stores a{display:block;line-height:0}.ah .stores img{width:auto;display:block}
.ah .soon{display:inline-block;border:1px solid var(--gold);color:var(--gold);border-radius:99px;padding:8px 18px;font-weight:600;font-size:14px}
.ah .fam{display:inline-block;margin:34px 0 0;font-weight:600;font-size:14.5px;text-decoration:none;border-bottom:1px solid var(--line)}
.ah .legal{margin:46px 0 0;padding-top:20px;border-top:1px solid var(--line);font-size:13.5px;color:var(--soft)}
.ah .legal a{color:var(--soft)}
.ah [data-l]:not(.on){display:none!important}
"""


def ON(l):
    return ' class="on"' if l == "en" else ""


def page(*, key, name, sub, icon, ledes, play=None, apple=None, email, desc, canonical):
    """ledes: {lang: 한 줄}. play: 패키지 이름, apple: App Store 주소(없으면 출시 예정)."""
    lede = "".join(f'<p data-l="{l}" class="lede{" on" if l == "en" else ""}">{ledes[l]}</p>' for l, _ in LANGS)
    def stores(l):
        b = l if l in ("ko", "de", "en") else "en"
        out = []
        if play:
            out.append(f'<a href="https://play.google.com/store/apps/details?id={play}&amp;hl={l}" target="_blank" rel="noopener" '
                       f'aria-label="Google Play"><img src="/badges/google-play-{b}-nb.png" alt="Google Play" style="height:48px;border-radius:10px;border:1px solid #a6a6a6;box-sizing:border-box"></a>')
        if apple:
            out.append(f'<a href="{apple}" target="_blank" rel="noopener" aria-label="App Store">'
                       f'<img src="/badges/app-store-{b}.svg" alt="App Store" style="height:48px"></a>')
        if not (play and apple):
            out.append(f'<span class="soon">{"App Store" if play else ("Google Play" if apple else "Google Play · App Store")} — {SOON[l]}</span>')
        return "".join(out)
    store_html = "".join(f'<div data-l="{l}" class="stores{" on" if l == "en" else ""}">{stores(l)}</div>' for l, _ in LANGS)
    fam = "".join(f'<a data-l="{l}" class="fam{" on" if l == "en" else ""}" href="{FAM[l]}">{FAMT[l]} →</a>' for l, _ in LANGS)
    legal = "".join(f'<p data-l="{l}"{ON(l)}><a href="/{key}/privacy/#{l}">{LEGAL[l][0]}</a> · <a href="/{key}/terms/#{l}">{LEGAL[l][1]}</a> · '
                    f'<a href="/impressum/">Impressum</a> · <a href="mailto:{email}">{email}</a></p>' for l, _ in LANGS)
    buttons = "".join(f'<button type="button" data-set="{l}">{n}</button>' for l, n in LANGS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} — Vicino Labs</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://vicinolabs.com{canonical}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{nomio_legal.CSS}{CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="ah">
<img class="ic" src="{icon}" srcset="{icon.replace('/apps/', '/apps/hi/')} 2x" alt="{name}" width="132" height="132">
<h1>{name}</h1><p class="sub">{sub}</p>
<div class="langs" role="group" aria-label="Language">{buttons}</div>
{lede}{store_html}{fam}
<div class="legal">{legal}</div>
</main>
<script>(function(){{var k="vl-app-lang",L=["ko","en","de","it"],s=null;try{{s=localStorage.getItem(k)}}catch(e){{}}
var h=(location.hash||"").slice(1),n=(navigator.language||"en").slice(0,2),l=L.indexOf(h)>=0?h:(L.indexOf(s)>=0?s:(L.indexOf(n)>=0?n:"en"));
function set(x){{l=x;document.documentElement.lang=x;document.querySelectorAll("[data-l]").forEach(function(e){{e.classList.toggle("on",e.getAttribute("data-l")===x)}});
document.querySelectorAll("[data-set]").forEach(function(b){{b.classList.toggle("on",b.getAttribute("data-set")===x)}});try{{localStorage.setItem(k,x)}}catch(e){{}}}}
document.querySelectorAll("[data-set]").forEach(function(b){{b.addEventListener("click",function(){{set(b.getAttribute("data-set"))}})}});set(l)}})();</script>
</body></html>
"""
