"""끼아베(Chiave) 개인정보처리방침 본문 (ko/en/de/it) — chiave_legal.py가 HTML로 만든다.

2026-11-06 버전 1.0 — 2026-11-06 운영자 승인, 게시. leggii_privacy_content.py의 틀과 문구를 따랐다.
회원가입·계정 없음. 악보·편집·스캔 원본 페이지 이미지는 기기 안에만(클라우드 없음).
악보 스캔(선택): 기기에서 페이지를 약 2마디 조각으로 잘라 서버(Supabase Edge Function, EU)로 →
Google Gemini API가 음표를 읽음. 조각 이미지·인식 결과는 서버에 저장하지 않음.
서버 기록: 기기 해시, 시각, 모델 이름, 성공 여부, 토큰 수 — 90일 뒤 삭제 (2026-11-06 승인).
요금제(페이지 수) 계산과 체험 반복 방지: SHA-256("chiave:"+기기 식별값)만 서버에.
무료 요금제에만 welegato 링크 배너(utm_source=chiave). 마이크·위치·분석 SDK·광고 네트워크 없음.
빈칸 채움 2026-11-06: 기록 90일, 기기 기록 마지막 스캔 후 1년(유료 기록은 세법 기간), Gemini 유료 키.
"""

from appoggio_privacy_content import EMAIL, _id_card, _contact

WELEGATO_PRIVACY = "https://welegato.com/legal/"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
APPLE_PRIVACY = "https://www.apple.com/legal/privacy/"

# 운영자가 채워야 하는 자리 — 모든 언어에 같은 문구로 보이게 둔다.

_DRAFT = {
 "ko": ("초안", "아직 승인되지 않은 문서입니다. 운영자가 확정하기 전에는 효력이 없습니다."),
 "en": ("Draft", "This document has not been approved yet and is not in effect until the operator confirms it."),
 "de": ("Entwurf", "Dieses Dokument ist noch nicht freigegeben und gilt erst, wenn der Betreiber es bestätigt."),
 "it": ("Bozza", "Questo documento non è ancora stato approvato e non è in vigore finché il gestore non lo conferma."),
}


def _draft(lang):
    word, text = _DRAFT[lang]
    return (f'<span style="display:block;margin:0 0 14px;padding:10px 14px;border:2px dashed #b4462f;'
            f'border-radius:8px;color:#b4462f;font-weight:600">{word} / DRAFT — {text}</span>')


PRIVACY = {
 "ko": {
  "title": "끼아베(Chiave) 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.11.06"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "Vicino Labs가 만든 끼아베(Chiave)는 악보를 쓰고, 스캔하고, 이조하는 앱입니다. 회원가입이 없고, 악보·편집 내용·스캔한 원본 페이지 이미지는 이용자의 기기에만 저장됩니다. 이용자가 악보 스캔을 쓸 때만 페이지를 잘게 나눈 조각 이미지가 저희 서버(EU)와 Google Gemini를 거칩니다. 앱이 다루는 정보를 정확하게 적어 둡니다.",
  "footer": "본 방침은 2026년 11월 6일부터 시행됩니다 (버전 1.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _id_card("ko") + "<p>Vicino Labs는 EU 일반개인정보보호규정(GDPR)상 이 앱과 관련된 개인정보 처리의 “컨트롤러(controller)”입니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>회원가입과 계정이 없습니다. 악보, 편집 내용, 스캔한 원본 페이지 이미지는 <strong>기기 안에만</strong> 저장되며 클라우드에 올리지 않습니다.</li>
<li><strong>악보 스캔</strong>(선택)을 쓰면 앱이 각 페이지를 기기에서 약 2마디 크기의 작은 조각으로 잘라 저희 서버를 거쳐 Google Gemini로 보내 음표를 읽습니다. 조각 이미지와 인식 결과는 서버에 <strong>저장하지 않습니다</strong>.</li>
<li>요금제의 페이지 수를 세기 위해 기기 식별값의 <strong>해시</strong>만 서버에 저장합니다.</li>
<li>광고 네트워크와 분석·추적 도구가 없습니다. 무료 요금제 화면 아래의 링크는 같은 회사 서비스 welegato를 알리는 자체 배너입니다.</li>
<li>마이크와 위치 정보는 쓰지 않습니다.</li>
</ul></div>"""),
   ("기기에 저장되는 정보", """<ul>
<li>이용자가 쓰거나 스캔한 악보와 편집·이조 내용</li>
<li>스캔할 때 고른 원본 페이지 이미지</li>
<li>앱 설정</li>
<li>iPhone·iPad에서는 키체인에, 웹에서는 브라우저에 저장한 무작위 기기 번호(아래 “요금제와 기기 식별값” 참고)</li>
</ul>
<p>이 정보는 기기 안의 앱 저장소에 있고, 악보 스캔 때 보내는 조각 이미지(아래)를 빼면 저희에게 전송되지 않습니다. 클라우드 저장이나 동기화 기능은 없습니다. 앱에서 악보를 지우거나 앱을 삭제하면 사라집니다. 다만 iPhone·iPad의 키체인에 저장한 기기 번호는 재설치 후 무료 체험이 반복되지 않도록 하기 위한 것이어서, 앱을 삭제해도 남을 수 있습니다. 처리 근거: 앱 기능 제공(GDPR 제6조 제1항 b호).</p>"""),
   ("카메라·사진·파일", """<p>악보 스캔에서 페이지를 고를 때만 카메라 권한을 요청하거나 사진 앨범·PDF 파일을 고르게 합니다. 고른 이미지는 기기에 저장되며, 스캔을 위해 보내는 조각 이미지(아래)를 빼면 기기 밖으로 나가지 않습니다.</p>"""),
   ("악보 스캔 (선택)", f"""<p>악보 스캔은 선택 기능이며, 이용자가 페이지(카메라, 사진 앨범, PDF)를 골라 스캔을 시작할 때만 동작합니다.</p>
<ul>
<li><strong>보내는 정보:</strong> 앱이 각 페이지를 기기 안에서 약 2마디 크기의 작은 조각 이미지로 자르고, 이 조각 이미지를 저희 서버로 보냅니다.</li>
<li><strong>처리:</strong> 저희 서버(Supabase Edge Function, EU)가 각 조각을 Google의 Gemini API로 전달해 음표를 읽고, 인식 결과를 이용자의 기기로 돌려보냅니다. 유료 API로 쓰며, Google은 이 데이터를 자사 모델 학습에 쓰지 않습니다.</li>
<li><strong>저장하지 않는 것:</strong> 조각 이미지와 인식 결과는 저희 서버에 저장하지 않습니다.</li>
<li><strong>서버에 남는 것:</strong> 기기 식별값의 해시, 시각, 사용한 AI 모델 이름, 성공 여부, 토큰 수만 기록합니다. 보관 기간: 90일이 지나면 지웁니다.</li>
</ul>
<p>처리 근거: 이용자가 요청한 기능의 제공(GDPR 제6조 제1항 b호), 서버 기록은 서비스 운영과 남용 방지를 위한 정당한 이익(f호). Google의 처리는 <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google 개인정보처리방침</a>을 따릅니다.</p>"""),
   ("요금제와 기기 식별값", f"""<p>요금제는 스캔한 악보 페이지 수로 셉니다. 페이지 수를 세고, 앱을 다시 설치해 무료 체험을 반복하는 것을 막기 위해 기기 식별값을 씁니다.</p>
<ul>
<li><strong>식별값:</strong> 안드로이드는 ANDROID_ID, iPhone·iPad는 키체인에 저장한 무작위 번호, 웹은 브라우저에 저장한 무작위 번호입니다.</li>
<li><strong>서버에 저장하는 것:</strong> 식별값 자체가 아니라 되돌릴 수 없는 SHA-256 해시(“chiave:” + 식별값)만, 페이지 사용 수와 요금제와 함께 저장합니다. 이름·이메일·전화번호는 필요하지 않습니다.</li>
<li><strong>보관 기간:</strong> 마지막으로 스캔한 날부터 1년이 지나면 지웁니다. 다만 유료 구독 기록은 세법상 보관 의무 기간(최대 10년) 동안 보관합니다.</li>
</ul>
<p>처리 근거: 요금제의 제공(b호), 무료 체험 남용 방지(f호).</p>"""),
   ("구매·구독", f"""<p>Pro·Pro+ 구독은 Google Play 또는 App Store 결제로 구매합니다. 결제와 카드 정보는 스토어가 처리하며 저희는 받지 않습니다. 스토어의 처리에는 <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google 개인정보처리방침</a> 또는 <a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">Apple 개인정보 처리방침</a>이 적용됩니다.</p>"""),
   ("서비스 제공자(수탁자)와 국외 이전", """<ul>
<li><strong>Supabase</strong> — 서버(Edge Function)와 데이터베이스, EU(독일 프랑크푸르트) 데이터센터 (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">방침</a>)</li>
<li><strong>Google</strong> — Gemini API(악보 스캔), Google Play 결제</li>
<li><strong>Apple</strong> — App Store 결제(iPhone·iPad)</li>
</ul>
<p>이 업체들이 EU 밖(예: 미국)에서 처리하는 경우, EU 표준계약조항 또는 EU-미국 데이터 프라이버시 프레임워크를 근거로 합니다.</p>"""),
   ("welegato 배너와 외부 링크", f"""<p>무료 요금제에서는 화면 아래에 welegato(같은 회사가 운영하는 음악 플랫폼, welegato.com)로 가는 링크가 표시됩니다. 광고 네트워크나 추적 도구가 아닌 자체 링크입니다. 설정에는 다른 Vicino Labs 앱의 스토어 페이지와 welegato.com으로 가는 링크가 있습니다.</p>
<p>링크는 <strong>누를 때만</strong> 브라우저나 스토어에서 열립니다. 배너 링크에는 “앱에서 왔다”는 표시(<code>utm_source=chiave</code> 등 utm 값)만 붙고 이용자를 식별하는 값은 없습니다. 열린 뒤에는 해당 사이트의 방침이 적용됩니다 — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato 개인정보처리방침</a>.</p>"""),
   ("공유·내보내기", """<p>악보를 PDF, PNG 이미지, MusicXML 또는 편집 가능한 파일로 내보내면, 이용자가 고른 경우에만 기기의 공유 화면이나 파일 선택 화면을 통해 이용자가 고른 앱·위치·사람에게 전달됩니다.</p>"""),
   ("수집하지 않는 정보", """<p>이름·이메일·전화번호 같은 계정 정보를 받지 않습니다. 마이크, 위치, 연락처, 광고 식별자는 쓰지 않으며, 분석 SDK와 광고 네트워크가 없습니다.</p>"""),
   ("아동", """<p>계정이 없고 연령 제한도 없습니다. 만 16세 미만이 악보 스캔을 쓸 때는 보호자의 동의를 받아 주세요. 어린이가 외부 링크를 쓸 때는 보호자가 함께해 주세요.</p>"""),
   ("정보주체의 권리", f"""<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리 — 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>악보와 스캔 이미지는 기기에만 있으므로 앱에서 지우거나 앱을 삭제하면 사라집니다. 서버의 기기 해시 기록은 <a href="mailto:{EMAIL}">{EMAIL}</a>로 요청하시면 지웁니다.</p>"""),
   ("방침의 변경", """<p>법령이나 앱 기능이 바뀌면 본 방침을 고칠 수 있으며, 변경 내용과 시행일을 이 페이지에 게시합니다. 앞으로의 버전에서 위레가토 통합 아이디 로그인이 제공될 수 있으며, 그때 본 방침을 고쳐 알립니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _contact("운영자")),
  ],
 },
 "en": {
  "title": "Chiave Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-11-06"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "Chiave, made by Vicino Labs, is an app for writing, scanning and transposing scores. There is no account; your scores, your edits and the original scanned page images are stored only on your device. Only when you use score scanning do small strip images of the pages go through our server (EU) and Google Gemini. Here is exactly what the app handles.",
  "footer": "This policy is effective from 6 November 2026 (version 1.0).",
  "other": "Terms of Service →",
  "sections": [
   ("Data controller", _id_card("en") + "<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for any personal data processed in connection with this app.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>No sign-up and no account. Scores, edits and original scanned page images stay <strong>on your device</strong> and are not uploaded to any cloud.</li>
<li>With <strong>score scanning</strong> (optional) the app cuts each page on your device into small strips of about 2 bars and sends them through our server to Google Gemini to read the notes. Strip images and recognised results are <strong>not stored</strong> on the server.</li>
<li>To count pages for your plan, only a <strong>hash</strong> of a device identifier is stored on our server.</li>
<li>No ad networks and no analytics or tracking tools. The link at the bottom of the screen on the Free plan is our own banner for welegato, a service of the same company.</li>
<li>The app does not use the microphone or your location.</li>
</ul></div>"""),
   ("Data stored on your device", """<ul>
<li>Scores you write or scan, and your edits and transpositions</li>
<li>The original page images you picked for scanning</li>
<li>App settings</li>
<li>On iPhone and iPad a random device number in the Keychain, on the web a random number stored in the browser (see “Plans and device identifier” below)</li>
</ul>
<p>This data stays in the app's storage on your device and is not sent to us, except for the strip images sent for scanning (below). There is no cloud storage or sync. It is deleted when you remove a score or uninstall the app. The device number in the iPhone/iPad Keychain, however, exists to stop the free trial from being repeated after reinstalling, so it may remain after the app is deleted. Legal basis: providing the app's features (Art. 6(1)(b) GDPR).</p>"""),
   ("Camera, photos and files", """<p>The app asks for the camera, or lets you pick photos from your album or a PDF file, only when you choose pages to scan. The images you pick are stored on your device and do not leave it, except for the strip images sent for scanning (below).</p>"""),
   ("Score scanning (optional)", f"""<p>Score scanning is optional and runs only when you pick pages (camera, photo album, PDF) and start a scan.</p>
<ul>
<li><strong>What is sent:</strong> the app cuts each page on your device into small strip images of about 2 bars and sends these strips to our server.</li>
<li><strong>Processing:</strong> our server (Supabase Edge Function, EU) forwards each strip to Google's Gemini API, which reads the notes; the result is sent back to your device. We use the paid API; Google does not use this data to train its models.</li>
<li><strong>Not stored:</strong> strip images and recognised results are not stored on our server.</li>
<li><strong>Kept on the server:</strong> only a hash of the device identifier, the time, the AI model name, a success flag and token counts. Retention period: deleted after 90 days.</li>
</ul>
<p>Legal basis: providing the feature you asked for (Art. 6(1)(b) GDPR); for the server log, our legitimate interest in running the service and preventing abuse (f). Google processes data under the <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google Privacy Policy</a>.</p>"""),
   ("Plans and device identifier", f"""<p>Plans are counted in scanned score pages. To count pages and to stop the free trial from being repeated by reinstalling the app, a device identifier is used.</p>
<ul>
<li><strong>Identifier:</strong> ANDROID_ID on Android, a random number stored in the Keychain on iPhone and iPad, a random number stored in the browser on the web.</li>
<li><strong>Stored on the server:</strong> not the identifier itself but only an irreversible SHA-256 hash (“chiave:” + identifier), together with page usage counts and your plan. No name, email or phone number is needed.</li>
<li><strong>Retention period:</strong> deleted one year after your last scan. Records of paid subscriptions are kept for as long as tax law requires (up to 10 years).</li>
</ul>
<p>Legal basis: providing your plan (b), preventing abuse of the free trial (f).</p>"""),
   ("Purchases and subscriptions", f"""<p>Pro and Pro+ subscriptions are bought through Google Play or the App Store. The store handles payment and card details; we never receive them. The store's processing falls under the <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Google Privacy Policy</a> or the <a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">Apple Privacy Policy</a>.</p>"""),
   ("Service providers (processors) and transfers", """<ul>
<li><strong>Supabase</strong> — server (Edge Function) and database, EU data centre (Frankfurt, Germany) (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">policy</a>)</li>
<li><strong>Google</strong> — Gemini API (score scanning), Google Play payments</li>
<li><strong>Apple</strong> — App Store payments (iPhone, iPad)</li>
</ul>
<p>Where these providers process data outside the EU (e.g. in the USA), this is based on the EU Standard Contractual Clauses or the EU-U.S. Data Privacy Framework.</p>"""),
   ("The welegato banner and external links", f"""<p>On the Free plan a link to welegato (a music platform of the same company, welegato.com) is shown at the bottom of the screen. It is our own link, not an ad network or tracking tool. Settings contains links to the store pages of other Vicino Labs apps and to welegato.com.</p>
<p>Links open in your browser or store <strong>only when you tap them</strong>. The banner link carries utm parameters (such as <code>utm_source=chiave</code>) that only say the visit came from the app, with no value that identifies you. Once open, that site's policy applies — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato privacy policy</a>.</p>"""),
   ("Sharing and export", """<p>When you export a score as PDF, PNG image, MusicXML or editable file, it goes — only if you choose to — through your device's share sheet or file picker to the app, place or person you pick.</p>"""),
   ("Data we don't collect", """<p>We receive no account data such as name, email or phone number. The app does not use the microphone, location, contacts or advertising ID, and contains no analytics SDK and no ad network.</p>"""),
   ("Children", """<p>There is no account and no age limit. Under 16, please use score scanning with a parent's consent. Children should use external links together with a parent.</p>"""),
   ("Your rights", f"""<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR)</li>
<li>Lodge a complaint with a supervisory authority — e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live</li>
</ul>
<p>Scores and scan images are only on your device, so deleting them in the app or uninstalling the app removes them. Records of your device hash on our server are deleted on request to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law or the app changes; changes and the effective date are posted on this page. A future version may offer sign-in with a welegato ID; this policy will then be updated.</p>"""),
   ("Contact", "<p>For questions about data protection, please contact us.</p>" + _contact("Operator")),
  ],
 },
 "de": {
  "title": "Chiave Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "06.11.2026"), ("Version", "1.0"), ("Betreiber", "Vicino Labs")],
  "lede": "Chiave von Vicino Labs ist eine App zum Schreiben, Scannen und Transponieren von Noten. Es gibt kein Konto; deine Noten, deine Bearbeitungen und die gescannten Originalseiten werden nur auf deinem Gerät gespeichert. Nur wenn du den Notenscan nutzt, gehen kleine Streifenbilder der Seiten über unseren Server (EU) und Google Gemini. Hier steht genau, welche Daten die App verarbeitet.",
  "footer": "Diese Erklärung gilt ab dem 6. November 2026 (Version 1.0).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _id_card("de") + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für Verarbeitungen im Zusammenhang mit dieser App.</p>"),
   ("Kurzfassung", """<div class="summary-box"><ul>
<li>Keine Registrierung und kein Konto. Noten, Bearbeitungen und gescannte Originalseiten bleiben <strong>auf deinem Gerät</strong> und werden in keine Cloud hochgeladen.</li>
<li>Beim <strong>Notenscan</strong> (freiwillig) schneidet die App jede Seite auf dem Gerät in kleine Streifen von etwa 2 Takten und sendet sie über unseren Server an Google Gemini, um die Noten zu lesen. Streifenbilder und Erkennungsergebnisse werden auf dem Server <strong>nicht gespeichert</strong>.</li>
<li>Um die Seiten deines Tarifs zu zählen, speichern wir nur einen <strong>Hash</strong> einer Gerätekennung.</li>
<li>Keine Werbenetzwerke und keine Analyse- oder Tracking-Tools. Der Link unten im Bildschirm im Free-Tarif ist unser eigenes Banner für welegato, einen Dienst desselben Unternehmens.</li>
<li>Die App nutzt weder Mikrofon noch Standort.</li>
</ul></div>"""),
   ("Auf dem Gerät gespeicherte Daten", """<ul>
<li>Von dir geschriebene oder gescannte Noten sowie deine Bearbeitungen und Transpositionen</li>
<li>Die Originalseiten, die du zum Scannen ausgewählt hast</li>
<li>App-Einstellungen</li>
<li>Auf iPhone und iPad eine zufällige Gerätenummer im Schlüsselbund, im Web eine im Browser gespeicherte Zufallsnummer (siehe „Tarife und Gerätekennung“ unten)</li>
</ul>
<p>Diese Daten bleiben im Speicher der App auf deinem Gerät und werden nicht an uns übermittelt – außer den Streifenbildern für den Scan (unten). Es gibt keine Cloud-Speicherung und keine Synchronisierung. Sie werden gelöscht, wenn du Noten entfernst oder die App deinstallierst. Die Gerätenummer im Schlüsselbund von iPhone/iPad dient jedoch dazu, eine Wiederholung der Testphase nach Neuinstallation zu verhindern, und kann daher nach dem Löschen der App erhalten bleiben. Rechtsgrundlage: Bereitstellung der App-Funktionen (Art. 6 Abs. 1 lit. b DSGVO).</p>"""),
   ("Kamera, Fotos und Dateien", """<p>Die App fragt nur nach der Kamera oder lässt dich Fotos aus dem Album oder eine PDF-Datei auswählen, wenn du Seiten zum Scannen wählst. Die ausgewählten Bilder werden auf dem Gerät gespeichert und verlassen es nicht – außer den Streifenbildern für den Scan (unten).</p>"""),
   ("Notenscan (freiwillig)", f"""<p>Der Notenscan ist freiwillig und läuft nur, wenn du Seiten (Kamera, Fotoalbum, PDF) auswählst und den Scan startest.</p>
<ul>
<li><strong>Gesendet werden:</strong> Die App schneidet jede Seite auf deinem Gerät in kleine Streifenbilder von etwa 2 Takten und sendet diese Streifen an unseren Server.</li>
<li><strong>Verarbeitung:</strong> Unser Server (Supabase Edge Function, EU) leitet jeden Streifen an die Gemini-API von Google weiter, die die Noten liest; das Ergebnis geht zurück an dein Gerät. Wir nutzen die kostenpflichtige API; Google verwendet diese Daten nicht zum Training seiner Modelle.</li>
<li><strong>Nicht gespeichert:</strong> Streifenbilder und Erkennungsergebnisse werden auf unserem Server nicht gespeichert.</li>
<li><strong>Auf dem Server bleiben:</strong> nur ein Hash der Gerätekennung, Zeitpunkt, Name des KI-Modells, Erfolgskennzeichen und Token-Anzahl. Speicherdauer: Löschung nach 90 Tagen.</li>
</ul>
<p>Rechtsgrundlage: Bereitstellung der gewünschten Funktion (Art. 6 Abs. 1 lit. b DSGVO); für das Server-Protokoll unser berechtigtes Interesse am Betrieb des Dienstes und am Missbrauchsschutz (lit. f). Google verarbeitet die Daten nach der <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von Google</a>.</p>"""),
   ("Tarife und Gerätekennung", f"""<p>Tarife werden in gescannten Notenseiten gezählt. Um Seiten zu zählen und zu verhindern, dass die Testphase durch Neuinstallation wiederholt wird, verwendet die App eine Gerätekennung.</p>
<ul>
<li><strong>Kennung:</strong> unter Android die ANDROID_ID, auf iPhone und iPad eine im Schlüsselbund gespeicherte Zufallsnummer, im Web eine im Browser gespeicherte Zufallsnummer.</li>
<li><strong>Auf dem Server gespeichert:</strong> nicht die Kennung selbst, sondern nur ein nicht umkehrbarer SHA-256-Hash („chiave:“ + Kennung), zusammen mit der Anzahl genutzter Seiten und deinem Tarif. Name, E-Mail oder Telefonnummer sind nicht nötig.</li>
<li><strong>Speicherdauer:</strong> Löschung ein Jahr nach dem letzten Scan. Aufzeichnungen zu bezahlten Abos bewahren wir so lange auf, wie es das Steuerrecht verlangt (bis zu 10 Jahre).</li>
</ul>
<p>Rechtsgrundlage: Bereitstellung deines Tarifs (lit. b), Missbrauchsschutz bei der Testphase (lit. f).</p>"""),
   ("Käufe und Abos", f"""<p>Pro- und Pro+-Abos kaufst du über Google Play oder den App Store. Zahlung und Kartendaten verarbeitet der Store; wir erhalten sie nicht. Für den Store gilt die <a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">Datenschutzerklärung von Google</a> bzw. die <a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">Datenschutzrichtlinie von Apple</a>.</p>"""),
   ("Dienstleister (Auftragsverarbeiter) und Übermittlungen", """<ul>
<li><strong>Supabase</strong> — Server (Edge Function) und Datenbank, EU-Rechenzentrum (Frankfurt) (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">Erklärung</a>)</li>
<li><strong>Google</strong> — Gemini-API (Notenscan), Google-Play-Zahlungen</li>
<li><strong>Apple</strong> — App-Store-Zahlungen (iPhone, iPad)</li>
</ul>
<p>Verarbeiten diese Anbieter Daten außerhalb der EU (z. B. in den USA), geschieht das auf Grundlage der EU-Standardvertragsklauseln oder des EU-U.S. Data Privacy Framework.</p>"""),
   ("welegato-Banner und externe Links", f"""<p>Im Free-Tarif wird unten im Bildschirm ein Link zu welegato (einer Musikplattform desselben Unternehmens, welegato.com) angezeigt. Es ist unser eigener Link, kein Werbenetzwerk und kein Tracking-Tool. In den Einstellungen gibt es Links zu den Store-Seiten anderer Apps von Vicino Labs und zu welegato.com.</p>
<p>Links öffnen sich im Browser oder Store <strong>nur, wenn du sie antippst</strong>. Der Banner-Link trägt utm-Parameter (z. B. <code>utm_source=chiave</code>), die nur sagen, dass der Besuch aus der App kommt, und dich nicht identifizieren. Danach gilt die Erklärung der jeweiligen Seite — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">welegato-Datenschutz</a>.</p>"""),
   ("Teilen und Export", """<p>Wenn du Noten als PDF, PNG-Bild, MusicXML oder bearbeitbare Datei exportierst, geht die Datei – nur wenn du es willst – über den Teilen-Dialog oder die Dateiauswahl des Geräts an die App, den Ort oder die Person, die du wählst.</p>"""),
   ("Nicht erhobene Daten", """<p>Wir erhalten keine Kontodaten wie Name, E-Mail-Adresse oder Telefonnummer. Die App nutzt weder Mikrofon, Standort, Kontakte noch Werbe-IDs und enthält kein Analyse-SDK und kein Werbenetzwerk.</p>"""),
   ("Kinder", """<p>Es gibt kein Konto und keine Altersgrenze. Unter 16 nutze den Notenscan bitte mit Einwilligung der Eltern. Kinder sollten externe Links gemeinsam mit Eltern nutzen.</p>"""),
   ("Deine Rechte", f"""<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO)</li>
<li>Beschwerde bei einer Aufsichtsbehörde — z. B. bei der Landesbeauftragten für Datenschutz und Informationsfreiheit NRW (LDI NRW) oder der Behörde deines Wohnorts</li>
</ul>
<p>Noten und Scanbilder liegen nur auf deinem Gerät; du löschst sie in der App oder durch Deinstallation. Einträge zu deinem Geräte-Hash auf unserem Server löschen wir auf Anfrage an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich Recht oder App ändern; Änderungen und das Datum stehen auf dieser Seite. Eine künftige Version kann die Anmeldung mit einer welegato-ID anbieten; diese Erklärung wird dann angepasst.</p>"""),
   ("Kontakt", "<p>Fragen zum Datenschutz richte bitte an:</p>" + _contact("Betreiber")),
  ],
 },
 "it": {
  "title": "Chiave — Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "06.11.2026"), ("Versione", "1.0"), ("Gestore", "Vicino Labs")],
  "lede": "Chiave, di Vicino Labs, è un'app per scrivere, scansionare e trasporre spartiti. Non c'è un account; i tuoi spartiti, le tue modifiche e le immagini originali delle pagine scansionate restano solo sul tuo dispositivo. Solo quando usi la scansione degli spartiti, piccole immagini a strisce delle pagine passano dal nostro server (UE) e da Google Gemini. Ecco esattamente quali dati tratta l'app.",
  "footer": "Questa informativa è in vigore dal 6 novembre 2026 (versione 1.0).",
  "other": "Termini di utilizzo →",
  "sections": [
   ("Titolare del trattamento", _id_card("it") + "<p>Vicino Labs è il titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per i dati trattati in relazione a questa app.</p>"),
   ("In breve", """<div class="summary-box"><ul>
<li>Nessuna registrazione e nessun account. Spartiti, modifiche e immagini originali delle pagine scansionate restano <strong>sul tuo dispositivo</strong> e non vengono caricati in alcun cloud.</li>
<li>Con la <strong>scansione degli spartiti</strong> (facoltativa) l'app taglia sul dispositivo ogni pagina in piccole strisce di circa 2 battute e le invia, tramite il nostro server, a Google Gemini per leggere le note. Le immagini a strisce e i risultati del riconoscimento <strong>non vengono salvati</strong> sul server.</li>
<li>Per contare le pagine del tuo piano salviamo sul server solo un <strong>hash</strong> di un identificativo del dispositivo.</li>
<li>Nessuna rete pubblicitaria e nessuno strumento di analisi o tracciamento. Il link in fondo allo schermo nel piano Free è il nostro banner per welegato, un servizio della stessa società.</li>
<li>L'app non usa il microfono né la posizione.</li>
</ul></div>"""),
   ("Dati salvati sul dispositivo", """<ul>
<li>Gli spartiti che scrivi o scansioni, con le tue modifiche e trasposizioni</li>
<li>Le immagini originali delle pagine scelte per la scansione</li>
<li>Le impostazioni dell'app</li>
<li>Su iPhone e iPad un numero casuale del dispositivo nel portachiavi, sul web un numero casuale salvato nel browser (vedi “Piani e identificativo del dispositivo” sotto)</li>
</ul>
<p>Questi dati restano nella memoria dell'app sul dispositivo e non ci vengono inviati, salvo le immagini a strisce inviate per la scansione (sotto). Non c'è archiviazione nel cloud né sincronizzazione. Si cancellano eliminando gli spartiti o disinstallando l'app. Il numero del dispositivo nel portachiavi di iPhone/iPad serve però a impedire che la prova gratuita si ripeta dopo una reinstallazione, quindi può restare anche dopo l'eliminazione dell'app. Base giuridica: fornitura delle funzioni dell'app (art. 6, par. 1, lett. b GDPR).</p>"""),
   ("Fotocamera, foto e file", """<p>L'app chiede la fotocamera, o ti fa scegliere foto dall'album o un file PDF, solo quando scegli le pagine da scansionare. Le immagini scelte restano sul dispositivo e non lo lasciano, salvo le immagini a strisce inviate per la scansione (sotto).</p>"""),
   ("Scansione degli spartiti (facoltativa)", f"""<p>La scansione degli spartiti è facoltativa e funziona solo quando scegli delle pagine (fotocamera, album, PDF) e avvii la scansione.</p>
<ul>
<li><strong>Cosa viene inviato:</strong> l'app taglia sul dispositivo ogni pagina in piccole immagini a strisce di circa 2 battute e invia queste strisce al nostro server.</li>
<li><strong>Trattamento:</strong> il nostro server (Supabase Edge Function, UE) inoltra ogni striscia all'API Gemini di Google, che legge le note; il risultato torna al tuo dispositivo. Usiamo l'API a pagamento; Google non usa questi dati per addestrare i propri modelli.</li>
<li><strong>Non salvato:</strong> le immagini a strisce e i risultati del riconoscimento non vengono salvati sul nostro server.</li>
<li><strong>Sul server restano:</strong> solo un hash dell'identificativo del dispositivo, il momento, il nome del modello AI, l'esito (riuscito o no) e il numero di token. Periodo di conservazione: cancellati dopo 90 giorni.</li>
</ul>
<p>Base giuridica: fornire la funzione richiesta (art. 6, par. 1, lett. b GDPR); per il registro del server, il nostro legittimo interesse a gestire il servizio e prevenire abusi (lett. f). Google tratta i dati secondo l'<a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">informativa privacy di Google</a>.</p>"""),
   ("Piani e identificativo del dispositivo", f"""<p>I piani si contano in pagine di spartito scansionate. Per contare le pagine e impedire che la prova gratuita si ripeta reinstallando l'app, si usa un identificativo del dispositivo.</p>
<ul>
<li><strong>Identificativo:</strong> ANDROID_ID su Android, un numero casuale salvato nel portachiavi su iPhone e iPad, un numero casuale salvato nel browser sul web.</li>
<li><strong>Salvato sul server:</strong> non l'identificativo stesso ma solo un hash SHA-256 irreversibile («chiave:» + identificativo), insieme al numero di pagine usate e al tuo piano. Non servono nome, email né numero di telefono.</li>
<li><strong>Periodo di conservazione:</strong> cancellati un anno dopo l’ultima scansione. I dati sugli abbonamenti a pagamento sono conservati per il periodo richiesto dalla legge fiscale (fino a 10 anni).</li>
</ul>
<p>Base giuridica: fornire il tuo piano (lett. b), prevenire abusi della prova gratuita (lett. f).</p>"""),
   ("Acquisti e abbonamenti", f"""<p>Gli abbonamenti Pro e Pro+ si acquistano tramite Google Play o l'App Store. Il pagamento e i dati della carta li gestisce lo store; noi non li riceviamo. Per lo store vale l'<a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">informativa privacy di Google</a> o l'<a href="{APPLE_PRIVACY}" target="_blank" rel="noopener">informativa privacy di Apple</a>.</p>"""),
   ("Fornitori di servizi (responsabili) e trasferimenti", """<ul>
<li><strong>Supabase</strong> — server (Edge Function) e database, data center UE (Francoforte) (<a href="https://supabase.com/privacy" target="_blank" rel="noopener">informativa</a>)</li>
<li><strong>Google</strong> — API Gemini (scansione degli spartiti), pagamenti Google Play</li>
<li><strong>Apple</strong> — pagamenti App Store (iPhone, iPad)</li>
</ul>
<p>Se questi fornitori trattano dati fuori dall'UE (ad es. negli USA), ciò avviene in base alle Clausole contrattuali standard UE o all'EU-U.S. Data Privacy Framework.</p>"""),
   ("Banner welegato e link esterni", f"""<p>Nel piano Free, in fondo allo schermo compare un link a welegato (una piattaforma musicale della stessa azienda, welegato.com). È un nostro link, non una rete pubblicitaria né uno strumento di tracciamento. Nelle impostazioni ci sono link alle pagine store delle altre app di Vicino Labs e a welegato.com.</p>
<p>I link si aprono nel browser o nello store <strong>solo quando li tocchi</strong>. Il link del banner porta parametri utm (ad es. <code>utm_source=chiave</code>) che indicano solo che la visita arriva dall'app e non ti identificano. Poi si applica l'informativa del sito aperto — <a href="{WELEGATO_PRIVACY}" target="_blank" rel="noopener">privacy di welegato</a>.</p>"""),
   ("Condivisione ed esportazione", """<p>Quando esporti uno spartito come PDF, immagine PNG, MusicXML o file modificabile, il file va – solo se lo scegli tu – tramite la finestra di condivisione o la selezione file del dispositivo all'app, al luogo o alla persona che scegli.</p>"""),
   ("Dati che non raccogliamo", """<p>Non riceviamo dati di account come nome, email o numero di telefono. L'app non usa microfono, posizione, contatti né ID pubblicitari, e non contiene SDK di analisi né reti pubblicitarie.</p>"""),
   ("Minori", """<p>Non c'è un account e non ci sono limiti di età. Sotto i 16 anni, usa la scansione degli spartiti con il consenso di un genitore. I bambini dovrebbero usare i link esterni insieme a un genitore.</p>"""),
   ("I tuoi diritti", f"""<ul>
<li>Accesso, rettifica, cancellazione, limitazione, portabilità e opposizione (artt. 15–21 GDPR)</li>
<li>Reclamo a un'autorità di controllo — ad es. l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o quella del tuo luogo di residenza</li>
</ul>
<p>Spartiti e immagini scansionate sono solo sul dispositivo: li elimini nell'app o disinstallandola. I dati relativi all'hash del tuo dispositivo sul nostro server vengono cancellati su richiesta a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
   ("Modifiche", """<p>Possiamo aggiornare questa informativa se cambiano la legge o l'app; modifiche e data di entrata in vigore sono pubblicate in questa pagina. Una versione futura potrà offrire l'accesso con un welegato ID; in quel caso l'informativa sarà aggiornata.</p>"""),
   ("Contatti", "<p>Per domande sulla protezione dei dati scrivici:</p>" + _contact("Gestore")),
  ],
 },
}
