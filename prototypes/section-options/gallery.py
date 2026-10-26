"""Achievements gallery: five ways to show only what Shruti has achieved, using the photos and clippings we already have."""
from common import *

CROPS["ramp"] = ("brand", (0.015, 0.178, 0.985, 0.99))  # Show 1 without the white label header

# the achievements, in order; kind "photo" uses an image, "text" is set in type (no photo exists)
REC = [
    ("2016", "Kerala Fashion League, Kochi", "Her collection Forest Fury on one of South India's biggest ramps.", "photo", "lineup"),
    ("2016", "Her own label on the ramp", "Shruti Mahajans Designer Wear, with Shruti taking the bow beside her model.", "photo", "brand"),
    ("2016", "Deccan Herald", "“Hubballi designer shines at Kerala Fashion League.”", "photo", "news_en"),
    ("2016", "Kannada press", "The same show, covered in the Kannada papers.", "photo", "news_kn"),
    ("Award", "Times of India", "Named youngest female entrepreneur.", "text", ("Youngest female entrepreneur", "Times of India")),
    ("15 yrs", "Designer and boutique owner", "15 years in fashion, 12+ running her own boutique in Hubli-Dharwad.", "text", ("15 years", "in fashion · 12+ with her own boutique")),
]

CSS = """
/* A: the record */
.recd{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:28px;padding:32px 28px;align-items:start}
.rec-list{display:flex;flex-direction:column;border-top:1px solid var(--ink)}
.rr{display:grid;grid-template-columns:64px minmax(0,1fr);gap:2px 16px;text-align:left;background:none;border:0;border-bottom:1px solid var(--rule);padding:14px 0;cursor:pointer;color:var(--ink);font:inherit;opacity:.45;transition:opacity .25s}
.rr.on,.rr:hover,.rr:focus-visible{opacity:1}
.rr .yr{grid-row:1/3;font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;padding-top:8px}
.rr .t{font-family:var(--serif);font-size:clamp(24px,3.4cqi,36px);line-height:1.05}
.rr .d{font-size:13px;line-height:1.45;color:#4a4843;max-height:0;overflow:hidden;transition:max-height .3s}
.rr.on .d{max-height:60px}
.rec-view{position:sticky;top:20px;aspect-ratio:4/5;background:#e9e6df}
.pane{position:absolute;inset:0;margin:0;opacity:0;transition:opacity .45s;display:flex}
.pane.on{opacity:1}
.pane img{width:100%;height:100%;object-fit:cover}
.pane.contain img{object-fit:contain;background:#e9e6df}
.pane.txt{background:var(--ink);color:var(--paper);flex-direction:column;justify-content:flex-end;padding:28px;gap:10px}
.pane.txt b{font-family:var(--serif);font-weight:400;font-size:clamp(34px,6cqi,60px);line-height:.95}
.pane.txt span{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#bdb8ae}
@container (max-width:640px){.recd{grid-template-columns:1fr;padding:20px}.rec-view{position:relative;top:0;order:-1;aspect-ratio:4/3}}

/* B: contact sheet */
.cs{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:28px;padding:28px;align-items:center}
.sheet{background:#1b1a18;padding:14px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px 8px}
.fr{position:relative;background:none;border:0;padding:0 0 16px;cursor:pointer;font:inherit}
.fr img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover;filter:grayscale(.15)}
.fr span{position:absolute;left:0;bottom:0;font-family:var(--mono);font-size:9px;letter-spacing:.12em;color:#c8b98f}
.fr svg{position:absolute;inset:-8px -6px 8px;width:calc(100% + 12px);height:calc(100% - 0px);overflow:visible;pointer-events:none;opacity:0}
.fr svg path{fill:none;stroke:#d23b2a;stroke-width:3;stroke-linecap:round;stroke-dasharray:600;stroke-dashoffset:600}
.fr.on svg{opacity:1}.fr.on svg path{animation:draw .6s ease-out forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.loupe{display:flex;flex-direction:column;gap:12px}
.loupe .lens{aspect-ratio:3/4;overflow:hidden;background:#e9e6df;border:1px solid var(--ink)}
.loupe .lens img{width:100%;height:100%;object-fit:cover}
.loupe b{font-family:var(--serif);font-weight:400;font-size:28px;line-height:1.05}
.loupe p{font-size:13.5px;margin:0;color:#4a4843}
@container (max-width:640px){.cs{grid-template-columns:1fr;padding:16px}.loupe{order:-1}.loupe .lens{aspect-ratio:4/3}}

/* C: magazine spread */
.mag{padding:28px;display:flex;flex-direction:column;gap:14px;perspective:1600px}
.spreads{position:relative;aspect-ratio:16/10}
.spread{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;opacity:0;pointer-events:none;box-shadow:0 20px 40px -28px rgba(0,0,0,.5)}
.spread.on{opacity:1;pointer-events:auto}
.spread .pg{position:relative;overflow:hidden;background:#fbfaf7}
.spread .pg+.pg{border-left:1px solid #e1ddd4;padding:7% 8%;display:flex;flex-direction:column;gap:10px;transform-origin:0 50%}
.spread.on .pg+.pg{animation:turn .7s cubic-bezier(.3,.7,.2,1)}
@keyframes turn{from{transform:rotateY(-80deg);opacity:.2}to{transform:none;opacity:1}}
.spread .pg img{width:100%;height:100%;object-fit:cover}
.spread .pg.contain img{object-fit:contain;background:#e9e6df}
.spread .pg.ink{background:var(--ink);color:var(--paper);display:flex;flex-direction:column;justify-content:flex-end;padding:8%}
.spread .pg.ink b{font-family:var(--serif);font-weight:400;font-size:clamp(30px,5cqi,54px);line-height:.95}
.spread .run{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--pencil);display:flex;justify-content:space-between}
.spread h5{margin:auto 0 0;font-family:var(--serif);font-weight:400;font-size:clamp(26px,4.2cqi,46px);line-height:1}
.spread p{margin:0;font-size:13.5px;color:#4a4843;max-width:34ch}
.spread q{font-family:var(--serif);font-style:italic;font-size:19px;line-height:1.2}
.mag-nav{display:flex;align-items:center;gap:12px;justify-content:center;font-family:var(--mono);font-size:11px;letter-spacing:.12em}
.mag-nav button{width:38px;height:38px;border-radius:50%;border:1px solid var(--ink);background:none;cursor:pointer;font:inherit;font-size:16px}
@container (max-width:640px){.mag{padding:16px}.spreads{aspect-ratio:auto;height:560px}.spread{grid-template-columns:1fr;grid-template-rows:55% 45%}.spread .pg+.pg{border-left:0;border-top:1px solid #e1ddd4;padding:18px}}

/* D: stack of prints */
.stk{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.8fr);gap:28px;padding:36px 28px;align-items:center}
.pile{position:relative;height:430px;touch-action:pan-y}
.print{position:absolute;left:50%;top:50%;width:min(270px,70%);background:#fff;padding:10px 10px 44px;box-shadow:0 14px 28px -16px rgba(0,0,0,.45);
  transform:translate(-50%,-50%) rotate(var(--r));transition:transform .5s cubic-bezier(.3,.7,.2,1),opacity .3s;cursor:grab;user-select:none}
.print img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;pointer-events:none}
.print.contain img{object-fit:contain;background:#efede8}
.print span{position:absolute;left:12px;right:12px;bottom:10px;font-family:var(--hand);font-size:21px;line-height:1;color:#2b2a27}
.print.out{transform:translate(-160%,-50%) rotate(-20deg);opacity:0}
.stk-side{display:flex;flex-direction:column;gap:12px}
.stk-side b{font-family:var(--serif);font-weight:400;font-size:clamp(28px,4cqi,40px);line-height:1}
.stk-side p{margin:0;font-size:14px;color:#4a4843}
.stk-side .mono{color:var(--pencil)}
@container (max-width:640px){.stk{grid-template-columns:1fr;padding:20px}.pile{height:380px}}

/* E: editorial mosaic */
.mos{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:150px;gap:8px;padding:28px}
.tile{position:relative;overflow:hidden;background:#e9e6df;margin:0}
.tile img{width:100%;height:100%;object-fit:cover;transition:transform .6s}
.tile:hover img{transform:scale(1.04)}
.tile.contain img{object-fit:contain}
.tile figcaption{position:absolute;left:0;right:0;bottom:0;padding:22px 10px 8px;background:linear-gradient(transparent,rgba(0,0,0,.6));color:#fff;font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;text-transform:uppercase}
.tile.fact{background:var(--ink);color:var(--paper);display:flex;flex-direction:column;justify-content:flex-end;padding:14px;gap:4px}
.tile.fact.light{background:#fbfaf7;color:var(--ink);border:1px solid var(--ink)}
.tile.fact b{font-family:var(--serif);font-weight:400;font-size:clamp(26px,3.6cqi,40px);line-height:.95}
.tile.fact span{font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;opacity:.75}
.w2{grid-column:span 2}.h2{grid-row:span 2}
@container (max-width:640px){.mos{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:130px;padding:16px}}
"""

# A
rows, panes = "", ""
for i, (yr, t, d, kind, src) in enumerate(REC):
    rows += f'<button type="button" class="rr{" on" if i == 0 else ""}" data-i="{i}"><span class="yr">{yr}</span><span class="t">{t}</span><span class="d">{d}</span></button>'
    if kind == "photo":
        cls = " contain" if src.startswith("news") else ""
        panes += f'<figure class="pane{cls}{" on" if i == 0 else ""}"><img src="{img(src, 700)}" alt="{t}"></figure>'
    else:
        panes += f'<div class="pane txt"><b>{src[0]}</b><span>{src[1]}</span></div>'
A = f'<div class="recd" id="ga"><div class="rec-list">{rows}</div><div class="rec-view">{panes}</div></div>'

# B
FR = [("lineup", "Forest Fury closes the show", "Kerala Fashion League, Kochi, 2016. Her name on the screen behind the line-up."),
      ("ramp", "Taking the bow", "Shruti on the KFL ramp beside her model, in her own label."),
      ("walk", "On the ramp", "Shruti walks out with her model at the end of the show."),
      ("cape", "The printed cape", "One of the Forest Fury looks, made from upholstery fabric."),
      ("trio", "Three looks, one print", "Forest Fury under the KFL lights."),
      ("curly", "Floral gown", "Forest Fury, Kerala Fashion League 2016.")]
ELL = '<svg viewBox="0 0 100 130" preserveAspectRatio="none"><path d="M52 4C20 2 3 30 4 66s20 60 48 60 45-26 44-64S78 2 40 8"/></svg>'
frames = "".join(f'<button type="button" class="fr{" on" if i == 0 else ""}" data-i="{i}" data-t="{t}" data-d="{d}"><img src="{img(k, 360)}" alt="{t}">{ELL}<span>{12 + i}A ▸ KODAK</span></button>' for i, (k, t, d) in enumerate(FR))
B = f'''<div class="cs" id="gb"><div class="sheet">{frames}</div>
<div class="loupe"><div class="lens"><img id="gb-img" src="{img(FR[0][0], 700)}" alt=""></div><span class="mono" style="color:var(--pencil)">Frame 12A</span><b id="gb-t">{FR[0][1]}</b><p id="gb-d">{FR[0][2]}</p></div></div>'''
B_FULL = [img(k, 700) for k, _, _ in FR]

# C
SP = [
    (f'<div class="pg"><img src="{img("lineup", 800)}" alt="Forest Fury line-up"></div>', "Kerala Fashion League", "Forest Fury on the Kochi ramp", "Her collection shown alongside more than 20 designers from across India, at one of the biggest fashion events in South India."),
    (f'<div class="pg contain"><img src="{img("news_en", 700)}" alt="Deccan Herald clipping"></div>', "In the papers", "“Hubballi designer shines”", '<q>These kind of events helped to understand the fashion industry, which is not taught by the books.</q>'),
    (f'<div class="pg"><img src="{img("ramp", 800)}" alt="Shruti with her model"></div>', "Her label", "Shruti Mahajans Designer Wear", "Shruti takes her bow on the KFL ramp in 2016, beside her model in a floral lehenga."),
    ('<div class="pg ink"><b>Youngest female entrepreneur</b></div>', "Recognition", "Times of India", "Named youngest female entrepreneur, with 15 years in fashion and 12+ running her own boutique in Hubli-Dharwad."),
]
spreads = "".join(f'<div class="spread{" on" if i == 0 else ""}">{left}<div class="pg"><div class="run"><span>Teaching Threads</span><span>p. {12 + i * 2}</span></div><span class="mono" style="color:var(--pencil)">{k}</span><h5>{h}</h5><p>{p}</p></div></div>' for i, (left, k, h, p) in enumerate(SP))
C = f'<div class="mag" id="gc"><div class="spreads">{spreads}</div><div class="mag-nav"><button type="button" data-d="-1" aria-label="Previous spread">←</button><span id="gc-n">1 / {len(SP)}</span><button type="button" data-d="1" aria-label="Next spread">→</button></div></div>'

# D
PR = [("lineup", "Kochi, KFL 2016", "Kerala Fashion League", "Forest Fury, her collection, on the ramp."),
      ("news_en", "Deccan Herald!", "In the papers", "“Hubballi designer shines at Kerala Fashion League.”"),
      ("ramp", "my label on the ramp", "Her own label", "Shruti Mahajans Designer Wear, Kochi 2016."),
      ("news_kn", "Kannada papers", "Kannada press", "The same show, covered in Kannada."),
      ("walk", "end of the show", "On the ramp", "Shruti walks out with her model.")]
rots = ["-3deg", "4deg", "-6deg", "2deg", "-1deg"]
prints = "".join(f'<div class="print{" contain" if k.startswith("news") else ""}" style="--r:{rots[i]};z-index:{len(PR) - i}" data-t="{t}" data-d="{d}"><img src="{img(k, 460)}" alt="{t}"><span>{hand}</span></div>' for i, (k, hand, t, d) in enumerate(PR))
D = f'''<div class="stk" id="gd"><div class="pile">{prints}</div>
<div class="stk-side"><span class="mono" id="gd-n">1 of {len(PR)} · tap or swipe the top print</span><b id="gd-t">{PR[0][2]}</b><p id="gd-d">{PR[0][3]}</p></div></div>'''

# E
E = f'''<div class="mos">
<figure class="tile w2 h2"><img src="{img("lineup", 700)}" alt=""><figcaption>Forest Fury · Kerala Fashion League 2016</figcaption></figure>
<figure class="tile h2 contain"><img src="{img("news_en", 400)}" alt=""><figcaption>Deccan Herald · 2016</figcaption></figure>
<div class="tile fact"><b>15 yrs</b><span>in fashion</span></div>
<div class="tile fact light"><b>12+ yrs</b><span>her own boutique</span></div>
<figure class="tile h2"><img src="{img("ramp", 400)}" alt=""><figcaption>Her label on the ramp</figcaption></figure>
<div class="tile fact w2"><b>Youngest female entrepreneur</b><span>Times of India</span></div>
<figure class="tile h2"><img src="{img("walk", 400)}" alt=""><figcaption>End of the show</figcaption></figure>
<figure class="tile w2 contain"><img src="{img("news_kn", 600)}" alt=""><figcaption>Kannada press</figcaption></figure>
</div>'''

body = "".join([
    option("A", "The record", A,
           "Her achievements as a short list in large type. Select a line and the panel beside it shows the proof: the photo, the clipping, or the award set in type where no photo exists. It steps through on its own until someone touches it.",
           "Every line is an achievement, so nothing on screen is decoration. The low-res photos are shown one at a time at a modest size, and the two facts without photos still get equal weight.",
           "The panel sits above the list. Tap a line to change it.",
           [("Framer: Hover Awards List", "https://www.framer.com/marketplace/components/hover-awards-list/"), ("Framer: Hover Reveal List", "https://www.framer.com/marketplace/components/hover-reveal-list/"), ("Awwwards: hover image reveal", "https://www.awwwards.com/inspiration/hover-image-reveal-castor-pollux")],
           rec=True),
    option("B", "Contact sheet", B,
           "The runway photos printed as frames on a photographer's proof sheet. The chosen frame gets circled in red grease pencil, the way editors mark the keeper, and opens large beside the sheet with its story.",
           "Photographers and fashion editors really pick shots this way, so it reads as backstage at a show. Small frames suit the WhatsApp-quality photos.",
           "The large view sits on top, the sheet below it in three columns.",
           [("Framer: Film Contact Sheet", "https://www.framer.com/community/marketplace/components/film-contact-sheet/"), ("Milanote: contact sheet template", "https://milanote.com/templates/photography/contact-sheet")]),
    option("C", "Magazine spread", C,
           "A fashion-magazine feature about her: each spread pairs a full-page photo with a page of text. The right page turns in when you go to the next spread. Four spreads: the show, the press, her label, the award.",
           "It's the format her world uses to celebrate designers, and the text page explains each achievement in a sentence.",
           "One page above the other, with the same arrows.",
           [("Codrops: page-flip effects", "https://tympanus.net/codrops/?s=page+flip"), ("Polimoda: archive storytelling", "https://www.polimoda.com/70-years-ago")],
           original=True),
    option("D", "Stack of prints", D,
           "Printed photos and clippings in a loose pile, with a handwritten note on each. Tap or swipe the top one and it slides off to the bottom of the pile, showing the next.",
           "Feels personal, like Shruti showing you her photos across the studio table. Swiping a pile is natural on a phone.",
           "Same pile, slightly smaller; swipe left to send a print to the back.",
           [("Codrops: stack of cards motion", "https://tympanus.net/codrops/?s=stack+cards")],
           original=True),
    option("E", "Editorial grid", E,
           "Everything at once in a tight magazine grid: the show, the clippings, her label and three fact tiles. No interaction beyond a slow zoom on hover.",
           "The quietest option. Nothing to learn, nothing to break, and it reads in two seconds. A safe pick if the page above already moves enough.",
           "Two columns; the big photo stays two tiles wide.",
           [("Awwwards: press page examples", "https://www.awwwards.com/inspiration/press-kristina-vilyams")]),
])
body += """<div class="aside"><h3>Notes</h3><ul>
<li>All options use only what we have: the runway photos, the two 2016 clippings and the facts from the course PDFs. Nothing new is needed from Shruti.</li>
<li>Only achievements: the show, her label, the press, the award and her years in fashion. The plain look photos (cape, gowns) appear only in B, where they're the show's own frames.</li>
<li>The page order will be: hero (Prototype 08) → this gallery → the five-stage swipe sequence.</li></ul></div>"""

JS = """
// A: select a line, auto-step until touched
(function(){const g=document.getElementById('ga'),rs=[...g.querySelectorAll('.rr')],ps=[...g.querySelectorAll('.pane')];let i=0,auto=true;
 const set=n=>{i=n;rs.forEach((r,k)=>r.classList.toggle('on',k===n));ps.forEach((p,k)=>p.classList.toggle('on',k===n))};
 rs.forEach((r,k)=>{const go=()=>{auto=false;set(k)};r.addEventListener('click',go);r.addEventListener('mouseenter',go);r.addEventListener('focus',go)});
 setInterval(()=>{if(auto)set((i+1)%rs.length)},3200)})();
// B: circle a frame
(function(){const g=document.getElementById('gb'),fs=[...g.querySelectorAll('.fr')],big=B_FULL;
 fs.forEach((f,k)=>f.addEventListener('click',()=>{fs.forEach(x=>x.classList.remove('on'));void f.offsetWidth;f.classList.add('on');
  document.getElementById('gb-img').src=big[k];document.getElementById('gb-t').textContent=f.dataset.t;document.getElementById('gb-d').textContent=f.dataset.d;
  g.querySelector('.loupe .mono').textContent='Frame '+(12+k)+'A'}))})();
// C: turn the spread
(function(){const g=document.getElementById('gc'),sp=[...g.querySelectorAll('.spread')];let i=0;
 g.querySelectorAll('.mag-nav button').forEach(b=>b.addEventListener('click',()=>{i=(i+(+b.dataset.d)+sp.length)%sp.length;
  sp.forEach((s,k)=>s.classList.toggle('on',k===i));document.getElementById('gc-n').textContent=(i+1)+' / '+sp.length}))})();
// D: send the top print to the back
(function(){const g=document.getElementById('gd'),pile=g.querySelector('.pile');let order=[...pile.querySelectorAll('.print')],n=0,sx=null;
 function next(){const top=order[0];top.classList.add('out');setTimeout(()=>{order.push(order.shift());order.forEach((p,k)=>p.style.zIndex=order.length-k);top.classList.remove('out');
  n=(n+1)%order.length;const t=order[0];document.getElementById('gd-t').textContent=t.dataset.t;document.getElementById('gd-d').textContent=t.dataset.d;
  document.getElementById('gd-n').textContent=(n+1)+' of '+order.length+' · tap or swipe the top print'},420)}
 pile.addEventListener('pointerdown',e=>{sx=e.clientX});
 pile.addEventListener('pointerup',e=>{if(sx===null)return;const dx=e.clientX-sx;sx=null;if(Math.abs(dx)>40||Math.abs(dx)<6)next()})})();
"""
JS = "const B_FULL=" + str(B_FULL).replace("'", '"') + ";\n" + JS.replace("big=B_FULL", "big=B_FULL")

page("gallery.html", "Achievements Gallery Options", "Gallery", "Her achievements",
     "A small gallery between the hero and the five stages that shows only what Shruti has done: the Kerala Fashion League show, her label, the press and the award. Five ways to show it, all built from photos we already have. Try each one, they're live.",
     body, CSS, JS)
