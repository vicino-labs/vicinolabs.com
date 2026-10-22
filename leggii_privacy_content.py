"""Leggii(렛지 악보) 개인정보처리방침 본문 (ko/en/de/it) — leggii_legal.py가 HTML로 만든다.

2026-10-22 버전 1.0 (앱 1.0.0). 회원가입·서버 없음. 악보·필기는 기기 안에만.
인터넷: IMSLP 검색·다운로드(사용자가 할 때만), Google Play 결제, 링크.
글자 인식은 기기 안(Google ML Kit / Apple Vision) — ML Kit가 Google에 익명 진단 정보를 보낼 수 있어 적어 둔다.
안드로이드 자동 백업은 설정만(악보 제외) 사용자의 Google 계정에.
"""

from appoggio_privacy_content import EMAIL, _id_card, _contact

WELEGATO_PRIVACY = "https://welegato.com/legal/"
IMSLP_PRIVACY = "https://imslp.org/wiki/IMSLP:Privacy_Policy"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
MLKIT_TERMS = "https://developers.google.com/ml-kit/terms"

PRIVACY = {
 "ko": {
  "title": "렛지 악보(Leggii) 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.10.22"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "Vicino Labs가 만든 악보 앱 렛지 악보(Leggii)는 회원가입이 없고, 저희 서버도 없습니다. 악보와 필기는 이용자의 기기 안에만 저장되며 저희는 볼 수 없습니다. 아래에 앱이 다루는 정보를 정확하게 적어 둡니다.",
  "footer": "본 방침은 2026년 10월 22일부터 시행됩니다 (버전 1.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _id_card("ko") + "<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>회원가입·로그인이 없고, 저희가 운영하는 서버로 보내는 정보가 없습니다.</li>
<li>가져온 악보(PDF), 필기·기호, 폴더, 셋리스트, 설정은 <strong>기기 안에만</strong> 저장됩니다.</li>
<li>광고 네트워크와 분석·추적 도구가 없습니다. 앱 아래의 배너는 같은 회사 서비스 welegato를 알리는 자체 배너입니다.</li>
<li>인터넷은 이용자가 <strong>IMSLP 검색·다운로드</strong>를 하거나, Pro를 구매하거나, 링크를 누를 때만 씁니다.</li>
<li>사진 스캔과 첫 페이지 글자 인식은 <strong>기기 안에서</strong> 처리되며 사진이 밖으로 나가지 않습니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>이용자가 가져오거나 만든 악보 PDF, 미리보기 이미지</li>
<li>필기·기호·텍스트·반복 연결, 책갈피, 마지막으로 본 페이지</li>
<li>악보 정보(제목, 작곡가, 출판사), 폴더, 즐겨찾기, 셋리스트</li>
<li>설정 — 언어, 펜, 메트로놈, 보기 효과, 무료 체험 시작일, Pro 구매 여부 등</li>
</ul>
<p>이 정보는 기기 안의 앱 전용 저장소에 있고 저희에게 전송되지 않습니다. 앱에서 악보를 지우거나 앱을 삭제하면 사라집니다. “서재 백업하기”로 만든 파일은 이용자가 고른 곳(드라이브, 컴퓨터 등)에만 저장됩니다. 처리 근거: 앱 기능 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("안드로이드 자동 백업", f"""<p>안드로이드에서는 기기의 Google 백업 기능이 켜져 있으면 앱의 <strong>설정</strong>(악보 파일은 제외)이 이용자의 Google 계정에 백업되어, 다시 설치할 때 복원됩니다. 이 백업은 Google이 <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google 개인정보처리방침</a>에 따라 처리하며 저희는 볼 수 없습니다. 기기 설정에서 끌 수 있습니다.</p>"""),
   ("카메라·사진", """<p>“사진으로 PDF 만들기”를 쓸 때만 카메라 권한을 요청하거나 사진을 고르게 합니다. 촬영·선택한 사진은 기기 안에서 PDF로 바뀌며 저희에게 보내지지 않습니다.</p>"""),
   ("글자 인식 (제목·작곡가 자동 채우기)", f"""<p>악보 첫 페이지의 제목과 작곡가를 읽을 때 기기 안의 글자 인식 기능을 씁니다 — 안드로이드는 Google ML Kit, iPhone·iPad는 Apple Vision. 페이지 이미지는 기기 밖으로 나가지 않습니다. 다만 Google ML Kit는 기능 개선·진단을 위해 기기 종류, 앱 버전, 처리 성능 같은 <strong>익명 사용 통계</strong>를 Google에 보낼 수 있습니다(<a href="{MLKIT_TERMS}" target="_blank" rel="noopener">ML Kit 약관</a>). 악보 내용이나 사진은 포함되지 않습니다.</p>"""),
   ("IMSLP 검색·다운로드", f"""<p>“IMSLP”를 고르면 앱이 공개 악보 사이트 IMSLP(imslp.org)에 검색어를 보내 곡과 파일 목록을 받아 오고, 파일을 받을 때는 IMSLP의 다운로드 페이지를 앱 안에서 엽니다. 이때 검색어와 기기의 IP 주소가 IMSLP 서버에 전달되고, IMSLP가 쿠키를 저장할 수 있습니다. 이 처리는 <a href="{IMSLP_PRIVACY}" target="_blank" rel="noopener">IMSLP 개인정보처리방침</a>을 따릅니다. 저희는 검색어나 받은 악보를 알 수 없습니다.</p>"""),
   ("Pro 구매", f"""<p>Pro는 Google Play(앱 스토어) 결제로 구매합니다. 결제와 결제 정보는 스토어가 처리하며, 앱은 구매 여부만 확인해 기기에 기록합니다. 저희는 카드 번호 등 결제 정보를 받지 않습니다. 스토어 처리에는 <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google 개인정보처리방침</a>이 적용됩니다.</p>"""),
   ("welegato 배너와 외부 링크", f"""<p>악보 목록 아래의 배너와 설정의 링크를 <strong>누를 때만</strong> 브라우저나 Google Play로 welegato(같은 회사가 운영하는 음악 플랫폼) 또는 다른 Vicino Labs 앱이 열립니다. 링크에는 “앱에서 왔다”는 표시(<code>utm_source=leggii</code>)만 붙고 이용자를 식별하는 값은 없습니다. 열린 뒤에는 해당 사이트의 방침이 적용됩니다 — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato 개인정보처리방침</a>.</p>
<p>무료 버전에서 사진 스캔 PDF를 공유하면 각 페이지 아래에 “위레가토와 함께하는 렛지 악보 · welegato.com” 문구가 들어갑니다. 이 문구에는 개인정보가 없습니다.</p>"""),
   ("공유·내보내기", """<p>악보를 공유하거나 필기 포함 PDF를 내보내면, 기기의 공유 화면에서 이용자가 고른 앱·사람에게만 파일이 전달됩니다.</p>"""),
   ("수집하지 않는 정보", """<p>이름, 이메일, 전화번호, 위치, 연락처, 마이크, 광고 식별자를 수집하지 않습니다. 블루투스 페달은 키보드처럼 동작하며 별도 권한을 쓰지 않습니다.</p>"""),
   ("아동", """<p>앱은 저희에게 개인정보를 보내지 않으므로 연령에 따른 별도의 제한은 없습니다. 어린이가 IMSLP나 외부 링크를 쓸 때는 보호자가 함께해 주세요.</p>"""),
   ("정보주체의 권리", """<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리 — 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>저희는 이용자의 정보를 갖고 있지 않으므로, 기기 안의 정보는 앱이나 앱 삭제로 직접 지울 수 있습니다. 궁금한 점은 아래로 연락해 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 본 방침을 고칠 수 있으며, 변경 내용과 시행일을 이 페이지에 게시합니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _contact("운영자")),
  ],
 },
 "en": {
  "title": "Leggii Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-10-22"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "Leggii, a sheet music app made by Vicino Labs, has no account and no server of ours. Your scores and notes stay on your device and we cannot see them. Here is exactly what the app handles.",
  "footer": "This policy is effective from 22 October 2026 (version 1.0).",
  "other": "Terms of Service →",
  "sections": [
   ("Data controller", _id_card("en") + "<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for any personal data processed in connection with this app.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>No account or sign-in, and nothing is sent to a server run by us.</li>
<li>Imported scores (PDFs), notes and symbols, folders, setlists and settings are stored <strong>only on your device</strong>.</li>
<li>No ad networks and no analytics or tracking SDKs. The banner at the bottom promotes welegato, a service of the same company.</li>
<li>The internet is used only when you <strong>search or download on IMSLP</strong>, buy Pro, or tap a link.</li>
<li>Photo scans and first-page text recognition are processed <strong>on the device</strong>; your photos never leave it.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>The score PDFs you import or create, and preview images</li>
<li>Notes, symbols, text and repeat links, bookmarks and the last page read</li>
<li>Score details (title, composer, publisher), folders, favourites and setlists</li>
<li>Settings — language, pens, metronome, reading look, start of the free trial, whether Pro was bought, and similar</li>
</ul>
<p>This data stays in the app's private storage and is never sent to us. It is deleted when you remove a score or uninstall the app. A file made with “Back up library” is saved only where you choose (a drive, a computer…). Legal basis: providing the app's features (Art. 6(1)(b) GDPR).</p>"""),
   ("Android backup", f"""<p>On Android, if your device's Google backup is on, the app's <strong>settings</strong> (not your score files) are backed up to your Google account and restored when you reinstall. Google handles this backup under the <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google Privacy Policy</a>; we cannot see it. You can turn it off in your device settings.</p>"""),
   ("Camera and photos", """<p>The app asks for the camera, or lets you pick photos, only when you use “Photos to PDF”. The photos are turned into a PDF on your device and are not sent to us.</p>"""),
   ("Text recognition (title and composer)", f"""<p>To read the title and composer from a score's first page, the app uses on-device text recognition — Google ML Kit on Android, Apple Vision on iPhone and iPad. Page images do not leave the device. Google ML Kit may send Google <strong>anonymous usage statistics</strong> such as device type, app version and performance, for diagnostics and improvement (<a href="{MLKIT_TERMS}" target="_blank" rel="noopener">ML Kit terms</a>). Score content and photos are not included.</p>"""),
   ("IMSLP search and downloads", f"""<p>When you use “IMSLP”, the app sends your search terms to the public sheet music library IMSLP (imslp.org) to get works and file lists, and opens IMSLP's download page inside the app when you download. Your search terms and your device's IP address reach IMSLP's servers, and IMSLP may set cookies. This is governed by the <a href="{IMSLP_PRIVACY}" target="_blank" rel="noopener">IMSLP privacy policy</a>. We do not learn what you search for or download.</p>"""),
   ("Buying Pro", f"""<p>Pro is bought through Google Play (the app store). The store handles the payment and payment data; the app only checks whether Pro was bought and records that on the device. We never receive card numbers or other payment details. The store's processing is covered by the <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google Privacy Policy</a>.</p>"""),
   ("The welegato banner and external links", f"""<p>The banner below the score list and the links in Settings open welegato (a music platform of the same company) or another Vicino Labs app in your browser or Google Play <strong>only when you tap them</strong>. Links carry a tag (<code>utm_source=leggii</code>) that only says the visit came from the app, with no value that identifies you. Once open, that site's policy applies — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato privacy policy</a>.</p>
<p>When you share a photo scan as PDF from the free version, each page carries the line “Leggii Score with welegato · welegato.com”. It contains no personal data.</p>"""),
   ("Sharing and export", """<p>When you share a score or export a PDF with notes, the file goes only to the app or person you pick in your device's share sheet.</p>"""),
   ("Data we don't collect", """<p>We do not collect names, email addresses, phone numbers, location, contacts, microphone data or advertising IDs. Bluetooth page-turn pedals work like a keyboard and need no extra permission.</p>"""),
   ("Children", """<p>Because the app sends no personal data to us, there is no age restriction for privacy reasons. Children should use IMSLP and external links with an adult.</p>"""),
   ("Your rights", """<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR)</li>
<li>Lodge a complaint with a supervisory authority — e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live</li>
</ul>
<p>We hold no data about you; what is on your device you can delete in the app or by uninstalling it. For any question, please contact us below.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law or the app changes; changes and the effective date are posted on this page.</p>"""),
   ("Contact", "<p>For questions about data protection, please contact us.</p>" + _contact("Operator")),
  ],
 },
 "de": {
  "title": "Leggii Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "22.10.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Leggii, eine Noten-App von Vicino Labs, hat kein Konto und keinen Server von uns. Deine Noten und Notizen bleiben auf deinem Gerät, wir können sie nicht sehen. Hier steht genau, welche Daten die App verarbeitet.",
  "footer": "Diese Erklärung gilt ab dem 22. Oktober 2026 (Version 1.0).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _id_card("de") + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für Verarbeitungen im Zusammenhang mit dieser App.</p>"),
   ("Kurzfassung", """<div class="summary-box"><ul>
<li>Kein Konto, keine Anmeldung, keine Übermittlung an einen von uns betriebenen Server.</li>
<li>Importierte Noten (PDF), Notizen und Zeichen, Ordner, Setlisten und Einstellungen werden <strong>nur auf deinem Gerät</strong> gespeichert.</li>
<li>Keine Werbenetzwerke, keine Analyse- oder Tracking-Tools. Das Banner unten wirbt für welegato, einen Dienst desselben Unternehmens.</li>
<li>Das Internet wird nur genutzt, wenn du <strong>bei IMSLP suchst oder herunterlädst</strong>, Pro kaufst oder einen Link antippst.</li>
<li>Foto-Scans und die Texterkennung der ersten Seite laufen <strong>auf dem Gerät</strong>; deine Fotos verlassen es nicht.</li>
</ul></div>"""),
   ("Auf dem Gerät gespeicherte Daten", """<ul>
<li>Von dir importierte oder erstellte Noten-PDFs und Vorschaubilder</li>
<li>Notizen, Zeichen, Text und Sprünge, Lesezeichen und die zuletzt gelesene Seite</li>
<li>Notendetails (Titel, Komponist, Verlag), Ordner, Favoriten und Setlisten</li>
<li>Einstellungen — Sprache, Stifte, Metronom, Ansicht, Beginn der Testphase, ob Pro gekauft wurde u. Ä.</li>
</ul>
<p>Diese Daten bleiben im privaten Speicher der App und werden nicht an uns übermittelt. Sie werden gelöscht, wenn du Noten entfernst oder die App deinstallierst. Eine mit „Bibliothek sichern“ erstellte Datei wird nur dort gespeichert, wo du es wählst. Rechtsgrundlage: Bereitstellung der App-Funktionen (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Android-Sicherung", f"""<p>Unter Android werden, wenn die Google-Sicherung des Geräts aktiv ist, die <strong>Einstellungen</strong> der App (nicht die Notendateien) in deinem Google-Konto gesichert und bei einer Neuinstallation wiederhergestellt. Google verarbeitet diese Sicherung gemäß der <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google-Datenschutzerklärung</a>; wir haben keinen Zugriff. Du kannst sie in den Geräteeinstellungen abschalten.</p>"""),
   ("Kamera und Fotos", """<p>Die App fragt nur bei „Fotos zu PDF“ nach der Kamera oder lässt dich Fotos auswählen. Die Fotos werden auf dem Gerät zu einem PDF und nicht an uns gesendet.</p>"""),
   ("Texterkennung (Titel und Komponist)", f"""<p>Um Titel und Komponist von der ersten Seite zu lesen, nutzt die App eine Texterkennung auf dem Gerät — Google ML Kit unter Android, Apple Vision auf iPhone und iPad. Seitenbilder verlassen das Gerät nicht. Google ML Kit kann <strong>anonyme Nutzungsstatistiken</strong> wie Gerätetyp, App-Version und Leistung zu Diagnosezwecken an Google senden (<a href="{MLKIT_TERMS}" target="_blank" rel="noopener">ML-Kit-Bedingungen</a>). Noteninhalte und Fotos sind nicht enthalten.</p>"""),
   ("Suche und Download bei IMSLP", f"""<p>Wenn du „IMSLP“ nutzt, sendet die App deine Suchbegriffe an die öffentliche Notenbibliothek IMSLP (imslp.org), um Werke und Dateilisten abzurufen, und öffnet beim Herunterladen die Download-Seite von IMSLP in der App. Dabei erreichen Suchbegriffe und die IP-Adresse deines Geräts die Server von IMSLP; IMSLP kann Cookies setzen. Es gilt die <a href="{IMSLP_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von IMSLP</a>. Wir erfahren nicht, was du suchst oder lädst.</p>"""),
   ("Kauf von Pro", f"""<p>Pro wird über Google Play gekauft. Zahlung und Zahlungsdaten verarbeitet der Store; die App prüft nur, ob Pro gekauft wurde, und speichert das auf dem Gerät. Kartennummern oder andere Zahlungsdaten erhalten wir nie. Es gilt die <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google-Datenschutzerklärung</a>.</p>"""),
   ("welegato-Banner und externe Links", f"""<p>Das Banner unter der Notenliste und die Links in den Einstellungen öffnen welegato (eine Musikplattform desselben Unternehmens) oder eine andere App von Vicino Labs im Browser oder in Google Play <strong>nur, wenn du sie antippst</strong>. Links tragen nur die Kennung <code>utm_source=leggii</code>, die dich nicht identifiziert. Danach gilt die Erklärung der jeweiligen Seite — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato-Datenschutz</a>.</p>
<p>Wenn du in der kostenlosen Version einen Foto-Scan als PDF teilst, steht unten auf jeder Seite „Leggii Noten mit welegato · welegato.com“. Diese Zeile enthält keine personenbezogenen Daten.</p>"""),
   ("Teilen und Export", """<p>Beim Teilen von Noten oder beim Export eines PDFs mit Notizen geht die Datei nur an die App oder Person, die du im Teilen-Dialog des Geräts wählst.</p>"""),
   ("Nicht erhobene Daten", """<p>Wir erheben keine Namen, E-Mail-Adressen, Telefonnummern, Standortdaten, Kontakte, Mikrofondaten oder Werbe-IDs. Bluetooth-Pedale funktionieren wie eine Tastatur und brauchen keine zusätzliche Berechtigung.</p>"""),
   ("Kinder", """<p>Da die App keine personenbezogenen Daten an uns sendet, gibt es aus Datenschutzgründen keine Altersgrenze. Kinder sollten IMSLP und externe Links gemeinsam mit Erwachsenen nutzen.</p>"""),
   ("Deine Rechte", """<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO)</li>
<li>Beschwerde bei einer Aufsichtsbehörde — z. B. bei der Landesbeauftragten für Datenschutz und Informationsfreiheit NRW (LDI NRW) oder der Behörde deines Wohnorts</li>
</ul>
<p>Wir speichern keine Daten über dich; Daten auf deinem Gerät kannst du in der App oder durch Deinstallation löschen. Bei Fragen erreichst du uns unten.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich Recht oder App ändern; Änderungen und das Datum stehen auf dieser Seite.</p>"""),
   ("Kontakt", "<p>Fragen zum Datenschutz richte bitte an:</p>" + _contact("Betreiber")),
  ],
 },
 "it": {
  "title": "Leggii — Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "22.10.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Leggii, un'app per spartiti di Vicino Labs, non ha account né un nostro server. Spartiti e annotazioni restano sul tuo dispositivo e non possiamo vederli. Ecco con precisione quali dati tratta l'app.",
  "footer": "Questa informativa è in vigore dal 22 ottobre 2026 (versione 1.0).",
  "other": "Termini di utilizzo →",
  "sections": [
   ("Titolare del trattamento", _id_card("it") + "<p>Vicino Labs è il titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per i dati trattati in relazione a questa app.</p>"),
   ("In breve", """<div class="summary-box"><ul>
<li>Nessun account, nessun accesso, nessun invio a un server gestito da noi.</li>
<li>Spartiti importati (PDF), annotazioni e simboli, cartelle, scalette e impostazioni restano <strong>solo sul dispositivo</strong>.</li>
<li>Nessuna rete pubblicitaria e nessuno strumento di analisi o tracciamento. Il banner in basso promuove welegato, un servizio della stessa azienda.</li>
<li>Internet si usa solo quando <strong>cerchi o scarichi da IMSLP</strong>, acquisti Pro o tocchi un link.</li>
<li>Le scansioni da foto e il riconoscimento del testo della prima pagina avvengono <strong>sul dispositivo</strong>; le foto non lo lasciano.</li>
</ul></div>"""),
   ("Dati salvati sul dispositivo", """<ul>
<li>I PDF degli spartiti importati o creati e le anteprime</li>
<li>Annotazioni, simboli, testo e collegamenti di ripetizione, segnalibri e l'ultima pagina letta</li>
<li>Dati dello spartito (titolo, compositore, editore), cartelle, preferiti e scalette</li>
<li>Impostazioni — lingua, penne, metronomo, aspetto, inizio della prova gratuita, acquisto di Pro e simili</li>
</ul>
<p>Questi dati restano nella memoria privata dell'app e non ci vengono inviati. Si cancellano eliminando gli spartiti o disinstallando l'app. Un file creato con “Backup della libreria” è salvato solo dove scegli tu. Base giuridica: fornitura delle funzioni dell'app (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Backup Android", f"""<p>Su Android, se il backup Google del dispositivo è attivo, le <strong>impostazioni</strong> dell'app (non i file degli spartiti) vengono salvate nel tuo account Google e ripristinate in caso di reinstallazione. Google le tratta secondo la propria <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">informativa sulla privacy</a>; noi non vi abbiamo accesso. Puoi disattivarlo nelle impostazioni del dispositivo.</p>"""),
   ("Fotocamera e foto", """<p>L'app chiede la fotocamera, o ti fa scegliere delle foto, solo quando usi “Foto in PDF”. Le foto diventano un PDF sul dispositivo e non ci vengono inviate.</p>"""),
   ("Riconoscimento del testo (titolo e compositore)", f"""<p>Per leggere titolo e compositore dalla prima pagina l'app usa un riconoscimento del testo sul dispositivo — Google ML Kit su Android, Apple Vision su iPhone e iPad. Le immagini delle pagine non lasciano il dispositivo. Google ML Kit può inviare a Google <strong>statistiche anonime d'uso</strong> come tipo di dispositivo, versione dell'app e prestazioni, a fini diagnostici (<a href="{MLKIT_TERMS}" target="_blank" rel="noopener">termini di ML Kit</a>). Contenuti degli spartiti e foto non sono inclusi.</p>"""),
   ("Ricerca e download su IMSLP", f"""<p>Quando usi “IMSLP”, l'app invia i termini di ricerca alla biblioteca musicale pubblica IMSLP (imslp.org) per ottenere opere ed elenchi di file, e apre nell'app la pagina di download di IMSLP. I termini di ricerca e l'indirizzo IP del dispositivo raggiungono i server di IMSLP, che può impostare cookie. Si applica l'<a href="{IMSLP_PRIVACY}" target="_blank" rel="noopener">informativa privacy di IMSLP</a>. Noi non sappiamo cosa cerchi o scarichi.</p>"""),
   ("Acquisto di Pro", f"""<p>Pro si acquista tramite Google Play. Pagamento e dati di pagamento sono gestiti dallo store; l'app verifica solo se Pro è stato acquistato e lo registra sul dispositivo. Non riceviamo mai numeri di carta o altri dati di pagamento. Si applica l'<a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">informativa privacy di Google</a>.</p>"""),
   ("Banner welegato e link esterni", f"""<p>Il banner sotto l'elenco degli spartiti e i link nelle impostazioni aprono welegato (una piattaforma musicale della stessa azienda) o un'altra app di Vicino Labs nel browser o in Google Play <strong>solo quando li tocchi</strong>. I link portano solo l'indicazione <code>utm_source=leggii</code>, che non ti identifica. Poi si applica l'informativa del sito aperto — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">privacy di welegato</a>.</p>
<p>Se nella versione gratuita condividi una scansione da foto come PDF, in fondo a ogni pagina compare “Leggii con welegato · welegato.com”. La riga non contiene dati personali.</p>"""),
   ("Condivisione ed esportazione", """<p>Quando condividi uno spartito o esporti un PDF con annotazioni, il file va solo all'app o alla persona che scegli nella finestra di condivisione del dispositivo.</p>"""),
   ("Dati che non raccogliamo", """<p>Non raccogliamo nomi, indirizzi e-mail, numeri di telefono, posizione, contatti, dati del microfono o ID pubblicitari. I pedali Bluetooth funzionano come una tastiera e non richiedono permessi aggiuntivi.</p>"""),
   ("Minori", """<p>Poiché l'app non ci invia dati personali, non ci sono limiti di età per motivi di privacy. I bambini dovrebbero usare IMSLP e i link esterni insieme a un adulto.</p>"""),
   ("I tuoi diritti", """<ul>
<li>Accesso, rettifica, cancellazione, limitazione, portabilità e opposizione (artt. 15–21 GDPR)</li>
<li>Reclamo a un'autorità di controllo — ad es. l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o quella del tuo luogo di residenza</li>
</ul>
<p>Non conserviamo dati su di te; quelli sul dispositivo puoi eliminarli nell'app o disinstallandola. Per domande contattaci qui sotto.</p>"""),
   ("Modifiche", """<p>Possiamo aggiornare questa informativa se cambiano la legge o l'app; modifiche e data di entrata in vigore sono pubblicate in questa pagina.</p>"""),
   ("Contatti", "<p>Per domande sulla protezione dei dati scrivici:</p>" + _contact("Gestore")),
  ],
 },
}
