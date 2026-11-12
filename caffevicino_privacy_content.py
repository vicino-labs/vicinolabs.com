"""Caffè Vicino 개인정보처리방침 본문 (ko/en/de/it) — caffevicino_legal.py가 HTML로 만든다.

2026-11-12 버전 1.0 초안(운영자 승인 전). Caffè Vicino는 앱이 아니라 유튜브 채널(@caffevicino)이다.
- 시청자: 저희가 직접 모으는 개인정보 없음. 유튜브(구글)가 자기 방침으로 처리. 저희는 YouTube 스튜디오의
  익명 합계 통계와 공개 댓글만 본다.
- 업로드 도구 "caffevicino"(Google Cloud OAuth 앱): Vicino Labs만 쓰는 내부 도구, 자기 채널에만
  YouTube Data API로 올린다(scope youtube.upload, youtube). 토큰은 운영자 컴퓨터에만.
  Google API Services User Data Policy(Limited Use), YouTube 약관·Google 방침 링크는 API 정책상 필수.
운영자 이름·주소 카드는 마지막 "문의처"에만(legal_owner 규칙), 1절은 안내 한 줄.
"""

from appoggio_privacy_content import EMAIL, _id_card
from legal_owner import op_ref

CHANNEL = "https://www.youtube.com/@caffevicino"
YT_TERMS = "https://www.youtube.com/t/terms"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
GOOGLE_PERMISSIONS = "https://myaccount.google.com/permissions"
GOOGLE_API_POLICY = "https://developers.google.com/terms/api-services-user-data-policy"

_OP = "@@OP@@"  # finish()가 마지막 절 번호를 넣은 안내 줄로 바꾼다


def _a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


def finish(docs):
    """1절의 자리표시를 '이 문서 맨 아래(#<lang>-<마지막 절>)' 안내 줄로 바꾼다."""
    for lang, d in docs.items():
        n = len(d["sections"])
        d["sections"] = [(t, b.replace(_OP, op_ref(lang, n))) for t, b in d["sections"]]
    return docs


PRIVACY = finish({
 "ko": {
  "title": "Caffè Vicino 개인정보처리방침",
  "h1": "개인정보처리방침",
  "meta": [("시행일", "2026.11.12"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "Caffè Vicino는 Vicino Labs가 운영하는 유튜브 채널로, 카페와 집중, 휴식을 위한 음악을 올립니다. 저희는 시청자의 개인정보를 직접 수집하지 않으며, 시청에 따르는 정보는 유튜브(Google)가 자체 개인정보처리방침에 따라 처리합니다. 이 방침은 저희가 자기 채널에 영상을 올릴 때 쓰는 내부 도구 “caffevicino”에도 적용됩니다.",
  "footer": "본 방침은 2026년 11월 12일부터 시행됩니다 (버전 1.0).",
  "other": "이용약관 보기 →",
  "sections": [
   ("처리자(운영자) 정보", _OP + "<p>Vicino Labs는 Caffè Vicino 채널과 업로드 도구 caffevicino와 관련해 저희가 직접 처리하는 개인정보에 대해 EU 일반개인정보보호규정(GDPR)상 “컨트롤러(controller)”입니다. 유튜브 안에서 이루어지는 처리는 Google이 자체 방침에 따라 책임집니다.</p>"),
   ("핵심 요약", """<div class="summary-box"><ul>
<li>저희는 시청자의 개인정보를 <strong>직접 수집하지 않습니다</strong>. 영상은 유튜브에서 재생되며, 그때 생기는 정보는 Google이 처리합니다.</li>
<li>저희가 보는 것은 YouTube 스튜디오의 <strong>익명 합계 통계</strong>와, 시청자가 채널에 <strong>공개로 남긴 댓글</strong>뿐입니다.</li>
<li>업로드 도구 caffevicino는 <strong>Vicino Labs만</strong> 쓰며, <strong>저희 채널에만</strong> 접근합니다. 다른 사람의 유튜브 계정이나 정보에는 접근하지 않습니다.</li>
<li>개인정보를 팔거나 제3자에게 넘기지 않으며, 광고나 AI 학습에 쓰지 않습니다.</li>
</ul></div>"""),
   ("유튜브에서 시청할 때", f"""<p>채널은 Google이 운영하는 서비스인 유튜브에 있습니다. 영상을 보실 때 유튜브는 IP 주소, 기기 정보, 시청 기록, 로그인한 경우 Google 계정 정보 등을 {_a(GOOGLE_PRIVACY, "Google 개인정보처리방침")}에 따라 처리합니다. 이 과정에서 정보가 EU 밖에서 처리될 수 있으며, 그 조건도 Google의 방침이 정합니다.</p>
<p>저희는 이 정보를 볼 수 없고, 유튜브가 무엇을 어떻게 처리할지 정하지도 않습니다. 광고 개인 맞춤 등 본인 정보에 관한 설정은 Google 계정에서 직접 바꾸실 수 있습니다.</p>"""),
   ("저희가 보는 통계", """<p>YouTube 스튜디오는 채널 운영자에게 조회수, 시청 시간, 시청 국가, 연령대와 같은 통계를 보여 줍니다. 이 통계는 여러 시청자를 합친 익명 수치이며, 저희는 이것으로 누가 시청했는지 알 수 없습니다. 어떤 영상이 도움이 되는지 살피는 데만 씁니다. 처리 근거: 정당한 이익(GDPR 제6조 제1항 f호).</p>"""),
   ("댓글", """<p>채널에 댓글을 남기시면 댓글 내용과 유튜브 사용자 이름이 공개되어 저희를 포함한 누구나 볼 수 있습니다.</p>
<ul>
<li>저희는 댓글을 읽고 답글을 달 수 있습니다.</li>
<li>유튜브 규정이나 법령에 어긋나는 댓글(스팸, 광고, 욕설, 타인의 권리를 침해하는 내용 등)은 숨기거나 삭제할 수 있습니다.</li>
<li>댓글과 사용자 이름을 유튜브 밖으로 옮겨 따로 보관하지 않습니다.</li>
<li>본인이 쓴 댓글은 유튜브에서 언제든지 직접 지우실 수 있습니다.</li>
</ul>
<p>처리 근거: 채널을 운영하고 관리하는 정당한 이익(GDPR 제6조 제1항 f호).</p>"""),
   ("이메일 문의", f"""<p><a href="mailto:{EMAIL}">{EMAIL}</a>로 메일을 보내시면 이메일 주소, 이름, 메일 내용을 문의에 답하는 데만 씁니다. 문의가 마무리되어 더 필요하지 않게 되면 삭제하며, 법령이 보관을 요구하는 경우에는 그 기간 동안만 보관합니다. 처리 근거: 문의에 답하는 정당한 이익(GDPR 제6조 제1항 f호), 이용 허락 등 계약에 관한 문의는 같은 항 b호.</p>"""),
   ("업로드 도구 caffevicino (YouTube API 서비스)", f"""<p>caffevicino는 저희가 Google Cloud에 같은 이름의 OAuth 앱으로 등록한 내부 도구이며, YouTube API 서비스(YouTube Data API)를 사용합니다. Vicino Labs만 사용하고, 일반에 제공하지 않습니다.</p>
<ul>
<li><strong>하는 일</strong> — Vicino Labs의 유튜브 채널에 영상, 미리보기 이미지, 제목·설명과 그 번역을 올리고 재생목록을 관리합니다.</li>
<li><strong>접근 권한</strong> — <code>youtube.upload</code>와 <code>youtube</code>. 이 권한으로 저희 채널의 정보(영상, 재생목록, 영상 정보 등)만 읽고 씁니다. 다른 사람의 유튜브 계정이나 정보에는 접근하지 않습니다.</li>
<li><strong>보관</strong> — Google이 발급한 인증 토큰(OAuth 토큰)은 운영자 본인의 컴퓨터에만 저장되며, 서버에 올리지 않습니다.</li>
<li><strong>이용 범위</strong> — Google API로 받은 정보는 위 업로드와 채널 관리에만 씁니다. 팔거나 제3자에게 넘기지 않으며, 광고에도, AI·머신러닝 모델 학습에도 쓰지 않습니다.</li>
<li><strong>Google 정책 준수</strong> — 이 도구가 Google API로 받은 정보를 이용하고 이전하는 방식은 제한적 사용(Limited Use) 요건을 포함한 {_a(GOOGLE_API_POLICY, "Google API 서비스 사용자 데이터 정책")}을 따릅니다.</li>
<li><strong>권한 철회</strong> — 도구에 준 접근 권한은 채널 계정의 {_a(GOOGLE_PERMISSIONS, "Google 계정 권한 페이지")}에서 언제든지 철회할 수 있습니다. 철회하면 컴퓨터에 남은 토큰은 더 쓸 수 없게 됩니다.</li>
</ul>
<p>YouTube API 서비스를 사용하므로 이 도구의 이용에는 {_a(YT_TERMS, "YouTube 서비스 약관")}이 적용되며, Google이 처리하는 정보에는 {_a(GOOGLE_PRIVACY, "Google 개인정보처리방침")}이 적용됩니다.</p>"""),
   ("이 웹사이트", """<p>이 웹사이트(vicinolabs.com)를 방문할 때의 정보 처리는 <a href="/datenschutz/">Datenschutz</a>(웹사이트 개인정보처리방침)에 따로 적혀 있습니다.</p>"""),
   ("정보주체의 권리", f"""<ul>
<li>열람·정정·삭제·처리제한·데이터 이동·이의제기권(GDPR 제15~21조)</li>
<li>감독기관에 민원을 제기할 권리 — 예: 노르트라인베스트팔렌주 정보보호·정보자유 감독관(LDI NRW) 또는 거주지 관할 감독기관</li>
</ul>
<p>저희가 갖고 있는 시청자 정보는 보내 주신 이메일뿐입니다. 유튜브가 처리하는 정보(시청 기록, 계정 정보, 댓글 등)에 대한 권리는 Google 계정 설정이나 Google에 직접 행사하실 수 있습니다. 저희에게 요청하실 일은 아래로 연락해 주세요.</p>"""),
   ("방침의 변경", """<p>법령이나 채널 운영 방식, 업로드 도구가 바뀌면 본 방침을 고칠 수 있습니다. 변경 내용과 시행일은 이 페이지에 게시합니다.</p>"""),
   ("문의처", "<p>개인정보 처리에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },

 "en": {
  "title": "Caffè Vicino Privacy Policy",
  "h1": "Privacy Policy",
  "meta": [("Effective", "2026-11-12"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "Caffè Vicino is a YouTube channel run by Vicino Labs with music for cafés, focus and rest. We do not collect viewers' personal data ourselves; the data that arises when you watch is processed by YouTube (Google) under its own privacy policy. This policy also covers “caffevicino”, the internal tool we use to upload videos to our own channels.",
  "footer": "This policy is effective from 12 November 2026 (version 1.0).",
  "other": "Terms of Use →",
  "sections": [
   ("Data controller", _OP + "<p>Vicino Labs is the “controller” under the EU General Data Protection Regulation (GDPR) for the personal data we ourselves process in connection with the Caffè Vicino channel and the caffevicino upload tool. Processing that takes place within YouTube is the responsibility of Google under its own policy.</p>"),
   ("Summary", """<div class="summary-box"><ul>
<li>We <strong>do not collect</strong> viewers' personal data ourselves. Videos play on YouTube, and the data that arises there is processed by Google.</li>
<li>All we see are <strong>aggregated, anonymous statistics</strong> in YouTube Studio and the <strong>comments viewers post publicly</strong> on the channel.</li>
<li>The caffevicino upload tool is used <strong>only by Vicino Labs</strong> and accesses <strong>only our own channels</strong>. It does not access any other person's YouTube account or data.</li>
<li>We do not sell personal data or pass it on to third parties, and we do not use it for advertising or AI training.</li>
</ul></div>"""),
   ("Watching on YouTube", f"""<p>The channel is hosted on YouTube, a service operated by Google. When you watch a video, YouTube processes data such as your IP address, device information, viewing activity and, if you are signed in, your Google account data in accordance with the {_a(GOOGLE_PRIVACY, "Google Privacy Policy")}. This may involve processing outside the EU; the conditions for that are also set out in Google's policy.</p>
<p>We cannot see this data and do not decide what YouTube processes or how. You can change settings concerning your data, such as ad personalisation, in your Google account.</p>"""),
   ("Statistics we see", """<p>YouTube Studio shows channel owners statistics such as views, watch time, viewers' countries and age ranges. These are aggregated, anonymous figures; we cannot tell from them who watched. We use them only to understand which videos are useful. Legal basis: legitimate interests (Art. 6(1)(f) GDPR).</p>"""),
   ("Comments", """<p>If you post a comment on the channel, the comment and your YouTube username are public and visible to everyone, including us.</p>
<ul>
<li>We read comments and may reply to them.</li>
<li>We may hide or delete comments that break YouTube's rules or the law (such as spam, advertising, insults or content infringing other people's rights).</li>
<li>We do not copy comments or usernames out of YouTube to keep them elsewhere.</li>
<li>You can delete your own comments on YouTube at any time.</li>
</ul>
<p>Legal basis: our legitimate interest in running and moderating the channel (Art. 6(1)(f) GDPR).</p>"""),
   ("Email enquiries", f"""<p>If you write to <a href="mailto:{EMAIL}">{EMAIL}</a>, we use your email address, your name and the content of your message only to answer you. We delete the correspondence once the matter is settled and it is no longer needed, unless the law requires us to keep it, and then only for that period. Legal basis: our legitimate interest in answering enquiries (Art. 6(1)(f) GDPR); for enquiries about a contract, such as a licence, Art. 6(1)(b) GDPR.</p>"""),
   ("The caffevicino upload tool (YouTube API Services)", f"""<p>caffevicino is an internal tool that we have registered under that name as an OAuth app in Google Cloud. It uses YouTube API Services (the YouTube Data API). Only Vicino Labs uses it; it is not offered to the public.</p>
<ul>
<li><strong>What it does</strong> — uploads videos, thumbnails, titles, descriptions and their translations to Vicino Labs' own YouTube channels and manages playlists there.</li>
<li><strong>Access (scopes)</strong> — <code>youtube.upload</code> and <code>youtube</code>. With these it reads and writes only the data of our own channels (for example videos, playlists and video details). It does not access any other person's YouTube account or data.</li>
<li><strong>Storage</strong> — the authorisation tokens issued by Google (OAuth tokens) are stored only on the operator's own computer, not on a server.</li>
<li><strong>Use</strong> — information received from Google APIs is used only for the uploading and channel management described above. It is not sold, not transferred to third parties, not used for advertising and not used to train AI or machine-learning models.</li>
<li><strong>Google policy</strong> — the tool's use and transfer of information received from Google APIs adheres to the {_a(GOOGLE_API_POLICY, "Google API Services User Data Policy")}, including the Limited Use requirements.</li>
<li><strong>Revoking access</strong> — access granted to the tool can be revoked at any time on the {_a(GOOGLE_PERMISSIONS, "Google account permissions page")} of the channel's account. After that, the tokens left on the computer no longer work.</li>
</ul>
<p>Because the tool uses YouTube API Services, its use is subject to the {_a(YT_TERMS, "YouTube Terms of Service")}, and data processed by Google is subject to the {_a(GOOGLE_PRIVACY, "Google Privacy Policy")}.</p>"""),
   ("This website", """<p>How data is processed when you visit this website (vicinolabs.com) is described separately under <a href="/datenschutz/">Datenschutz</a> (website privacy policy).</p>"""),
   ("Your rights", """<ul>
<li>Access, rectification, erasure, restriction of processing, data portability and objection (Art. 15–21 GDPR)</li>
<li>Lodge a complaint with a supervisory authority — e.g. the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia (LDI NRW) or the authority where you live</li>
</ul>
<p>The only viewer data we hold ourselves are the emails you send us. For data processed by YouTube (viewing activity, account data, comments and so on), you can exercise your rights in your Google account settings or directly with Google. For anything you wish to ask of us, please contact us below.</p>"""),
   ("Changes to this policy", """<p>We may update this policy when the law, the way we run the channel or the upload tool changes; changes and the effective date are posted on this page.</p>"""),
   ("Contact", "<p>For questions about data processing, please contact:</p>" + _id_card("en")),
  ],
 },

 "de": {
  "title": "Caffè Vicino Datenschutzerklärung",
  "h1": "Datenschutzerklärung",
  "meta": [("Gültig ab", "12.11.2026"), ("Version", "1.0"), ("Anbieter", "Vicino Labs")],
  "lede": "Caffè Vicino ist ein YouTube-Kanal von Vicino Labs mit Musik für Cafés, zum Konzentrieren und zum Entspannen. Wir selbst erheben keine personenbezogenen Daten der Zuschauerinnen und Zuschauer; die beim Ansehen anfallenden Daten verarbeitet YouTube (Google) nach seiner eigenen Datenschutzerklärung. Diese Erklärung gilt auch für „caffevicino“, das interne Werkzeug, mit dem wir Videos auf unsere eigenen Kanäle hochladen.",
  "footer": "Diese Erklärung gilt ab dem 12. November 2026 (Version 1.0).",
  "other": "Nutzungsbedingungen →",
  "sections": [
   ("Verantwortlicher", _OP + "<p>Vicino Labs ist Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) für die personenbezogenen Daten, die wir selbst im Zusammenhang mit dem Kanal Caffè Vicino und dem Upload-Werkzeug caffevicino verarbeiten. Für die Verarbeitung innerhalb von YouTube ist Google nach seiner eigenen Datenschutzerklärung verantwortlich.</p>"),
   ("Das Wichtigste in Kürze", """<div class="summary-box"><ul>
<li>Wir selbst <strong>erheben keine</strong> personenbezogenen Daten der Zuschauer. Die Videos laufen auf YouTube; die dort anfallenden Daten verarbeitet Google.</li>
<li>Wir sehen nur <strong>zusammengefasste, anonyme Statistiken</strong> in YouTube Studio und die <strong>Kommentare, die öffentlich</strong> auf dem Kanal hinterlassen werden.</li>
<li>Das Upload-Werkzeug caffevicino wird <strong>nur von Vicino Labs</strong> genutzt und greift <strong>nur auf unsere eigenen Kanäle</strong> zu, nicht auf YouTube-Konten oder Daten anderer Personen.</li>
<li>Wir verkaufen keine personenbezogenen Daten, geben sie nicht an Dritte weiter und nutzen sie weder für Werbung noch für KI-Training.</li>
</ul></div>"""),
   ("Ansehen auf YouTube", f"""<p>Der Kanal befindet sich auf YouTube, einem Dienst von Google. Wenn Sie ein Video ansehen, verarbeitet YouTube Daten wie Ihre IP-Adresse, Geräteinformationen, Ihr Nutzungsverhalten und, wenn Sie angemeldet sind, Daten Ihres Google-Kontos nach der {_a(GOOGLE_PRIVACY, "Datenschutzerklärung von Google")}. Dabei können Daten auch außerhalb der EU verarbeitet werden; die Bedingungen dafür ergeben sich ebenfalls aus der Datenschutzerklärung von Google.</p>
<p>Wir können diese Daten nicht einsehen und bestimmen nicht, was YouTube wie verarbeitet. Einstellungen zu Ihren Daten, etwa zur personalisierten Werbung, können Sie in Ihrem Google-Konto ändern.</p>"""),
   ("Statistiken, die wir sehen", """<p>YouTube Studio zeigt Kanalbetreibern Statistiken wie Aufrufe, Wiedergabezeit, Länder und Altersgruppen der Zuschauer. Das sind zusammengefasste, anonyme Werte; wir können daraus nicht erkennen, wer ein Video angesehen hat. Wir nutzen sie nur, um zu verstehen, welche Videos hilfreich sind. Rechtsgrundlage: berechtigtes Interesse (Art. 6 Abs. 1 lit. f DSGVO).</p>"""),
   ("Kommentare", """<p>Wenn Sie auf dem Kanal einen Kommentar schreiben, sind der Kommentar und Ihr YouTube-Nutzername öffentlich und für alle sichtbar, auch für uns.</p>
<ul>
<li>Wir lesen Kommentare und antworten gegebenenfalls darauf.</li>
<li>Kommentare, die gegen die Regeln von YouTube oder gegen geltendes Recht verstoßen (etwa Spam, Werbung, Beleidigungen oder Inhalte, die Rechte anderer verletzen), können wir ausblenden oder löschen.</li>
<li>Wir übertragen Kommentare und Nutzernamen nicht aus YouTube heraus, um sie an anderer Stelle zu speichern.</li>
<li>Ihre eigenen Kommentare können Sie auf YouTube jederzeit selbst löschen.</li>
</ul>
<p>Rechtsgrundlage: unser berechtigtes Interesse am Betrieb und an der Moderation des Kanals (Art. 6 Abs. 1 lit. f DSGVO).</p>"""),
   ("Anfragen per E-Mail", f"""<p>Wenn Sie uns an <a href="mailto:{EMAIL}">{EMAIL}</a> schreiben, verwenden wir Ihre E-Mail-Adresse, Ihren Namen und den Inhalt Ihrer Nachricht nur, um Ihnen zu antworten. Wir löschen den Schriftwechsel, sobald das Anliegen erledigt ist und er nicht mehr benötigt wird, sofern keine gesetzlichen Aufbewahrungspflichten bestehen; in diesem Fall nur für deren Dauer. Rechtsgrundlage: unser berechtigtes Interesse an der Beantwortung von Anfragen (Art. 6 Abs. 1 lit. f DSGVO); bei Anfragen zu einem Vertrag, etwa einer Lizenz, Art. 6 Abs. 1 lit. b DSGVO.</p>"""),
   ("Das Upload-Werkzeug caffevicino (YouTube-API-Dienste)", f"""<p>caffevicino ist ein internes Werkzeug, das wir unter diesem Namen als OAuth-App in Google Cloud registriert haben. Es nutzt die YouTube-API-Dienste (YouTube Data API). Nur Vicino Labs verwendet es; es wird nicht öffentlich angeboten.</p>
<ul>
<li><strong>Zweck</strong> — Es lädt Videos, Vorschaubilder, Titel, Beschreibungen und deren Übersetzungen auf die eigenen YouTube-Kanäle von Vicino Labs hoch und verwaltet dort Playlists.</li>
<li><strong>Zugriff (Scopes)</strong> — <code>youtube.upload</code> und <code>youtube</code>. Damit liest und schreibt das Werkzeug ausschließlich Daten unserer eigenen Kanäle (zum Beispiel Videos, Playlists und Videodetails). Es greift nicht auf YouTube-Konten oder Daten anderer Personen zu.</li>
<li><strong>Speicherung</strong> — Die von Google ausgestellten Zugriffstoken (OAuth-Token) werden nur auf dem eigenen Computer des Betreibers gespeichert, nicht auf einem Server.</li>
<li><strong>Verwendung</strong> — Über Google-APIs erhaltene Informationen werden nur für das oben beschriebene Hochladen und die Kanalverwaltung verwendet. Sie werden nicht verkauft, nicht an Dritte weitergegeben, nicht für Werbung und nicht zum Training von KI- oder Machine-Learning-Modellen genutzt.</li>
<li><strong>Google-Richtlinie</strong> — Die Verwendung und Weitergabe von Informationen, die das Werkzeug über Google-APIs erhält, entspricht der {_a(GOOGLE_API_POLICY, "Google API Services User Data Policy")} einschließlich der Anforderungen zur eingeschränkten Nutzung (Limited Use).</li>
<li><strong>Widerruf</strong> — Der dem Werkzeug erteilte Zugriff kann jederzeit auf der {_a(GOOGLE_PERMISSIONS, "Berechtigungsseite des Google-Kontos")} des Kanals widerrufen werden. Danach sind die auf dem Computer verbliebenen Token unbrauchbar.</li>
</ul>
<p>Da das Werkzeug die YouTube-API-Dienste nutzt, gelten für seine Nutzung die {_a(YT_TERMS, "YouTube-Nutzungsbedingungen")}; für die von Google verarbeiteten Daten gilt die {_a(GOOGLE_PRIVACY, "Datenschutzerklärung von Google")}.</p>"""),
   ("Diese Website", """<p>Wie beim Besuch dieser Website (vicinolabs.com) Daten verarbeitet werden, steht gesondert unter <a href="/datenschutz/">Datenschutz</a>.</p>"""),
   ("Ihre Rechte", """<ul>
<li>Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO)</li>
<li>Beschwerde bei einer Aufsichtsbehörde — z. B. der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW) oder der Behörde an Ihrem Wohnort</li>
</ul>
<p>Die einzigen Daten von Zuschauern, die wir selbst speichern, sind E-Mails, die Sie uns schicken. Für Daten, die YouTube verarbeitet (Nutzungsverhalten, Kontodaten, Kommentare usw.), können Sie Ihre Rechte in den Einstellungen Ihres Google-Kontos oder direkt gegenüber Google ausüben. Mit Anliegen an uns erreichen Sie uns unten.</p>"""),
   ("Änderungen", """<p>Wir können diese Erklärung anpassen, wenn sich das Recht, der Betrieb des Kanals oder das Upload-Werkzeug ändern; Änderungen und Gültigkeitsdatum veröffentlichen wir auf dieser Seite.</p>"""),
   ("Kontakt", "<p>Für Fragen zur Datenverarbeitung:</p>" + _id_card("de")),
  ],
 },

 "it": {
  "title": "Caffè Vicino — Informativa sulla privacy",
  "h1": "Informativa sulla privacy",
  "meta": [("In vigore dal", "12/11/2026"), ("Versione", "1.0"), ("Titolare", "Vicino Labs")],
  "lede": "Caffè Vicino è un canale YouTube di Vicino Labs con musica per il caffè, la concentrazione e il riposo. Non raccogliamo direttamente dati personali degli spettatori; i dati generati dalla visione sono trattati da YouTube (Google) secondo la propria informativa. Questa informativa riguarda anche “caffevicino”, lo strumento interno con cui carichiamo i video sui nostri canali.",
  "footer": "La presente informativa è in vigore dal 12 novembre 2026 (versione 1.0).",
  "other": "Termini di utilizzo →",
  "sections": [
   ("Titolare del trattamento", _OP + "<p>Vicino Labs è il titolare del trattamento ai sensi del Regolamento generale sulla protezione dei dati (GDPR) per i dati personali che trattiamo direttamente in relazione al canale Caffè Vicino e allo strumento di caricamento caffevicino. Del trattamento che avviene all'interno di YouTube è responsabile Google, secondo la propria informativa.</p>"),
   ("In breve", """<div class="summary-box"><ul>
<li><strong>Non raccogliamo</strong> direttamente dati personali degli spettatori. I video si guardano su YouTube e i dati che ne derivano sono trattati da Google.</li>
<li>Vediamo soltanto <strong>statistiche aggregate e anonime</strong> in YouTube Studio e i <strong>commenti pubblicati</strong> sul canale.</li>
<li>Lo strumento di caricamento caffevicino è usato <strong>solo da Vicino Labs</strong> e accede <strong>solo ai nostri canali</strong>, mai all'account YouTube o ai dati di altre persone.</li>
<li>Non vendiamo dati personali, non li cediamo a terzi e non li usiamo per pubblicità né per addestrare sistemi di IA.</li>
</ul></div>"""),
   ("Guardare i video su YouTube", f"""<p>Il canale si trova su YouTube, un servizio di Google. Quando guardi un video, YouTube tratta dati come l'indirizzo IP, le informazioni sul dispositivo, l'attività di visione e, se hai effettuato l'accesso, i dati del tuo account Google, secondo le {_a(GOOGLE_PRIVACY, "Norme sulla privacy di Google")}. I dati possono essere trattati anche fuori dall'UE; anche le relative condizioni sono indicate nelle norme di Google.</p>
<p>Noi non possiamo vedere questi dati e non decidiamo che cosa YouTube tratta né come. Puoi modificare le impostazioni sui tuoi dati, ad esempio la personalizzazione degli annunci, nel tuo account Google.</p>"""),
   ("Le statistiche che vediamo", """<p>YouTube Studio mostra a chi gestisce un canale statistiche come visualizzazioni, tempo di visualizzazione, paesi e fasce d'età degli spettatori. Sono valori aggregati e anonimi: non ci permettono di sapere chi ha guardato un video. Li usiamo solo per capire quali video sono utili. Base giuridica: legittimo interesse (art. 6, par. 1, lett. f GDPR).</p>"""),
   ("Commenti", """<p>Se scrivi un commento sul canale, il commento e il tuo nome utente YouTube sono pubblici e visibili a tutti, noi compresi.</p>
<ul>
<li>Leggiamo i commenti e possiamo rispondere.</li>
<li>Possiamo nascondere o eliminare i commenti contrari alle regole di YouTube o alla legge (ad es. spam, pubblicità, insulti o contenuti che violano diritti altrui).</li>
<li>Non copiamo commenti e nomi utente fuori da YouTube per conservarli altrove.</li>
<li>Puoi eliminare i tuoi commenti su YouTube in qualsiasi momento.</li>
</ul>
<p>Base giuridica: il nostro legittimo interesse a gestire e moderare il canale (art. 6, par. 1, lett. f GDPR).</p>"""),
   ("Richieste via e-mail", f"""<p>Se scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a>, usiamo il tuo indirizzo e-mail, il tuo nome e il contenuto del messaggio solo per risponderti. Cancelliamo la corrispondenza quando la richiesta è conclusa e non serve più, salvo obblighi di conservazione previsti dalla legge e, in tal caso, solo per la durata prevista. Base giuridica: il nostro legittimo interesse a rispondere alle richieste (art. 6, par. 1, lett. f GDPR); per richieste relative a un contratto, ad esempio una licenza, art. 6, par. 1, lett. b GDPR.</p>"""),
   ("Lo strumento di caricamento caffevicino (Servizi API di YouTube)", f"""<p>caffevicino è uno strumento interno che abbiamo registrato con questo nome come app OAuth in Google Cloud. Utilizza i Servizi API di YouTube (YouTube Data API). Lo usa soltanto Vicino Labs; non è offerto al pubblico.</p>
<ul>
<li><strong>A che cosa serve</strong> — carica video, miniature, titoli, descrizioni e relative traduzioni sui canali YouTube di Vicino Labs e ne gestisce le playlist.</li>
<li><strong>Accesso (ambiti)</strong> — <code>youtube.upload</code> e <code>youtube</code>. Con questi ambiti lo strumento legge e scrive soltanto i dati dei nostri canali (ad esempio video, playlist e dettagli dei video). Non accede all'account YouTube o ai dati di altre persone.</li>
<li><strong>Conservazione</strong> — i token di autorizzazione rilasciati da Google (token OAuth) sono salvati solo sul computer del gestore, non su un server.</li>
<li><strong>Utilizzo</strong> — le informazioni ricevute dalle API di Google sono usate solo per il caricamento e la gestione dei canali descritti sopra. Non sono vendute, non sono trasferite a terzi, non sono usate per pubblicità né per addestrare modelli di IA o di machine learning.</li>
<li><strong>Norme di Google</strong> — l'uso e il trasferimento delle informazioni ricevute dalle API di Google da parte dello strumento rispettano la {_a(GOOGLE_API_POLICY, "Google API Services User Data Policy")}, compresi i requisiti di uso limitato (Limited Use).</li>
<li><strong>Revoca</strong> — l'accesso concesso allo strumento può essere revocato in qualsiasi momento dalla {_a(GOOGLE_PERMISSIONS, "pagina delle autorizzazioni dell'account Google")} del canale. Dopo la revoca i token rimasti sul computer non funzionano più.</li>
</ul>
<p>Poiché lo strumento utilizza i Servizi API di YouTube, al suo uso si applicano i {_a(YT_TERMS, "Termini di servizio di YouTube")}; ai dati trattati da Google si applicano le {_a(GOOGLE_PRIVACY, "Norme sulla privacy di Google")}.</p>"""),
   ("Questo sito", """<p>Il trattamento dei dati durante la visita di questo sito (vicinolabs.com) è descritto a parte in <a href="/datenschutz/">Datenschutz</a> (informativa del sito).</p>"""),
   ("I tuoi diritti", """<ul>
<li>Accesso, rettifica, cancellazione, limitazione del trattamento, portabilità e opposizione (artt. 15–21 GDPR)</li>
<li>Reclamo a un'autorità di controllo — ad es. l'autorità per la protezione dei dati della Renania Settentrionale-Vestfalia (LDI NRW) o il Garante del tuo paese di residenza</li>
</ul>
<p>Gli unici dati degli spettatori che conserviamo direttamente sono le e-mail che ci invii. Per i dati trattati da YouTube (attività di visione, dati dell'account, commenti ecc.) puoi esercitare i tuoi diritti dalle impostazioni del tuo account Google o rivolgendoti direttamente a Google. Per le richieste rivolte a noi, contattaci qui sotto.</p>"""),
   ("Modifiche", """<p>Potremo aggiornare questa informativa in caso di modifiche normative, del modo in cui gestiamo il canale o dello strumento di caricamento; modifiche e data di entrata in vigore saranno pubblicate in questa pagina.</p>"""),
   ("Contatti", "<p>Per domande sul trattamento dei dati:</p>" + _id_card("it")),
  ],
 },
})
