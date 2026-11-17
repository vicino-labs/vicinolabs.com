#!/usr/bin/env python3
"""렛지 Plus 구독 — vicinolabs.com/leggii/plus/ 와 .../plus/danke/ (2026-11-17).

홈페이지에서 바로 위레가토 아이디로 가입·로그인하고 스트라이프로 결제한다.
앱 안에서는 이 쪽으로 유도하지 않는다(애플·구글 안티스티어링). 홈페이지 안에서는
가입·구매 경로가 잘 보이게 둔다(대표님, HQ 2026-11-17).

- 로그인: Supabase Auth REST 를 fetch 로 직접 부른다. 바깥 스크립트를 한 줄도
  불러오지 않는다(사이트 Datenschutz 에 그렇게 적혀 있다).
- 가격은 화면에 보여 주기만 하고, 실제 금액은 엣지 함수 web-checkout 이 서버에서 정한다.
- 유럽만 받는다. 화면에서 시간대로 먼저 거르고(아니면 스토어로 보냄), 진짜 판단은
  stripe-webhook 이 청구 국가로 한다. 영국은 제외.

build.py 가 leggii_legal.py 를 통해 부른다.
"""

import leggii_site as S

SUPABASE_URL = "https://zowwxefjkvklmzzzznvr.supabase.co"
# 공개용 키(publishable). 비밀값이 아니다 — 브라우저에 넣으라고 만든 키다.
SUPABASE_KEY = "sb_publishable_GWm8fIiIeGt33SiRdQbXAg_aUiwMUQz"

LANGS = S.LANGS
PLAY, APPLE, EMAIL = S.PLAY, S.APPLE, S.EMAIL

# 50GB 는 어느 스토어에도 없는 새 상품이라 대표님 결정 전까지 화면에 내보내지 않는다
# (HQ 2026-11-17). 서버(web-checkout)도 hidden 상품은 거절한다. 정해지면 True 로.
SHOW_50 = False

# 가격은 스토어와 같다(HQ, 대표님 확인 2026-11-17). 화면 표시용.
# 센트로 둔다. 화면에서는 그 나라 꼴로 찍는다(ko/en €3.99, de 3,99 €).
PRICES = {
    "plus-10-month": 399, "plus-10-year": 3999,
    "plus-50-month": 599, "plus-50-year": 5999,
}

CSS = S.CSS + """
.buy{max-width:720px;margin:0 auto;padding:44px 0 0}
.buy h1{font-size:clamp(30px,4.6vw,46px);margin:0 0 10px}
.buy .lede{color:var(--soft);font-size:17px;margin:0 0 30px}
.step{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:24px;margin:0 0 16px}
.step h2{font-size:20px;margin:0 0 4px}
.step .hint{color:var(--soft);font-size:14.5px;margin:0 0 16px}
.sizes{display:inline-flex;border:1px solid var(--line);border-radius:999px;padding:3px;background:var(--bg);margin:0 0 14px}
.sizes button{border:0;background:transparent;color:var(--soft);font:600 13.5px/1 inherit;font-family:inherit;padding:9px 16px;border-radius:999px;cursor:pointer}
.sizes button.on{background:var(--ink);color:var(--bg)}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:560px){.opts{grid-template-columns:1fr}}
.opt{border:1px solid var(--line);border-radius:14px;padding:16px 18px;background:var(--bg);cursor:pointer;text-align:left;font:inherit;color:inherit;display:block;width:100%}
.opt.on{border-color:var(--gold);box-shadow:0 0 0 1px var(--gold) inset}
.opt b{display:block;font-family:Georgia,serif;font-size:21px;font-weight:500}
.opt span{display:block;color:var(--soft);font-size:13.5px;margin-top:2px}
.opt .save{color:var(--gold);font-weight:600}
.incl{margin:16px 0 0;padding:0;list-style:none}
.incl li{position:relative;padding-left:18px;color:var(--soft);font-size:15px;margin:6px 0}
.incl li::before{content:"";position:absolute;left:1px;top:.7em;width:5px;height:5px;border-radius:50%;background:var(--goldl)}
label.f{display:block;font-size:13px;color:var(--soft);margin:12px 0 4px}
input[type=email],input[type=password]{width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--bg);color:var(--ink);font:inherit;font-size:15px}
.btn{display:inline-block;background:var(--accent);color:#fff;border:0;border-radius:999px;padding:13px 26px;font:600 15.5px/1 inherit;font-family:inherit;cursor:pointer;text-decoration:none}
.btn[disabled]{opacity:.45;cursor:default}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:16px}
.social{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:14px 0 0}
@media(max-width:480px){.social{grid-template-columns:1fr}}
.social button{border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:12px;padding:11px 10px;font:600 14px/1 inherit;font-family:inherit;cursor:pointer}
.sep{display:flex;align-items:center;gap:12px;color:var(--faint);font-size:12.5px;margin:18px 0 4px}
.sep::before,.sep::after{content:"";flex:1;height:1px;background:var(--line)}
.waiver{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:var(--soft);margin:4px 0 0}
.waiver input{margin-top:5px;flex:none}
.msg{margin:14px 0 0;font-size:14.5px;border-radius:12px;padding:12px 14px;background:var(--tint);color:var(--ink)}
.msg.bad{color:var(--accent)}
.who{font-size:14px;color:var(--soft)}
.who b{color:var(--ink)}
.fine{color:var(--faint);font-size:13px;margin:16px 0 0}
.fine a{color:var(--faint)}
.outside .stores{justify-content:flex-start;margin-top:16px}
.hidden{display:none!important}
"""


T = {
"ko": {
 "title": "Leggii Plus 구독 | 렛지 악보 · Vicino Labs",
 "desc": "렛지 Plus를 홈페이지에서 바로 구독하세요. 위레가토 아이디로 가입하고, 앱에서 같은 아이디로 로그인하면 열립니다.",
 "h1": "Leggii Plus",
 "lede": "레슨은 AI가 정리하고, 악보와 녹음은 어느 기기에서나 그대로입니다. 여기서 구독하신 뒤 앱에서 같은 위레가토 아이디로 로그인하시면 됩니다.",
 "s1": "1. 요금제 고르기", "s1h": "결제 주기를 고르세요. 가격은 앱 스토어·구글 플레이와 같습니다.",
 "size10": "클라우드 10GB", "size50": "클라우드 50GB",
 "month": "월간", "year": "연간", "per_month": "월", "per_year": "년",
 "save": "2개월 무료",
 "incl_h": "Plus에 들어 있는 것",
 "incl": ["Pro 기능 전부, 광고 없음", "매월 AI 분석 5시간", "렛지 클라우드: 악보·필기·폴더·연주목록·녹음이 모든 기기에서 똑같이 유지됩니다"],
 "s2": "2. 위레가토 아이디", "s2h": "위레가토 아이디 하나로 Vicino Labs 앱을 모두 쓰실 수 있습니다. 이미 있으시면 그대로 로그인하세요.",
 "email": "이메일", "pw": "비밀번호",
 "login": "로그인", "signup": "가입하기", "or": "또는",
 "toggle_signup": "처음이신가요? 가입하기", "toggle_login": "이미 아이디가 있으신가요? 로그인",
 "logged": "로그인했습니다", "logout": "로그아웃",
 "s3": "3. 결제", "s3h": "카드 결제는 스트라이프가 처리합니다.",
 "waiver": "지금 바로 구독을 시작하는 데 동의하며, 그에 따라 청약철회권이 사라진다는 점을 확인합니다(독일 민법 제356조 제5항).",
 "pay": "구독하기",
 "vat": "소규모사업자로 부가가치세는 붙지 않습니다(독일 부가가치세법 제19조).",
 "renew": "결제가 끝나면 바로 이용하실 수 있습니다. 구독은 자동으로 갱신되며, 다음 결제일 전까지 언제든 해지하실 수 있습니다.",
 "have": "이 아이디로 이미 Plus를 쓰고 있습니다.",
 "until": "다음 결제일", "ending": "이 날짜까지 이용하실 수 있습니다",
 "manage": "구독 관리·해지",
 "out_h": "홈페이지 결제는 지금 유럽에서만 받습니다",
 "out_p": "앱 스토어나 구글 플레이에서 구독해 주세요. 앱에서 구독하셔도 똑같이 쓰실 수 있습니다.",
 "out_link": "유럽에서 결제하시나요?",
 "err": {"waiver": "위 항목에 동의해 주세요.", "login": "이메일 또는 비밀번호가 맞지 않습니다.",
         "signup": "가입할 수 없습니다. 이미 가입된 이메일인지 확인해 주세요.",
         "confirm": "메일로 보내 드린 링크로 이메일 인증을 마친 뒤 로그인해 주세요.",
         "already_subscribed": "이미 구독 중입니다.", "app_store_only": "홈페이지 결제는 유럽에서만 받습니다.",
         "store_subscribed": "앱 스토어에서 이미 구독 중입니다.", "no_subscription": "구독 내역을 찾을 수 없습니다.", "interval_mismatch": "월간은 월간으로, 연간은 연간으로만 변경하실 수 있습니다.", "captcha": "사람인지 확인하는 절차를 마치지 못했습니다. 위 확인 상자를 눌러 주세요.",
         "too_many": "시도가 너무 잦습니다. 잠시 뒤에 다시 해 주세요.",
         "taken": "이미 가입된 이메일입니다. 로그인해 주세요.",
         "weak": "비밀번호가 너무 짧습니다. 여섯 자 이상으로 해 주세요.",
         "other": "잠시 후 다시 시도해 주세요."},
  "cloud_note": "클라우드는 10GB로 시작합니다. 나중에 '나의 구독'에서 50GB로 올리실 수 있습니다.",
 "launch_price": "출시 가격입니다. 2027년 12월 31일까지 구독을 시작하시면 구독하시는 동안 이 가격이 그대로 유지됩니다.",
 "acc_h": "나의 구독",
 "acc_plan": "현재 요금제",
 "acc_next": "다음 결제일",
 "acc_ends": "이 날짜까지 이용하실 수 있습니다",
 "acc_up": "50GB로 올리기",
 "acc_up_note": "바로 바뀌고, 남은 기간에 대한 차액만 결제됩니다.",
 "acc_cancel": "해지하기",
 "acc_cancel_note": "해지하시면 다음 결제일에 자동 결제되지 않으며, 남은 이용 기간 동안 그대로 이용하실 수 있습니다.",
 "acc_resume": "해지 취소",
 "acc_quota_note": "저장 공간이 차면 새로 올리는 것만 멈추고 이미 올린 파일은 지우지 않습니다. 기기에 있는 파일도 그대로입니다.",
 "acc_end_note": "Plus가 끝나면 새로 올리는 것은 멈추고 90일 동안 내려받으실 수 있습니다. 메일로 두 번 알려 드린 뒤 클라우드의 파일을 지웁니다. 기기에 있는 악보와 녹음은 그대로 남습니다.",
 "acc_store": "앱 스토어에서 구독 중입니다. 변경과 해지는 구독하신 스토어에서 하실 수 있습니다.",
 "acc_benefit": "위레가토 회원 혜택으로 Plus를 쓰고 계십니다.",
 "acc_portal": "결제 내역 · 결제 수단 변경",
 "done": "변경되었습니다.",
 "back": "렛지 소개로",
 "privacy": "개인정보처리방침", "terms": "이용약관",
 "thanks_title": "구독이 시작되었습니다 | 렛지 악보",
 "thanks_h": "구독이 시작되었습니다", "thanks_p": "영수증을 메일로 보내 드렸습니다.",
 "thanks_id": "구독한 아이디", "thanks_get": "앱 받기", "thanks_manage": "구독 관리",
},
"en": {
 "title": "Leggii Plus subscription | Vicino Labs",
 "desc": "Subscribe to Leggii Plus here. Sign up with your welegato ID and sign in to the app with the same ID.",
 "h1": "Leggii Plus",
 "lede": "The AI writes up your lessons, and your scores and recordings are the same on every device. Subscribe here, then sign in to the app with the same welegato ID.",
 "s1": "1. Choose a plan", "s1h": "Monthly or yearly. The price is the same as on the App Store and Google Play.",
 "size10": "10 GB cloud", "size50": "50 GB cloud",
 "month": "Monthly", "year": "Yearly", "per_month": "a month", "per_year": "a year",
 "save": "Two months free",
 "incl_h": "What Plus includes",
 "incl": ["Every Pro feature, no ads", "5 hours of AI analysis a month", "Leggii cloud: scores, ink, folders, setlists and recordings in sync on every device"],
 "s2": "2. welegato ID", "s2h": "One welegato ID for the Vicino Labs apps. Already have one? Just sign in.",
 "email": "Email", "pw": "Password",
 "login": "Sign in", "signup": "Create account", "or": "or",
 "toggle_signup": "New here? Create an account", "toggle_login": "Already have a welegato ID? Sign in",
 "logged": "Signed in", "logout": "Sign out",
 "s3": "3. Payment", "s3h": "Stripe handles the card payment.",
 "waiver": "I want the subscription to start right away and understand that my right of withdrawal lapses (§ 356(5) German Civil Code).",
 "pay": "Subscribe",
 "vat": "No VAT is charged (small business, § 19 German VAT Act).",
 "renew": "You can start as soon as the payment goes through. The subscription renews automatically and you can cancel any time before the next billing date.",
 "have": "This ID already has Plus.",
 "until": "Next billing date", "ending": "Runs until",
 "manage": "Manage subscription",
 "out_h": "We can only take website payments in Europe at the moment",
 "out_p": "Please subscribe on the App Store or Google Play. A subscription from the app works exactly the same.",
 "out_link": "Paying from Europe?",
 "err": {"waiver": "Please tick the box above first.", "login": "That email or password does not match.",
         "signup": "Could not create the account. Perhaps the email is already in use.",
         "confirm": "Check your inbox and open the link, then sign in.",
         "already_subscribed": "You are already subscribed.", "app_store_only": "Website payment is only for Europe.",
         "store_subscribed": "You are already subscribed through an app store.", "no_subscription": "No subscription found.", "interval_mismatch": "You can only move up within the same billing period.", "captcha": "The check that you are human did not finish. Please tick the box above.",
         "too_many": "Too many attempts. Please wait a moment and try again.",
         "taken": "That email already has an account. Please sign in.",
         "weak": "That password is too short. Please use at least six characters.",
         "other": "Something went wrong. Please try again in a moment."},
  "cloud_note": "The cloud starts at 10 GB. You can move up to 50 GB later on your subscription page.",
 "launch_price": "This is the launch price: subscribe before 31 December 2027 and it stays at this price for as long as your subscription runs.",
 "acc_h": "Your subscription",
 "acc_plan": "Current plan",
 "acc_next": "Next billing date",
 "acc_ends": "Runs until",
 "acc_up": "Move up to 50 GB",
 "acc_up_note": "It changes right away and you only pay the difference for the time left.",
 "acc_cancel": "Cancel",
 "acc_cancel_note": "After you cancel, nothing is taken on the next billing date and Plus keeps working until the end of the period you paid for.",
 "acc_resume": "Keep the subscription",
 "acc_quota_note": "When the cloud is full, only new uploads stop and nothing is deleted. Files on your device are never touched.",
 "acc_end_note": "When Plus ends, new uploads stop, everything can be downloaded for 90 days, and after two reminder emails the cloud files are deleted. Scores and recordings on your device stay.",
 "acc_store": "You subscribe through an app store. Changes and cancellation happen in the store you subscribed with.",
 "acc_benefit": "You have Plus through your welegato membership.",
 "acc_portal": "Invoices and payment method",
 "done": "Done.",
 "back": "Back to Leggii",
 "privacy": "Privacy Policy", "terms": "Terms of Service",
 "thanks_title": "Your subscription is active | Leggii",
 "thanks_h": "Your subscription is active", "thanks_p": "We have sent the receipt to your inbox.",
 "thanks_id": "Subscribed with", "thanks_get": "Get the app", "thanks_manage": "Manage subscription",
},
"de": {
 "title": "Leggii Plus Abo | Vicino Labs",
 "desc": "Leggii Plus direkt hier abonnieren. Mit der welegato-ID anmelden und sich in der App mit derselben ID anmelden.",
 "h1": "Leggii Plus",
 "lede": "Die KI fasst Ihren Unterricht zusammen, und Noten und Aufnahmen sind auf jedem Gerät dieselben. Hier abonnieren, dann in der App mit derselben welegato-ID anmelden.",
 "s1": "1. Tarif wählen", "s1h": "Monatlich oder jährlich. Der Preis ist derselbe wie im App Store und bei Google Play.",
 "size10": "10 GB Cloud", "size50": "50 GB Cloud",
 "month": "Monatlich", "year": "Jährlich", "per_month": "im Monat", "per_year": "im Jahr",
 "save": "2 Monate gratis",
 "incl_h": "In Plus enthalten",
 "incl": ["Alle Pro-Funktionen, keine Werbung", "5 Stunden KI-Analyse im Monat", "Leggii Cloud: Noten, Notizen, Ordner, Setlists und Aufnahmen auf allen Geräten synchron"],
 "s2": "2. welegato-ID", "s2h": "Mit einer welegato-ID nutzen Sie alle Apps von Vicino Labs. Wenn Sie schon eine haben, melden Sie sich einfach an.",
 "email": "E-Mail", "pw": "Passwort",
 "login": "Anmelden", "signup": "Konto erstellen", "or": "oder",
 "toggle_signup": "Noch keine welegato-ID? Konto erstellen", "toggle_login": "Sie haben schon eine welegato-ID? Anmelden",
 "logged": "Angemeldet", "logout": "Abmelden",
 "s3": "3. Bezahlen", "s3h": "Die Kartenzahlung übernimmt Stripe.",
 "waiver": "Ich verlange ausdrücklich, dass Sie vor Ablauf der Widerrufsfrist mit der Leistung beginnen. Mir ist bekannt, dass ich damit mein Widerrufsrecht verliere (§ 356 Abs. 5 BGB).",
 "pay": "Zahlungspflichtig abonnieren",
 "vat": "Gemäß § 19 UStG wird keine Umsatzsteuer berechnet (Kleinunternehmer).",
 "renew": "Nach der Zahlung steht Ihnen Plus sofort zur Verfügung. Das Abo verlängert sich automatisch und ist jederzeit bis zur nächsten Abbuchung kündbar.",
 "have": "Diese ID hat Plus bereits.",
 "until": "Nächste Abbuchung", "ending": "Läuft noch bis",
 "manage": "Abo verwalten",
 "out_h": "Über die Website können wir derzeit nur in Europa abrechnen",
 "out_p": "Bitte abonnieren Sie im App Store oder bei Google Play. Ein Abo aus der App funktioniert genauso.",
 "out_link": "Sie zahlen aus Europa?",
 "err": {"waiver": "Bitte setzen Sie oben zuerst das Häkchen.", "login": "E-Mail oder Passwort stimmen nicht.",
         "signup": "Das Konto konnte nicht angelegt werden. Vielleicht ist die E-Mail schon vergeben.",
         "confirm": "Bitte öffnen Sie den Link in Ihrer E-Mail und melden Sie sich dann an.",
         "already_subscribed": "Sie haben bereits ein Abo.", "app_store_only": "Die Zahlung über die Website gibt es nur in Europa.",
         "store_subscribed": "Sie haben bereits ein Abo über einen App-Store.", "no_subscription": "Kein Abo gefunden.", "interval_mismatch": "Ein Wechsel ist nur innerhalb desselben Abrechnungszeitraums möglich.", "captcha": "Die Prüfung, ob Sie ein Mensch sind, wurde nicht abgeschlossen. Bitte setzen Sie oben das Häkchen.",
         "too_many": "Zu viele Versuche. Bitte warten Sie einen Moment.",
         "taken": "Für diese E-Mail gibt es schon ein Konto. Bitte melden Sie sich an.",
         "weak": "Das Passwort ist zu kurz. Bitte mindestens sechs Zeichen.",
         "other": "Das hat nicht geklappt. Bitte versuchen Sie es gleich noch einmal."},
  "cloud_note": "Die Cloud startet mit 10 GB. Auf 50 GB können Sie später unter „Mein Abo“ wechseln.",
 "launch_price": "Das ist der Einführungspreis: Wenn Sie bis zum 31. Dezember 2027 abonnieren, bleibt er für die Dauer Ihres Abos bestehen.",
 "acc_h": "Mein Abo",
 "acc_plan": "Aktueller Tarif",
 "acc_next": "Nächste Abbuchung",
 "acc_ends": "Läuft noch bis",
 "acc_up": "Auf 50 GB wechseln",
 "acc_up_note": "Gilt sofort; berechnet wird nur die Differenz für die restliche Zeit.",
 "acc_cancel": "Kündigen",
 "acc_cancel_note": "Nach der Kündigung wird nichts mehr abgebucht. Bis zum Ende des bezahlten Zeitraums können Sie Plus weiter nutzen.",
 "acc_resume": "Kündigung zurücknehmen",
 "acc_quota_note": "Ist die Cloud voll, stoppen nur neue Uploads, es wird nichts gelöscht. Dateien auf Ihrem Gerät bleiben unangetastet.",
 "acc_end_note": "Endet Plus, stoppen neue Uploads; 90 Tage lang kann alles heruntergeladen werden, nach zwei Erinnerungs-E-Mails werden die Cloud-Dateien gelöscht. Noten und Aufnahmen auf dem Gerät bleiben.",
 "acc_store": "Sie haben das Abo über einen App-Store. Ändern und kündigen können Sie es dort, wo Sie es abgeschlossen haben.",
 "acc_benefit": "Sie haben Plus über Ihre welegato-Mitgliedschaft.",
 "acc_portal": "Rechnungen und Zahlungsart",
 "done": "Erledigt.",
 "back": "Zurück zu Leggii",
 "privacy": "Datenschutzerklärung", "terms": "Nutzungsbedingungen",
 "thanks_title": "Ihr Abo ist aktiv | Leggii",
 "thanks_h": "Ihr Abo ist aktiv", "thanks_p": "Die Rechnung haben wir Ihnen per E-Mail geschickt.",
 "thanks_id": "Abonniert mit", "thanks_get": "App laden", "thanks_manage": "Abo verwalten",
},
}


def _badges():
    return "".join(f'<div data-l="{l}" class="stores{S._on(l)}" style="justify-content:flex-start">{S.badge(l)}</div>'
                   for l, _ in LANGS)


def _head(title, desc, path, extra=""):
    buttons = "".join(f'<button type="button" data-set="{l}"{" class=on" if l == "en" else ""}>{n}</button>'
                      for l, n in LANGS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="https://vicinolabs.com{path}">
<meta name="robots" content="noindex">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="stylesheet" href="/fonts/fonts-v2.css">
<style>{CSS}{extra}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/leggii/"><img src="/logo.png" alt="" width="47" height="26">Vicino&nbsp;Labs</a>
<div class="langbar" role="group" aria-label="Language">{buttons}</div></div></div>
"""


FOOT = f"""<footer><div class="wrap"><p style="margin:0">
<a href="/leggii/">Leggii</a><a href="/leggii/privacy/" data-t="privacy"></a><a href="/leggii/terms/" data-t="terms"></a>
<a href="/impressum/">Impressum</a><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<div style="margin-top:10px">© 2026 Vicino Labs</div></div></footer>"""


COMMON_JS = f"""
var SB="{SUPABASE_URL}",KEY="{SUPABASE_KEY}",APP="leggii",TITLE_KEY="title";
var T=__T__,L=["ko","en","de"],lang="en";
function pick(){{var k="vl-app-lang",s=null;try{{s=localStorage.getItem(k)}}catch(e){{}}
var h=(location.hash||"").slice(1).split("&")[0],n=(navigator.language||"en").slice(0,2);
return L.indexOf(h)>=0?h:(L.indexOf(s)>=0?s:(L.indexOf(n)>=0?n:"en"));}}
function setLang(x){{lang=x;document.documentElement.lang=x;
try{{localStorage.setItem("vl-app-lang",x)}}catch(e){{}}
document.querySelectorAll("[data-l]").forEach(function(e){{e.classList.toggle("on",e.getAttribute("data-l")===x)}});
document.querySelectorAll("[data-set]").forEach(function(b){{b.classList.toggle("on",b.getAttribute("data-set")===x)}});
document.querySelectorAll("[data-t]").forEach(function(e){{var v=T[x][e.getAttribute("data-t")];if(typeof v==="string")e.textContent=v}});
if(T[x][TITLE_KEY])document.title=T[x][TITLE_KEY];
var m=document.querySelector('meta[name="description"]');if(m&&T[x].desc)m.setAttribute("content",T[x].desc);
render();}}
/* ---- 로그인 상태는 브라우저에만 둔다 ---- */
var SKEY="vl-session";
function session(){{try{{return JSON.parse(localStorage.getItem(SKEY)||"null")}}catch(e){{return null}}}}
function save(s){{try{{s?localStorage.setItem(SKEY,JSON.stringify(s)):localStorage.removeItem(SKEY)}}catch(e){{}}}}
function store(d){{if(!d||!d.access_token)return null;
var s={{access_token:d.access_token,refresh_token:d.refresh_token,
expires_at:(d.expires_at?d.expires_at*1000:Date.now()+(d.expires_in||3600)*1000),
email:(d.user&&d.user.email)||(session()||{{}}).email||null}};save(s);return s;}}
function auth(path,body){{return fetch(SB+"/auth/v1/"+path,{{method:"POST",
headers:{{"apikey":KEY,"Content-Type":"application/json"}},body:JSON.stringify(body)}})
.then(function(r){{return r.json().then(function(j){{return {{ok:r.ok,j:j}}}})}});}}
function token(){{var s=session();if(!s)return Promise.resolve(null);
if(s.expires_at-60000>Date.now())return Promise.resolve(s);
return auth("token?grant_type=refresh_token",{{refresh_token:s.refresh_token}})
.then(function(r){{return r.ok?store(r.j):(save(null),null)}});}}
function fn(name,body){{return token().then(function(s){{if(!s)return {{ok:false,j:{{error:"unauthorized"}}}};
return fetch(SB+"/functions/v1/"+name,{{method:"POST",
headers:{{"apikey":KEY,"Authorization":"Bearer "+s.access_token,"Content-Type":"application/json"}},
body:JSON.stringify(body)}}).then(function(r){{return r.json().then(function(j){{return {{ok:r.ok,j:j}}}})}});}});}}
/* OAuth 로 돌아올 때 토큰이 주소 뒤에 붙어 온다 */
function fromHash(){{var h=location.hash||"";if(h.indexOf("access_token=")<0)return;
var p={{}};h.slice(1).split("&").forEach(function(kv){{var i=kv.indexOf("=");
if(i>0)p[decodeURIComponent(kv.slice(0,i))]=decodeURIComponent(kv.slice(i+1))}});
if(p.access_token){{store({{access_token:p.access_token,refresh_token:p.refresh_token,
expires_in:Number(p.expires_in||3600)}});history.replaceState(null,"",location.pathname+location.search);}}}}
function oauth(p){{location.href=SB+"/auth/v1/authorize?provider="+p+
"&redirect_to="+encodeURIComponent(location.origin+location.pathname);}}
/* Cloudflare Turnstile — 이 Supabase 프로젝트는 캡차 보호가 켜져 있어,
   토큰 없이는 이메일 로그인·가입·비밀번호 재설정이 모두 거부된다.
   위레가토 앱과 같은 사이트 키를 쓴다(공개 키다). 스크립트는 로그인하려는
   사람에게만 받아 온다 — 그냥 읽기만 하는 사람에게는 안 받는다. */
var CF_KEY="0x4AAAAAAE-DPE-XNwkkeKAg",cfId=null,cfTok="",cfErr="",cfLoad=null;
function cfReady(){{
if(cfLoad)return cfLoad;
cfLoad=new Promise(function(res,rej){{
var el=document.createElement("script");
el.src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
el.async=true;el.defer=true;el.onload=res;
el.onerror=function(){{rej(new Error("cf_load"))}};
document.head.appendChild(el);}}).then(function(){{
cfId=turnstile.render("#cf",{{sitekey:CF_KEY,
callback:function(t){{cfTok=t;cfErr=""}},
"expired-callback":function(){{cfTok=""}},
"error-callback":function(e){{cfTok="";cfErr=String(e||"cf_error")}}}});}});
return cfLoad;}}
/* 토큰이 올 때까지 기다린다(최대 20초). 사람이 상자를 눌러야 할 수도 있다. */
function captcha(){{return cfReady().then(function(){{
if(cfTok)return cfTok;
return new Promise(function(res,rej){{var n=0,iv=setInterval(function(){{
if(cfTok){{clearInterval(iv);res(cfTok)}}
else if(cfErr||++n>80){{clearInterval(iv);rej(new Error(cfErr||"cf_timeout"))}}}},250);}});}});}}
/* 토큰은 한 번만 쓸 수 있다. 실패했으면 새로 받아야 한다. */
function cfReset(){{cfTok="";cfErr="";if(cfId!==null&&window.turnstile)turnstile.reset(cfId);}}
/* 서버가 하는 말을 그대로 전한다. 모르는 코드는 뭉개지 말고 함께 보여 준다. */
function authErr(j,isSignup){{var t=T[lang].err,c=(j&&(j.error_code||j.error_description||j.error))||"";
if(c==="captcha_failed")return t.captcha;
if(c==="email_not_confirmed")return t.confirm;
if(c==="over_request_rate_limit"||c==="over_email_send_rate_limit")return t.too_many;
if(c==="user_already_exists"||c==="email_exists")return t.taken;
if(c==="weak_password")return t.weak;
if(c==="invalid_credentials")return t.login;
return (isSignup?t.signup:t.login)+" ("+(c||"?")+")";}}
"""


BUY_BODY = """
<main class="wrap buy">
<h1 data-t="h1"></h1><p class="lede" data-t="lede"></p>

<div class="step outside hidden" id="outside">
  <h2 data-t="out_h"></h2><p class="hint" data-t="out_p"></p>
  __BADGES__
  <p style="margin:16px 0 0"><a href="#" id="anyway" data-t="out_link"></a></p>
</div>

<div id="flow">
  <div class="step">
    <h2 data-t="s1"></h2><p class="hint" data-t="s1h"></p>
    <div class="sizes__HIDE50__" role="group">
      <button type="button" data-size="10" class="on"></button><button type="button" data-size="50"></button>
    </div>
    <div class="opts">
      <button type="button" class="opt on" data-every="month"><b id="pm"></b><span id="lm"></span></button>
      <button type="button" class="opt" data-every="year"><b id="py"></b><span id="ly"></span></button>
    </div>
    <p class="hint" style="margin:20px 0 0" data-t="incl_h"></p>
    <ul class="incl" id="incl"></ul>
    <p class="fine" data-t="cloud_note"></p>
    <p class="fine" style="margin-top:4px" data-t="launch_price"></p>
  </div>

  <div class="step">
    <h2 data-t="s2"></h2><p class="hint" data-t="s2h"></p>
    <div id="anon">
      <label class="f" for="em" data-t="email"></label><input id="em" type="email" autocomplete="email">
      <label class="f" for="pw" data-t="pw"></label><input id="pw" type="password" autocomplete="current-password">
      <div id="cf"></div>
      <div class="row"><button type="button" class="btn" id="go"></button>
      <button type="button" class="btn ghost" id="toggle"></button></div>
      <div class="sep"><span data-t="or"></span></div>
      <div class="social"><button type="button" data-p="google">Google</button>
      <button type="button" data-p="kakao">Kakao</button></div>
    </div>
    <div id="known" class="hidden">
      <p class="who"><span data-t="logged"></span>: <b id="who"></b></p>
      <div class="row"><button type="button" class="btn ghost" id="out" data-t="logout"></button></div>
    </div>
    <div id="amsg" class="msg hidden"></div>
  </div>

  <div class="step" id="paystep">
    <h2 data-t="s3"></h2><p class="hint" data-t="s3h"></p>
    <label class="waiver"><input type="checkbox" id="waiver"><span data-t="waiver"></span></label>
    <div class="row"><button type="button" class="btn" id="pay" data-t="pay"></button></div>
    <p class="fine"><span data-t="renew"></span> <span data-t="vat"></span></p>
    <div id="pmsg" class="msg hidden"></div>
  </div>

</div>

<div class="step hidden" id="account">
  <h2 data-t="acc_h"></h2>
  <p class="who" id="accplan"></p>
  <p class="hint" id="accwhen" style="margin:4px 0 0"></p>
  <p class="hint" id="accnote" style="margin:12px 0 0"></p>
  <div class="row" id="accbtns">
    <button type="button" class="btn hidden" id="up"></button>
    <button type="button" class="btn ghost hidden" id="cancel"></button>
    <button type="button" class="btn ghost hidden" id="resume"></button>
    <button type="button" class="btn ghost hidden" id="portal"></button>
  </div>
  <p class="fine" id="upnote"></p>
  <p class="fine" data-t="acc_quota_note"></p>
  <p class="fine" style="margin-top:4px" data-t="acc_end_note"></p>
  <div id="accmsg" class="msg hidden"></div>
</div>

<p class="fine" style="margin-top:26px"><a href="/leggii/" data-t="back"></a></p>
</main>
"""

BUY_JS = """
var PRICE=__PRICES__,SHOW50=__SHOW50__,size="10",every="month",signup=false,sub=null,noEurope=false;
function product(){return "plus-"+size+"-"+every}
var MONEY={ko:"ko-KR",en:"en-GB",de:"de-DE"};
function euro(p){var c=PRICE[p];if(c==null)return "";
try{return new Intl.NumberFormat(MONEY[lang]||"en-GB",{style:"currency",currency:"EUR"}).format(c/100)}
catch(e){return (c/100).toFixed(2)+" €"}}
/* 유럽인지 대충 본다(시간대). 진짜 판단은 결제 뒤 서버가 청구 국가로 한다. */
function europe(){try{var z=Intl.DateTimeFormat().resolvedOptions().timeZone||"";
if(/^Europe\\//.test(z))return ["Europe/London","Europe/Moscow","Europe/Istanbul","Europe/Kyiv",
"Europe/Kiev","Europe/Minsk","Europe/Simferopol","Europe/Volgograd","Europe/Samara","Europe/Saratov",
"Europe/Astrakhan","Europe/Ulyanovsk","Europe/Kirov"].indexOf(z)<0;
return ["Atlantic/Reykjavik","Atlantic/Canary","Atlantic/Madeira","Atlantic/Azores","Atlantic/Faroe"].indexOf(z)>=0;
}catch(e){return true}}
function msg(el,text,bad){var e=document.getElementById(el);
if(!text){e.classList.add("hidden");return}e.textContent=text;e.classList.toggle("bad",!!bad);e.classList.remove("hidden");}
function planName(code){var t=T[lang];if(!code)return "—";
return (code.indexOf("plus-50")===0?t.size50:t.size10)+" · "+(/-year$/.test(code)?t.year:t.month)}
function render(){var t=T[lang];
document.querySelectorAll("[data-size]").forEach(function(b){
b.textContent=t[b.getAttribute("data-size")==="10"?"size10":"size50"];
b.classList.toggle("on",b.getAttribute("data-size")===size)});
document.querySelectorAll("[data-every]").forEach(function(b){
b.classList.toggle("on",b.getAttribute("data-every")===every)});
var sep=lang==="ko"?" / ":" ";
document.getElementById("pm").textContent=euro("plus-"+size+"-month")+sep+t.per_month;
document.getElementById("py").textContent=euro("plus-"+size+"-year")+sep+t.per_year;
document.getElementById("lm").textContent=t.month;
document.getElementById("ly").textContent=t.year+" · "+t.save;
document.getElementById("incl").innerHTML=t.incl.map(function(x){
return "<li>"+x.replace(/[&<>]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;"}[c]})+"</li>"}).join("");
document.getElementById("go").textContent=signup?t.signup:t.login;
document.getElementById("toggle").textContent=signup?t.toggle_login:t.toggle_signup;
var s=session();
document.getElementById("anon").classList.toggle("hidden",!!s);
document.getElementById("known").classList.toggle("hidden",!s);
if(s)document.getElementById("who").textContent=s.email||"";
var src=(sub&&sub.source)||"none",mine=src!=="none";
document.getElementById("account").classList.toggle("hidden",!mine);
document.getElementById("flow").classList.toggle("hidden",mine&&!noEurope);
var el=function(id){return document.getElementById(id)};
["up","cancel","resume","portal"].forEach(function(id){el(id).classList.add("hidden")});
el("accnote").textContent="";el("upnote").textContent="";
el("accplan").textContent="";el("accwhen").textContent="";
if(src==="web"){
el("accplan").innerHTML="<span>"+t.acc_plan+"</span>: <b>"+planName(sub.product)+"</b>";
var d=sub.currentPeriodEnd?new Date(sub.currentPeriodEnd).toLocaleDateString(lang):"";
el("accwhen").textContent=(sub.cancelAtPeriodEnd?t.acc_ends:t.acc_next)+": "+d;
if(sub.upgradeTo&&!sub.cancelAtPeriodEnd){el("up").textContent=t.acc_up;el("up").classList.remove("hidden");
el("upnote").textContent=t.acc_up_note;}
if(sub.cancelAtPeriodEnd){el("resume").textContent=t.acc_resume;el("resume").classList.remove("hidden");}
else{el("cancel").textContent=t.acc_cancel;el("cancel").classList.remove("hidden");
el("accnote").textContent=t.acc_cancel_note;}
el("portal").textContent=t.acc_portal;el("portal").classList.remove("hidden");
}else if(src==="store"){
el("accplan").textContent=t.acc_store;el("accwhen").textContent="";
}else if(src==="benefit"){
var u=sub.until?new Date(sub.until).toLocaleDateString(lang):"";
el("accplan").textContent=t.acc_benefit;
el("accwhen").textContent=u?t.acc_ends+": "+u:"";
}
}
function refreshStatus(){if(!session()){sub=null;render();return Promise.resolve()}
return fn("web-checkout",{app:APP,action:"status"}).then(function(r){
if(r.ok){sub=r.j;var s=session();if(s&&r.j.email){s.email=r.j.email;save(s)}}
else if(r.j&&r.j.error==="unauthorized"){save(null);sub=null}
render();});}
document.addEventListener("click",function(e){
var b=e.target.closest("[data-set]");if(b){setLang(b.getAttribute("data-set"));return}
b=e.target.closest("[data-size]");if(b){if(SHOW50)size=b.getAttribute("data-size");render();return}
b=e.target.closest("[data-every]");if(b){every=b.getAttribute("data-every");render();return}
b=e.target.closest("[data-p]");if(b){oauth(b.getAttribute("data-p"));return}
if(e.target.closest("#anyway")){e.preventDefault();noEurope=false;
document.getElementById("outside").classList.add("hidden");render();return}
if(e.target.closest("#toggle")){signup=!signup;msg("amsg","");render();return}
if(e.target.closest("#out")){save(null);sub=null;render();return}
if(e.target.closest("#go")){
var em=document.getElementById("em").value.trim(),pw=document.getElementById("pw").value;
if(!em||!pw)return;msg("amsg","");
var gob=document.getElementById("go");gob.disabled=true;msg("amsg","");
captcha().then(function(tok){
return auth(signup?"signup":"token?grant_type=password",
{email:em,password:pw,gotrue_meta_security:{captcha_token:tok}});
}).then(function(r){gob.disabled=false;cfReset();
if(r.ok&&r.j.access_token){store(r.j);document.getElementById("pw").value="";return refreshStatus()}
if(r.ok&&signup){msg("amsg",T[lang].err.confirm);return}
msg("amsg",authErr(r.j,signup),true);
},function(e){gob.disabled=false;cfReset();
msg("amsg",T[lang].err.captcha+" ("+(e&&e.message||"?")+")",true);});return}
if(e.target.closest("#pay")){
if(!session()){document.getElementById("em").focus();return}
if(!document.getElementById("waiver").checked){msg("pmsg",T[lang].err.waiver,true);return}
msg("pmsg","");var btn=document.getElementById("pay");btn.disabled=true;
fn("web-checkout",{app:APP,product:product(),withdrawal_waiver:true,locale:lang}).then(function(r){
if(r.ok&&r.j.url){location.href=r.j.url;return}
btn.disabled=false;msg("pmsg",T[lang].err[(r.j&&r.j.error)]||T[lang].err.other,true);});return}
if(e.target.closest("#portal")){var p=document.getElementById("portal");p.disabled=true;
fn("billing-portal",{app:APP}).then(function(r){
if(r.ok&&r.j.url){location.href=r.j.url;return}p.disabled=false;msg("accmsg",T[lang].err.other,true);});return}
var act=e.target.closest("#up")?"upgrade":(e.target.closest("#cancel")?"cancel":(e.target.closest("#resume")?"resume":""));
if(act){var b2=e.target.closest("button");b2.disabled=true;msg("accmsg","");
fn("web-checkout",{app:APP,action:act,product:act==="upgrade"?sub.upgradeTo:undefined}).then(function(r){
b2.disabled=false;
if(r.ok&&r.j.ok){msg("accmsg",T[lang].done);return refreshStatus()}
msg("accmsg",T[lang].err[(r.j&&r.j.error)]||T[lang].err.other,true);});return}
});
fromHash();
if(!europe()){noEurope=true;document.getElementById("outside").classList.remove("hidden");
document.getElementById("flow").classList.add("hidden");}
setLang(pick());
refreshStatus();
"""


THANKS_BODY = """
<main class="wrap buy">
<h1 data-t="thanks_h"></h1><p class="lede" data-t="thanks_p"></p>
<div class="step">
  <p class="who"><span data-t="thanks_id"></span>: <b id="who">—</b></p>
  <p class="hint" id="havewhen" style="margin:6px 0 0"></p>
  <p class="hint" style="margin:18px 0 6px" data-t="thanks_get"></p>
  __BADGES__
  <div class="row"><button type="button" class="btn ghost" id="portal" data-t="thanks_manage"></button></div>
</div>
<p class="fine" style="margin-top:26px"><a href="/leggii/" data-t="back"></a></p>
</main>
"""

THANKS_JS = """
TITLE_KEY="thanks_title";
var sub=null;
function render(){var t=T[lang],s=session();
document.getElementById("who").textContent=(sub&&sub.email)||(s&&s.email)||"—";
var w=document.getElementById("havewhen");
w.textContent=(sub&&sub.subscribed&&sub.currentPeriodEnd)
?t.until+": "+new Date(sub.currentPeriodEnd).toLocaleDateString(lang):"";}
document.addEventListener("click",function(e){
var b=e.target.closest("[data-set]");if(b){setLang(b.getAttribute("data-set"));return}
if(e.target.closest("#portal")){var p=document.getElementById("portal");p.disabled=true;
fn("billing-portal",{app:"leggii"}).then(function(r){
if(r.ok&&r.j.url){location.href=r.j.url;return}p.disabled=false;});}});
fromHash();
setLang(pick());
/* 웹훅이 들어오기 전에 돌아올 수 있어서 몇 초 동안 다시 본다. */
var tries=0;
(function look(){if(!session())return;
fn("web-checkout",{app:"leggii",action:"status"}).then(function(r){
if(r.ok){sub=r.j;render()}
if((!r.ok||!r.j.subscribed)&&tries++<5)setTimeout(look,2000);});})();
"""


def _json(x):
    import json
    return json.dumps(x, ensure_ascii=False)


def buy_page():
    body = (BUY_BODY.replace("__BADGES__", _badges())
        .replace("__HIDE50__", "" if SHOW_50 else " hidden"))
    js = (COMMON_JS.replace("__T__", _json(T))
          + BUY_JS.replace("__PRICES__", _json(PRICES)).replace("__SHOW50__", "true" if SHOW_50 else "false"))
    return (_head(T["en"]["title"], T["en"]["desc"], "/leggii/plus/")
            + body + FOOT + f"<script>{js}</script>\n</body></html>\n")


def thanks_page():
    body = THANKS_BODY.replace("__BADGES__", _badges())
    js = COMMON_JS.replace("__T__", _json(T)) + THANKS_JS
    return (_head(T["en"]["thanks_title"], T["en"]["desc"], "/leggii/plus/danke/")
            + body + FOOT + f"<script>{js}</script>\n</body></html>\n")
