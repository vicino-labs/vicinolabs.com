"""Pianino 개인정보처리방침 본문 (ko/en/de/it) — pianino_legal.py가 HTML로 만든다.

2026-11-07 버전 1.0 초안. 앱은 인터넷에 연결하지 않는다(Android INTERNET 권한 없음,
서버·계정·분석·광고 네트워크 없음). 마이크는 튜너에서만, 기기 안에서 실시간으로 음높이만
계산하고 녹음·저장·전송하지 않는다. 광고는 welegato 자체 배너 하나뿐(Play "광고 포함").
"""

from appoggio_privacy_content import EMAIL, WELEGATO_PRIVACY, _id_card


# Like welegato (the user's wish): the owner's name and address are not shown
# at the top; the first section points to the card at the end and the Impressum.
_OP_REF = {
    "ko": '운영자의 주소와 연락처는 <a href="#ko-12">이 문서 맨 아래</a>와 <a href="/impressum/">Impressum</a>에 있습니다.',
    "en": 'The operator\'s address and contact details are at <a href="#en-12">the end of this document</a> and in the <a href="/impressum/">Impressum</a>.',
    "de": 'Anschrift und Kontaktdaten des Anbieters finden Sie <a href="#de-12">am Ende dieses Dokuments</a> und im <a href="/impressum/">Impressum</a>.',
    "it": 'Indirizzo e contatti del gestore si trovano <a href="#it-12">alla fine di questo documento</a> e nell\'<a href="/impressum/">Impressum</a>.',
}


def _op_ref(lang):
    return f'<p class="op-ref">{_OP_REF[lang]}</p>'


PRIVACY = {
 "ko": {
  "title": "Pianino 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.11.07"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "Vicino Labs가 만든 피아노·메트로놈·튜너 앱 Pianino는 개인정보를 수집하지 않습니다. 회원가입도, 광고 네트워크도, 결제도, 서버도 없습니다. 튜너가 쓰는 마이크 소리는 기기 안에서 음높이를 재는 데만 쓰이고 녹음되거나 전송되지 않습니다. 아래에 그 내용을 정확하게 적어 둡니다.",
  "footer": "본 방침은 2026년 11월 7일부터 시행됩니다 (버전 1.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _op_ref("ko") + "<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>회원가입·로그인이 없습니다. 설정은 <strong>기기 안에만</strong> 저장되고, 저희는 이를 볼 수 없습니다.</li>
<li><strong>마이크</strong>는 튜너 화면에서 듣기를 켰을 때만 쓰입니다. 소리는 기기 안에서 실시간으로 음높이만 계산하고 바로 버려지며, <strong>녹음·저장·전송되지 않습니다</strong>.</li>
<li><strong>광고 네트워크와 인앱결제가 없습니다.</strong> 앱에 표시되는 광고는 같은 회사 서비스 welegato를 알리는 자체 배너 하나뿐입니다. 광고 식별자, 분석·추적 도구도 없습니다.</li>
<li>앱은 스스로 인터넷에 연결하지 않습니다. welegato 배너, “함께 쓰면 좋은 앱”, 약관 링크를 <strong>누를 때만</strong> 브라우저나 스토어가 열립니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>피아노 설정 — 피아노 소리, 기준음(A4), 건반 수·줄 수·건반 이름 표시, 보이는 음역</li>
<li>메트로놈 설정 — 템포, 박자, 클릭 소리, 강세, 세분박</li>
<li>튜너 설정 — 이조 악기 표시</li>
<li>화면 설정 — 언어, 음이름 방식, 화면 모드, 테마 색상</li>
</ul>
<p>이 정보는 기기 안의 앱 전용 저장소에만 있고 저희에게 전송되지 않습니다. 앱을 삭제하면 함께 지워집니다. 처리 근거: 앱 기능 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("마이크(튜너)", """<p>튜너 화면에서 처음 듣기를 켜면 앱이 기기의 <strong>마이크 권한</strong>을 요청합니다.</p>
<ul>
<li>마이크 소리는 기기 메모리 안에서 몇 분의 1초 단위로 음높이(주파수)를 계산하는 데만 쓰이고 곧바로 덮어써집니다. 화면의 음높이 그래프도 최근 몇 초의 음높이 값만 기억하며, 튜너를 떠나면 지워집니다.</li>
<li>소리 자체를 파일로 녹음하거나 저장하지 않고, 어디로도 보내지 않습니다. 앱에는 인터넷 권한이 없습니다.</li>
<li>튜너 화면을 떠나거나 앱이 백그라운드로 가면 마이크를 끕니다.</li>
<li>권한은 기기 설정에서 언제든 끌 수 있습니다. 끄면 튜너의 듣기 기능만 쓸 수 없고, 피아노·메트로놈·기준음 듣기는 그대로 쓸 수 있습니다.</li>
</ul>"""),
   ("소리·백그라운드 재생·화면 켜짐", """<p>피아노 소리와 메트로놈 클릭은 앱에 들어 있는 음원으로 기기 안에서 만들어집니다. 메트로놈은 다른 앱으로 넘어가거나 화면을 꺼도 계속 울릴 수 있고(iOS 백그라운드 오디오), 튜너가 듣는 동안에는 화면이 꺼지지 않습니다. 이 기능들은 모두 기기 안에서만 동작하며 어떤 정보도 보내지 않습니다.</p>"""),
   ("welegato 배너와 외부 링크", f"""<p>화면 아래에는 같은 회사(Vicino Labs)가 운영하는 음악 레슨 플랫폼 <strong>welegato</strong>를 안내하는 배너가 있고, 설정에는 같은 회사의 다른 앱을 소개하는 “함께 쓰면 좋은 앱”이 있습니다. 이를 <strong>누를 때만</strong> 기기의 브라우저나 앱 스토어가 열리며, 앱은 그 전에도 그 후에도 어떤 개인정보도 전달하지 않습니다.</p>
<ul>
<li>링크 주소에는 “Pianino에서 왔다”는 것만 알려주는 캠페인 표시(<code>utm_source=pianino</code>)가 붙습니다. 이용자를 식별하는 값은 들어 있지 않습니다.</li>
<li>웹사이트나 스토어가 열린 뒤에는 그쪽의 개인정보처리방침이 적용됩니다 — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato 개인정보처리방침</a>, 이 사이트(vicinolabs.com)는 <a href="/datenschutz/">Datenschutz</a>.</li>
<li>웹사이트를 여는 순간, 인터넷 연결의 특성상 기기의 IP 주소가 해당 사이트의 서버(호스팅 업체)에 전달됩니다.</li>
</ul>"""),
   ("앱 스토어", """<p>앱은 Google Play와 Apple App Store를 통해 배포됩니다. 설치·업데이트·충돌 보고 등은 각 스토어가 자체 개인정보처리방침에 따라 처리하며, 저희는 스토어가 제공하는 익명 통계(설치 수, 충돌 건수 등)만 볼 수 있습니다.</p>"""),
   ("수집하지 않는 정보", """<p>이름, 이메일, 전화번호, 위치, 연락처, 사진, 카메라, 녹음된 소리, 광고 식별자, 기기 식별자를 수집하지 않습니다. 앱에는 Android 인터넷 권한도 없습니다.</p>"""),
   ("아동", """<p>앱은 개인정보를 수집하지 않으므로 연령에 따른 별도의 제한이 없습니다.</p>"""),
   ("정보주체의 권리", """<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리 — 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>저희는 이용자의 정보를 갖고 있지 않으므로, 기기 안의 설정은 앱 삭제로 직접 지울 수 있습니다. 궁금한 점은 아래로 연락해 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 본 방침을 고칠 수 있습니다. 변경 내용과 시행일은 이 페이지에 게시합니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Pianino Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-11-07"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "Pianino, a piano, metronome and tuner app made by Vicino Labs, does not collect personal data. There is no account, no ad network, no purchase and no server. The microphone sound the tuner uses only serves to measure pitch on your device; it is never recorded or sent anywhere. Here are the details, as precisely as we can put them.",
  "footer": "This policy is effective from 7 November 2026 (version 1.0).",
  "other": "Terms of Service →",
  "sections": [
   ("Data controller", _op_ref("en") + "<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for any personal data processed in connection with this app.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>No account or sign-in. Your settings are stored <strong>only on your device</strong> — we cannot see them.</li>
<li>The <strong>microphone</strong> is used only while listening is on in the tuner. The sound is analysed on the device in real time for its pitch and then discarded — it is <strong>never recorded, stored or sent</strong>.</li>
<li><strong>No ad networks and no in-app purchases.</strong> The only ad in the app is our own banner for welegato, a service of the same company. No advertising ID, and no analytics or tracking tools.</li>
<li>The app does not connect to the internet by itself. Your browser or app store opens <strong>only when you tap</strong> the welegato banner, “More apps for musicians” or a link to our legal documents.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>Piano settings — piano sound, concert pitch (A4), number of keys and rows, key labels, visible range</li>
<li>Metronome settings — tempo, metre, click sound, accents, subdivision</li>
<li>Tuner settings — transposing instrument</li>
<li>Display settings — language, note-name system, appearance, colour theme</li>
</ul>
<p>This data stays in the app's private storage on your device and is never sent to us. It is deleted when you uninstall the app. Legal basis: providing the app's features (Art. 6(1)(b) GDPR).</p>"""),
   ("Microphone (tuner)", """<p>The first time you turn on listening in the tuner, the app asks for your device's <strong>microphone permission</strong>.</p>
<ul>
<li>The microphone sound is used only to calculate the pitch (frequency) in the device's memory, a fraction of a second at a time, and is overwritten straight away. The pitch graph on screen keeps only the pitch values of the last few seconds and is cleared when you leave the tuner.</li>
<li>The sound itself is never recorded to a file, stored or sent anywhere. The app does not have the internet permission.</li>
<li>The microphone is switched off when you leave the tuner or the app goes to the background.</li>
<li>You can revoke the permission in your device settings at any time. Only the tuner's listening stops working; the piano, the metronome and the reference tones still work.</li>
</ul>"""),
   ("Sound, background playback and screen", """<p>Piano sounds and metronome clicks are generated on the device from sound samples included in the app. The metronome can keep playing when you switch apps or turn off the screen (iOS background audio), and the screen stays on while the tuner is listening. All of this works entirely on the device and sends no data.</p>"""),
   ("The welegato banner and external links", f"""<p>At the bottom of the screen there is a banner for <strong>welegato</strong>, a music-lesson platform run by the same company (Vicino Labs), and the settings show “More apps for musicians” from the same company. Your browser or app store opens <strong>only when you tap</strong> one of them; the app does not pass on any personal data, before or after.</p>
<ul>
<li>The link carries a campaign tag (<code>utm_source=pianino</code>) that only says the visit came from Pianino. It contains no value that identifies you.</li>
<li>Once a website or store page is open, its own privacy policy applies — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato privacy policy</a>; for this site (vicinolabs.com) see <a href="/datenschutz/">Datenschutz</a>.</li>
<li>As with any website visit, your device's IP address reaches that site's server (hosting provider) when the page loads.</li>
</ul>"""),
   ("App stores", """<p>The app is distributed through Google Play and the Apple App Store. Installs, updates and crash reports are handled by the store under its own privacy policy; we only see anonymous statistics the store provides (such as install and crash counts).</p>"""),
   ("Data we don't collect", """<p>We do not collect names, email addresses, phone numbers, location, contacts, photos, camera data, recorded sound, advertising IDs or device identifiers. The Android app does not even have the internet permission.</p>"""),
   ("Children", """<p>Because the app collects no personal data, there is no age restriction for privacy reasons.</p>"""),
   ("Your rights", """<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR)</li>
<li>Lodge a complaint with a supervisory authority — e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live</li>
</ul>
<p>We hold no data about you; the settings on your device are deleted when you uninstall the app. For any question, please contact us below.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law or the app changes; changes and the effective date are posted on this page.</p>"""),
   ("Contact", "<p>For questions about data processing, please contact:</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Pianino Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "07.11.2026"), ("Version", "1.0"), ("Anbieter", "Vicino Labs")],
  "lede": "Pianino, eine App mit Klavier, Metronom und Stimmgerät von Vicino Labs, erhebt keine personenbezogenen Daten. Es gibt kein Konto, kein Werbenetzwerk, keine Käufe und keinen Server. Der Mikrofonton des Stimmgeräts dient nur dazu, auf Ihrem Gerät die Tonhöhe zu messen; er wird nie aufgenommen oder übertragen. Hier die Einzelheiten.",
  "footer": "Diese Erklärung gilt ab dem 7. November 2026 (Version 1.0).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _op_ref("de") + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für eine etwaige Verarbeitung personenbezogener Daten im Zusammenhang mit dieser App.</p>"),
   ("Das Wichtigste in Kürze", """<div class="summary-box"><ul>
<li>Kein Konto, keine Anmeldung. Ihre Einstellungen werden <strong>nur auf Ihrem Gerät</strong> gespeichert — wir können sie nicht einsehen.</li>
<li>Das <strong>Mikrofon</strong> wird nur verwendet, solange im Stimmgerät das Zuhören eingeschaltet ist. Der Ton wird auf dem Gerät in Echtzeit auf seine Tonhöhe ausgewertet und sofort verworfen — er wird <strong>nie aufgenommen, gespeichert oder übertragen</strong>.</li>
<li><strong>Keine Werbenetzwerke und keine In-App-Käufe.</strong> Die einzige Werbung in der App ist unser eigenes Banner für welegato, einen Dienst desselben Anbieters. Keine Werbe-ID, keine Analyse- oder Tracking-Dienste.</li>
<li>Die App verbindet sich nicht selbst mit dem Internet. Browser oder App-Store öffnen sich <strong>nur, wenn Sie</strong> auf das welegato-Banner, „Weitere Apps für Musiker“ oder einen Link zu unseren Rechtstexten <strong>tippen</strong>.</li>
</ul></div>"""),
   ("Auf Ihrem Gerät gespeicherte Daten", """<ul>
<li>Klavier — Klang, Kammerton (A4), Anzahl der Tasten und Reihen, Tastenbeschriftung, sichtbarer Tonumfang</li>
<li>Metronom — Tempo, Takt, Klickton, Betonungen, Unterteilung</li>
<li>Stimmgerät — transponierendes Instrument</li>
<li>Anzeige — Sprache, Notennamen, Darstellung, Farbthema</li>
</ul>
<p>Diese Daten bleiben im privaten Speicher der App auf Ihrem Gerät und werden nicht an uns übertragen. Beim Deinstallieren der App werden sie gelöscht. Rechtsgrundlage: Bereitstellung der App-Funktionen (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Mikrofon (Stimmgerät)", """<p>Wenn Sie im Stimmgerät zum ersten Mal das Zuhören einschalten, fragt die App nach der <strong>Mikrofonberechtigung</strong>.</p>
<ul>
<li>Der Mikrofonton dient nur dazu, im Arbeitsspeicher des Geräts in Bruchteilen einer Sekunde die Tonhöhe (Frequenz) zu berechnen, und wird sofort überschrieben. Die Tonhöhenkurve auf dem Bildschirm merkt sich nur die Tonhöhenwerte der letzten Sekunden und wird beim Verlassen des Stimmgeräts gelöscht.</li>
<li>Der Ton selbst wird nie als Datei aufgenommen, gespeichert oder irgendwohin übertragen. Die App hat keine Internet-Berechtigung.</li>
<li>Das Mikrofon wird ausgeschaltet, wenn Sie das Stimmgerät verlassen oder die App in den Hintergrund geht.</li>
<li>Sie können die Berechtigung jederzeit in den Geräteeinstellungen entziehen. Dann funktioniert nur das Zuhören des Stimmgeräts nicht mehr; Klavier, Metronom und Referenztöne bleiben nutzbar.</li>
</ul>"""),
   ("Ton, Wiedergabe im Hintergrund und Bildschirm", """<p>Klavierklänge und Metronom-Klicks werden auf dem Gerät aus Klangproben erzeugt, die in der App enthalten sind. Das Metronom kann weiterspielen, wenn Sie die App wechseln oder den Bildschirm ausschalten (iOS-Hintergrundaudio), und der Bildschirm bleibt an, solange das Stimmgerät zuhört. All das funktioniert ausschließlich auf dem Gerät und übermittelt keine Daten.</p>"""),
   ("welegato-Banner und externe Links", f"""<p>Unten auf dem Bildschirm weist ein Banner auf <strong>welegato</strong> hin, eine Plattform für Musikunterricht desselben Anbieters (Vicino Labs); in den Einstellungen stellt „Weitere Apps für Musiker“ weitere Apps desselben Anbieters vor. Browser oder App-Store öffnen sich <strong>nur, wenn Sie darauf tippen</strong>; die App gibt dabei weder vorher noch nachher personenbezogene Daten weiter.</p>
<ul>
<li>Der Link enthält eine Kampagnenkennung (<code>utm_source=pianino</code>), die nur angibt, dass der Besuch aus Pianino kommt. Sie enthält keinen Wert, der Sie identifiziert.</li>
<li>Sobald eine Website oder Store-Seite geöffnet ist, gilt deren Datenschutzerklärung — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von welegato</a>; für diese Website (vicinolabs.com) siehe <a href="/datenschutz/">Datenschutz</a>.</li>
<li>Wie bei jedem Website-Besuch wird beim Laden der Seite die IP-Adresse Ihres Geräts an den Server (Hoster) dieser Website übermittelt.</li>
</ul>"""),
   ("App-Stores", """<p>Die App wird über Google Play und den Apple App Store vertrieben. Installationen, Updates und Absturzberichte verarbeitet der jeweilige Store nach seiner eigenen Datenschutzerklärung; wir sehen nur anonyme Statistiken des Stores (z. B. Installations- und Absturzzahlen).</p>"""),
   ("Was wir nicht erheben", """<p>Wir erheben keine Namen, E-Mail-Adressen, Telefonnummern, Standortdaten, Kontakte, Fotos, Kameradaten, aufgenommenen Töne, Werbe-IDs oder Gerätekennungen. Die Android-App hat nicht einmal die Internet-Berechtigung.</p>"""),
   ("Kinder", """<p>Da die App keine personenbezogenen Daten erhebt, gibt es aus Datenschutzgründen keine Altersgrenze.</p>"""),
   ("Ihre Rechte", """<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO)</li>
<li>Beschwerde bei einer Aufsichtsbehörde — z. B. der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW) oder der Behörde an Ihrem Wohnort</li>
</ul>
<p>Wir speichern keine Daten über Sie; die Einstellungen auf Ihrem Gerät werden beim Deinstallieren gelöscht. Bei Fragen erreichen Sie uns unten.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich Recht oder App ändern; Änderungen und Gültigkeitsdatum veröffentlichen wir auf dieser Seite.</p>"""),
   ("Kontakt", "<p>Für Fragen zur Datenverarbeitung:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Pianino — Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "07/11/2026"), ("Versione", "1.0"), ("Titolare", "Vicino Labs")],
  "lede": "Pianino, l'app con pianoforte, metronomo e accordatore realizzata da Vicino Labs, non raccoglie dati personali. Non ci sono account, reti pubblicitarie, acquisti né server. Il suono del microfono usato dall'accordatore serve solo a misurare l'intonazione sul tuo dispositivo: non viene mai registrato né inviato. Ecco i dettagli.",
  "footer": "La presente informativa è in vigore dal 7 novembre 2026 (versione 1.0).",
  "other": "Termini di servizio →",
  "sections": [
   ("Titolare del trattamento", _op_ref("it") + "<p>Vicino Labs è il titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per gli eventuali dati personali trattati in relazione a questa app.</p>"),
   ("In sintesi", """<div class="summary-box"><ul>
<li>Nessun account né login. Le impostazioni sono salvate <strong>solo sul tuo dispositivo</strong>: noi non possiamo vederle.</li>
<li>Il <strong>microfono</strong> è usato solo mentre l'ascolto dell'accordatore è attivo. Il suono viene analizzato sul dispositivo in tempo reale per ricavarne l'altezza e poi scartato: <strong>non viene mai registrato, salvato né inviato</strong>.</li>
<li><strong>Nessuna rete pubblicitaria e nessun acquisto in-app.</strong> L'unica pubblicità nell'app è il nostro banner per welegato, un servizio della stessa società. Nessun ID pubblicitario, nessuno strumento di analisi o tracciamento.</li>
<li>L'app non si collega a Internet da sola. Il browser o lo store si aprono <strong>solo quando tocchi</strong> il banner di welegato, “Altre app per musicisti” o un link ai nostri documenti legali.</li>
</ul></div>"""),
   ("Dati salvati sul dispositivo", """<ul>
<li>Pianoforte — suono, diapason (La4), numero di tasti e di file, nomi dei tasti, estensione visibile</li>
<li>Metronomo — tempo, metro, suono del clic, accenti, suddivisione</li>
<li>Accordatore — strumento traspositore</li>
<li>Visualizzazione — lingua, nomi delle note, aspetto, tema colore</li>
</ul>
<p>Questi dati restano nella memoria privata dell'app sul dispositivo e non ci vengono mai inviati. Vengono cancellati quando disinstalli l'app. Base giuridica: fornitura delle funzioni dell'app (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Microfono (accordatore)", """<p>La prima volta che attivi l'ascolto nell'accordatore, l'app chiede l'<strong>autorizzazione al microfono</strong>.</p>
<ul>
<li>Il suono del microfono serve solo a calcolare l'altezza (frequenza) nella memoria del dispositivo, una frazione di secondo alla volta, e viene subito sovrascritto. Il grafico dell'intonazione sullo schermo conserva solo i valori degli ultimi secondi e si cancella quando lasci l'accordatore.</li>
<li>Il suono non viene mai registrato in un file, salvato né inviato altrove. L'app non ha l'autorizzazione di accesso a Internet.</li>
<li>Il microfono si spegne quando lasci l'accordatore o l'app passa in background.</li>
<li>Puoi revocare l'autorizzazione dalle impostazioni del dispositivo in qualsiasi momento. Smette di funzionare solo l'ascolto dell'accordatore; pianoforte, metronomo e note di riferimento restano disponibili.</li>
</ul>"""),
   ("Suono, riproduzione in background e schermo", """<p>I suoni del pianoforte e i clic del metronomo sono generati sul dispositivo a partire da campioni sonori inclusi nell'app. Il metronomo può continuare a suonare quando cambi app o spegni lo schermo (audio in background su iOS), e lo schermo resta acceso mentre l'accordatore è in ascolto. Tutto questo funziona solo sul dispositivo e non invia dati.</p>"""),
   ("Il banner di welegato e i link esterni", f"""<p>In fondo allo schermo c'è un banner di <strong>welegato</strong>, una piattaforma di lezioni di musica gestita dalla stessa società (Vicino Labs); nelle impostazioni “Altre app per musicisti” presenta altre app della stessa società. Il browser o lo store si aprono <strong>solo se li tocchi</strong>; l'app non trasmette alcun dato personale, né prima né dopo.</p>
<ul>
<li>Il link contiene un parametro di campagna (<code>utm_source=pianino</code>) che indica soltanto che la visita proviene da Pianino. Non contiene alcun valore che ti identifichi.</li>
<li>Una volta aperto il sito o lo store, si applica la sua informativa — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">informativa privacy di welegato</a>; per questo sito (vicinolabs.com) vedi <a href="/datenschutz/">Datenschutz</a>.</li>
<li>Come per ogni visita a un sito web, al caricamento della pagina l'indirizzo IP del dispositivo raggiunge il server (hosting) di quel sito.</li>
</ul>"""),
   ("App store", """<p>L'app è distribuita tramite Google Play e l'Apple App Store. Installazioni, aggiornamenti e segnalazioni di arresti anomali sono gestiti dallo store secondo la propria informativa; noi vediamo solo statistiche anonime fornite dallo store (ad es. numero di installazioni e di arresti).</p>"""),
   ("Dati che non raccogliamo", """<p>Non raccogliamo nomi, indirizzi e-mail, numeri di telefono, posizione, contatti, foto, dati della fotocamera, suoni registrati, ID pubblicitari o identificativi del dispositivo. L'app Android non ha nemmeno l'autorizzazione di accesso a Internet.</p>"""),
   ("Minori", """<p>Poiché l'app non raccoglie dati personali, non ci sono limiti di età per motivi di privacy.</p>"""),
   ("I tuoi diritti", """<ul>
<li>Accesso, rettifica, cancellazione, limitazione del trattamento, portabilità e opposizione (artt. 15–21 GDPR)</li>
<li>Reclamo a un'autorità di controllo — ad es. l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o il Garante del tuo paese di residenza</li>
</ul>
<p>Non conserviamo dati su di te; le impostazioni sul dispositivo si cancellano disinstallando l'app. Per qualsiasi domanda, contattaci qui sotto.</p>"""),
   ("Modifiche", """<p>Potremo aggiornare questa informativa in caso di modifiche normative o dell'app; modifiche e data di entrata in vigore saranno pubblicate in questa pagina.</p>"""),
   ("Contatti", "<p>Per domande sul trattamento dei dati:</p>" + _id_card("it")),
  ],
 },
}
