"""스퀼로(Squillo) 개인정보처리방침 본문 (ko/en/de/it) — squillo_legal.py가 HTML로 만든다.

2026-11-26 버전 1.0 초안 (운영자 승인 전, 페이지에 초안 표시가 붙음).
틀과 문구는 chiave_privacy_content.py(위레가토 통합 아이디·구독)와
leggii_privacy_content.py(클라우드 R2)를 따랐다.
사실 출처: claude-handoff/SQUILLO.md 「스퀼로 세션이 확인해 준 사실」, 스퀼로 Pro 사양(2026-11-26),
그리고 2026-11-26 코드 확인(App/squillo e080e09):
- 로그인은 선택(위레가토 통합 아이디: 이메일·Google·카카오·Apple, Turnstile, signup_app=Squillo).
  로그인하지 않아도 무료 범위(기본 발성 8곡, 곡집마다 앞 2곡)는 그대로 쓴다.
- 3일 체험은 처음 설치부터, 로그인 없이(대표님 2026-11-26). 재설치 반복은 기기 해시 서버로 막음(대표님 결정, 끼아베와 같은 방식, 0180 squillo_devices, 마지막 확인 후 1년 보관). 구독 기록 squillo_subscriptions.
- 백업(Pro, 1GB)은 leggii-cloud 함수와 같은 길(Cloudflare R2 + Supabase 목록). 아직 앱에 연결 전.
  보관 기간 "Pro 종료 후 90일"은 렛지와 같게 둔 가정이다 — 운영자 확인 필요.
- 무료 악보 찾기: R2 공개 버킷에서 내려받기만.
- 마이크·카메라·사진·위치·알림 권한 없음. 분석·크래시·광고 SDK 없음.
- 위레가토 링크에 utm_source=squillo.
"""

from appoggio_privacy_content import EMAIL, _id_card
from chiave_privacy_content import _op_ref, _draft

WELEGATO_PRIVACY = "https://welegato.com/legal/"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
APPLE_PRIVACY = "https://www.apple.com/legal/privacy/"
CF_PRIVACY = "https://www.cloudflare.com/privacypolicy/"
SUPABASE_PRIVACY = "https://supabase.com/privacy"

LAST = 15  # 문의처 절 번호 (_op_ref가 가리키는 곳)

PRIVACY = {
 "ko": {
  "title": "스퀼로(Squillo) 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.12.01 (예정)"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": _draft("ko") + "Vicino Labs가 만든 스퀼로(Squillo)는 성악가와 노래하는 분을 위한 발성 연습 앱입니다. 기본 발성과 무료 연습곡은 로그인 없이 쓸 수 있고, 설정과 「나의 연습」 악보는 이용자의 기기에 저장됩니다. 선택 로그인(위레가토 통합 아이디), 체험과 구독, Pro 백업, 무료 악보 찾기를 쓸 때만 저희 서버(EU)와 아래 서비스를 거칩니다. 앱이 다루는 정보를 정확하게 적어 둡니다.",
  "footer": "본 방침은 운영자가 확정한 날부터 시행됩니다 (버전 1.0 초안).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _op_ref("ko", LAST) + "<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>기본 발성 연습과 무료 연습곡은 <strong>로그인 없이</strong> 쓸 수 있습니다. 설정과 「나의 연습」 악보는 <strong>기기 안에</strong> 저장됩니다.</li>
<li>앱은 <strong>마이크, 카메라, 사진, 위치, 연락처를 쓰지 않습니다.</strong> 노래를 녹음하거나 연습 기록을 서버로 보내지 않습니다.</li>
<li><strong>위레가토 통합 아이디</strong> 로그인은 선택입니다. Pro 구독과 Pro 백업을 쓰려면 로그인이 필요합니다(처음 설치 뒤 3일 체험에는 필요하지 않습니다). 계정 정보는 위레가토 개인정보처리방침에 따라 처리됩니다.</li>
<li><strong>Pro 백업</strong>을 쓰면 「나의 연습」 악보가 같은 아이디의 기기들을 위해 클라우드(Cloudflare R2)에 저장됩니다.</li>
<li>광고 네트워크와 분석·추적 도구가 없습니다. 화면의 welegato 링크는 같은 회사 서비스를 알리는 자체 배너입니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>앱 설정(성부, 기준음, 템포, 피아노 소리, 테마, 언어 등)과 즐겨찾기</li>
<li>「나의 연습」에 가져온 악보(MusicXML)</li>
<li>연주를 위해 기기에서 만든 피아노 소리 파일</li>
<li>로그인한 경우 로그인 상태를 유지하기 위한 토큰과 마지막으로 받은 요금제 정보</li>
</ul>
<p>이 정보는 기기 안의 앱 저장소에 있고, 아래 Pro 백업을 켠 경우를 빼면 저희에게 전송되지 않습니다. 앱을 삭제하면 사라집니다. 안드로이드에서는 기기의 Google 백업 기능이 켜져 있으면 앱 데이터가 이용자의 Google 계정에 백업될 수 있으며, 이 백업은 Google이 처리하고 저희는 볼 수 없습니다. 처리 근거: 앱 기능 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("무료 악보 찾기", """<p>「나의 연습」에서 무료 악보를 찾으면 앱이 저희가 공개해 둔 악보 목록과 악보 파일을 Cloudflare R2에서 내려받습니다. 이때 앱은 아무 정보도 올리지 않으며, 로그인도 필요하지 않습니다. 인터넷 연결의 특성상 Cloudflare는 요청한 기기의 IP 주소를 짧게 처리합니다.</p>"""),
   ("위레가토 통합 아이디 (선택)", f"""<p>로그인하지 않아도 기본 발성 연습과 무료 연습곡을 그대로 쓸 수 있습니다. 로그인하면 같은 회사가 운영하는 위레가토의 계정(위레가토 통합 아이디)을 씁니다.</p>
<ul>
<li><strong>계정 정보</strong>(이메일, 이름, 로그인 방식 Apple·Google·카카오·이메일, 계정 번호)는 <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">위레가토 개인정보처리방침</a>에 따라 처리됩니다. 스퀼로에서 가입하면 “스퀼로에서 가입함” 표시가 계정에 남습니다.</li>
<li>이메일 가입·로그인에서는 자동 가입을 막기 위해 Cloudflare Turnstile이 브라우저 정보를 확인합니다(<a href="{CF_PRIVACY}" target="_blank" rel="noopener">Cloudflare 개인정보처리방침</a>). Apple·Google·카카오 로그인에는 각 회사의 방침이 적용됩니다.</li>
<li>아이폰·아이패드에서 “Apple로 계속”을 고르면 Apple이 확인한 이름과 이메일을 받습니다. 이용자가 “이메일 가리기”를 고르면 Apple이 만든 중계 주소만 받습니다.</li>
<li><strong>아이디 삭제:</strong> 설정 › 내 아이디 › 아이디 관리 › 아이디 삭제(탈퇴)에서 언제든 지울 수 있습니다. 위레가토 계정이 지워지며 모든 Vicino Labs 앱에 함께 적용됩니다. 스퀼로의 Pro 백업 파일도 함께 지워집니다(세법상 보관해야 하는 결제 기록은 아래와 같습니다). 기기 안의 설정과 악보는 남습니다.</li>
</ul>
<p>위레가토 약관에 따라 로그인은 만 16세 이상만 할 수 있습니다. 처리 근거: 이용자가 선택한 기능의 제공(b호).</p>"""),
   ("무료 체험과 구독", f"""<ul>
<li><strong>3일 무료 체험:</strong> 앱을 처음 설치하면 로그인 없이 3일 동안 모든 기능이 열립니다. 앱을 다시 설치해 체험을 되풀이하지 않도록 기기 식별값(안드로이드는 ANDROID_ID, iPhone·iPad는 키체인에 저장한 무작위 번호)을 씁니다. 서버에는 식별값 자체가 아니라 되돌릴 수 없는 SHA-256 해시(“squillo:” + 식별값)와 처음·마지막으로 확인한 시각만 저장합니다. 이름·이메일은 필요하지 않습니다. 보관 기간: 마지막으로 확인한 날부터 1년이 지나면 지웁니다. iPhone·iPad의 키체인 번호는 앱을 삭제해도 남을 수 있습니다.</li>
<li><strong>구독:</strong> Pro 구독은 Google Play 또는 App Store 결제로 삽니다. 결제와 카드 정보는 스토어가 처리하며 저희는 받지 않습니다. 구독이 유효한지 확인하기 위해 아이디 번호, 상품 이름, 상태, 만료 시각, 스토어의 구매 확인 값을 저장합니다.</li>
<li><strong>보관 기간:</strong> 결제와 관련된 기록은 세법상 보관 의무 기간(최대 10년) 동안 보관합니다.</li>
</ul>
<p>스토어의 처리에는 <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google 개인정보처리방침</a> 또는 <a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">Apple 개인정보 처리방침</a>이 적용됩니다. 처리 근거: 계약 이행(b호), 법적 의무(c호), 체험 남용 방지(f호).</p>"""),
   ("Pro 백업 (선택)", """<p>Pro(체험 포함) 이용자가 로그인한 상태로 백업을 쓰면, 같은 아이디의 기기들에서 「나의 연습」 악보를 똑같이 맞춥니다. 용량은 아이디당 1GB입니다.</p>
<ul>
<li><strong>저장하는 정보:</strong> 「나의 연습」 악보 파일(MusicXML)과 파일 이름, 크기, 지문값(SHA-256), 바뀐 시각.</li>
<li><strong>저장 위치:</strong> 파일은 Cloudflare R2(Cloudflare, Inc., 수탁자)에, 목록과 용량 기록은 저희 서버(Supabase, EU 독일 프랑크푸르트)에 저장됩니다. 전송은 암호화되며, 파일은 짧게만 유효한 서명된 주소로 해당 아이디의 앱에서만 주고받습니다. 저희는 이용자의 악보를 열어 보지 않습니다.</li>
<li><strong>지우기와 보관 기간:</strong> 앱에서 백업 파일을 지우거나 아이디를 지우면 클라우드에서도 지워집니다. Pro가 끝난 뒤에는 90일 동안 보관하고, 그 안에 다시 구독하지 않으면 지웁니다.</li>
</ul>
<p>처리 근거: 이용자가 선택한 기능의 제공(b호).</p>"""),
   ("서비스 제공자(수탁자)와 국외 이전", f"""<ul>
<li><strong>Supabase</strong> — 서버와 데이터베이스, 로그인(위레가토 통합 아이디), EU(독일 프랑크푸르트) 데이터센터 (<a href="{SUPABASE_PRIVACY}" target="_blank" rel="noopener">방침</a>)</li>
<li><strong>Cloudflare</strong> — Pro 백업 파일 저장(R2), 무료 악보 내려받기(R2), 이메일 로그인의 자동 가입 방지(Turnstile)</li>
<li><strong>Google</strong> — Google Play 결제, Google 로그인</li>
<li><strong>Apple</strong> — App Store 결제, Apple로 로그인(iPhone·iPad)</li>
<li><strong>Kakao</strong> — 카카오 로그인</li>
</ul>
<p>이 업체들이 EU 밖(예: 미국)에서 처리하는 경우, EU 표준계약조항 또는 EU-미국 데이터 프라이버시 프레임워크를 근거로 합니다.</p>"""),
   ("welegato 배너와 외부 링크", f"""<p>앱 화면에는 welegato(같은 회사가 운영하는 음악 플랫폼, welegato.com)로 가는 링크가 있고, 설정에는 다른 Vicino Labs 앱의 스토어 페이지로 가는 링크가 있습니다. 광고 네트워크나 추적 도구가 아닌 자체 링크입니다.</p>
<p>링크는 <strong>누를 때만</strong> 브라우저나 스토어에서 열립니다. welegato 링크에는 “스퀼로에서 왔다”는 표시(<code>utm_source=squillo</code> 등 utm 값)만 붙고 이용자를 식별하는 값은 없습니다. 열린 뒤에는 해당 사이트의 방침이 적용됩니다 — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato 개인정보처리방침</a>.</p>"""),
   ("기기 권한", """<p>안드로이드에서는 화면이 꺼져도 연습 소리가 끊기지 않도록 재생 관련 권한(WAKE_LOCK, 미디어 재생 포그라운드 서비스)만 씁니다. 마이크, 카메라, 사진, 위치, 연락처, 알림 권한은 요청하지 않습니다.</p>"""),
   ("수집하지 않는 정보", """<p>로그인하지 않으면 이름·이메일 같은 계정 정보를 받지 않습니다. 노래 소리, 연습 기록, 위치, 연락처, 광고 식별자는 쓰지 않으며, 분석 SDK와 광고 네트워크가 없습니다.</p>"""),
   ("아동", """<p>기본 기능에는 연령 제한이 없습니다. 위레가토 통합 아이디 로그인과 구독은 만 16세 이상만 할 수 있습니다. 어린이가 외부 링크를 쓸 때는 보호자가 함께해 주세요.</p>"""),
   ("정보주체의 권리", f"""<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리 — 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>아이디와 백업은 앱에서 직접 지울 수 있습니다. 그 밖의 요청은 <a href="mailto:{EMAIL}">{EMAIL}</a>로 보내 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 본 방침을 고칠 수 있으며, 변경 내용과 시행일을 이 페이지에 게시합니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Squillo Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-12-01 (planned)"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": _draft("en") + "Squillo, made by Vicino Labs, is a vocal warm-up and practice app for singers. The basic warm-ups and the free studies work without an account, and your settings and My pieces scores are stored on your device. Only the optional sign-in (welegato ID), the trial and subscription, Pro backup and the free score search go through our server (EU) and the services below. Here is exactly what the app handles.",
  "footer": "This policy takes effect on the date the operator confirms it (version 1.0, draft).",
  "other": "Terms of Service →",
  "sections": [
   ("Controller", _op_ref("en", LAST) + "<p>Vicino Labs is the controller under the EU General Data Protection Regulation (GDPR) for the processing of personal data in connection with this app.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>The basic warm-ups and the free studies work <strong>without signing in</strong>. Settings and My pieces scores are stored <strong>on your device</strong>.</li>
<li>The app <strong>does not use the microphone, camera, photos, location or contacts.</strong> It does not record your singing or send practice history to a server.</li>
<li>Signing in with a <strong>welegato ID</strong> is optional. You need it for a Pro subscription and Pro backup (not for the 3-day trial after install). Account data is handled under the welegato privacy policy.</li>
<li>With <strong>Pro backup</strong>, your My pieces scores are stored in the cloud (Cloudflare R2) for the devices signed in with the same ID.</li>
<li>There are no ad networks and no analytics or tracking tools. The welegato link in the app is our own banner for a service of the same company.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>App settings (voice type, concert pitch, tempo, piano sound, theme, language, etc.) and favourites</li>
<li>Scores imported into My pieces (MusicXML)</li>
<li>Piano sound files the app renders on the device for playback</li>
<li>If you are signed in, the token that keeps you signed in and the last plan information received</li>
</ul>
<p>This data stays in the app's storage on your device and is not sent to us, except with Pro backup (below). It is removed when you delete the app. On Android, if Google backup is switched on for the device, app data may be backed up to your Google account; Google handles that backup and we cannot see it. Legal basis: providing the app (Art. 6(1)(b) GDPR).</p>"""),
   ("Free score search", """<p>When you look for free scores in My pieces, the app downloads our public score list and score files from Cloudflare R2. The app uploads nothing for this and no sign-in is needed. As with any internet connection, Cloudflare briefly processes the requesting device's IP address.</p>"""),
   ("welegato ID (optional)", f"""<p>Without signing in you can keep using the basic warm-ups and free studies. If you sign in, you use an account of welegato, a service run by the same company (the welegato ID).</p>
<ul>
<li><strong>Account data</strong> (email, name, sign-in method Apple, Google, Kakao or email, account number) is processed under the <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato privacy policy</a>. If you sign up in Squillo, the account notes “signed up in Squillo”.</li>
<li>For email sign-up and sign-in, Cloudflare Turnstile checks browser information to stop automated sign-ups (<a href="{CF_PRIVACY}" target="_blank" rel="noopener">Cloudflare privacy policy</a>). Sign-in with Apple, Google or Kakao is subject to each company's policy.</li>
<li>If you choose “Continue with Apple” on iPhone or iPad, we receive the name and email confirmed by Apple. If you choose “Hide My Email”, we receive only Apple's relay address.</li>
<li><strong>Deleting your ID:</strong> you can delete it at any time under Settings › My ID › Manage ID › Delete ID. This deletes the welegato account and applies to all Vicino Labs apps. Your Squillo Pro backup files are deleted with it (payment records we must keep for tax purposes are described below). Settings and scores on your device remain.</li>
</ul>
<p>Under the welegato terms, sign-in is for people aged 16 and over. Legal basis: providing the feature you chose (Art. 6(1)(b)).</p>"""),
   ("Free trial and subscription", f"""<ul>
<li><strong>3-day free trial:</strong> when you first install the app, all features are open for 3 days without signing in. So the trial cannot be repeated by reinstalling, the app uses a device identifier (ANDROID_ID on Android, a random number stored in the Keychain on iPhone and iPad). Our server stores not the identifier itself but only an irreversible SHA-256 hash (“squillo:” + identifier) with the first and last time it was checked. No name or email is needed. Retention: deleted one year after it was last checked. The Keychain number on iPhone and iPad may remain after the app is deleted.</li>
<li><strong>Subscription:</strong> Pro is bought through Google Play or the App Store. The store handles payment and card details; we do not receive them. To check that a subscription is valid we store the account number, product name, status, expiry time and the store's purchase confirmation value.</li>
<li><strong>Retention:</strong> payment-related records are kept for the period required by tax law (up to 10 years).</li>
</ul>
<p>The stores' processing is governed by the <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google Privacy Policy</a> or the <a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">Apple Privacy Policy</a>. Legal basis: performance of the contract (b), legal obligation (c), preventing trial abuse (f).</p>"""),
   ("Pro backup (optional)", """<p>When a Pro user (including during the trial) signs in and uses backup, My pieces scores are kept the same on all devices signed in with that ID. Storage is 1 GB per ID.</p>
<ul>
<li><strong>What is stored:</strong> My pieces score files (MusicXML) with file name, size, fingerprint (SHA-256) and last change time.</li>
<li><strong>Where:</strong> files in Cloudflare R2 (Cloudflare, Inc., processor); the list and usage records on our server (Supabase, EU, Frankfurt, Germany). Transfers are encrypted, and files move only through short-lived signed addresses between the app and that ID. We do not open your scores.</li>
<li><strong>Deletion and retention:</strong> deleting a backup file in the app, or deleting your ID, removes it from the cloud as well. After Pro ends we keep the backup for 90 days and delete it if you do not subscribe again in that time.</li>
</ul>
<p>Legal basis: providing the feature you chose (b).</p>"""),
   ("Processors and transfers outside the EU", f"""<ul>
<li><strong>Supabase</strong> — server and database, sign-in (welegato ID), EU data centre (Frankfurt, Germany) (<a href="{SUPABASE_PRIVACY}" target="_blank" rel="noopener">policy</a>)</li>
<li><strong>Cloudflare</strong> — Pro backup storage (R2), free score downloads (R2), protection against automated email sign-ups (Turnstile)</li>
<li><strong>Google</strong> — Google Play billing, Google sign-in</li>
<li><strong>Apple</strong> — App Store billing, Sign in with Apple (iPhone, iPad)</li>
<li><strong>Kakao</strong> — Kakao sign-in</li>
</ul>
<p>Where these providers process data outside the EU (for example in the USA), this is based on the EU Standard Contractual Clauses or the EU-US Data Privacy Framework.</p>"""),
   ("welegato banner and external links", f"""<p>The app shows a link to welegato (a music platform run by the same company, welegato.com), and Settings has links to the store pages of other Vicino Labs apps. These are our own links, not an ad network or tracking tool.</p>
<p>Links open in the browser or store <strong>only when you tap them</strong>. The welegato link carries only a note that you came from Squillo (utm values such as <code>utm_source=squillo</code>) and nothing that identifies you. Once opened, that site's policy applies: <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato privacy policy</a>.</p>"""),
   ("Device permissions", """<p>On Android the app uses only playback permissions (WAKE_LOCK and a media-playback foreground service) so practice sound keeps playing with the screen off. It does not ask for the microphone, camera, photos, location, contacts or notifications.</p>"""),
   ("What we do not collect", """<p>If you do not sign in, we receive no account data such as name or email. The app does not use your singing, practice history, location, contacts or advertising identifiers, and has no analytics SDK or ad network.</p>"""),
   ("Children", """<p>The basic features have no age limit. Signing in with a welegato ID and subscribing are for people aged 16 and over. Children should use external links together with a parent or guardian.</p>"""),
   ("Your rights", f"""<ul>
<li>Access, rectification, erasure, restriction, data portability and objection (Art. 15 to 21 GDPR)</li>
<li>The right to lodge a complaint with a supervisory authority, for example the North Rhine-Westphalia data protection commissioner (LDI NRW) or the authority where you live</li>
</ul>
<p>You can delete your ID and backups yourself in the app. For anything else, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when laws or app features change, and will post the changes and their effective date on this page.</p>"""),
   ("Contact", "<p>For questions about data protection, please contact us.</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Squillo Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "01.12.2026 (geplant)"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": _draft("de") + "Squillo von Vicino Labs ist eine App zum Einsingen und Üben für Sängerinnen und Sänger. Die Grundübungen und die kostenlosen Etüden funktionieren ohne Konto, Einstellungen und Noten unter „Meine Stücke“ bleiben auf deinem Gerät. Nur die optionale Anmeldung (welegato-ID), Testphase und Abo, das Pro-Backup und die kostenlose Notensuche laufen über unseren Server (EU) und die unten genannten Dienste. Hier steht genau, welche Daten die App verarbeitet.",
  "footer": "Diese Erklärung gilt ab dem Tag, an dem der Betreiber sie bestätigt (Version 1.0, Entwurf).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _op_ref("de", LAST) + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für die Verarbeitung personenbezogener Daten im Zusammenhang mit dieser App.</p>"),
   ("Das Wichtigste", """<div class="summary-box"><ul>
<li>Grundübungen und kostenlose Etüden funktionieren <strong>ohne Anmeldung</strong>. Einstellungen und Noten unter „Meine Stücke“ werden <strong>auf deinem Gerät</strong> gespeichert.</li>
<li>Die App <strong>nutzt weder Mikrofon noch Kamera, Fotos, Standort oder Kontakte.</strong> Sie nimmt deinen Gesang nicht auf und schickt keinen Übungsverlauf an einen Server.</li>
<li>Die Anmeldung mit einer <strong>welegato-ID</strong> ist freiwillig. Du brauchst sie für ein Pro-Abo und das Pro-Backup (nicht für die 3-tägige Testphase nach der Installation). Kontodaten werden nach der Datenschutzerklärung von welegato verarbeitet.</li>
<li>Mit dem <strong>Pro-Backup</strong> werden deine Noten unter „Meine Stücke“ für alle Geräte mit derselben ID in der Cloud (Cloudflare R2) gespeichert.</li>
<li>Es gibt keine Werbenetzwerke und keine Analyse- oder Tracking-Tools. Der welegato-Link in der App ist unser eigenes Banner für einen Dienst desselben Unternehmens.</li>
</ul></div>"""),
   ("Daten auf deinem Gerät", """<ul>
<li>App-Einstellungen (Stimmlage, Kammerton, Tempo, Klavierklang, Design, Sprache usw.) und Favoriten</li>
<li>In „Meine Stücke“ importierte Noten (MusicXML)</li>
<li>Klavierklang-Dateien, die die App für die Wiedergabe auf dem Gerät erzeugt</li>
<li>Wenn du angemeldet bist: das Token, das dich angemeldet hält, und die zuletzt empfangenen Tarifinformationen</li>
</ul>
<p>Diese Daten bleiben im App-Speicher auf deinem Gerät und werden nicht an uns gesendet, außer beim Pro-Backup (unten). Beim Löschen der App werden sie entfernt. Ist auf einem Android-Gerät die Google-Sicherung aktiviert, können App-Daten in deinem Google-Konto gesichert werden; diese Sicherung verarbeitet Google, wir sehen sie nicht. Rechtsgrundlage: Bereitstellung der App (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Kostenlose Notensuche", """<p>Wenn du unter „Meine Stücke“ nach kostenlosen Noten suchst, lädt die App unsere öffentliche Notenliste und Notendateien von Cloudflare R2 herunter. Dabei lädt die App nichts hoch, eine Anmeldung ist nicht nötig. Wie bei jeder Internetverbindung verarbeitet Cloudflare kurz die IP-Adresse des anfragenden Geräts.</p>"""),
   ("welegato-ID (freiwillig)", f"""<p>Ohne Anmeldung kannst du die Grundübungen und kostenlosen Etüden weiter nutzen. Wenn du dich anmeldest, verwendest du ein Konto bei welegato, einem Dienst desselben Unternehmens (welegato-ID).</p>
<ul>
<li><strong>Kontodaten</strong> (E-Mail, Name, Anmeldeart Apple, Google, Kakao oder E-Mail, Kontonummer) werden nach der <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von welegato</a> verarbeitet. Registrierst du dich in Squillo, vermerkt das Konto „in Squillo registriert“.</li>
<li>Bei Registrierung und Anmeldung per E-Mail prüft Cloudflare Turnstile Browserinformationen, um automatische Registrierungen zu verhindern (<a href="{CF_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von Cloudflare</a>). Für die Anmeldung mit Apple, Google oder Kakao gelten die Richtlinien des jeweiligen Unternehmens.</li>
<li>Wählst du auf iPhone oder iPad „Mit Apple fortfahren“, erhalten wir den von Apple bestätigten Namen und die E-Mail-Adresse. Wählst du „E-Mail-Adresse verbergen“, erhalten wir nur Apples Weiterleitungsadresse.</li>
<li><strong>ID löschen:</strong> jederzeit unter Einstellungen › Meine ID › ID verwalten › ID löschen. Damit wird das welegato-Konto gelöscht, für alle Apps von Vicino Labs. Deine Pro-Backup-Dateien von Squillo werden mitgelöscht (steuerlich aufzubewahrende Zahlungsdaten siehe unten). Einstellungen und Noten auf deinem Gerät bleiben erhalten.</li>
</ul>
<p>Nach den welegato-Bedingungen ist die Anmeldung ab 16 Jahren möglich. Rechtsgrundlage: Bereitstellung der von dir gewählten Funktion (lit. b).</p>"""),
   ("Testphase und Abo", f"""<ul>
<li><strong>3 Tage kostenlos testen:</strong> Nach der ersten Installation sind 3 Tage lang alle Funktionen ohne Anmeldung offen. Damit sich die Testphase durch Neuinstallation nicht wiederholt, nutzt die App eine Gerätekennung (unter Android die ANDROID_ID, auf iPhone und iPad eine im Schlüsselbund gespeicherte Zufallsnummer). Unser Server speichert nicht die Kennung selbst, sondern nur einen nicht umkehrbaren SHA-256-Hash („squillo:“ + Kennung) sowie den Zeitpunkt der ersten und letzten Prüfung. Name oder E-Mail sind nicht nötig. Speicherdauer: Löschung ein Jahr nach der letzten Prüfung. Die Nummer im Schlüsselbund von iPhone und iPad kann nach dem Löschen der App erhalten bleiben.</li>
<li><strong>Abo:</strong> Pro wird über Google Play oder den App Store gekauft. Zahlung und Kartendaten verarbeitet der Store, wir erhalten sie nicht. Um zu prüfen, ob ein Abo gültig ist, speichern wir Kontonummer, Produktname, Status, Ablaufzeit und den Kaufnachweis des Stores.</li>
<li><strong>Speicherdauer:</strong> Zahlungsbezogene Daten bewahren wir so lange auf, wie es das Steuerrecht verlangt (bis zu 10 Jahre).</li>
</ul>
<p>Für die Verarbeitung durch die Stores gelten die <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von Google</a> bzw. die <a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">Datenschutzrichtlinie von Apple</a>. Rechtsgrundlage: Vertragserfüllung (lit. b), rechtliche Pflicht (lit. c), Schutz vor Missbrauch der Testphase (lit. f).</p>"""),
   ("Pro-Backup (freiwillig)", """<p>Nutzt du als Pro-Kunde (auch in der Testphase) angemeldet das Backup, bleiben deine Noten unter „Meine Stücke“ auf allen Geräten mit derselben ID gleich. Der Speicher beträgt 1 GB pro ID.</p>
<ul>
<li><strong>Was gespeichert wird:</strong> Notendateien aus „Meine Stücke“ (MusicXML) mit Dateiname, Größe, Prüfsumme (SHA-256) und Änderungszeit.</li>
<li><strong>Wo:</strong> Dateien bei Cloudflare R2 (Cloudflare, Inc., Auftragsverarbeiter), Liste und Speicherverbrauch auf unserem Server (Supabase, EU, Frankfurt). Die Übertragung ist verschlüsselt, Dateien laufen nur über kurz gültige, signierte Adressen zwischen der App und dieser ID. Wir öffnen deine Noten nicht.</li>
<li><strong>Löschen und Speicherdauer:</strong> Löschst du eine Backup-Datei in der App oder deine ID, wird sie auch in der Cloud gelöscht. Nach Ende von Pro bewahren wir das Backup 90 Tage auf und löschen es, wenn du in dieser Zeit nicht erneut abonnierst.</li>
</ul>
<p>Rechtsgrundlage: Bereitstellung der von dir gewählten Funktion (lit. b).</p>"""),
   ("Auftragsverarbeiter und Übermittlung außerhalb der EU", f"""<ul>
<li><strong>Supabase</strong> – Server und Datenbank, Anmeldung (welegato-ID), Rechenzentrum in der EU (Frankfurt) (<a href="{SUPABASE_PRIVACY}" target="_blank" rel="noopener">Richtlinie</a>)</li>
<li><strong>Cloudflare</strong> – Speicher für das Pro-Backup (R2), Download kostenloser Noten (R2), Schutz vor automatischen E-Mail-Registrierungen (Turnstile)</li>
<li><strong>Google</strong> – Abrechnung über Google Play, Google-Anmeldung</li>
<li><strong>Apple</strong> – Abrechnung über den App Store, Mit Apple anmelden (iPhone, iPad)</li>
<li><strong>Kakao</strong> – Kakao-Anmeldung</li>
</ul>
<p>Soweit diese Anbieter Daten außerhalb der EU verarbeiten (z. B. in den USA), geschieht dies auf Grundlage der EU-Standardvertragsklauseln oder des EU-US Data Privacy Framework.</p>"""),
   ("welegato-Banner und externe Links", f"""<p>Die App zeigt einen Link zu welegato (einer Musikplattform desselben Unternehmens, welegato.com), in den Einstellungen gibt es Links zu den Store-Seiten anderer Vicino-Labs-Apps. Das sind unsere eigenen Links, kein Werbenetzwerk und kein Tracking-Tool.</p>
<p>Links öffnen sich im Browser oder Store <strong>nur, wenn du sie antippst</strong>. Der welegato-Link trägt nur den Hinweis, dass du aus Squillo kommst (utm-Werte wie <code>utm_source=squillo</code>), aber nichts, was dich identifiziert. Danach gilt die Erklärung der jeweiligen Seite: <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von welegato</a>.</p>"""),
   ("Geräteberechtigungen", """<p>Unter Android nutzt die App nur Berechtigungen für die Wiedergabe (WAKE_LOCK und einen Vordergrunddienst für Medienwiedergabe), damit der Übungsklang bei ausgeschaltetem Bildschirm weiterläuft. Mikrofon, Kamera, Fotos, Standort, Kontakte und Benachrichtigungen werden nicht angefragt.</p>"""),
   ("Was wir nicht erheben", """<p>Ohne Anmeldung erhalten wir keine Kontodaten wie Name oder E-Mail. Die App nutzt weder deinen Gesang noch Übungsverlauf, Standort, Kontakte oder Werbe-IDs und enthält kein Analyse-SDK und kein Werbenetzwerk.</p>"""),
   ("Kinder", """<p>Die Grundfunktionen haben keine Altersgrenze. Anmeldung mit welegato-ID und Abo sind ab 16 Jahren möglich. Kinder sollten externe Links gemeinsam mit einem Elternteil nutzen.</p>"""),
   ("Deine Rechte", f"""<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch (Art. 15 bis 21 DSGVO)</li>
<li>Beschwerderecht bei einer Aufsichtsbehörde, z. B. der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW) oder der Behörde an deinem Wohnort</li>
</ul>
<p>ID und Backups kannst du selbst in der App löschen. Für alles andere schreib an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich Gesetze oder Funktionen der App ändern, und veröffentlichen Änderungen mit Gültigkeitsdatum auf dieser Seite.</p>"""),
   ("Kontakt", "<p>Fragen zum Datenschutz richte bitte an:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Squillo Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "01.12.2026 (previsto)"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": _draft("it") + "Squillo, creata da Vicino Labs, è un'app di vocalizzi e studio per cantanti. I vocalizzi di base e gli studi gratuiti funzionano senza account; impostazioni e spartiti di “I miei brani” restano sul tuo dispositivo. Solo l'accesso facoltativo (ID welegato), la prova e l'abbonamento, il backup Pro e la ricerca di spartiti gratuiti passano dal nostro server (UE) e dai servizi indicati sotto. Ecco esattamente quali dati tratta l'app.",
  "footer": "Questa informativa entra in vigore dal giorno in cui il gestore la conferma (versione 1.0, bozza).",
  "other": "Termini di servizio →",
  "sections": [
   ("Titolare del trattamento", _op_ref("it", LAST) + "<p>Vicino Labs è titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per i dati personali trattati in relazione a questa app.</p>"),
   ("In breve", """<div class="summary-box"><ul>
<li>I vocalizzi di base e gli studi gratuiti funzionano <strong>senza accesso</strong>. Impostazioni e spartiti di “I miei brani” sono salvati <strong>sul tuo dispositivo</strong>.</li>
<li>L'app <strong>non usa microfono, fotocamera, foto, posizione né contatti.</strong> Non registra il tuo canto e non invia la cronologia dello studio a un server.</li>
<li>L'accesso con un <strong>ID welegato</strong> è facoltativo. Serve per l'abbonamento Pro e il backup Pro (non per la prova di 3 giorni dopo l'installazione). I dati dell'account sono trattati secondo l'informativa di welegato.</li>
<li>Con il <strong>backup Pro</strong> gli spartiti di “I miei brani” vengono salvati nel cloud (Cloudflare R2) per i dispositivi con lo stesso ID.</li>
<li>Non ci sono reti pubblicitarie né strumenti di analisi o tracciamento. Il link a welegato nell'app è un nostro banner per un servizio della stessa azienda.</li>
</ul></div>"""),
   ("Dati salvati sul dispositivo", """<ul>
<li>Impostazioni dell'app (registro vocale, diapason, tempo, suono del pianoforte, tema, lingua ecc.) e preferiti</li>
<li>Spartiti importati in “I miei brani” (MusicXML)</li>
<li>File audio del pianoforte che l'app genera sul dispositivo per la riproduzione</li>
<li>Se hai effettuato l'accesso, il token che mantiene l'accesso e le ultime informazioni sul piano ricevute</li>
</ul>
<p>Questi dati restano nella memoria dell'app sul dispositivo e non ci vengono inviati, tranne con il backup Pro (sotto). Vengono rimossi quando elimini l'app. Su Android, se il backup Google del dispositivo è attivo, i dati dell'app possono essere salvati nel tuo account Google; quel backup è gestito da Google e noi non lo vediamo. Base giuridica: fornitura dell'app (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Ricerca di spartiti gratuiti", """<p>Quando cerchi spartiti gratuiti in “I miei brani”, l'app scarica il nostro elenco pubblico e i file degli spartiti da Cloudflare R2. L'app non carica nulla e non serve l'accesso. Come in ogni connessione a internet, Cloudflare tratta brevemente l'indirizzo IP del dispositivo.</p>"""),
   ("ID welegato (facoltativo)", f"""<p>Anche senza accesso puoi continuare a usare i vocalizzi di base e gli studi gratuiti. Se accedi, usi un account di welegato, un servizio della stessa azienda (ID welegato).</p>
<ul>
<li>I <strong>dati dell'account</strong> (email, nome, metodo di accesso Apple, Google, Kakao o email, numero di account) sono trattati secondo l'<a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">informativa sulla privacy di welegato</a>. Se ti registri in Squillo, l'account riporta “registrato in Squillo”.</li>
<li>Per la registrazione e l'accesso via email, Cloudflare Turnstile controlla alcune informazioni del browser per bloccare le registrazioni automatiche (<a href="{CF_PRIVACY}" target="_blank" rel="noopener">informativa di Cloudflare</a>). All'accesso con Apple, Google o Kakao si applica l'informativa di ciascuna azienda.</li>
<li>Se su iPhone o iPad scegli “Continua con Apple”, riceviamo il nome e l'email confermati da Apple. Se scegli “Nascondi la mia email”, riceviamo solo l'indirizzo di inoltro di Apple.</li>
<li><strong>Eliminare l'ID:</strong> in qualsiasi momento da Impostazioni › Il mio ID › Gestisci ID › Elimina ID. L'account welegato viene eliminato, per tutte le app di Vicino Labs. Vengono eliminati anche i file del backup Pro di Squillo (per i dati di pagamento da conservare per legge vedi sotto). Impostazioni e spartiti sul dispositivo restano.</li>
</ul>
<p>Secondo i termini di welegato l'accesso è consentito dai 16 anni in su. Base giuridica: fornitura della funzione scelta (lett. b).</p>"""),
   ("Prova gratuita e abbonamento", f"""<ul>
<li><strong>Prova gratuita di 3 giorni:</strong> alla prima installazione tutte le funzioni sono aperte per 3 giorni, senza accesso. Perché la prova non si ripeta reinstallando l'app, usiamo un identificativo del dispositivo (ANDROID_ID su Android, un numero casuale salvato nel Portachiavi su iPhone e iPad). Il nostro server non salva l'identificativo ma solo un hash SHA-256 non reversibile (“squillo:” + identificativo) con l'ora del primo e dell'ultimo controllo. Non servono nome né email. Conservazione: eliminato un anno dopo l'ultimo controllo. Il numero nel Portachiavi di iPhone e iPad può restare anche dopo l'eliminazione dell'app.</li>
<li><strong>Abbonamento:</strong> Pro si acquista tramite Google Play o App Store. Pagamento e dati della carta sono gestiti dallo store e non li riceviamo. Per verificare che l'abbonamento sia valido salviamo numero di account, nome del prodotto, stato, scadenza e la conferma d'acquisto dello store.</li>
<li><strong>Conservazione:</strong> i dati legati ai pagamenti sono conservati per il periodo richiesto dalla legge fiscale (fino a 10 anni).</li>
</ul>
<p>Al trattamento da parte degli store si applicano l'<a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">informativa sulla privacy di Google</a> o l'<a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">informativa sulla privacy di Apple</a>. Base giuridica: esecuzione del contratto (lett. b), obbligo legale (lett. c), prevenzione degli abusi della prova (lett. f).</p>"""),
   ("Backup Pro (facoltativo)", """<p>Se un utente Pro (anche durante la prova) usa il backup con l'accesso effettuato, gli spartiti di “I miei brani” restano uguali su tutti i dispositivi con lo stesso ID. Lo spazio è di 1 GB per ID.</p>
<ul>
<li><strong>Cosa salviamo:</strong> i file degli spartiti di “I miei brani” (MusicXML) con nome, dimensione, impronta (SHA-256) e ora dell'ultima modifica.</li>
<li><strong>Dove:</strong> i file su Cloudflare R2 (Cloudflare, Inc., responsabile del trattamento), l'elenco e lo spazio usato sul nostro server (Supabase, UE, Francoforte). Il trasferimento è cifrato e i file passano solo tramite indirizzi firmati di breve durata tra l'app e quell'ID. Non apriamo i tuoi spartiti.</li>
<li><strong>Eliminazione e conservazione:</strong> se elimini un file di backup nell'app o elimini l'ID, viene eliminato anche dal cloud. Alla fine di Pro conserviamo il backup per 90 giorni e lo eliminiamo se nel frattempo non ti abboni di nuovo.</li>
</ul>
<p>Base giuridica: fornitura della funzione scelta (lett. b).</p>"""),
   ("Responsabili del trattamento e trasferimenti fuori dall'UE", f"""<ul>
<li><strong>Supabase</strong>: server e database, accesso (ID welegato), data center nell'UE (Francoforte, Germania) (<a href="{SUPABASE_PRIVACY}" target="_blank" rel="noopener">informativa</a>)</li>
<li><strong>Cloudflare</strong>: archiviazione del backup Pro (R2), download degli spartiti gratuiti (R2), protezione dalle registrazioni email automatiche (Turnstile)</li>
<li><strong>Google</strong>: pagamenti Google Play, accesso con Google</li>
<li><strong>Apple</strong>: pagamenti App Store, Accedi con Apple (iPhone, iPad)</li>
<li><strong>Kakao</strong>: accesso con Kakao</li>
</ul>
<p>Se questi fornitori trattano dati fuori dall'UE (ad esempio negli USA), ciò avviene sulla base delle clausole contrattuali standard UE o del EU-US Data Privacy Framework.</p>"""),
   ("Banner welegato e link esterni", f"""<p>L'app mostra un link a welegato (piattaforma musicale della stessa azienda, welegato.com) e nelle impostazioni ci sono link alle pagine store di altre app di Vicino Labs. Sono nostri link, non una rete pubblicitaria né uno strumento di tracciamento.</p>
<p>I link si aprono nel browser o nello store <strong>solo quando li tocchi</strong>. Il link a welegato contiene solo l'indicazione che arrivi da Squillo (valori utm come <code>utm_source=squillo</code>) e nulla che ti identifichi. Una volta aperto, vale l'informativa di quel sito: <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">informativa sulla privacy di welegato</a>.</p>"""),
   ("Autorizzazioni del dispositivo", """<p>Su Android l'app usa solo autorizzazioni per la riproduzione (WAKE_LOCK e un servizio in primo piano per la riproduzione multimediale), così il suono dello studio continua anche a schermo spento. Non chiede microfono, fotocamera, foto, posizione, contatti né notifiche.</p>"""),
   ("Cosa non raccogliamo", """<p>Senza accesso non riceviamo dati dell'account come nome o email. L'app non usa il tuo canto, la cronologia dello studio, la posizione, i contatti né identificatori pubblicitari, e non contiene SDK di analisi né reti pubblicitarie.</p>"""),
   ("Minori", """<p>Le funzioni di base non hanno limiti di età. L'accesso con ID welegato e l'abbonamento sono consentiti dai 16 anni in su. I bambini dovrebbero usare i link esterni insieme a un genitore.</p>"""),
   ("I tuoi diritti", f"""<ul>
<li>Accesso, rettifica, cancellazione, limitazione, portabilità dei dati e opposizione (artt. 15-21 GDPR)</li>
<li>Diritto di reclamo a un'autorità di controllo, ad esempio l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o quella del tuo luogo di residenza</li>
</ul>
<p>Puoi eliminare ID e backup direttamente nell'app. Per tutto il resto scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Modifiche", """<p>Possiamo aggiornare questa informativa se cambiano le leggi o le funzioni dell'app, e pubblicheremo le modifiche con la data di entrata in vigore su questa pagina.</p>"""),
   ("Contatti", "<p>Per domande sulla protezione dei dati scrivici:</p>" + _id_card("it")),
  ],
 },
}
