"""Nomio 이용약관 본문 (ko/en/de) — nomio_legal.py가 HTML로 만든다.

2026-10-01 버전 4.0: nomio-privacy(GitHub Pages)에서 옮기며 운영자 연락처, 서비스
내용(앱 안 알림·테마), 프리미엄 구성과 디지털 콘텐츠 철회권 문구를 고쳤다.
"""

TERMS = {'ko': {'title': 'Nomio 이용약관',
        'h1': '이용약관',
        'meta': [('시행일', '2026.10.01'), ('버전', '4.0'), ('운영자', 'Vicino Labs')],
        'lede': '본 약관은 Vicino Labs가 만든 다통화 가계부 앱 Nomio를 이용하시는 분들과 저희 사이의 약속을 담고 있습니다. 앱을 설치하고 이용하시는 순간부터 아래 내용에 동의하신 '
                '것으로 봅니다.',
        'footer': '본 약관은 2026년 10월 1일부터 시행됩니다 (버전 4.0).',
        'other': '개인정보처리방침 보기 →',
        'sections': [('목적',
                      '<p>본 약관은 Vicino Labs(이하 "회사")가 제공하는 모바일 애플리케이션 Nomio(이하 "앱")의 이용과 관련하여 회사와 이용자 간의 권리, 의무 및 '
                      '책임사항을 규정함을 목적으로 합니다.</p>'),
                     ('정의',
                      '<ol>\n'
                      '<li><strong>"앱"</strong>이란 회사가 제작한 개인용 다통화 가계부 애플리케이션 Nomio를 말합니다.</li>\n'
                      '<li><strong>"이용자"</strong>란 본 약관에 따라 앱을 설치하고 이용하는 자를 말합니다.</li>\n'
                      '<li><strong>"콘텐츠"</strong>란 앱 내에서 제공되는 화면 구성, 로고, 디자인, 소스코드 등 일체의 저작물을 말합니다.</li>\n'
                      '</ol>'),
                     ('사업자 정보',
                      '<div class="id-card"><dt>상호</dt><dd>Vicino Labs (개인사업자, '
                      'Einzelunternehmen)</dd><dt>대표자</dt><dd>Jeong-Hwan Lee</dd><dt>주소</dt><dd>Ruhrallee 41, 44139 '
                      'Dortmund, Germany</dd><dt>이메일</dt><dd><a '
                      'href="mailto:contact@vicinolabs.com">contact@vicinolabs.com</a></dd><dt>Impressum</dt><dd><a '
                      'href="/impressum/">vicinolabs.com/impressum</a></dd></div>'),
                     ('약관의 효력 및 변경',
                      '<ol>\n'
                      '<li>본 약관은 앱 내 또는 회사가 정한 방법으로 공지함으로써 효력이 발생합니다.</li>\n'
                      '<li>회사는 필요한 경우 관련 법령을 위반하지 않는 범위에서 본 약관을 개정할 수 있으며, 개정 시 적용일자 및 개정사유를 명시하여 사전에 공지합니다.</li>\n'
                      '<li>이용자가 개정 약관에 동의하지 않는 경우 앱 이용을 중단하고 삭제할 수 있으며, 개정약관 공지 후에도 계속 앱을 이용하는 경우 개정약관에 동의한 것으로 '
                      '봅니다.</li>\n'
                      '</ol>'),
                     ('서비스의 내용',
                      '<p>앱은 다음과 같은 기능을 제공합니다.</p>\n'
                      '<ol>\n'
                      '<li>지출·수입·계좌·자산 기록 및 다통화 환산, 예산 관리, 반복 거래, 통계·추이 화면</li>\n'
                      '<li>영수증 사진 첨부와 금액 인식, 거래 검색·필터, CSV/JSON 백업 내보내기·가져오기</li>\n'
                      '<li>선택적 구글드라이브 백업/복원</li>\n'
                      '<li>앱 잠금(생체 인증), 예산 초과·반복 거래 안내(앱 안에서 표시)</li>\n'
                      '<li>다국어, 다크 모드, 테마 색상 등 화면 설정</li>\n'
                      '<li>인앱 결제로 구매하는 프리미엄(광고 제거 및 추가 기능)</li>\n'
                      '</ol>'),
                     ('서비스 이용 관련 유의사항',
                      '<ol>\n'
                      '<li>앱은 개인이 지출·수입을 기록하고 관리하도록 돕는 도구이며, <strong>투자·세무·재무 자문을 제공하지 않으며</strong> 어떠한 재무적 결정에 대한 '
                      '조언으로 해석되어서는 안 됩니다.</li>\n'
                      '<li>환율 정보는 참고용이며, 실제 거래 시점의 환율과 다를 수 있고 그 정확성이 보장되지 않습니다.</li>\n'
                      '<li>금융 데이터는 기본적으로 이용자의 기기에만 저장됩니다. 기기 분실, 앱 삭제, 초기화 등으로 인한 데이터 손실에 대해 이용자가 스스로 백업 여부를 결정하고 '
                      '책임집니다.</li>\n'
                      '</ol>'),
                     ('지적재산권',
                      '<p>앱에 포함된 로고, 상표("Nomio" 명칭 및 엠블럼 포함), 디자인, 문구, 소스코드 등 일체의 콘텐츠에 대한 저작권 및 지적재산권은 회사에 귀속됩니다. 이용자는 '
                      '회사의 사전 서면 동의 없이 이를 복제, 배포, 전송, 출판, 2차적저작물 작성, 역설계 등의 방법으로 이용하거나 제3자에게 이용하게 할 수 없습니다.</p>'),
                     ('이용자의 의무',
                      '<p>이용자는 다음 행위를 하여서는 안 됩니다.</p>\n'
                      '<ol>\n'
                      '<li>앱을 역설계(리버스 엔지니어링), 디컴파일 또는 소스코드를 추출하는 행위</li>\n'
                      '<li>앱의 정상적인 운영을 방해하거나 다른 이용자의 이용을 방해하는 행위</li>\n'
                      '<li>관련 법령 및 본 약관을 위반하는 행위</li>\n'
                      '</ol>'),
                     ('유료 서비스(프리미엄) 및 결제',
                      '<ol>\n'
                      '<li>앱은 기본적으로 무료이며, 무료 이용 시 Google AdMob 광고가 표시됩니다.</li>\n'
                      '<li>이용자는 인앱 결제로 <strong>프리미엄을 일회성으로</strong> 구매할 수 있습니다. 프리미엄에는 광고 제거, PDF 월간 보고서, 저축 목표, 예산 '
                      '이월, 추가 위젯 스타일, 계좌·카테고리·반복 거래 개수 제한 해제가 포함됩니다. 구독이 아니므로 해지 절차가 필요 없습니다.</li>\n'
                      '<li>가격은 이용자가 속한 스토어(Google Play/Apple App Store) 화면에 표시된 금액에 따르며, 결제는 해당 스토어가 처리합니다.</li>\n'
                      '<li>환불은 결제가 이루어진 스토어의 환불 정책과 절차에 따르며, 회사가 직접 환불을 처리하지 않습니다. 기기를 바꾸면 같은 스토어 계정으로 “구매 복원”을 눌러 되살릴 '
                      '수 있습니다.</li>\n'
                      '<li>디지털 콘텐츠의 특성상, 이용자가 계약 이행이 즉시 시작되는 데 명시적으로 동의하고 그로 인해 철회권을 잃는다는 점을 확인한 경우 관련 법령에 따라 청약철회권이 '
                      '소멸할 수 있습니다(독일 민법 제356조 5항).</li>\n'
                      '</ol>'),
                     ('광고',
                      '<ol>\n'
                      '<li>무료 버전에는 Google AdMob이 제공하는 광고가 포함됩니다. 광고 관련 정보 처리에 관한 자세한 사항은 개인정보처리방침을 따릅니다.</li>\n'
                      '<li>광고의 내용은 Google 및 광고주에 의해 결정되며, 회사는 개별 광고의 내용을 사전에 통제하지 않습니다. 광고를 통해 노출되는 제3자의 상품·서비스에 대해 '
                      '회사는 책임을 지지 않습니다.</li>\n'
                      '</ol>'),
                     ('서비스의 변경, 중단 및 종료',
                      '<ol>\n'
                      '<li>회사는 운영상·기술상의 필요에 따라 앱이 제공하는 서비스의 전부 또는 일부를 변경하거나 중단할 수 있습니다.</li>\n'
                      '<li>회사는 긴급한 사정(보안, 법령 준수 등)이 있는 경우를 제외하고, 서비스 중단 시 이를 사전에 공지합니다.</li>\n'
                      '</ol>'),
                     ('면책조항',
                      '<ol>\n'
                      '<li>앱은 <strong>"있는 그대로(AS-IS)"</strong> 제공되며, 회사는 환율·계산 결과 등 앱이 제공하는 정보의 완전성·정확성·최신성을 보증하지 '
                      '않습니다.</li>\n'
                      '<li>회사는 이용자의 재무적 의사결정 결과, 기기 고장·데이터 손상·백업 미사용으로 인한 데이터 유실, 제3자 서비스(환율 API, Google Drive, Google '
                      'AdMob 등)의 장애나 정책 변경으로 인한 서비스 이용 제한에 대해 고의 또는 중과실이 없는 한 책임을 지지 않습니다.</li>\n'
                      '<li>회사는 천재지변, 정전, 이용자의 귀책사유 등 통상적인 관리 범위를 벗어난 사유로 서비스를 제공할 수 없는 경우 책임이 면제됩니다.</li>\n'
                      '<li>관련 법령이 허용하는 최대 범위에서, 회사의 배상 책임은 이용자가 실제로 지급한 금액(무료 이용의 경우 0원)을 한도로 합니다.</li>\n'
                      '</ol>'),
                     ('준거법 및 관할',
                      '<p>본 약관의 해석 및 회사와 이용자 간의 분쟁에 관하여는 독일연방공화국 법을 준거법으로 합니다. 소비자인 이용자가 자신의 상거소가 있는 국가(예: 유럽연합 회원국)의 '
                      '강행법규에 따라 부여받는 소비자보호 권리는 이에 영향을 받지 않습니다. 그 외의 경우, 분쟁에 대한 관할법원은 회사의 소재지(독일 도르트문트)를 관할하는 법원으로 '
                      '합니다.</p>'),
                     ('문의처',
                      '<p>약관에 관한 문의사항이 있으시면 아래로 연락해 주세요.</p>\n'
                      '<div class="contact-card"><span class="role">Operator</span><span class="name">Vicino '
                      'Labs</span><a href="mailto:contact@vicinolabs.com">contact@vicinolabs.com</a></div>')]},
 'en': {'title': 'Nomio Terms of Service',
        'h1': 'Terms of Service',
        'meta': [('Effective', '2026-10-01'), ('Version', '4.0'), ('Operator', 'Vicino Labs')],
        'lede': 'These Terms set out the agreement between you and us for using Nomio, a multi-currency budgeting app '
                'made by Vicino Labs. By installing and using the app, you agree to what follows.',
        'footer': 'These Terms are effective as of October 1, 2026 (version 4.0).',
        'other': 'View Privacy Policy →',
        'sections': [('Purpose',
                      '<p>These Terms govern the rights, obligations, and responsibilities between Vicino Labs ("we", '
                      '"us", "the Company") and users of the mobile application Nomio (the "App").</p>'),
                     ('Definitions',
                      '<ol>\n'
                      '<li><strong>"App"</strong> means Nomio, a personal multi-currency budgeting application made by '
                      'the Company.</li>\n'
                      '<li><strong>"User"</strong> means anyone who installs and uses the App under these Terms.</li>\n'
                      '<li><strong>"Content"</strong> means the App\'s screens, logos, design, and source code.</li>\n'
                      '</ol>'),
                     ('About the operator',
                      '<div class="id-card"><dt>Trading name</dt><dd>Vicino Labs (sole proprietorship, '
                      'Einzelunternehmen)</dd><dt>Owner</dt><dd>Jeong-Hwan Lee</dd><dt>Address</dt><dd>Ruhrallee 41, '
                      '44139 Dortmund, Germany</dd><dt>Email</dt><dd><a '
                      'href="mailto:contact@vicinolabs.com">contact@vicinolabs.com</a></dd><dt>Legal notice</dt><dd><a '
                      'href="/impressum/">vicinolabs.com/impressum</a></dd></div>'),
                     ('Effect and changes to these Terms',
                      '<ol>\n'
                      '<li>These Terms take effect once posted in the App or by any other method we designate.</li>\n'
                      '<li>We may amend these Terms within the limits of applicable law, and will give advance notice '
                      'of the effective date and the reason for any change.</li>\n'
                      "<li>If you don't agree to amended Terms, you may stop using the App and delete it. Continuing "
                      'to use the App after amended Terms take effect means you accept them.</li>\n'
                      '</ol>'),
                     ('The service',
                      '<p>The App provides:</p>\n'
                      '<ol>\n'
                      '<li>Expense, income, account and asset tracking with multi-currency conversion, budgeting, '
                      'recurring transactions, and statistics/trend views</li>\n'
                      '<li>Receipt photo attachments with amount recognition, transaction search/filtering, and '
                      'CSV/JSON backup export/import</li>\n'
                      '<li>Optional Google Drive backup/restore</li>\n'
                      '<li>App lock (biometrics) and in-app reminders for budget overspend and recurring '
                      'transactions</li>\n'
                      '<li>Multiple languages and display settings including dark mode and theme colors</li>\n'
                      '<li>Premium (no ads plus extra features) as an in-app purchase</li>\n'
                      '</ol>'),
                     ('Important notes on using the service',
                      '<ol>\n'
                      '<li>The App is a tool for tracking your own income and expenses. It <strong>does not provide '
                      'investment, tax, or financial advice</strong>, and nothing in it should be read as advice on '
                      'any financial decision.</li>\n'
                      '<li>Exchange-rate data is for reference only, may differ from the rate at the time of an actual '
                      'transaction, and its accuracy is not guaranteed.</li>\n'
                      '<li>Your financial data is stored only on your device by default. You are responsible for '
                      'deciding whether and how to back it up, and for any loss of data due to a lost device, app '
                      'deletion, or a reset.</li>\n'
                      '</ol>'),
                     ('Intellectual property',
                      "<p>All copyright and intellectual property rights in the App's logo, trademarks (including the "
                      '"Nomio" name and emblem), design, copy, and source code belong to the Company. Users may not '
                      'reproduce, distribute, transmit, publish, reverse-engineer, or create derivative works from any '
                      'of this without our prior written consent, nor allow a third party to do so.</p>'),
                     ('Your obligations',
                      '<p>You must not:</p>\n'
                      '<ol>\n'
                      '<li>Reverse-engineer, decompile, or extract source code from the App</li>\n'
                      "<li>Interfere with the App's normal operation or with other users' use of it</li>\n"
                      '<li>Violate applicable law or these Terms</li>\n'
                      '</ol>'),
                     ('Paid features (Premium) & payment',
                      '<ol>\n'
                      '<li>The App is free to use by default; the free version shows ads served through Google '
                      'AdMob.</li>\n'
                      '<li>You can buy <strong>Premium as a one-time</strong> in-app purchase. Premium removes ads and '
                      'unlocks PDF monthly reports, savings goals, budget rollover, extra widget styles, and unlimited '
                      'accounts, categories and recurring transactions. It is not a subscription, so no cancellation '
                      'is needed.</li>\n'
                      '<li>Pricing follows the amount shown in your store (Google Play/Apple App Store), and payment '
                      'is processed by that store.</li>\n'
                      '<li>Refunds follow the policy and process of the store that processed the payment; we do not '
                      'process refunds directly. When you switch devices, use “Restore purchase” with the same store '
                      'account.</li>\n'
                      '<li>For digital content, your right of withdrawal may expire once performance has begun with '
                      'your express consent and your acknowledgment that you thereby lose the right of withdrawal (§ '
                      '356(5) of the German Civil Code), to the extent permitted by law.</li>\n'
                      '</ol>'),
                     ('Advertising',
                      '<ol>\n'
                      '<li>The free version includes ads served through Google AdMob. See our Privacy Policy for '
                      'details on how ad-related data is processed.</li>\n'
                      '<li>Ad content is determined by Google and its advertisers; we do not control the content of '
                      'individual ads in advance and are not responsible for third-party products or services '
                      'advertised through them.</li>\n'
                      '</ol>'),
                     ('Changes, suspension, and discontinuation of the service',
                      '<ol>\n'
                      "<li>We may change or discontinue all or part of the App's services for operational or technical "
                      'reasons.</li>\n'
                      '<li>Except in urgent circumstances (security, legal compliance, etc.), we will give advance '
                      'notice before suspending the service.</li>\n'
                      '</ol>'),
                     ('Disclaimer of liability',
                      '<ol>\n'
                      '<li>The App is provided <strong>"as is"</strong>; we do not warrant the completeness, accuracy, '
                      'or timeliness of exchange-rate data, calculations, or any other information the App '
                      'provides.</li>\n'
                      '<li>Except in cases of intent or gross negligence, we are not liable for the outcome of your '
                      'financial decisions, for data loss due to device failure, data corruption, or not using backup, '
                      'or for service limitations arising from an outage or policy change at a third-party service '
                      '(exchange-rate API, Google Drive, Google AdMob, etc.).</li>\n'
                      '<li>We are not liable for failing to provide the service due to force majeure, power outages, '
                      'causes attributable to the user, or other circumstances outside our normal control.</li>\n'
                      '<li>To the maximum extent permitted by law, our liability for damages is limited to the amount '
                      'you actually paid (zero for free use).</li>\n'
                      '</ol>'),
                     ('Governing law and venue',
                      '<p>These Terms and any dispute between the Company and a user are governed by the laws of the '
                      'Federal Republic of Germany. This does not affect any mandatory consumer-protection rights you '
                      'have under the law of your country of habitual residence (for example, as an EU member state). '
                      "Otherwise, disputes are subject to the jurisdiction of the courts responsible for the Company's "
                      'registered location (Dortmund, Germany).</p>'),
                     ('Contact',
                      '<p>For any question about these Terms, please reach out.</p>\n'
                      '<div class="contact-card"><span class="role">Operator</span><span class="name">Vicino '
                      'Labs</span><a href="mailto:contact@vicinolabs.com">contact@vicinolabs.com</a></div>')]},
 'de': {'title': 'Nomio Nutzungsbedingungen',
        'h1': 'Nutzungsbedingungen',
        'meta': [('Stand', '01.10.2026'), ('Version', '4.0'), ('Betreiber', 'Vicino Labs')],
        'lede': 'Diese Nutzungsbedingungen regeln die Vereinbarung zwischen Ihnen und uns über die Nutzung von Nomio, '
                'einer Haushaltsbuch-App für mehrere Währungen von Vicino Labs. Mit der Installation und Nutzung der '
                'App erklären Sie sich mit den folgenden Bestimmungen einverstanden.',
        'footer': 'Diese Bedingungen gelten ab dem 1. Oktober 2026 (Version 4.0).',
        'other': 'Zur Datenschutzerklärung →',
        'sections': [('Gegenstand',
                      '<p>Diese Nutzungsbedingungen regeln die Rechte, Pflichten und Verantwortlichkeiten zwischen '
                      'Vicino Labs ("wir", "das Unternehmen") und den Nutzern der mobilen Anwendung Nomio ("die '
                      'App").</p>'),
                     ('Begriffsbestimmungen',
                      '<ol>\n'
                      '<li><strong>"App"</strong> bezeichnet Nomio, eine vom Unternehmen entwickelte persönliche '
                      'Haushaltsbuch-Anwendung für mehrere Währungen.</li>\n'
                      '<li><strong>"Nutzer"</strong> bezeichnet jede Person, die die App gemäß diesen Bedingungen '
                      'installiert und nutzt.</li>\n'
                      '<li><strong>"Inhalte"</strong> bezeichnet die Bildschirme, Logos, das Design und den Quellcode '
                      'der App.</li>\n'
                      '</ol>'),
                     ('Anbieter',
                      '<div class="id-card"><dt>Firma</dt><dd>Vicino Labs '
                      '(Einzelunternehmen)</dd><dt>Inhaber</dt><dd>Jeong-Hwan Lee</dd><dt>Anschrift</dt><dd>Ruhrallee '
                      '41, 44139 Dortmund, Deutschland</dd><dt>E-Mail</dt><dd><a '
                      'href="mailto:contact@vicinolabs.com">contact@vicinolabs.com</a></dd><dt>Impressum</dt><dd><a '
                      'href="/impressum/">vicinolabs.com/impressum</a></dd></div>'),
                     ('Geltung und Änderung dieser Bedingungen',
                      '<ol>\n'
                      '<li>Diese Bedingungen gelten, sobald sie in der App oder auf andere von uns bestimmte Weise '
                      'veröffentlicht wurden.</li>\n'
                      '<li>Wir können diese Bedingungen im Rahmen des geltenden Rechts ändern und kündigen dabei '
                      'Geltungsdatum und Änderungsgrund im Voraus an.</li>\n'
                      '<li>Stimmen Sie geänderten Bedingungen nicht zu, können Sie die Nutzung beenden und die App '
                      'löschen. Nutzen Sie die App nach Bekanntgabe der geänderten Bedingungen weiter, gelten diese '
                      'als angenommen.</li>\n'
                      '</ol>'),
                     ('Leistungsumfang',
                      '<p>Die App bietet:</p>\n'
                      '<ol>\n'
                      '<li>Erfassung von Ausgaben, Einnahmen, Konten und Vermögenswerten mit Währungsumrechnung, '
                      'Budgetverwaltung, wiederkehrenden Buchungen sowie Statistik-/Trendansichten</li>\n'
                      '<li>Belegfotos mit Betragserkennung, Suche/Filterung von Buchungen sowie '
                      'CSV-/JSON-Backup-Export/-Import</li>\n'
                      '<li>Optionales Backup/Wiederherstellen über Google Drive</li>\n'
                      '<li>App-Sperre (Biometrie) sowie Hinweise in der App bei Budgetüberschreitung und '
                      'wiederkehrenden Buchungen</li>\n'
                      '<li>Mehrsprachigkeit und Anzeigeeinstellungen einschließlich Dunkelmodus und Designfarben</li>\n'
                      '<li>Premium (keine Werbung plus Zusatzfunktionen) als In-App-Kauf</li>\n'
                      '</ol>'),
                     ('Nutzungshinweise',
                      '<ol>\n'
                      '<li>Die App ist ein Werkzeug zur Erfassung eigener Einnahmen und Ausgaben. Sie <strong>erbringt '
                      'keine Anlage-, Steuer- oder Finanzberatung</strong>, und nichts darin ist als Empfehlung für '
                      'eine finanzielle Entscheidung zu verstehen.</li>\n'
                      '<li>Wechselkursdaten dienen nur der Orientierung, können vom tatsächlichen Kurs zum Zeitpunkt '
                      'einer Transaktion abweichen, und ihre Richtigkeit wird nicht garantiert.</li>\n'
                      '<li>Ihre Finanzdaten werden standardmäßig nur auf Ihrem Gerät gespeichert. Sie entscheiden '
                      'selbst über Art und Umfang einer Sicherung und tragen die Verantwortung für einen Datenverlust '
                      'durch Geräteverlust, Löschen der App oder ein Zurücksetzen.</li>\n'
                      '</ol>'),
                     ('Geistiges Eigentum',
                      '<p>Sämtliche Urheber- und Schutzrechte an Logo, Marken (einschließlich des Namens und Emblems '
                      '"Nomio"), Design, Texten und Quellcode der App stehen dem Unternehmen zu. Nutzer dürfen diese '
                      'ohne vorherige schriftliche Zustimmung des Unternehmens weder vervielfältigen, verbreiten, '
                      'übermitteln, veröffentlichen, zurückentwickeln noch daraus abgeleitete Werke erstellen oder '
                      'Dritten eine entsprechende Nutzung ermöglichen.</p>'),
                     ('Pflichten der Nutzer',
                      '<p>Nutzer dürfen die App nicht:</p>\n'
                      '<ol>\n'
                      '<li>zurückentwickeln (Reverse Engineering), dekompilieren oder deren Quellcode '
                      'extrahieren</li>\n'
                      '<li>in ihrem normalen Betrieb stören oder die Nutzung durch andere beeinträchtigen</li>\n'
                      '<li>unter Verstoß gegen geltendes Recht oder diese Bedingungen nutzen</li>\n'
                      '</ol>'),
                     ('Kostenpflichtige Leistungen (Premium) und Zahlung',
                      '<ol>\n'
                      '<li>Die App ist standardmäßig kostenlos nutzbar; die kostenlose Version zeigt über Google AdMob '
                      'ausgespielte Werbung.</li>\n'
                      '<li>Sie können <strong>Premium als einmaligen</strong> In-App-Kauf erwerben. Premium entfernt '
                      'die Werbung und schaltet PDF-Monatsberichte, Sparziele, Budget-Übertrag, zusätzliche '
                      'Widget-Stile sowie unbegrenzte Konten, Kategorien und wiederkehrende Buchungen frei. Es handelt '
                      'sich nicht um ein Abonnement, sodass keine Kündigung erforderlich ist.</li>\n'
                      '<li>Der Preis richtet sich nach dem im jeweiligen Store (Google Play/Apple App Store) '
                      'angezeigten Betrag; die Zahlung wird über diesen Store abgewickelt.</li>\n'
                      '<li>Erstattungen richten sich nach den Richtlinien und Verfahren des Stores, über den die '
                      'Zahlung erfolgt ist; wir wickeln Erstattungen nicht selbst ab. Bei einem Gerätewechsel stellen '
                      'Sie den Kauf über „Kauf wiederherstellen“ mit demselben Store-Konto wieder her.</li>\n'
                      '<li>Bei digitalen Inhalten erlischt das Widerrufsrecht, wenn mit der Ausführung begonnen wurde, '
                      'nachdem Sie ausdrücklich zugestimmt und bestätigt haben, dass Sie dadurch Ihr Widerrufsrecht '
                      'verlieren (§ 356 Abs. 5 BGB).</li>\n'
                      '</ol>'),
                     ('Werbung',
                      '<ol>\n'
                      '<li>Die kostenlose Version enthält über Google AdMob ausgespielte Werbung. Einzelheiten zur '
                      'Verarbeitung werbebezogener Daten finden Sie in unserer Datenschutzerklärung.</li>\n'
                      '<li>Der Inhalt der Werbung wird von Google und dessen Werbetreibenden bestimmt; wir '
                      'kontrollieren einzelne Anzeigen nicht im Voraus und übernehmen keine Verantwortung für über sie '
                      'beworbene Produkte oder Dienstleistungen Dritter.</li>\n'
                      '</ol>'),
                     ('Änderung, Aussetzung und Einstellung des Dienstes',
                      '<ol>\n'
                      '<li>Wir können aus betrieblichen oder technischen Gründen den Dienst ganz oder teilweise ändern '
                      'oder einstellen.</li>\n'
                      '<li>Außer in dringenden Fällen (Sicherheit, Rechtsvorgaben usw.) kündigen wir eine Einstellung '
                      'des Dienstes vorab an.</li>\n'
                      '</ol>'),
                     ('Haftungsausschluss',
                      '<ol>\n'
                      '<li>Die App wird <strong>"wie besehen" (AS-IS)</strong> bereitgestellt; wir übernehmen keine '
                      'Gewähr für die Vollständigkeit, Richtigkeit oder Aktualität von Wechselkursdaten, Berechnungen '
                      'oder anderen von der App bereitgestellten Informationen.</li>\n'
                      '<li>Außer bei Vorsatz oder grober Fahrlässigkeit haften wir nicht für das Ergebnis Ihrer '
                      'finanziellen Entscheidungen, für Datenverlust durch Gerätefehler, Datenbeschädigung oder '
                      'unterlassene Sicherung, oder für Einschränkungen des Dienstes infolge eines Ausfalls oder einer '
                      'Richtlinienänderung bei einem Drittdienst (Wechselkurs-API, Google Drive, Google AdMob '
                      'usw.).</li>\n'
                      '<li>Wir haften nicht, wenn wir den Dienst aufgrund höherer Gewalt, Stromausfalls, eines dem '
                      'Nutzer zuzurechnenden Grundes oder anderer Umstände außerhalb unseres üblichen Einflussbereichs '
                      'nicht erbringen können.</li>\n'
                      '<li>Im gesetzlich zulässigen Umfang ist unsere Haftung auf den vom Nutzer tatsächlich gezahlten '
                      'Betrag begrenzt (bei kostenloser Nutzung: null Euro).</li>\n'
                      '</ol>'),
                     ('Anwendbares Recht und Gerichtsstand',
                      '<p>Diese Bedingungen und etwaige Streitigkeiten zwischen dem Unternehmen und einem Nutzer '
                      'unterliegen dem Recht der Bundesrepublik Deutschland. Zwingende verbraucherschützende '
                      'Vorschriften des Staates, in dem der Nutzer als Verbraucher seinen gewöhnlichen Aufenthalt hat '
                      '(z. B. eines EU-Mitgliedstaats), bleiben hiervon unberührt. Im Übrigen ist Gerichtsstand für '
                      'Streitigkeiten der Sitz des Unternehmens (Dortmund, Deutschland).</p>'),
                     ('Kontakt',
                      '<p>Bei Fragen zu diesen Bedingungen wenden Sie sich bitte an:</p>\n'
                      '<div class="contact-card"><span class="role">Betreiber</span><span class="name">Vicino '
                      'Labs</span><a href="mailto:contact@vicinolabs.com">contact@vicinolabs.com</a></div>')]}}
