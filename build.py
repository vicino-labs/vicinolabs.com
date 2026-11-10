#!/usr/bin/env python3
"""vicinolabs.com — Vicino Labs 회사 페이지(2026-09-27). GitHub Pages로
올린다(무료 HTTPS). 메일(MX)은 IONOS 그대로. 고친 뒤 python3 build.py."""
import os

EMAIL = "contact@vicinolabs.com"
CSS = """
:root{--bg:#f5f0e8;--paper:#fffcf6;--ink:#1c1714;--soft:#6b5f56;--faint:#9a8c7f;--line:#e4d9c8;--accent:#6e1a2f;--gold:#a8823f;--goldl:#d9b878}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#13110f;--paper:#1c1916;--ink:#f1e8da;--soft:#bfb2a2;--faint:#8f8274;--line:#2e2823;--accent:#e2a3b1;--gold:#d4b07a;--goldl:#8a6f45}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}.wrap{max-width:1080px;margin:0 auto;padding:0 20px}.narrow{max-width:760px}
header{border-bottom:1px solid var(--line)}.nav{display:flex;justify-content:space-between;align-items:center;padding-top:18px;padding-bottom:18px;gap:12px}
.brand{white-space:nowrap;display:inline-flex;align-items:center;gap:10px;font-family:Georgia,"Times New Roman",serif;font-size:23px;letter-spacing:.01em;color:var(--ink);text-decoration:none}.brand img{height:30px;width:auto;display:block}
.nav nav{display:flex;gap:18px;font-size:14px}.nav nav a{color:var(--soft);text-decoration:none}.nav nav a:hover{color:var(--ink)}
h1{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:clamp(34px,6vw,60px);line-height:1.1;margin:0 0 18px;letter-spacing:-.015em}
h1 em{font-style:italic;color:var(--accent)}
h2{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:clamp(24px,3.4vw,32px);margin:0 0 6px;letter-spacing:-.01em}
.kicker{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:600;margin:0 0 14px}
.lead{font-size:clamp(17px,2vw,19px);color:var(--soft);margin:0;max-width:620px}
.hero{padding:72px 0 64px}
.icons{display:flex;flex-wrap:wrap;gap:10px;margin-top:34px}.icons img{width:46px;height:46px;border-radius:11px;box-shadow:0 4px 12px rgba(40,25,15,.14)}
section{padding:8px 0 56px}.sub{color:var(--soft);margin:0 0 26px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.card{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:22px;display:flex;gap:18px;align-items:flex-start}
.card img{width:72px;height:72px;border-radius:17px;flex:none;box-shadow:0 6px 16px rgba(40,25,15,.16)}
.card h3{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:22px;margin:0;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.card p{margin:4px 0 10px;color:var(--soft);font-size:15px}
.card .links{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:14px}.card .links a{font-weight:600;text-decoration:none}.card .links a:hover{text-decoration:underline}
.soon{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);border:1px solid var(--goldl);border-radius:99px;padding:2px 9px}
.values{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:28px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:34px 0}
.values b{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:19px;display:block;margin-bottom:4px}.values span{color:var(--soft);font-size:15px}
.contact{padding:56px 0 8px}.contact a.btn{display:inline-block;margin-top:14px;background:var(--ink);color:var(--bg);text-decoration:none;padding:11px 20px;border-radius:99px;font-weight:600;font-size:15px}
main.narrow h1{font-size:clamp(28px,4.4vw,40px);margin-top:48px}main.narrow h2{font-size:23px;margin:40px 0 12px}
dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 16px;margin:0;font-size:14.5px;color:var(--soft)}dt{color:var(--soft)}dd{margin:0}
@media(max-width:520px){dl{grid-template-columns:1fr}dt{margin-top:8px}.hero{padding:48px 0 44px}.card{padding:18px;gap:14px}.card img{width:60px;height:60px;border-radius:14px}.grid{grid-template-columns:1fr}.nav nav{gap:12px}.nav nav a:first-child{display:none}.icons{gap:7px}.icons img{width:34px;height:34px;border-radius:8px}}
.lang{position:relative}.lang summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:6px;color:var(--soft);font-size:14px}
.lang summary::-webkit-details-marker{display:none}.lang summary svg{width:16px;height:16px}
.lang .menu{position:absolute;right:0;top:calc(100% + 10px);background:var(--paper);border:1px solid var(--line);border-radius:10px;box-shadow:0 14px 34px rgba(0,0,0,.18);min-width:160px;padding:6px;z-index:20}
.lang .menu a{display:block;padding:8px 12px;border-radius:6px;font-size:14.5px;color:var(--ink)!important}.lang .menu a:hover{background:var(--bg)}.lang .menu a.on{color:var(--accent)!important;font-weight:700}
footer{border-top:1px solid var(--line);margin-top:64px;padding:24px 0 40px;font-size:13.5px;color:var(--soft)}
footer a{color:var(--soft);margin-right:16px}
"""

FONT_CSS = """
body{font-family:Pretendard,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-synthesis:none}
h1,h2,.card h3,.values b{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-style:italic;font-weight:500}
h1{font-size:clamp(40px,6.4vw,68px)}h1 em{font-style:italic}
html[lang=ko] h1,html[lang=ko] h2,html[lang=ko] .card h3,html[lang=ko] .values b,html[lang=zh] h1,html[lang=zh] h2,html[lang=zh] .card h3,html[lang=zh] .values b{font-family:"Noto Serif KR","Songti SC","Noto Serif SC",serif;font-style:normal;font-weight:600;letter-spacing:-.01em}
html[lang=ko] h1,html[lang=zh] h1{font-size:clamp(32px,5vw,52px);line-height:1.2}
html[lang=ko] h1 em,html[lang=zh] h1 em{font-style:normal}
html[lang=ko] body{word-break:keep-all}
h1,h2,.lead{text-wrap:balance}.card p,.values span{text-wrap:pretty}
"""

def page(lang, path, title, desc, body, alt=None, wide=False):
    alt_links = ""
    if alt:
        alt_links = "".join(f'<link rel="alternate" hreflang="{l}" href="https://vicinolabs.com{p}">' for l, p in alt.items())
        alt_links += f'<link rel="alternate" hreflang="x-default" href="https://vicinolabs.com{alt["de"]}">'
    t = TXT[lang]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="https://vicinolabs.com{path}">{alt_links}
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:image" content="https://vicinolabs.com/icon-512.png">
<link rel="stylesheet" href="/fonts/{"fonts-v2.css" if lang in ("ko", "zh") else "fonts-v2-latin.css"}"><style>{CSS}{FONT_CSS}</style>
</head>
<body>
<header><div class="wrap nav"><a class="brand" href="{t['home']}"><img src="/logo.png" alt="" width="58" height="32">Vicino Labs</a>
<nav><a href="{t['home']}#apps">{t['apps_nav']}</a><a href="/impressum/">Impressum</a>{lang_menu(lang, alt)}</nav></div></header>
<main class="wrap{'' if wide else ' narrow'}">{body}</main>
<footer><div class="wrap"><a href="/impressum/">Impressum</a><a href="/datenschutz/">{t['privacy']}</a><a href="mailto:{EMAIL}">{EMAIL}</a><div style="margin-top:10px">© 2026 Vicino Labs</div></div></footer>
</body></html>
"""

PLAY = "https://play.google.com/store/apps/details?id="
# 앱 순서(2026-11-08): 음악 앱(출시 → 준비 중), 노미오는 맨 끝 '일상' 묶음.
MUSIC = ["welegato", "leggii", "appoggio", "pianino", "chiave", "prova", "squillo"]
# App Store 번호(2026-11-10). 나라 없는 링크 — 아이폰은 그 사람 나라 스토어로, 컴퓨터는 미국 스토어
# (아뽀조·피아니노는 미국에도 있음). 렛지는 승인되면 6832925566 추가.
APPLE = {"appoggio": "6832364161", "pianino": "6832363954"}
STORE = {"leggii": "com.vicinolabs.leggii", "appoggio": "com.vicinolabs.appoggio", "pianino": "com.vicinolabs.pianino", "nomio": "app.nomio.finance"}
NAMES = {"welegato": "welegato", "leggii": "Leggii", "appoggio": "Appoggio", "chiave": "Chiave", "pianino": "Pianino", "prova": "Prova", "squillo": "Squillo", "nomio": "Nomio"}
SOON = {"chiave", "prova", "squillo"}
LEGAL_ONLY = {"chiave", "prova"}  # 2026-11-09 법문 페이지만 먼저 연결

import site_i18n as I
import famiglia
TXT = {}
for _l in I.LANGS:
    _h = dict(I.HOME[_l]); _f = famiglia.T[_l]
    _h["home"] = I.home_path(_l); _h["fam_href"] = I.fam_path(_l)
    _h["soon"] = _f["soon"]; _h["play"] = "Google Play"
    _h["d"] = dict(_f["d"]); _h["d"]["nomio"] = _h["nomio"]
    TXT[_l] = _h

LANG_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9.2"/><ellipse cx="12" cy="12" rx="4" ry="9.2"/><path d="M3 12h18"/></svg>'

def lang_menu(lang, alt):
    """언어 메뉴 — 이 페이지의 다른 언어판이 있으면 그리로, 없으면 그 언어 첫 화면으로."""
    items = "".join(f'<a href="{(alt or {}).get(l, I.home_path(l))}" hreflang="{l}" lang="{l}"{" class=on" if l == lang else ""}>{I.LANG_NAMES[l]}</a>' for l in I.LANGS)
    return f'<details class="lang"><summary aria-label="Language">{LANG_ICON}<span>{lang.upper()}</span></summary><div class="menu">{items}</div></details>'

def card(lang, key):
    t = TXT[lang]
    ext = ' target="_blank" rel="noopener"'  # 사이트 밖 링크만 새 탭
    soon = key in SOON
    links = []
    if key == "welegato":
        links.append(f'<a href="{I.welegato_url(lang)}"{ext}>{t["site"]} →</a>')
    if key in STORE:
        links.append(f'<a href="{PLAY}{STORE[key]}"{ext}>{t["play"]}</a>')
        if key in APPLE:
            links.append(f'<a href="https://apps.apple.com/app/id{APPLE[key]}"{ext}>App Store</a>')
        links.append(f'<a href="/{key}/">{t["privacy_l"]}</a>')
    elif key in LEGAL_ONLY:  # 출시 전(Bald) 앱: 법문 링크만, Play 링크는 출시 후 STORE에 추가
        links.append(f'<a href="/{key}/">{t["privacy_l"]}</a>')
    badge = f' <span class="soon">{t["soon"]}</span>' if soon else ""
    return (f'<div class="card"><img src="/apps/{key}.png" alt="" width="72" height="72" loading="lazy">'
            f'<div><h3>{NAMES[key]}{badge}</h3><p>{t["d"][key]}</p><div class="links">{"".join(links)}</div></div></div>')

def home(lang):
    t = TXT[lang]
    strip = "".join(f'<img src="/apps/{k}.png" alt="{NAMES[k]}" width="46" height="46">' for k in MUSIC + ["nomio"])
    music = "".join(card(lang, k) for k in MUSIC)
    values = "".join(f'<div><b>{h}</b><span>{d}</span></div>' for h, d in t["values"])
    return (f'<div class="hero"><p class="kicker">{t["kicker"]}</p><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p><div class="icons">{strip}</div></div>'
            f'<section id="apps"><h2>{t["music_h"]}</h2><p class="sub">{t["music_sub"]} <a href="{t["fam_href"]}" style="font-weight:600;text-decoration:none">{t["fam_link"]}</a></p><div class="grid">{music}</div></section>'
            f'<section><h2>{t["life_h"]}</h2><p class="sub"></p><div class="grid">{card(lang, "nomio")}</div></section>'
            f'<div class="values">{values}</div>'
            f'<div class="contact"><h2>{t["contact_h"]}</h2><p class="sub" style="margin:0">{t["contact"]}</p><a class="btn" href="mailto:{EMAIL}">{t["btn"]}</a></div>')

IMPRESSUM = f"""<h1 style="font-size:28px">Impressum</h1>
<p class="lead">Angaben gemäß § 5 DDG</p>
<dl>
<dt>Anbieter</dt><dd>Vicino Labs (Einzelunternehmen, Inh. Jeong-Hwan Lee)</dd>
<dt>Anschrift</dt><dd>Ruhrallee 41, 44139 Dortmund, Deutschland</dd>
<dt>E-Mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Kontaktformular</dt><dd><a href="https://welegato.com/kontakt/?lang=de" target="_blank" rel="noopener">welegato.com/kontakt</a></dd>
<dt>Handelsregister</dt><dd>entfällt (nicht eingetragenes Einzelunternehmen)</dd>
<dt>Umsatzsteuer</dt><dd>Kleinunternehmer gemäß § 19 UStG – es wird keine Umsatzsteuer berechnet.</dd>
<dt>Verantwortlich für den Inhalt gemäß § 18 Abs. 2 MStV</dt><dd>Jeong-Hwan Lee, Anschrift wie oben</dd>
</dl>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht verpflichtet und nicht bereit, an einem Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<p style="color:var(--soft);font-size:14px">Legal notice (German law). The operator is Vicino Labs, a sole proprietorship of Jeong-Hwan Lee, Ruhrallee 41, 44139 Dortmund, Germany.</p>"""

PRIVACY = f"""<h1>Datenschutzerklärung</h1>
<p class="lead">Stand: 27.09.2026</p>
<p>Verantwortlich für diese Website ist Vicino Labs. Anschrift und Kontaktdaten finden Sie <a href="#verantwortlicher">am Ende dieser Seite</a> und im <a href="/impressum/">Impressum</a>.</p>
<h2>Hosting</h2>
<p>Diese Website wird über GitHub Pages bereitgestellt (GitHub Inc., 88 Colin P. Kelly Jr. St., San Francisco, CA 94107, USA). Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie Ihre IP-Adresse, Datum und Uhrzeit sowie die aufgerufene Seite, um die Website auszuliefern und vor Missbrauch zu schützen (Art. 6 Abs. 1 lit. f DSGVO). GitHub ist unter dem EU-US Data Privacy Framework zertifiziert. Weitere Informationen: <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>
<h2>Keine Cookies, kein Tracking</h2>
<p>Diese Website setzt keine Cookies, verwendet keine Analyse- oder Werbedienste und lädt keine Schriften oder Skripte von Drittanbietern.</p>
<h2>Kontakt per E-Mail</h2>
<p>Wenn Sie uns per E-Mail schreiben, verarbeiten wir Ihre Angaben, um Ihre Anfrage zu beantworten (Art. 6 Abs. 1 lit. b bzw. f DSGVO), und löschen sie, wenn sie nicht mehr erforderlich sind. Unser E-Mail-Postfach wird von IONOS SE (Montabaur, Deutschland) betrieben.</p>
<h2>Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO) sowie auf Beschwerde bei einer Aufsichtsbehörde, z. B. der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen.</p>
<h2 id="verantwortlicher">Verantwortlicher</h2>
<p style="color:var(--soft);font-size:14px">Vicino Labs, Inh. Jeong-Hwan Lee, Ruhrallee 41, 44139 Dortmund, Deutschland · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="color:var(--soft);font-size:14px">Our apps have their own privacy policies, linked in each app and on its website.</p>"""

def write(path, html):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)

alt = {l: I.home_path(l) for l in I.LANGS}
for lang, path in alt.items():
    write(path, page(lang, path, TXT[lang]["title"], TXT[lang]["desc"], home(lang), alt, wide=True))
# Famiglia Vicino 포트폴리오(2026-11-10) — famiglia.py, 8개 언어
FAM_ALT = {l: famiglia.T[l]["path"] for l in I.LANGS}
for _l in I.LANGS:
    _t = famiglia.T[_l]
    write(_t["path"], page(_l, _t["path"], _t["title"], _t["desc"], famiglia.body(_l, SOON), FAM_ALT, wide=True))
write("/impressum/", page("de", "/impressum/", "Impressum — Vicino Labs", "Impressum von Vicino Labs.", IMPRESSUM))
write("/datenschutz/", page("de", "/datenschutz/", "Datenschutzerklärung — Vicino Labs", "Datenschutzerklärung von vicinolabs.com.", PRIVACY))
# Nomio 개인정보처리방침·이용약관 (/nomio/privacy/, /nomio/terms/) — nomio_legal.py
import nomio_legal
nomio_legal.build(os.path.dirname(os.path.abspath(__file__)))
# Appoggio 개인정보처리방침·이용약관 (/appoggio/privacy/, /appoggio/terms/) — appoggio_legal.py
import appoggio_legal
appoggio_legal.build(os.path.dirname(os.path.abspath(__file__)))
# Leggii(렛지 악보) 개인정보처리방침·이용약관 (/leggii/privacy/, /leggii/terms/) — leggii_legal.py
import leggii_legal
leggii_legal.build(os.path.dirname(os.path.abspath(__file__)))
# 끼아베(Chiave) 개인정보처리방침·이용약관 (/chiave/privacy/, /chiave/terms/) — chiave_legal.py (2026-11-06 초안)
import chiave_legal
chiave_legal.build(os.path.dirname(os.path.abspath(__file__)))
# 프로바(Prova) 개인정보처리방침·이용약관 (/prova/privacy/, /prova/terms/) — prova_legal.py (2026-11-07 초안)
import prova_legal
prova_legal.build(os.path.dirname(os.path.abspath(__file__)))
# Pianino 개인정보처리방침·이용약관 (/pianino/privacy/, /pianino/terms/) — pianino_legal.py (2026-11-07 초안)
import pianino_legal
pianino_legal.build(os.path.dirname(os.path.abspath(__file__)))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "CNAME"), "w").write("vicinolabs.com\n")
print("ok")
