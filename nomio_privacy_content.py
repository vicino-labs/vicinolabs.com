"""Nomio 개인정보처리방침 본문 (ko/en/de) — nomio_legal.py가 HTML로 만든다.

2026-10-01 버전 4.0: vicinolabs.com으로 이전하면서 실제 앱 동작과 맞지 않던
부분을 고쳤다 (Google UMP 동의 창은 앱 1.6에서 실제로 추가, 시스템 알림 없음,
드라이브 백업 삭제 방법, 환율 API·PDF 글꼴에 IP 주소가 전달된다는 점, GDPR 제6조
처리 근거, 16세 기준, 연락처 contact@vicinolabs.com).
"""

EMAIL = "contact@vicinolabs.com"
DRIVE_APPS = "https://drive.google.com/drive/settings"
GOOGLE_PERMS = "https://myaccount.google.com/permissions"

PRIVACY = {
 "ko": {
  "title": "Nomio 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.10.01"), ("버전", "4.0"), ("운영자", "Vicino Labs")],
  "lede": "Vicino Labs가 만든 다통화 가계부 앱 Nomio는 여러분의 정보를 어떻게 다루는지 되도록 정확하게 알려드리려 합니다. 지출·수입 같은 금융 기록은 기기 밖으로 나가지 않으며, 저희는 서버를 운영하지 않습니다.",
  "footer": "본 방침은 2026년 10월 1일부터 시행됩니다 (버전 4.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", f"""<div class="id-card"><dt>상호</dt><dd>Vicino Labs (개인사업자, Einzelunternehmen)</dd><dt>대표자</dt><dd>Jeong-Hwan Lee</dd><dt>주소</dt><dd>Ruhrallee 41, 44139 Dortmund, Germany</dd><dt>이메일</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>Impressum</dt><dd><a href="/impressum/">vicinolabs.com/impressum</a></dd></div>
<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"""),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>회원가입·로그인 없이 쓸 수 있습니다. 지출·수입·계좌·예산·영수증 사진 등 금융 기록은 <strong>기기 안에만</strong> 저장되고, 저희는 이를 볼 수 없습니다.</li>
<li>무료 버전에는 <strong>Google AdMob</strong> 광고가 나옵니다. EU·EEA·영국·스위스에서는 광고를 불러오기 전에 Google의 동의 창으로 <strong>먼저 동의를 묻고</strong>, 설정 › 광고 개인정보 설정에서 언제든 바꿀 수 있습니다.</li>
<li>환율은 <strong>exchangerate-api.com</strong>에서 받아옵니다. 이때 기기의 IP 주소가 그 서비스에 전달됩니다.</li>
<li>구글드라이브 백업은 <strong>직접 실행할 때만</strong> 작동하며, 본인 드라이브의 Nomio 전용 숨김 폴더만 씁니다.</li>
<li>행동 분석·추적 도구(Firebase Analytics 등)는 쓰지 않습니다. 알림은 앱 안에서만 보이고 푸시 알림은 없습니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>지출·수입 내역(금액, 통화, 카테고리, 날짜, 메모, 영수증 사진), 계좌·자산·부채, 예산, 저축 목표, 반복 거래</li>
<li>앱 설정(언어, 기준 통화, 테마, 글자 크기, 앱 잠금 여부 등)과 마지막으로 받은 환율</li>
<li>프리미엄 구매 여부(“구매함” 표시만)</li>
</ul>
<p>이 정보는 기기의 앱 전용 저장소(SQLite 데이터베이스와 앱 폴더)에만 있습니다. Nomio에는 저희 서버가 없어서 저희가 이 정보를 보거나 받을 수 없습니다. 앱을 지우거나 설정의 초기화 기능을 쓰면 함께 지워집니다. 처리 근거: 앱 기능 제공(GDPR 제6조 1항 b).</p>"""),
   ("환율 조회", """<p>최신 환율을 보여주기 위해 앱이 <strong>exchangerate-api.com</strong>(ExchangeRate-API)에 기준 통화의 환율을 요청합니다. 요청에는 통화 코드만 들어가지만, 인터넷 통신의 특성상 기기의 <strong>IP 주소</strong>와 기본 접속 정보가 해당 서비스에 전달되며 그 서비스의 개인정보처리방침에 따라 처리됩니다. 받아온 환율은 기기에 저장해 두고 오프라인일 때 씁니다. 처리 근거: 정확한 환산이라는 정당한 이익(GDPR 제6조 1항 f).</p>"""),
   ("광고(Google AdMob)와 동의", """<p>무료 버전에서는 Google Ireland Limited(Gordon House, Barrow Street, Dublin 4, Ireland)의 <strong>Google AdMob</strong>으로 배너 광고를 보여줍니다. 이때 Google과 광고 파트너는 광고 식별자(Android 광고 ID / iOS의 IDFA — iOS는 앱 추적 투명성(ATT) 허용 시에만), IP 주소, 기기·앱 정보, 광고 노출·클릭 정보를 처리할 수 있습니다.</p>
<ul>
<li><strong>EU·EEA·영국·스위스:</strong> 광고를 불러오기 전에 Google의 인증된 동의 관리 도구(UMP, IAB TCF)로 동의 창을 보여줍니다. 맞춤형 광고와 기기 저장소 접근은 <strong>동의한 경우에만</strong> 이뤄집니다(GDPR 제6조 1항 a, 독일 TDDDG 제25조). 동의하지 않아도 앱은 그대로 쓸 수 있고, 이 경우 맞춤형이 아닌(제한된) 광고가 나올 수 있습니다.</li>
<li>선택은 앱의 <strong>설정 › 광고 개인정보 설정</strong>에서 언제든 바꾸거나 철회할 수 있습니다. 철회는 그 이전 처리의 적법성에 영향을 주지 않습니다.</li>
<li>Google은 이 정보를 미국으로 전송할 수 있으며, Google LLC는 EU-미국 데이터 프라이버시 프레임워크(DPF)에 인증되어 있습니다.</li>
<li>프리미엄을 구매하면 광고를 전혀 불러오지 않습니다.</li>
</ul>
<p>자세한 내용: <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">Google 파트너 사이트·앱의 데이터 사용</a>, <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google 개인정보처리방침</a>.</p>"""),
   ("인앱 결제(프리미엄)", """<p>프리미엄(광고 제거 및 추가 기능)은 Google Play 또는 Apple App Store의 일회성 인앱 결제로 구매합니다. 결제와 결제 정보는 전적으로 각 스토어가 처리하며, 저희는 카드 정보 등을 받지 않습니다. 앱은 스토어가 알려준 구매 확인 결과만 받아 기기에 “구매함”으로 저장합니다. 처리 근거: 계약 이행(GDPR 제6조 1항 b).</p>"""),
   ("구글드라이브 백업(선택)", f"""<p>설정에서 <strong>구글드라이브 백업·복원을 직접 실행할 때만</strong> 아래 처리가 일어납니다.</p>
<ul>
<li>Google 로그인으로 구글 계정(이메일 주소)을 확인합니다.</li>
<li>본인 구글 드라이브 안의 <strong>Nomio 전용 숨김 폴더</strong>(drive.appdata 권한)에 백업 파일(거래·계좌·카테고리·예산·반복 거래·설정)을 저장하고 읽습니다. 이 권한으로는 드라이브의 다른 파일, 메일, 연락처에 접근할 수 없습니다.</li>
<li>파일은 기기와 본인 구글 계정 사이에서만 오가며, 저희 서버를 거치지 않습니다.</li>
</ul>
<p><strong>백업 삭제:</strong> 웹의 <a href="{DRIVE_APPS}" target="_blank" rel="noopener">Google 드라이브 설정 › 앱 관리</a>에서 Nomio의 “숨겨진 앱 데이터 삭제”를 누르면 됩니다. 앱의 접근 권한은 <a href="{GOOGLE_PERMS}" target="_blank" rel="noopener">Google 계정 › 서드파티 연결</a>에서 해제할 수 있습니다. 처리 근거: 요청한 기능 제공(GDPR 제6조 1항 b).</p>"""),
   ("영수증 사진과 금액 인식", """<p>카메라와 사진은 영수증을 첨부할 때 <strong>직접 고른 경우에만</strong> 사용합니다. 고른 사진은 앱 폴더에 복사해 기기에만 저장하며 업로드하지 않습니다. 사진 속 금액 인식은 기기 안에서 이루어집니다(Android: Google ML Kit, iOS: Apple Vision). Google ML Kit는 서비스 개선을 위해 기기 종류, 앱 버전, 기능 사용 여부 같은 제한된 진단 정보를 Google에 보낼 수 있지만, 사진 내용은 보내지 않습니다.</p>"""),
   ("PDF 보고서", """<p>PDF 월간 보고서를 만들 때, 여러 언어 글자를 제대로 표시하기 위해 앱이 Google Fonts(fonts.gstatic.com)에서 글꼴 파일을 내려받습니다. 이때 기기의 IP 주소가 Google에 전달됩니다. 보고서 자체는 기기에서 만들어지고, 공유할지는 직접 정합니다. 처리 근거: 요청한 기능 제공(GDPR 제6조 1항 b·f).</p>"""),
   ("앱 잠금·알림·리뷰", """<p>앱 잠금을 켜면 기기의 생체 인증(지문, Face ID 등)이나 화면 잠금을 사용합니다. 생체 정보는 기기의 보안 영역에서만 처리되고 앱은 성공/실패 결과만 받습니다. 예산 초과·반복 거래 안내는 앱 안에서만 보이며 푸시 알림이나 외부 서버를 쓰지 않습니다. 앱 평가 요청 창은 Google Play/Apple이 직접 띄우고 처리합니다.</p>"""),
   ("받는 곳과 국외 이전", """<p>금융 기록은 누구에게도 전달하지 않습니다. 위에 설명한 경우에만 다음 서비스가 자체 정책에 따라 정보를 처리합니다: Google(광고, 인앱 결제, 드라이브 백업, ML Kit, Google Fonts), Apple(인앱 결제, iOS), ExchangeRate-API(환율). 미국 등 EU 밖으로의 전송은 EU-미국 데이터 프라이버시 프레임워크 또는 EU 표준계약조항을 근거로 이루어집니다.</p>"""),
   ("보유 기간과 삭제", """<p>기기의 정보는 직접 지울 때(설정의 초기화, 거래 삭제, 앱 삭제)까지 보관됩니다. 구글드라이브 백업 파일은 위 방법으로 지울 때까지 본인 드라이브에 남습니다. 광고 관련 정보는 Google의 보유 정책을 따릅니다.</p>"""),
   ("아동", """<p>Nomio는 아동을 대상으로 하지 않습니다. 맞춤형 광고에 대한 동의는 만 16세 이상만 할 수 있습니다(GDPR 제8조, 독일 기준). 16세 미만이라면 광고 동의 창에서 동의하지 마세요.</p>"""),
   ("정보주체의 권리", f"""<ul>
<li>열람, 정정, 삭제, 처리 제한, 데이터 이동, 이의 제기 권리(GDPR 제15~21조). 정당한 이익에 근거한 처리에는 언제든 이의를 제기할 수 있습니다.</li>
<li>동의를 언제든 철회할 권리 (광고: 설정 › 광고 개인정보 설정).</li>
<li>감독기관에 민원을 낼 권리 — 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 감독기관.</li>
</ul>
<p>대부분의 정보는 기기에만 있으므로 앱에서 바로 보고 고치고 지울 수 있습니다(설정 › 백업은 CSV/JSON 내보내기). 그 밖의 요청은 <a href="mailto:{EMAIL}">{EMAIL}</a>로 보내 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 이 방침을 고칠 수 있습니다. 바뀐 내용과 시행일은 이 페이지에 게시하고, 중요한 변경은 앱에서도 알려드립니다.</p>"""),
   ("문의", f"""<p>개인정보 처리에 관한 문의나 요청은 아래로 연락해 주세요.</p>
<div class="contact-card"><span class="role">Operator</span><span class="name">Vicino Labs</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>"""),
  ],
 },
 "en": {
  "title": "Nomio Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-10-01"), ("Version", "4.0"), ("Operator", "Vicino Labs")],
  "lede": "Nomio is a multi-currency budgeting app made by Vicino Labs. We'd rather be precise than vague about how your information is handled: your financial records never leave your device, and we don't run any server.",
  "footer": "This policy is effective as of October 1, 2026 (version 4.0).",
  "other": "View Terms of Service →",
  "sections": [
   ("Data controller", f"""<div class="id-card"><dt>Trading name</dt><dd>Vicino Labs (sole proprietorship, Einzelunternehmen)</dd><dt>Owner</dt><dd>Jeong-Hwan Lee</dd><dt>Address</dt><dd>Ruhrallee 41, 44139 Dortmund, Germany</dd><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>Legal notice</dt><dd><a href="/impressum/">vicinolabs.com/impressum</a></dd></div>
<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for personal data processed in connection with this app.</p>"""),
   ("Summary", """<div class="summary-box"><ul>
<li>No account or sign-in. Expenses, income, accounts, budgets and receipt photos are stored <strong>only on your device</strong> — we cannot see them.</li>
<li>The free version shows <strong>Google AdMob</strong> ads. In the EU/EEA, UK and Switzerland we <strong>ask for your consent first</strong> using Google's consent form, and you can change your choice anytime in Settings › Ad privacy settings.</li>
<li>Exchange rates come from <strong>exchangerate-api.com</strong>; your device's IP address is visible to that service.</li>
<li>Google Drive backup runs <strong>only when you start it</strong> and uses a hidden, Nomio-only folder in your own Drive.</li>
<li>No analytics or tracking SDKs (e.g. Firebase Analytics). Reminders appear inside the app only — there are no push notifications.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>Expense and income entries (amount, currency, category, date, note, receipt photo), accounts, assets/liabilities, budgets, savings goals, recurring transactions</li>
<li>App settings (language, base currency, theme, font size, app lock, etc.) and the most recently downloaded exchange rates</li>
<li>Whether you bought Premium (a “purchased” flag only)</li>
</ul>
<p>This information stays in the app's private storage on your device (an SQLite database and the app folder). Nomio has no server, so we can neither see nor receive it. It is deleted when you uninstall the app or use the reset options in Settings. Legal basis: providing the app's features (Art. 6(1)(b) GDPR).</p>"""),
   ("Exchange rates", """<p>To show current rates, the app requests rates for your base currency from <strong>exchangerate-api.com</strong> (ExchangeRate-API). The request contains only currency codes, but as with any internet request your device's <strong>IP address</strong> and basic connection data reach that service and are processed under its own privacy policy. Downloaded rates are stored on your device for offline use. Legal basis: our legitimate interest in accurate conversions (Art. 6(1)(f) GDPR).</p>"""),
   ("Advertising (Google AdMob) and consent", """<p>The free version shows banner ads through <strong>Google AdMob</strong>, provided by Google Ireland Limited (Gordon House, Barrow Street, Dublin 4, Ireland). Google and its ad partners may process your advertising ID (Android advertising ID; on iOS the IDFA, only if you allow App Tracking Transparency), IP address, device and app information, and ad impression/click data.</p>
<ul>
<li><strong>EU/EEA, UK and Switzerland:</strong> before any ads are loaded, the app shows a consent form from Google's certified consent management platform (UMP, IAB TCF). Personalized ads and access to device storage happen <strong>only with your consent</strong> (Art. 6(1)(a) GDPR, § 25 TDDDG). You can use the app fully without consenting; you may then see non-personalized (limited) ads.</li>
<li>You can change or withdraw your choice anytime in <strong>Settings › Ad privacy settings</strong>. Withdrawal does not affect processing carried out before it.</li>
<li>Google may transfer data to the USA; Google LLC is certified under the EU-U.S. Data Privacy Framework.</li>
<li>With Premium, no ads are requested at all.</li>
</ul>
<p>More: <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">How Google uses data from partner sites and apps</a>, <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Privacy Policy</a>.</p>"""),
   ("In-app purchase (Premium)", """<p>Premium (no ads plus extra features) is a one-time in-app purchase through Google Play or the Apple App Store. Payment and payment data are handled entirely by the store — we never receive card details. The app only receives the store's purchase confirmation and stores a “purchased” flag on your device. Legal basis: performance of a contract (Art. 6(1)(b) GDPR).</p>"""),
   ("Google Drive backup (optional)", f"""<p>The following happens <strong>only when you start a Google Drive backup or restore</strong> in Settings:</p>
<ul>
<li>Google Sign-In confirms your Google account (email address).</li>
<li>The app saves and reads a backup file (transactions, accounts, categories, budgets, recurring rules, settings) in a <strong>hidden, Nomio-only folder</strong> in your own Google Drive (the drive.appdata scope). This permission cannot access your other Drive files, email or contacts.</li>
<li>The file travels only between your device and your Google account — never through a server of ours.</li>
</ul>
<p><strong>Deleting the backup:</strong> open <a href="{DRIVE_APPS}" target="_blank" rel="noopener">Google Drive settings › Manage apps</a> on the web and choose “Delete hidden app data” for Nomio. You can revoke the app's access under <a href="{GOOGLE_PERMS}" target="_blank" rel="noopener">Google Account › Third-party connections</a>. Legal basis: providing a feature you requested (Art. 6(1)(b) GDPR).</p>"""),
   ("Receipt photos and amount recognition", """<p>The camera and photos are used <strong>only when you choose</strong> to attach a receipt. The photo is copied into the app folder and stays on your device; it is never uploaded. Reading the amount from the photo happens on your device (Android: Google ML Kit; iOS: Apple Vision). Google ML Kit may send Google limited diagnostic information (such as device model, app version and feature usage) to improve the service, but not the content of your photos.</p>"""),
   ("PDF reports", """<p>When you create a monthly PDF report, the app downloads font files from Google Fonts (fonts.gstatic.com) so that all languages render correctly; your device's IP address is transmitted to Google in the process. The report itself is generated on your device, and you decide whether to share it. Legal basis: providing a feature you requested (Art. 6(1)(b) and (f) GDPR).</p>"""),
   ("App lock, reminders and ratings", """<p>If you turn on app lock, the app uses your device's biometrics (fingerprint, Face ID, etc.) or screen lock. Biometric data is processed only in the device's secure hardware; the app receives just a pass/fail result. Budget and recurring-transaction reminders are shown inside the app only — no push notifications and no server. The rating prompt is shown and handled by Google Play/Apple.</p>"""),
   ("Recipients and international transfers", """<p>We don't pass your financial records to anyone. Only in the cases described above do the following services process data under their own policies: Google (ads, in-app purchase, Drive backup, ML Kit, Google Fonts), Apple (in-app purchase, iOS) and ExchangeRate-API (exchange rates). Transfers outside the EU (e.g. to the USA) rely on the EU-U.S. Data Privacy Framework or the EU Standard Contractual Clauses.</p>"""),
   ("Retention and deletion", """<p>Data on your device is kept until you delete it (reset options, deleting entries, uninstalling the app). A Google Drive backup stays in your Drive until you delete it as described above. Ad-related data follows Google's retention policies.</p>"""),
   ("Children", """<p>Nomio is not directed at children. Consent to personalized ads may only be given by people aged 16 or older (Art. 8 GDPR, as applied in Germany). If you are under 16, please do not consent in the ad consent form.</p>"""),
   ("Your rights", f"""<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR). You may object at any time to processing based on legitimate interests.</li>
<li>Withdraw consent at any time (ads: Settings › Ad privacy settings).</li>
<li>Lodge a complaint with a supervisory authority — e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live.</li>
</ul>
<p>Because most data lives only on your device, you can view, correct and delete it directly in the app (Settings › Backup exports CSV/JSON). For anything else, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law or the app's features change. Changes and the effective date are posted on this page; significant changes are also announced in the app.</p>"""),
   ("Contact", f"""<p>For questions or requests about data processing, please contact:</p>
<div class="contact-card"><span class="role">Operator</span><span class="name">Vicino Labs</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>"""),
  ],
 },
 "de": {
  "title": "Nomio Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Stand", "01.10.2026"), ("Version", "4.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Nomio ist eine Haushaltsbuch-App für mehrere Währungen von Vicino Labs. Wir möchten möglichst genau erklären, wie mit Ihren Daten umgegangen wird: Ihre Finanzdaten verlassen Ihr Gerät nicht, und wir betreiben keinen Server.",
  "footer": "Diese Erklärung gilt ab dem 1. Oktober 2026 (Version 4.0).",
  "other": "Zu den Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", f"""<div class="id-card"><dt>Firma</dt><dd>Vicino Labs (Einzelunternehmen)</dd><dt>Inhaber</dt><dd>Jeong-Hwan Lee</dd><dt>Anschrift</dt><dd>Ruhrallee 41, 44139 Dortmund, Deutschland</dd><dt>E-Mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>Impressum</dt><dd><a href="/impressum/">vicinolabs.com/impressum</a></dd></div>
<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für die Verarbeitung personenbezogener Daten im Zusammenhang mit dieser App.</p>"""),
   ("Zusammenfassung", """<div class="summary-box"><ul>
<li>Kein Konto, keine Anmeldung. Ausgaben, Einnahmen, Konten, Budgets und Belegfotos werden <strong>nur auf Ihrem Gerät</strong> gespeichert — wir können sie nicht einsehen.</li>
<li>Die kostenlose Version zeigt Werbung über <strong>Google AdMob</strong>. In der EU/im EWR, im Vereinigten Königreich und in der Schweiz <strong>fragen wir vorher nach Ihrer Einwilligung</strong> (Einwilligungsformular von Google); Sie können Ihre Wahl jederzeit unter Einstellungen › Datenschutz-Einstellungen für Werbung ändern.</li>
<li>Wechselkurse kommen von <strong>exchangerate-api.com</strong>; dabei ist die IP-Adresse Ihres Geräts für diesen Dienst sichtbar.</li>
<li>Das Google-Drive-Backup läuft <strong>nur, wenn Sie es selbst starten</strong>, und nutzt einen versteckten, nur für Nomio bestimmten Ordner in Ihrem eigenen Drive.</li>
<li>Keine Analyse- oder Tracking-Tools (z. B. Firebase Analytics). Hinweise erscheinen nur in der App — es gibt keine Push-Benachrichtigungen.</li>
</ul></div>"""),
   ("Auf Ihrem Gerät gespeicherte Daten", """<ul>
<li>Ausgaben und Einnahmen (Betrag, Währung, Kategorie, Datum, Notiz, Belegfoto), Konten, Vermögen/Verbindlichkeiten, Budgets, Sparziele, wiederkehrende Buchungen</li>
<li>App-Einstellungen (Sprache, Basiswährung, Design, Schriftgröße, App-Sperre usw.) und die zuletzt geladenen Wechselkurse</li>
<li>Ob Sie Premium gekauft haben (nur ein Merkmal „gekauft“)</li>
</ul>
<p>Diese Daten liegen im privaten Speicher der App auf Ihrem Gerät (SQLite-Datenbank und App-Ordner). Nomio hat keinen Server — wir können die Daten weder einsehen noch erhalten. Sie werden gelöscht, wenn Sie die App deinstallieren oder die Zurücksetzen-Funktionen in den Einstellungen nutzen. Rechtsgrundlage: Bereitstellung der App-Funktionen (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Wechselkurse", """<p>Um aktuelle Kurse anzuzeigen, ruft die App die Kurse Ihrer Basiswährung bei <strong>exchangerate-api.com</strong> (ExchangeRate-API) ab. Die Anfrage enthält nur Währungscodes; technisch bedingt werden dabei aber die <strong>IP-Adresse</strong> Ihres Geräts und grundlegende Verbindungsdaten an den Dienst übermittelt und nach dessen Datenschutzerklärung verarbeitet. Geladene Kurse werden für die Offline-Nutzung auf dem Gerät gespeichert. Rechtsgrundlage: berechtigtes Interesse an korrekten Umrechnungen (Art. 6 Abs. 1 lit. f DSGVO).</p>"""),
   ("Werbung (Google AdMob) und Einwilligung", """<p>Die kostenlose Version zeigt Bannerwerbung über <strong>Google AdMob</strong>, einen Dienst der Google Ireland Limited (Gordon House, Barrow Street, Dublin 4, Irland). Google und seine Werbepartner können dabei Ihre Werbe-ID (Android-Werbe-ID; unter iOS die IDFA, nur wenn Sie App-Tracking-Transparenz erlauben), IP-Adresse, Geräte- und App-Informationen sowie Daten zu Werbeeinblendungen und Klicks verarbeiten.</p>
<ul>
<li><strong>EU/EWR, Vereinigtes Königreich und Schweiz:</strong> Bevor Werbung geladen wird, zeigt die App ein Einwilligungsformular der zertifizierten Consent-Management-Plattform von Google (UMP, IAB TCF). Personalisierte Werbung und der Zugriff auf den Gerätespeicher erfolgen <strong>nur mit Ihrer Einwilligung</strong> (Art. 6 Abs. 1 lit. a DSGVO, § 25 TDDDG). Sie können die App ohne Einwilligung uneingeschränkt nutzen; dann kann nicht personalisierte (eingeschränkte) Werbung erscheinen.</li>
<li>Ihre Wahl können Sie jederzeit unter <strong>Einstellungen › Datenschutz-Einstellungen für Werbung</strong> ändern oder widerrufen. Der Widerruf berührt nicht die Rechtmäßigkeit der bis dahin erfolgten Verarbeitung.</li>
<li>Google kann Daten in die USA übermitteln; die Google LLC ist nach dem EU-US Data Privacy Framework zertifiziert.</li>
<li>Mit Premium wird keine Werbung mehr angefordert.</li>
</ul>
<p>Mehr dazu: <a href="https://policies.google.com/technologies/partner-sites?hl=de" target="_blank" rel="noopener">Datennutzung durch Google bei Partner-Websites und -Apps</a>, <a href="https://policies.google.com/privacy?hl=de" target="_blank" rel="noopener">Datenschutzerklärung von Google</a>.</p>"""),
   ("In-App-Kauf (Premium)", """<p>Premium (keine Werbung plus Zusatzfunktionen) ist ein einmaliger In-App-Kauf über Google Play oder den Apple App Store. Zahlung und Zahlungsdaten werden vollständig vom jeweiligen Store abgewickelt — wir erhalten keine Kartendaten. Die App erhält nur die Kaufbestätigung des Stores und speichert auf dem Gerät das Merkmal „gekauft“. Rechtsgrundlage: Vertragserfüllung (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Google-Drive-Backup (optional)", f"""<p>Nur wenn Sie in den Einstellungen <strong>selbst ein Google-Drive-Backup oder eine Wiederherstellung starten</strong>, geschieht Folgendes:</p>
<ul>
<li>Über die Google-Anmeldung wird Ihr Google-Konto (E-Mail-Adresse) bestätigt.</li>
<li>Die App speichert und liest eine Backup-Datei (Buchungen, Konten, Kategorien, Budgets, wiederkehrende Buchungen, Einstellungen) in einem <strong>versteckten, nur für Nomio bestimmten Ordner</strong> Ihres eigenen Google Drive (Berechtigung drive.appdata). Auf andere Dateien, E-Mails oder Kontakte besteht kein Zugriff.</li>
<li>Die Datei wird nur zwischen Ihrem Gerät und Ihrem Google-Konto übertragen — nie über einen Server von uns.</li>
</ul>
<p><strong>Backup löschen:</strong> Öffnen Sie im Browser <a href="{DRIVE_APPS}" target="_blank" rel="noopener">Google-Drive-Einstellungen › Apps verwalten</a> und wählen Sie bei Nomio „Ausgeblendete App-Daten löschen“. Den Zugriff der App können Sie unter <a href="{GOOGLE_PERMS}" target="_blank" rel="noopener">Google-Konto › Verbindungen zu Drittanbietern</a> entziehen. Rechtsgrundlage: Bereitstellung der von Ihnen angeforderten Funktion (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Belegfotos und Betragserkennung", """<p>Kamera und Fotos werden <strong>nur genutzt, wenn Sie selbst</strong> einen Beleg anhängen. Das Foto wird in den App-Ordner kopiert, bleibt auf Ihrem Gerät und wird nicht hochgeladen. Das Erkennen des Betrags erfolgt auf dem Gerät (Android: Google ML Kit, iOS: Apple Vision). Google ML Kit kann eingeschränkte Diagnosedaten (z. B. Gerätemodell, App-Version, Funktionsnutzung) zur Verbesserung des Dienstes an Google senden, jedoch nicht den Inhalt Ihrer Fotos.</p>"""),
   ("PDF-Berichte", """<p>Wenn Sie einen monatlichen PDF-Bericht erstellen, lädt die App Schriftdateien von Google Fonts (fonts.gstatic.com), damit alle Sprachen korrekt dargestellt werden; dabei wird die IP-Adresse Ihres Geräts an Google übermittelt. Der Bericht selbst wird auf Ihrem Gerät erstellt, und Sie entscheiden, ob Sie ihn teilen. Rechtsgrundlage: Bereitstellung der angeforderten Funktion (Art. 6 Abs. 1 lit. b und f DSGVO).</p>"""),
   ("App-Sperre, Hinweise und Bewertungen", """<p>Wenn Sie die App-Sperre aktivieren, nutzt die App die Biometrie (Fingerabdruck, Face ID usw.) oder die Bildschirmsperre Ihres Geräts. Biometrische Daten werden nur in der sicheren Hardware des Geräts verarbeitet; die App erhält lediglich das Ergebnis (erfolgreich/nicht erfolgreich). Hinweise zu Budgets und wiederkehrenden Buchungen erscheinen nur in der App — ohne Push-Benachrichtigungen und ohne Server. Die Bewertungsanfrage wird von Google Play/Apple angezeigt und verarbeitet.</p>"""),
   ("Empfänger und Drittlandübermittlung", """<p>Ihre Finanzdaten geben wir an niemanden weiter. Nur in den oben beschriebenen Fällen verarbeiten folgende Dienste Daten nach ihren eigenen Richtlinien: Google (Werbung, In-App-Kauf, Drive-Backup, ML Kit, Google Fonts), Apple (In-App-Kauf, iOS) und ExchangeRate-API (Wechselkurse). Übermittlungen in Länder außerhalb der EU (z. B. die USA) erfolgen auf Grundlage des EU-US Data Privacy Framework oder der EU-Standardvertragsklauseln.</p>"""),
   ("Speicherdauer und Löschung", """<p>Daten auf Ihrem Gerät bleiben gespeichert, bis Sie sie löschen (Zurücksetzen, Buchungen löschen, App deinstallieren). Ein Google-Drive-Backup bleibt in Ihrem Drive, bis Sie es wie oben beschrieben löschen. Werbebezogene Daten unterliegen den Speicherfristen von Google.</p>"""),
   ("Kinder", """<p>Nomio richtet sich nicht an Kinder. In personalisierte Werbung können nur Personen ab 16 Jahren einwilligen (Art. 8 DSGVO). Wenn Sie jünger als 16 sind, willigen Sie im Einwilligungsformular bitte nicht ein.</p>"""),
   ("Ihre Rechte", f"""<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO). Einer Verarbeitung auf Grundlage berechtigter Interessen können Sie jederzeit widersprechen.</li>
<li>Widerruf einer Einwilligung jederzeit (Werbung: Einstellungen › Datenschutz-Einstellungen für Werbung).</li>
<li>Beschwerde bei einer Aufsichtsbehörde — z. B. bei der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW) oder der Behörde an Ihrem Wohnort.</li>
</ul>
<p>Da die meisten Daten nur auf Ihrem Gerät liegen, können Sie sie direkt in der App einsehen, berichtigen und löschen (Einstellungen › Backup exportiert CSV/JSON). Für alles Weitere schreiben Sie an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Änderungen dieser Erklärung", """<p>Wir können diese Erklärung anpassen, wenn sich Rechtslage oder Funktionen der App ändern. Änderungen und Geltungsdatum veröffentlichen wir auf dieser Seite; wesentliche Änderungen kündigen wir zusätzlich in der App an.</p>"""),
   ("Kontakt", f"""<p>Bei Fragen oder Anliegen zur Datenverarbeitung wenden Sie sich bitte an:</p>
<div class="contact-card"><span class="role">Betreiber</span><span class="name">Vicino Labs</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>"""),
  ],
 },
}
