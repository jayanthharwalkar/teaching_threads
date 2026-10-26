from common import *

PATHS = [("Open your own boutique", "Boutique management + branding modules (6-month)."),
         ("Stitch from home", "Take blouse and kurta orders from your neighbourhood."),
         ("Blouse &amp; bridal specialist", "8 blouse types, lehenga, Aari work."),
         ("Alterations service", "Fast, steady local income."),
         ("Aari &amp; embroidery work", "Pearl, beads, zardozi, thread work (6-month)."),
         ("Go on to a design degree", "A portfolio of real garments for NIFT-style entrance.")]

CSS = """
.railwrap{padding:34px 0 28px;display:grid;gap:18px}
.railwrap .hd{padding:0 28px}
.rail{position:relative;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 28px 14px}
.rail .bar{position:absolute;left:0;right:0;top:12px;height:4px;background:var(--ink);border-radius:2px;min-width:1200px}
.rail .row{display:flex;gap:22px;width:max-content;padding-top:4px}
.hanger{width:170px;scroll-snap-align:start;display:flex;flex-direction:column;align-items:center;cursor:pointer;flex:none}
.hanger svg{width:120px;height:62px;stroke:var(--ink);fill:none;stroke-width:2}
.htag{width:150px;min-height:150px;perspective:800px;margin-top:-4px}
.htag .in{position:relative;width:100%;height:150px;transition:transform .6s;transform-style:preserve-3d;transform-origin:50% 0;animation:sway 5s ease-in-out infinite}
.hanger:nth-child(even) .htag .in{animation-delay:-2.5s}
.hanger.flip .htag .in{transform:rotateY(180deg)}
.htag .f{position:absolute;inset:0;backface-visibility:hidden;background:#ece5d6;border:1px solid #c9bfa9;border-radius:4px;padding:14px 12px;display:flex;flex-direction:column;gap:6px}
.htag .b{transform:rotateY(180deg);background:#fbfaf6}
.htag .f .t{font-family:var(--serif);font-size:23px;line-height:1}
.htag .f p{margin:0;font-size:12px;line-height:1.35}
@keyframes sway{0%,100%{rotate:-1.5deg}50%{rotate:1.5deg}}

.pieces{display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:30px 28px;align-items:center;min-height:440px}
.pieces svg{width:100%;height:auto;max-height:380px}
.pieces .pc{fill:#fbfaf6;stroke:var(--ink);stroke-width:1.4;transition:transform 1.1s cubic-bezier(.6,0,.2,1)}
.pieces .lbl{font-family:var(--mono);font-size:9px;letter-spacing:.1em;fill:var(--ink);transition:opacity .4s}
.pieces .notch{stroke:var(--ink);stroke-dasharray:4 3;fill:none}
.pieces:not(.go) .p1{transform:translate(-60px,-40px) rotate(-12deg)}
.pieces:not(.go) .p2{transform:translate(70px,-30px) rotate(10deg)}
.pieces:not(.go) .p3{transform:translate(-70px,70px) rotate(14deg)}
.pieces:not(.go) .p4{transform:translate(80px,80px) rotate(-16deg)}
.pieces .then{opacity:0;transition:opacity .6s .9s;display:grid;gap:8px}
.pieces.go .then{opacity:1}
.pieces.go .lbl{opacity:0}
.pieces ul{margin:0;padding:0;list-style:none;display:grid;gap:6px}
.pieces li{font-family:var(--serif);font-size:24px;line-height:1.1;border-bottom:1px solid var(--rule);padding-bottom:6px}
@container (max-width:600px){.pieces{grid-template-columns:1fr}}

.sign{padding:36px 28px;display:grid;gap:26px}
.board{background:#1d1c1a;color:#f5f1e6;border-radius:4px;padding:26px 28px;border:6px solid #3a3733;box-shadow:inset 0 0 0 1px #57534c;display:grid;gap:6px;text-align:center}
.board .name{font-family:var(--serif);font-size:clamp(38px,7.4cqi,72px);line-height:1;min-height:1em}
.board .name .cur{display:inline-block;width:3px;height:.8em;background:#f5f1e6;margin-left:4px;vertical-align:-2px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.board .en{font-family:var(--mono);font-size:12px;letter-spacing:.2em;text-transform:uppercase}
.board .kn{font-family:var(--kn);font-size:20px;font-weight:600;letter-spacing:.02em}
.cards3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.cards3 div{border-top:1.5px solid var(--ink);padding-top:10px}
.cards3 b{font-family:var(--serif);font-weight:400;font-size:23px;display:block;line-height:1.05}
.cards3 p{margin:4px 0 0;font-size:12.5px;color:#4a4843}
@container (max-width:560px){.cards3{grid-template-columns:1fr}}

.ledger{padding:36px 28px;display:flex;justify-content:center}
.book{width:min(620px,100%);background:#fbfaf6;border:1px solid #cfc9bc;padding:22px 24px;background-image:repeating-linear-gradient(180deg,transparent 0 31px,#cfd8e3 31px 32px);background-position:0 54px}
.book h6{margin:0 0 18px;font-family:var(--serif);font-weight:400;font-size:28px;line-height:1}
.book .r{display:grid;grid-template-columns:40px 1fr 110px;height:32px;align-items:end;font-family:var(--hand);font-size:22px;border-left:1px solid #e2a7a0}
.book .r span:first-child{font-family:var(--mono);font-size:10px;padding-left:6px;color:var(--pencil)}
.book .r span:last-child{font-family:var(--mono);font-size:13px}
"""

hanger_svg = '<svg viewBox="0 0 120 62"><path d="M60 4 q8 0 8 7 q0 6 -8 9 v6 L8 56 h104 L60 26"/></svg>'
A = '<div class="railwrap"><div class="hd"><span class="eyebrow">After the course</span><p class="h2">Pick a path off the rail.</p></div><div class="rail"><div class="bar"></div><div class="row">'
for t, p in PATHS:
    A += f'<div class="hanger" tabindex="0" role="button">{hanger_svg}<div class="htag"><div class="in"><div class="f"><span class="mono" style="font-size:9px">Path</span><span class="t">{t}</span><span class="mono" style="font-size:9px;margin-top:auto;color:#6b6150">tap ↻</span></div><div class="f b"><span class="mono" style="font-size:9px">What you need next</span><p>{p}</p></div></div></div></div>'
A += "</div></div></div>"

B = """<div class="pieces" id="pieces">
<svg viewBox="0 0 300 300" aria-hidden="true">
 <g class="pc p1"><path d="M70 60 L130 50 L140 150 L60 150 Z"/><text class="lbl" x="72" y="105">MEASURE</text></g>
 <g class="pc p2"><path d="M150 50 L210 60 L220 150 L140 150 Z"/><text class="lbl" x="160" y="105">DRAFT</text></g>
 <g class="pc p3"><path d="M60 150 L140 150 L135 240 L70 240 Z"/><text class="lbl" x="74" y="200">STITCH</text></g>
 <g class="pc p4"><path d="M140 150 L220 150 L210 240 L145 240 Z"/><text class="lbl" x="152" y="200">FINISH</text></g>
 <path class="notch" d="M100 52 Q140 90 180 52"/>
</svg>
<div><span class="eyebrow">Skills, assembled</span><p class="h2" style="margin:8px 0 14px">Four skills. One garment.</p>
<div class="then"><span class="mono">…and now you can</span><ul><li>Open your own boutique</li><li>Stitch orders from home</li><li>Specialise in bridal blouses</li></ul></div>
<button class="btn ghost" id="assemble" type="button" style="margin-top:14px">Assemble</button></div></div>"""

C = """<div class="sign"><span class="eyebrow">After the course</span>
<div class="board"><div class="name"><span id="tw"></span><span class="cur"></span></div>
<div class="en">Boutique · Ladies tailoring · Blouse specialist</div>
<div class="kn">ಲೇಡೀಸ್ ಟೈಲರಿಂಗ್ · ಬ್ಲೌಸ್ ಸ್ಪೆಷಲಿಸ್ಟ್</div></div>
<div class="cards3"><div><b>Open your own boutique</b><p>The 6-month course includes boutique management, branding and a local market visit.</p></div>
<div><b>Stitch from home</b><p>Blouse and kurta orders from your street, on your hours.</p></div>
<div><b>Go further</b><p>Aari specialist, alterations, or on to a design degree with a real portfolio.</p></div></div>
<span class="ph" style="justify-self:start">Kannada line to be checked by a native speaker</span></div>"""

D = """<div class="ledger"><div class="book"><h6>Your first orders</h6>
<div class="r"><span>01</span><span>Princess-cut blouse, padded</span><span>₹ ____</span></div>
<div class="r"><span>02</span><span>Kurti alteration</span><span>₹ ____</span></div>
<div class="r"><span>03</span><span>Umbrella-flare lehenga</span><span>₹ ____</span></div>
<div class="r"><span>04</span><span>Boat-neck blouse</span><span>₹ ____</span></div>
<div class="r"><span>05</span><span>Aari work, sleeves</span><span>₹ ____</span></div>
<div style="margin-top:14px"><span class="ph">only with real local rates from Shruti; never invent them</span></div></div></div>"""

body = "".join([
    option("A", "Clothes rail of paths", A,
           "Six clay hangers on a black rail, each with a swing tag naming a real local career. Tap a tag to flip it and see what you'd need next.",
           "Turns a list of careers into a physical object. Honest content, no made-up numbers.",
           "A horizontal snap scroller, one hanger at a time.",
           [("Polimoda: career-path filter", "https://www.polimoda.com/courses"), ("Pearl Academy: careers list", "https://pearlacademy.com/programs/certificate-courses/fashion/fashion-design-womenswear")],
           runner=True, original=True),
    option("B", "Pattern pieces assemble", B,
           "Four blouse pattern pieces labelled Measure, Draft, Stitch, Finish float apart, then slide together into one garment, revealing what you can do now. Press Assemble.",
           "Shows skills combining into a livelihood, and reuses the stage vocabulary from the course section.",
           "Shorter scroll pin, or just show the assembled still.",
           [("Codrops: SVG shapes on scroll", "https://tympanus.net/codrops/2022/06/08/how-to-animate-svg-shapes-on-scroll/"), ("Framer: Scroll Stack", "https://www.framer.com/marketplace/components/scroll-stack/")]),
    option("C", "Shop-front signboard", C,
           "A painted Hubballi shop board: \"____ Boutique · Ladies tailoring · Blouse specialist\", with the blank typing out different names. A Kannada line underneath, like real signboards. Three path cards below.",
           "Aspirational and very local: the real outcome for most students is their own shop. Karnataka signboards are bilingual by law, so the Kannada line feels native.",
           "Works as is.",
           [("Yellowslice: Kannada signage", "https://yellowslice.in/bed/?p=11115"), ("Parsons: Maya Eapen, Bangalore display lettering", "https://bfacd.parsons.edu/2021/maya-eapen")],
           rec=True, original=True),
    option("D", "First-orders ledger", D,
           "An order-book page of \"your first orders\": blouse, alteration, lehenga, each with a price.",
           "Makes earning potential concrete.",
           "Works as is.",
           [("No precedent found; based on real tailor order books", "https://en.wikipedia.org/wiki/Tailor")],
           original=True),
])
body += """<div class="aside"><h3>The rule here</h3><p>No placement percentages or salary claims. Big schools quote them (Marangoni: "91% find work within a year"); we don't have the data, so every option names paths, not numbers.</p></div>"""

JS = """
document.querySelectorAll('.hanger').forEach(h=>{const f=()=>h.classList.toggle('flip');h.addEventListener('click',f);h.addEventListener('keydown',e=>{if(e.key==='Enter'){f()}})});
const pc=document.getElementById('pieces');document.getElementById('assemble').addEventListener('click',e=>{pc.classList.toggle('go');e.target.textContent=pc.classList.contains('go')?'Take apart':'Assemble'});
const names=['Your name','Priya','Ananya','Lakshmi','Shreya','Your name'],tw=document.getElementById('tw');let ni=0,ci=0,del=false;
function step(){const n=names[ni]+' Boutique';if(!del){ci++;tw.textContent=n.slice(0,ci);if(ci===n.length){del=true;return setTimeout(step,1600)}}
 else{ci--;tw.textContent=n.slice(0,ci);if(ci===0){del=false;ni=(ni+1)%names.length}}setTimeout(step,del?45:90)}
if(matchMedia('(prefers-reduced-motion: reduce)').matches){tw.textContent='Your name Boutique'}else step();
"""
page("after.html", "After The Course Options", "06 / 09", "After the course",
     "What a student can do once they finish. No student stories or placement numbers yet, so these name real local paths: a boutique, stitching from home, bridal blouses, Aari work, alterations, further study.",
     body, CSS, JS)
