#!/usr/bin/env python3
"""프로바 Plus 구독 — vicinolabs.com/prova/plus/ 와 .../plus/danke/ (2026-11-19).

렛지 Plus 페이지(leggii_plus.py)와 **같은 화면, 같은 흐름**이다. 틀을 그대로
가져다 쓰고 프로바에만 다른 것만 바꾼다. 두 벌을 따로 들고 있으면 한쪽만
고쳐지는 날이 온다.

프로바에서 다른 것:
- 50GB 를 화면에 내보낸다. 렛지는 아직 숨겨 두었지만(SHOW_50=False) 프로바
  50GB 는 두 스토어에 이미 있고 소개 페이지 요금제에도 올라가 있다.
- 값이 다르다(10GB 4,99/49,99 · 50GB 6,99/69,99 €). 두 스토어와 같은 값이다.
- 말투가 ~어요다. 프로바 페이지가 그렇다. 다만 **돈과 계약을 설명하는 줄**
  (갱신·해지·환불·청약철회·부가세)은 ~습니다로 둔다.
- 출시 가격 약속은 넣지 않는다. 렛지에는 2027년까지라는 약속이 있지만
  프로바에는 그런 약속이 없다. 없는 약속을 적으면 안 된다.

서버는 손댈 것이 없다(HQ 2026-11-19 확인):
- web-checkout 의 APPS 에 "prova" 가 들어 있다.
- stripe-webhook/web_sub.ts 와 web_sub_apply 는 앱을 가리지 않고
  메타데이터의 app 을 그대로 쓴다.
- leggii_ai_config.web_products 에 prova 넷이 들어가 있다.
- 스트라이프 가격은 web-checkout 이 lookup key 로 없으면 만들어 쓴다.

prova_legal.py 가 부른다.
"""

import leggii_plus as LP
import prova_site as P

LANGS = P.LANGS
EMAIL = P.EMAIL

# 프로바 50GB 는 두 스토어에 이미 있다. 숨길 까닭이 없다(HQ 2026-11-19).
SHOW_50 = True

# 화면 표시용. 진짜 금액은 web-checkout 이 서버에서 정한다.
# 센트. 두 스토어와 같은 값이다.
PRICES = {
    "plus-10-month": 499, "plus-10-year": 4999,
    "plus-50-month": 699, "plus-50-year": 6999,
}

CSS = LP.CSS


T = {
"ko": {
 "title": "Prova Plus 구독 | 프로바 · Vicino Labs",
 "desc": "프로바 Plus를 홈페이지에서 바로 구독하세요. 위레가토 아이디로 가입하고, 앱에서 같은 아이디로 로그인하면 열려요.",
 "h1": "Prova Plus",
 "lede": "AI가 연주를 듣고 짚어 주고, 녹음은 클라우드에 그대로 남아요. 여기서 구독하신 뒤 앱에서 같은 위레가토 아이디로 로그인하시면 돼요.",
 "s1": "1. 요금제 고르기", "s1h": "저장 공간과 결제 주기를 고르세요. 값은 앱 스토어·구글 플레이와 같아요.",
 "size10": "클라우드 10GB", "size50": "클라우드 50GB",
 "month": "월간", "year": "연간", "per_month": "월", "per_year": "연",
 "save": "2개월 무료", "per_month_is": "월 {p}",
 "incl_h": "Plus에 들어 있는 것",
 "incl": ["AI 레슨 노트와 AI 연주 점검 매월 10시간",
          "AI 시간은 렛지와 함께 써요. 둘 다 구독하시면 시간이 합쳐져요",
          "프로바 클라우드: 녹음의 소리를 보관해요. 영상은 소리만 올라가요"],
 "s2": "2. 위레가토 아이디", "s2h": "위레가토 아이디 하나로 Vicino Labs 앱을 모두 쓰실 수 있어요. 이미 있으시면 그대로 로그인하세요.",
 "email": "이메일", "pw": "비밀번호",
 "login": "로그인", "signup": "가입하기", "or": "또는",
 "toggle_signup": "처음이신가요? 가입하기", "toggle_login": "이미 아이디가 있으신가요? 로그인",
 "logged": "로그인했어요", "logout": "로그아웃",
 "wg": "위레가토는 Vicino Labs가 만드는 음악 사이트예요. 선생님과 연주자를 찾고 연락하는 곳이고, 프로바와 아이디를 함께 써요.",
 "wg_link": "welegato.com 둘러보기 →",
 "acc_settings": "계정 설정", "acc_pw": "비밀번호 바꾸기", "acc_delete": "회원 탈퇴",
 "acc_store_apple": "App Store에서 구독 관리", "acc_store_google": "Google Play에서 구독 관리",
 "s3": "3. 결제", "s3h": "",
 # 아래 다섯 줄은 돈과 계약을 설명하는 자리라 ~습니다로 둔다.
 "waiver": "지금 바로 구독을 시작하는 데 동의하며, 그에 따라 청약철회권이 사라진다는 점을 확인합니다(독일 민법 제356조 제5항).",
 "agree": "구독하시면 아래에 동의하시는 것으로 봅니다.", "pay": "구독하기",
 "vat": "소규모사업자로 부가가치세는 붙지 않습니다(독일 부가가치세법 제19조).",
 "renew": "결제가 끝나면 바로 이용하실 수 있습니다. 구독은 자동으로 갱신되며, 다음 결제일 전까지 언제든 해지하실 수 있습니다.",
 "have": "이 아이디로 이미 Plus를 쓰고 있어요.",
 "until": "다음 결제일", "ending": "이 날짜까지 이용하실 수 있습니다",
 "manage": "구독 관리·해지",
 "out_h": "홈페이지 결제는 지금 유럽에서만 받아요",
 "out_p": "앱 스토어나 구글 플레이에서 구독해 주세요. 앱에서 구독하셔도 똑같이 쓰실 수 있어요.",
 "out_link": "유럽에서 결제하시나요?",
 "err": {"waiver": "위 항목에 동의해 주세요.", "login": "이메일 또는 비밀번호가 맞지 않아요.",
         "signup": "가입할 수 없어요. 이미 가입된 이메일인지 확인해 주세요.",
         "confirm": "메일로 보내 드린 링크로 이메일 인증을 마친 뒤 로그인해 주세요.",
         "already_subscribed": "이미 구독 중이에요.", "app_store_only": "홈페이지 결제는 유럽에서만 받아요.",
         "store_subscribed": "앱 스토어에서 이미 구독 중이에요.", "no_subscription": "구독 내역을 찾을 수 없어요.",
         "interval_mismatch": "월간은 월간으로, 연간은 연간으로만 변경하실 수 있습니다.",
         "captcha": "사람인지 확인하는 절차를 마치지 못했어요. 위 확인 상자를 눌러 주세요.",
         "captcha_off": "이메일 로그인은 지금 막혀 있어요. 비밀번호 문제가 아니에요. 아래 구글이나 카카오로 들어와 주세요.",
         "too_many": "시도가 너무 잦아요. 잠시 뒤에 다시 해 주세요.",
         "taken": "이미 가입된 이메일이에요. 로그인해 주세요.",
         "weak": "비밀번호가 너무 짧아요. 여섯 자 이상으로 해 주세요.",
         "other": "잠시 후 다시 시도해 주세요."},
 "cloud_note": "나중에 '나의 구독'에서 50GB로 올리실 수 있어요.",
 "acc_h": "나의 구독",
 "acc_plan": "현재 요금제",
 "acc_next": "다음 결제일",
 "acc_ends": "이 날짜까지 이용하실 수 있습니다",
 "acc_up": "50GB로 올리기",
 "acc_up_note": "바로 바뀌고, 남은 기간에 대한 차액만 결제됩니다.",
 "acc_cancel": "해지하기",
 "acc_cancel_note": "해지하시면 다음 결제일에 자동 결제되지 않으며, 남은 이용 기간 동안 그대로 이용하실 수 있습니다.",
 "acc_resume": "해지 취소",
 "acc_quota_note": "저장 공간이 차면 새로 올리는 것만 멈추고 이미 올린 파일은 지우지 않습니다. 기기에 있는 녹음도 그대로입니다.",
 "acc_end_note": "Plus가 끝나면 새로 올리는 것은 멈추고 90일 동안 내려받으실 수 있습니다. 메일로 두 번 알려 드린 뒤 클라우드의 파일을 지웁니다. 기기에 있는 녹음과 영상은 그대로 남습니다.",
 "acc_store": "앱 스토어에서 구독 중이에요. 변경과 해지는 구독하신 스토어에서 하실 수 있어요.",
 "acc_benefit": "위레가토 회원 혜택으로 Plus를 쓰고 계세요.",
 "acc_portal": "결제 내역 · 결제 수단 변경",
 "done": "변경되었어요.",
 "back": "프로바 소개로",
 "privacy": "개인정보처리방침", "terms": "이용약관",
 "thanks_title": "구독이 시작되었어요 | 프로바",
 "thanks_h": "구독이 시작되었어요", "thanks_p": "영수증을 메일로 보내 드렸어요.",
 "thanks_id": "구독한 아이디", "thanks_get": "앱 받기", "thanks_manage": "구독 관리",
},
"en": {
 "title": "Prova Plus subscription | Vicino Labs",
 "desc": "Subscribe to Prova Plus here. Sign up with your welegato ID and sign in to the app with the same ID.",
 "h1": "Prova Plus",
 "lede": "The AI listens to your playing and marks it, and your recordings stay in the cloud. Subscribe here, then sign in to the app with the same welegato ID.",
 "s1": "1. Choose a plan", "s1h": "Pick the cloud size and how often you pay. The price is the same as on the App Store and Google Play.",
 "size10": "10 GB cloud", "size50": "50 GB cloud",
 "month": "Monthly", "year": "Yearly", "per_month": "a month", "per_year": "a year",
 "save": "2 months free", "per_month_is": "{p}/mo",
 "incl_h": "What Plus includes",
 "incl": ["10 hours a month of AI lesson notes and AI review of your playing",
          "The AI hours are shared with Leggii: subscribe to both and they add up",
          "Prova cloud: it keeps the sound of your takes. Of a video, only the sound goes up"],
 "s2": "2. welegato ID", "s2h": "One welegato ID for the Vicino Labs apps. Already have one? Just sign in.",
 "email": "Email", "pw": "Password",
 "login": "Sign in", "signup": "Create account", "or": "or",
 "toggle_signup": "New here? Create an account", "toggle_login": "Already have a welegato ID? Sign in",
 "logged": "Signed in", "logout": "Sign out",
 "wg": "welegato is the music site Vicino Labs builds. It is where you find and contact teachers and musicians, and it shares its ID with Prova.",
 "wg_link": "Have a look at welegato.com →",
 "acc_settings": "Account settings", "acc_pw": "Change password", "acc_delete": "Delete account",
 "acc_store_apple": "Manage on the App Store", "acc_store_google": "Manage on Google Play",
 "s3": "3. Payment", "s3h": "",
 "waiver": "I want the subscription to start right away and understand that my right of withdrawal lapses (§ 356(5) German Civil Code).",
 "agree": "By subscribing you agree to:", "pay": "Subscribe",
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
         "store_subscribed": "You are already subscribed through an app store.", "no_subscription": "No subscription found.",
         "interval_mismatch": "You can only move up within the same billing period.",
         "captcha": "The check that you are human did not finish. Please tick the box above.",
         "captcha_off": "Email sign-in is blocked at the moment. It is not your password. Please use Google or Kakao below.",
         "too_many": "Too many attempts. Please wait a moment and try again.",
         "taken": "That email already has an account. Please sign in.",
         "weak": "That password is too short. Please use at least six characters.",
         "other": "Something went wrong. Please try again in a moment."},
 "cloud_note": "You can move up to 50 GB later on your subscription page.",
 "acc_h": "Your subscription",
 "acc_plan": "Current plan",
 "acc_next": "Next billing date",
 "acc_ends": "Runs until",
 "acc_up": "Move up to 50 GB",
 "acc_up_note": "It changes straight away and you pay only the difference for the rest of the period.",
 "acc_cancel": "Cancel",
 "acc_cancel_note": "Cancelling stops the next payment. You keep Plus until the end of the period you have paid for.",
 "acc_resume": "Undo cancellation",
 "acc_quota_note": "When the space is full only new uploads stop; nothing already uploaded is deleted. What is on your device stays either way.",
 "acc_end_note": "When Plus ends, uploads stop and you can download for 90 days. We write twice, then delete the files in the cloud. The recordings and videos on your device stay.",
 "acc_store": "You subscribe through an app store. Change or cancel it in the store you subscribed in.",
 "acc_benefit": "You have Plus through your welegato membership.",
 "acc_portal": "Invoices · change card",
 "done": "Done.",
 "back": "Back to Prova",
 "privacy": "Privacy policy", "terms": "Terms",
 "thanks_title": "Your subscription has started | Prova",
 "thanks_h": "Your subscription has started", "thanks_p": "The receipt is on its way to your inbox.",
 "thanks_id": "Subscribed ID", "thanks_get": "Get the app", "thanks_manage": "Manage subscription",
},
"de": {
 "title": "Prova Plus abonnieren | Vicino Labs",
 "desc": "Prova Plus hier direkt abonnieren. Mit der welegato-ID anmelden und sich in der App mit derselben ID anmelden.",
 "h1": "Prova Plus",
 "lede": "Die KI hört Ihr Spiel und markiert es, und Ihre Aufnahmen bleiben in der Cloud. Hier abonnieren und sich dann in der App mit derselben welegato-ID anmelden.",
 "s1": "1. Tarif wählen", "s1h": "Speicherplatz und Zahlungsweise wählen. Der Preis ist derselbe wie im App Store und bei Google Play.",
 "size10": "10 GB Cloud", "size50": "50 GB Cloud",
 "month": "Monatlich", "year": "Jährlich", "per_month": "im Monat", "per_year": "im Jahr",
 "save": "2 Monate geschenkt", "per_month_is": "{p} im Monat",
 "incl_h": "In Plus enthalten",
 "incl": ["10 Stunden KI im Monat für Notizen zur Stunde und für die Durchsicht Ihres Spiels",
          "Die KI-Stunden teilen sich mit Leggii: wer beides abonniert, bekommt sie zusammengezählt",
          "Prova-Cloud: sie bewahrt den Ton Ihrer Aufnahmen. Von einem Video geht nur der Ton hoch"],
 "s2": "2. welegato-ID", "s2h": "Eine welegato-ID für alle Apps von Vicino Labs. Schon eine da? Dann einfach anmelden.",
 "email": "E-Mail", "pw": "Passwort",
 "login": "Anmelden", "signup": "Konto anlegen", "or": "oder",
 "toggle_signup": "Zum ersten Mal hier? Konto anlegen", "toggle_login": "Schon eine welegato-ID? Anmelden",
 "logged": "Angemeldet", "logout": "Abmelden",
 "wg": "welegato ist die Musikseite von Vicino Labs. Dort finden und kontaktieren Sie Lehrende und Musikerinnen und Musiker, und sie teilt die ID mit Prova.",
 "wg_link": "welegato.com ansehen →",
 "acc_settings": "Kontoeinstellungen", "acc_pw": "Passwort ändern", "acc_delete": "Konto löschen",
 "acc_store_apple": "Im App Store verwalten", "acc_store_google": "Bei Google Play verwalten",
 "s3": "3. Zahlung", "s3h": "",
 "waiver": "Ich möchte, dass das Abo sofort beginnt, und weiß, dass mein Widerrufsrecht damit erlischt (§ 356 Abs. 5 BGB).",
 "agree": "Mit dem Abo stimmen Sie zu:", "pay": "Abonnieren",
 "vat": "Es wird keine Umsatzsteuer berechnet (Kleinunternehmer, § 19 UStG).",
 "renew": "Sobald die Zahlung durch ist, können Sie loslegen. Das Abo verlängert sich automatisch und lässt sich jederzeit vor dem nächsten Abrechnungstag kündigen.",
 "have": "Diese ID hat Plus bereits.",
 "until": "Nächster Abrechnungstag", "ending": "Läuft bis",
 "manage": "Abo verwalten",
 "out_h": "Zahlungen über die Webseite nehmen wir derzeit nur in Europa an",
 "out_p": "Bitte im App Store oder bei Google Play abonnieren. Ein Abo aus der App ist genau dasselbe.",
 "out_link": "Zahlen Sie aus Europa?",
 "err": {"waiver": "Bitte zuerst oben zustimmen.", "login": "E-Mail oder Passwort stimmen nicht.",
         "signup": "Das Konto konnte nicht angelegt werden. Vielleicht ist die E-Mail schon vergeben.",
         "confirm": "Bitte den Link aus der E-Mail öffnen und sich dann anmelden.",
         "already_subscribed": "Sie haben bereits ein Abo.", "app_store_only": "Zahlungen über die Webseite gibt es nur in Europa.",
         "store_subscribed": "Sie haben bereits ein Abo über einen App-Store.", "no_subscription": "Kein Abo gefunden.",
         "interval_mismatch": "Ein Wechsel ist nur innerhalb derselben Zahlungsweise möglich.",
         "captcha": "Die Prüfung, ob Sie ein Mensch sind, ist nicht durchgelaufen. Bitte oben das Kästchen antippen.",
         "captcha_off": "Die Anmeldung per E-Mail ist gerade gesperrt. Es liegt nicht am Passwort. Bitte unten Google oder Kakao nehmen.",
         "too_many": "Zu viele Versuche. Bitte kurz warten und noch einmal probieren.",
         "taken": "Für diese E-Mail gibt es schon ein Konto. Bitte anmelden.",
         "weak": "Das Passwort ist zu kurz. Bitte mindestens sechs Zeichen.",
         "other": "Bitte gleich noch einmal versuchen."},
 "cloud_note": "Auf 50 GB können Sie später unter „Mein Abo“ wechseln.",
 "acc_h": "Mein Abo",
 "acc_plan": "Aktueller Tarif",
 "acc_next": "Nächster Abrechnungstag",
 "acc_ends": "Läuft bis",
 "acc_up": "Auf 50 GB wechseln",
 "acc_up_note": "Der Wechsel gilt sofort, berechnet wird nur die Differenz für den Rest des Zeitraums.",
 "acc_cancel": "Kündigen",
 "acc_cancel_note": "Nach der Kündigung wird am nächsten Abrechnungstag nicht mehr abgebucht. Bis zum Ende des bezahlten Zeitraums bleibt alles nutzbar.",
 "acc_resume": "Kündigung zurücknehmen",
 "acc_quota_note": "Ist der Speicher voll, stoppen nur neue Uploads; nichts bereits Hochgeladenes wird gelöscht. Was auf dem Gerät liegt, bleibt ohnehin.",
 "acc_end_note": "Endet Plus, stoppen die Uploads und Sie können 90 Tage lang herunterladen. Wir schreiben zweimal, danach löschen wir die Dateien in der Cloud. Aufnahmen und Videos auf dem Gerät bleiben.",
 "acc_store": "Sie haben ein Abo über einen App-Store. Ändern und kündigen können Sie es dort, wo Sie es abgeschlossen haben.",
 "acc_benefit": "Sie haben Plus über Ihre welegato-Mitgliedschaft.",
 "acc_portal": "Rechnungen · Karte ändern",
 "done": "Erledigt.",
 "back": "Zurück zu Prova",
 "privacy": "Datenschutz", "terms": "Nutzungsbedingungen",
 "thanks_title": "Ihr Abo läuft | Prova",
 "thanks_h": "Ihr Abo läuft", "thanks_p": "Die Rechnung ist unterwegs in Ihr Postfach.",
 "thanks_id": "Abonnierte ID", "thanks_get": "App holen", "thanks_manage": "Abo verwalten",
},
}


def _badges():
    """스토어 배지. 프로바 것을 쓴다(App Store 는 승인되면 저절로 붙는다)."""
    return "".join(f'<div data-l="{l}"{" class=on" if l == "en" else ""}>{P._stores(l)}</div>'
                   for l, _ in LANGS)


def _head(title, desc, path):
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
<style>{CSS}</style>
</head>
<body>
<div class="top"><div class="in"><a class="co" href="/prova/"><img src="/logo.png" alt="" width="47" height="26">Vicino&nbsp;Labs</a>
<div class="langbar" role="group" aria-label="Language">{buttons}</div></div></div>
"""


FOOT = f"""<footer><div class="wrap"><p style="margin:0">
<a href="/prova/">Prova</a><a href="/prova/privacy/" data-t="privacy"></a><a href="/prova/terms/" data-t="terms"></a>
<a href="/impressum/">Impressum</a><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<div style="margin-top:10px">© 2026 Vicino Labs</div></div></footer>"""


def _mine(s):
    """렛지 틀을 프로바 것으로 돌린다.

    앱 이름과 주소만 바뀐다. 화면과 흐름은 손대지 않는다 — 한쪽만 고쳐지는
    일을 막으려고 일부러 같은 틀을 쓴다.
    """
    return (s.replace('APP="leggii"', 'APP="prova"')
             .replace('app:"leggii"', 'app:"prova"')
             .replace("/leggii/", "/prova/"))


# 출시 가격 약속 줄은 뺀다. 렛지에는 2027년까지라는 약속이 있지만 프로바에는
# 없다. 틀에서 그 한 줄만 들어낸다.
BUY_BODY = _mine(LP.BUY_BODY).replace(
    '\n    <p class="fine" style="margin-top:4px" data-t="launch_price"></p>', "")


def buy_page():
    body = (BUY_BODY.replace("__BADGES__", _badges())
            .replace("__HIDE50__", "" if SHOW_50 else " hidden"))
    js = (_mine(LP.COMMON_JS).replace("__T__", LP._json(T))
          + _mine(LP.BUY_JS).replace("__PRICES__", LP._json(PRICES))
                            .replace("__SHOW50__", "true" if SHOW_50 else "false"))
    return (_head(T["en"]["title"], T["en"]["desc"], "/prova/plus/")
            + body + FOOT + f"<script>{js}</script>\n</body></html>\n")


def thanks_page():
    body = _mine(LP.THANKS_BODY).replace("__BADGES__", _badges())
    js = _mine(LP.COMMON_JS).replace("__T__", LP._json(T)) + _mine(LP.THANKS_JS)
    return (_head(T["en"]["thanks_title"], T["en"]["desc"], "/prova/plus/danke/")
            + body + FOOT + f"<script>{js}</script>\n</body></html>\n")
