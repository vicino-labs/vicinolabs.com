"""Leggii(렛지 악보) 이용약관 본문 (ko/en/de/it) — leggii_legal.py가 HTML로 만든다.

2026-10-22 버전 1.0 (앱 1.0.0). 기본 기능 무료 + Pro 평생 이용권(스토어 인앱 결제) +
처음 7일 Pro 무료 체험. 이용자가 가져온 악보의 저작권은 이용자 책임(IMSLP 판본은 나라마다 다름).
2026-11-05 버전 1.1 (앱 1.2.0~1.4.0): 녹음, Leggii Plus 구독, AI 시간·충전, AI 레슨 분석,
렛지에게 물어보기, 위레가토 통합 아이디(선택).
2026-11-06 버전 1.2 (앱 1.5.0): 렛지 클라우드(Plus 10GB/50GB), 출시 가격 유지, Plus 종료 후 90일.
2026-12-21 버전 1.3 (앱 1.5.1, 2026-11-09 공지): 위레가토 채팅으로 보내기(7일, 권리·책임·신고·한도),
클라우드와 어긋나던 "기기에만 저장" 문장 정리. 위레가토 이용약관 1.4와 같은 날 시행.
책임 제한은 독일법상 허용 범위(고의·중과실, 생명·신체·건강, 제조물책임법은 제한 불가).
"""

from appoggio_privacy_content import _id_card
from leggii_privacy_content import _op_ref, _fix_end

TERMS = {
 "ko": {
  "title": "렛지 악보(Leggii) 이용약관",
  "h1": "이용약관",
  "meta": [("시행일", "2026.12.21"), ("버전", "1.3"), ("운영자", "Vicino Labs")],
  "lede": "본 약관은 Vicino Labs가 만든 악보 앱 렛지 악보(Leggii)를 이용하시는 분들과 저희 사이의 약속입니다. 앱을 설치하고 이용하시면 아래 내용에 동의하신 것으로 봅니다.",
  "footer": "본 약관은 2026년 12월 21일부터 시행됩니다 (버전 1.3, 2026년 11월 9일 공지). 그 전까지는 버전 1.2(2026년 11월 6일)가 적용됩니다. 이전 버전 1.1: 2026년 11월 5일, 1.0: 2026년 10월 22일.",
  "other": "개인정보처리방침 보기 →",
  "sections": [
   ("목적", "<p>본 약관은 Vicino Labs(이하 “회사”)가 제공하는 모바일 앱 렛지 악보(Leggii, 이하 “앱”)의 이용에 관한 회사와 이용자의 권리·의무를 정합니다.</p>"),
   ("사업자 정보", _op_ref("ko")),
   ("약관의 효력과 변경", """<ol>
<li>본 약관은 앱 안 또는 회사가 정한 방법으로 게시하면 효력이 생깁니다.</li>
<li>회사는 관련 법령을 위반하지 않는 범위에서 약관을 고칠 수 있으며, 시행일과 변경 이유를 미리 알립니다.</li>
<li>변경된 약관에 동의하지 않으면 앱 이용을 멈추고 삭제할 수 있습니다.</li>
</ol>"""),
   ("서비스 내용", """<ol>
<li><strong>무료 기능:</strong> PDF 악보 보기와 페이지 넘기기(페달 포함), 가져오기·사진 스캔·IMSLP 검색, 오선지 만들기, 필기·기본 기호, 폴더·셋리스트·PDF 합치기, 메트로놈, 서재 백업 등</li>
<li><strong>Pro 기능:</strong> 배너 없음, 사진 스캔 PDF 공유 시 하단 문구 없음, 나만의 펜, 추가 기호, 반복·D.C. 연결, 페이지 편집, 필기 포함 PDF 내보내기와 앞으로 Pro에 추가되는 기능</li>
<li>무료 버전에는 같은 회사 서비스 welegato를 알리는 배너가 표시됩니다.</li>
<li><strong>AI 레슨 분석:</strong> 이용자가 요청하면 녹음으로 레슨 노트나 대화 받아 적기를 만듭니다. AI 시간(분)을 씁니다.</li>
<li><strong>위레가토 통합 아이디(선택):</strong> 로그인하면 Pro·Plus·AI 시간이 여러 기기에서 이어집니다.</li>
<li><strong>렛지에게 물어보기:</strong> 앱 사용법과 요금제를 답하고 악보 찾기 같은 동작을 도와주는 AI 도우미(무료, 하루 30회까지).</li>
</ol>"""),
   ("Pro, Leggii Plus와 AI 시간", """<ol>
<li><strong>무료 체험:</strong> 앱을 처음 설치하면 <strong>7일 동안</strong> Pro 기능을 무료로 쓸 수 있고, 기기당 한 번 AI 시간 30분을 드립니다. 체험이 끝나면 자동으로 무료 버전으로 돌아가며 자동 결제는 없습니다. 체험 중에 만든 필기·기호·연결·페이지는 그대로 남습니다.</li>
<li><strong>Pro:</strong> 앱 스토어 인앱 결제로 한 번 구매하는 <strong>평생 이용권</strong>입니다. 매월 AI 시간 30분과 처음 한 번 환영 보너스 60분이 포함됩니다. 같은 스토어 계정으로 다시 설치하면 “구매 복원”으로 되살릴 수 있습니다.</li>
<li><strong>Leggii Plus:</strong> 월간 또는 연간 <strong>정기 구독</strong>으로, 모든 Pro 기능과 매월 AI 시간 5시간이 포함됩니다. 해지할 때까지 같은 기간으로 자동 갱신되며, Google Play(또는 App Store)의 구독 관리에서 언제든 해지할 수 있습니다. 해지해도 이미 결제한 기간이 끝날 때까지 쓸 수 있고, 그 뒤에는 Pro를 구매했다면 Pro로, 아니면 무료 버전으로 돌아갑니다.</li>
<li><strong>렛지 클라우드(Plus):</strong> 위레가토 통합 아이디로 로그인하면 악보·필기·폴더·셋리스트·개인 노트와, 이용자가 켜 둔 경우 녹음을 같은 아이디의 기기들에 맞춥니다. Plus에는 10GB가 포함되며, 더 큰 공간은 50GB 요금제로 바꿀 수 있습니다(올릴 때는 Google Play가 남은 기간의 차액만 받습니다). 공간이 차면 새로 올리는 것만 멈추고 아무것도 지우지 않습니다. 한 기기에서 지운 항목은 다른 기기와 클라우드에서도 지워집니다. Plus가 끝나면 새 업로드가 멈추고 90일 동안 내려받을 수 있으며, 두 번 메일로 알린 뒤 클라우드의 파일을 지웁니다. 클라우드는 이용자 본인의 기기들 사이의 동기화를 위한 것입니다. 다른 사람은 이용자가 아래 “위레가토 채팅으로 보내기”로 고른 파일만, 정해진 기간 동안 열어 볼 수 있습니다. 중요한 자료는 “서재 백업하기”로도 따로 보관하기를 권합니다.</li>
<li><strong>출시 가격:</strong> 2027년 12월 31일까지 Plus를 구독하면, 구독을 이어 가는 동안 그때의 가격이 유지됩니다. 그 뒤 새로 구독하는 경우에는 다른 가격이 적용될 수 있습니다.</li>
<li><strong>AI 시간 충전:</strong> 5시간·15시간 단위로 한 번 결제하며 구독이 아닙니다. 구매일로부터 12개월 동안 쓸 수 있고, Plus 구독 여부와 상관없이 남습니다.</li>
<li><strong>AI 시간 계산:</strong> 레슨 노트는 녹음 1분에 1분, 대화 받아 적기는 녹음 1분에 3분이 차감되며, 시작 전에 화면에 표시됩니다. 매월 주어지는 시간을 먼저 쓰고 그다음 충전 시간을 씁니다. 매월 시간은 다음 달로 넘어가지 않습니다. AI 시간은 현금으로 바꾸거나 다른 사람에게 넘길 수 없습니다.</li>
<li><strong>통합 아이디와 구매:</strong> 로그인하면 구매와 AI 시간이 그 아이디에 연결됩니다. 하나의 구매는 처음 연결된 아이디 하나에만 속합니다.</li>
<li>가격은 결제 화면에 표시됩니다. 결제·환불은 각 스토어의 정책과 절차에 따릅니다. 디지털 콘텐츠의 특성상, 구매 즉시 이용이 시작되는 데 동의하면 법이 허용하는 범위에서 청약철회권이 소멸할 수 있으며, 이 경우에도 스토어의 환불 절차는 이용할 수 있습니다.</li>
<li>회사는 Pro의 핵심 기능을 정당한 이유 없이 유료 이용자에게서 빼지 않습니다. 매월 AI 시간이나 충전 조건을 바꿀 때는 미리 알리며, 이미 결제한 기간과 이미 충전한 시간에는 적용하지 않습니다.</li>
</ol>"""),
   ("악보와 저작권", """<ol>
<li>이용자가 앱에 가져오거나 스캔·공유하는 악보에 대한 저작권 준수는 이용자의 책임입니다.</li>
<li>IMSLP의 악보는 IMSLP가 정한 조건으로 제공되며, 저작권 보호 기간은 나라마다 다릅니다. 앱은 EU에서 보호될 수 있는 판본에 안내를 표시하지만, 최종 판단은 이용자에게 있습니다.</li>
<li>렛지 클라우드를 쓰지 않으면 악보는 기기에만 있습니다. 클라우드를 쓰면 이용자 본인의 기기들에 맞추기 위해 저장되며, 회사는 그 내용을 살펴보지 않습니다.</li>
</ol>"""),
   ("녹음", """<ol>
<li>앱의 녹음 기능은 레슨·리허설·앙상블·연습을 이용자 본인의 연습과 기록을 위해 남기는 용도입니다.</li>
<li>다른 사람(선생님, 지휘자, 함께 연주하는 사람 등)의 목소리나 연주가 녹음되는 경우, 이용자는 녹음 전에 그분들의 동의를 받아야 합니다. 동의 없이 녹음하거나 녹음을 쓰는 데 따른 책임은 이용자에게 있습니다.</li>
<li>녹음을 다른 사람에게 보내거나 공개·배포할 때는 녹음된 사람들의 동의와 연주된 작품의 저작권·실연자 권리를 이용자가 확인해야 합니다.</li>
<li>녹음은 이용자의 기기에 저장되며, 이용자가 클라우드에 녹음 올리기를 켠 경우에만 렛지 클라우드에도 저장됩니다. AI 분석을 요청하면 분석하는 동안만 잠시 처리합니다. 회사는 기기에 있는 녹음을 보관하지 않으며, 잃어버린 녹음을 되살려 드릴 수 없습니다. 중요한 녹음은 “서재 백업하기”나 보내기로 따로 보관해 주세요.</li>
</ol>"""),
   ("AI 레슨 분석과 렛지에게 물어보기", """<ol>
<li>AI 레슨 분석과 렛지에게 물어보기의 결과는 AI가 만들며 <strong>틀리거나 빠진 내용이 있을 수 있습니다.</strong> 레슨이나 리허설의 지시를 대신하지 않으니 중요한 내용은 직접 확인해 주세요.</li>
<li>AI 레슨 분석은 이용자가 녹음 권리와 녹음된 사람들의 동의를 갖춘 녹음에만 써야 합니다.</li>
<li>렛지에게 물어보기는 무료로 기기당 하루 30회까지 쓸 수 있습니다. 회사는 남용을 막기 위해 이용 횟수를 제한할 수 있습니다.</li>
<li>도우미가 제안하는 동작 중 AI 시간이 차감되는 것은 이용자가 확인하고 시작할 때만 실행됩니다. 결제와 구매는 도우미가 대신하지 않습니다.</li>
</ol>"""),
   ("위레가토 통합 아이디", """<ol>
<li>로그인은 선택이며, 로그인하지 않아도 렛지의 기본 기능을 모두 쓸 수 있습니다.</li>
<li>통합 아이디는 같은 회사가 운영하는 위레가토의 계정입니다. 아이디를 만들고 쓰는 데에는 <a href="https://welegato.com/legal/terms/" target="_blank" rel="noopener">위레가토 이용약관</a>이 함께 적용되며, 만 16세 이상만 로그인할 수 있습니다.</li>
<li>설정 › 위레가토 통합 아이디 › 아이디 관리에서 아이디를 삭제할 수 있습니다. 삭제하면 이 아이디로 쓰던 모든 Vicino Labs 앱에서 함께 지워지며, Leggii Plus 구독은 별도로 스토어에서 해지해야 결제가 멈춥니다.</li>
<li>계약 해지 방법은 설정 › 약관 및 정책 › 계약 해지(Verträge hier kündigen)에 모아 두었습니다.</li>
</ol>"""),
   ("위레가토 채팅으로 보내기", """<ol>
<li>위레가토 통합 아이디로 로그인한 이용자는 렛지 클라우드에 있는 악보 PDF, AI 레슨 노트 PDF, 녹음(오디오)을 위레가토 대화 상대에게 보낼 수 있습니다. 파일은 복사되지 않으며, 상대는 보낸 때부터 7일 동안 열어 볼 수 있습니다. 필기와 AI 분석 결과는 함께 가지 않습니다. 보낸 사람은 위레가토 채팅에서 언제든 공유를 끌 수 있습니다.</li>
<li>보내는 파일에 필요한 권리는 이용자에게 있어야 합니다. 여기에는 악보와 연주의 저작권, 그리고 녹음된 분들의 동의가 포함됩니다. 저작권자의 허락 없이 스캔하거나 복사한 악보나 녹음은 보낼 수 없습니다. 보낸 파일의 내용과 권리에 대한 책임은 보낸 이용자에게 있으며, 회사는 파일을 미리 살펴보지 않습니다.</li>
<li>신고된 파일은 바로 닫힙니다. 회사는 검토한 뒤 권리 침해나 불법 콘텐츠로 판단하면 공유를 계속 막고, 위레가토 이용약관에 따라 이용을 제한할 수 있습니다.</li>
<li>남용을 막기 위해 하루 20개, 한 번에 500MB까지 보낼 수 있습니다. 회사는 이 한도를 바꿀 수 있습니다.</li>
</ol>"""),
   ("welegato 및 외부 서비스", """<p>앱에는 welegato, IMSLP, Google Play 등 외부 서비스로 가는 링크와 기능이 있습니다. 이 서비스들은 앱과 별개이며 각자의 이용약관과 개인정보처리방침이 적용됩니다. 외부 서비스의 내용과 이용 가능 여부에 대해 회사는 책임지지 않습니다.</p>"""),
   ("지적재산권", """<p>앱의 로고, “Leggii·렛지” 명칭, 디자인, 문구, 소스코드에 대한 권리는 회사에 있습니다. 회사의 사전 서면 동의 없이 복제·배포·전송·출판·역설계하거나 2차적 저작물을 만들 수 없습니다.</p>"""),
   ("이용자의 의무", """<ol>
<li>앱을 역설계·디컴파일하거나 결제를 우회하지 않습니다.</li>
<li>앱의 정상적인 운영을 방해하지 않습니다.</li>
<li>관련 법령과 본 약관을 지킵니다.</li>
<li>필요한 권리가 없는 악보·녹음 등의 파일을 위레가토 채팅으로 보내지 않습니다(저작권자의 허락 없이 스캔·복사한 악보나 녹음 포함).</li>
</ol>"""),
   ("서비스의 변경·중단", """<p>회사는 운영상·기술상 필요에 따라 앱 기능의 전부 또는 일부를 바꾸거나 중단할 수 있으며, 긴급한 경우가 아니면 미리 알립니다. 외부 서비스(IMSLP 등)의 변경으로 관련 기능이 제한될 수 있습니다.</p>"""),
   ("책임", """<ol>
<li>회사는 고의 또는 중대한 과실, 생명·신체·건강의 침해, 그리고 제조물책임법에 따른 경우에는 법률에 따라 제한 없이 책임을 집니다.</li>
<li>경과실의 경우 회사는 계약상 본질적인 의무를 위반했을 때에만, 계약 체결 시 예견할 수 있었던 통상적인 손해에 한해 책임을 집니다.</li>
<li>클라우드를 쓰지 않으면 악보와 필기는 기기에만 저장됩니다. 기기 분실·앱 삭제·초기화로 인한 손실에 대비해 “서재 백업하기”로 직접 백업해 주세요.</li>
</ol>"""),
   ("준거법과 관할", """<p>본 약관에는 독일연방공화국 법이 적용됩니다. 소비자인 이용자가 상거소 국가(예: EU 회원국)의 강행 소비자보호 규정에 따라 갖는 권리는 영향을 받지 않습니다. 그 밖의 경우 관할 법원은 회사 소재지(독일 도르트문트)의 법원입니다.</p>"""),
   ("문의처", "<p>약관에 관한 문의는 아래로 연락해 주세요.</p>" + _id_card("ko")),
  ],
 },
 "en": {
  "title": "Leggii Terms of Service",
  "h1": "Terms of Service",
  "meta": [("Effective", "2026-12-21"), ("Version", "1.3"), ("Operator", "Vicino Labs")],
  "lede": "These terms are the agreement between you and Vicino Labs for using Leggii, a sheet music app. By installing and using the app you agree to them.",
  "footer": "These terms are effective from 21 December 2026 (version 1.3, announced 9 November 2026). Until then version 1.2 (6 November 2026) applies. Previous versions 1.1: 5 November 2026, 1.0: 22 October 2026.",
  "other": "Privacy Policy →",
  "sections": [
   ("Scope", "<p>These terms govern the use of the mobile app Leggii (the “app”) provided by Vicino Labs (the “company”).</p>"),
   ("Provider", _op_ref("en")),
   ("Validity and changes", """<ol>
<li>These terms take effect when published in the app or in another way chosen by the company.</li>
<li>The company may change them within the law and will announce the effective date and reason in advance.</li>
<li>If you do not agree to changed terms, you may stop using and delete the app.</li>
</ol>"""),
   ("What the app offers", """<ol>
<li><strong>Free:</strong> reading PDF scores and turning pages (including pedals), importing, photo scans, IMSLP search, staff paper, notes and basic symbols, folders, setlists, merging PDFs, metronome, library backup and more</li>
<li><strong>Pro:</strong> no banner, no credit line on shared photo scans, your own pens, more symbols, repeat and D.C. jumps, page editing, PDF export with notes, and Pro features added later</li>
<li>The free version shows a banner for welegato, a service of the same company.</li>
<li><strong>AI lesson analysis:</strong> on request, lesson notes or a transcript from a recording. It uses AI time (minutes).</li>
<li><strong>welegato ID (optional):</strong> signed in, Pro, Plus and AI time follow you to other devices.</li>
<li><strong>Ask Leggii:</strong> an AI assistant that answers how the app and plans work and helps with actions such as finding a score (free, up to 30 questions a day).</li>
</ol>"""),
   ("Pro, Leggii Plus and AI time", """<ol>
<li><strong>Free trial:</strong> after the first installation you can use the Pro features free for <strong>7 days</strong>, plus 30 AI minutes once per device. The trial then ends by itself; there is no automatic payment. Notes, symbols, links and pages made during the trial stay.</li>
<li><strong>Pro:</strong> a one-time in-app purchase that is <strong>yours for life</strong>, with 30 AI minutes every month and a one-time 60-minute welcome bonus. Reinstalling with the same store account restores it with “Restore purchase”.</li>
<li><strong>Leggii Plus:</strong> a monthly or yearly <strong>subscription</strong> with all Pro features and 5 hours of AI time every month. It renews for the same period until cancelled; cancel any time in Google Play (or the App Store) subscriptions. It keeps working until the paid period ends; afterwards you are back to Pro if you bought Pro, otherwise to the free version.</li>
<li><strong>Leggii cloud (Plus):</strong> signed in with the welegato ID, scores, ink, folders, setlists, my notes and — if you keep it on — recordings stay the same on the devices of that ID. Plus includes 10 GB; for more space you can switch to the 50 GB plan (Google Play then charges only the difference for the rest of the period). When the cloud is full, only new uploads stop and nothing is deleted. Something deleted on one device is deleted on the other devices and in the cloud too. When Plus ends, new uploads stop, everything can be downloaded for 90 days, and after two reminder emails the cloud files are deleted. The cloud is for syncing your own devices. Others can open only the files you choose with “Send to a welegato chat” below, and only for a limited time. We recommend also keeping important material with “Back up library”.</li>
<li><strong>Launch price:</strong> subscribe to Plus by 31 December 2027 and keep that price for as long as you stay subscribed. A different price may apply to new subscriptions after that.</li>
<li><strong>AI time top-ups:</strong> 5 or 15 hours, paid once, not a subscription. Usable for 12 months from purchase, whether or not you subscribe to Plus.</li>
<li><strong>How AI time is counted:</strong> lesson notes use 1 minute per recording minute, transcripts 3 minutes; the cost is shown before starting. Monthly minutes are used first, then top-ups. Monthly minutes do not carry over. AI time has no cash value and cannot be transferred.</li>
<li><strong>welegato ID and purchases:</strong> when you sign in, purchases and AI time are linked to that ID. A purchase belongs to the first ID it was linked to.</li>
<li>Prices are shown at checkout. Payment and refunds follow each store's rules and process. For digital content, if you agree that use starts immediately, your right of withdrawal may end as far as the law allows; the store's refund process remains available.</li>
<li>We will not remove core Pro features from paying users without good reason. Changes to monthly AI time or top-up terms are announced in advance and do not apply to periods already paid or time already bought.</li>
</ol>"""),
   ("Scores and copyright", """<ol>
<li>You are responsible for respecting copyright in the scores you import, scan or share.</li>
<li>Scores from IMSLP are provided on IMSLP's terms, and copyright terms differ by country. The app flags editions that may still be protected in the EU, but the final judgement is yours.</li>
<li>Without Leggii cloud your scores stay on your device. With the cloud they are stored to keep your own devices in sync; the company does not look at their contents.</li>
</ol>"""),
   ("Recordings", """<ol>
<li>The recording feature is for keeping lessons, rehearsals, ensembles and practice for your own practice and notes.</li>
<li>If other people's voices or playing are recorded (a teacher, conductor or fellow musicians, for example), you must get their consent before recording. You are responsible for recording, or using a recording, without consent.</li>
<li>Before you send a recording to others or publish or distribute it, you must make sure the people recorded agree and that copyright and performers' rights in the music allow it.</li>
<li>Recordings are stored on your device, and in Leggii cloud only if you turn on recordings in the cloud. An AI analysis you ask for handles them only briefly. The company does not keep the recordings on your device and cannot restore a lost recording. Keep important recordings safe with “Back up library” or by sending them.</li>
</ol>"""),
   ("AI lesson analysis and Ask Leggii", """<ol>
<li>Results of the AI lesson analysis and Ask Leggii are made by AI and <strong>can be wrong or incomplete.</strong> They do not replace what was said in the lesson or rehearsal; please check what matters.</li>
<li>Use the AI lesson analysis only for recordings you may make, with the consent of the people recorded.</li>
<li>Ask Leggii is free for up to 30 questions a day per device. We may limit use to prevent abuse.</li>
<li>Suggested actions that use AI time run only after you confirm them. The assistant never pays or buys for you.</li>
</ol>"""),
   ("welegato ID", """<ol>
<li>Signing in is optional; all basic features of Leggii work without it.</li>
<li>The ID is an account of welegato, run by the same company. Creating and using it is also governed by the <a href="https://welegato.com/legal/terms/" target="_blank" rel="noopener">welegato terms of use</a>; only people aged 16 or over can sign in.</li>
<li>You can delete the ID in Settings › welegato ID › Manage ID. It is then removed from all Vicino Labs apps; a Leggii Plus subscription must be cancelled separately in the store to stop payments.</li>
<li>How to end each contract is collected in Settings › Terms & policies › Cancel contracts (Verträge hier kündigen).</li>
</ol>"""),
   ("Send to a welegato chat", """<ol>
<li>Signed in with the welegato ID, you can send score PDFs, AI lesson-note PDFs and recordings (audio) in your Leggii cloud to someone you chat with on welegato. The file is not copied; they can open it for 7 days from sending. Ink and AI analysis results are not included. You can turn sharing off at any time in the welegato chat.</li>
<li>You must hold the rights needed for what you send, including copyright in the score and the performance and the consent of the people recorded. Scores or recordings scanned or copied without the rights holder's permission may not be sent. The sender is responsible for the content of the file and the rights in it; the company does not check files in advance.</li>
<li>A reported file is closed at once. If, after review, the company finds an infringement or illegal content, it may keep the sharing blocked and restrict use under the welegato terms.</li>
<li>To prevent misuse you can send up to 20 files a day and up to 500 MB at a time. The company may change these limits.</li>
</ol>"""),
   ("welegato and external services", """<p>The app links to and uses external services such as welegato, IMSLP and Google Play. They are separate from the app and governed by their own terms and privacy policies. The company is not responsible for their content or availability.</p>"""),
   ("Intellectual property", """<p>The company holds the rights to the app's logo, the name “Leggii”, its design, texts and source code. You may not copy, distribute, transmit, publish, reverse-engineer or create derivative works without prior written consent.</p>"""),
   ("Your obligations", """<ol>
<li>Do not reverse-engineer or decompile the app or circumvent payment.</li>
<li>Do not disrupt the app's normal operation.</li>
<li>Comply with applicable law and these terms.</li>
<li>Do not send files such as scores or recordings to a welegato chat without the rights needed (including scores or recordings scanned or copied without the rights holder's permission).</li>
</ol>"""),
   ("Changes and discontinuation", """<p>The company may change or discontinue all or part of the app for operational or technical reasons and will announce this in advance unless urgent. Changes to external services (such as IMSLP) may limit related features.</p>"""),
   ("Liability", """<ol>
<li>The company is liable without limitation for intent and gross negligence, for injury to life, body or health, and under the Product Liability Act.</li>
<li>For slight negligence the company is liable only for breach of essential contractual obligations, limited to the typical damage foreseeable when the contract was made.</li>
<li>Without the cloud, scores and notes are stored only on your device. To protect against loss of the device, deletion or reset, please make your own backups with “Back up library”.</li>
</ol>"""),
   ("Governing law and jurisdiction", """<p>German law applies. Mandatory consumer-protection rules of the country where you, as a consumer, habitually reside (e.g. an EU member state) remain unaffected. Otherwise the courts at the company's seat (Dortmund, Germany) have jurisdiction.</p>"""),
   ("Contact", "<p>For questions about these terms, please contact us.</p>" + _id_card("en")),
  ],
 },
 "de": {
  "title": "Leggii Nutzungsbedingungen",
  "h1": "Nutzungsbedingungen",
  "meta": [("Gültig ab", "21.12.2026"), ("Version", "1.3"), ("Betreiber", "Vicino Labs")],
  "lede": "Diese Bedingungen regeln die Nutzung von Leggii, einer Noten-App von Vicino Labs. Mit Installation und Nutzung der App stimmst du ihnen zu.",
  "footer": "Diese Bedingungen gelten ab dem 21. Dezember 2026 (Version 1.3, angekündigt am 9. November 2026). Bis dahin gilt Version 1.2 (6. November 2026). Vorherige Versionen 1.1: 5. November 2026, 1.0: 22. Oktober 2026.",
  "other": "Datenschutzerklärung →",
  "sections": [
   ("Geltungsbereich", "<p>Diese Bedingungen regeln die Nutzung der mobilen App Leggii („App“) von Vicino Labs („Anbieter“).</p>"),
   ("Anbieter", _op_ref("de")),
   ("Geltung und Änderungen", """<ol>
<li>Die Bedingungen gelten ab Veröffentlichung in der App oder auf andere vom Anbieter gewählte Weise.</li>
<li>Der Anbieter kann sie im Rahmen des Gesetzes ändern und kündigt Datum und Grund vorher an.</li>
<li>Wenn du geänderten Bedingungen nicht zustimmst, kannst du die App nicht mehr nutzen und löschen.</li>
</ol>"""),
   ("Leistungen", """<ol>
<li><strong>Kostenlos:</strong> PDF-Noten lesen und blättern (auch mit Pedal), Import, Foto-Scans, IMSLP-Suche, Notenpapier, Notizen und Grundzeichen, Ordner, Setlisten, PDFs zusammenfügen, Metronom, Bibliothekssicherung u. a.</li>
<li><strong>Pro:</strong> kein Banner, keine Hinweiszeile in geteilten Foto-Scans, eigene Stifte, weitere Zeichen, Wiederholungs- und D.C.-Sprünge, Seitenbearbeitung, PDF-Export mit Notizen sowie später hinzukommende Pro-Funktionen</li>
<li>Die kostenlose Version zeigt ein Banner für welegato, einen Dienst desselben Anbieters.</li>
<li><strong>KI-Unterrichtsanalyse:</strong> auf Wunsch Unterrichtsnotizen oder eine Mitschrift aus einer Aufnahme. Sie verbraucht KI-Zeit (Minuten).</li>
<li><strong>welegato-ID (freiwillig):</strong> angemeldet gelten Pro, Plus und KI-Zeit auf weiteren Geräten.</li>
<li><strong>Leggii fragen:</strong> ein KI-Assistent, der App und Tarife erklärt und bei Aktionen wie der Notensuche hilft (kostenlos, bis zu 30 Fragen pro Tag).</li>
</ol>"""),
   ("Pro, Leggii Plus und KI-Zeit", """<ol>
<li><strong>Testphase:</strong> Nach der ersten Installation kannst du die Pro-Funktionen <strong>7 Tage</strong> kostenlos nutzen, dazu einmal pro Gerät 30 KI-Minuten. Danach endet die Testphase von selbst; es gibt keine automatische Zahlung. Während der Testphase erstellte Notizen, Zeichen, Verknüpfungen und Seiten bleiben erhalten.</li>
<li><strong>Pro:</strong> ein einmaliger In-App-Kauf, <strong>dauerhaft</strong> nutzbar, mit 30 KI-Minuten pro Monat und einmalig 60 Willkommensminuten. Bei Neuinstallation mit demselben Store-Konto stellt „Kauf wiederherstellen“ ihn wieder her.</li>
<li><strong>Leggii Plus:</strong> ein monatliches oder jährliches <strong>Abo</strong> mit allen Pro-Funktionen und 5 Stunden KI-Zeit pro Monat. Es verlängert sich um denselben Zeitraum, bis du kündigst; kündigen kannst du jederzeit in den Abos von Google Play (oder dem App Store). Es läuft bis zum Ende des bezahlten Zeitraums; danach gilt wieder Pro, wenn du Pro gekauft hast, sonst die kostenlose Version.</li>
<li><strong>Leggii Cloud (Plus):</strong> Mit der welegato-ID angemeldet sind Noten, Notizen, Ordner, Setlists, Meine Notizen und – wenn du es eingeschaltet lässt – Aufnahmen auf den Geräten dieser ID gleich. Plus enthält 10 GB; für mehr Platz kannst du auf den 50-GB-Tarif wechseln (Google Play berechnet dann nur die Differenz für den Rest des Zeitraums). Ist die Cloud voll, stoppen nur neue Uploads, es wird nichts gelöscht. Was auf einem Gerät gelöscht wird, wird auch auf den anderen Geräten und in der Cloud gelöscht. Endet Plus, stoppen neue Uploads; 90 Tage lang kann alles heruntergeladen werden, nach zwei Erinnerungs-E-Mails werden die Cloud-Dateien gelöscht. Die Cloud dient dem Abgleich deiner eigenen Geräte. Andere können nur die Dateien öffnen, die du unten mit „An welegato-Chat senden“ auswählst, und nur für begrenzte Zeit. Wir empfehlen, Wichtiges zusätzlich mit „Bibliothek sichern“ aufzubewahren.</li>
<li><strong>Einführungspreis:</strong> Wer Plus bis zum 31. Dezember 2027 abonniert, behält diesen Preis, solange das Abo läuft. Für spätere neue Abos kann ein anderer Preis gelten.</li>
<li><strong>KI-Zeit-Aufladungen:</strong> 5 oder 15 Stunden, einmal bezahlt, kein Abo. Nutzbar 12 Monate ab Kauf, unabhängig von einem Plus-Abo.</li>
<li><strong>Berechnung der KI-Zeit:</strong> Unterrichtsnotizen verbrauchen 1 Minute pro Aufnahmeminute, Mitschriften 3 Minuten; die Kosten werden vor dem Start angezeigt. Zuerst werden die Monatsminuten verbraucht, dann Aufladungen. Monatsminuten verfallen am Monatsende. KI-Zeit hat keinen Geldwert und ist nicht übertragbar.</li>
<li><strong>welegato-ID und Käufe:</strong> Bei Anmeldung werden Käufe und KI-Zeit mit dieser ID verknüpft. Ein Kauf gehört zu der ID, mit der er zuerst verknüpft wurde.</li>
<li>Preise werden an der Kasse angezeigt. Zahlung und Erstattung richten sich nach den Regeln und Abläufen des jeweiligen Stores. Bei digitalen Inhalten kann das Widerrufsrecht im gesetzlich zulässigen Umfang erlöschen, wenn du dem sofortigen Beginn zustimmst; das Erstattungsverfahren des Stores bleibt möglich.</li>
<li>Wir entfernen zahlenden Nutzern zentrale Pro-Funktionen nicht ohne triftigen Grund. Änderungen der monatlichen KI-Zeit oder der Aufladebedingungen kündigen wir vorher an; sie gelten nicht für bereits bezahlte Zeiträume oder bereits gekaufte Zeit.</li>
</ol>"""),
   ("Noten und Urheberrecht", """<ol>
<li>Für die Einhaltung des Urheberrechts an importierten, gescannten oder geteilten Noten bist du selbst verantwortlich.</li>
<li>Noten von IMSLP werden zu den Bedingungen von IMSLP bereitgestellt; Schutzfristen sind je nach Land verschieden. Die App kennzeichnet Ausgaben, die in der EU noch geschützt sein können, die endgültige Beurteilung liegt aber bei dir.</li>
<li>Ohne Leggii Cloud bleiben deine Noten auf deinem Gerät. Mit der Cloud werden sie gespeichert, um deine eigenen Geräte abzugleichen; der Anbieter sieht sich ihren Inhalt nicht an.</li>
</ol>"""),
   ("Aufnahmen", """<ol>
<li>Die Aufnahmefunktion dient dazu, Unterricht, Proben, Ensembles und Üben für dein eigenes Üben und deine Notizen festzuhalten.</li>
<li>Werden Stimme oder Spiel anderer Personen aufgenommen (z. B. Lehrkraft, Dirigent oder Mitmusiker), musst du vor der Aufnahme ihre Einwilligung einholen. Für Aufnahmen oder deren Nutzung ohne Einwilligung bist du verantwortlich.</li>
<li>Bevor du eine Aufnahme weitergibst, veröffentlichst oder verbreitest, musst du sicherstellen, dass die aufgenommenen Personen einverstanden sind und Urheber- und Leistungsschutzrechte an der Musik dies erlauben.</li>
<li>Aufnahmen werden auf deinem Gerät gespeichert und nur dann auch in der Leggii Cloud, wenn du Aufnahmen in der Cloud einschaltest. Eine von dir gewünschte KI-Analyse verarbeitet sie nur kurz. Der Anbieter speichert die Aufnahmen auf deinem Gerät nicht und kann verlorene Aufnahmen nicht wiederherstellen. Sichere wichtige Aufnahmen mit „Bibliothek sichern“ oder indem du sie sendest.</li>
</ol>"""),
   ("KI-Unterrichtsanalyse und „Leggii fragen“", """<ol>
<li>Ergebnisse der KI-Unterrichtsanalyse und von „Leggii fragen“ erstellt eine KI; sie <strong>können falsch oder unvollständig sein.</strong> Sie ersetzen nicht, was im Unterricht oder in der Probe gesagt wurde; bitte prüfe Wichtiges selbst.</li>
<li>Nutze die KI-Unterrichtsanalyse nur für Aufnahmen, die du machen darfst, mit Einwilligung der aufgenommenen Personen.</li>
<li>„Leggii fragen“ ist kostenlos für bis zu 30 Fragen pro Tag und Gerät. Zum Schutz vor Missbrauch können wir die Nutzung begrenzen.</li>
<li>Vorgeschlagene Aktionen, die KI-Zeit verbrauchen, starten erst nach deiner Bestätigung. Der Assistent zahlt oder kauft nie für dich.</li>
</ol>"""),
   ("welegato-ID", """<ol>
<li>Die Anmeldung ist freiwillig; alle Grundfunktionen von Leggii funktionieren ohne sie.</li>
<li>Die ID ist ein Konto von welegato, einem Dienst desselben Unternehmens. Für Erstellung und Nutzung gelten zusätzlich die <a href="https://welegato.com/legal/terms/" target="_blank" rel="noopener">Nutzungsbedingungen von welegato</a>; anmelden können sich nur Personen ab 16 Jahren.</li>
<li>Du kannst die ID unter Einstellungen › welegato-ID › ID verwalten löschen. Sie wird dann in allen Apps von Vicino Labs entfernt; ein Leggii-Plus-Abo musst du zusätzlich im Store kündigen, damit die Zahlungen enden.</li>
<li>Wie du jeden Vertrag beendest, steht gesammelt unter Einstellungen › AGB & Richtlinien › Verträge hier kündigen.</li>
</ol>"""),
   ("An welegato-Chat senden", """<ol>
<li>Mit der welegato-ID angemeldet kannst du Noten-PDFs, PDFs mit KI-Unterrichtsnotizen und Aufnahmen (Audio) aus deiner Leggii Cloud an jemanden senden, mit dem du auf welegato chattest. Die Datei wird nicht kopiert; die andere Person kann sie ab dem Senden 7 Tage lang öffnen. Notizen auf den Noten und KI-Analyseergebnisse werden nicht mitgesendet. Du kannst das Teilen im welegato-Chat jederzeit beenden.</li>
<li>Du musst die nötigen Rechte an dem haben, was du sendest – einschließlich der Urheberrechte an Noten und Darbietung und der Einwilligung der aufgenommenen Personen. Ohne Erlaubnis der Rechteinhaber gescannte oder kopierte Noten oder Aufnahmen dürfen nicht gesendet werden. Für Inhalt und Rechte der Datei ist die Person verantwortlich, die sie sendet; der Anbieter prüft Dateien nicht vorab.</li>
<li>Eine gemeldete Datei wird sofort geschlossen. Stellt der Anbieter nach Prüfung eine Rechtsverletzung oder rechtswidrige Inhalte fest, kann er das Teilen gesperrt lassen und die Nutzung nach den welegato-Nutzungsbedingungen einschränken.</li>
<li>Um Missbrauch zu verhindern, kannst du bis zu 20 Dateien pro Tag und bis zu 500 MB auf einmal senden. Der Anbieter kann diese Grenzen ändern.</li>
</ol>"""),
   ("welegato und externe Dienste", """<p>Die App verlinkt und nutzt externe Dienste wie welegato, IMSLP und Google Play. Sie sind von der App getrennt; es gelten deren eigene Bedingungen und Datenschutzerklärungen. Für deren Inhalte und Verfügbarkeit ist der Anbieter nicht verantwortlich.</p>"""),
   ("Geistiges Eigentum", """<p>Die Rechte an Logo, dem Namen „Leggii“, Gestaltung, Texten und Quellcode der App liegen beim Anbieter. Ohne vorherige schriftliche Zustimmung sind Vervielfältigung, Verbreitung, Übertragung, Veröffentlichung, Reverse Engineering und Bearbeitungen nicht erlaubt.</p>"""),
   ("Pflichten der Nutzer", """<ol>
<li>Kein Reverse Engineering oder Dekompilieren der App und keine Umgehung der Bezahlung.</li>
<li>Keine Störung des normalen Betriebs der App.</li>
<li>Einhaltung der Gesetze und dieser Bedingungen.</li>
<li>Keine Dateien wie Noten oder Aufnahmen ohne die nötigen Rechte an einen welegato-Chat senden (auch keine ohne Erlaubnis der Rechteinhaber gescannten oder kopierten Noten oder Aufnahmen).</li>
</ol>"""),
   ("Änderung und Einstellung", """<p>Der Anbieter kann Funktionen der App aus betrieblichen oder technischen Gründen ganz oder teilweise ändern oder einstellen und kündigt dies, außer in dringenden Fällen, vorher an. Änderungen externer Dienste (z. B. IMSLP) können zugehörige Funktionen einschränken.</p>"""),
   ("Haftung", """<ol>
<li>Der Anbieter haftet unbeschränkt bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit sowie nach dem Produkthaftungsgesetz.</li>
<li>Bei leichter Fahrlässigkeit haftet der Anbieter nur bei Verletzung wesentlicher Vertragspflichten und begrenzt auf den bei Vertragsschluss vorhersehbaren, typischen Schaden.</li>
<li>Ohne Cloud werden Noten und Notizen nur auf deinem Gerät gespeichert. Sichere sie mit „Bibliothek sichern“ gegen Verlust des Geräts, Löschung oder Zurücksetzen.</li>
</ol>"""),
   ("Anwendbares Recht und Gerichtsstand", """<p>Es gilt deutsches Recht. Zwingende Verbraucherschutzvorschriften des Staates, in dem du als Verbraucher deinen gewöhnlichen Aufenthalt hast (z. B. ein EU-Mitgliedstaat), bleiben unberührt. Im Übrigen ist Gerichtsstand der Sitz des Anbieters (Dortmund).</p>"""),
   ("Kontakt", "<p>Fragen zu diesen Bedingungen richte bitte an:</p>" + _id_card("de")),
  ],
 },
 "it": {
  "title": "Leggii — Termini di utilizzo",
  "h1": "Termini di utilizzo",
  "meta": [("In vigore dal", "21.12.2026"), ("Versione", "1.3"), ("Gestore", "Vicino Labs")],
  "lede": "Questi termini regolano l'uso di Leggii, un'app per spartiti di Vicino Labs. Installando e usando l'app li accetti.",
  "footer": "Questi termini sono in vigore dal 21 dicembre 2026 (versione 1.3, annunciata il 9 novembre 2026). Fino ad allora vale la versione 1.2 (6 novembre 2026). Versioni precedenti 1.1: 5 novembre 2026, 1.0: 22 ottobre 2026.",
  "other": "Informativa sulla privacy →",
  "sections": [
   ("Oggetto", "<p>Questi termini regolano l'uso dell'app mobile Leggii (“app”) fornita da Vicino Labs (“fornitore”).</p>"),
   ("Fornitore", _op_ref("it")),
   ("Validità e modifiche", """<ol>
<li>I termini sono validi dalla pubblicazione nell'app o in altro modo scelto dal fornitore.</li>
<li>Il fornitore può modificarli nei limiti di legge, comunicando in anticipo data e motivo.</li>
<li>Se non accetti i termini modificati puoi smettere di usare l'app ed eliminarla.</li>
</ol>"""),
   ("Cosa offre l'app", """<ol>
<li><strong>Gratis:</strong> lettura di spartiti PDF e cambio pagina (anche con pedale), importazione, scansioni da foto, ricerca IMSLP, carta pentagrammata, annotazioni e simboli di base, cartelle, scalette, unione di PDF, metronomo, backup della libreria e altro</li>
<li><strong>Pro:</strong> niente banner, nessuna riga di credito sulle scansioni condivise, penne personali, altri simboli, salti per ritornelli e D.C., modifica delle pagine, esportazione PDF con annotazioni e le funzioni Pro future</li>
<li>La versione gratuita mostra un banner di welegato, un servizio dello stesso fornitore.</li>
<li><strong>Analisi AI delle lezioni:</strong> su richiesta, note della lezione o una trascrizione da una registrazione. Usa tempo AI (minuti).</li>
<li><strong>welegato ID (facoltativo):</strong> con l'accesso, Pro, Plus e tempo AI ti seguono su altri dispositivi.</li>
<li><strong>Chiedi a Leggii:</strong> un assistente AI che spiega l'app e i piani e aiuta con azioni come trovare uno spartito (gratuito, fino a 30 domande al giorno).</li>
</ol>"""),
   ("Pro, Leggii Plus e tempo AI", """<ol>
<li><strong>Prova gratuita:</strong> dopo la prima installazione puoi usare le funzioni Pro gratis per <strong>7 giorni</strong>, più 30 minuti AI una sola volta per dispositivo. Poi la prova termina da sola; non c'è alcun pagamento automatico. Annotazioni, simboli, collegamenti e pagine creati durante la prova restano.</li>
<li><strong>Pro:</strong> un acquisto in-app unico, <strong>per sempre</strong>, con 30 minuti AI al mese e un bonus di benvenuto unico di 60 minuti. Reinstallando con lo stesso account dello store, «Ripristina acquisto» lo recupera.</li>
<li><strong>Leggii Plus:</strong> un <strong>abbonamento</strong> mensile o annuale con tutte le funzioni Pro e 5 ore di tempo AI al mese. Si rinnova per lo stesso periodo fino alla disdetta; puoi annullarlo in qualsiasi momento negli abbonamenti di Google Play (o dell'App Store). Resta attivo fino alla fine del periodo pagato; poi torni a Pro se lo hai acquistato, altrimenti alla versione gratuita.</li>
<li><strong>Cloud di Leggii (Plus):</strong> con il welegato ID connesso, spartiti, annotazioni, cartelle, scalette, Le mie note e – se lo lasci attivo – le registrazioni restano uguali sui dispositivi di quell'ID. Plus include 10 GB; per più spazio puoi passare al piano da 50 GB (Google Play addebita solo la differenza per il resto del periodo). Quando il cloud è pieno si fermano solo i nuovi caricamenti e nulla viene eliminato. Ciò che elimini su un dispositivo viene eliminato anche sugli altri dispositivi e nel cloud. Quando Plus termina, i nuovi caricamenti si fermano, per 90 giorni puoi scaricare tutto e, dopo due email di promemoria, i file nel cloud vengono eliminati. Il cloud serve a sincronizzare i tuoi dispositivi. Altre persone possono aprire solo i file che scegli con «Invia a una chat welegato» qui sotto, e solo per un periodo limitato. Consigliamo di conservare il materiale importante anche con “Backup della libreria”.</li>
<li><strong>Prezzo di lancio:</strong> chi si abbona a Plus entro il 31 dicembre 2027 mantiene quel prezzo finché resta abbonato. Ai nuovi abbonamenti successivi può applicarsi un prezzo diverso.</li>
<li><strong>Ricariche di tempo AI:</strong> 5 o 15 ore, pagate una volta, non un abbonamento. Utilizzabili per 12 mesi dall'acquisto, con o senza Plus.</li>
<li><strong>Come si conta il tempo AI:</strong> le note della lezione usano 1 minuto per minuto di registrazione, le trascrizioni 3 minuti; il costo è mostrato prima di iniziare. Prima si usano i minuti mensili, poi le ricariche. I minuti mensili non si accumulano. Il tempo AI non ha valore in denaro e non è trasferibile.</li>
<li><strong>welegato ID e acquisti:</strong> con l'accesso, acquisti e tempo AI vengono collegati a quell'ID. Un acquisto appartiene al primo ID a cui è stato collegato.</li>
<li>I prezzi sono indicati al momento del pagamento. Pagamenti e rimborsi seguono le regole e le procedure di ciascuno store. Per i contenuti digitali, se accetti l'inizio immediato dell'uso, il diritto di recesso può estinguersi nei limiti di legge; la procedura di rimborso dello store resta disponibile.</li>
<li>Non togliamo funzioni Pro essenziali agli utenti paganti senza un valido motivo. Le modifiche al tempo AI mensile o alle condizioni delle ricariche vengono annunciate prima e non valgono per periodi già pagati o tempo già acquistato.</li>
</ol>"""),
   ("Spartiti e diritto d'autore", """<ol>
<li>Sei responsabile del rispetto del diritto d'autore sugli spartiti che importi, scansioni o condividi.</li>
<li>Gli spartiti di IMSLP sono forniti alle condizioni di IMSLP e la durata della protezione varia da paese a paese. L'app segnala le edizioni che potrebbero essere ancora protette nell'UE, ma la valutazione finale spetta a te.</li>
<li>Senza il cloud di Leggii i tuoi spartiti restano sul dispositivo. Con il cloud vengono salvati per sincronizzare i tuoi dispositivi; il fornitore non ne esamina il contenuto.</li>
</ol>"""),
   ("Registrazioni", """<ol>
<li>La funzione di registrazione serve a conservare lezioni, prove, ensemble e studio per il tuo esercizio e i tuoi appunti.</li>
<li>Se vengono registrate la voce o l'esecuzione di altre persone (ad es. insegnante, direttore o colleghi), devi ottenere il loro consenso prima di registrare. La responsabilità di registrazioni o usi senza consenso è tua.</li>
<li>Prima di inviare una registrazione ad altri, pubblicarla o diffonderla, devi assicurarti che le persone registrate siano d'accordo e che il diritto d'autore e i diritti degli interpreti sulla musica lo consentano.</li>
<li>Le registrazioni sono salvate sul tuo dispositivo e, solo se attivi le registrazioni nel cloud, anche nel cloud di Leggii. Un'analisi AI che hai chiesto le tratta solo brevemente. Il fornitore non conserva le registrazioni del tuo dispositivo e non può recuperare registrazioni perse. Conserva quelle importanti con “Backup della libreria” o inviandole.</li>
</ol>"""),
   ("Analisi AI delle lezioni e «Chiedi a Leggii»", """<ol>
<li>I risultati dell'analisi AI e di «Chiedi a Leggii» sono generati da un'AI e <strong>possono essere errati o incompleti.</strong> Non sostituiscono quanto detto a lezione o in prova; verifica ciò che è importante.</li>
<li>Usa l'analisi AI solo per registrazioni che puoi fare, con il consenso delle persone registrate.</li>
<li>«Chiedi a Leggii» è gratuito fino a 30 domande al giorno per dispositivo. Possiamo limitarne l'uso per prevenire abusi.</li>
<li>Le azioni proposte che usano tempo AI partono solo dopo la tua conferma. L'assistente non paga né acquista mai al posto tuo.</li>
</ol>"""),
   ("welegato ID", """<ol>
<li>L'accesso è facoltativo; tutte le funzioni di base di Leggii funzionano anche senza.</li>
<li>L'ID è un account di welegato, servizio della stessa società. Per crearlo e usarlo valgono anche i <a href="https://welegato.com/legal/terms/" target="_blank" rel="noopener">termini di welegato</a>; possono accedere solo persone dai 16 anni in su.</li>
<li>Puoi eliminare l'ID in Impostazioni › welegato ID › Gestisci ID. Viene rimosso da tutte le app di Vicino Labs; un abbonamento Leggii Plus va disdetto a parte nello store perché i pagamenti si fermino.</li>
<li>Come chiudere ogni contratto è riassunto in Impostazioni › Termini e informative › Disdici contratti (Verträge hier kündigen).</li>
</ol>"""),
   ("Invia a una chat welegato", """<ol>
<li>Con il welegato ID connesso puoi inviare PDF di spartiti, PDF di note di lezione AI e registrazioni (audio) del tuo cloud di Leggii a una persona con cui chatti su welegato. Il file non viene copiato; l'altra persona può aprirlo per 7 giorni dall'invio. Annotazioni e risultati delle analisi AI non vengono inviati. Puoi disattivare la condivisione in qualsiasi momento nella chat welegato.</li>
<li>Devi avere i diritti necessari su ciò che invii, compresi i diritti d'autore su spartito ed esecuzione e il consenso delle persone registrate. Non si possono inviare spartiti o registrazioni scansionati o copiati senza il permesso del titolare dei diritti. Chi invia è responsabile del contenuto del file e dei relativi diritti; il fornitore non controlla i file in anticipo.</li>
<li>Un file segnalato viene chiuso subito. Se dopo la verifica il fornitore riscontra una violazione o contenuti illeciti, può mantenere bloccata la condivisione e limitare l'uso secondo i termini di welegato.</li>
<li>Per evitare abusi puoi inviare fino a 20 file al giorno e fino a 500 MB alla volta. Il fornitore può modificare questi limiti.</li>
</ol>"""),
   ("welegato e servizi esterni", """<p>L'app collega e usa servizi esterni come welegato, IMSLP e Google Play. Sono separati dall'app e regolati dai propri termini e informative. Il fornitore non risponde del loro contenuto o della loro disponibilità.</p>"""),
   ("Proprietà intellettuale", """<p>I diritti su logo, nome “Leggii”, grafica, testi e codice sorgente dell'app appartengono al fornitore. Senza consenso scritto preventivo non è consentito copiare, distribuire, trasmettere, pubblicare, decompilare o creare opere derivate.</p>"""),
   ("Obblighi dell'utente", """<ol>
<li>Non decompilare o analizzare l'app né aggirare il pagamento.</li>
<li>Non ostacolare il normale funzionamento dell'app.</li>
<li>Rispettare la legge e questi termini.</li>
<li>Non inviare a una chat welegato file come spartiti o registrazioni senza i diritti necessari (compresi spartiti o registrazioni scansionati o copiati senza il permesso del titolare dei diritti).</li>
</ol>"""),
   ("Modifica e sospensione", """<p>Il fornitore può modificare o sospendere in tutto o in parte le funzioni dell'app per motivi organizzativi o tecnici, avvisando prima salvo urgenza. Cambiamenti dei servizi esterni (come IMSLP) possono limitare le funzioni collegate.</p>"""),
   ("Responsabilità", """<ol>
<li>Il fornitore risponde senza limiti per dolo e colpa grave, per danni alla vita, al corpo o alla salute e ai sensi della legge sulla responsabilità del produttore.</li>
<li>Per colpa lieve risponde solo in caso di violazione di obblighi contrattuali essenziali, nei limiti del danno tipico prevedibile alla conclusione del contratto.</li>
<li>Senza il cloud, spartiti e annotazioni sono salvati solo sul dispositivo. Fai i tuoi backup con “Backup della libreria” contro perdita del dispositivo, cancellazione o ripristino.</li>
</ol>"""),
   ("Legge applicabile e foro", """<p>Si applica la legge tedesca. Restano salve le norme imperative a tutela dei consumatori del paese in cui risiedi abitualmente (ad es. uno Stato UE). Per il resto è competente il foro della sede del fornitore (Dortmund, Germania).</p>"""),
   ("Contatti", "<p>Per domande su questi termini scrivici:</p>" + _id_card("it")),
  ],
 },
}

_fix_end(TERMS)
