"""Appoggio 개인정보처리방침 본문 (ko/en/de/it) — appoggio_legal.py가 HTML로 만든다.

2026-10-01 버전 3.0: vicinolabs.com으로 이전. 앱 1.2.0에서 광고(AdMob)와 인앱결제를
없애서 그 내용을 모두 뺐다. 앱 자체는 인터넷에 연결하지 않고(INTERNET 권한 없음),
사용자가 링크를 누를 때만 브라우저가 열린다(welegato 안내 배너, 법적 문서).
"""

EMAIL = "contact@vicinolabs.com"
WELEGATO_PRIVACY = "https://welegato.com/legal/"

_ID = {
 "ko": ("상호", "Vicino Labs (개인사업자, Einzelunternehmen)", "대표자", "주소", "이메일"),
 "en": ("Trading name", "Vicino Labs (sole proprietorship, Einzelunternehmen)", "Owner", "Address", "Email"),
 "de": ("Firma", "Vicino Labs (Einzelunternehmen)", "Inhaber", "Anschrift", "E-Mail"),
 "it": ("Denominazione", "Vicino Labs (ditta individuale, Einzelunternehmen)", "Titolare", "Indirizzo", "E-mail"),
}


def _id_card(lang):
    t, name, owner, addr, mail = _ID[lang]
    return (f'<div class="id-card"><dt>{t}</dt><dd>{name}</dd><dt>{owner}</dt><dd>Jeong-Hwan Lee</dd>'
            f'<dt>{addr}</dt><dd>Ruhrallee 41, 44139 Dortmund, Germany</dd>'
            f'<dt>{mail}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>'
            f'<dt>Impressum</dt><dd><a href="/impressum/">vicinolabs.com/impressum</a></dd></div>')


def _contact(role):
    return (f'<div class="contact-card"><span class="role">{role}</span><span class="name">Vicino Labs</span>'
            f'<a href="mailto:{EMAIL}">{EMAIL}</a></div>')


PRIVACY = {
 "ko": {
  "title": "Appoggio 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.10.01"), ("버전", "3.0"), ("운영자", "Vicino Labs")],
  "lede": "Vicino Labs가 만든 성악가를 위한 호흡 훈련 앱 Appoggio는 개인정보를 수집하지 않습니다. 회원가입도, 광고도, 결제도, 서버도 없고, 훈련 기록은 기기 밖으로 나가지 않습니다. 아래에 그 내용을 정확하게 적어 둡니다.",
  "footer": "본 방침은 2026년 10월 1일부터 시행됩니다 (버전 3.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _id_card("ko") + "<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>회원가입·로그인이 없습니다. 훈련 설정, 리마인더 시각, 훈련 기록은 <strong>기기 안에만</strong> 저장되고, 저희는 이를 볼 수 없습니다.</li>
<li><strong>광고와 인앱결제가 없습니다</strong> (버전 1.2.0부터). 광고 식별자를 쓰지 않고, 분석·추적 도구(Firebase Analytics 등)도 없습니다.</li>
<li>앱은 스스로 인터넷에 연결하지 않습니다. 화면 아래 <strong>welegato 안내 배너</strong>나 개인정보처리방침·약관 링크를 <strong>누를 때만</strong> 브라우저가 열립니다.</li>
<li>리마인더 알림은 기기 안에서 예약되는 로컬 알림이며, 푸시 서버를 쓰지 않습니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>훈련 설정 — 라운드 수, 타이머 스타일, 피드백 방식(소리·진동), 언어, 다크 모드, 색상 테마</li>
<li>리마인더 설정 — 켜짐/꺼짐과 시각</li>
<li>훈련 기록 — 훈련을 완료한 날짜와 그날 완료한 훈련 방법(4가지 중 어떤 것). 정확한 시각이나 소요 시간은 저장하지 않습니다.</li>
</ul>
<p>이 정보는 기기 안의 앱 전용 저장소에만 있고 저희에게 전송되지 않습니다. 기록 화면의 “기록 초기화”나 앱 삭제로 언제든 지울 수 있습니다. 처리 근거: 앱 기능 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("알림·소리·진동·화면 켜짐", """<p>리마인더를 켜면 앱이 기기의 <strong>알림 권한</strong>을 요청합니다. 알림은 기기 안에서 예약·표시되며 외부 서버와 통신하지 않습니다. 권한은 기기 설정에서 언제든 끌 수 있습니다. 훈련 중 단계가 바뀔 때의 소리·진동, 그리고 훈련 중 화면이 꺼지지 않게 하는 기능도 모두 기기 안에서만 동작하며 어떤 정보도 보내지 않습니다.</p>"""),
   ("welegato 안내 배너와 외부 링크", f"""<p>홈·연습 화면 아래에는 같은 회사(Vicino Labs)가 운영하는 음악 레슨 플랫폼 <strong>welegato</strong>를 안내하는 배너가 있습니다. 배너를 <strong>누를 때만</strong> 기기의 브라우저로 welegato 웹사이트가 열리며, 앱은 그 전에도 그 후에도 어떤 개인정보도 전달하지 않습니다.</p>
<ul>
<li>링크 주소에는 “앱에서 왔다”는 것만 알려주는 캠페인 표시(<code>utm_source=appoggio</code>)가 붙습니다. 이용자를 식별하는 값은 들어 있지 않습니다.</li>
<li>웹사이트가 열린 뒤에는 그 사이트의 개인정보처리방침이 적용됩니다 — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato 개인정보처리방침</a>, 이 사이트(vicinolabs.com)는 <a href="/datenschutz/">Datenschutz</a>.</li>
<li>웹사이트를 여는 순간, 인터넷 연결의 특성상 기기의 IP 주소가 해당 사이트의 서버(호스팅 업체)에 전달됩니다.</li>
</ul>"""),
   ("앱 스토어", """<p>앱은 Google Play(및 향후 Apple App Store)를 통해 배포됩니다. 설치·업데이트·충돌 보고 등은 각 스토어가 자체 개인정보처리방침에 따라 처리하며, 저희는 스토어가 제공하는 익명 통계(설치 수, 충돌 건수 등)만 볼 수 있습니다.</p>"""),
   ("수집하지 않는 정보", """<p>이름, 이메일, 전화번호, 위치, 연락처, 사진, 카메라·마이크, 광고 식별자, 기기 식별자를 수집하지 않습니다. 앱에는 Android 인터넷 권한도 없습니다.</p>"""),
   ("아동", """<p>앱은 개인정보를 수집하지 않으므로 연령에 따른 별도의 제한이 없습니다. 다만 호흡 훈련은 보호자의 지도 아래 무리하지 않게 해 주세요(이용약관의 건강 안내 참고).</p>"""),
   ("정보주체의 권리", """<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리 — 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>저희는 이용자의 정보를 갖고 있지 않으므로, 기기 안의 정보는 앱(기록 초기화)이나 앱 삭제로 직접 지울 수 있습니다. 궁금한 점은 아래로 연락해 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 본 방침을 고칠 수 있습니다. 변경 내용과 시행일은 이 페이지에 게시합니다. 이전 버전(2.0)과 달리, 버전 3.0은 광고·인앱결제가 없어진 앱 1.2.0 기준입니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _contact("운영자")),
  ],
 },
 "en": {
  "title": "Appoggio Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-10-01"), ("Version", "3.0"), ("Operator", "Vicino Labs")],
  "lede": "Appoggio, a breathing-training app for singers made by Vicino Labs, does not collect personal data. There is no account, no advertising, no purchase and no server, and your training history never leaves your device. Here are the details, as precisely as we can put them.",
  "footer": "This policy is effective from 1 October 2026 (version 3.0).",
  "other": "Terms of Service →",
  "sections": [
   ("Data controller", _id_card("en") + "<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for any personal data processed in connection with this app.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>No account or sign-in. Training settings, reminder times and training history are stored <strong>only on your device</strong> — we cannot see them.</li>
<li><strong>No ads and no in-app purchases</strong> (since version 1.2.0). No advertising ID, and no analytics or tracking SDKs (e.g. Firebase Analytics).</li>
<li>The app does not connect to the internet by itself. Your browser opens <strong>only when you tap</strong> the <strong>welegato banner</strong> or a link to our privacy policy or terms.</li>
<li>Reminders are local notifications scheduled on your device — no push server is involved.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>Training settings — number of rounds, timer style, feedback (sound/vibration), language, dark mode, colour theme</li>
<li>Reminder settings — on/off and time</li>
<li>Training history — the dates you trained and which of the four methods you completed that day. We don't store the exact time or session length.</li>
</ul>
<p>This data stays in the app's private storage on your device and is never sent to us. You can delete it anytime with “Reset records” on the records screen or by uninstalling the app. Legal basis: providing the app's features (Art. 6(1)(b) GDPR).</p>"""),
   ("Notifications, sound, vibration and screen", """<p>When you turn on a reminder, the app asks for your device's <strong>notification permission</strong>. Notifications are scheduled and shown on the device without contacting any server, and you can revoke the permission in your device settings at any time. The sound and vibration cues between breathing phases, and keeping the screen on during a session, also work entirely on the device and send no data.</p>"""),
   ("The welegato banner and external links", f"""<p>At the bottom of the home and training screens there is a banner for <strong>welegato</strong>, a music-lesson platform run by the same company (Vicino Labs). The welegato website opens in your browser <strong>only when you tap the banner</strong>; the app does not pass on any personal data, before or after.</p>
<ul>
<li>The link carries a campaign tag (<code>utm_source=appoggio</code>) that only says the visit came from the app. It contains no value that identifies you.</li>
<li>Once a website is open, that website's privacy policy applies — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato privacy policy</a>; for this site (vicinolabs.com) see <a href="/datenschutz/">Datenschutz</a>.</li>
<li>As with any website visit, your device's IP address reaches that site's server (hosting provider) when the page loads.</li>
</ul>"""),
   ("App stores", """<p>The app is distributed through Google Play (and later possibly the Apple App Store). Installs, updates and crash reports are handled by the store under its own privacy policy; we only see anonymous statistics the store provides (such as install and crash counts).</p>"""),
   ("Data we don't collect", """<p>We do not collect names, email addresses, phone numbers, location, contacts, photos, camera or microphone data, advertising IDs or device identifiers. The Android app does not even have the internet permission.</p>"""),
   ("Children", """<p>Because the app collects no personal data, there is no age restriction for privacy reasons. Please practise breathing exercises sensibly and, for children, under adult supervision (see the health notes in our Terms).</p>"""),
   ("Your rights", """<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR)</li>
<li>Lodge a complaint with a supervisory authority — e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live</li>
</ul>
<p>We hold no data about you; what is on your device you can delete yourself in the app (Reset records) or by uninstalling it. For any question, please contact us below.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law or the app changes; changes and the effective date are posted on this page. Unlike version 2.0, version 3.0 reflects app version 1.2.0, which no longer has ads or in-app purchases.</p>"""),
   ("Contact", "<p>For questions about data processing, please contact:</p>" + _contact("Operator")),
  ],
 },
 "de": {
  "title": "Appoggio Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "01.10.2026"), ("Version", "3.0"), ("Anbieter", "Vicino Labs")],
  "lede": "Appoggio, eine Atemtrainings-App für Sängerinnen und Sänger von Vicino Labs, erhebt keine personenbezogenen Daten. Es gibt kein Konto, keine Werbung, keine Käufe und keinen Server, und Ihr Trainingsverlauf verlässt Ihr Gerät nicht. Hier die Einzelheiten.",
  "footer": "Diese Erklärung gilt ab dem 1. Oktober 2026 (Version 3.0).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _id_card("de") + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für eine etwaige Verarbeitung personenbezogener Daten im Zusammenhang mit dieser App.</p>"),
   ("Das Wichtigste in Kürze", """<div class="summary-box"><ul>
<li>Kein Konto, keine Anmeldung. Trainingseinstellungen, Erinnerungszeiten und Trainingsverlauf werden <strong>nur auf Ihrem Gerät</strong> gespeichert — wir können sie nicht einsehen.</li>
<li><strong>Keine Werbung und keine In-App-Käufe</strong> (seit Version 1.2.0). Keine Werbe-ID, keine Analyse- oder Tracking-Dienste (z. B. Firebase Analytics).</li>
<li>Die App verbindet sich nicht selbst mit dem Internet. Ihr Browser öffnet sich <strong>nur, wenn Sie</strong> auf das <strong>welegato-Banner</strong> oder einen Link zu Datenschutzerklärung bzw. Nutzungsbedingungen <strong>tippen</strong>.</li>
<li>Erinnerungen sind lokale Benachrichtigungen, die auf dem Gerät geplant werden — ohne Push-Server.</li>
</ul></div>"""),
   ("Auf Ihrem Gerät gespeicherte Daten", """<ul>
<li>Trainingseinstellungen — Rundenzahl, Timer-Stil, Rückmeldung (Ton/Vibration), Sprache, Dunkelmodus, Farbthema</li>
<li>Erinnerungen — an/aus und Uhrzeit</li>
<li>Trainingsverlauf — an welchen Tagen Sie trainiert und welche der vier Methoden Sie abgeschlossen haben. Genaue Uhrzeit oder Dauer speichern wir nicht.</li>
</ul>
<p>Diese Daten bleiben im privaten Speicher der App auf Ihrem Gerät und werden nicht an uns übertragen. Sie können sie jederzeit mit „Aufzeichnungen zurücksetzen“ oder durch Deinstallieren der App löschen. Rechtsgrundlage: Bereitstellung der App-Funktionen (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Benachrichtigungen, Ton, Vibration und Bildschirm", """<p>Wenn Sie eine Erinnerung einschalten, fragt die App nach der <strong>Benachrichtigungsberechtigung</strong>. Benachrichtigungen werden auf dem Gerät geplant und angezeigt, ohne einen Server zu kontaktieren; die Berechtigung können Sie jederzeit in den Geräteeinstellungen entziehen. Auch Ton- und Vibrationssignale zwischen den Atemphasen sowie das Wachhalten des Bildschirms während des Trainings funktionieren ausschließlich auf dem Gerät und übermitteln keine Daten.</p>"""),
   ("welegato-Banner und externe Links", f"""<p>Unten auf dem Start- und Trainingsbildschirm weist ein Banner auf <strong>welegato</strong> hin, eine Plattform für Musikunterricht desselben Anbieters (Vicino Labs). Die welegato-Website öffnet sich in Ihrem Browser <strong>nur, wenn Sie auf das Banner tippen</strong>; die App gibt dabei weder vorher noch nachher personenbezogene Daten weiter.</p>
<ul>
<li>Der Link enthält eine Kampagnenkennung (<code>utm_source=appoggio</code>), die nur angibt, dass der Besuch aus der App kommt. Sie enthält keinen Wert, der Sie identifiziert.</li>
<li>Sobald eine Website geöffnet ist, gilt deren Datenschutzerklärung — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von welegato</a>; für diese Website (vicinolabs.com) siehe <a href="/datenschutz/">Datenschutz</a>.</li>
<li>Wie bei jedem Website-Besuch wird beim Laden der Seite die IP-Adresse Ihres Geräts an den Server (Hoster) dieser Website übermittelt.</li>
</ul>"""),
   ("App-Stores", """<p>Die App wird über Google Play (und künftig ggf. den Apple App Store) vertrieben. Installationen, Updates und Absturzberichte verarbeitet der jeweilige Store nach seiner eigenen Datenschutzerklärung; wir sehen nur anonyme Statistiken des Stores (z. B. Installations- und Absturzzahlen).</p>"""),
   ("Was wir nicht erheben", """<p>Wir erheben keine Namen, E-Mail-Adressen, Telefonnummern, Standortdaten, Kontakte, Fotos, Kamera- oder Mikrofondaten, Werbe-IDs oder Gerätekennungen. Die Android-App hat nicht einmal die Internet-Berechtigung.</p>"""),
   ("Kinder", """<p>Da die App keine personenbezogenen Daten erhebt, gibt es aus Datenschutzgründen keine Altersgrenze. Bitte üben Sie Atemübungen mit Maß und bei Kindern unter Aufsicht Erwachsener (siehe Gesundheitshinweise in den Nutzungsbedingungen).</p>"""),
   ("Ihre Rechte", """<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO)</li>
<li>Beschwerde bei einer Aufsichtsbehörde — z. B. der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW) oder der Behörde an Ihrem Wohnort</li>
</ul>
<p>Wir speichern keine Daten über Sie; was auf Ihrem Gerät liegt, können Sie selbst in der App (Aufzeichnungen zurücksetzen) oder durch Deinstallieren löschen. Bei Fragen erreichen Sie uns unten.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich Recht oder App ändern; Änderungen und Gültigkeitsdatum veröffentlichen wir auf dieser Seite. Anders als Version 2.0 beschreibt Version 3.0 die App-Version 1.2.0 ohne Werbung und In-App-Käufe.</p>"""),
   ("Kontakt", "<p>Für Fragen zur Datenverarbeitung:</p>" + _contact("Anbieter")),
  ],
 },
 "it": {
  "title": "Appoggio — Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "01/10/2026"), ("Versione", "3.0"), ("Titolare", "Vicino Labs")],
  "lede": "Appoggio, l'app di allenamento del respiro per cantanti realizzata da Vicino Labs, non raccoglie dati personali. Non ci sono account, pubblicità, acquisti né server, e lo storico degli allenamenti non lascia mai il tuo dispositivo. Ecco i dettagli.",
  "footer": "La presente informativa è in vigore dal 1° ottobre 2026 (versione 3.0).",
  "other": "Termini di servizio →",
  "sections": [
   ("Titolare del trattamento", _id_card("it") + "<p>Vicino Labs è il titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per gli eventuali dati personali trattati in relazione a questa app.</p>"),
   ("In sintesi", """<div class="summary-box"><ul>
<li>Nessun account né login. Impostazioni, orari dei promemoria e storico degli allenamenti sono salvati <strong>solo sul tuo dispositivo</strong>: noi non possiamo vederli.</li>
<li><strong>Nessuna pubblicità e nessun acquisto in-app</strong> (dalla versione 1.2.0). Nessun ID pubblicitario, nessuno strumento di analisi o tracciamento (es. Firebase Analytics).</li>
<li>L'app non si collega a Internet da sola. Il browser si apre <strong>solo quando tocchi</strong> il <strong>banner di welegato</strong> o un link all'informativa o ai termini.</li>
<li>I promemoria sono notifiche locali programmate sul dispositivo, senza server push.</li>
</ul></div>"""),
   ("Dati salvati sul dispositivo", """<ul>
<li>Impostazioni di allenamento — numero di round, stile del timer, segnali (suono/vibrazione), lingua, modalità scura, tema colore</li>
<li>Promemoria — attivo/disattivo e orario</li>
<li>Storico — i giorni in cui ti sei allenato e quali dei quattro metodi hai completato. Non salviamo l'ora esatta né la durata.</li>
</ul>
<p>Questi dati restano nella memoria privata dell'app sul dispositivo e non ci vengono mai inviati. Puoi cancellarli in qualsiasi momento con “Reimposta registri” o disinstallando l'app. Base giuridica: fornitura delle funzioni dell'app (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Notifiche, suono, vibrazione e schermo", """<p>Quando attivi un promemoria, l'app chiede l'<strong>autorizzazione alle notifiche</strong>. Le notifiche sono programmate e mostrate sul dispositivo senza contattare alcun server; puoi revocare l'autorizzazione dalle impostazioni del dispositivo. Anche i segnali sonori e di vibrazione tra le fasi e lo schermo sempre acceso durante l'allenamento funzionano solo sul dispositivo e non inviano dati.</p>"""),
   ("Il banner di welegato e i link esterni", f"""<p>In fondo alla schermata principale e a quella di allenamento c'è un banner di <strong>welegato</strong>, una piattaforma di lezioni di musica gestita dalla stessa società (Vicino Labs). Il sito di welegato si apre nel browser <strong>solo se tocchi il banner</strong>; l'app non trasmette alcun dato personale, né prima né dopo.</p>
<ul>
<li>Il link contiene un parametro di campagna (<code>utm_source=appoggio</code>) che indica soltanto che la visita proviene dall'app. Non contiene alcun valore che ti identifichi.</li>
<li>Una volta aperto il sito, si applica la sua informativa — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">informativa privacy di welegato</a>; per questo sito (vicinolabs.com) vedi <a href="/datenschutz/">Datenschutz</a>.</li>
<li>Come per ogni visita a un sito web, al caricamento della pagina l'indirizzo IP del dispositivo raggiunge il server (hosting) di quel sito.</li>
</ul>"""),
   ("App store", """<p>L'app è distribuita tramite Google Play (e in futuro eventualmente l'Apple App Store). Installazioni, aggiornamenti e segnalazioni di arresti anomali sono gestiti dallo store secondo la propria informativa; noi vediamo solo statistiche anonime fornite dallo store (ad es. numero di installazioni e di arresti).</p>"""),
   ("Dati che non raccogliamo", """<p>Non raccogliamo nomi, indirizzi e-mail, numeri di telefono, posizione, contatti, foto, dati di fotocamera o microfono, ID pubblicitari o identificativi del dispositivo. L'app Android non ha nemmeno l'autorizzazione di accesso a Internet.</p>"""),
   ("Minori", """<p>Poiché l'app non raccoglie dati personali, non ci sono limiti di età per motivi di privacy. Esegui gli esercizi di respirazione con moderazione e, per i bambini, sotto la supervisione di un adulto (vedi le avvertenze sulla salute nei Termini).</p>"""),
   ("I tuoi diritti", """<ul>
<li>Accesso, rettifica, cancellazione, limitazione del trattamento, portabilità e opposizione (artt. 15–21 GDPR)</li>
<li>Reclamo a un'autorità di controllo — ad es. l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o il Garante del tuo paese di residenza</li>
</ul>
<p>Non conserviamo dati su di te; ciò che si trova sul dispositivo puoi cancellarlo da solo nell'app (Reimposta registri) o disinstallandola. Per qualsiasi domanda, contattaci qui sotto.</p>"""),
   ("Modifiche", """<p>Potremo aggiornare questa informativa in caso di modifiche normative o dell'app; modifiche e data di entrata in vigore saranno pubblicate in questa pagina. A differenza della versione 2.0, la versione 3.0 si riferisce alla versione 1.2.0 dell'app, senza pubblicità né acquisti in-app.</p>"""),
   ("Contatti", "<p>Per domande sul trattamento dei dati:</p>" + _contact("Titolare")),
  ],
 },
}
