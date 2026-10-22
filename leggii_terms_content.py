"""Leggii(렛지 악보) 이용약관 본문 (ko/en/de/it) — leggii_legal.py가 HTML로 만든다.

2026-10-22 버전 1.0 (앱 1.0.0). 기본 기능 무료 + Pro 평생 이용권(스토어 인앱 결제) +
처음 7일 Pro 무료 체험. 이용자가 가져온 악보의 저작권은 이용자 책임(IMSLP 판본은 나라마다 다름).
책임 제한은 독일법상 허용 범위(고의·중과실, 생명·신체·건강, 제조물책임법은 제한 불가).
"""

from appoggio_privacy_content import _id_card, _contact

TERMS = {
 "ko": {
  "title": "렛지 악보(Leggii) 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.10.22"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 만든 악보 앱 렛지 악보(Leggii)를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 2026년 10월 22일부터 시행됩니다 (버전 1.0).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 렛지 악보(Leggii, 이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _id_card("ko")),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li><strong>무료 기능:</strong> PDF 악보 보기와 페이지 넘기기(페달 포함), 가져오기·사진 스캔·IMSLP 검색, 오선지 만들기, 필기·기본 기호, 폴더·셋리스트·PDF 합치기, 메트로놈, 서재 백업 등</li>
<li><strong>Pro 기능:</strong> 배너 없음, 사진 스캔 PDF 공유 시 하단 문구 없음, 나만의 펜, 추가 기호, 반복·D.C. 연결, 페이지 편집, 필기 포함 PDF 내보내기와 앞으로 Pro에 추가되는 기능</li>
<li>무료 버전에는 같은 회사 서비스 welegato를 알리는 배너가 표시됩니다.</li>
</ol>"""),
   ("Pro 이용권과 무료 체험", """<ol>
<li>앱을 처음 설치하면 <strong>7일 동안</strong> Pro 기능을 무료로 쓸 수 있습니다. 체험이 끝나면 자동으로 무료 버전으로 돌아가며, 자동 결제는 없습니다.</li>
<li>체험 중에 만든 필기·기호·연결·페이지는 체험이 끝난 뒤에도 그대로 남습니다.</li>
<li>Pro는 Google Play 등 앱 스토어의 인앱 결제로 한 번 구매하는 <strong>평생 이용권</strong>입니다. 가격은 결제 화면에 표시됩니다. 같은 스토어 계정으로 다시 설치하면 “구매 복원”으로 되살릴 수 있습니다.</li>
<li>결제·환불은 각 스토어의 정책에 따릅니다. 디지털 콘텐츠의 특성상, 구매 즉시 이용이 시작되는 데 동의하면 법이 허용하는 범위에서 청약철회권이 소멸할 수 있으며, 이 경우에도 스토어의 환불 절차는 이용할 수 있습니다.</li>
<li>회사는 Pro의 핵심 기능을 정당한 이유 없이 유료 이용자에게서 빼지 않습니다.</li>
</ol>"""),
   ("악보와 저작권", """<ol>
<li>이용자가 앱에 가져오거나 스캔·공유하는 악보에 대한 저작권 준수는 이용자의 책임입니다.</li>
<li>IMSLP의 악보는 IMSLP가 정한 조건으로 제공되며, 저작권 보호 기간은 나라마다 다릅니다. 앱은 EU에서 보호될 수 있는 판본에 안내를 표시하지만, 최종 판단은 이용자에게 있습니다.</li>
<li>앱은 이용자의 악보를 회사로 보내지 않으며, 회사는 그 내용을 알지 못합니다.</li>
</ol>"""),
   ("welegato 및 외부 서비스", """<p>앱에는 welegato, IMSLP, Google Play 등 외부 서비스로 가는 링크와 기능이 있습니다. 이 서비스들은 앱과 별개이며 각자의 이용약관과 개인정보처리방침이 적용됩니다. 외부 서비스의 내용과 이용 가능 여부에 대해 회사는 책임지지 않습니다.</p>"""),
   ("지적재산권", """<p>앱의 로고, “Leggii·렛지” 명칭, 디자인, 문구, 소스코드에 대한 권리는 회사에 있습니다. 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다.</p>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 결제를 우회하지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다. 외부 서비스(IMSLP 등)의 변경으로 관련 기능이 제한될 수 있습니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 생명·신체·건강의 침해, 그리고 제조물책임법에 따른 경우에는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>경과실의 경우 회사는 계약상 본질적인 의무를 위반했을 때에만, 계약 체결 시 예견할 수 있었던 통상적인 손해에 한해 책임을 집니다.</li>
<li>악보와 필기는 기기에만 저장됩니다. 기기 분실·앱 삭제·초기화로 인한 손실에 대비해 “서재 백업하기”로 직접 백업해 주세요.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _contact("운영자")),
  ],
 },
 "en": {
  "title": "Leggii Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-10-22"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "These terms are the agreement between you and Vicino Labs for using Leggii, a sheet music app. By installing and using the app you agree to them.",
  "footer": "These terms are effective from 22 October 2026 (version 1.0).",
  "other": "Privacy Policy →",
  "sections": [
   ("Scope", "<p>These terms govern the use of the mobile app Leggii (the “app”) provided by Vicino Labs (the “company”).</p>"),
   ("Provider", _id_card("en")),
   ("Validity and changes", """<ol>
<li>These terms take effect when published in the app or in another way chosen by the company.</li>
<li>The company may change them within the law and will announce the effective date and reason in advance.</li>
<li>If you do not agree to changed terms, you may stop using and delete the app.</li>
</ol>"""),
   ("What the app offers", """<ol>
<li><strong>Free:</strong> reading PDF scores and turning pages (including pedals), importing, photo scans, IMSLP search, staff paper, notes and basic symbols, folders, setlists, merging PDFs, metronome, library backup and more</li>
<li><strong>Pro:</strong> no banner, no credit line on shared photo scans, your own pens, more symbols, repeat and D.C. jumps, page editing, PDF export with notes, and Pro features added later</li>
<li>The free version shows a banner for welegato, a service of the same company.</li>
</ol>"""),
   ("Pro and the free trial", """<ol>
<li>After first installing the app you can use every Pro feature free for <strong>7 days</strong>. The app then returns to the free version on its own; nothing is charged automatically.</li>
<li>Notes, symbols, links and pages made during the trial stay after it ends.</li>
<li>Pro is a <strong>lifetime licence</strong> bought once through the app store's in-app purchase (e.g. Google Play). The price is shown at checkout. On reinstall with the same store account, use “Restore purchase”.</li>
<li>Payments and refunds follow the store's policies. For digital content, if you agree that use begins immediately after purchase, your right of withdrawal may expire as far as the law allows; the store's refund process remains available.</li>
<li>The company will not remove core Pro features from paying users without good reason.</li>
</ol>"""),
   ("Scores and copyright", """<ol>
<li>You are responsible for respecting copyright in the scores you import, scan or share.</li>
<li>Scores from IMSLP are provided on IMSLP's terms, and copyright terms differ by country. The app flags editions that may still be protected in the EU, but the final judgement is yours.</li>
<li>The app does not send your scores to the company, and the company does not know their contents.</li>
</ol>"""),
   ("welegato and external services", """<p>The app links to and uses external services such as welegato, IMSLP and Google Play. They are separate from the app and governed by their own terms and privacy policies. The company is not responsible for their content or availability.</p>"""),
   ("Intellectual property", """<p>The company holds the rights to the app's logo, the name “Leggii”, its design, texts and source code. You may not copy, distribute, transmit, publish, reverse-engineer or create derivative works without prior written consent.</p>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the app or circumvent payment.</li>
<li>Do not disrupt the app's normal operation.</li>
<li>Comply with applicable law and these terms.</li>
</ol>"""),
   ("Changes and discontinuation", """<p>The company may change or discontinue all or part of the app for operational or technical reasons and will announce this in advance unless urgent. Changes to external services (such as IMSLP) may limit related features.</p>"""),
   ("Liability", """<ol>
<li>The company is liable without limitation for intent and gross negligence, for injury to life, body or health, and under the Product Liability Act.</li>
<li>For slight negligence the company is liable only for breach of essential contractual obligations, limited to the typical damage foreseeable when the contract was made.</li>
<li>Scores and notes are stored only on your device. To protect against loss of the device, deletion or reset, please make your own backups with “Back up library”.</li>
</ol>"""),
   ("Governing law and jurisdiction", """<p>German law applies. Mandatory consumer-protection rules of the country where you, as a consumer, habitually reside (e.g. an EU member state) remain unaffected. Otherwise the courts at the company's seat (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For questions about these terms, please contact us.</p>" + _contact("Operator")),
  ],
 },
 "de": {
  "title": "Leggii Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "22.10.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln die Nutzung von Leggii, einer Noten-App von Vicino Labs. Mit Installation und Nutzung der App stimmst du ihnen zu.",
  "footer": "Diese Bedingungen gelten ab dem 22. Oktober 2026 (Version 1.0).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Geltungsbereich", "<p>Diese Bedingungen regeln die Nutzung der mobilen App Leggii („App“) von Vicino Labs („Anbieter“).</p>"),
   ("Anbieter", _id_card("de")),
   ("Geltung und Änderungen", """<ol>
<li>Die Bedingungen gelten ab Veröffentlichung in der App oder auf andere vom Anbieter gewählte Weise.</li>
<li>Der Anbieter kann sie im Rahmen des Gesetzes ändern und kündigt Datum und Grund vorher an.</li>
<li>Wenn du geänderten Bedingungen nicht zustimmst, kannst du die App nicht mehr nutzen und löschen.</li>
</ol>"""),
   ("Leistungen", """<ol>
<li><strong>Kostenlos:</strong> PDF-Noten lesen und blättern (auch mit Pedal), Import, Foto-Scans, IMSLP-Suche, Notenpapier, Notizen und Grundzeichen, Ordner, Setlisten, PDFs zusammenfügen, Metronom, Bibliothekssicherung u. a.</li>
<li><strong>Pro:</strong> kein Banner, keine Hinweiszeile in geteilten Foto-Scans, eigene Stifte, weitere Zeichen, Wiederholungs- und D.C.-Sprünge, Seitenbearbeitung, PDF-Export mit Notizen sowie später hinzukommende Pro-Funktionen</li>
<li>Die kostenlose Version zeigt ein Banner für welegato, einen Dienst desselben Anbieters.</li>
</ol>"""),
   ("Pro und kostenlose Testphase", """<ol>
<li>Nach der ersten Installation kannst du alle Pro-Funktionen <strong>7 Tage</strong> kostenlos nutzen. Danach kehrt die App von selbst zur kostenlosen Version zurück; es wird nichts automatisch berechnet.</li>
<li>In der Testphase erstellte Notizen, Zeichen, Sprünge und Seiten bleiben danach erhalten.</li>
<li>Pro ist eine <strong>dauerhafte Lizenz</strong>, die einmalig per In-App-Kauf im App-Store (z. B. Google Play) erworben wird. Der Preis wird beim Kauf angezeigt. Nach Neuinstallation mit demselben Store-Konto stellst du sie mit „Kauf wiederherstellen“ wieder her.</li>
<li>Zahlung und Erstattung richten sich nach den Regeln des Stores. Bei digitalen Inhalten kann das Widerrufsrecht erlöschen, wenn du zustimmst, dass die Nutzung sofort nach dem Kauf beginnt; das Erstattungsverfahren des Stores bleibt davon unberührt.</li>
<li>Der Anbieter entzieht zahlenden Nutzern zentrale Pro-Funktionen nicht ohne sachlichen Grund.</li>
</ol>"""),
   ("Noten und Urheberrecht", """<ol>
<li>Für die Einhaltung des Urheberrechts an importierten, gescannten oder geteilten Noten bist du selbst verantwortlich.</li>
<li>Noten von IMSLP werden zu den Bedingungen von IMSLP bereitgestellt; Schutzfristen sind je nach Land verschieden. Die App kennzeichnet Ausgaben, die in der EU noch geschützt sein können, die endgültige Beurteilung liegt aber bei dir.</li>
<li>Die App sendet deine Noten nicht an den Anbieter; der Anbieter kennt ihren Inhalt nicht.</li>
</ol>"""),
   ("welegato und externe Dienste", """<p>Die App verlinkt und nutzt externe Dienste wie welegato, IMSLP und Google Play. Sie sind von der App getrennt; es gelten deren eigene Bedingungen und Datenschutzerklärungen. Für deren Inhalte und Verfügbarkeit ist der Anbieter nicht verantwortlich.</p>"""),
   ("Geistiges Eigentum", """<p>Die Rechte an Logo, dem Namen „Leggii“, Gestaltung, Texten und Quellcode der App liegen beim Anbieter. Ohne vorherige schriftliche Zustimmung sind Vervielfältigung, Verbreitung, Übertragung, Veröffentlichung, Reverse Engineering und Bearbeitungen nicht erlaubt.</p>"""),
   ("Pflichten der Nutzer", """<ol>
<li>Kein Reverse Engineering oder Dekompilieren der App und keine Umgehung der Bezahlung.</li>
<li>Keine Störung des normalen Betriebs der App.</li>
<li>Einhaltung der Gesetze und dieser Bedingungen.</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Der Anbieter kann Funktionen der App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigt dies, außer in dringenden Fällen, vorher an. Änderungen externer Dienste (z. B. IMSLP) können zugehörige Funktionen einschränken.</p>"""),
   ("Haftung", """<ol>
<li>Der Anbieter haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit sowie nach dem Produkthaftungsgesetz.</li>
<li>Bei leichter Fahrlässigkeit haftet der Anbieter nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den bei Vertragsschluss vorhersehbaren, typischen Schaden.</li>
<li>Noten und Notizen werden nur auf deinem Gerät gespeichert. Sichere sie mit „Bibliothek sichern“ gegen Verlust des Geräts, Löschung oder Zurücksetzen.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt deutsches Recht. Zwingende Verbraucherschutzvorschriften des Staates, in dem du als Verbraucher deinen gewöhnlichen Aufenthalt hast (z. B. ein EU-Mitgliedstaat), bleiben unberührt. Im Übrigen ist Gerichtsstand der Sitz des Anbieters (Dortmund).</p>"""),
   ("Kontakt", "<p>Fragen zu diesen Bedingungen richte bitte an:</p>" + _contact("Betreiber")),
  ],
 },
 "it": {
  "title": "Leggii — Termini di utilizzo",
  "h1": "Termini di utilizzo",
  "meta": [("In vigore dal", "22.10.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Questi termini regolano l'uso di Leggii, un'app per spartiti di Vicino Labs. Installando e usando l'app li accetti.",
  "footer": "Questi termini sono in vigore dal 22 ottobre 2026 (versione 1.0).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>Questi termini regolano l'uso dell'app mobile Leggii (“app”) fornita da Vicino Labs (“fornitore”).</p>"),
   ("Fornitore", _id_card("it")),
   ("Validità e modifiche", """<ol>
<li>I termini sono validi dalla pubblicazione nell'app o in altro modo scelto dal fornitore.</li>
<li>Il fornitore può modificarli nei limiti di legge, comunicando in anticipo data e motivo.</li>
<li>Se non accetti i termini modificati puoi smettere di usare l'app ed eliminarla.</li>
</ol>"""),
   ("Cosa offre l'app", """<ol>
<li><strong>Gratis:</strong> lettura di spartiti PDF e cambio pagina (anche con pedale), importazione, scansioni da foto, ricerca IMSLP, carta pentagrammata, annotazioni e simboli di base, cartelle, scalette, unione di PDF, metronomo, backup della libreria e altro</li>
<li><strong>Pro:</strong> niente banner, nessuna riga di credito sulle scansioni condivise, penne personali, altri simboli, salti per ritornelli e D.C., modifica delle pagine, esportazione PDF con annotazioni e le funzioni Pro future</li>
<li>La versione gratuita mostra un banner di welegato, un servizio dello stesso fornitore.</li>
</ol>"""),
   ("Pro e prova gratuita", """<ol>
<li>Dopo la prima installazione puoi usare tutte le funzioni Pro gratis per <strong>7 giorni</strong>. Poi l'app torna da sola alla versione gratuita; non viene addebitato nulla automaticamente.</li>
<li>Annotazioni, simboli, collegamenti e pagine creati durante la prova restano anche dopo.</li>
<li>Pro è una <strong>licenza a vita</strong> acquistata una sola volta con l'acquisto in-app dello store (es. Google Play). Il prezzo è indicato al momento del pagamento. Dopo una reinstallazione con lo stesso account usa “Ripristina acquisto”.</li>
<li>Pagamenti e rimborsi seguono le regole dello store. Per i contenuti digitali il diritto di recesso può estinguersi, nei limiti di legge, se accetti che l'uso inizi subito dopo l'acquisto; resta disponibile la procedura di rimborso dello store.</li>
<li>Il fornitore non toglie funzioni Pro essenziali agli utenti paganti senza un giustificato motivo.</li>
</ol>"""),
   ("Spartiti e diritto d'autore", """<ol>
<li>Sei responsabile del rispetto del diritto d'autore sugli spartiti che importi, scansioni o condividi.</li>
<li>Gli spartiti di IMSLP sono forniti alle condizioni di IMSLP e la durata della protezione varia da paese a paese. L'app segnala le edizioni che potrebbero essere ancora protette nell'UE, ma la valutazione finale spetta a te.</li>
<li>L'app non invia i tuoi spartiti al fornitore, che non ne conosce il contenuto.</li>
</ol>"""),
   ("welegato e servizi esterni", """<p>L'app collega e usa servizi esterni come welegato, IMSLP e Google Play. Sono separati dall'app e regolati dai propri termini e informative. Il fornitore non risponde del loro contenuto o della loro disponibilità.</p>"""),
   ("Proprietà intellettuale", """<p>I diritti su logo, nome “Leggii”, grafica, testi e codice sorgente dell'app appartengono al fornitore. Senza consenso scritto preventivo non è consentito copiare, distribuire, trasmettere, pubblicare, decompilare o creare opere derivate.</p>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare o analizzare l'app né aggirare il pagamento.</li>
<li>Non ostacolare il normale funzionamento dell'app.</li>
<li>Rispettare la legge e questi termini.</li>
</ol>"""),
   ("Modifica e sospensione", """<p>Il fornitore può modificare o sospendere in tutto o in parte le funzioni dell'app per motivi organizzativi o tecnici, avvisando prima salvo urgenza. Cambiamenti dei servizi esterni (come IMSLP) possono limitare le funzioni collegate.</p>"""),
   ("Responsabilità", """<ol>
<li>Il fornitore risponde senza limiti per dolo e colpa grave, per danni alla vita, al corpo o alla salute e ai sensi della legge sulla responsabilità del produttore.</li>
<li>Per colpa lieve risponde solo in caso di violazione di obblighi contrattuali essenziali, nei limiti del danno tipico prevedibile alla conclusione del contratto.</li>
<li>Spartiti e annotazioni sono salvati solo sul dispositivo. Fai i tuoi backup con “Backup della libreria” contro perdita del dispositivo, cancellazione o ripristino.</li>
</ol>"""),
   ("Legge applicabile e foro", """<p>Si applica la legge tedesca. Restano salve le norme imperative a tutela dei consumatori del paese in cui risiedi abitualmente (ad es. uno Stato UE). Per il resto è competente il foro della sede del fornitore (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande su questi termini scrivici:</p>" + _contact("Gestore")),
  ],
 },
}
