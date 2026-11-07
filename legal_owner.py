"""Keep the owner's name and address out of the top of legal pages.

The user's wish (2026-11-07, as on welegato.com/legal): the early
"controller"/"provider" section only points to the end of the document and
the Impressum; the full card (trading name, owner, address, email) sits in
the last section, "Contact", instead of the short contact card.
"""

import re

_CARD = re.compile(r'<div class="id-card">.*?</div>', re.S)
_CONTACT = re.compile(r'<div class="contact-card">.*?</div>', re.S)

OP_REF = {
    "ko": '운영자의 주소와 연락처는 <a href="#ko-{n}">이 문서 맨 아래</a>와 <a href="/impressum/">Impressum</a>에 있습니다.',
    "en": 'The operator\'s address and contact details are at <a href="#en-{n}">the end of this document</a> and in the <a href="/impressum/">Impressum</a>.',
    "de": 'Anschrift und Kontaktdaten des Anbieters finden Sie <a href="#de-{n}">am Ende dieses Dokuments</a> und im <a href="/impressum/">Impressum</a>.',
    "it": 'Indirizzo e contatti del gestore si trovano <a href="#it-{n}">alla fine di questo documento</a> e nell\'<a href="/impressum/">Impressum</a>.',
}


def op_ref(lang, n):
    return f'<p class="op-ref">{OP_REF[lang].format(n=n)}</p>'


def card_to_end(docs):
    """Move each language's id card from its early section into the last one."""
    for lang, d in docs.items():
        secs = list(d["sections"])
        last = len(secs) - 1
        for i, (title, body) in enumerate(secs[:last]):
            m = _CARD.search(body)
            if not m:
                continue
            card = m.group(0)
            secs[i] = (title, body[:m.start()] + op_ref(lang, last + 1) + body[m.end():])
            t, b = secs[last]
            b, k = _CONTACT.subn(lambda _: card, b, count=1)
            secs[last] = (t, b if k else b + card)
            break
        d["sections"] = secs
    return docs
