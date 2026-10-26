from common import *

QA = [("I've never touched a sewing machine. Can I join?", "Yes.", "The course starts with taking measurements and machine practice on industrial machines, before any garment. <span class='ph'>confirm: beginners welcome</span>"),
      ("Do I need my own machine?", "No", "You practise on the studio's industrial machines. <span class='ph'>confirm</span>"),
      ("Which language is it taught in?", "<span class='ph'>?</span>", "<span class='ph'>Kannada / Hindi / English, confirm</span>"),
      ("What are the timings?", "<span class='ph'>?</span>", "<span class='ph'>morning and evening batches? confirm</span> Timings for college students and working women."),
      ("What are the fees? Can I pay in instalments?", "<span class='ph'>₹ ?</span>", "<span class='ph'>fee for each course and whether instalments are allowed</span>"),
      ("Do I get a certificate?", "<span class='ph'>?</span>", "<span class='ph'>confirm</span>"),
      ("Can I start a boutique after this?", "Yes", "The 6-month course includes boutique management, branding and marketing, and a fabric and local-market visit.")]

CSS = """
.ob{padding:30px 28px;display:grid;gap:10px}
.chit{background:#fbfaf6;border:1px solid #cfc9bc;position:relative;padding-left:22px}
.chit::before{content:"";position:absolute;left:8px;top:0;bottom:0;width:0;border-left:2px dotted #b8b2a5}
.chit button{all:unset;cursor:pointer;display:grid;grid-template-columns:86px 1fr 24px;gap:12px;align-items:baseline;padding:14px 14px 14px 4px;width:calc(100% - 18px)}
.chit button:focus-visible{outline:2px solid var(--ink)}
.chit .no{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;color:#b0472f}
.chit .q{font-family:var(--serif);font-size:21px;line-height:1.15}
.chit .pm{font-family:var(--mono);font-size:16px;transition:transform .3s;text-align:right}
.chit button[aria-expanded="true"] .pm{transform:rotate(45deg)}
.chit .a{display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s}
.chit .a>div{overflow:hidden}
.chit .a p{margin:0;padding:0 14px 16px 102px;font-size:14px;line-height:1.5;background:repeating-linear-gradient(180deg,transparent 0 23px,#dfe5ec 23px 24px)}
.chit.open .a{grid-template-rows:1fr}
.chit.ask{border-style:dashed;background:transparent}
@container (max-width:560px){.chit button{grid-template-columns:1fr 24px}.chit .no{grid-column:1/-1}.chit .a p{padding-left:4px}}

.mgrid{padding:30px 28px}
.mgrid table{width:100%;border-collapse:collapse}
.mgrid th{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--pencil);font-weight:400;text-align:left;padding:8px;border-bottom:1.5px solid var(--ink)}
.mgrid td{padding:12px 8px;border-bottom:1px solid var(--rule);vertical-align:top;font-size:14px}
.mgrid td:first-child{font-family:var(--serif);font-size:19px;line-height:1.15;width:55%}
.mgrid td:nth-child(2){font-family:var(--mono);font-size:13px;white-space:nowrap}
.mgrid details summary{cursor:pointer;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}
.mgrid details p{margin:6px 0 0}

.board2{padding:34px 24px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px;background-color:#e9e5db}
.slip{background:#f6f1e4;border:1px solid #d7cfbd;padding:22px 14px 14px;position:relative;cursor:pointer;transform:rotate(var(--r));transition:transform .3s;
  clip-path:polygon(0 3%,8% 0,30% 2%,55% 0,80% 3%,100% 0,98% 30%,100% 60%,97% 100%,60% 98%,30% 100%,4% 97%,2% 60%,0 30%)}
.slip:hover{transform:rotate(0) scale(1.02)}
.slip i{position:absolute;top:7px;left:50%;width:10px;height:10px;border-radius:50%;background:#b0472f;transform:translateX(-50%);box-shadow:0 1px 0 rgba(0,0,0,.3)}
.slip b{font-family:var(--serif);font-weight:400;font-size:19px;line-height:1.15;display:block}
.slip p{margin:0;font-size:13px;max-height:0;overflow:hidden;transition:max-height .4s,margin .4s}
.slip.open p{max-height:160px;margin-top:8px}
@container (max-width:600px){.board2{grid-template-columns:1fr 1fr}}

.askc{padding:34px 28px;display:flex;justify-content:center}
.blank{width:min(560px,100%);background:#fbfaf6;border:1.5px dashed var(--ink);padding:22px;display:grid;gap:12px}
.blank label{font-family:var(--serif);font-size:26px;line-height:1.1}
.blank textarea{font:inherit;font-size:15px;border:0;border-bottom:1px solid var(--ink);background:repeating-linear-gradient(180deg,transparent 0 27px,#dfe5ec 27px 28px);resize:vertical;min-height:84px;line-height:28px;padding:0 2px;color:var(--ink)}
.blank textarea:focus{outline:none;border-bottom-width:2px}
.msg{background:#e6f2df;border-radius:10px 10px 10px 2px;padding:12px 14px;font-size:14px;line-height:1.45;color:#1d2b17}
.msg small{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#4d6343;margin-bottom:4px}
"""

def chits(items, start=127):
    h = ""
    for i, (q, s, a) in enumerate(items):
        h += f'<div class="chit"><button type="button" aria-expanded="false" id="q{i}"><span class="no">No. 0{start + i}</span><span class="q">{q}</span><span class="pm">+</span></button><div class="a" role="region" aria-labelledby="q{i}"><div><p>{a}</p></div></div></div>'
    return h

A = f'<div class="ob"><span class="eyebrow">Questions · Order book</span>{chits(QA[:5])}<div class="chit ask"><button type="button" aria-expanded="false"><span class="no">No. 0___</span><span class="q">Your question isn\'t here? Ask Shruti on WhatsApp.</span><span class="pm">→</span></button></div></div>'

rows = "".join(f'<tr><td>{q}</td><td>{s}</td><td><details><summary>more</summary><p>{a}</p></details></td></tr>' for q, s, a in QA)
B = f'<div class="mgrid"><table><thead><tr><th>Question</th><th>Short</th><th>Detail</th></tr></thead><tbody>{rows}</tbody></table></div>'

rots = [-3, 2, -1.5, 3, -2, 1.5]
C = '<div class="board2">' + "".join(f'<div class="slip" style="--r:{rots[i]}deg" tabindex="0" role="button"><i></i><b>{q}</b><p>{a}</p></div>' for i, (q, s, a) in enumerate(QA[:6])) + "</div>"

D = """<div class="askc"><div class="blank"><span class="eyebrow">No. 0___ · blank chit</span>
<label for="askq">Your question isn't here?</label>
<textarea id="askq" placeholder="Write it here…">Can I join if I can only come on weekends?</textarea>
<div class="msg"><small>Your WhatsApp message</small><span id="askOut"></span></div>
<span class="btn" style="justify-self:start">Ask Shruti on WhatsApp</span></div></div>"""

body = "".join([
    option("A", "Tailor's order book", A,
           "A carbon-copy order book with a perforated edge. Each question is a numbered chit; tap to slide out the answer on ruled paper. The last chit is blank and opens WhatsApp.",
           "The most recognisable local object, and it's a proper accessible accordion underneath (buttons with aria-expanded, several open at once).",
           "Full-width chits; the number moves above the question.",
           [("One Page Love: Shelf FAQ accordion", "https://onepagelove.com/section/faq-accordion/shelf"), ("One Page Love: FAQ collection", "https://onepagelove.com/tag/faq"),
            ("NN/g: accordions on desktop", "https://www.nngroup.com/articles/accordions-on-desktop/")],
           rec=True, original=True),
    option("B", "Measurement-chart grid", B,
           "A measurement chart where each row is a question and the short answer is visible without clicking (\"Machine needed? No\"). Longer answers expand.",
           "The short answers never hide, which is NN/g's main rule for FAQs.",
           "Question and short answer stay; Detail drops under the row.",
           [("One Page Love: Pairio FAQ grid", "https://onepagelove.com/section/faq-grid/pairio"), ("NN/g: accordions on mobile", "https://www.nngroup.com/videos/accordions-on-mobile/")],
           runner=True),
    option("C", "Pinned pattern slips", C,
           "Questions written on torn scraps of pattern paper pinned to a board. Tap a slip to unfold the answer.",
           "The most playful of the four.",
           "Harder to scan, so only for 5-6 questions; two per row.",
           [("No precedent found; pinned-note boards are the nearest", "https://onepagelove.com/tag/faq")],
           original=True),
    option("D", "\"Ask Shruti\" blank chit", D,
           "A blank order chit: type your question and it becomes a WhatsApp message to Shruti. Best used as the last item of A.",
           "Turns leftover doubt into an enquiry.",
           "Works as is.",
           [("Bird: WhatsApp click-to-chat with prefilled text", "https://bird.com/explained/whatsapp/what-is-a-whatsapp-click-to-chat-link")]),
])
body += """<div class="aside"><h3>SEO note</h3><p>Google stopped showing FAQ rich results in May 2026, so FAQ markup adds nothing. The questions still matter as visible text, because people search exactly these phrases. Fees, duration and timings must also appear in the Courses section, never only inside the FAQ.</p></div>"""

JS = """
document.querySelectorAll('.chit').forEach(c=>{const b=c.querySelector('button');if(!c.querySelector('.a'))return;
 b.addEventListener('click',()=>{const o=c.classList.toggle('open');b.setAttribute('aria-expanded',o)})});
document.querySelector('.chit')?.querySelector('button').click();
document.querySelectorAll('.slip').forEach(s=>{const f=()=>s.classList.toggle('open');s.addEventListener('click',f);s.addEventListener('keydown',e=>{if(e.key==='Enter')f()})});
const ta=document.getElementById('askq'),ao=document.getElementById('askOut');const u=()=>ao.textContent='Hi Shruti, '+(ta.value.trim()||'…');ta.addEventListener('input',u);u();
"""
page("faq.html", "FAQ Options", "08 / 09", "FAQ",
     "The questions a beginner in Hubballi actually asks before joining. Answers come from the PDFs where they exist; orange tags are facts only Shruti can give us.",
     body, CSS, JS)
