"""끼아베(Chiave) 이용약관 본문 (ko/en/de/it) — chiave_legal.py가 HTML로 만든다.

2026-11-06 버전 1.0 — 2026-11-06 운영자 승인, 게시. leggii_terms_content.py의 틀과 문구를 따랐다.
요금제는 스캔 페이지 수: 7일 체험 3페이지(모두), Free 월 1, Pro 월 20, Pro+ 월 50.
가격은 Pro €5.99/월, Pro+ €9.99/월 (2026-11-06 운영자 결정, 출시 때 최종 확인).
책임 제한은 Leggii와 같은 독일법상 허용 범위.
"""

from appoggio_privacy_content import _id_card, _contact


TERMS = {
 "ko": {
  "title": "끼아베(Chiave) 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.11.06"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 만든 악보 앱 끼아베(Chiave)를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 2026년 11월 6일부터 시행됩니다 (버전 1.0).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 끼아베(Chiave, 이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _id_card("ko")),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li>악보 쓰기·편집, 이조, 피아노 소리로 듣기</li>
<li><strong>악보 스캔(선택):</strong> 카메라·사진 앨범·PDF의 페이지를 AI로 읽어 편집할 수 있는 악보로 만듭니다. 스캔한 페이지 수는 요금제에 따라 셉니다.</li>
<li><strong>내보내기:</strong> PDF, PNG 이미지, MusicXML, 편집 가능한 파일</li>
<li>무료 요금제에는 같은 회사 서비스 welegato로 가는 링크가 화면 아래에 표시됩니다.</li>
<li>회원가입이 없으며, 악보는 이용자의 기기에만 저장됩니다.</li>
</ol>"""),
   ("요금제와 구독", f"""<ol>
<li><strong>무료 체험:</strong> 모든 이용자는 처음 <strong>7일 동안 3페이지</strong>를 스캔할 수 있습니다. 체험은 기기당 한 번이며, 앱을 다시 설치해도 반복되지 않습니다. 체험이 끝나면 무료 요금제가 적용되며 자동 결제는 없습니다.</li>
<li><strong>Free:</strong> 매월 1페이지 스캔</li>
<li><strong>Pro:</strong> 매월 20페이지 스캔, 배너 없음 — 월 €5.99</li>
<li><strong>Pro+:</strong> 매월 50페이지 스캔, 배너 없음 — 월 €9.99</li>
<li>Pro와 Pro+는 <strong>월간 정기 구독</strong>으로, Google Play 또는 App Store가 스토어에 표시된 가격으로 청구합니다. 해지할 때까지 같은 기간으로 자동 갱신되며, 스토어의 구독 관리에서 언제든 해지할 수 있습니다. 해지해도 이미 결제한 기간이 끝날 때까지 쓸 수 있고, 그 뒤에는 무료 요금제로 돌아갑니다.</li>
<li>스캔 페이지는 현금으로 바꾸거나 다른 사람에게 넘길 수 없습니다.</li>
<li>가격은 결제 화면에 표시됩니다. 결제·환불은 각 스토어의 정책과 절차에 따릅니다. 디지털 콘텐츠의 특성상, 구매 즉시 이용이 시작되는 데 동의하면 법이 허용하는 범위에서 청약철회권이 소멸할 수 있으며, 이 경우에도 스토어의 환불 절차는 이용할 수 있습니다.</li>
<li>매월 페이지 수나 요금제 조건을 바꿀 때는 미리 알리며, 이미 결제한 기간에는 적용하지 않습니다.</li>
</ol>"""),
   ("악보 스캔", """<ol>
<li>스캔 결과는 AI가 읽은 것으로 <strong>틀리거나 빠진 음표가 있을 수 있습니다.</strong> 연주나 출판에 쓰기 전에 원본과 비교해 확인해 주세요.</li>
<li>스캔은 이용자가 이용할 권리가 있는 악보에만 써야 합니다.</li>
<li>회사는 남용을 막기 위해 이용을 제한할 수 있습니다.</li>
</ol>"""),
   ("악보와 저작권", """<ol>
<li>이용자가 앱에서 쓰거나 스캔·이조·내보내기·공유하는 악보에 대한 저작권 준수는 이용자의 책임입니다.</li>
<li>회사는 이용자의 악보를 서버에 보관하지 않습니다. 스캔할 때 보내는 조각 이미지는 음표 인식에만 쓰고 저장하지 않습니다.</li>
</ol>"""),
   ("welegato 및 외부 서비스", """<p>앱에는 welegato, 다른 Vicino Labs 앱의 스토어 페이지, Google Play·App Store 등 외부 서비스로 가는 링크와 기능이 있습니다. 이 서비스들은 앱과 별개이며 각자의 이용약관과 개인정보처리방침이 적용됩니다. 외부 서비스의 내용과 이용 가능 여부에 대해 회사는 책임지지 않습니다.</p>"""),
   ("지적재산권", """<p>앱의 로고, “Chiave·끼아베” 명칭, 디자인, 문구, 소스코드에 대한 권리는 회사에 있습니다. 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다.</p>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 결제·페이지 제한을 우회하지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다. 외부 서비스(Google Gemini 등)의 변경으로 관련 기능이 제한될 수 있습니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 생명·신체·건강의 침해, 그리고 제조물책임법에 따른 경우에는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>경과실의 경우 회사는 계약상 본질적인 의무를 위반했을 때에만, 계약 체결 시 예견할 수 있었던 통상적인 손해에 한해 책임을 집니다.</li>
<li>악보는 기기에만 저장되고 클라우드 백업이 없습니다. 기기 분실·앱 삭제·초기화로 인한 손실에 대비해 중요한 악보는 내보내기로 직접 보관해 주세요.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _contact("운영자")),
  ],
 },
 "en": {
  "title": "Chiave Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-11-06"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "These terms are the agreement between you and Vicino Labs for using Chiave, a sheet music app. By installing and using the app you agree to them.",
  "footer": "These terms are effective from 6 November 2026 (version 1.0).",
  "other": "Privacy Policy →",
  "sections": [
   ("Scope", "<p>These terms govern the use of the mobile app Chiave (the “app”) provided by Vicino Labs (the “company”).</p>"),
   ("Provider", _id_card("en")),
   ("Validity and changes", """<ol>
<li>These terms take effect when published in the app or in another way chosen by the company.</li>
<li>The company may change them within the law and will announce the effective date and reason in advance.</li>
<li>If you do not agree to changed terms, you may stop using and delete the app.</li>
</ol>"""),
   ("What the app offers", """<ol>
<li>Writing and editing scores, transposing, and listening with a piano sound</li>
<li><strong>Score scanning (optional):</strong> pages from the camera, photo album or a PDF are read by AI and turned into an editable score. Scanned pages are counted according to your plan.</li>
<li><strong>Export:</strong> PDF, PNG image, MusicXML, editable file</li>
<li>The Free plan shows a link to welegato, a service of the same company, at the bottom of the screen.</li>
<li>There is no sign-up; scores are stored only on your device.</li>
</ol>"""),
   ("Plans and subscriptions", f"""<ol>
<li><strong>Free trial:</strong> everyone can scan <strong>3 pages during the first 7 days</strong>. The trial is available once per device and does not restart when you reinstall the app. Afterwards the Free plan applies; there is no automatic payment.</li>
<li><strong>Free:</strong> 1 scanned page per month</li>
<li><strong>Pro:</strong> 20 scanned pages per month, no banner — €5.99 per month</li>
<li><strong>Pro+:</strong> 50 scanned pages per month, no banner — €9.99 per month</li>
<li>Pro and Pro+ are <strong>monthly subscriptions</strong>, billed by Google Play or the Apple App Store at the price shown in the store. They renew for the same period until cancelled; cancel any time in the store's subscription settings. A subscription keeps working until the paid period ends; afterwards the Free plan applies.</li>
<li>Scan pages have no cash value and cannot be transferred.</li>
<li>Prices are shown at checkout. Payment and refunds follow each store's rules and process. For digital content, if you agree that use starts immediately, your right of withdrawal may end as far as the law allows; the store's refund process remains available.</li>
<li>Changes to the monthly pages or plan terms are announced in advance and do not apply to periods already paid.</li>
</ol>"""),
   ("Score scanning", """<ol>
<li>Scan results are read by AI and <strong>can contain wrong or missing notes.</strong> Please check them against the original before performing or publishing.</li>
<li>Only scan scores you have the right to use.</li>
<li>We may limit use to prevent abuse.</li>
</ol>"""),
   ("Scores and copyright", """<ol>
<li>You are responsible for respecting copyright in the scores you write, scan, transpose, export or share in the app.</li>
<li>The company does not keep your scores on its server. The strip images sent for scanning are used only to recognise the notes and are not stored.</li>
</ol>"""),
   ("welegato and external services", """<p>The app links to and uses external services such as welegato, the store pages of other Vicino Labs apps, Google Play and the App Store. They are separate from the app and governed by their own terms and privacy policies. The company is not responsible for their content or availability.</p>"""),
   ("Intellectual property", """<p>The company holds the rights to the app's logo, the name “Chiave”, its design, texts and source code. You may not copy, distribute, transmit, publish, reverse-engineer or create derivative works without prior written consent.</p>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the app or circumvent payment or page limits.</li>
<li>Do not disrupt the app's normal operation.</li>
<li>Comply with applicable law and these terms.</li>
</ol>"""),
   ("Changes and discontinuation", """<p>The company may change or discontinue all or part of the app for operational or technical reasons and will announce this in advance unless urgent. Changes to external services (such as Google Gemini) may limit related features.</p>"""),
   ("Liability", """<ol>
<li>The company is liable without limitation for intent and gross negligence, for injury to life, body or health, and under the Product Liability Act.</li>
<li>For slight negligence the company is liable only for breach of essential contractual obligations, limited to the typical damage foreseeable when the contract was made.</li>
<li>Scores are stored only on your device and there is no cloud backup. To protect against loss of the device, deletion or reset, please keep important scores yourself by exporting them.</li>
</ol>"""),
   ("Governing law and jurisdiction", """<p>German law applies. Mandatory consumer-protection rules of the country where you, as a consumer, habitually reside (e.g. an EU member state) remain unaffected. Otherwise the courts at the company's seat (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For questions about these terms, please contact us.</p>" + _contact("Operator")),
  ],
 },
 "de": {
  "title": "Chiave Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "06.11.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln die Nutzung von Chiave, einer Noten-App von Vicino Labs. Mit Installation und Nutzung der App stimmst du ihnen zu.",
  "footer": "Diese Bedingungen gelten ab dem 6. November 2026 (Version 1.0).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Geltungsbereich", "<p>Diese Bedingungen regeln die Nutzung der mobilen App Chiave („App“) von Vicino Labs („Anbieter“).</p>"),
   ("Anbieter", _id_card("de")),
   ("Geltung und Änderungen", """<ol>
<li>Die Bedingungen gelten ab Veröffentlichung in der App oder auf andere vom Anbieter gewählte Weise.</li>
<li>Der Anbieter kann sie im Rahmen des Gesetzes ändern und kündigt Datum und Grund vorher an.</li>
<li>Wenn du geänderten Bedingungen nicht zustimmst, kannst du die App nicht mehr nutzen und löschen.</li>
</ol>"""),
   ("Leistungen", """<ol>
<li>Noten schreiben und bearbeiten, transponieren und mit Klavierklang anhören</li>
<li><strong>Notenscan (freiwillig):</strong> Seiten aus Kamera, Fotoalbum oder PDF werden per KI gelesen und zu bearbeitbaren Noten. Gescannte Seiten werden je nach Tarif gezählt.</li>
<li><strong>Export:</strong> PDF, PNG-Bild, MusicXML, bearbeitbare Datei</li>
<li>Im Free-Tarif wird unten im Bildschirm ein Link zu welegato, einem Dienst desselben Anbieters, angezeigt.</li>
<li>Es gibt keine Registrierung; Noten werden nur auf deinem Gerät gespeichert.</li>
</ol>"""),
   ("Tarife und Abos", f"""<ol>
<li><strong>Testphase:</strong> Alle können in den ersten <strong>7 Tagen 3 Seiten</strong> scannen. Die Testphase gibt es einmal pro Gerät; sie beginnt bei Neuinstallation nicht neu. Danach gilt der Free-Tarif; es gibt keine automatische Zahlung.</li>
<li><strong>Free:</strong> 1 gescannte Seite pro Monat</li>
<li><strong>Pro:</strong> 20 gescannte Seiten pro Monat, kein Banner — 5,99 € pro Monat</li>
<li><strong>Pro+:</strong> 50 gescannte Seiten pro Monat, kein Banner — 9,99 € pro Monat</li>
<li>Pro und Pro+ sind <strong>monatliche Abos</strong>, die Google Play oder der Apple App Store zum im Store angezeigten Preis abrechnet. Sie verlängern sich um denselben Zeitraum, bis du kündigst; kündigen kannst du jederzeit in den Abo-Einstellungen des Stores. Ein Abo läuft bis zum Ende des bezahlten Zeitraums; danach gilt der Free-Tarif.</li>
<li>Scan-Seiten haben keinen Geldwert und sind nicht übertragbar.</li>
<li>Preise werden an der Kasse angezeigt. Zahlung und Erstattung richten sich nach den Regeln und Abläufen des jeweiligen Stores. Bei digitalen Inhalten kann das Widerrufsrecht im gesetzlich zulässigen Umfang erlöschen, wenn du dem sofortigen Beginn zustimmst; das Erstattungsverfahren des Stores bleibt möglich.</li>
<li>Änderungen der monatlichen Seiten oder der Tarifbedingungen kündigen wir vorher an; sie gelten nicht für bereits bezahlte Zeiträume.</li>
</ol>"""),
   ("Notenscan", """<ol>
<li>Scan-Ergebnisse liest eine KI; sie <strong>können falsche oder fehlende Noten enthalten.</strong> Bitte vergleiche sie vor Aufführung oder Veröffentlichung mit dem Original.</li>
<li>Scanne nur Noten, die du nutzen darfst.</li>
<li>Zum Schutz vor Missbrauch können wir die Nutzung begrenzen.</li>
</ol>"""),
   ("Noten und Urheberrecht", """<ol>
<li>Für die Einhaltung des Urheberrechts an Noten, die du in der App schreibst, scannst, transponierst, exportierst oder teilst, bist du selbst verantwortlich.</li>
<li>Der Anbieter speichert deine Noten nicht auf seinem Server. Die für den Scan gesendeten Streifenbilder dienen nur der Notenerkennung und werden nicht gespeichert.</li>
</ol>"""),
   ("welegato und externe Dienste", """<p>Die App verlinkt und nutzt externe Dienste wie welegato, die Store-Seiten anderer Apps von Vicino Labs, Google Play und den App Store. Sie sind von der App getrennt; es gelten deren eigene Bedingungen und Datenschutzerklärungen. Für deren Inhalte und Verfügbarkeit ist der Anbieter nicht verantwortlich.</p>"""),
   ("Geistiges Eigentum", """<p>Die Rechte an Logo, dem Namen „Chiave“, Gestaltung, Texten und Quellcode der App liegen beim Anbieter. Ohne vorherige schriftliche Zustimmung sind Vervielfältigung, Verbreitung, Übertragung, Veröffentlichung, Reverse Engineering und Bearbeitungen nicht erlaubt.</p>"""),
   ("Pflichten der Nutzer", """<ol>
<li>Kein Reverse Engineering oder Dekompilieren der App und keine Umgehung der Bezahlung oder der Seitenlimits.</li>
<li>Keine Störung des normalen Betriebs der App.</li>
<li>Einhaltung der Gesetze und dieser Bedingungen.</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Der Anbieter kann Funktionen der App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigt dies, außer in dringenden Fällen, vorher an. Änderungen externer Dienste (z. B. Google Gemini) können zugehörige Funktionen einschränken.</p>"""),
   ("Haftung", """<ol>
<li>Der Anbieter haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit sowie nach dem Produkthaftungsgesetz.</li>
<li>Bei leichter Fahrlässigkeit haftet der Anbieter nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den bei Vertragsschluss vorhersehbaren, typischen Schaden.</li>
<li>Noten werden nur auf deinem Gerät gespeichert; eine Cloud-Sicherung gibt es nicht. Sichere wichtige Noten per Export selbst gegen Verlust des Geräts, Löschung oder Zurücksetzen.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt deutsches Recht. Zwingende Verbraucherschutzvorschriften des Staates, in dem du als Verbraucher deinen gewöhnlichen Aufenthalt hast (z. B. ein EU-Mitgliedstaat), bleiben unberührt. Im Übrigen ist Gerichtsstand der Sitz des Anbieters (Dortmund).</p>"""),
   ("Kontakt", "<p>Fragen zu diesen Bedingungen richte bitte an:</p>" + _contact("Betreiber")),
  ],
 },
 "it": {
  "title": "Chiave — Termini di utilizzo",
  "h1": "Termini di utilizzo",
  "meta": [("In vigore dal", "06.11.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Questi termini regolano l'uso di Chiave, un'app per spartiti di Vicino Labs. Installando e usando l'app li accetti.",
  "footer": "Questi termini sono in vigore dal 6 novembre 2026 (versione 1.0).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>Questi termini regolano l'uso dell'app mobile Chiave (“app”) fornita da Vicino Labs (“fornitore”).</p>"),
   ("Fornitore", _id_card("it")),
   ("Validità e modifiche", """<ol>
<li>I termini sono validi dalla pubblicazione nell'app o in altro modo scelto dal fornitore.</li>
<li>Il fornitore può modificarli nei limiti di legge, comunicando in anticipo data e motivo.</li>
<li>Se non accetti i termini modificati puoi smettere di usare l'app ed eliminarla.</li>
</ol>"""),
   ("Cosa offre l'app", """<ol>
<li>Scrittura e modifica di spartiti, trasposizione e ascolto con suono di pianoforte</li>
<li><strong>Scansione degli spartiti (facoltativa):</strong> le pagine da fotocamera, album o PDF vengono lette dall'AI e trasformate in uno spartito modificabile. Le pagine scansionate si contano secondo il piano.</li>
<li><strong>Esportazione:</strong> PDF, immagine PNG, MusicXML, file modificabile</li>
<li>Il piano Free mostra in fondo allo schermo un link a welegato, un servizio dello stesso fornitore.</li>
<li>Non c'è registrazione; gli spartiti restano solo sul tuo dispositivo.</li>
</ol>"""),
   ("Piani e abbonamenti", f"""<ol>
<li><strong>Prova gratuita:</strong> tutti possono scansionare <strong>3 pagine nei primi 7 giorni</strong>. La prova vale una volta per dispositivo e non riparte reinstallando l'app. Poi si applica il piano Free; non c'è alcun pagamento automatico.</li>
<li><strong>Free:</strong> 1 pagina scansionata al mese</li>
<li><strong>Pro:</strong> 20 pagine scansionate al mese, niente banner — 5,99 € al mese</li>
<li><strong>Pro+:</strong> 50 pagine scansionate al mese, niente banner — 9,99 € al mese</li>
<li>Pro e Pro+ sono <strong>abbonamenti mensili</strong>, addebitati da Google Play o dall'Apple App Store al prezzo indicato nello store. Si rinnovano per lo stesso periodo fino alla disdetta; puoi annullarli in qualsiasi momento nelle impostazioni degli abbonamenti dello store. Un abbonamento resta attivo fino alla fine del periodo pagato; poi si applica il piano Free.</li>
<li>Le pagine di scansione non hanno valore in denaro e non sono trasferibili.</li>
<li>I prezzi sono indicati al momento del pagamento. Pagamenti e rimborsi seguono le regole e le procedure di ciascuno store. Per i contenuti digitali, se accetti l'inizio immediato dell'uso, il diritto di recesso può estinguersi nei limiti di legge; la procedura di rimborso dello store resta disponibile.</li>
<li>Le modifiche alle pagine mensili o alle condizioni dei piani vengono annunciate prima e non valgono per periodi già pagati.</li>
</ol>"""),
   ("Scansione degli spartiti", """<ol>
<li>I risultati della scansione sono letti da un'AI e <strong>possono contenere note errate o mancanti.</strong> Confrontali con l'originale prima di eseguirli o pubblicarli.</li>
<li>Scansiona solo spartiti che hai il diritto di usare.</li>
<li>Possiamo limitarne l'uso per prevenire abusi.</li>
</ol>"""),
   ("Spartiti e diritto d'autore", """<ol>
<li>Sei responsabile del rispetto del diritto d'autore sugli spartiti che scrivi, scansioni, trasponi, esporti o condividi nell'app.</li>
<li>Il fornitore non conserva i tuoi spartiti sul proprio server. Le immagini a strisce inviate per la scansione servono solo a riconoscere le note e non vengono salvate.</li>
</ol>"""),
   ("welegato e servizi esterni", """<p>L'app collega e usa servizi esterni come welegato, le pagine store delle altre app di Vicino Labs, Google Play e l'App Store. Sono separati dall'app e regolati dai propri termini e informative. Il fornitore non risponde del loro contenuto o della loro disponibilità.</p>"""),
   ("Proprietà intellettuale", """<p>I diritti su logo, nome “Chiave”, grafica, testi e codice sorgente dell'app appartengono al fornitore. Senza consenso scritto preventivo non è consentito copiare, distribuire, trasmettere, pubblicare, decompilare o creare opere derivate.</p>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare o analizzare l'app né aggirare il pagamento o i limiti di pagine.</li>
<li>Non ostacolare il normale funzionamento dell'app.</li>
<li>Rispettare la legge e questi termini.</li>
</ol>"""),
   ("Modifica e sospensione", """<p>Il fornitore può modificare o sospendere in tutto o in parte le funzioni dell'app per motivi organizzativi o tecnici, avvisando prima salvo urgenza. Cambiamenti dei servizi esterni (come Google Gemini) possono limitare le funzioni collegate.</p>"""),
   ("Responsabilità", """<ol>
<li>Il fornitore risponde senza limiti per dolo e colpa grave, per danni alla vita, al corpo o alla salute e ai sensi della legge sulla responsabilità del produttore.</li>
<li>Per colpa lieve risponde solo in caso di violazione di obblighi contrattuali essenziali, nei limiti del danno tipico prevedibile alla conclusione del contratto.</li>
<li>Gli spartiti sono salvati solo sul dispositivo e non esiste un backup nel cloud. Conserva tu quelli importanti esportandoli, contro perdita del dispositivo, cancellazione o ripristino.</li>
</ol>"""),
   ("Legge applicabile e foro", """<p>Si applica la legge tedesca. Restano salve le norme imperative a tutela dei consumatori del paese in cui risiedi abitualmente (ad es. uno Stato UE). Per il resto è competente il foro della sede del fornitore (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande su questi termini scrivici:</p>" + _contact("Gestore")),
  ],
 },
}
