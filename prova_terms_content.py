"""프로바(Prova) 이용약관 본문 (ko/en/de/it) — prova_legal.py가 HTML로 만든다.

2026-11-07 버전 1.0 초안 (앱 1.0). chiave/leggii_terms_content.py의 틀과 문구를 따랐다. 운영자 승인 전.
세 모드: 레슨(오디오·영상), 연습 테이크(같은 구간 여러 번 녹음·비교), 제출 영상(오디션·콩쿠르).
다른 사람을 동의 없이 녹음하는 책임은 이용자(독일 형법 §201). 녹음 중 방해 금지(안드로이드).
위레가토 통합 아이디와 함께 오는 기능: AI 분석(오디오만), 클라우드(Plus), 구독 — 아이디 로그인 필수.
가격은 약관에 적지 않음(스토어가 표시, Chiave와 같음). Leggii·Prova 함께 구독 할인은 "제안이 표시될 수 있음"으로만.
책임 제한은 Leggii·Chiave와 같은 독일법상 허용 범위.
"""

from appoggio_privacy_content import _id_card
from prova_privacy_content import _op_ref

WELEGATO_TERMS = "https://welegato.com/legal/terms/"
DELETE_ID = "https://welegato.com/konto-loeschen"

TERMS = {
 "ko": {
  "title": "프로바(Prova) 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.11.07"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 만든 레슨·연습 녹음 앱 프로바(Prova)를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 2026년 11월 7일부터 시행됩니다 (버전 1.0).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 프로바(Prova, 이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _op_ref("ko", 18)),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li><strong>레슨:</strong> 레슨을 오디오 또는 영상으로 남깁니다.</li>
<li><strong>연습 테이크:</strong> 같은 구간을 여러 번 녹음하고 테이크끼리 비교합니다.</li>
<li><strong>제출 영상:</strong> 오디션·콩쿠르용 영상을 찍고 점검합니다.</li>
<li>녹음과 영상은 이용자의 기기에만 저장되며, 계정 없이 쓸 수 있습니다. 녹음 중 방해 금지(안드로이드)와 영상의 정지 화면 보기를 제공합니다.</li>
<li><strong>위레가토 통합 아이디와 함께 제공되는 기능:</strong> AI 분석, 클라우드(Plus), 구독. 이 기능들은 위레가토 통합 아이디로 로그인해야 쓸 수 있습니다.</li>
<li>앱에는 광고가 없습니다.</li>
</ol>"""),
   ("녹음과 다른 사람의 동의", """<ol>
<li>앱의 녹음·녹화 기능은 이용자 본인의 레슨·연습 기록과 제출 영상 준비를 위한 것입니다.</li>
<li>다른 사람(선생님, 반주자, 함께 연주하는 사람 등)의 말·목소리·연주나 모습이 녹음·녹화되는 경우, 이용자는 시작 전에 그분들의 동의를 받아야 합니다. 미성년자가 함께 녹음되면 보호자의 동의도 필요합니다. 동의 없는 녹음은 법으로 금지될 수 있습니다(예: 독일 형법 제201조).</li>
<li>레슨 모드에서 앱이 동의 여부를 묻는 것은 안내일 뿐이며, 실제로 동의를 받는 것과 동의 없이 녹음하거나 녹음을 쓰는 데 따른 책임은 이용자에게 있습니다.</li>
<li>녹음이나 영상을 다른 사람에게 보내거나 공개·제출할 때는 녹음된 사람들의 동의와 연주된 작품의 저작권·실연자 권리를 이용자가 확인해야 합니다.</li>
</ol>"""),
   ("제출 영상", """<p>앱의 점검은 도움을 위한 것이며, 오디션·콩쿠르의 규정을 대신하지 않습니다. 영상 길이, 편집 금지, 형식 등 제출 조건은 각 주최 측의 최신 요강을 이용자가 직접 확인해야 하며, 영상이 받아들여지는지에 대해 회사는 책임지지 않습니다.</p>"""),
   ("녹음 중 방해 금지", """<ol>
<li>안드로이드에서 이용자가 허용하면, 앱은 테이크를 녹음하는 동안 방해 금지를 켜고 끝나면 이용자의 원래 설정으로 되돌립니다. 이 동안 전화, 메시지, 알림이 보류되어 놓칠 수 있습니다.</li>
<li>앱이 강제로 종료되거나 기기가 꺼지는 등의 경우 원래 설정으로 되돌리지 못할 수 있으니, 필요하면 기기 설정에서 확인해 주세요.</li>
<li>iPhone·iPad에서는 앱이 방해 금지를 바꿀 수 없으며 집중 모드를 켜도록 안내만 합니다. 비행기 모드는 앱이 권할 뿐 바꾸지 않습니다.</li>
</ol>"""),
   ("위레가토 통합 아이디", f"""<ol>
<li>녹음과 테이크 비교에는 로그인이 필요 없습니다. AI 분석, 클라우드, 구독은 위레가토 통합 아이디로 로그인해야 쓸 수 있습니다.</li>
<li>통합 아이디는 같은 회사가 운영하는 위레가토의 계정으로, 모든 Vicino Labs 앱에서 함께 씁니다. 아이디를 만들고 쓰는 데에는 <a href="{WELEGATO_TERMS}" target="_blank" rel="noopener">위레가토 이용약관</a>이 함께 적용되며, 만 16세 이상만 로그인할 수 있습니다.</li>
<li>앱의 아이디 관리 또는 <a href="{DELETE_ID}" target="_blank" rel="noopener">welegato.com/konto-loeschen</a>에서 아이디를 삭제할 수 있습니다. 삭제하면 이 아이디로 쓰던 모든 Vicino Labs 앱에서 함께 지워지며, 구독은 별도로 스토어에서 해지해야 결제가 멈춥니다.</li>
</ol>"""),
   ("구독과 AI 시간", """<ol>
<li>구독과 AI 시간은 Google Play 또는 App Store 인앱 결제로 삽니다. 구독하려면 먼저 위레가토 통합 아이디로 로그인해야 하며, 그래야 구독이 다른 Vicino Labs 앱과 안드로이드·iOS 사이에서 이어집니다.</li>
<li>구독은 해지할 때까지 같은 기간으로 자동 갱신되며, 스토어의 구독 관리에서 언제든 해지할 수 있습니다. 해지해도 이미 결제한 기간이 끝날 때까지 쓸 수 있습니다.</li>
<li><strong>AI 시간:</strong> AI 분석은 AI 시간(분)을 쓰며, 차감될 시간은 시작 전에 화면에 표시됩니다. AI 시간은 위레가토 통합 아이디별로 렛지 악보(Leggii)와 함께 씁니다. AI 시간은 현금으로 바꾸거나 다른 사람에게 넘길 수 없습니다.</li>
<li>렛지 악보와 프로바를 함께 구독하는 분 등에게 할인 같은 제안이 표시될 수 있으며, 그 조건은 제안이 표시될 때 안내합니다.</li>
<li>가격은 구매 전에 스토어 결제 화면에 표시되며, 나라마다 다를 수 있습니다. 결제·환불은 각 스토어의 정책과 절차에 따릅니다. 디지털 콘텐츠의 특성상, 구매 즉시 이용이 시작되는 데 동의하면 법이 허용하는 범위에서 청약철회권이 소멸할 수 있으며, 이 경우에도 스토어의 환불 절차는 이용할 수 있습니다.</li>
<li>구독에 포함된 AI 시간이나 클라우드 용량 등의 조건을 바꿀 때는 미리 알리며, 이미 결제한 기간과 이미 충전한 시간에는 적용하지 않습니다.</li>
</ol>"""),
   ("클라우드 (Plus)", """<ol>
<li>Plus를 구독하고 로그인하면 테이크의 오디오와 테이크 정보를 같은 아이디의 기기들에 맞춥니다. 영상은 이용자가 별표하거나 고른 테이크만 올립니다.</li>
<li>클라우드 용량은 아이디별로 렛지 클라우드와 함께 쓰며, 두 앱이 쓰는 양을 더해 계산합니다. 공간이 차면 새로 올리는 것만 멈추고 아무것도 지우지 않습니다.</li>
<li>한 기기에서 지운 테이크는 다른 기기와 클라우드에서도 지워집니다. Plus가 끝나면 새 업로드가 멈추고 90일 동안 내려받을 수 있으며, 두 번 메일로 알린 뒤 클라우드의 파일을 지웁니다.</li>
<li>클라우드는 이용자 본인의 기기들 사이의 동기화를 위한 것으로, 다른 사람과 공유하는 기능이 아닙니다.</li>
</ol>"""),
   ("AI 분석", """<ol>
<li>AI 분석의 결과는 AI가 만들며 <strong>틀리거나 빠진 내용이 있을 수 있습니다.</strong> 선생님의 지도나 심사를 대신하지 않으니 중요한 내용은 직접 확인해 주세요.</li>
<li>AI 분석은 소리만 분석하며, 영상의 화면은 분석하지 않습니다.</li>
<li>AI 분석은 이용자가 녹음 권리와 녹음된 사람들의 동의를 갖춘 녹음에만 써야 합니다.</li>
<li>회사는 남용을 막기 위해 이용을 제한할 수 있습니다.</li>
</ol>"""),
   ("외부 서비스", """<p>앱은 위레가토 통합 아이디, Google Play·App Store 등 외부 서비스와 함께 동작합니다. 이 서비스들은 앱과 별개이며 각자의 이용약관과 개인정보처리방침이 적용됩니다. 외부 서비스의 내용과 이용 가능 여부에 대해 회사는 책임지지 않습니다.</p>"""),
   ("지적재산권", """<p>앱의 로고, “Prova·프로바” 명칭, 디자인, 문구, 소스코드에 대한 권리는 회사에 있습니다. 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다. 이용자가 만든 녹음과 영상에 대한 권리는 이용자(와 녹음된 사람들)에게 있습니다.</p>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 결제·이용 제한을 우회하지 않습니다.</li>
<li>앱을 다른 사람의 동의 없는 녹음·촬영 등 법에 어긋나는 목적으로 쓰지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다. 외부 서비스(Google Gemini 등)나 기기 운영체제의 변경으로 관련 기능이 제한될 수 있습니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 생명·신체·건강의 침해, 그리고 제조물책임법에 따른 경우에는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>경과실의 경우 회사는 계약상 본질적인 의무를 위반했을 때에만, 계약 체결 시 예견할 수 있었던 통상적인 손해에 한해 책임을 집니다.</li>
<li>클라우드를 쓰지 않으면 녹음과 영상은 기기에만 저장됩니다. 회사는 이를 보관하지 않으며 잃어버린 테이크를 되살려 드릴 수 없습니다. 기기 분실·앱 삭제·초기화에 대비해 중요한 테이크는 따로 보관해 주세요.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Prova Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-11-07"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "These terms are the agreement between you and Vicino Labs for using Prova, an app for recording lessons and practice. By installing and using the app you agree to them.",
  "footer": "These terms are effective from 7 November 2026 (version 1.0).",
  "other": "Privacy Policy →",
  "sections": [
   ("Scope", "<p>These terms govern the use of the mobile app Prova (the “app”) provided by Vicino Labs (the “company”).</p>"),
   ("Provider", _op_ref("en", 18)),
   ("Validity and changes", """<ol>
<li>These terms take effect when published in the app or in another way chosen by the company.</li>
<li>The company may change them within the law and will announce the effective date and reason in advance.</li>
<li>If you do not agree to changed terms, you may stop using and delete the app.</li>
</ol>"""),
   ("What the app offers", """<ol>
<li><strong>Lesson:</strong> keep a lesson as audio or video.</li>
<li><strong>Practice takes:</strong> record a passage several times and compare the takes.</li>
<li><strong>Submission video:</strong> film and check videos for auditions and competitions.</li>
<li>Recordings and videos are stored only on your device, and the app works without an account. It offers Do Not Disturb while recording (Android) and silent stills from videos.</li>
<li><strong>Features that come with the welegato ID:</strong> AI analysis, the cloud (Plus) and subscriptions. They require signing in with a welegato ID.</li>
<li>The app contains no ads.</li>
</ol>"""),
   ("Recording and other people's consent", """<ol>
<li>The recording and filming features are for keeping your own lessons and practice and preparing submission videos.</li>
<li>If other people's words, voice, playing or image are recorded (a teacher, accompanist or fellow musicians, for example), you must get their consent before you start. If a minor is recorded, a parent's or guardian's consent is needed too. Recording without consent can be against the law (e.g. § 201 of the German Criminal Code).</li>
<li>The question the app asks in lesson mode is only a reminder. Actually obtaining consent, and recording or using a recording without consent, are your responsibility.</li>
<li>Before you send a recording or video to others, publish or submit it, you must make sure the people recorded agree and that copyright and performers' rights in the music allow it.</li>
</ol>"""),
   ("Submission videos", """<p>The app's checks are a help and do not replace the rules of an audition or competition. You must check the organiser's current requirements yourself (length, no edits, format and so on); the company is not responsible for whether a video is accepted.</p>"""),
   ("Do Not Disturb while recording", """<ol>
<li>On Android, if you allow it, the app switches Do Not Disturb on while a take is being recorded and restores your own setting afterwards. Calls, messages and notifications are held back during that time, so you may miss them.</li>
<li>If the app is force-closed or the device switches off, your setting may not be restored; check your device settings if needed.</li>
<li>On iPhone and iPad the app cannot change Do Not Disturb and only reminds you to turn on a Focus. The app only suggests airplane mode and never changes it.</li>
</ol>"""),
   ("welegato ID", f"""<ol>
<li>Recording and comparing takes need no sign-in. AI analysis, the cloud and subscriptions require signing in with a welegato ID.</li>
<li>The ID is an account of welegato, run by the same company, shared by all Vicino Labs apps. Creating and using it is also governed by the <a href="{WELEGATO_TERMS}" target="_blank" rel="noopener">welegato terms of use</a>; only people aged 16 or over can sign in.</li>
<li>You can delete the ID in the app or at <a href="{DELETE_ID}" target="_blank" rel="noopener">welegato.com/konto-loeschen</a>. It is then removed from all Vicino Labs apps; a subscription must be cancelled separately in the store to stop payments.</li>
</ol>"""),
   ("Subscriptions and AI time", """<ol>
<li>Subscriptions and AI time are bought as in-app purchases through Google Play or the App Store. To subscribe you must first sign in with a welegato ID, so the subscription works across Vicino Labs apps and between Android and iOS.</li>
<li>A subscription renews for the same period until cancelled; cancel any time in the store's subscription settings. It keeps working until the paid period ends.</li>
<li><strong>AI time:</strong> AI analysis uses AI time (minutes); the minutes it costs are shown before it starts. AI time is shared per welegato ID with Leggii. AI time has no cash value and cannot be transferred.</li>
<li>Offers, such as a discount for people who subscribe to both Leggii and Prova, may be shown; their conditions are explained when the offer is shown.</li>
<li>Prices are shown in the store before you buy and may differ by country. Payment and refunds follow each store's rules and process. For digital content, if you agree that use starts immediately, your right of withdrawal may end as far as the law allows; the store's refund process remains available.</li>
<li>Changes to the AI time or cloud space included in a subscription are announced in advance and do not apply to periods already paid or time already topped up.</li>
</ol>"""),
   ("Cloud (Plus)", """<ol>
<li>With Plus and signed in, the audio and details of your takes are kept the same on the devices of your ID. Video is uploaded only for takes you star or choose.</li>
<li>Cloud space is shared per ID with the Leggii cloud; what both apps use is added up. When the space is full, only new uploads stop; nothing is deleted.</li>
<li>A take deleted on one device is deleted on the other devices and in the cloud too. When Plus ends, new uploads stop and everything can be downloaded for 90 days; after two reminder emails the cloud files are deleted.</li>
<li>The cloud is for syncing between your own devices, not for sharing with others.</li>
</ol>"""),
   ("AI analysis", """<ol>
<li>AI analysis results are made by AI and <strong>can be wrong or incomplete.</strong> They do not replace your teacher's guidance or a jury's judgement; please check what matters.</li>
<li>AI analysis analyses only the sound, not the picture of a video.</li>
<li>Use AI analysis only for recordings you may make, with the consent of the people recorded.</li>
<li>We may limit use to prevent abuse.</li>
</ol>"""),
   ("External services", """<p>The app works with external services such as the welegato ID, Google Play and the App Store. They are separate from the app and governed by their own terms and privacy policies. The company is not responsible for their content or availability.</p>"""),
   ("Intellectual property", """<p>The company holds the rights to the app's logo, the name “Prova”, its design, texts and source code. You may not copy, distribute, transmit, publish, reverse-engineer or create derivative works without prior written consent. The rights in the recordings and videos you make stay with you (and the people recorded).</p>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the app or circumvent payment or usage limits.</li>
<li>Do not use the app for unlawful purposes, such as recording or filming people without their consent.</li>
<li>Do not disrupt the app's normal operation.</li>
<li>Comply with applicable law and these terms.</li>
</ol>"""),
   ("Changes and discontinuation", """<p>The company may change or discontinue all or part of the app for operational or technical reasons and will announce this in advance unless urgent. Changes to external services (such as Google Gemini) or to the device's operating system may limit related features.</p>"""),
   ("Liability", """<ol>
<li>The company is liable without limitation for intent and gross negligence, for injury to life, body or health, and under the Product Liability Act.</li>
<li>For slight negligence the company is liable only for breach of essential contractual obligations, limited to the typical damage foreseeable when the contract was made.</li>
<li>Without the cloud, recordings and videos are stored only on your device. The company does not keep them and cannot restore a lost take. To protect against loss of the device, deletion or reset, please keep important takes safe yourself.</li>
</ol>"""),
   ("Governing law and jurisdiction", """<p>German law applies. Mandatory consumer-protection rules of the country where you, as a consumer, habitually reside (e.g. an EU member state) remain unaffected. Otherwise the courts at the company's seat (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For questions about these terms, please contact us.</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Prova Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "07.11.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln die Nutzung von Prova, einer App von Vicino Labs zum Aufnehmen von Unterricht und Üben. Mit Installation und Nutzung der App stimmst du ihnen zu.",
  "footer": "Diese Bedingungen gelten ab dem 7. November 2026 (Version 1.0).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Geltungsbereich", "<p>Diese Bedingungen regeln die Nutzung der mobilen App Prova („App“) von Vicino Labs („Anbieter“).</p>"),
   ("Anbieter", _op_ref("de", 18)),
   ("Geltung und Änderungen", """<ol>
<li>Die Bedingungen gelten ab Veröffentlichung in der App oder auf andere vom Anbieter gewählte Weise.</li>
<li>Der Anbieter kann sie im Rahmen des Gesetzes ändern und kündigt Datum und Grund vorher an.</li>
<li>Wenn du geänderten Bedingungen nicht zustimmst, kannst du die App nicht mehr nutzen und löschen.</li>
</ol>"""),
   ("Leistungen", """<ol>
<li><strong>Unterricht:</strong> Unterricht als Ton oder Video festhalten.</li>
<li><strong>Übe-Takes:</strong> eine Stelle mehrmals aufnehmen und die Takes vergleichen.</li>
<li><strong>Bewerbungsvideo:</strong> Videos für Vorspiele und Wettbewerbe filmen und prüfen.</li>
<li>Aufnahmen und Videos werden nur auf deinem Gerät gespeichert; die App funktioniert ohne Konto. Sie bietet „Bitte nicht stören“ während der Aufnahme (Android) und stumme Standbilder aus Videos.</li>
<li><strong>Funktionen, die mit der welegato-ID kommen:</strong> KI-Analyse, Cloud (Plus) und Abos. Sie setzen die Anmeldung mit einer welegato-ID voraus.</li>
<li>Die App enthält keine Werbung.</li>
</ol>"""),
   ("Aufnahmen und Einwilligung anderer", """<ol>
<li>Die Aufnahme- und Filmfunktionen dienen dazu, deinen eigenen Unterricht und dein Üben festzuhalten und Bewerbungsvideos vorzubereiten.</li>
<li>Werden Wort, Stimme, Spiel oder Bild anderer Personen aufgenommen (z. B. Lehrkraft, Begleitung oder Mitmusiker), musst du vor Beginn ihre Einwilligung einholen. Werden Minderjährige aufgenommen, ist zusätzlich die Einwilligung der Eltern bzw. Sorgeberechtigten nötig. Aufnahmen ohne Einwilligung können strafbar sein (z. B. § 201 StGB).</li>
<li>Die Abfrage der App im Unterrichtsmodus ist nur ein Hinweis. Die Einwilligung tatsächlich einzuholen sowie Aufnahmen oder deren Nutzung ohne Einwilligung liegen in deiner Verantwortung.</li>
<li>Bevor du eine Aufnahme oder ein Video weitergibst, veröffentlichst oder einreichst, musst du sicherstellen, dass die aufgenommenen Personen einverstanden sind und Urheber- und Leistungsschutzrechte an der Musik dies erlauben.</li>
</ol>"""),
   ("Bewerbungsvideos", """<p>Die Prüfungen der App sind eine Hilfe und ersetzen nicht die Regeln eines Vorspiels oder Wettbewerbs. Die aktuellen Anforderungen des Veranstalters (Länge, keine Schnitte, Format usw.) prüfst du selbst; der Anbieter ist nicht dafür verantwortlich, ob ein Video angenommen wird.</p>"""),
   ("„Bitte nicht stören“ während der Aufnahme", """<ol>
<li>Unter Android schaltet die App, wenn du es erlaubst, „Bitte nicht stören“ ein, solange ein Take aufgenommen wird, und stellt danach deine eigene Einstellung wieder her. In dieser Zeit werden Anrufe, Nachrichten und Benachrichtigungen zurückgehalten; du kannst sie also verpassen.</li>
<li>Wird die App zwangsweise beendet oder schaltet sich das Gerät aus, wird deine Einstellung möglicherweise nicht wiederhergestellt; prüfe bei Bedarf die Geräteeinstellungen.</li>
<li>Auf iPhone und iPad kann die App „Nicht stören“ nicht ändern und erinnert nur daran, einen Fokus einzuschalten. Den Flugmodus empfiehlt die App nur; sie ändert ihn nie.</li>
</ol>"""),
   ("welegato-ID", f"""<ol>
<li>Aufnehmen und Takes vergleichen funktionieren ohne Anmeldung. KI-Analyse, Cloud und Abos setzen die Anmeldung mit einer welegato-ID voraus.</li>
<li>Die ID ist ein Konto von welegato, einem Dienst desselben Unternehmens, und gilt für alle Apps von Vicino Labs. Für Erstellung und Nutzung gelten zusätzlich die <a href="{WELEGATO_TERMS}" target="_blank" rel="noopener">Nutzungsbedingungen von welegato</a>; anmelden können sich nur Personen ab 16 Jahren.</li>
<li>Du kannst die ID in der App oder unter <a href="{DELETE_ID}" target="_blank" rel="noopener">welegato.com/konto-loeschen</a> löschen. Sie wird dann in allen Apps von Vicino Labs entfernt; ein Abo musst du zusätzlich im Store kündigen, damit die Zahlungen enden.</li>
</ol>"""),
   ("Abos und KI-Zeit", """<ol>
<li>Abos und KI-Zeit kaufst du als In-App-Kauf über Google Play oder den App Store. Für ein Abo musst du dich zuerst mit einer welegato-ID anmelden, damit es in den Apps von Vicino Labs und zwischen Android und iOS gilt.</li>
<li>Ein Abo verlängert sich um denselben Zeitraum, bis du kündigst; kündigen kannst du jederzeit in den Abo-Einstellungen des Stores. Es läuft bis zum Ende des bezahlten Zeitraums.</li>
<li><strong>KI-Zeit:</strong> Die KI-Analyse verbraucht KI-Zeit (Minuten); die Kosten werden vor dem Start angezeigt. Die KI-Zeit wird je welegato-ID mit Leggii geteilt. KI-Zeit hat keinen Geldwert und ist nicht übertragbar.</li>
<li>Es können Angebote angezeigt werden, etwa ein Rabatt für Personen, die Leggii und Prova abonnieren; die Bedingungen werden mit dem Angebot erklärt.</li>
<li>Preise werden vor dem Kauf im Store angezeigt und können je nach Land abweichen. Zahlung und Erstattung richten sich nach den Regeln und Abläufen des jeweiligen Stores. Bei digitalen Inhalten kann das Widerrufsrecht im gesetzlich zulässigen Umfang erlöschen, wenn du dem sofortigen Beginn zustimmst; das Erstattungsverfahren des Stores bleibt möglich.</li>
<li>Änderungen der in einem Abo enthaltenen KI-Zeit oder des Cloud-Speichers kündigen wir vorher an; sie gelten nicht für bereits bezahlte Zeiträume oder bereits aufgeladene Zeit.</li>
</ol>"""),
   ("Cloud (Plus)", """<ol>
<li>Mit Plus und Anmeldung werden Ton und Angaben deiner Takes auf den Geräten deiner ID gleich gehalten. Videos werden nur bei Takes hochgeladen, die du markierst oder auswählst.</li>
<li>Der Cloud-Speicher wird je ID mit der Leggii Cloud geteilt; was beide Apps belegen, wird zusammengerechnet. Ist der Speicher voll, stoppen nur neue Uploads; nichts wird gelöscht.</li>
<li>Ein auf einem Gerät gelöschter Take wird auch auf den anderen Geräten und in der Cloud gelöscht. Endet Plus, stoppen neue Uploads; 90 Tage lang kann alles heruntergeladen werden, nach zwei Erinnerungs-E-Mails werden die Cloud-Dateien gelöscht.</li>
<li>Die Cloud dient der Synchronisierung zwischen deinen eigenen Geräten, nicht dem Teilen mit anderen.</li>
</ol>"""),
   ("KI-Analyse", """<ol>
<li>Ergebnisse der KI-Analyse erstellt eine KI; sie <strong>können falsch oder unvollständig sein.</strong> Sie ersetzen weder die Anleitung deiner Lehrkraft noch das Urteil einer Jury; bitte prüfe Wichtiges selbst.</li>
<li>Die KI-Analyse wertet nur den Ton aus, nicht das Bild eines Videos.</li>
<li>Nutze die KI-Analyse nur für Aufnahmen, die du machen darfst, mit Einwilligung der aufgenommenen Personen.</li>
<li>Zum Schutz vor Missbrauch können wir die Nutzung begrenzen.</li>
</ol>"""),
   ("Externe Dienste", """<p>Die App arbeitet mit externen Diensten wie der welegato-ID, Google Play und dem App Store. Sie sind von der App getrennt; es gelten deren eigene Bedingungen und Datenschutzerklärungen. Für deren Inhalte und Verfügbarkeit ist der Anbieter nicht verantwortlich.</p>"""),
   ("Geistiges Eigentum", """<p>Die Rechte an Logo, dem Namen „Prova“, Gestaltung, Texten und Quellcode der App liegen beim Anbieter. Ohne vorherige schriftliche Zustimmung sind Vervielfältigung, Verbreitung, Übertragung, Veröffentlichung, Reverse Engineering und Bearbeitungen nicht erlaubt. Die Rechte an deinen Aufnahmen und Videos bleiben bei dir (und den aufgenommenen Personen).</p>"""),
   ("Pflichten der Nutzer", """<ol>
<li>Kein Reverse Engineering oder Dekompilieren der App und keine Umgehung der Bezahlung oder der Nutzungsgrenzen.</li>
<li>Keine Nutzung der App für rechtswidrige Zwecke, etwa Aufnahmen oder Filme von Personen ohne deren Einwilligung.</li>
<li>Keine Störung des normalen Betriebs der App.</li>
<li>Einhaltung der Gesetze und dieser Bedingungen.</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Der Anbieter kann Funktionen der App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigt dies, außer in dringenden Fällen, vorher an. Änderungen externer Dienste (z. B. Google Gemini) oder des Betriebssystems können zugehörige Funktionen einschränken.</p>"""),
   ("Haftung", """<ol>
<li>Der Anbieter haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit sowie nach dem Produkthaftungsgesetz.</li>
<li>Bei leichter Fahrlässigkeit haftet der Anbieter nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den bei Vertragsschluss vorhersehbaren, typischen Schaden.</li>
<li>Ohne Cloud werden Aufnahmen und Videos nur auf deinem Gerät gespeichert. Der Anbieter speichert sie nicht und kann verlorene Takes nicht wiederherstellen. Sichere wichtige Takes selbst gegen Verlust des Geräts, Löschung oder Zurücksetzen.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt deutsches Recht. Zwingende Verbraucherschutzvorschriften des Staates, in dem du als Verbraucher deinen gewöhnlichen Aufenthalt hast (z. B. ein EU-Mitgliedstaat), bleiben unberührt. Im Übrigen ist Gerichtsstand der Sitz des Anbieters (Dortmund).</p>"""),
   ("Kontakt", "<p>Fragen zu diesen Bedingungen richte bitte an:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Prova — Termini di utilizzo",
  "h1": "Termini di utilizzo",
  "meta": [("In vigore dal", "07.11.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Questi termini regolano l'uso di Prova, un'app di Vicino Labs per registrare lezioni e studio. Installando e usando l'app li accetti.",
  "footer": "Questi termini sono in vigore dal 7 novembre 2026 (versione 1.0).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>Questi termini regolano l'uso dell'app mobile Prova (“app”) fornita da Vicino Labs (“fornitore”).</p>"),
   ("Fornitore", _op_ref("it", 18)),
   ("Validità e modifiche", """<ol>
<li>I termini sono validi dalla pubblicazione nell'app o in altro modo scelto dal fornitore.</li>
<li>Il fornitore può modificarli nei limiti di legge, comunicando in anticipo data e motivo.</li>
<li>Se non accetti i termini modificati puoi smettere di usare l'app ed eliminarla.</li>
</ol>"""),
   ("Cosa offre l'app", """<ol>
<li><strong>Lezione:</strong> conserva una lezione in audio o in video.</li>
<li><strong>Take di studio:</strong> registra più volte un passaggio e confronta le take.</li>
<li><strong>Video per audizioni:</strong> filma e controlla video per audizioni e concorsi.</li>
<li>Registrazioni e video restano solo sul tuo dispositivo e l'app funziona senza account. Offre il «Non disturbare» durante la registrazione (Android) e fotogrammi muti dai video.</li>
<li><strong>Funzioni che arrivano con il welegato ID:</strong> analisi AI, cloud (Plus) e abbonamenti. Richiedono l'accesso con un welegato ID.</li>
<li>L'app non contiene pubblicità.</li>
</ol>"""),
   ("Registrazione e consenso degli altri", """<ol>
<li>Le funzioni di registrazione e ripresa servono a conservare le tue lezioni e il tuo studio e a preparare video per audizioni.</li>
<li>Se vengono registrate parole, voce, esecuzione o immagine di altre persone (ad es. insegnante, accompagnatore o colleghi), devi ottenere il loro consenso prima di iniziare. Se viene registrato un minore, serve anche il consenso di un genitore o tutore. Registrare senza consenso può essere vietato dalla legge (ad es. § 201 del codice penale tedesco).</li>
<li>La domanda posta dall'app nella modalità lezione è solo un promemoria. Ottenere davvero il consenso, e registrare o usare registrazioni senza consenso, sono tua responsabilità.</li>
<li>Prima di inviare una registrazione o un video ad altri, pubblicarli o presentarli, devi assicurarti che le persone registrate siano d'accordo e che il diritto d'autore e i diritti degli interpreti sulla musica lo consentano.</li>
</ol>"""),
   ("Video per audizioni", """<p>I controlli dell'app sono un aiuto e non sostituiscono il regolamento di un'audizione o di un concorso. Verifica tu i requisiti aggiornati dell'organizzatore (durata, divieto di montaggio, formato ecc.); il fornitore non risponde dell'accettazione di un video.</p>"""),
   ("«Non disturbare» durante la registrazione", """<ol>
<li>Su Android, se lo consenti, l'app attiva il «Non disturbare» mentre registri una take e poi ripristina la tua impostazione. In quel tempo chiamate, messaggi e notifiche vengono trattenuti, quindi potresti perderli.</li>
<li>Se l'app viene chiusa forzatamente o il dispositivo si spegne, la tua impostazione potrebbe non essere ripristinata; se serve, controlla le impostazioni del dispositivo.</li>
<li>Su iPhone e iPad l'app non può cambiare il «Non disturbare» e ti ricorda solo di attivare una modalità Full immersion. La modalità aereo l'app la suggerisce soltanto e non la cambia mai.</li>
</ol>"""),
   ("welegato ID", f"""<ol>
<li>Registrare e confrontare le take non richiede l'accesso. Analisi AI, cloud e abbonamenti richiedono l'accesso con un welegato ID.</li>
<li>L'ID è un account di welegato, servizio della stessa società, valido per tutte le app di Vicino Labs. Per crearlo e usarlo valgono anche i <a href="{WELEGATO_TERMS}" target="_blank" rel="noopener">termini di welegato</a>; possono accedere solo persone dai 16 anni in su.</li>
<li>Puoi eliminare l'ID nell'app o su <a href="{DELETE_ID}" target="_blank" rel="noopener">welegato.com/konto-loeschen</a>. Viene rimosso da tutte le app di Vicino Labs; un abbonamento va disdetto a parte nello store perché i pagamenti si fermino.</li>
</ol>"""),
   ("Abbonamenti e tempo AI", """<ol>
<li>Abbonamenti e tempo AI si acquistano in-app tramite Google Play o l'App Store. Per abbonarti devi prima accedere con un welegato ID, così l'abbonamento vale nelle app di Vicino Labs e tra Android e iOS.</li>
<li>Un abbonamento si rinnova per lo stesso periodo fino alla disdetta; puoi annullarlo in qualsiasi momento nelle impostazioni degli abbonamenti dello store. Resta attivo fino alla fine del periodo pagato.</li>
<li><strong>Tempo AI:</strong> l'analisi AI usa tempo AI (minuti); il costo è mostrato prima dell'avvio. Il tempo AI è condiviso per welegato ID con Leggii. Il tempo AI non ha valore in denaro e non è trasferibile.</li>
<li>Possono essere mostrate offerte, ad esempio uno sconto per chi si abbona sia a Leggii sia a Prova; le condizioni sono spiegate insieme all'offerta.</li>
<li>I prezzi sono indicati nello store prima dell’acquisto e possono variare da paese a paese. Pagamenti e rimborsi seguono le regole e le procedure di ciascuno store. Per i contenuti digitali, se accetti l'inizio immediato dell'uso, il diritto di recesso può estinguersi nei limiti di legge; la procedura di rimborso dello store resta disponibile.</li>
<li>Le modifiche al tempo AI o allo spazio cloud inclusi in un abbonamento vengono annunciate prima e non valgono per periodi già pagati o tempo già ricaricato.</li>
</ol>"""),
   ("Cloud (Plus)", """<ol>
<li>Con Plus e l'accesso, audio e dati delle take restano uguali sui dispositivi del tuo ID. Il video viene caricato solo per le take che contrassegni con la stella o scegli.</li>
<li>Lo spazio nel cloud è condiviso per ID con il cloud di Leggii; ciò che usano le due app viene sommato. Quando lo spazio è pieno si fermano solo i nuovi caricamenti; non viene cancellato nulla.</li>
<li>Una take eliminata su un dispositivo viene eliminata anche sugli altri dispositivi e nel cloud. Quando Plus termina, i nuovi caricamenti si fermano e per 90 giorni puoi scaricare tutto; dopo due email di promemoria i file nel cloud vengono cancellati.</li>
<li>Il cloud serve a sincronizzare i tuoi dispositivi, non a condividere con altri.</li>
</ol>"""),
   ("Analisi AI", """<ol>
<li>I risultati dell'analisi AI sono generati da un'AI e <strong>possono essere errati o incompleti.</strong> Non sostituiscono le indicazioni del tuo insegnante né il giudizio di una giuria; verifica ciò che è importante.</li>
<li>L'analisi AI analizza solo il suono, non l'immagine di un video.</li>
<li>Usa l'analisi AI solo per registrazioni che puoi fare, con il consenso delle persone registrate.</li>
<li>Possiamo limitarne l'uso per prevenire abusi.</li>
</ol>"""),
   ("Servizi esterni", """<p>L'app funziona con servizi esterni come il welegato ID, Google Play e l'App Store. Sono separati dall'app e regolati dai propri termini e informative. Il fornitore non risponde del loro contenuto o della loro disponibilità.</p>"""),
   ("Proprietà intellettuale", """<p>I diritti su logo, nome “Prova”, grafica, testi e codice sorgente dell'app appartengono al fornitore. Senza consenso scritto preventivo non è consentito copiare, distribuire, trasmettere, pubblicare, decompilare o creare opere derivate. I diritti sulle registrazioni e sui video che fai restano a te (e alle persone registrate).</p>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare o analizzare l'app né aggirare il pagamento o i limiti d'uso.</li>
<li>Non usare l'app per scopi illeciti, come registrare o filmare persone senza il loro consenso.</li>
<li>Non ostacolare il normale funzionamento dell'app.</li>
<li>Rispettare la legge e questi termini.</li>
</ol>"""),
   ("Modifica e sospensione", """<p>Il fornitore può modificare o sospendere in tutto o in parte le funzioni dell'app per motivi organizzativi o tecnici, avvisando prima salvo urgenza. Cambiamenti dei servizi esterni (come Google Gemini) o del sistema operativo possono limitare le funzioni collegate.</p>"""),
   ("Responsabilità", """<ol>
<li>Il fornitore risponde senza limiti per dolo e colpa grave, per danni alla vita, al corpo o alla salute e ai sensi della legge sulla responsabilità del produttore.</li>
<li>Per colpa lieve risponde solo in caso di violazione di obblighi contrattuali essenziali, nei limiti del danno tipico prevedibile alla conclusione del contratto.</li>
<li>Senza il cloud, registrazioni e video sono salvati solo sul dispositivo. Il fornitore non li conserva e non può recuperare take perse. Conserva tu quelle importanti, contro perdita del dispositivo, cancellazione o ripristino.</li>
</ol>"""),
   ("Legge applicabile e foro", """<p>Si applica la legge tedesca. Restano salve le norme imperative a tutela dei consumatori del paese in cui risiedi abitualmente (ad es. uno Stato UE). Per il resto è competente il foro della sede del fornitore (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande su questi termini scrivici:</p>" + _id_card("it")),
  ],
 },
}
