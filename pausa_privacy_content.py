"""파우사(Pausa) 개인정보처리방침 본문 (ko/en/de/it). pausa_legal.py가 HTML로 만든다.

2026-11-12 버전 1.0 초안 (앱 1.0). 운영자 승인 전 초안. 시행일은 "2026.11.13" 자리를 운영자가 채운다.
prova_privacy_content.py의 틀과 문구를 따랐다(운영자 이름·주소는 맨 아래 문의처에만, 1장은 한 줄 안내).
앱 1.0: 계정 없음, 카메라·위치·연락처 없음, 마이크는 무대 탭 조율기에서만(누를 때, 기기 안에서 분석, 녹음·저장·전송 없음), 광고·분석·추적 SDK 없음, Vicino Labs 서버로 올리는 것 없음.
모든 소리는 앱에 들어 있어 스트리밍 없음. 기기에만: 마지막 믹스, 저장한 믹스, 언어, 첫 안내 완료 여부,
체험 시작일·기간, 구독 상태 캐시. 결제는 App Store·Google Play만(스토어 플러그인으로 구매 상태·토큰만 받음).
체험 종료 2일 전 로컬 알림(허용 시, 푸시 서버 없음). 안드로이드 자동 백업(Prova와 같음).
2026-11-12 밤 새 설계(무대 탭): 조율기가 마이크를 씀(기기 안에서만), 무대 계획·기록·기준음은 기기에만 저장.
2026-11-12 앱에 위레가토 통합 아이디 로그인(선택)이 들어가 "위레가토 통합 아이디" 장을 더했다. 로그인에 기대는 기능은 아직 없다.
2026-11-13 수탁자 장(9장) 추가(GDPR 13조, HQ), 첫 문단의 '계정 없음'을 '로그인 없이'로 고침. 문의처는 14장.
환영 메일은 보내지 않는다(서버에 Pausa용 메일이 없음). 로그인 화면은 이메일 쪽에 Cloudflare Turnstile을 쓴다.
"""

from appoggio_privacy_content import EMAIL, _id_card
from prova_privacy_content import _op_ref

GOOGLE_PRIVACY = "https://policies.google.com/privacy"
APPLE_PRIVACY = "https://www.apple.com/legal/privacy/"

# Contact is the last section: keep N in step with the section list.
N = 14

_G = f'href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener"'
_A = f'href="{APPLE_PRIVACY}" target="_blank" rel="noopener"'

PRIVACY = {
 "ko": {
  "title": "파우사(Pausa) 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.11.13"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "Vicino Labs가 만든 파우사(Pausa)는 카페, 독서, 작업, 잠들기 전 같은 시간에 어울리는 소리를 만드는 앱입니다. 음악에 빗소리, 장작불, 카페 소음, 바람을 섞을 수 있습니다. 무대에 오르기 전 준비를 돕는 무대 탭도 있습니다. 로그인 없이 모두 쓸 수 있고, 모든 소리는 앱 안에 들어 있으며, 로그인하지 않으면 저희 서버로 보내는 정보가 없습니다. 앱이 다루는 정보를 정확하게 적어 둡니다.",
  "footer": "본 방침은 2026년 11월 13일부터 시행됩니다 (버전 1.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _op_ref("ko", N) + "<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>로그인 없이 모두 쓸 수 있습니다. 위레가토 통합 아이디 로그인은 선택이며, 로그인하지 않으면 이름, 이메일, 전화번호를 받지 않습니다.</li>
<li>믹스와 설정은 <strong>기기 안에만</strong> 저장되며, 저희 서버로 올라가는 정보가 없습니다.</li>
<li>모든 소리는 앱 안에 들어 있어 인터넷 없이도 재생됩니다. 스트리밍하지 않습니다.</li>
<li>카메라, 위치, 연락처를 쓰지 않습니다. 마이크는 무대 탭의 조율기를 켤 때만 쓰고, 소리를 녹음하거나 보내지 않습니다.</li>
<li>광고, 분석·추적 도구가 없습니다.</li>
<li>결제는 App Store와 Google Play가 처리하며, 저희는 카드 정보를 받지 않습니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>마지막으로 들은 믹스와 이용자가 저장한 믹스</li>
<li>고른 언어, 처음 안내를 마쳤는지 여부</li>
<li>무료 체험 시작일과 기간</li>
<li>구독·구매 상태(스토어에서 받은 상태를 기기에 잠시 저장해 둔 것)</li>
</ul>
<p>이 정보는 기기 안의 앱 전용 저장소에 있고 저희에게 전송되지 않습니다. 앱을 삭제하면 사라집니다. 처리 근거: 앱 기능 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("재생과 권한", """<p>파우사는 카메라, 위치, 연락처 권한을 요청하지 않습니다. 마이크 권한은 무대 탭에서 조율기(소리 내어 맞춰 보기)를 처음 켤 때만 묻습니다. 조율기는 들어오는 소리의 높이를 기기 안에서 바로 계산해 화면에 보여 줄 뿐이며, 소리를 녹음하거나 저장하거나 어디로도 보내지 않습니다. 허용하지 않아도 다른 기능은 모두 쓸 수 있습니다. 바이노럴 비트는 기기에서 바로 만들어 내는 소리이며(왼쪽과 오른쪽 귀에 서로 다른 음), 다른 소리도 모두 앱 안에 들어 있습니다. 그래서 다른 앱을 쓰거나 화면이 꺼져 있어도, 그리고 인터넷 없이도 재생됩니다.</p>"""),
   ("구독·구매", f"""<p>구독(연간, 월간)과 한 번 결제하는 평생 이용권은 App Store 또는 Google Play에서만 삽니다. 결제와 카드 정보는 스토어가 처리하며 저희는 받지 않습니다.</p>
<ul>
<li>앱은 스토어의 결제 기능을 통해 기기에서 구매 상태와 구매 증명(토큰)을 받아, 유료 기능을 열지 판단합니다. 이 정보는 저희 서버로 보내지 않습니다.</li>
<li>스토어의 처리에는 <a {_A}>Apple 개인정보 처리방침</a> 또는 <a {_G}>Google 개인정보처리방침</a>이 적용됩니다.</li>
</ul>
<p>처리 근거: 구매한 서비스의 제공(b호).</p>"""),
   ("무료 체험 종료 알림", """<p>연간 구독의 7일 무료 체험을 시작하기 전에 앱이 체험이 끝나는 정확한 날짜를 보여 드립니다. 이용자가 알림을 허용하면, 체험이 끝나기 2일 전에 기기 안에서 알림이 한 번 울리도록 예약합니다. 이 알림은 기기에서만 만들고 울리며, 저희는 푸시 서버를 쓰지 않습니다. 알림 권한은 언제든 기기 설정에서 끌 수 있습니다.</p>"""),
   ("안드로이드 자동 백업", f"""<p>안드로이드에서는 기기의 Google 백업 기능이 켜져 있으면 앱의 <strong>설정</strong>이 이용자의 Google 계정에 백업되어, 다시 설치할 때 복원될 수 있습니다. 이 백업은 Google이 <a {_G}>Google 개인정보처리방침</a>에 따라 처리하며 저희는 볼 수 없습니다. 기기 설정에서 끌 수 있습니다.</p>"""),
   ("위레가토 통합 아이디 (선택)", f"""<p>파우사는 로그인 없이 모두 쓸 수 있습니다. 원하면 설정에서 위레가토 통합 아이디(같은 회사가 운영하는 위레가토의 계정, 모든 Vicino Labs 앱에서 쓰는 하나의 아이디)로 로그인할 수 있습니다. 아래 내용은 이용자가 로그인할 때만 적용됩니다.</p>
<ul>
<li><strong>계정 정보</strong>(이메일, 이름, 로그인 방식 Google·카카오·Apple·이메일, 계정 번호)는 <a href="https://welegato.com/legal/" target="_blank" rel="noopener">위레가토 개인정보처리방침</a>에 따라 처리됩니다. 로그인은 Supabase Auth로 처리됩니다. 파우사에서 가입하면 “파우사에서 가입함” 표시가 계정에 남습니다.</li>
<li>지금 파우사는 로그인 정보를 다른 기능에 쓰지 않습니다. 믹스와 설정은 로그인해도 기기에만 남습니다.</li>
<li>이메일 가입·로그인에서는 자동 가입을 막기 위해 Cloudflare Turnstile이 브라우저 정보를 확인합니다(<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">Cloudflare 개인정보처리방침</a>). Google, 카카오, Apple 로그인에는 각 회사의 방침이 적용됩니다.</li>
<li>앱의 아이디 관리 또는 <a href="https://welegato.com/konto-loeschen" target="_blank" rel="noopener">welegato.com/konto-loeschen</a>에서 아이디를 삭제하면, 이 아이디를 쓰는 모든 Vicino Labs 앱에서 계정이 지워집니다. 기기 안의 믹스와 설정은 남습니다.</li>
</ul>
<p>위레가토 약관에 따라 로그인은 만 16세 이상만 할 수 있습니다. 처리 근거: 이용자가 선택한 기능의 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("서비스 제공자(수탁자)와 국외 이전", """<ul>
<li><strong>Supabase</strong>: 위레가토 통합 아이디 로그인과 계정 데이터베이스, 계정 삭제 처리. EU(독일 프랑크푸르트) 데이터센터 (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">방침</a>)</li>
<li><strong>Google</strong>: Google Play 결제, Google 로그인, 안드로이드 자동 백업</li>
<li><strong>Apple</strong>: App Store 결제, Apple로 로그인(iPhone·iPad)</li>
<li><strong>Kakao</strong>: 카카오 로그인</li>
<li><strong>Cloudflare</strong>: 이메일 로그인의 자동 가입 방지(Turnstile) (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">방침</a>)</li>
</ul>
<p>로그인하지 않으면 Supabase, Kakao, Cloudflare로 가는 정보는 없습니다. 이 업체들이 EU 밖(예: 미국)에서 처리하는 경우, EU 표준계약조항 또는 EU-미국 데이터 프라이버시 프레임워크를 근거로 합니다.</p>"""),
   ("수집하지 않는 정보", """<p>로그인하지 않으면 이름, 이메일, 전화번호를 받지 않습니다. 위치, 연락처, 광고 식별자를 수집하지 않으며, 카메라를 쓰지 않습니다. 마이크는 조율기에서만 기기 안에서 쓰고 소리를 녹음하거나 보내지 않습니다. 광고 네트워크와 분석·추적 SDK가 없고, 위레가토 통합 아이디 로그인 말고는 저희가 운영하는 서버로 보내는 정보가 없습니다. 그래서 저희는 이용자가 누구인지, 앱을 어떻게 쓰는지 알 수 없습니다.</p>"""),
   ("아동", """<p>이 앱은 만 16세 미만 아동을 대상으로 하지 않습니다. 로그인은 위레가토 약관에 따라 만 16세 이상만 할 수 있습니다.</p>"""),
   ("정보주체의 권리", f"""<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리. 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>저희는 이용자에 관한 정보를 서버에 갖고 있지 않습니다. 기기 안의 정보는 앱을 삭제하면 사라집니다. 궁금한 점은 <a href="mailto:{EMAIL}">{EMAIL}</a>로 문의해 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 본 방침을 고칠 수 있으며, 변경 내용과 시행일을 이 페이지에 게시합니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Pausa Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-11-13"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "Pausa, made by Vicino Labs, creates sound for the café, reading, desk work and bedtime. You can mix music with rain, fireplace, café murmur and wind. A Stage tab helps you get ready before you go on. Everything works without signing in, every sound is built into the app, and if you don't sign in nothing is sent to our servers. Here is exactly what the app handles.",
  "footer": "This policy is effective from 13 November 2026 (version 1.0).",
  "other": "Terms of Service →",
  "sections": [
   ("Data controller", _op_ref("en", N) + "<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for any personal data processed in connection with this app.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>Everything works without signing in. Signing in with a welegato ID is optional; if you don't, we receive no name, email or phone number.</li>
<li>Your mixes and settings stay <strong>on your device</strong>; nothing is uploaded to our servers.</li>
<li>Every sound is built into the app and plays offline. Nothing is streamed.</li>
<li>No camera, location or contacts. The microphone is used only by the tuner on the Stage tab, and nothing is recorded or sent.</li>
<li>No ads, and no analytics or tracking tools.</li>
<li>Payments are handled by the App Store and Google Play; we never receive card details.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>The mix you last listened to and the mixes you saved</li>
<li>Your chosen language and whether you finished the introduction</li>
<li>The start date and length of your free trial</li>
<li>Your subscription or purchase status (a copy of what the store reports, kept on the device)</li>
</ul>
<p>This data stays in the app's private storage and is never sent to us. It is deleted when you uninstall the app. Legal basis: providing the app's features (Art. 6(1)(b) GDPR).</p>"""),
   ("Playback and permissions", """<p>Pausa asks for no camera, location or contacts permission. It asks for the microphone only when you first turn on the tuner on the Stage tab. The tuner works out the pitch of what it hears on your device, in real time, and shows it on screen; it does not record, store or send any sound. Everything else works without this permission. The binaural tone is generated live on your device (a different tone in each ear), and all other sounds are built into the app. So it keeps playing in the background, with the screen off and without an internet connection.</p>"""),
   ("Subscriptions and purchases", f"""<p>Subscriptions (yearly and monthly) and the one-time lifetime purchase are bought only through the App Store or Google Play. The store handles payment and card details; we never receive them.</p>
<ul>
<li>Through the store's payment interface on your device, the app receives the purchase status and proof of purchase (token) to decide whether to unlock paid features. This is not sent to our servers.</li>
<li>The store's processing falls under the <a {_A}>Apple Privacy Policy</a> or the <a {_G}>Google Privacy Policy</a>.</li>
</ul>
<p>Legal basis: providing what you bought (b).</p>"""),
   ("Free trial reminder", """<p>Before you start the 7-day free trial of the yearly subscription, the app shows the exact date the trial ends. If you allow notifications, the app schedules one notification on your device for 2 days before the trial ends. It is created and shown on the device only; we use no push server. You can turn notifications off at any time in your device settings.</p>"""),
   ("Android backup", f"""<p>On Android, if your device's Google backup is on, the app's <strong>settings</strong> may be backed up to your Google account and restored when you reinstall. Google handles this backup under the <a {_G}>Google Privacy Policy</a>; we cannot see it. You can turn it off in your device settings.</p>"""),
   ("welegato ID (optional)", f"""<p>Everything in Pausa works without signing in. If you want, you can sign in under Settings with a welegato ID (an account of welegato, run by the same company: one ID for all Vicino Labs apps). This section applies only when you sign in.</p>
<ul>
<li><strong>Account data</strong> (email, name, sign-in method Google, Kakao, Apple or email, account number) is processed under the <a href="https://welegato.com/legal/" target="_blank" rel="noopener">welegato privacy policy</a>. Sign-in is handled by Supabase Auth. An ID created in Pausa is marked “signed up in Pausa”.</li>
<li>Pausa does not use your sign-in for anything else yet. Your mixes and settings stay on your device even when you are signed in.</li>
<li>For email sign-up and sign-in, Cloudflare Turnstile checks browser signals to stop automated sign-ups (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">Cloudflare privacy policy</a>). Google, Kakao and Apple sign-in fall under those companies' policies.</li>
<li>Deleting the ID in the app or at <a href="https://welegato.com/konto-loeschen" target="_blank" rel="noopener">welegato.com/konto-loeschen</a> deletes the account in every Vicino Labs app that uses it. Mixes and settings on your device stay.</li>
</ul>
<p>Under welegato's terms, only people aged 16 or over can sign in. Legal basis: providing the feature you chose (Art. 6(1)(b) GDPR).</p>"""),
   ("Service providers (processors) and transfers", """<ul>
<li><strong>Supabase</strong>: welegato ID sign-in, the account database and account deletion. EU data centre (Frankfurt, Germany) (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">policy</a>)</li>
<li><strong>Google</strong>: Google Play payments, Google sign-in, Android auto backup</li>
<li><strong>Apple</strong>: App Store payments, Sign in with Apple (iPhone, iPad)</li>
<li><strong>Kakao</strong>: Kakao sign-in</li>
<li><strong>Cloudflare</strong>: protection against automated email sign-ups (Turnstile) (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">policy</a>)</li>
</ul>
<p>If you don't sign in, nothing goes to Supabase, Kakao or Cloudflare. Where these providers process data outside the EU (e.g. in the USA), this is based on the EU Standard Contractual Clauses or the EU-U.S. Data Privacy Framework.</p>"""),
   ("Data we don't collect", """<p>Unless you sign in, we receive no name, email or phone number. We collect no location, contacts or advertising ID, and the app does not use the camera. The microphone is used only by the tuner, on your device, and nothing is recorded or sent. There are no ad networks or analytics or tracking SDKs, and apart from the optional welegato ID sign-in nothing is sent to any server we run. So we cannot tell who you are or how you use the app.</p>"""),
   ("Children", """<p>The app is not directed at children under 16. Under welegato's terms only people aged 16 or over can sign in.</p>"""),
   ("Your rights", f"""<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR)</li>
<li>Lodge a complaint with a supervisory authority, e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live</li>
</ul>
<p>We hold no data about you on any server. Data on your device is deleted when you uninstall the app. For any questions, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law or the app changes; changes and the effective date are posted on this page.</p>"""),
   ("Contact", "<p>For questions about data protection, please contact us.</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Pausa Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "13.11.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Pausa von Vicino Labs macht Klang fürs Café, zum Lesen, für die Arbeit am Schreibtisch und vor dem Schlafen. Du kannst Musik mit Regen, Kaminfeuer, Cafégeräuschen und Wind mischen. Der Bühnen-Tab hilft dir, dich vor dem Auftritt vorzubereiten. Alles funktioniert ohne Anmeldung, alle Klänge stecken in der App, und ohne Anmeldung werden keine Daten an unsere Server gesendet. Hier steht genau, welche Daten die App verarbeitet.",
  "footer": "Diese Erklärung gilt ab dem 13. November 2026 (Version 1.0).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _op_ref("de", N) + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für Verarbeitungen im Zusammenhang mit dieser App.</p>"),
   ("Kurzfassung", """<div class="summary-box"><ul>
<li>Alles funktioniert ohne Anmeldung. Die Anmeldung mit einer welegato-ID ist freiwillig; ohne sie erhalten wir weder Namen noch E-Mail-Adresse oder Telefonnummer.</li>
<li>Deine Mixe und Einstellungen bleiben <strong>auf deinem Gerät</strong>; nichts wird auf unsere Server hochgeladen.</li>
<li>Alle Klänge stecken in der App und laufen auch offline. Es wird nichts gestreamt.</li>
<li>Keine Kamera, kein Standort, keine Kontakte. Das Mikrofon nutzt nur das Stimmgerät im Tab „Bühne“; nichts wird aufgenommen oder gesendet.</li>
<li>Keine Werbung und keine Analyse- oder Tracking-Tools.</li>
<li>Zahlungen wickeln der App Store und Google Play ab; Kartendaten erhalten wir nie.</li>
</ul></div>"""),
   ("Auf dem Gerät gespeicherte Daten", """<ul>
<li>Der zuletzt gehörte Mix und deine gespeicherten Mixe</li>
<li>Die gewählte Sprache und ob du die Einführung abgeschlossen hast</li>
<li>Beginn und Dauer deines kostenlosen Probezeitraums</li>
<li>Dein Abo- oder Kaufstatus (eine auf dem Gerät gespeicherte Kopie dessen, was der Store meldet)</li>
</ul>
<p>Diese Daten bleiben im privaten Speicher der App und werden nicht an uns übermittelt. Sie werden gelöscht, wenn du die App deinstallierst. Rechtsgrundlage: Bereitstellung der App-Funktionen (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Wiedergabe und Berechtigungen", """<p>Pausa fragt nicht nach Kamera, Standort oder Kontakten. Nach dem Mikrofon fragt die App nur, wenn du im Tab „Bühne“ zum ersten Mal das Stimmgerät einschaltest. Das Stimmgerät bestimmt die Tonhöhe des Gehörten direkt auf deinem Gerät und zeigt sie an; es nimmt keinen Ton auf, speichert nichts und sendet nichts. Alles andere funktioniert auch ohne diese Berechtigung. Der binaurale Ton wird direkt auf deinem Gerät erzeugt (auf jedem Ohr ein anderer Ton), alle anderen Klänge stecken in der App. Deshalb läuft die Wiedergabe auch im Hintergrund, bei ausgeschaltetem Bildschirm und ohne Internetverbindung weiter.</p>"""),
   ("Abos und Käufe", f"""<p>Abos (jährlich und monatlich) und den einmaligen Kauf auf Lebenszeit gibt es nur über den App Store oder Google Play. Zahlung und Kartendaten verarbeitet der Store; wir erhalten sie nicht.</p>
<ul>
<li>Über die Kaufschnittstelle des Stores auf deinem Gerät erhält die App den Kaufstatus und den Kaufnachweis (Token), um zu entscheiden, ob kostenpflichtige Funktionen freigeschaltet werden. Diese Daten werden nicht an unsere Server gesendet.</li>
<li>Für den Store gilt die <a {_A}>Datenschutzrichtlinie von Apple</a> bzw. die <a {_G}>Datenschutzerklärung von Google</a>.</li>
</ul>
<p>Rechtsgrundlage: Erbringung des Gekauften (lit. b).</p>"""),
   ("Erinnerung vor Ende des Probezeitraums", """<p>Bevor du den 7-tägigen kostenlosen Probezeitraum des Jahresabos startest, zeigt dir die App das genaue Enddatum. Wenn du Benachrichtigungen erlaubst, plant die App auf deinem Gerät eine Benachrichtigung 2 Tage vor dem Ende ein. Sie wird nur auf dem Gerät erstellt und angezeigt; wir nutzen keinen Push-Server. Benachrichtigungen kannst du jederzeit in den Geräteeinstellungen abschalten.</p>"""),
   ("Android-Sicherung", f"""<p>Unter Android können, wenn die Google-Sicherung des Geräts aktiv ist, die <strong>Einstellungen</strong> der App in deinem Google-Konto gesichert und bei einer Neuinstallation wiederhergestellt werden. Google verarbeitet diese Sicherung gemäß der <a {_G}>Google-Datenschutzerklärung</a>; wir haben keinen Zugriff. Du kannst sie in den Geräteeinstellungen abschalten.</p>"""),
   ("welegato-ID (freiwillig)", f"""<p>Pausa funktioniert vollständig ohne Anmeldung. Wenn du möchtest, kannst du dich in den Einstellungen mit einer welegato-ID anmelden (ein Konto von welegato, einem Dienst desselben Unternehmens: eine ID für alle Apps von Vicino Labs). Dieser Abschnitt gilt nur, wenn du dich anmeldest.</p>
<ul>
<li><strong>Kontodaten</strong> (E-Mail, Name, Anmeldeweg Google, Kakao, Apple oder E-Mail, Kontonummer) werden nach der <a href="https://welegato.com/legal/" target="_blank" rel="noopener">welegato-Datenschutzerklärung</a> verarbeitet. Die Anmeldung läuft über Supabase Auth. Eine in Pausa erstellte ID wird als „in Pausa registriert“ markiert.</li>
<li>Pausa nutzt die Anmeldung bisher für nichts weiter. Deine Mixe und Einstellungen bleiben auch angemeldet auf deinem Gerät.</li>
<li>Bei Registrierung und Anmeldung per E-Mail prüft Cloudflare Turnstile Browser-Signale gegen automatische Registrierungen (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">Datenschutzerklärung von Cloudflare</a>). Für die Anmeldung mit Google, Kakao oder Apple gelten deren Erklärungen.</li>
<li>Löschst du die ID in der App oder unter <a href="https://welegato.com/konto-loeschen" target="_blank" rel="noopener">welegato.com/konto-loeschen</a>, wird das Konto in allen Apps von Vicino Labs gelöscht, die diese ID nutzen. Mixe und Einstellungen auf dem Gerät bleiben.</li>
</ul>
<p>Nach den welegato-Bedingungen können sich nur Personen ab 16 Jahren anmelden. Rechtsgrundlage: Bereitstellung der gewählten Funktion (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Dienstleister (Auftragsverarbeiter) und Übermittlungen", """<ul>
<li><strong>Supabase</strong>: Anmeldung mit der welegato-ID, Konto-Datenbank und Kontolöschung. EU-Rechenzentrum (Frankfurt) (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">Erklärung</a>)</li>
<li><strong>Google</strong>: Google-Play-Zahlungen, Google-Anmeldung, automatische Android-Sicherung</li>
<li><strong>Apple</strong>: App-Store-Zahlungen, „Mit Apple anmelden“ (iPhone, iPad)</li>
<li><strong>Kakao</strong>: Kakao-Anmeldung</li>
<li><strong>Cloudflare</strong>: Schutz vor automatischen E-Mail-Registrierungen (Turnstile) (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">Erklärung</a>)</li>
</ul>
<p>Ohne Anmeldung gehen keine Daten an Supabase, Kakao oder Cloudflare. Verarbeiten diese Anbieter Daten außerhalb der EU (z. B. in den USA), geschieht das auf Grundlage der EU-Standardvertragsklauseln oder des EU-U.S. Data Privacy Framework.</p>"""),
   ("Nicht erhobene Daten", """<p>Ohne Anmeldung erhalten wir weder Namen noch E-Mail-Adresse oder Telefonnummer. Standort, Kontakte und Werbe-IDs erheben wir nicht, und die App nutzt keine Kamera. Das Mikrofon nutzt nur das Stimmgerät, auf deinem Gerät, ohne Aufnahme oder Übertragung. Es gibt keine Werbenetzwerke und keine Analyse- oder Tracking-SDKs, und außer bei der freiwilligen Anmeldung mit der welegato-ID werden keine Daten an einen von uns betriebenen Server gesendet. Wir wissen also nicht, wer du bist oder wie du die App nutzt.</p>"""),
   ("Kinder", """<p>Die App richtet sich nicht an Kinder unter 16 Jahren. Anmelden können sich nach den welegato-Bedingungen nur Personen ab 16 Jahren.</p>"""),
   ("Deine Rechte", f"""<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO)</li>
<li>Beschwerde bei einer Aufsichtsbehörde, z. B. bei der Landesbeauftragten für Datenschutz und Informationsfreiheit NRW (LDI NRW) oder der Behörde deines Wohnorts</li>
</ul>
<p>Wir speichern auf keinem Server Daten über dich. Daten auf deinem Gerät werden gelöscht, wenn du die App deinstallierst. Bei Fragen schreib uns an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich Recht oder App ändern; Änderungen und das Datum stehen auf dieser Seite.</p>"""),
   ("Kontakt", "<p>Fragen zum Datenschutz richte bitte an:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Pausa — Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "13.11.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Pausa, di Vicino Labs, crea il sottofondo giusto per il bar, la lettura, il lavoro alla scrivania e la sera prima di dormire. Puoi mescolare la musica con pioggia, camino, brusio del caffè e vento. La scheda Palco ti aiuta a prepararti prima di salire sul palco. Tutto funziona senza accesso, tutti i suoni sono già nell'app e, se non accedi, nulla viene inviato ai nostri server. Ecco esattamente quali dati tratta l'app.",
  "footer": "Questa informativa è in vigore dal 13 novembre 2026 (versione 1.0).",
  "other": "Termini di utilizzo →",
  "sections": [
   ("Titolare del trattamento", _op_ref("it", N) + "<p>Vicino Labs è il titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per i dati trattati in relazione a questa app.</p>"),
   ("In breve", """<div class="summary-box"><ul>
<li>Tutto funziona senza accesso. L'accesso con un welegato ID è facoltativo; senza, non riceviamo nome, email né numero di telefono.</li>
<li>I tuoi mix e le impostazioni restano <strong>sul tuo dispositivo</strong>; nulla viene caricato sui nostri server.</li>
<li>Tutti i suoni sono già nell'app e funzionano anche offline. Niente streaming.</li>
<li>Niente fotocamera, posizione o contatti. Il microfono lo usa solo l'accordatore nella scheda Palco, senza registrare né inviare nulla.</li>
<li>Niente pubblicità e nessuno strumento di analisi o tracciamento.</li>
<li>I pagamenti li gestiscono l'App Store e Google Play; non riceviamo mai i dati della carta.</li>
</ul></div>"""),
   ("Dati salvati sul dispositivo", """<ul>
<li>L'ultimo mix ascoltato e i mix che hai salvato</li>
<li>La lingua scelta e se hai completato l'introduzione</li>
<li>Data di inizio e durata della prova gratuita</li>
<li>Lo stato dell'abbonamento o dell'acquisto (una copia di quanto comunica lo store, salvata sul dispositivo)</li>
</ul>
<p>Questi dati restano nella memoria privata dell'app e non ci vengono inviati. Si cancellano disinstallando l'app. Base giuridica: fornitura delle funzioni dell'app (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Riproduzione e permessi", """<p>Pausa non chiede l'accesso a fotocamera, posizione o contatti. Chiede il microfono solo quando accendi per la prima volta l'accordatore nella scheda Palco. L'accordatore calcola l'altezza del suono direttamente sul dispositivo e la mostra sullo schermo; non registra, non salva e non invia alcun suono. Tutto il resto funziona anche senza questo permesso. Il tono binaurale è generato in tempo reale sul dispositivo (un tono diverso per ciascun orecchio) e tutti gli altri suoni sono già nell'app. Per questo la riproduzione continua in background, a schermo spento e senza connessione a internet.</p>"""),
   ("Abbonamenti e acquisti", f"""<p>Gli abbonamenti (annuale e mensile) e l'acquisto a vita una tantum si comprano solo tramite l'App Store o Google Play. Il pagamento e i dati della carta li gestisce lo store; noi non li riceviamo.</p>
<ul>
<li>Tramite il sistema di pagamento dello store sul dispositivo, l'app riceve lo stato dell'acquisto e la prova d'acquisto (token) per decidere se sbloccare le funzioni a pagamento. Questi dati non vengono inviati ai nostri server.</li>
<li>Per lo store vale l'<a {_A}>informativa privacy di Apple</a> o l'<a {_G}>informativa privacy di Google</a>.</li>
</ul>
<p>Base giuridica: fornire quanto acquistato (lett. b).</p>"""),
   ("Promemoria di fine prova", """<p>Prima di avviare la prova gratuita di 7 giorni dell'abbonamento annuale, l'app ti mostra la data esatta in cui termina. Se consenti le notifiche, l'app programma sul dispositivo una notifica 2 giorni prima della fine. Viene creata e mostrata solo sul dispositivo; non usiamo alcun server push. Puoi disattivare le notifiche in qualsiasi momento nelle impostazioni del dispositivo.</p>"""),
   ("Backup Android", f"""<p>Su Android, se il backup Google del dispositivo è attivo, le <strong>impostazioni</strong> dell'app possono essere salvate nel tuo account Google e ripristinate in caso di reinstallazione. Google le tratta secondo la propria <a {_G}>informativa sulla privacy</a>; noi non vi abbiamo accesso. Puoi disattivarlo nelle impostazioni del dispositivo.</p>"""),
   ("welegato ID (facoltativo)", f"""<p>Pausa funziona tutta senza accesso. Se vuoi, nelle Impostazioni puoi accedere con un welegato ID (un account di welegato, servizio della stessa società: un solo ID per tutte le app di Vicino Labs). Questa sezione vale solo quando accedi.</p>
<ul>
<li>I <strong>dati dell'account</strong> (email, nome, modo di accesso Google, Kakao, Apple o email, numero di account) sono trattati secondo l'<a href="https://welegato.com/legal/" target="_blank" rel="noopener">informativa privacy di welegato</a>. L'accesso è gestito da Supabase Auth. Un ID creato in Pausa viene segnato «registrato in Pausa».</li>
<li>Per ora Pausa non usa l'accesso per nient'altro. I tuoi mix e le impostazioni restano sul dispositivo anche quando hai fatto l'accesso.</li>
<li>Per registrazione e accesso via email, Cloudflare Turnstile controlla segnali del browser contro le registrazioni automatiche (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">informativa di Cloudflare</a>). Per l'accesso con Google, Kakao o Apple valgono le loro informative.</li>
<li>Eliminando l'ID nell'app o su <a href="https://welegato.com/konto-loeschen" target="_blank" rel="noopener">welegato.com/konto-loeschen</a> l'account viene cancellato in tutte le app di Vicino Labs che lo usano. Mix e impostazioni sul dispositivo restano.</li>
</ul>
<p>Secondo i termini di welegato, possono accedere solo persone dai 16 anni in su. Base giuridica: fornire la funzione scelta (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Fornitori di servizi (responsabili) e trasferimenti", """<ul>
<li><strong>Supabase</strong>: accesso con welegato ID, database degli account e cancellazione dell'account. Data center UE (Francoforte) (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">informativa</a>)</li>
<li><strong>Google</strong>: pagamenti Google Play, accesso con Google, backup automatico di Android</li>
<li><strong>Apple</strong>: pagamenti App Store, accesso con Apple (iPhone, iPad)</li>
<li><strong>Kakao</strong>: accesso con Kakao</li>
<li><strong>Cloudflare</strong>: protezione dalle registrazioni email automatiche (Turnstile) (<a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">informativa</a>)</li>
</ul>
<p>Se non accedi, nessun dato va a Supabase, Kakao o Cloudflare. Se questi fornitori trattano dati fuori dall'UE (ad es. negli USA), ciò avviene in base alle Clausole contrattuali standard UE o all'EU-U.S. Data Privacy Framework.</p>"""),
   ("Dati che non raccogliamo", """<p>Se non accedi, non riceviamo nome, email né numero di telefono. Non raccogliamo posizione, contatti né ID pubblicitari, e l'app non usa la fotocamera. Il microfono lo usa solo l'accordatore, sul dispositivo, senza registrare né inviare nulla. Non ci sono reti pubblicitarie né SDK di analisi o tracciamento, e, a parte l'accesso facoltativo con il welegato ID, nulla viene inviato a server gestiti da noi. Quindi non sappiamo chi sei né come usi l'app.</p>"""),
   ("Minori", """<p>L'app non è rivolta a minori di 16 anni. Secondo i termini di welegato possono accedere solo persone dai 16 anni in su.</p>"""),
   ("I tuoi diritti", f"""<ul>
<li>Accesso, rettifica, cancellazione, limitazione, portabilità e opposizione (artt. 15–21 GDPR)</li>
<li>Reclamo a un'autorità di controllo, ad es. l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o quella del tuo luogo di residenza</li>
</ul>
<p>Non conserviamo dati su di te in alcun server. I dati sul dispositivo si cancellano disinstallando l'app. Per qualsiasi domanda scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Modifiche", """<p>Possiamo aggiornare questa informativa se cambiano la legge o l'app; modifiche e data di entrata in vigore sono pubblicate in questa pagina.</p>"""),
   ("Contatti", "<p>Per domande sulla protezione dei dati scrivici:</p>" + _id_card("it")),
  ],
 },
}

for _d in PRIVACY.values():
    assert len(_d["sections"]) == N, "update N (Contact section number)"
