"""Nomio 법적 문서 페이지 — vicinolabs.com/nomio/privacy/, /nomio/terms/ (2026-10-01).

예전 주소(vicino-labs.github.io/nomio-privacy)에서 옮겼다. 회사 사이트와 같은 원칙으로
외부 글꼴·스크립트를 불러오지 않는다(사이트 Datenschutz에 그렇게 적혀 있음).
본문은 nomio_privacy_content.py / nomio_terms_content.py. build.py가 함께 실행한다.
한 페이지에 한국어·영어·독일어가 다 있고 위쪽 단추로 바꾼다(#ko/#en/#de, 앱이 언어에 맞춰 연다).
"""
import html
import os

from nomio_privacy_content import PRIVACY, EMAIL
from nomio_terms_content import TERMS

LANGS = [("ko", "한국어"), ("en", "English"), ("de", "Deutsch")]

CSS = """
:root{--bg:#f7f2ea;--paper:#fffcf7;--ink:#1c1714;--soft:#6b5f56;--line:#e7dcca;--accent:#2a2724;--gold:#8a6a33;--tag:#efe7da}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141110;--paper:#1d1916;--ink:#f1e8da;--soft:#bfb2a2;--line:#2e2823;--accent:#e9d3a6;--gold:#d4b07a;--tag:#26201c}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased;word-break:keep-all}
a{color:var(--gold)}
.top{border-bottom:1px solid var(--line)}
.top .in{max-width:1080px;margin:0 auto;padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.co{display:inline-flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-family:Georgia,"Times New Roman",serif;font-size:19px}
.co img{height:26px;width:auto}
.langbar{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:var(--paper)}
.langbar button{border:0;background:transparent;color:var(--soft);font:600 13px/1 inherit;font-family:inherit;padding:8px 14px;cursor:pointer}
.langbar button.active{background:var(--ink);color:var(--bg)}
.page{max-width:1080px;margin:0 auto;padding:0 20px}
.mast{padding:40px 0 22px;border-bottom:1px solid var(--line)}
.app{display:inline-flex;align-items:center;gap:10px;color:var(--soft);text-decoration:none;font-weight:600;font-size:14px}
.mark{width:30px;height:30px;border-radius:8px;background:#2a2724;color:#d4b07a;display:grid;place-items:center;font:italic 600 19px Georgia,serif;border:1px solid rgba(212,176,122,.35)}
h1{font-family:Georgia,"Times New Roman","Nanum Myeongjo",serif;font-weight:500;font-size:clamp(30px,5vw,42px);line-height:1.2;margin:16px 0 14px;letter-spacing:-.01em}
.meta{display:flex;gap:8px;flex-wrap:wrap}
.tag{background:var(--tag);border-radius:999px;padding:4px 12px;font-size:12.5px;color:var(--soft)}.tag b{color:var(--ink);font-weight:600}
.layout{display:grid;grid-template-columns:220px 1fr;gap:44px;padding:30px 0 10px}
@media(max-width:860px){.layout{grid-template-columns:1fr;gap:10px}.toc{position:static!important;max-height:none!important;border:1px solid var(--line);border-radius:10px;padding:14px 16px!important;background:var(--paper)}}
.toc{position:sticky;top:20px;align-self:start;max-height:calc(100vh - 40px);overflow:auto;padding-top:4px}
.toc-label{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);margin-bottom:8px}
.toc a{display:block;color:var(--soft);text-decoration:none;font-size:13.5px;padding:4px 0;line-height:1.4}.toc a:hover{color:var(--ink)}
article{min-width:0;max-width:720px}
.lede{font-size:17px;color:var(--soft);margin:0 0 8px}
section{padding-top:14px}
h2{font-family:Georgia,"Times New Roman","Nanum Myeongjo",serif;font-weight:500;font-size:23px;margin:28px 0 10px;scroll-margin-top:16px}
p,li{font-size:15.5px}ul,ol{padding-left:22px}li{margin:4px 0}
.summary-box{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:6px 20px}
.id-card{display:grid;grid-template-columns:max-content 1fr;gap:6px 18px;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:16px 20px;margin:6px 0 12px;font-size:15px}
.id-card dt{color:var(--soft)}.id-card dd{margin:0}
@media(max-width:520px){.id-card{grid-template-columns:1fr}.id-card dt{margin-top:6px}}
.contact-card{display:flex;flex-direction:column;gap:2px;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin-top:8px}
.contact-card .role{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft)}
.contact-card .name{font-family:Georgia,serif;font-size:18px}
footer{margin:46px 0 0;padding:22px 0 44px;border-top:1px solid var(--line);display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px 20px;font-size:13.5px;color:var(--soft)}
footer a{color:var(--soft);margin-right:14px}
"""

SCRIPT = """
(function(){
  var bar=document.querySelector('.langbar'),docs=document.querySelectorAll('.doc'),ok=['ko','en','de'];
  function set(l){docs.forEach(function(d){d.hidden=d.getAttribute('data-lang')!==l});
    bar.querySelectorAll('button').forEach(function(b){b.classList.toggle('active',b.getAttribute('data-lang')===l)});
    document.documentElement.lang=l;try{localStorage.setItem('nomio-legal-lang',l)}catch(e){}}
  bar.addEventListener('click',function(e){var b=e.target.closest('button[data-lang]');if(b)set(b.getAttribute('data-lang'))});
  var init='en';
  try{var h=(location.hash||'').replace('#',''),s=localStorage.getItem('nomio-legal-lang'),n=(navigator.language||'en').slice(0,2);
    if(ok.indexOf(h)!==-1)init=h;else if(s&&ok.indexOf(s)!==-1)init=s;else if(ok.indexOf(n)!==-1)init=n;}catch(e){}
  set(init);
})();
"""


def _num(lang, i):
    return f"§ {i}" if lang == "de" else f"{i}."


def _doc(lang, d, other_href, first):
    toc = "".join(f'<a href="#{lang}-{i}">{_num(lang, i)} {html.escape(t)}</a>'
                  for i, (t, _) in enumerate(d["sections"], 1))
    secs = "".join(f'<section id="{lang}-{i}"><h2>{_num(lang, i)} {html.escape(t)}</h2>{b}</section>'
                   for i, (t, b) in enumerate(d["sections"], 1))
    meta = "".join(f'<span class="tag">{k} <b>{v}</b></span>' for k, v in d["meta"])
    hidden = "" if first else " hidden"
    return f"""<div class="doc" data-lang="{lang}"{hidden}>
<div class="mast"><a class="app" href="/nomio/"><span class="mark">n.</span>Nomio</a><h1>{d['h1']}</h1><div class="meta">{meta}</div></div>
<div class="layout"><nav class="toc"><div class="toc-label">Contents</div>{toc}</nav>
<article><p class="lede">{d['lede']}</p>{secs}</article></div>
<footer><span>{d['footer']}</span><span><a href="{other_href}#{lang}">{d['other']}</a><a href="/impressum/">Impressum</a></span></footer>
</div>"""


def legal_page(path, content, other_href, title_lang="en"):
    docs = "".join(_doc(l, content[l], other_href, l == "en") for l, _ in LANGS)
    tabs = "".join(f'<button type="button" data-lang="{l}"{" class=active" if l == "en" else ""}>{n}</button>'
                   for l, n in LANGS)
    t = content[title_lang]["title"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} — Vicino Labs</title>
<meta name="description" content="{t}">
<link rel="canonical" href="https://vicinolabs.com{path}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a>
<div class="langbar" role="tablist" aria-label="Language">{tabs}</div></div></div>
<main class="page">{docs}</main>
<script>{SCRIPT}</script>
</body></html>
"""


NOMIO_HOME = {
 "title": "Nomio — Vicino Labs",
 "body": f"""<div class="mast"><span class="app"><span class="mark">n.</span>Nomio</span>
<h1>Nomio</h1>
<p class="lede">A budget book for income and expenses in many currencies and languages — your records stay on your device.<br>
Haushaltsbuch für Einnahmen und Ausgaben in vielen Währungen und Sprachen.<br>
여러 나라 돈을 한 장부에 — 기록은 기기에만 남는 가계부.</p></div>
<div style="padding:26px 0;max-width:720px">
<p><a href="https://play.google.com/store/apps/details?id=app.nomio.finance" target="_blank" rel="noopener">Google Play →</a></p>
<p>Privacy Policy · Datenschutzerklärung · 개인정보처리방침: <a href="/nomio/privacy/">vicinolabs.com/nomio/privacy</a><br>
Terms of Service · Nutzungsbedingungen · 이용약관: <a href="/nomio/terms/">vicinolabs.com/nomio/terms</a><br>
Impressum: <a href="/impressum/">vicinolabs.com/impressum</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>""",
}


def nomio_home():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{NOMIO_HOME['title']}</title>
<meta name="description" content="Nomio — multi-currency budget app by Vicino Labs.">
<link rel="canonical" href="https://vicinolabs.com/nomio/">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<style>{CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/"><img src="/logo.png" alt="" width="47" height="26">Vicino Labs</a></div></div>
<main class="page">{NOMIO_HOME['body']}</main>
</body></html>
"""


def build(root):
    def write(path, text):
        out = os.path.join(root, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(text)
    write("/nomio/", nomio_home())
    write("/nomio/privacy/", legal_page("/nomio/privacy/", PRIVACY, "/nomio/terms/"))
    write("/nomio/terms/", legal_page("/nomio/terms/", TERMS, "/nomio/privacy/"))


if __name__ == "__main__":
    build(os.path.dirname(os.path.abspath(__file__)))
    print("ok")
