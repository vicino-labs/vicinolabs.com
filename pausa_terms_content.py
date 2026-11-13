"""파우사(Pausa) 이용약관 본문 (ko/en/de/it). pausa_legal.py가 HTML로 만든다.

2026-11-12 버전 1.0 초안 (앱 1.0). 운영자 승인 전 초안. 시행일은 "2026.11.13" 자리를 운영자가 채운다.
prova_terms_content.py의 틀과 문구를 따랐다. 책임 제한은 Prova·Leggii·Chiave와 같은 독일법상 허용 범위.
앱 1.0: 믹서(음악 + 빗소리·장작불·카페 소음·바람), 기기에서 만드는 바이노럴 비트, 취침 타이머(서서히 작아짐),
상황 프리셋, 믹스 저장, 백그라운드·오프라인 재생(모든 소리 앱 안에 포함). 계정 없음, 광고 없음.
결제: 연간 구독(7일 무료 체험)·월간 구독·한 번 결제 평생 이용권, App Store·Google Play만. 가격은 약관에 적지 않음.
의료 제품 아님(효과 주장 없음), 적당한 음량, 운전 중 금지. 음악·소리는 개인·비상업 청취만, 매장 공개 재생 등
영업용 이용은 포함 안 됨(영업용 이용권은 나중에 따로 생길 수 있으나 약관에는 아직 쓰지 않음).
나중에 위레가토 통합 아이디 로그인을 넣으면 이 약관(아이디 장)을 반드시 고쳐야 한다.
"""

from appoggio_privacy_content import _id_card
from prova_privacy_content import _op_ref

# Contact is the last section: keep N in step with the section list.
N = 14

TERMS = {
 "ko": {
  "title": "파우사(Pausa) 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.11.13"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 만든 사운드 앱 파우사(Pausa)를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 2026년 11월 13일부터 시행됩니다 (버전 1.0).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 파우사(Pausa, 이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _op_ref("ko", N)),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li><strong>믹스:</strong> 음악에 빗소리, 장작불, 카페 소음, 바람을 원하는 만큼 섞습니다.</li>
<li><strong>바이노럴 비트:</strong> 기기에서 바로 만드는 소리로, 왼쪽과 오른쪽 귀에 서로 다른 음을 들려줍니다. 헤드폰으로 들어야 합니다.</li>
<li><strong>취침 타이머:</strong> 정한 시간이 지나면 소리가 천천히 작아지며 꺼집니다.</li>
<li><strong>상황:</strong> 카페, 독서, 작업, 잠들기 전 같은 상황에 맞춘 믹스를 고르고, 나만의 믹스를 저장합니다.</li>
<li>모든 소리는 앱 안에 들어 있어, 다른 앱을 쓰거나 화면이 꺼져 있어도, 인터넷 없이도 재생됩니다.</li>
<li>계정이 필요 없으며, 앱에는 광고가 없습니다.</li>
</ol>"""),
   ("건강과 안전", """<ol>
<li>파우사는 의료기기나 치료 도구가 아닙니다. 수면, 집중, 휴식, 건강에 어떤 효과가 있다고 약속하지 않으며, 질병의 진단·치료·예방을 위한 것이 아닙니다.</li>
<li>바이노럴 비트를 비롯한 앱의 모든 소리는 분위기를 위한 것입니다.</li>
<li>적당한 음량으로 들어 주세요. 큰 소리로 오래 들으면 청력이 상할 수 있습니다.</li>
<li>운전 중이거나 기계를 다룰 때처럼 주의를 기울여야 하는 상황에서는 앱을 쓰지 마세요.</li>
</ol>"""),
   ("구독, 평생 이용권, 무료 체험", """<ol>
<li>유료 기능은 App Store 또는 Google Play 인앱 결제로 삽니다. 연간 구독, 월간 구독, 그리고 한 번 결제하는 평생 이용권이 있습니다.</li>
<li>구독은 해지할 때까지 같은 기간으로 자동 갱신되며, 스토어의 구독 관리에서 언제든 해지할 수 있습니다. 해지해도 이미 결제한 기간이 끝날 때까지 쓸 수 있습니다.</li>
<li><strong>무료 체험:</strong> 연간 구독에는 7일 무료 체험이 있습니다. 시작하기 전에 앱이 체험이 끝나는 날짜를 보여 드립니다. App Store에서는 체험이 끝나기 최소 24시간 전까지, Google Play에서는 체험이 끝나기 전까지 해지하지 않으면 연간 구독으로 바뀌어 결제됩니다. 알림을 허용하면 체험이 끝나기 2일 전에 기기에서 알림을 드립니다.</li>
<li><strong>평생 이용권:</strong> 한 번 결제하며 자동 갱신되지 않습니다. 같은 스토어 계정으로 앱의 “구매 복원”에서 다시 불러올 수 있습니다.</li>
<li>가격은 구매 전에 스토어 결제 화면에 표시되며, 나라마다 다를 수 있습니다. 결제·환불은 각 스토어의 정책과 절차에 따릅니다. 디지털 콘텐츠의 특성상, 구매 즉시 이용이 시작되는 데 동의하면 법이 허용하는 범위에서 청약철회권이 소멸할 수 있으며, 이 경우에도 스토어의 환불 절차는 이용할 수 있습니다.</li>
</ol>"""),
   ("음악과 소리의 이용 범위", """<ol>
<li>앱의 음악과 소리는 이용자 개인이 앱 안에서 비상업적으로 듣는 용도로만 이용이 허락됩니다. 구독이나 평생 이용권도 같습니다.</li>
<li>매장, 카페, 식당, 사무실 등에서 손님이나 여러 사람에게 들려주는 공개 재생은 허락되지 않습니다. 이런 영업용 이용은 본 약관에 포함되지 않습니다.</li>
<li>앱의 음악과 소리를 녹음하거나 추출해 따로 쓰거나 다른 사람에게 나눠 주는 것은 허락되지 않습니다.</li>
</ol>"""),
   ("외부 서비스", """<p>앱의 결제는 App Store와 Google Play를 통해 이루어집니다. 이 서비스들은 앱과 별개이며 각자의 이용약관과 개인정보처리방침이 적용됩니다. 외부 서비스의 내용과 이용 가능 여부에 대해 회사는 책임지지 않습니다.</p>"""),
   ("지적재산권", """<p>앱의 로고, “Pausa·파우사” 명칭, 디자인, 문구, 소스코드와 앱에 들어 있는 음악·소리에 대한 권리는 회사 또는 회사에 이용을 허락한 권리자에게 있습니다. 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다.</p>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 결제·이용 제한을 우회하지 않습니다.</li>
<li>앱의 음악과 소리를 위 이용 범위를 넘어 쓰지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다. 스토어나 기기 운영체제의 변경으로 관련 기능이 제한될 수 있습니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 생명·신체·건강의 침해, 그리고 제조물책임법에 따른 경우에는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>경과실의 경우 회사는 계약상 본질적인 의무를 위반했을 때에만, 계약 체결 시 예견할 수 있었던 통상적인 손해에 한해 책임을 집니다.</li>
<li>저장한 믹스와 설정은 기기에만 저장됩니다. 회사는 이를 보관하지 않으며, 기기 분실·앱 삭제·초기화로 잃어버린 믹스를 되살려 드릴 수 없습니다.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Pausa Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-11-13"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "These terms are the agreement between you and Vicino Labs for using Pausa, a soundscape app. By installing and using the app you agree to them.",
  "footer": "These terms are effective from 13 November 2026 (version 1.0).",
  "other": "Privacy Policy →",
  "sections": [
   ("Scope", "<p>These terms govern the use of the mobile app Pausa (the “app”) provided by Vicino Labs (the “company”).</p>"),
   ("Provider", _op_ref("en", N)),
   ("Validity and changes", """<ol>
<li>These terms take effect when published in the app or in another way chosen by the company.</li>
<li>The company may change them within the law and will announce the effective date and reason in advance.</li>
<li>If you do not agree to changed terms, you may stop using and delete the app.</li>
</ol>"""),
   ("What the app offers", """<ol>
<li><strong>Mix:</strong> blend music with rain, fireplace, café murmur and wind, each at the level you like.</li>
<li><strong>Binaural tone:</strong> generated live on your device, with a different tone in each ear. Use headphones.</li>
<li><strong>Sleep timer:</strong> after the time you set, the sound slowly fades out and stops.</li>
<li><strong>Moments:</strong> pick a mix made for the café, reading, desk work or bedtime, and save your own mixes.</li>
<li>Every sound is built into the app, so it plays in the background, with the screen off and offline.</li>
<li>No account is needed, and the app contains no ads.</li>
</ol>"""),
   ("Health and safety", """<ol>
<li>Pausa is not a medical device or a therapy. It makes no promise of any effect on sleep, focus, relaxation or health, and is not meant to diagnose, treat or prevent any condition.</li>
<li>All sounds in the app, including the binaural tone, are for atmosphere only.</li>
<li>Please listen at a moderate volume. Listening loudly for long periods can damage your hearing.</li>
<li>Do not use the app while driving, operating machinery or in any other situation that needs your attention.</li>
</ol>"""),
   ("Subscriptions, lifetime purchase and free trial", """<ol>
<li>Paid features are bought as in-app purchases through the App Store or Google Play: a yearly subscription, a monthly subscription and a one-time lifetime purchase.</li>
<li>A subscription renews for the same period until cancelled; cancel any time in the store's subscription settings. It keeps working until the paid period ends.</li>
<li><strong>Free trial:</strong> the yearly subscription comes with a 7-day free trial. Before you start, the app shows the date the trial ends. Unless you cancel at least 24 hours before the trial ends (App Store) or before the trial ends (Google Play), it turns into a paid yearly subscription. If you allow notifications, your device reminds you 2 days before the trial ends.</li>
<li><strong>Lifetime purchase:</strong> paid once and never renewed. With the same store account you can bring it back with “Restore purchases” in the app.</li>
<li>Prices are shown in the store before you buy and may differ by country. Payment and refunds follow each store's rules and process. For digital content, if you agree that use starts immediately, your right of withdrawal may end as far as the law allows; the store's refund process remains available.</li>
</ol>"""),
   ("Use of the music and sounds", """<ol>
<li>The music and sounds in the app are licensed to you only for personal, non-commercial listening inside the app. This also applies with a subscription or the lifetime purchase.</li>
<li>Playing them to customers or the public, for example in a shop, café, restaurant or office, is not allowed. Business use of this kind is not covered by these terms.</li>
<li>You may not record or extract the music and sounds to use them elsewhere or pass them on to others.</li>
</ol>"""),
   ("External services", """<p>Payments in the app go through the App Store and Google Play. They are separate from the app and governed by their own terms and privacy policies. The company is not responsible for their content or availability.</p>"""),
   ("Intellectual property", """<p>The rights to the app's logo, the name “Pausa”, its design, texts and source code and to the music and sounds in the app belong to the company or to the rights holders who licensed them to it. You may not copy, distribute, transmit, publish, reverse-engineer or create derivative works without prior written consent.</p>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the app or circumvent payment or usage limits.</li>
<li>Do not use the music and sounds beyond the scope described above.</li>
<li>Do not disrupt the app's normal operation.</li>
<li>Comply with applicable law and these terms.</li>
</ol>"""),
   ("Changes and discontinuation", """<p>The company may change or discontinue all or part of the app for operational or technical reasons and will announce this in advance unless urgent. Changes to the stores or to the device's operating system may limit related features.</p>"""),
   ("Liability", """<ol>
<li>The company is liable without limitation for intent and gross negligence, for injury to life, body or health, and under the Product Liability Act.</li>
<li>For slight negligence the company is liable only for breach of essential contractual obligations, limited to the typical damage foreseeable when the contract was made.</li>
<li>Saved mixes and settings are stored only on your device. The company does not keep them and cannot restore mixes lost through loss of the device, deletion or reset.</li>
</ol>"""),
   ("Governing law and jurisdiction", """<p>German law applies. Mandatory consumer-protection rules of the country where you, as a consumer, habitually reside (e.g. an EU member state) remain unaffected. Otherwise the courts at the company's seat (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For questions about these terms, please contact us.</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Pausa Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "13.11.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln die Nutzung von Pausa, einer Klang-App von Vicino Labs. Mit Installation und Nutzung der App stimmst du ihnen zu.",
  "footer": "Diese Bedingungen gelten ab dem 13. November 2026 (Version 1.0).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Geltungsbereich", "<p>Diese Bedingungen regeln die Nutzung der mobilen App Pausa („App“) von Vicino Labs („Anbieter“).</p>"),
   ("Anbieter", _op_ref("de", N)),
   ("Geltung und Änderungen", """<ol>
<li>Die Bedingungen gelten ab Veröffentlichung in der App oder auf andere vom Anbieter gewählte Weise.</li>
<li>Der Anbieter kann sie im Rahmen des Gesetzes ändern und kündigt Datum und Grund vorher an.</li>
<li>Wenn du geänderten Bedingungen nicht zustimmst, kannst du die App nicht mehr nutzen und löschen.</li>
</ol>"""),
   ("Leistungen", """<ol>
<li><strong>Mix:</strong> Musik mit Regen, Kaminfeuer, Cafégeräuschen und Wind mischen, jeweils so laut, wie du magst.</li>
<li><strong>Binauraler Ton:</strong> wird direkt auf deinem Gerät erzeugt, auf jedem Ohr ein anderer Ton. Nur mit Kopfhörern.</li>
<li><strong>Sleep-Timer:</strong> Nach der eingestellten Zeit wird der Klang langsam leiser und verstummt.</li>
<li><strong>Momente:</strong> einen passenden Mix fürs Café, zum Lesen, für die Arbeit oder vor dem Schlafen wählen und eigene Mixe speichern.</li>
<li>Alle Klänge stecken in der App; sie laufen im Hintergrund, bei ausgeschaltetem Bildschirm und offline.</li>
<li>Ein Konto ist nicht nötig, und die App enthält keine Werbung.</li>
</ol>"""),
   ("Gesundheit und Sicherheit", """<ol>
<li>Pausa ist kein Medizinprodukt und keine Therapie. Die App verspricht keine Wirkung auf Schlaf, Konzentration, Entspannung oder Gesundheit und dient nicht der Diagnose, Behandlung oder Vorbeugung von Krankheiten.</li>
<li>Alle Klänge der App, auch der binaurale Ton, dienen nur der Atmosphäre.</li>
<li>Bitte hör in angemessener Lautstärke. Langes, lautes Hören kann das Gehör schädigen.</li>
<li>Nutze die App nicht beim Autofahren, beim Bedienen von Maschinen oder in anderen Situationen, die deine Aufmerksamkeit erfordern.</li>
</ol>"""),
   ("Abos, Kauf auf Lebenszeit und kostenloser Probezeitraum", """<ol>
<li>Kostenpflichtige Funktionen kaufst du als In-App-Kauf über den App Store oder Google Play: ein Jahresabo, ein Monatsabo und einen einmaligen Kauf auf Lebenszeit.</li>
<li>Ein Abo verlängert sich um denselben Zeitraum, bis du kündigst; kündigen kannst du jederzeit in den Abo-Einstellungen des Stores. Es läuft bis zum Ende des bezahlten Zeitraums.</li>
<li><strong>Probezeitraum:</strong> Zum Jahresabo gehört ein kostenloser Probezeitraum von 7 Tagen. Vor dem Start zeigt dir die App das Enddatum. Wenn du nicht spätestens 24 Stunden vor Ende (App Store) bzw. vor Ende (Google Play) kündigst, geht er in ein kostenpflichtiges Jahresabo über. Wenn du Benachrichtigungen erlaubst, erinnert dich dein Gerät 2 Tage vor dem Ende.</li>
<li><strong>Kauf auf Lebenszeit:</strong> wird einmal bezahlt und verlängert sich nicht. Mit demselben Store-Konto kannst du ihn in der App über „Käufe wiederherstellen“ zurückholen.</li>
<li>Preise werden vor dem Kauf im Store angezeigt und können je nach Land abweichen. Zahlung und Erstattung richten sich nach den Regeln und Abläufen des jeweiligen Stores. Bei digitalen Inhalten kann das Widerrufsrecht im gesetzlich zulässigen Umfang erlöschen, wenn du dem sofortigen Beginn zustimmst; das Erstattungsverfahren des Stores bleibt möglich.</li>
</ol>"""),
   ("Nutzung der Musik und Klänge", """<ol>
<li>Musik und Klänge der App sind dir nur zum privaten, nicht kommerziellen Hören in der App lizenziert. Das gilt auch mit Abo oder Kauf auf Lebenszeit.</li>
<li>Das Abspielen für Kundschaft oder Publikum, etwa in Geschäften, Cafés, Restaurants oder Büros, ist nicht erlaubt. Eine solche geschäftliche Nutzung ist von diesen Bedingungen nicht umfasst.</li>
<li>Musik und Klänge dürfen nicht aufgenommen oder herausgelöst werden, um sie anderweitig zu nutzen oder weiterzugeben.</li>
</ol>"""),
   ("Externe Dienste", """<p>Zahlungen in der App laufen über den App Store und Google Play. Sie sind von der App getrennt; es gelten deren eigene Bedingungen und Datenschutzerklärungen. Für deren Inhalte und Verfügbarkeit ist der Anbieter nicht verantwortlich.</p>"""),
   ("Geistiges Eigentum", """<p>Die Rechte an Logo, dem Namen „Pausa“, Gestaltung, Texten und Quellcode der App sowie an den enthaltenen Musikstücken und Klängen liegen beim Anbieter oder bei den Rechteinhabern, die sie ihm lizenziert haben. Ohne vorherige schriftliche Zustimmung sind Vervielfältigung, Verbreitung, Übertragung, Veröffentlichung, Reverse Engineering und Bearbeitungen nicht erlaubt.</p>"""),
   ("Pflichten der Nutzer", """<ol>
<li>Kein Reverse Engineering oder Dekompilieren der App und keine Umgehung der Bezahlung oder der Nutzungsgrenzen.</li>
<li>Keine Nutzung der Musik und Klänge über den oben beschriebenen Umfang hinaus.</li>
<li>Keine Störung des normalen Betriebs der App.</li>
<li>Einhaltung der Gesetze und dieser Bedingungen.</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Der Anbieter kann Funktionen der App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigt dies, außer in dringenden Fällen, vorher an. Änderungen der Stores oder des Betriebssystems können zugehörige Funktionen einschränken.</p>"""),
   ("Haftung", """<ol>
<li>Der Anbieter haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit sowie nach dem Produkthaftungsgesetz.</li>
<li>Bei leichter Fahrlässigkeit haftet der Anbieter nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den bei Vertragsschluss vorhersehbaren, typischen Schaden.</li>
<li>Gespeicherte Mixe und Einstellungen liegen nur auf deinem Gerät. Der Anbieter speichert sie nicht und kann Mixe, die durch Verlust des Geräts, Löschung oder Zurücksetzen verloren gehen, nicht wiederherstellen.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt deutsches Recht. Zwingende Verbraucherschutzvorschriften des Staates, in dem du als Verbraucher deinen gewöhnlichen Aufenthalt hast (z. B. ein EU-Mitgliedstaat), bleiben unberührt. Im Übrigen ist Gerichtsstand der Sitz des Anbieters (Dortmund).</p>"""),
   ("Kontakt", "<p>Fragen zu diesen Bedingungen richte bitte an:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Pausa — Termini di utilizzo",
  "h1": "Termini di utilizzo",
  "meta": [("In vigore dal", "13.11.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Questi termini regolano l'uso di Pausa, un'app di sottofondi sonori di Vicino Labs. Installando e usando l'app li accetti.",
  "footer": "Questi termini sono in vigore dal 13 novembre 2026 (versione 1.0).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>Questi termini regolano l'uso dell'app mobile Pausa (“app”) fornita da Vicino Labs (“fornitore”).</p>"),
   ("Fornitore", _op_ref("it", N)),
   ("Validità e modifiche", """<ol>
<li>I termini sono validi dalla pubblicazione nell'app o in altro modo scelto dal fornitore.</li>
<li>Il fornitore può modificarli nei limiti di legge, comunicando in anticipo data e motivo.</li>
<li>Se non accetti i termini modificati puoi smettere di usare l'app ed eliminarla.</li>
</ol>"""),
   ("Cosa offre l'app", """<ol>
<li><strong>Mix:</strong> mescola la musica con pioggia, camino, brusio del caffè e vento, ciascuno al volume che preferisci.</li>
<li><strong>Tono binaurale:</strong> generato in tempo reale sul dispositivo, con un tono diverso per ciascun orecchio. Servono le cuffie.</li>
<li><strong>Timer di spegnimento:</strong> allo scadere del tempo impostato il suono si abbassa piano e si spegne.</li>
<li><strong>Momenti:</strong> scegli un mix pensato per il bar, la lettura, il lavoro o la sera prima di dormire e salva i tuoi mix.</li>
<li>Tutti i suoni sono già nell'app: funzionano in background, a schermo spento e offline.</li>
<li>Non serve un account e l'app non contiene pubblicità.</li>
</ol>"""),
   ("Salute e sicurezza", """<ol>
<li>Pausa non è un dispositivo medico né una terapia. Non promette alcun effetto su sonno, concentrazione, rilassamento o salute e non serve a diagnosticare, curare o prevenire malattie.</li>
<li>Tutti i suoni dell'app, compreso il tono binaurale, servono solo a creare atmosfera.</li>
<li>Ascolta a volume moderato. Ascoltare a lungo ad alto volume può danneggiare l'udito.</li>
<li>Non usare l'app mentre guidi, usi macchinari o in altre situazioni che richiedono attenzione.</li>
</ol>"""),
   ("Abbonamenti, acquisto a vita e prova gratuita", """<ol>
<li>Le funzioni a pagamento si acquistano in-app tramite l'App Store o Google Play: un abbonamento annuale, un abbonamento mensile e un acquisto a vita una tantum.</li>
<li>Un abbonamento si rinnova per lo stesso periodo fino alla disdetta; puoi annullarlo in qualsiasi momento nelle impostazioni degli abbonamenti dello store. Resta attivo fino alla fine del periodo pagato.</li>
<li><strong>Prova gratuita:</strong> l'abbonamento annuale include una prova gratuita di 7 giorni. Prima di iniziare, l'app ti mostra la data in cui termina. Se non disdici almeno 24 ore prima della fine (App Store) o prima della fine (Google Play), diventa un abbonamento annuale a pagamento. Se consenti le notifiche, il dispositivo te lo ricorda 2 giorni prima della fine.</li>
<li><strong>Acquisto a vita:</strong> si paga una volta e non si rinnova. Con lo stesso account dello store puoi recuperarlo dall'app con «Ripristina acquisti».</li>
<li>I prezzi sono indicati nello store prima dell’acquisto e possono variare da paese a paese. Pagamenti e rimborsi seguono le regole e le procedure di ciascuno store. Per i contenuti digitali, se accetti l'inizio immediato dell'uso, il diritto di recesso può estinguersi nei limiti di legge; la procedura di rimborso dello store resta disponibile.</li>
</ol>"""),
   ("Uso della musica e dei suoni", """<ol>
<li>La musica e i suoni dell'app ti sono concessi in licenza solo per l'ascolto personale e non commerciale all'interno dell'app. Vale anche con un abbonamento o con l'acquisto a vita.</li>
<li>Non è consentito diffonderli per clienti o pubblico, ad esempio in negozi, bar, ristoranti o uffici. Questo uso commerciale non rientra in questi termini.</li>
<li>Non è consentito registrare o estrarre la musica e i suoni per usarli altrove o darli ad altri.</li>
</ol>"""),
   ("Servizi esterni", """<p>I pagamenti nell'app passano dall'App Store e da Google Play. Sono separati dall'app e regolati dai propri termini e informative. Il fornitore non risponde del loro contenuto o della loro disponibilità.</p>"""),
   ("Proprietà intellettuale", """<p>I diritti su logo, nome “Pausa”, grafica, testi e codice sorgente dell'app e sulla musica e i suoni in essa contenuti appartengono al fornitore o ai titolari che glieli hanno concessi in licenza. Senza consenso scritto preventivo non è consentito copiare, distribuire, trasmettere, pubblicare, decompilare o creare opere derivate.</p>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare o analizzare l'app né aggirare il pagamento o i limiti d'uso.</li>
<li>Non usare la musica e i suoni oltre i limiti descritti sopra.</li>
<li>Non ostacolare il normale funzionamento dell'app.</li>
<li>Rispettare la legge e questi termini.</li>
</ol>"""),
   ("Modifica e sospensione", """<p>Il fornitore può modificare o sospendere in tutto o in parte le funzioni dell'app per motivi organizzativi o tecnici, avvisando prima salvo urgenza. Cambiamenti degli store o del sistema operativo possono limitare le funzioni collegate.</p>"""),
   ("Responsabilità", """<ol>
<li>Il fornitore risponde senza limiti per dolo e colpa grave, per danni alla vita, al corpo o alla salute e ai sensi della legge sulla responsabilità del produttore.</li>
<li>Per colpa lieve risponde solo in caso di violazione di obblighi contrattuali essenziali, nei limiti del danno tipico prevedibile alla conclusione del contratto.</li>
<li>I mix salvati e le impostazioni restano solo sul dispositivo. Il fornitore non li conserva e non può recuperare mix persi per smarrimento del dispositivo, cancellazione o ripristino.</li>
</ol>"""),
   ("Legge applicabile e foro", """<p>Si applica la legge tedesca. Restano salve le norme imperative a tutela dei consumatori del paese in cui risiedi abitualmente (ad es. uno Stato UE). Per il resto è competente il foro della sede del fornitore (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande su questi termini scrivici:</p>" + _id_card("it")),
  ],
 },
}

for _d in TERMS.values():
    assert len(_d["sections"]) == N, "update N (Contact section number)"
