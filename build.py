#!/usr/bin/env python3
"""vicinolabs.com — Vicino Labs 회사 페이지(2026-09-27). GitHub Pages로
올린다(무료 HTTPS). 메일(MX)은 IONOS 그대로. 고친 뒤 python3 build.py."""
import os

EMAIL = "contact@vicinolabs.com"
CSS = """
:root{--bg:#f6f3ee;--paper:#fffdf9;--ink:#1b1917;--soft:#6b635b;--line:#e5ddd1;--accent:#6e1a2f;--gold:#b08d57}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141211;--paper:#1c1a18;--ink:#efe9e1;--soft:#a79d92;--line:#2e2a26;--accent:#d88a9c;--gold:#c9a66b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line)}.nav{display:flex;justify-content:space-between;align-items:center;padding:18px 0;gap:12px}
.brand{display:inline-flex;align-items:center;gap:10px;font-family:Georgia,"Times New Roman",serif;font-size:24px;letter-spacing:.01em;color:var(--ink);text-decoration:none}.brand img{height:32px;width:auto;display:block}
.nav nav{display:flex;gap:16px;font-size:14px}.nav nav a{color:var(--soft);text-decoration:none}.nav nav a:hover{color:var(--ink)}
h1{font-family:Georgia,"Times New Roman",serif;font-weight:500;font-size:clamp(30px,5vw,44px);line-height:1.2;margin:56px 0 14px;letter-spacing:-.01em}
h2{font-family:Georgia,"Times New Roman",serif;font-weight:500;font-size:24px;margin:44px 0 14px}
.lead{font-size:18px;color:var(--soft);margin:0 0 8px}
.apps{display:grid;gap:14px}.app{background:var(--paper);border:1px solid var(--line);padding:20px 22px;border-radius:4px}
.app b{font-size:18px}.app p{margin:6px 0 10px;color:var(--soft)}.app a{font-weight:600;text-decoration:none}
dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 16px;margin:0;font-size:14.5px;color:var(--soft)}dt{color:var(--soft)}dd{margin:0}
@media(max-width:520px){dl{grid-template-columns:1fr}dt{margin-top:8px}}
footer{border-top:1px solid var(--line);margin-top:64px;padding:24px 0 40px;font-size:13.5px;color:var(--soft)}
footer a{color:var(--soft);margin-right:16px}
"""

def page(lang, path, title, desc, body, alt=None):
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
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap nav"><a class="brand" href="{t['home']}"><img src="/logo.png" alt="" width="58" height="32">Vicino Labs</a>
<nav><a href="{t['home']}#apps">{t['apps_nav']}</a><a href="/impressum/">Impressum</a><a href="{t['other_href']}">{t['other']}</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><a href="/impressum/">Impressum</a><a href="/datenschutz/">{t['privacy']}</a><a href="mailto:{EMAIL}">{EMAIL}</a><div style="margin-top:10px">© 2026 Vicino Labs · Dortmund</div></div></footer>
</body></html>
"""

TXT = {
 "de": {"home": "/", "apps_nav": "Apps", "other": "English", "other_href": "/en/", "privacy": "Datenschutz",
  "title": "Vicino Labs — Apps aus Dortmund",
  "desc": "Vicino Labs entwickelt Apps für den Alltag und für Musikerinnen und Musiker: welegato und Nomio.",
  "h1": "Apps, die im Alltag helfen.",
  "lead": "Vicino Labs ist ein kleines Softwarestudio aus Dortmund. Wir entwickeln Apps für Musikerinnen und Musiker und für den Alltag — mehrsprachig und mit Blick auf Datenschutz.",
  "apps": [
   ("welegato", "Musikunterricht, Korrepetition und Musiker in Deutschland und Österreich finden — mit automatischer Übersetzung im Chat.", "https://welegato.com/", "welegato.com →"),
   ("Nomio", "Haushaltsbuch für Einnahmen und Ausgaben in vielen Währungen und Sprachen.", "https://play.google.com/store/apps/details?id=app.nomio.finance", "Google Play →"),
  ],
  "contact_h": "Kontakt", "contact": f'Fragen, Kooperationen oder Presse: <a href="mailto:{EMAIL}">{EMAIL}</a>'},
 "en": {"home": "/en/", "apps_nav": "Apps", "other": "Deutsch", "other_href": "/", "privacy": "Privacy",
  "title": "Vicino Labs — Apps from Dortmund, Germany",
  "desc": "Vicino Labs builds apps for everyday life and for musicians: welegato and Nomio.",
  "h1": "Apps that help in everyday life.",
  "lead": "Vicino Labs is a small software studio in Dortmund, Germany. We build apps for musicians and for everyday life — multilingual and privacy-minded.",
  "apps": [
   ("welegato", "Find music teachers, accompanists and musicians in Germany and Austria — with automatic chat translation.", "https://welegato.com/en/", "welegato.com →"),
   ("Nomio", "A budget book for income and expenses in many currencies and languages.", "https://play.google.com/store/apps/details?id=app.nomio.finance", "Google Play →"),
  ],
  "contact_h": "Contact", "contact": f'Questions, partnerships or press: <a href="mailto:{EMAIL}">{EMAIL}</a>'},
}

def home(lang):
    t = TXT[lang]
    apps = "".join(f'<div class="app"><b>{n}</b><p>{d}</p><a href="{u}" target="_blank" rel="noopener">{l}</a></div>' for n, d, u, l in t["apps"])
    return f'<h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p><h2 id="apps">Apps</h2><div class="apps">{apps}</div><h2>{t["contact_h"]}</h2><p>{t["contact"]}</p>'

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

alt = {"de": "/", "en": "/en/"}
for lang, path in alt.items():
    write(path, page(lang, path, TXT[lang]["title"], TXT[lang]["desc"], home(lang), alt))
write("/impressum/", page("de", "/impressum/", "Impressum — Vicino Labs", "Impressum von Vicino Labs, Dortmund.", IMPRESSUM))
write("/datenschutz/", page("de", "/datenschutz/", "Datenschutzerklärung — Vicino Labs", "Datenschutzerklärung von vicinolabs.com.", PRIVACY))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "CNAME"), "w").write("vicinolabs.com\n")
print("ok")
