"""Pianino 이용약관 본문 (ko/en/de/it) — pianino_legal.py가 HTML로 만든다.

2026-11-07 버전 1.0 초안. Appoggio 약관 틀을 따른다: 무료 앱이라 책임은 고의·중과실과
생명·신체·건강 침해에 한정(독일법상 그 이상은 제한 불가). Pianino 고유 조항: 튜너·기준음
정확도 안내, 음량(청력) 안내, 앱에 든 피아노 음원의 라이선스.
"""

from appoggio_privacy_content import _id_card
from pianino_privacy_content import _op_ref

TERMS = {
 "ko": {
  "title": "Pianino 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.11.07"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 만든 피아노·메트로놈·튜너 앱 Pianino를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 2026년 11월 7일부터 시행됩니다 (버전 1.0).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 Pianino(이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _op_ref("ko")),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li>피아노 — 가로 화면 건반, 페달, 여러 피아노 소리, 한두 줄 건반</li>
<li>메트로놈 — 템포, 박자, 강세, 세분박, 탭 템포</li>
<li>튜너 — 노래와 모든 악기의 음높이 측정, 음높이 그래프, 기준음 듣기, 이조 악기 표시</li>
<li>피아노와 튜너가 함께 쓰는 기준음(A4) 설정, 음이름 방식, 8개 언어, 화면 모드, 테마 색상</li>
</ol>
<p>앱은 <strong>모든 기능을 무료로</strong> 제공하며 인앱결제가 없습니다. 화면 아래에는 같은 회사 서비스인 welegato를 알리는 배너가 표시됩니다.</p>"""),
   ("정확도와 소리에 관한 안내", """<ol>
<li>튜너와 기준음은 연습을 위한 도구입니다. 회사는 정확하게 만들려고 노력하지만, 측정값은 기기의 마이크·스피커, 주변 소음, 소리의 성질에 따라 달라질 수 있습니다. 악기 조율이나 녹음처럼 정확도가 중요한 경우에는 결과를 직접 확인해 주세요.</li>
<li>이어폰이나 헤드폰으로 들을 때는 적당한 음량으로 들어 청력을 보호하세요.</li>
</ol>"""),
   ("welegato 및 외부 웹사이트", """<p>앱에는 같은 회사가 운영하는 음악 레슨 플랫폼 welegato로 가는 안내 배너와 같은 회사의 다른 앱을 소개하는 링크가 있습니다. welegato, 앱 스토어와 그 밖의 외부 웹사이트는 앱과 별개의 서비스이며, 각자의 이용약관과 개인정보처리방침이 적용됩니다.</p>"""),
   ("지적재산권", """<ol>
<li>앱의 로고, “Pianino” 명칭과 아이콘, 디자인, 문구, 소스코드에 대한 권리는 회사에 있습니다. 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다.</li>
<li>앱에 들어 있는 피아노 음원 일부는 제3자가 공개한 음원(Creative Commons Attribution 3.0, CC0, 퍼블릭 도메인)을 회사가 다듬은 것이며, 각 원저작자와 라이선스는 앱의 설정 › 음원·라이선스에 적혀 있습니다. 그 음원에는 해당 라이선스가 적용됩니다.</li>
<li>이용자가 앱으로 연주하거나 연습한 내용은 이용자의 것입니다. 앱은 이를 녹음하거나 저장하지 않습니다.</li>
</ol>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 소스코드를 추출하지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 그리고 생명·신체·건강의 침해에 대해서는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>앱은 무료로 제공되므로, 그 밖의 경우 회사의 책임은 법이 허용하는 범위에서 제외됩니다.</li>
<li>설정은 기기에만 저장됩니다. 기기 분실·앱 삭제·초기화로 설정이 없어질 수 있습니다.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Pianino Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-11-07"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "These Terms set out the agreement between you and us for using Pianino, a piano, metronome and tuner app made by Vicino Labs. By installing and using the app, you agree to what follows.",
  "footer": "These Terms are effective from 7 November 2026 (version 1.0).",
  "other": "Privacy Policy →",
  "sections": [
   ("Purpose", "<p>These Terms govern the rights and obligations between Vicino Labs (“we”, “us”) and users of the mobile app Pianino (the “App”).</p>"),
   ("About the operator", _op_ref("en")),
   ("Effect and changes", """<ol>
<li>These Terms take effect once posted in the App or by another method we designate.</li>
<li>We may amend these Terms within the limits of applicable law and will announce the effective date and the reason in advance.</li>
<li>If you don't agree to amended Terms, you may stop using the App and delete it.</li>
</ol>"""),
   ("The service", """<ol>
<li>Piano — landscape keyboard, sustain pedal, several piano sounds, one or two rows of keys</li>
<li>Metronome — tempo, metre, accents, subdivision, tap tempo</li>
<li>Tuner — pitch detection for voices and all instruments, pitch graph, reference tones, transposing instruments</li>
<li>One concert-pitch (A4) setting shared by piano and tuner, note-name systems, eight languages, appearance and colour themes</li>
</ol>
<p>The App provides <strong>all features free of charge</strong>, with no in-app purchases. A banner for welegato, a service of the same company, is shown at the bottom of the screen.</p>"""),
   ("Accuracy and sound", """<ol>
<li>The tuner and reference tones are practice tools. We work to make them accurate, but readings can vary with your device's microphone and speaker, background noise and the nature of the sound. Where accuracy matters, such as tuning an instrument or recording, please check the result yourself.</li>
<li>When listening through earphones or headphones, keep the volume moderate to protect your hearing.</li>
</ol>"""),
   ("welegato and external websites", """<p>The App contains a banner linking to welegato, a music-lesson platform run by the same company, and links to our other apps. welegato, the app stores and any other external website are separate services from the App; their own terms and privacy policies apply.</p>"""),
   ("Intellectual property", """<ol>
<li>All rights in the App's logo, the “Pianino” name and icon, design, copy and source code belong to us. Without our prior written consent you may not reproduce, distribute, transmit, publish or reverse-engineer them or create derivative works.</li>
<li>Some piano sounds in the App are third-party samples (Creative Commons Attribution 3.0, CC0, public domain) adapted by us; their authors and licences are listed in the App under Settings › Sounds &amp; licences, and those licences apply to them.</li>
<li>What you play or practise with the App is yours. The App does not record or store it.</li>
</ol>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the App or extract its source code.</li>
<li>Do not interfere with the App's normal operation.</li>
<li>Comply with applicable law and these Terms.</li>
</ol>"""),
   ("Changes and discontinuation", """<p>We may change or discontinue all or part of the App for operational or technical reasons and will announce this in advance except in urgent cases.</p>"""),
   ("Liability", """<ol>
<li>We are liable without limitation, in accordance with the law, for intent and gross negligence and for injury to life, body or health.</li>
<li>As the App is provided free of charge, our liability is otherwise excluded to the extent permitted by law.</li>
<li>Your settings are stored only on your device and may be lost if the device is lost, the App is uninstalled or the device is reset.</li>
</ol>"""),
   ("Governing law and venue", """<p>These Terms are governed by the laws of the Federal Republic of Germany. This does not affect mandatory consumer-protection rights under the law of your country of habitual residence (for example, an EU member state). Otherwise, the courts at our place of business (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For any question about these Terms, please contact:</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Pianino Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "07.11.2026"), ("Version", "1.0"), ("Anbieter", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln die Nutzung von Pianino, einer App mit Klavier, Metronom und Stimmgerät von Vicino Labs. Mit der Installation und Nutzung der App erklären Sie sich damit einverstanden.",
  "footer": "Diese Bedingungen gelten ab dem 7. November 2026 (Version 1.0).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Gegenstand", "<p>Diese Bedingungen regeln die Rechte und Pflichten zwischen Vicino Labs („wir“) und den Nutzerinnen und Nutzern der mobilen App Pianino („App“).</p>"),
   ("Anbieter", _op_ref("de")),
   ("Geltung und Änderungen", """<ol>
<li>Diese Bedingungen gelten, sobald sie in der App oder auf andere von uns bestimmte Weise veröffentlicht sind.</li>
<li>Wir können sie im Rahmen des geltenden Rechts ändern und kündigen Gültigkeitsdatum und Grund vorher an.</li>
<li>Wenn Sie geänderten Bedingungen nicht zustimmen, können Sie die Nutzung beenden und die App löschen.</li>
</ol>"""),
   ("Leistungen", """<ol>
<li>Klavier — Tastatur im Querformat, Pedal, mehrere Klavierklänge, eine oder zwei Tastenreihen</li>
<li>Metronom — Tempo, Takt, Betonungen, Unterteilung, Tipp-Tempo</li>
<li>Stimmgerät — Tonhöhenerkennung für Stimmen und alle Instrumente, Tonhöhenkurve, Referenztöne, transponierende Instrumente</li>
<li>Ein gemeinsamer Kammerton (A4) für Klavier und Stimmgerät, Notennamen-Systeme, acht Sprachen, Darstellung und Farbthemen</li>
</ol>
<p>Die App bietet <strong>alle Funktionen kostenlos</strong>, ohne In-App-Käufe. Unten auf dem Bildschirm wird ein Banner für welegato, einen Dienst desselben Anbieters, angezeigt.</p>"""),
   ("Genauigkeit und Ton", """<ol>
<li>Stimmgerät und Referenztöne sind Übungshilfen. Wir bemühen uns um Genauigkeit, doch Messwerte können je nach Mikrofon und Lautsprecher des Geräts, Umgebungsgeräuschen und Art des Klangs abweichen. Wo es auf Genauigkeit ankommt, etwa beim Stimmen eines Instruments oder bei Aufnahmen, prüfen Sie das Ergebnis bitte selbst.</li>
<li>Hören Sie über Ohr- oder Kopfhörer mit gemäßigter Lautstärke, um Ihr Gehör zu schützen.</li>
</ol>"""),
   ("welegato und externe Websites", """<p>Die App enthält ein Banner mit Link zu welegato, einer Plattform für Musikunterricht desselben Anbieters, sowie Links zu unseren weiteren Apps. welegato, die App-Stores und andere externe Websites sind von der App getrennte Dienste; es gelten deren eigene Nutzungsbedingungen und Datenschutzerklärungen.</p>"""),
   ("Geistiges Eigentum", """<ol>
<li>Alle Rechte an Logo, Name und Symbol „Pianino“, Design, Texten und Quellcode der App liegen bei uns. Ohne unsere vorherige schriftliche Zustimmung dürfen Sie diese nicht vervielfältigen, verbreiten, übertragen, veröffentlichen, zurückentwickeln oder bearbeiten.</li>
<li>Einige Klavierklänge der App sind von uns bearbeitete Klangproben Dritter (Creative Commons Attribution 3.0, CC0, gemeinfrei); Urheber und Lizenzen stehen in der App unter Einstellungen › Klänge &amp; Lizenzen, und für diese Klänge gelten die jeweiligen Lizenzen.</li>
<li>Was Sie mit der App spielen oder üben, gehört Ihnen. Die App nimmt es weder auf noch speichert sie es.</li>
</ol>"""),
   ("Pflichten der Nutzer", """<ol>
<li>Die App nicht zurückentwickeln oder dekompilieren und keinen Quellcode extrahieren.</li>
<li>Den normalen Betrieb der App nicht stören.</li>
<li>Geltendes Recht und diese Bedingungen einhalten.</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Wir können die App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigen dies, außer in dringenden Fällen, vorher an.</p>"""),
   ("Haftung", """<ol>
<li>Wir haften unbeschränkt nach den gesetzlichen Vorschriften für Vorsatz und grobe Fahrlässigkeit sowie für Schäden aus der Verletzung des Lebens, des Körpers oder der Gesundheit.</li>
<li>Da die App unentgeltlich bereitgestellt wird, ist unsere Haftung im Übrigen ausgeschlossen, soweit gesetzlich zulässig.</li>
<li>Ihre Einstellungen werden nur auf Ihrem Gerät gespeichert und können bei Geräteverlust, Deinstallation oder Zurücksetzen verloren gehen.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt das Recht der Bundesrepublik Deutschland. Zwingende Verbraucherschutzvorschriften Ihres gewöhnlichen Aufenthaltsstaats (z. B. eines EU-Mitgliedstaats) bleiben unberührt. Im Übrigen sind die Gerichte an unserem Sitz (Dortmund) zuständig.</p>"""),
   ("Kontakt", "<p>Bei Fragen zu diesen Bedingungen:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Pianino — Termini di servizio",
  "h1": "Termini di servizio",
  "meta": [("In vigore dal", "07/11/2026"), ("Versione", "1.0"), ("Titolare", "Vicino Labs")],
  "lede": "Questi Termini regolano l'uso di Pianino, l'app con pianoforte, metronomo e accordatore realizzata da Vicino Labs. Installando e utilizzando l'app, accetti quanto segue.",
  "footer": "I presenti Termini sono in vigore dal 7 novembre 2026 (versione 1.0).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>I presenti Termini disciplinano i diritti e gli obblighi tra Vicino Labs (“noi”) e gli utenti dell'app mobile Pianino (l'“App”).</p>"),
   ("Chi siamo", _op_ref("it")),
   ("Efficacia e modifiche", """<ol>
<li>I Termini sono efficaci dalla pubblicazione nell'App o con altra modalità da noi indicata.</li>
<li>Possiamo modificarli nei limiti della legge, comunicando in anticipo la data di efficacia e il motivo.</li>
<li>Se non accetti i Termini modificati, puoi smettere di usare l'App e disinstallarla.</li>
</ol>"""),
   ("Il servizio", """<ol>
<li>Pianoforte — tastiera in orizzontale, pedale di risonanza, diversi suoni di pianoforte, una o due file di tasti</li>
<li>Metronomo — tempo, metro, accenti, suddivisione, tap tempo</li>
<li>Accordatore — rilevamento dell'intonazione per voci e tutti gli strumenti, grafico dell'intonazione, note di riferimento, strumenti traspositori</li>
<li>Un unico diapason (La4) per pianoforte e accordatore, sistemi di nomi delle note, otto lingue, aspetto e temi colore</li>
</ol>
<p>L'App offre <strong>tutte le funzioni gratuitamente</strong>, senza acquisti in-app. In fondo allo schermo è mostrato un banner di welegato, un servizio della stessa società.</p>"""),
   ("Precisione e suono", """<ol>
<li>L'accordatore e le note di riferimento sono strumenti di studio. Ci impegniamo a renderli precisi, ma le misure possono variare con il microfono e l'altoparlante del dispositivo, il rumore ambientale e la natura del suono. Quando la precisione è importante, ad esempio per accordare uno strumento o per una registrazione, verifica tu stesso il risultato.</li>
<li>Se ascolti con auricolari o cuffie, mantieni un volume moderato per proteggere l'udito.</li>
</ol>"""),
   ("welegato e siti esterni", """<p>L'App contiene un banner con un link a welegato, una piattaforma di lezioni di musica gestita dalla stessa società, e link alle nostre altre app. welegato, gli app store e gli altri siti esterni sono servizi distinti dall'App; si applicano i rispettivi termini e informative sulla privacy.</p>"""),
   ("Proprietà intellettuale", """<ol>
<li>Tutti i diritti su logo, nome e icona “Pianino”, design, testi e codice sorgente dell'App appartengono a noi. Senza il nostro previo consenso scritto non è consentito riprodurli, distribuirli, trasmetterli, pubblicarli, decompilarli o crearne opere derivate.</li>
<li>Alcuni suoni di pianoforte dell'App sono campioni di terzi (Creative Commons Attribution 3.0, CC0, pubblico dominio) da noi adattati; autori e licenze sono indicati nell'App in Impostazioni › Suoni e licenze, e a quei suoni si applicano le rispettive licenze.</li>
<li>Ciò che suoni o studi con l'App è tuo. L'App non lo registra né lo salva.</li>
</ol>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare l'App, non effettuarne il reverse engineering e non estrarne il codice sorgente.</li>
<li>Non ostacolare il normale funzionamento dell'App.</li>
<li>Rispettare la legge e i presenti Termini.</li>
</ol>"""),
   ("Modifica e interruzione", """<p>Possiamo modificare o interrompere in tutto o in parte l'App per motivi operativi o tecnici, dandone preavviso salvo casi urgenti.</p>"""),
   ("Responsabilità", """<ol>
<li>Rispondiamo senza limiti, secondo la legge, per dolo e colpa grave e per danni alla vita, al corpo o alla salute.</li>
<li>Poiché l'App è gratuita, per il resto la nostra responsabilità è esclusa nei limiti consentiti dalla legge.</li>
<li>Le impostazioni sono salvate solo sul dispositivo e possono andare perse in caso di smarrimento del dispositivo, disinstallazione o azzeramento.</li>
</ol>"""),
   ("Legge applicabile e foro competente", """<p>Si applica la legge della Repubblica Federale di Germania. Restano salvi i diritti inderogabili dei consumatori previsti dalla legge del paese di residenza abituale (ad es. uno Stato membro dell'UE). Negli altri casi è competente il foro della nostra sede (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande sui presenti Termini:</p>" + _id_card("it")),
  ],
 },
}
