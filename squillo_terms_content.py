"""스퀼로(Squillo) 이용약관 본문 (ko/en/de/it) — squillo_legal.py가 HTML로 만든다.

2026-11-26 버전 1.0 초안 (운영자 승인 전). chiave_terms_content.py의 틀(구독·책임)과
pianino_terms_content.py의 음원 라이선스 조항을 따랐다.
요금제(대표님 확정 2026-11-26): 무료 = 기본 발성 8곡 + 곡집마다 앞 2곡, Pro = 연습곡 전부 +
나의 연습 + 백업 1GB, 처음 설치 뒤 3일 체험(로그인 없이, 대표님 2026-11-26), 체험 뒤 자동 결제 없음. 월·연 구독.
가격은 약관에 적지 않음(스토어 결제 화면이 표시, 끼아베와 같은 결정).
저자 표시(CC BY 3.0): Salamander Grand Piano v3(Alexander Holm), 바카이 3–22번 MusicXML(Mark Probert, vaccai.info).
"""

from appoggio_privacy_content import _id_card
from chiave_privacy_content import _op_ref, _draft

LAST = 16

TERMS = {
 "ko": {
  "title": "스퀼로(Squillo) 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.12.01 (예정)"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": _draft("ko") + "본 약관은 Vicino Labs가 만든 발성 연습 앱 스퀼로(Squillo)를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 운영자가 확정한 날부터 시행됩니다 (버전 1.0 초안).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 스퀼로(Squillo, 이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _op_ref("ko", LAST)),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다. 구독은 스토어에서 해지할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li>기본 발성 연습 — 성부와 기준음에 맞춘 스케일·발성 연습과 피아노 반주</li>
<li>연습곡 — 콘코네, 파노프카, 바카이, 마르케시 등 저작권이 끝난 교재를 회사가 직접 입력한 악보와 반주</li>
<li>나의 연습 — 이용자가 가져온 MusicXML 악보와 무료 악보로 연습</li>
<li>위레가토 통합 아이디 로그인(선택), Pro 백업</li>
</ol>"""),
   ("요금제와 구독", """<ol>
<li><strong>무료:</strong> 기본 발성 연습 전부와, 연습곡 곡집마다 앞 2곡을 로그인 없이 무료로 쓸 수 있습니다.</li>
<li><strong>Pro:</strong> 연습곡 전부, 「나의 연습」, Pro 백업(아이디당 1GB)이 열립니다.</li>
<li><strong>3일 무료 체험:</strong> 앱을 처음 설치하면 로그인 없이 3일 동안 모든 기능을 무료로 쓸 수 있습니다. 체험이 끝나도 자동으로 결제되지 않고 무료 범위로 돌아갑니다. Pro를 계속 쓰려면 위레가토 통합 아이디로 가입하거나 로그인한 뒤 구독합니다.</li>
<li>Pro는 <strong>월간 또는 연간 정기 구독</strong>으로, Google Play 또는 App Store가 스토어에 표시된 가격으로 청구합니다. 해지할 때까지 같은 기간으로 자동 갱신되며, 스토어의 구독 관리에서 언제든 해지할 수 있습니다. 해지해도 이미 결제한 기간이 끝날 때까지 쓸 수 있고, 그 뒤에는 무료 범위로 돌아갑니다.</li>
<li>가격은 구매 전에 스토어 결제 화면에 표시되며, 나라마다 다를 수 있습니다. 결제·환불은 각 스토어의 정책과 절차에 따릅니다. 디지털 콘텐츠의 특성상, 구매 즉시 이용이 시작되는 데 동의하면 법이 허용하는 범위에서 청약철회권이 소멸할 수 있으며, 이 경우에도 스토어의 환불 절차는 이용할 수 있습니다.</li>
<li>다른 기기에서 산 구독은 같은 스토어 계정으로 앱의 “구매 복원”을 눌러 다시 열 수 있습니다.</li>
<li>요금제 조건을 바꿀 때는 미리 알리며, 이미 결제한 기간에는 적용하지 않습니다.</li>
</ol>"""),
   ("Pro 백업", """<ol>
<li>Pro 백업은 「나의 연습」 악보를 같은 아이디의 기기들에 맞추는 기능이며, 용량은 아이디당 1GB입니다.</li>
<li>Pro가 끝나면 백업을 90일 동안 보관하고, 그 안에 다시 구독하지 않으면 지웁니다. 아이디를 지우면 백업도 바로 지워집니다.</li>
<li>백업은 편의 기능입니다. 중요한 악보는 원본 파일을 따로 보관해 주세요.</li>
</ol>"""),
   ("악보와 저작권", """<ol>
<li>이용자가 「나의 연습」에 가져오거나 백업하는 악보에 대한 저작권 준수는 이용자의 책임입니다. 이용할 권리가 있는 악보만 가져와 주세요.</li>
<li>회사는 이용자의 악보를 열어 보거나 다른 사람과 공유하지 않습니다.</li>
</ol>"""),
   ("음원·악보 라이선스와 저자 표시", """<ol>
<li>기본 피아노 소리: <strong>Salamander Grand Piano v3</strong>, Alexander Holm, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>. 회사가 44.1kHz로 줄이고 음정·소리 길이를 다듬어 씁니다.</li>
<li>바카이 3–22번 악보: Mark Probert의 MusicXML(<a href="https://vaccai.info" target="_blank" rel="noopener">vaccai.info</a>, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>)을 바탕으로 회사가 조를 옮기고 원본 악보와 대조했습니다.</li>
<li>콘서트 피아노 소리 Splendid Grand(퍼블릭 도메인), 악보 글꼴 Bravura(SIL Open Font License), 합창 악기 소리(MuseScore General 일부, MIT 라이선스)를 씁니다.</li>
<li>콘코네·파노프카·바카이·마르케시의 교재는 저작권 보호 기간이 끝난 작품이며, 앱의 악보 데이터는 회사가 직접 입력한 것입니다.</li>
<li>각 라이선스의 자세한 내용은 앱의 설정에도 적혀 있으며, 그 음원과 악보에는 해당 라이선스가 적용됩니다.</li>
</ol>"""),
   ("목소리 건강", """<p>앱은 연습을 돕는 도구이며 의학적 조언이나 성악 선생님의 지도를 대신하지 않습니다. 목이 아프거나 쉬면 연습을 멈추고 쉬어 주세요. 이어폰·헤드폰을 쓸 때는 음량을 알맞게 낮춰 주세요.</p>"""),
   ("welegato 및 외부 서비스", """<p>앱에는 welegato, 다른 Vicino Labs 앱의 스토어 페이지, Google Play·App Store 등 외부 서비스로 가는 링크와 기능이 있습니다. 이 서비스들은 앱과 별개이며 각자의 이용약관과 개인정보처리방침이 적용됩니다. 위레가토 통합 아이디에는 위레가토 이용약관이 함께 적용됩니다.</p>"""),
   ("지적재산권", """<p>앱의 로고, “Squillo·스퀼로” 명칭, 디자인, 문구, 소스코드, 회사가 입력한 악보 데이터에 대한 권리는 회사에 있습니다(위 라이선스 음원·악보는 각 라이선스를 따릅니다). 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다.</p>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 결제·체험 제한을 우회하지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다. 유료 기능을 중단할 때는 이미 결제한 기간에 대해 법령과 스토어 절차에 따라 처리합니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 생명·신체·건강의 침해, 그리고 제조물책임법에 따른 경우에는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>경과실의 경우 회사는 계약상 본질적인 의무를 위반했을 때에만, 계약 체결 시 예견할 수 있었던 통상적인 손해에 한해 책임을 집니다.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Squillo Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-12-01 (planned)"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": _draft("en") + "These terms are the agreement between Vicino Labs and the people who use Squillo, our vocal warm-up and practice app. By installing and using the app you agree to them.",
  "footer": "These terms take effect on the date the operator confirms them (version 1.0, draft).",
  "other": "Privacy Policy →",
  "sections": [
   ("Scope", "<p>These terms govern the use of the mobile app Squillo (the “app”) provided by Vicino Labs (the “company”).</p>"),
   ("Provider", _op_ref("en", LAST)),
   ("Validity and changes", """<ol>
<li>These terms take effect when published in the app or in another way the company chooses.</li>
<li>The company may change the terms within the limits of the law and will announce the effective date and the reason in advance.</li>
<li>If you do not agree to changed terms, you may stop using and delete the app. Subscriptions can be cancelled in the store.</li>
</ol>"""),
   ("What the app offers", """<ol>
<li>Basic warm-ups: scales and vocal exercises set to your voice type and concert pitch, with piano accompaniment</li>
<li>Studies: public-domain method books such as Concone, Panofka, Vaccai and Marchesi, entered by the company, with accompaniment</li>
<li>My pieces: practise with MusicXML scores you import and with free scores</li>
<li>Optional sign-in with a welegato ID, Pro backup</li>
</ol>"""),
   ("Plans and subscriptions", """<ol>
<li><strong>Free:</strong> all basic warm-ups and the first 2 pieces of each study collection, without signing in.</li>
<li><strong>Pro:</strong> all studies, My pieces and Pro backup (1 GB per ID).</li>
<li><strong>3-day free trial:</strong> when you first install the app, all features are free for 3 days without signing in. When the trial ends nothing is charged and you return to the free plan. To keep Pro, sign up or sign in with a welegato ID and subscribe.</li>
<li>Pro is a <strong>monthly or yearly subscription</strong> charged by Google Play or the App Store at the price shown in the store. It renews automatically for the same period until cancelled, and you can cancel at any time in the store's subscription settings. After cancelling you keep Pro until the end of the period already paid, then return to the free plan.</li>
<li>Prices are shown in the store before purchase and may differ by country. Payments and refunds follow each store's policies. Because this is digital content, if you agree that use starts immediately, your right of withdrawal may expire to the extent the law allows; the store's refund process remains available.</li>
<li>A subscription bought on another device can be restored with “Restore purchases” in the app, using the same store account.</li>
<li>Changes to plan conditions will be announced in advance and do not apply to periods already paid.</li>
</ol>"""),
   ("Pro backup", """<ol>
<li>Pro backup keeps your My pieces scores the same on the devices signed in with the same ID; storage is 1 GB per ID.</li>
<li>After Pro ends the backup is kept for 90 days and deleted if you do not subscribe again in that time. Deleting your ID deletes the backup immediately.</li>
<li>Backup is a convenience. Please keep your own copy of important score files.</li>
</ol>"""),
   ("Scores and copyright", """<ol>
<li>You are responsible for respecting copyright in scores you import into My pieces or back up. Please import only scores you have the right to use.</li>
<li>The company does not open your scores or share them with anyone.</li>
</ol>"""),
   ("Sound and score licences and credits", """<ol>
<li>Default piano sound: <strong>Salamander Grand Piano v3</strong> by Alexander Holm, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>. The company converted it to 44.1 kHz and adjusted tuning and note lengths.</li>
<li>Vaccai Nos. 3 to 22: based on MusicXML by Mark Probert (<a href="https://vaccai.info" target="_blank" rel="noopener">vaccai.info</a>, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>), transposed and checked against the original edition by the company.</li>
<li>The app also uses the concert piano Splendid Grand (public domain), the music font Bravura (SIL Open Font License) and choir instrument sounds (part of MuseScore General, MIT licence).</li>
<li>The Concone, Panofka, Vaccai and Marchesi method books are in the public domain; the score data in the app was entered by the company.</li>
<li>Details of each licence are also listed in the app's settings, and those sounds and scores remain under their licences.</li>
</ol>"""),
   ("Voice care", """<p>The app is a practice aid and does not replace medical advice or a singing teacher. If your voice hurts or becomes hoarse, stop and rest. Keep the volume at a comfortable level when using earphones or headphones.</p>"""),
   ("welegato and external services", """<p>The app contains links and features for external services such as welegato, store pages of other Vicino Labs apps, Google Play and the App Store. These are separate from the app and have their own terms and privacy policies. The welegato ID is also subject to the welegato terms.</p>"""),
   ("Intellectual property", """<p>The rights to the app's logo, the name “Squillo”, its design, text, source code and the score data entered by the company belong to the company (the licensed sounds and scores above follow their licences). Without the company's prior written consent you may not copy, distribute, transmit, publish, reverse-engineer or create derivative works.</p>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the app or get around payment or trial limits.</li>
<li>Do not disrupt the normal operation of the app.</li>
<li>Follow the applicable laws and these terms.</li>
</ol>"""),
   ("Changes and discontinuation", """<p>The company may change or discontinue all or part of the app for operational or technical reasons and will give notice in advance unless it is urgent. If a paid feature is discontinued, periods already paid are handled according to the law and the store's procedures.</p>"""),
   ("Liability", """<ol>
<li>The company is liable without limitation as provided by law for intent and gross negligence, for injury to life, body or health, and under the Product Liability Act.</li>
<li>For slight negligence the company is liable only for breach of essential contractual obligations, and only for typical damage foreseeable when the contract was made.</li>
</ol>"""),
   ("Governing law and jurisdiction", """<p>These terms are governed by the law of the Federal Republic of Germany. Mandatory consumer protection rights in the country where a consumer lives (for example an EU member state) are not affected. Otherwise the courts at the company's seat (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For questions about these terms, please contact us.</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Squillo Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "01.12.2026 (geplant)"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": _draft("de") + "Diese Bedingungen sind die Vereinbarung zwischen Vicino Labs und allen, die Squillo nutzen, unsere App zum Einsingen und Üben. Mit Installation und Nutzung der App stimmst du ihnen zu.",
  "footer": "Diese Bedingungen gelten ab dem Tag, an dem der Betreiber sie bestätigt (Version 1.0, Entwurf).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Geltungsbereich", "<p>Diese Bedingungen regeln die Nutzung der mobilen App Squillo („App“) von Vicino Labs („Unternehmen“).</p>"),
   ("Anbieter", _op_ref("de", LAST)),
   ("Gültigkeit und Änderungen", """<ol>
<li>Diese Bedingungen gelten mit ihrer Veröffentlichung in der App oder auf eine andere vom Unternehmen gewählte Weise.</li>
<li>Das Unternehmen kann die Bedingungen im gesetzlichen Rahmen ändern und kündigt Gültigkeitsdatum und Grund vorher an.</li>
<li>Wenn du geänderten Bedingungen nicht zustimmst, kannst du die App nicht mehr nutzen und löschen. Abos kannst du im Store kündigen.</li>
</ol>"""),
   ("Leistungen der App", """<ol>
<li>Grundübungen: Tonleitern und Stimmübungen passend zu Stimmlage und Kammerton, mit Klavierbegleitung</li>
<li>Etüden: gemeinfreie Gesangsschulen wie Concone, Panofka, Vaccai und Marchesi, vom Unternehmen selbst erfasst, mit Begleitung</li>
<li>Meine Stücke: Üben mit importierten MusicXML-Noten und kostenlosen Noten</li>
<li>Freiwillige Anmeldung mit welegato-ID, Pro-Backup</li>
</ol>"""),
   ("Tarife und Abos", """<ol>
<li><strong>Kostenlos:</strong> alle Grundübungen und die ersten 2 Stücke jeder Etüdensammlung, ohne Anmeldung.</li>
<li><strong>Pro:</strong> alle Etüden, „Meine Stücke“ und das Pro-Backup (1 GB pro ID).</li>
<li><strong>3 Tage kostenlos testen:</strong> Nach der ersten Installation kannst du 3 Tage lang alle Funktionen ohne Anmeldung kostenlos nutzen. Danach wird nichts abgebucht, und du kehrst zum kostenlosen Tarif zurück. Für Pro registrierst du dich mit einer welegato-ID oder meldest dich an und schließt ein Abo ab.</li>
<li>Pro ist ein <strong>monatliches oder jährliches Abo</strong>, das Google Play oder der App Store zum im Store angezeigten Preis abrechnet. Es verlängert sich automatisch um denselben Zeitraum, bis du kündigst; kündigen kannst du jederzeit in der Aboverwaltung des Stores. Nach der Kündigung bleibt Pro bis zum Ende des bezahlten Zeitraums aktiv, danach gilt wieder der kostenlose Tarif.</li>
<li>Preise werden vor dem Kauf im Store angezeigt und können je nach Land abweichen. Zahlung und Erstattung richten sich nach den Regeln des jeweiligen Stores. Da es sich um digitale Inhalte handelt, kann dein Widerrufsrecht im gesetzlich zulässigen Umfang erlöschen, wenn du dem sofortigen Beginn der Nutzung zustimmst; das Erstattungsverfahren des Stores bleibt davon unberührt.</li>
<li>Ein auf einem anderen Gerät gekauftes Abo kannst du mit „Käufe wiederherstellen“ in der App mit demselben Store-Konto wieder freischalten.</li>
<li>Änderungen der Tarifbedingungen werden vorher angekündigt und gelten nicht für bereits bezahlte Zeiträume.</li>
</ol>"""),
   ("Pro-Backup", """<ol>
<li>Das Pro-Backup hält deine Noten unter „Meine Stücke“ auf allen Geräten mit derselben ID gleich; der Speicher beträgt 1 GB pro ID.</li>
<li>Nach Ende von Pro bewahren wir das Backup 90 Tage auf und löschen es, wenn du in dieser Zeit nicht erneut abonnierst. Löschst du deine ID, wird das Backup sofort gelöscht.</li>
<li>Das Backup ist eine Komfortfunktion. Bitte bewahre wichtige Notendateien zusätzlich selbst auf.</li>
</ol>"""),
   ("Noten und Urheberrecht", """<ol>
<li>Für die Einhaltung des Urheberrechts an Noten, die du unter „Meine Stücke“ importierst oder sicherst, bist du selbst verantwortlich. Importiere bitte nur Noten, die du nutzen darfst.</li>
<li>Das Unternehmen öffnet deine Noten nicht und gibt sie an niemanden weiter.</li>
</ol>"""),
   ("Lizenzen und Urhebernennung für Klänge und Noten", """<ol>
<li>Standard-Klavierklang: <strong>Salamander Grand Piano v3</strong> von Alexander Holm, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>. Das Unternehmen hat ihn auf 44,1 kHz umgerechnet und Stimmung und Tonlängen angepasst.</li>
<li>Vaccai Nr. 3 bis 22: auf Grundlage der MusicXML-Dateien von Mark Probert (<a href="https://vaccai.info" target="_blank" rel="noopener">vaccai.info</a>, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>), vom Unternehmen transponiert und mit der Originalausgabe abgeglichen.</li>
<li>Außerdem verwendet die App den Konzertflügel Splendid Grand (gemeinfrei), die Notenschrift Bravura (SIL Open Font License) und Chorinstrumentklänge (Teil von MuseScore General, MIT-Lizenz).</li>
<li>Die Gesangsschulen von Concone, Panofka, Vaccai und Marchesi sind gemeinfrei; die Notendaten in der App hat das Unternehmen selbst erfasst.</li>
<li>Einzelheiten zu jeder Lizenz stehen auch in den Einstellungen der App; diese Klänge und Noten unterliegen ihren jeweiligen Lizenzen.</li>
</ol>"""),
   ("Stimmgesundheit", """<p>Die App ist eine Übungshilfe und ersetzt weder ärztlichen Rat noch Gesangsunterricht. Wenn deine Stimme schmerzt oder heiser wird, hör auf und ruh dich aus. Stell die Lautstärke mit Kopfhörern angenehm leise ein.</p>"""),
   ("welegato und externe Dienste", """<p>Die App enthält Links und Funktionen zu externen Diensten wie welegato, Store-Seiten anderer Vicino-Labs-Apps, Google Play und dem App Store. Diese sind von der App getrennt und haben eigene Bedingungen und Datenschutzerklärungen. Für die welegato-ID gelten zusätzlich die welegato-Bedingungen.</p>"""),
   ("Geistiges Eigentum", """<p>Die Rechte an Logo, Name „Squillo“, Design, Texten, Quellcode und den vom Unternehmen erfassten Notendaten liegen beim Unternehmen (für die oben genannten lizenzierten Klänge und Noten gelten deren Lizenzen). Ohne vorherige schriftliche Zustimmung des Unternehmens darfst du nichts davon vervielfältigen, verbreiten, übertragen, veröffentlichen, zurückentwickeln oder bearbeiten.</p>"""),
   ("Deine Pflichten", """<ol>
<li>Die App nicht zurückentwickeln oder dekompilieren und Zahlungs- oder Testphasengrenzen nicht umgehen.</li>
<li>Den normalen Betrieb der App nicht stören.</li>
<li>Die geltenden Gesetze und diese Bedingungen einhalten.</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Das Unternehmen kann Funktionen der App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigt dies vorher an, außer in dringenden Fällen. Wird eine kostenpflichtige Funktion eingestellt, werden bereits bezahlte Zeiträume nach Gesetz und Store-Verfahren behandelt.</p>"""),
   ("Haftung", """<ol>
<li>Das Unternehmen haftet unbeschränkt nach den gesetzlichen Vorschriften bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit sowie nach dem Produkthaftungsgesetz.</li>
<li>Bei leichter Fahrlässigkeit haftet das Unternehmen nur bei Verletzung wesentlicher Vertragspflichten und nur für den bei Vertragsschluss vorhersehbaren, typischen Schaden.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt das Recht der Bundesrepublik Deutschland. Zwingende Verbraucherschutzvorschriften des Staates, in dem ein Verbraucher seinen gewöhnlichen Aufenthalt hat (z. B. ein EU-Mitgliedstaat), bleiben unberührt. Im Übrigen ist Gerichtsstand der Sitz des Unternehmens (Dortmund).</p>"""),
   ("Kontakt", "<p>Fragen zu diesen Bedingungen richte bitte an:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Squillo Termini di servizio",
  "h1": "Termini di servizio",
  "meta": [("In vigore dal", "01.12.2026 (previsto)"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": _draft("it") + "Questi termini sono l'accordo tra Vicino Labs e chi usa Squillo, la nostra app di vocalizzi e studio. Installando e usando l'app li accetti.",
  "footer": "Questi termini entrano in vigore dal giorno in cui il gestore li conferma (versione 1.0, bozza).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>Questi termini regolano l'uso dell'app mobile Squillo (l'“app”) fornita da Vicino Labs (l'“azienda”).</p>"),
   ("Fornitore", _op_ref("it", LAST)),
   ("Validità e modifiche", """<ol>
<li>Questi termini sono validi dalla pubblicazione nell'app o in altro modo scelto dall'azienda.</li>
<li>L'azienda può modificarli nei limiti di legge e annuncia in anticipo la data di entrata in vigore e il motivo.</li>
<li>Se non accetti i termini modificati puoi smettere di usare l'app ed eliminarla. Gli abbonamenti si disdicono nello store.</li>
</ol>"""),
   ("Cosa offre l'app", """<ol>
<li>Vocalizzi di base: scale ed esercizi adattati al registro vocale e al diapason, con accompagnamento al pianoforte</li>
<li>Studi: metodi di pubblico dominio come Concone, Panofka, Vaccai e Marchesi, trascritti dall'azienda, con accompagnamento</li>
<li>I miei brani: studio con spartiti MusicXML importati e spartiti gratuiti</li>
<li>Accesso facoltativo con ID welegato, backup Pro</li>
</ol>"""),
   ("Piani e abbonamenti", """<ol>
<li><strong>Gratis:</strong> tutti i vocalizzi di base e i primi 2 brani di ogni raccolta di studi, senza accesso.</li>
<li><strong>Pro:</strong> tutti gli studi, “I miei brani” e il backup Pro (1 GB per ID).</li>
<li><strong>Prova gratuita di 3 giorni:</strong> alla prima installazione puoi usare gratis tutte le funzioni per 3 giorni, senza accesso. Alla fine della prova non viene addebitato nulla e torni al piano gratuito. Per continuare con Pro registrati o accedi con un ID welegato e abbonati.</li>
<li>Pro è un <strong>abbonamento mensile o annuale</strong> addebitato da Google Play o App Store al prezzo indicato nello store. Si rinnova automaticamente per lo stesso periodo fino alla disdetta, che puoi fare in qualsiasi momento nella gestione abbonamenti dello store. Dopo la disdetta Pro resta attivo fino alla fine del periodo pagato, poi torni al piano gratuito.</li>
<li>I prezzi sono indicati nello store prima dell'acquisto e possono variare da paese a paese. Pagamenti e rimborsi seguono le regole di ciascuno store. Trattandosi di contenuti digitali, se accetti che l'uso inizi subito il diritto di recesso può estinguersi nei limiti di legge; la procedura di rimborso dello store resta disponibile.</li>
<li>Un abbonamento acquistato su un altro dispositivo si riattiva con “Ripristina acquisti” nell'app, usando lo stesso account dello store.</li>
<li>Le modifiche alle condizioni dei piani vengono annunciate in anticipo e non si applicano ai periodi già pagati.</li>
</ol>"""),
   ("Backup Pro", """<ol>
<li>Il backup Pro mantiene uguali gli spartiti di “I miei brani” sui dispositivi con lo stesso ID; lo spazio è di 1 GB per ID.</li>
<li>Alla fine di Pro conserviamo il backup per 90 giorni e lo eliminiamo se nel frattempo non ti abboni di nuovo. Se elimini l'ID, il backup viene eliminato subito.</li>
<li>Il backup è una comodità. Conserva anche una tua copia dei file importanti.</li>
</ol>"""),
   ("Spartiti e diritto d'autore", """<ol>
<li>Sei responsabile del rispetto del diritto d'autore sugli spartiti che importi in “I miei brani” o salvi nel backup. Importa solo spartiti che hai il diritto di usare.</li>
<li>L'azienda non apre i tuoi spartiti e non li condivide con nessuno.</li>
</ol>"""),
   ("Licenze e attribuzioni di suoni e spartiti", """<ol>
<li>Suono del pianoforte predefinito: <strong>Salamander Grand Piano v3</strong> di Alexander Holm, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>. L'azienda l'ha convertito a 44,1 kHz e ne ha regolato intonazione e durate.</li>
<li>Vaccai n. 3-22: basati sui file MusicXML di Mark Probert (<a href="https://vaccai.info" target="_blank" rel="noopener">vaccai.info</a>, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>), trasportati dall'azienda e confrontati con l'edizione originale.</li>
<li>L'app usa inoltre il pianoforte da concerto Splendid Grand (pubblico dominio), il font musicale Bravura (SIL Open Font License) e suoni di strumenti per il coro (parte di MuseScore General, licenza MIT).</li>
<li>I metodi di Concone, Panofka, Vaccai e Marchesi sono di pubblico dominio; i dati degli spartiti nell'app sono stati trascritti dall'azienda.</li>
<li>I dettagli di ogni licenza sono indicati anche nelle impostazioni dell'app; quei suoni e spartiti restano soggetti alle rispettive licenze.</li>
</ol>"""),
   ("Salute della voce", """<p>L'app è un aiuto allo studio e non sostituisce il parere medico né l'insegnante di canto. Se la voce fa male o diventa rauca, fermati e riposa. Con auricolari o cuffie tieni il volume a un livello confortevole.</p>"""),
   ("welegato e servizi esterni", """<p>L'app contiene link e funzioni verso servizi esterni come welegato, le pagine store di altre app di Vicino Labs, Google Play e App Store. Sono separati dall'app e hanno propri termini e informative. All'ID welegato si applicano anche i termini di welegato.</p>"""),
   ("Proprietà intellettuale", """<p>I diritti su logo, nome “Squillo”, design, testi, codice sorgente e dati degli spartiti trascritti dall'azienda appartengono all'azienda (i suoni e gli spartiti in licenza sopra indicati seguono le rispettive licenze). Senza il previo consenso scritto dell'azienda non puoi copiarli, distribuirli, trasmetterli, pubblicarli, decompilarli o crearne opere derivate.</p>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare né analizzare l'app e non aggirare i limiti di pagamento o della prova.</li>
<li>Non disturbare il normale funzionamento dell'app.</li>
<li>Rispettare le leggi applicabili e questi termini.</li>
</ol>"""),
   ("Modifica e sospensione", """<p>L'azienda può modificare o sospendere in tutto o in parte le funzioni dell'app per motivi operativi o tecnici e lo annuncia in anticipo, salvo urgenze. Se una funzione a pagamento viene sospesa, i periodi già pagati sono gestiti secondo la legge e le procedure dello store.</p>"""),
   ("Responsabilità", """<ol>
<li>L'azienda risponde senza limiti, secondo la legge, per dolo e colpa grave, per lesioni alla vita, al corpo o alla salute e ai sensi della legge sulla responsabilità per danno da prodotti.</li>
<li>Per colpa lieve l'azienda risponde solo per la violazione di obblighi contrattuali essenziali e solo per il danno tipico prevedibile al momento della conclusione del contratto.</li>
</ol>"""),
   ("Legge applicabile e foro", """<p>Si applica la legge della Repubblica Federale di Germania. Restano salvi i diritti inderogabili a tutela dei consumatori del paese di residenza abituale del consumatore (ad esempio uno Stato membro dell'UE). Negli altri casi è competente il foro della sede dell'azienda (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande su questi termini scrivici:</p>" + _id_card("it")),
  ],
 },
}
