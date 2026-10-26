from common import *

CSS = """
.hero{display:grid;grid-template-columns:1.1fr .9fr;min-height:440px}
.hero .txt{padding:36px 32px;display:flex;flex-direction:column;gap:18px;justify-content:center;position:relative;z-index:2}
.hero .pic{position:relative;overflow:hidden;border-left:1px solid var(--rule)}
@container (max-width:620px){.hero{grid-template-columns:1fr}.hero .pic{height:300px;border-left:0;border-top:1px solid var(--rule)}.hero .txt{padding:26px 20px}}

/* A seam */
.seam{width:100%;max-width:440px;height:14px;display:block;animation:sew 5s ease-in-out infinite}
.seam path{stroke:var(--ink);stroke-width:2;stroke-dasharray:9 6;fill:none}
@keyframes sew{0%{clip-path:inset(0 100% 0 0)}45%,100%{clip-path:inset(0 0 0 0)}}
.stages{display:flex;flex-wrap:wrap;gap:4px 14px;list-style:none;margin:0;padding:0}
.stages li{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);animation:tick 5s infinite}
.stages li:nth-child(2){animation-delay:.25s}.stages li:nth-child(3){animation-delay:.5s}.stages li:nth-child(4){animation-delay:.75s}.stages li:nth-child(5){animation-delay:1s}
@keyframes tick{0%,20%{color:#bdb9b0}35%,100%{color:var(--ink)}}
.thread{position:absolute;left:-1px;top:62%;width:60%;height:2px;background:repeating-linear-gradient(90deg,var(--ink) 0 9px,transparent 9px 15px);animation:sew 5s ease-in-out infinite}
.scrubhint{position:absolute;right:12px;bottom:12px;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;background:var(--paper);padding:4px 7px;border:1px solid var(--rule)}

/* B kainchi */
.stage-b{position:relative;overflow:hidden;border-left:1px solid var(--rule)}
.stage-b .under{position:absolute;inset:0}
.paper{position:absolute;inset:0;background-color:#efede6;
  background-image:linear-gradient(#d9d5cb 1px,transparent 1px),linear-gradient(90deg,#d9d5cb 1px,transparent 1px);background-size:22px 22px;
  animation:lift 7s ease-in-out infinite;transform-origin:0 0}
.paper svg{position:absolute;inset:0;width:100%;height:100%}
.paper .cutline{stroke:var(--ink);stroke-width:1.6;stroke-dasharray:7 5;fill:none}
.paper .grain{font-family:var(--mono);font-size:9px;letter-spacing:.14em;fill:#6f6b62}
.scissor{position:absolute;left:0;top:0;font-size:26px;offset-path:path("M 30 300 C 120 120, 260 120, 360 40");offset-rotate:auto;animation:snip 7s ease-in-out infinite}
@keyframes snip{0%,8%{offset-distance:0%;opacity:1}45%{offset-distance:100%;opacity:1}50%,100%{offset-distance:100%;opacity:0}}
@keyframes lift{0%,48%{transform:none;opacity:1}62%,88%{transform:translate(-30%,-40%) rotate(-18deg);opacity:0}100%{transform:none;opacity:0}}
.replay{position:absolute;right:12px;bottom:12px;z-index:3}

/* C chalk */
.chalk{padding:36px 32px 32px;display:grid;gap:18px}
.chalk svg{width:100%;height:auto;display:block}
.chalk text{font-family:var(--serif);font-size:118px;letter-spacing:-1px;animation:chalk 6s ease-in-out infinite;fill:var(--ink);stroke:var(--ink);stroke-width:1.2}
@keyframes chalk{0%,15%{fill:transparent;stroke:#a7a296;stroke-dasharray:3 5;stroke-dashoffset:0}
 50%{fill:transparent;stroke:var(--ink);stroke-dasharray:3 5;stroke-dashoffset:-60}
 70%,100%{fill:var(--ink);stroke:var(--ink);stroke-dasharray:none}}
.chalk .row{display:flex;justify-content:space-between;align-items:end;gap:18px;flex-wrap:wrap}
@container (max-width:620px){.chalk{padding:24px 20px}}

/* D tape */
.tapewrap{display:grid;grid-template-columns:1fr 150px;min-height:470px}
.tape{position:relative;border-left:1px solid var(--rule);background:var(--paper);padding:16px 0}
.tape .band{position:absolute;left:40px;top:16px;bottom:16px;width:44px;background:#ebe7dc;border:1px solid #cfc9bc;
  background-image:repeating-linear-gradient(180deg,var(--ink) 0 1px,transparent 1px 8px),repeating-linear-gradient(180deg,var(--ink) 0 1px,transparent 1px 40px);
  background-size:12px 100%,24px 100%;background-repeat:no-repeat;background-position:0 0,0 0}
.tape .fill{position:absolute;left:40px;top:16px;width:44px;background:rgba(22,21,20,.12);height:0;transition:height .2s}
.tape .mark{position:absolute;left:92px;font-family:var(--mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:#bdb9b0;transform:translateY(-50%);transition:color .2s;line-height:1.2}
.tape .mark.on{color:var(--ink)}
.tape .mark.x{font-style:italic}
.tape .tip{position:absolute;left:28px;bottom:2px;width:68px;padding:7px 0;border-radius:3px;background:#a9a59b;color:#fff;font-size:10px;font-weight:700;text-align:center;letter-spacing:.04em}
.tapewrap .txt{padding:36px 32px;display:flex;flex-direction:column;gap:18px;justify-content:center}
.sim{display:flex;gap:10px;align-items:center;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}
.sim input{width:160px;accent-color:#161514}
@container (max-width:620px){.tapewrap{grid-template-columns:1fr 130px}.tapewrap .txt{padding:24px 16px}}

/* E lookbook */
.look .pic{background:var(--paper)}
.look .slide{position:absolute;inset:0;opacity:0;animation:cycle 12s infinite;display:flex;flex-direction:column}
.look .slide .frame{flex:1;min-height:0}
.look .slide figcaption{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;padding:10px 14px;border-top:1px solid var(--rule);background:var(--paper)}
.look .slide:nth-child(1){animation-delay:0s;opacity:1}.look .slide:nth-child(2){animation-delay:3s}.look .slide:nth-child(3){animation-delay:6s}.look .slide:nth-child(4){animation-delay:9s}
@keyframes cycle{0%{opacity:0}4%,25%{opacity:1}29%,100%{opacity:0}}
.wapill{position:absolute;right:14px;bottom:14px;z-index:4;background:var(--ink);color:var(--paper);font-size:12px;font-weight:600;padding:9px 13px;border-radius:999px}
.copybank{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.copybank div{background:var(--paper);color:var(--ink);border:1px solid var(--line);padding:18px;font-family:var(--serif);font-size:24px;line-height:1.05}
.copybank small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil);margin-top:10px}
@media (max-width:720px){.copybank{grid-template-columns:1fr}}
"""

TEXT = """
<span class="eyebrow">Teaching Threads Fashion Academy · Hubballi (Hubli)</span>
<h3 class="h1">{{h1}}</h3>
{{extra}}
<p class="sub">3- and 6-month fashion design &amp; tailoring courses, taught by designer Shruti Mahajan on industrial machines.</p>
<div class="ctas"><span class="btn">Enquire on WhatsApp</span><span class="btn ghost">Book a studio visit</span></div>
"""

def text(h1, extra=""):
    return T(TEXT, h1=h1, extra=extra)

A = f"""
<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="hero">
  <div class="txt">{text("Learn to make<br>what you wear.", '<svg class="seam" viewBox="0 0 440 14" preserveAspectRatio="none"><path d="M0 7 H440"/></svg><ol class="stages"><li>01 Measure</li><li>02 Draft</li><li>03 Stitch</li><li>04 Blouse</li><li>05 Lehenga</li></ol>')}</div>
  <div class="pic"><img class="clay" src="{img('machine', 640)}" alt="Clay sewing machine POV"><div class="thread"></div><span class="scrubhint">frames scrub on scroll ↓</span></div>
</div>"""

B = f"""
<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="hero">
  <div class="txt">{text("Every garment<br>starts on paper.")}</div>
  <div class="stage-b" id="stageB">
    <div class="under"><img class="clay" src="{img('dressform', 640)}" alt="Clay dress form"></div>
    <div class="paper" id="paperB">
      <svg viewBox="0 0 400 440" preserveAspectRatio="xMidYMid slice">
        <path class="cutline" d="M 30 300 C 120 120, 260 120, 360 40"/>
        <text class="grain" x="40" y="380">3 MONTHS · 6 MONTHS · HUBBALLI STUDIO · BEGINNERS WELCOME</text>
        <text class="grain" x="40" y="400">CUT 1 ON FOLD  ←  GRAINLINE  →</text>
        <text class="grain" x="250" y="250">FRONT BODICE · TT-01</text>
      </svg>
      <span class="scissor">✂</span>
    </div>
    <button class="btn ghost replay" id="replayB" type="button">Replay cut</button>
  </div>
</div>"""

C = f"""
<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="chalk">
  <span class="eyebrow">Teaching Threads Fashion Academy · Hubballi (Hubli)</span>
  <svg viewBox="0 0 900 270" role="img" aria-label="Learn to make what you wear.">
    <text x="0" y="110">Learn to make</text>
    <text x="0" y="240" font-style="italic">what you wear.</text>
  </svg>
  <div class="row"><p class="sub">3- and 6-month fashion design &amp; tailoring courses, taught by designer Shruti Mahajan on industrial machines.</p>
  <div class="ctas"><span class="btn">Enquire on WhatsApp</span><span class="btn ghost">Book a studio visit</span></div></div>
</div>"""

D = f"""
<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="tapewrap">
  <div class="txt">{text("Every garment starts with a measurement.", '<label class="sim" for="tapeSim">Simulate scroll <input id="tapeSim" type="range" min="0" max="100" value="38"></label>')}</div>
  <div class="tape" id="tape">
    <div class="band"></div><div class="fill" id="tapeFill"></div>
    <span class="mark" data-at="4" style="top:6%">0″ Measure</span>
    <span class="mark" data-at="20" style="top:20%">10″ Draft</span>
    <span class="mark" data-at="34" style="top:34%">20″ Stitch</span>
    <span class="mark" data-at="48" style="top:48%">30″ Blouse</span>
    <span class="mark" data-at="62" style="top:62%">40″ Lehenga<br>◂ 3 months</span>
    <span class="mark x" data-at="74" style="top:74%">Aari work</span>
    <span class="mark x" data-at="84" style="top:84%">Boutique mgmt<br>◂ 6 months</span>
    <span class="tip">WhatsApp</span>
  </div>
</div>"""

E = f"""
<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="hero look">
  <div class="txt">{text("From the runway<br>to your first stitch.")}</div>
  <div class="pic">
    <figure class="slide" style="margin:0"><div class="frame duo grain"><img src="{img('cape', 640)}" alt="Forest Fury cape look"></div><figcaption>Forest Fury · Kerala Fashion League · 2016</figcaption></figure>
    <figure class="slide" style="margin:0"><div class="frame"><img class="clay" src="{img('measure', 640)}" alt="Clay hands measuring a dress form"></div><figcaption>Stage 01 · Measure</figcaption></figure>
    <figure class="slide" style="margin:0"><div class="frame duo grain"><img src="{img('floral', 640)}" alt="Floral gown look"></div><figcaption>Shruti Mahajan · runway work</figcaption></figure>
    <figure class="slide" style="margin:0"><div class="frame"><img class="clay" src="{img('lehenga', 640)}" alt="Clay lehenga with dori"></div><figcaption>Stage 05 · Lehenga</figcaption></figure>
    <span class="wapill">WhatsApp</span>
  </div>
</div>"""

body = "".join([
    option("A", "The Seam", A,
           "The clay sewing machine plays frame by frame as you scroll (the pipeline we already have). The thread leaving the needle becomes a dashed stitch that underlines the headline, then runs down the page into the five stages, ticking each one from grey to black.",
           "One signature motion, reusing what's built. The thread becomes the spine of the whole page, so the hero, the stages and the footer feel like one garment.",
           "Use a portrait Kling render, pinned for at most 2 screen-heights. Frame 0 is a normal &lt;img&gt; so the page loads fast. A WhatsApp pill sits bottom-right from the first second.",
           [("GreenSock image-sequence scrub", "https://codepen.io/GreenSock/pen/RwvrNqN"), ("Apple AirPods Pro", "https://www.apple.com/airpods-pro/"),
            ("Codrops: SVG shapes on scroll", "https://tympanus.net/codrops/2022/06/08/how-to-animate-svg-shapes-on-scroll/"), ("CSS-Tricks: SVG line drawing", "https://css-tricks.com/?p=163222")],
           rec=True),
    option("B", "Kainchi Cut", B,
           "The hero loads as a sheet of pattern paper: 1&nbsp;cm grid, grainline notes, a dashed cutting curve. The kainchi runs along the line, the piece lifts away, and the clay dress form is revealed underneath.",
           "The biggest 'wow' of the set, and it builds on the kainchi prototype already on this branch. The micro-type on the paper is real copy, so it still explains the offer.",
           "Plays once on load, never tied to scroll. People with reduced motion see the after-cut state.",
           [("Codrops: SVG clip-path text", "https://tympanus.net/codrops/2024/01/10/experimental-on-scroll-text-animations-with-svg-clip-path/"),
            ("Codrops: dynamic CSS masks", "https://tympanus.net/codrops/2021/05/04/dynamic-css-masks-with-custom-properties-and-gsap/"),
            ("Adobe forum: scissor removes dash marks", "https://community.adobe.com/t5/animate-discussions/simple-scissor-animation-removing-dash-marks-where-scissor-cuts/m-p/11049819/highlight/true")],
           runner=True),
    option("C", "Chalk to Stitch", C,
           "A giant two-line headline starts as broken tailor's-chalk outlines, then gets stitched over and filled with solid ink. Type only, no media.",
           "The lightest and fastest option, and the most typographic. It can also be layered on top of A as the headline treatment.",
           "Works best of all on phones because there is nothing to load. Keep the real &lt;h1&gt; in HTML under the SVG for Google.",
           [("Codrops: Ghost Trails (Oct 2026)", "https://tympanus.net/codrops/2026/10/13/scroll-driven-ghost-trails/"),
            ("Codrops: animated text fills", "https://tympanus.net/Tutorials/AnimatedTextFills/index.html"),
            ("Codrops: stagger text reveal", "https://tympanus.net/codrops/2020/06/17/making-stagger-reveal-animations-for-text/")]),
    option("D", "Inchi Tape", D,
           "A measuring tape runs down the right edge and fills as you scroll. Its inch marks are the five stages; the 3-month course ends at 40″, and the 6-month course keeps going into Aari work and boutique management. The metal end-tab is the WhatsApp button. Drag the slider to fake the scroll.",
           "The tape is the course timeline, so it explains 3 vs 6 months without a paragraph. It also works as the page's progress bar.",
           "The tape becomes a thin ruler on the right edge of the screen.",
           [("Codrops: Sticky Grid Scroll", "https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/"),
            ("Codrops: Layered Zoom scroll", "https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/"),
            ("thesuperrco.com (playful objects)", "https://thesuperrco.com/")],
           original=True),
    option("E", "Lookbook Split", E,
           "Headline and buttons pinned on the left. On the right, a stack alternates Shruti's inked runway looks with clay stage stills, each with a caption like a lookbook plate.",
           "Shows credibility and the course in one view. Of the five, it explains the offer most directly and uses the runway photos from second one.",
           "Stacks: headline, then a swipeable card row, then the buttons.",
           [("Awwwards: Martine Rose hero gallery", "https://www.awwwards.com/inspiration/hero-scroll-gallery-martine-rose"),
            ("Sabyasachi (headline over media)", "https://sabyasachi.com/"), ("Raw Mango (desktop/mobile crops)", "https://www.rawmango.com/")]),
])

body += """
<div class="aside"><h3>Headline bank</h3><p>Formula that works for course sites: outcome + honest timeframe + who's teaching or where. Mix and match with any option.</p></div>
<div class="copybank">
 <div>Learn to make what you wear.<small>Prototype line, warm</small></div>
 <div>From measuring tape to lehenga in 6 months.<small>Outcome + timeframe</small></div>
 <div>Learn fashion design from a fashion designer.<small>From Shruti's own PDF</small></div>
 <div>From the runway to your first stitch.<small>Credibility-led</small></div>
 <div>Measure. Draft. Stitch. Wear it.<small>Process, matches the stages</small></div>
 <div>Fashion designing &amp; tailoring courses in Hubballi.<small>SEO line, use as the real H1 or eyebrow</small></div>
</div>
<div class="aside"><h3>Rules every option keeps</h3><ul>
<li>Eyebrow, headline, one-line offer and both buttons are plain HTML, visible on load, never waiting on an animation.</li>
<li>Primary CTA: WhatsApp with a prefilled message ("Hi, I'm interested in the fashion design course"). Secondary: book a studio visit.</li>
<li>Rejected: a zoom through video-filled letters (breaks on 375px phones) and a cursor thread trail (does nothing on touch, so it moved to the founder page).</li></ul></div>
"""

JS = """
const r=document.getElementById('tapeSim'),fill=document.getElementById('tapeFill'),tape=document.getElementById('tape');
function upd(){const v=+r.value;fill.style.height=(v/100*(tape.clientHeight-32))+'px';
 tape.querySelectorAll('.mark').forEach(m=>m.classList.toggle('on',v>=+m.dataset.at));}
r.addEventListener('input',upd);window.addEventListener('resize',upd);upd();
document.getElementById('replayB').addEventListener('click',()=>{
 document.querySelectorAll('#stageB .paper,#stageB .scissor').forEach(el=>{el.style.animation='none';el.offsetWidth;el.style.animation='';});});
"""

page("hero.html", "Hero Options", "01 / 09", "Hero",
     "Five ways to open the page. Every one keeps the same information layer: who we are, what we teach, where, and two buttons. They differ only in the one signature motion. The mocks are rough, motion loops so you can see it without scrolling.",
     body, CSS, JS)
