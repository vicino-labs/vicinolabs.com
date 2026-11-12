"""Caffè Vicino 이용약관 본문 (ko/en/de/it) — caffevicino_legal.py가 HTML로 만든다.

2026-11-12 버전 1.0 초안(운영자 승인 전). 유튜브 채널의 음악·영상을 어디까지 써도 되는지 정한다.
- 허용: 유튜브에서 무료로, 개인적·비상업적으로 듣기.
- 서면 허락 필요: 내려받기, 다시 올리기·재송출, 자기 영상·팟캐스트·라이브·앱·광고에 쓰기,
  AI 학습·데이터셋, 자기 것이라고 하기, Content ID 등록.
- 매장 재생: 유튜브 약관이 개인적·비상업적 이용만 허용하므로 별도 이용 허락 필요(준비 중, 문의).
- 책임·준거법은 pianino_terms_content.py 틀(무료 제공: 고의·중과실, 생명·신체·건강만 무제한).
운영자 카드는 마지막 "문의처"에만.
"""

from appoggio_privacy_content import EMAIL, _id_card
from caffevicino_privacy_content import CHANNEL, YT_TERMS, _OP, _a, finish

_MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

TERMS = finish({
 "ko": {
  "title": "Caffè Vicino 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.11.12"), ("버전", "1.0"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 운영하는 유튜브 채널 Caffè Vicino의 음악과 영상을 어떻게 이용하실 수 있는지 정합니다. 유튜브에서 듣는 것은 무료이며, 그 밖의 이용에는 아래 내용이 적용됩니다.",
  "footer": "본 약관은 2026년 11월 12일부터 시행됩니다 (버전 1.0).",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", f"""<p>본 약관은 Vicino Labs(이하 “회사”)가 유튜브 채널 Caffè Vicino({_a(CHANNEL, "@caffevicino")}와 앞으로 여는 언어별 채널, 이하 “채널”)에 공개하는 음악, 녹음, 영상, 이미지(이하 “콘텐츠”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"""),
   ("사업자 정보", _OP),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 이 페이지에 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 변경 내용과 시행일을 이 페이지에 게시합니다.</li>
</ol>"""),
   ("채널 소개", f"""<ol>
<li>채널은 카페, 집중, 휴식을 위한 긴 음악 영상을 올립니다. 음악은 회사가 만든 창작곡과, 저작권 보호 기간이 끝난 선율(예: 크리스마스 캐럴)을 회사가 편곡한 곡이며, 샘플 음원 악기로 연주합니다.</li>
<li>영상의 이미지는 이용 허락을 받은 스톡 사진에 잔잔한 움직임을 더한 것입니다.</li>
<li>AI 도구로 만든 콘텐츠가 있는 경우, 유튜브가 요구하는 대로 유튜브의 “변경되거나 합성된 콘텐츠” 설정에 표시합니다.</li>
<li>유튜브는 Google이 운영하는 별개의 서비스이며, 유튜브 이용에는 {_a(YT_TERMS, "YouTube 서비스 약관")}이 적용됩니다.</li>
</ol>"""),
   ("허용되는 이용", """<ol>
<li>유튜브에서 채널의 콘텐츠를 <strong>무료로</strong>, <strong>개인적이고 비상업적인 용도</strong>로 보고 들으실 수 있습니다.</li>
<li>영상의 유튜브 링크를 다른 사람에게 알리는 것은 자유입니다.</li>
</ol>"""),
   ("서면 허락이 필요한 이용", f"""<p>다음은 회사의 사전 서면 허락 없이는 할 수 없습니다.</p>
<ol>
<li>콘텐츠를 내려받거나 음원·영상을 추출하는 것</li>
<li>유튜브나 다른 곳에 다시 올리거나 재송출하는 것</li>
<li>본인의 영상, 팟캐스트, 라이브 방송, 앱, 광고에 사용하는 것</li>
<li>AI·머신러닝 학습이나 데이터셋 구축에 사용하는 것</li>
<li>본인의 작품이라고 하는 것</li>
<li>Content ID 등 저작권 관리 시스템에 등록하는 것</li>
</ol>
<p>회사는 콘텐츠에 대한 텍스트·데이터 마이닝을 명시적으로 유보합니다(독일 저작권법 제44b조 제3항). 이용 허락 문의: {_MAIL}</p>"""),
   ("매장 등 공개 재생", f"""<p>유튜브의 약관은 개인적·비상업적 이용만 허용합니다. 따라서 카페, 상점, 호텔 등 영업장에서 채널의 음악을 틀려면 별도의 이용 허락이 필요합니다. 회사는 영업장을 위한 이용 허락을 준비하고 있습니다. 필요하신 분은 {_MAIL}로 문의해 주세요.</p>"""),
   ("권리와 출처 표시", """<ol>
<li>회사의 창작곡, 편곡, 녹음, 믹스, 영상과 “Caffè Vicino” 명칭·로고에 대한 권리는 회사에 있습니다.</li>
<li>저작권 보호 기간이 끝난 선율은 여전히 누구나 쓸 수 있습니다. 다만 회사가 만든 편곡, 녹음, 믹스, 영상은 보호됩니다.</li>
<li>연주에 쓰는 샘플 음원 일부는 제3자가 공개한 것(퍼블릭 도메인 피아노 샘플, Creative Commons Attribution 라이선스의 Salamander Grand Piano 등)입니다. 라이선스가 요구하는 경우 영상 설명에 출처를 적습니다.</li>
<li>영상의 사진은 Unsplash 라이선스에 따라 사용하며, 사진에 대한 권리는 각 사진가에게 있습니다.</li>
</ol>"""),
   ("댓글", """<p>댓글은 유튜브의 규정에 따라 남겨 주세요. 회사는 유튜브 규정이나 법령에 어긋나는 댓글을 숨기거나 삭제할 수 있습니다. 댓글과 관련된 정보 처리는 개인정보처리방침에 적혀 있습니다.</p>"""),
   ("업로드 도구와 YouTube API 서비스", f"""<p>회사는 채널에 영상을 올릴 때 YouTube API 서비스를 사용하는 내부 도구 caffevicino를 씁니다. 이 도구는 회사만 사용하며 일반에 제공하지 않습니다. 이 도구를 사용하는 사람은 {_a(YT_TERMS, "YouTube 서비스 약관")}에 동의하고 이를 따릅니다. 도구가 다루는 정보는 개인정보처리방침에 적혀 있습니다.</p>"""),
   ("제공의 변경·중단", """<p>회사는 채널과 각 영상이 항상 제공된다고 보증하지 않습니다. 회사는 영상을 바꾸거나 내리거나 비공개로 돌릴 수 있고 채널 운영을 멈출 수 있으며, 유튜브의 사정으로 영상을 볼 수 없게 될 수도 있습니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 그리고 생명·신체·건강의 침해에 대해서는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>채널의 콘텐츠는 무료로 제공되므로, 그 밖의 경우 회사의 책임은 법이 허용하는 범위에서 제외됩니다.</li>
<li>유튜브 서비스 자체(재생, 광고, 추천, 장애 등)는 Google이 제공하며 회사가 책임지지 않습니다.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관과 이용 허락에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },

 "en": {
  "title": "Caffè Vicino Terms of Use",
  "h1": "Terms of Use",
  "meta": [("Effective", "2026-11-12"), ("Version", "1.0"), ("Operator", "Vicino Labs")],
  "lede": "These Terms set out how you may use the music and videos of Caffè Vicino, a YouTube channel run by Vicino Labs. Listening on YouTube is free; any other use is subject to what follows.",
  "footer": "These Terms are effective from 12 November 2026 (version 1.0).",
  "other": "Privacy Policy →",
  "sections": [
   ("Purpose", f"""<p>These Terms govern the rights and obligations between Vicino Labs (“we”, “us”) and you regarding the music, recordings, videos and images (the “Content”) that we publish on the YouTube channel Caffè Vicino ({_a(CHANNEL, "@caffevicino")} and the language channels we open later; the “Channel”).</p>"""),
   ("About the operator", _OP),
   ("Effect and changes", """<ol>
<li>These Terms take effect once posted on this page.</li>
<li>We may amend these Terms within the limits of applicable law; changes and their effective date are posted on this page.</li>
</ol>"""),
   ("The Channel", f"""<ol>
<li>The Channel publishes long music videos for cafés, focus and rest. The music consists of our own compositions and our arrangements of public-domain melodies (for example Christmas carols), played with sampled instruments.</li>
<li>The images are licensed stock photos with subtle animation.</li>
<li>Where Content is made with AI tools, we label it in YouTube's “altered or synthetic content” setting, as YouTube requires.</li>
<li>YouTube is a separate service operated by Google; the {_a(YT_TERMS, "YouTube Terms of Service")} apply to your use of YouTube.</li>
</ol>"""),
   ("What you may do", """<ol>
<li>You may watch and listen to the Content on YouTube <strong>free of charge</strong> for <strong>personal, non-commercial use</strong>.</li>
<li>You are welcome to share the YouTube links to our videos.</li>
</ol>"""),
   ("What requires written permission", f"""<p>Without our prior written permission you may not:</p>
<ol>
<li>download the Content or rip its audio or video;</li>
<li>re-upload or re-stream it, on YouTube or elsewhere;</li>
<li>use it in your own videos, podcasts, livestreams, apps or advertisements;</li>
<li>use it to train AI or machine-learning systems or to build datasets;</li>
<li>claim it as your own work;</li>
<li>register it in Content ID or any other rights-management system.</li>
</ol>
<p>We expressly reserve the use of the Content for text and data mining (Section 44b(3) of the German Copyright Act). For permission, write to {_MAIL}.</p>"""),
   ("Businesses and public playback", f"""<p>YouTube's own terms permit only personal, non-commercial use. Playing the Channel's music in a business such as a café, shop or hotel therefore requires a separate licence. We are preparing a licence for businesses; if you need one, please write to {_MAIL}.</p>"""),
   ("Rights and credits", """<ol>
<li>All rights in our compositions, arrangements, recordings, mixes and videos and in the name and logo “Caffè Vicino” belong to us.</li>
<li>Public-domain melodies remain in the public domain. Our arrangements, recordings, mixes and videos of them are nevertheless protected.</li>
<li>Some of the sampled instruments we play are third-party samples (for example public-domain piano samples and the Salamander Grand Piano under a Creative Commons Attribution licence). Where a licence requires attribution, we give it in the video description.</li>
<li>The photos are used under the Unsplash licence; rights in them remain with the photographers.</li>
</ol>"""),
   ("Comments", """<p>Please follow YouTube's rules when you comment. We may hide or delete comments that break YouTube's rules or the law. How data connected with comments is handled is described in the Privacy Policy.</p>"""),
   ("Upload tool and YouTube API Services", f"""<p>To publish on the Channel we use caffevicino, an internal tool that uses YouTube API Services. Only we use it; it is not offered to the public. Anyone using the tool agrees to be bound by the {_a(YT_TERMS, "YouTube Terms of Service")}. The data the tool handles is described in the Privacy Policy.</p>"""),
   ("Availability and changes", """<p>We do not guarantee that the Channel or any video will always be available. We may change, remove or unlist videos or stop running the Channel, and videos may become unavailable for reasons on YouTube's side.</p>"""),
   ("Liability", """<ol>
<li>We are liable without limitation, in accordance with the law, for intent and gross negligence and for injury to life, body or health.</li>
<li>As the Content is provided free of charge, our liability is otherwise excluded to the extent permitted by law.</li>
<li>The YouTube service itself (playback, advertising, recommendations, outages and so on) is provided by Google; we are not responsible for it.</li>
</ol>"""),
   ("Governing law and venue", """<p>These Terms are governed by the laws of the Federal Republic of Germany. This does not affect mandatory consumer-protection rights under the law of your country of habitual residence (for example, an EU member state). Otherwise, the courts at our place of business (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For any question about these Terms or about permission to use our music, please contact:</p>" + _id_card("en")),
  ],
 },

 "de": {
  "title": "Caffè Vicino Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "12.11.2026"), ("Version", "1.0"), ("Anbieter", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln, wie Sie die Musik und die Videos von Caffè Vicino, einem YouTube-Kanal von Vicino Labs, nutzen dürfen. Das Anhören auf YouTube ist kostenlos; für jede weitere Nutzung gilt das Folgende.",
  "footer": "Diese Bedingungen gelten ab dem 12. November 2026 (Version 1.0).",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Gegenstand", f"""<p>Diese Bedingungen regeln die Rechte und Pflichten zwischen Vicino Labs („wir“) und Ihnen in Bezug auf die Musik, Aufnahmen, Videos und Bilder („Inhalte“), die wir auf dem YouTube-Kanal Caffè Vicino ({_a(CHANNEL, "@caffevicino")} sowie künftigen Sprachkanälen; „Kanal“) veröffentlichen.</p>"""),
   ("Anbieter", _OP),
   ("Geltung und Änderungen", """<ol>
<li>Diese Bedingungen gelten, sobald sie auf dieser Seite veröffentlicht sind.</li>
<li>Wir können sie im Rahmen des geltenden Rechts ändern; Änderungen und Gültigkeitsdatum veröffentlichen wir auf dieser Seite.</li>
</ol>"""),
   ("Der Kanal", f"""<ol>
<li>Der Kanal veröffentlicht lange Musikvideos für Cafés, zum Konzentrieren und zum Entspannen. Die Musik besteht aus eigenen Kompositionen und eigenen Bearbeitungen gemeinfreier Melodien (zum Beispiel Weihnachtslieder), gespielt mit gesampelten Instrumenten.</li>
<li>Die Bilder sind lizenzierte Stockfotos mit dezenter Animation.</li>
<li>Soweit Inhalte mit KI-Werkzeugen erstellt werden, kennzeichnen wir dies in der YouTube-Einstellung „Veränderte oder synthetische Inhalte“, wie YouTube es verlangt.</li>
<li>YouTube ist ein eigenständiger Dienst von Google; für die Nutzung von YouTube gelten die {_a(YT_TERMS, "YouTube-Nutzungsbedingungen")}.</li>
</ol>"""),
   ("Erlaubte Nutzung", """<ol>
<li>Sie dürfen die Inhalte auf YouTube <strong>kostenlos</strong> zum <strong>privaten, nicht kommerziellen Gebrauch</strong> ansehen und anhören.</li>
<li>Die YouTube-Links zu unseren Videos dürfen Sie gern weitergeben.</li>
</ol>"""),
   ("Nutzung nur mit schriftlicher Erlaubnis", f"""<p>Ohne unsere vorherige schriftliche Erlaubnis ist es nicht gestattet,</p>
<ol>
<li>die Inhalte herunterzuladen oder Ton oder Bild daraus zu extrahieren,</li>
<li>sie auf YouTube oder anderswo erneut hochzuladen oder zu streamen,</li>
<li>sie in eigenen Videos, Podcasts, Livestreams, Apps oder in der Werbung zu verwenden,</li>
<li>sie zum Training von KI- oder Machine-Learning-Systemen oder zum Aufbau von Datensätzen zu verwenden,</li>
<li>sie als eigenes Werk auszugeben,</li>
<li>sie bei Content ID oder einem anderen Rechteverwaltungssystem anzumelden.</li>
</ol>
<p>Die Nutzung der Inhalte für Text und Data Mining behalten wir uns ausdrücklich vor (§ 44b Abs. 3 UrhG). Anfragen zu einer Erlaubnis richten Sie bitte an {_MAIL}.</p>"""),
   ("Gewerbliche und öffentliche Wiedergabe", f"""<p>Die Nutzungsbedingungen von YouTube erlauben nur den privaten, nicht kommerziellen Gebrauch. Wer die Musik des Kanals in einem Betrieb wie einem Café, Geschäft oder Hotel abspielen möchte, benötigt deshalb eine gesonderte Lizenz. Ein Lizenzangebot für Betriebe ist in Vorbereitung; bei Bedarf schreiben Sie uns bitte an {_MAIL}.</p>"""),
   ("Rechte und Quellenangaben", """<ol>
<li>Alle Rechte an unseren Kompositionen, Bearbeitungen, Aufnahmen, Abmischungen und Videos sowie an Name und Logo „Caffè Vicino“ liegen bei uns.</li>
<li>Gemeinfreie Melodien bleiben gemeinfrei. Unsere Bearbeitungen, Aufnahmen, Abmischungen und Videos davon sind dennoch geschützt.</li>
<li>Ein Teil der gesampelten Instrumente stammt von Dritten (zum Beispiel gemeinfreie Klaviersamples und das Salamander Grand Piano unter einer Creative-Commons-Lizenz mit Namensnennung). Wo eine Lizenz die Namensnennung verlangt, steht sie in der Videobeschreibung.</li>
<li>Die Fotos werden unter der Unsplash-Lizenz verwendet; die Rechte daran liegen bei den Fotografinnen und Fotografen.</li>
</ol>"""),
   ("Kommentare", """<p>Bitte halten Sie sich beim Kommentieren an die Regeln von YouTube. Kommentare, die gegen die Regeln von YouTube oder gegen geltendes Recht verstoßen, können wir ausblenden oder löschen. Wie Daten im Zusammenhang mit Kommentaren verarbeitet werden, steht in der Datenschutzerklärung.</p>"""),
   ("Upload-Werkzeug und YouTube-API-Dienste", f"""<p>Für Veröffentlichungen auf dem Kanal verwenden wir caffevicino, ein internes Werkzeug, das die YouTube-API-Dienste nutzt. Nur wir verwenden es; es wird nicht öffentlich angeboten. Wer das Werkzeug nutzt, erklärt sich mit den {_a(YT_TERMS, "YouTube-Nutzungsbedingungen")} einverstanden. Welche Daten das Werkzeug verarbeitet, steht in der Datenschutzerklärung.</p>"""),
   ("Verfügbarkeit und Änderungen", """<p>Wir übernehmen keine Gewähr dafür, dass der Kanal oder einzelne Videos jederzeit verfügbar sind. Wir können Videos ändern, entfernen oder auf nicht gelistet stellen oder den Kanal einstellen; Videos können auch aus Gründen, die bei YouTube liegen, nicht abrufbar sein.</p>"""),
   ("Haftung", """<ol>
<li>Wir haften unbeschränkt nach den gesetzlichen Vorschriften für Vorsatz und grobe Fahrlässigkeit sowie für Schäden aus der Verletzung des Lebens, des Körpers oder der Gesundheit.</li>
<li>Da die Inhalte unentgeltlich bereitgestellt werden, ist unsere Haftung im Übrigen ausgeschlossen, soweit gesetzlich zulässig.</li>
<li>Den Dienst YouTube selbst (Wiedergabe, Werbung, Empfehlungen, Störungen usw.) erbringt Google; dafür sind wir nicht verantwortlich.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt das Recht der Bundesrepublik Deutschland. Zwingende Verbraucherschutzvorschriften Ihres gewöhnlichen Aufenthaltsstaats (z. B. eines EU-Mitgliedstaats) bleiben unberührt. Im Übrigen sind die Gerichte an unserem Sitz (Dortmund) zuständig.</p>"""),
   ("Kontakt", "<p>Bei Fragen zu diesen Bedingungen oder zu einer Nutzungserlaubnis:</p>" + _id_card("de")),
  ],
 },

 "it": {
  "title": "Caffè Vicino — Termini di utilizzo",
  "h1": "Termini di utilizzo",
  "meta": [("In vigore dal", "12/11/2026"), ("Versione", "1.0"), ("Titolare", "Vicino Labs")],
  "lede": "Questi Termini stabiliscono come puoi utilizzare la musica e i video di Caffè Vicino, un canale YouTube di Vicino Labs. L'ascolto su YouTube è gratuito; per ogni altro utilizzo vale quanto segue.",
  "footer": "I presenti Termini sono in vigore dal 12 novembre 2026 (versione 1.0).",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", f"""<p>I presenti Termini disciplinano i diritti e gli obblighi tra Vicino Labs (“noi”) e te riguardo alla musica, alle registrazioni, ai video e alle immagini (i “Contenuti”) che pubblichiamo sul canale YouTube Caffè Vicino ({_a(CHANNEL, "@caffevicino")} e i canali in altre lingue che apriremo; il “Canale”).</p>"""),
   ("Chi siamo", _OP),
   ("Efficacia e modifiche", """<ol>
<li>I Termini sono efficaci dalla pubblicazione in questa pagina.</li>
<li>Possiamo modificarli nei limiti della legge; modifiche e data di efficacia sono pubblicate in questa pagina.</li>
</ol>"""),
   ("Il Canale", f"""<ol>
<li>Il Canale pubblica lunghi video musicali per il caffè, la concentrazione e il riposo. La musica è composta da nostri brani originali e da nostri arrangiamenti di melodie di pubblico dominio (ad esempio canti natalizi), eseguiti con strumenti campionati.</li>
<li>Le immagini sono foto stock concesse in licenza, con una leggera animazione.</li>
<li>Se un Contenuto è realizzato con strumenti di IA, lo segnaliamo nell'impostazione di YouTube “Contenuti alterati o sintetici”, come richiesto da YouTube.</li>
<li>YouTube è un servizio distinto gestito da Google; all'uso di YouTube si applicano i {_a(YT_TERMS, "Termini di servizio di YouTube")}.</li>
</ol>"""),
   ("Che cosa puoi fare", """<ol>
<li>Puoi guardare e ascoltare i Contenuti su YouTube <strong>gratuitamente</strong>, per <strong>uso personale e non commerciale</strong>.</li>
<li>Puoi condividere liberamente i link YouTube dei nostri video.</li>
</ol>"""),
   ("Utilizzi che richiedono un'autorizzazione scritta", f"""<p>Senza la nostra previa autorizzazione scritta non è consentito:</p>
<ol>
<li>scaricare i Contenuti o estrarne l'audio o il video;</li>
<li>ricaricarli o ritrasmetterli, su YouTube o altrove;</li>
<li>utilizzarli in video, podcast, dirette, app o pubblicità propri;</li>
<li>utilizzarli per addestrare sistemi di IA o di machine learning o per creare dataset;</li>
<li>presentarli come opera propria;</li>
<li>registrarli in Content ID o in altri sistemi di gestione dei diritti.</li>
</ol>
<p>Ci riserviamo espressamente l'utilizzo dei Contenuti per l'estrazione di testo e di dati (§ 44b, comma 3, della legge tedesca sul diritto d'autore). Per un'autorizzazione scrivi a {_MAIL}.</p>"""),
   ("Locali e riproduzione in pubblico", f"""<p>I termini di YouTube consentono solo l'uso personale e non commerciale. Per diffondere la musica del Canale in un'attività come un bar, un negozio o un hotel serve quindi una licenza separata. Stiamo preparando una licenza per le attività commerciali; se ti serve, scrivi a {_MAIL}.</p>"""),
   ("Diritti e crediti", """<ol>
<li>Tutti i diritti sulle nostre composizioni, sui nostri arrangiamenti, registrazioni, mix e video e sul nome e sul logo “Caffè Vicino” appartengono a noi.</li>
<li>Le melodie di pubblico dominio restano di pubblico dominio. I nostri arrangiamenti, registrazioni, mix e video sono comunque protetti.</li>
<li>Alcuni degli strumenti campionati sono di terzi (ad esempio campioni di pianoforte di pubblico dominio e il Salamander Grand Piano con licenza Creative Commons Attribuzione). Quando la licenza richiede l'attribuzione, la indichiamo nella descrizione del video.</li>
<li>Le foto sono utilizzate con licenza Unsplash; i relativi diritti restano ai fotografi.</li>
</ol>"""),
   ("Commenti", """<p>Quando commenti, rispetta le regole di YouTube. Possiamo nascondere o eliminare i commenti contrari alle regole di YouTube o alla legge. Il trattamento dei dati legati ai commenti è descritto nell'Informativa sulla privacy.</p>"""),
   ("Strumento di caricamento e Servizi API di YouTube", f"""<p>Per pubblicare sul Canale usiamo caffevicino, uno strumento interno che utilizza i Servizi API di YouTube. Lo usiamo soltanto noi; non è offerto al pubblico. Chi utilizza lo strumento accetta di essere vincolato dai {_a(YT_TERMS, "Termini di servizio di YouTube")}. I dati gestiti dallo strumento sono descritti nell'Informativa sulla privacy.</p>"""),
   ("Disponibilità e modifiche", """<p>Non garantiamo che il Canale o i singoli video siano sempre disponibili. Possiamo modificare, rimuovere o rendere non in elenco i video o interrompere il Canale; i video possono inoltre non essere disponibili per cause dipendenti da YouTube.</p>"""),
   ("Responsabilità", """<ol>
<li>Rispondiamo senza limiti, secondo la legge, per dolo e colpa grave e per danni alla vita, al corpo o alla salute.</li>
<li>Poiché i Contenuti sono offerti gratuitamente, per il resto la nostra responsabilità è esclusa nei limiti consentiti dalla legge.</li>
<li>Il servizio YouTube in sé (riproduzione, pubblicità, suggerimenti, interruzioni ecc.) è fornito da Google; non ne siamo responsabili.</li>
</ol>"""),
   ("Legge applicabile e foro competente", """<p>Si applica la legge della Repubblica Federale di Germania. Restano salvi i diritti inderogabili dei consumatori previsti dalla legge del paese di residenza abituale (ad es. uno Stato membro dell'UE). Negli altri casi è competente il foro della nostra sede (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande sui presenti Termini o su un'autorizzazione all'uso della nostra musica:</p>" + _id_card("it")),
  ],
 },
})
