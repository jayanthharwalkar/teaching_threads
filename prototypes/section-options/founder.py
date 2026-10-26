from common import *

CSS = """
.ed{display:grid;grid-template-columns:.8fr 1.2fr;gap:32px;padding:36px 32px;align-items:start}
.ed .portrait{aspect-ratio:4/5}
.ed figcaption{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil);margin-top:8px}
.ed .col{display:grid;gap:16px}
.ed .quote{font-family:var(--serif);font-size:clamp(26px,4.2cqi,40px);line-height:1.05;margin:0;border-left:2px solid var(--ink);padding-left:16px}
.ed .quote em{font-style:italic}
.ed p.body{margin:0;font-size:14px;line-height:1.6;max-width:56ch;color:#3a3834}
.contact{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.contact .duo{aspect-ratio:3/4;position:relative}
.contact b{position:absolute;left:5px;bottom:4px;font-family:var(--mono);font-size:9px;font-weight:400;letter-spacing:.08em;z-index:2;background:var(--paper);padding:0 3px}
.contact .circ::before{content:"";position:absolute;inset:8% 6%;border:2.5px solid #b0472f;border-radius:50%;z-index:3;transform:rotate(-8deg)}
@container (max-width:620px){.ed{grid-template-columns:1fr;padding:24px 18px}}

.tl{padding:36px 32px;display:grid;gap:0;position:relative}
.tl::before{content:"";position:absolute;left:calc(32px + 76px);top:40px;bottom:40px;width:1px;background:var(--ink)}
.tl .it{display:grid;grid-template-columns:76px 1fr 120px;gap:22px;padding:16px 0;align-items:center}
.tl .yr{font-family:var(--mono);font-size:12px;letter-spacing:.08em}
.tl .it>div:nth-child(2){position:relative;padding-left:4px}
.tl .it>div:nth-child(2)::before{content:"";position:absolute;left:-27px;top:8px;width:9px;height:9px;border-radius:50%;background:var(--ink)}
.tl h6{margin:0;font-family:var(--serif);font-weight:400;font-size:26px;line-height:1.05}
.tl p{margin:2px 0 0;font-size:13px;color:#4a4843}
.tl .th{aspect-ratio:1;width:120px}
@container (max-width:560px){.tl{padding:24px 14px}.tl::before{left:calc(14px + 54px)}.tl .it{grid-template-columns:54px 1fr 70px;gap:16px}.tl .th{width:70px}.tl h6{font-size:21px}}

.letterbox{padding:44px 24px;display:flex;justify-content:center}
.letter{position:relative;width:min(560px,100%);background:#fdfcf9;border:1px solid #ddd8cc;padding:38px 36px 30px;box-shadow:0 18px 30px -18px rgba(0,0,0,.25);transform:rotate(-.6deg)}
.letter p{font-family:var(--hand);font-size:24px;line-height:1.3;margin:0 0 12px;color:#23221f}
.letter .sig{font-family:var(--hand);font-size:34px;margin-top:6px}
.polaroid{position:absolute;right:-18px;top:-26px;width:120px;background:#fff;padding:7px 7px 24px;box-shadow:0 6px 16px rgba(0,0,0,.15);transform:rotate(6deg)}
.polaroid .duo{aspect-ratio:3/4}
.polaroid span{position:absolute;bottom:5px;left:0;right:0;text-align:center;font-family:var(--hand);font-size:15px}
.pin{position:absolute;left:50%;top:-6px;width:12px;height:12px;border-radius:50%;background:#2b2a27;transform:translateX(-50%)}
@container (max-width:520px){.letter{padding:30px 20px}.polaroid{width:88px;right:-6px}.letter p{font-size:21px}}

.chap{display:grid;grid-template-columns:.9fr 1.1fr;min-height:460px}
.chap .left{position:relative;border-right:1px solid var(--rule)}
.chap .left .duo{position:absolute;inset:0;opacity:0;transition:opacity .5s}
.chap .left .duo.on{opacity:1}
.chap .right{padding:28px;display:grid;gap:4px;align-content:center}
.chap button{all:unset;cursor:pointer;display:grid;gap:4px;padding:16px 0;border-bottom:1px solid var(--rule)}
.chap button .n{font-family:var(--mono);font-size:10px;letter-spacing:.12em;color:var(--pencil)}
.chap button .t{font-family:var(--serif);font-size:clamp(26px,4cqi,38px);line-height:1;color:#b9b5ac;transition:color .3s}
.chap button p{margin:0;font-size:13px;max-height:0;overflow:hidden;transition:max-height .4s;color:#3a3834}
.chap button[aria-selected="true"] .t{color:var(--ink)}
.chap button[aria-selected="true"] p{max-height:120px}
.chap button:focus-visible{outline:2px solid var(--ink)}
@container (max-width:600px){.chap{grid-template-columns:1fr}.chap .left{height:300px;border-right:0;border-bottom:1px solid var(--rule)}}

.trail{position:relative;height:460px;overflow:hidden;cursor:crosshair}
.trail svg.th{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.trail svg.th polyline{fill:none;stroke:var(--ink);stroke-width:1.2;stroke-dasharray:6 5}
.trail .card{position:absolute;width:110px;aspect-ratio:3/4;transform:translate(-50%,-50%) rotate(var(--r));animation:drop 2.6s forwards;pointer-events:none;border:1px solid var(--rule)}
@keyframes drop{0%{opacity:0;scale:.6}12%{opacity:1;scale:1}75%{opacity:1}100%{opacity:0;scale:.9}}
.trail .center{position:absolute;inset:0;display:grid;place-content:center;text-align:center;gap:10px;pointer-events:none;padding:20px}
.trail .center .h1{font-size:clamp(34px,6cqi,60px)}
"""

FACT = ("Shruti Mahajan is a registered fashion designer with 15 years in the industry. She has run her own boutique in Hubli-Dharwad for "
        "12 years, was named the youngest female entrepreneur by the Times of India, and showed her Forest Fury collection at the "
        "Kerala Fashion League in 2016.")

A = f"""<div class="ed">
<figure style="margin:0"><div class="duo grain portrait"><img src="{img('portrait', 600)}" alt="Shruti Mahajan"></div><figcaption>Shruti Mahajan · Kerala Fashion League, 2016</figcaption></figure>
<div class="col"><span class="eyebrow">Hubballi, Karnataka · The founder</span>
<p class="h2">Learn from someone who still makes clothes for a living.</p>
<p class="body">{FACT}</p>
<blockquote class="quote">“I teach the way I learned: <em>measure first,</em> then everything else.” <span class="ph">placeholder, her words</span></blockquote>
<div class="contact"><div class="duo grain"><img src="{img('cape', 300)}" alt=""><b>FF-01</b></div><div class="duo grain circ"><img src="{img('trio', 300)}" alt=""><b>FF-02</b></div><div class="duo grain"><img src="{img('floral', 300)}" alt=""><b>FF-06</b></div></div>
</div></div>"""

items = [("2016", "Kerala Fashion League", "Shows the Forest Fury collection in Kochi.", "lineup"),
         ("2016", "In the papers", "\"Hubballi designer shines at Kerala Fashion League\".", "news_en"),
         ('<span class="ph">year?</span>', "Youngest female entrepreneur", "Awarded by the Times of India.", "brand"),
         ("12+ yrs", "Her boutique, Hubli-Dharwad", "Running her own designer-wear boutique.", "floral_blue"),
         ('<span class="ph">year?</span>', "Teaching Threads opens", "3- and 6-month courses in Hubballi.", None)]
tl = ""
for y, h, p, k in items:
    th = f'<div class="duo grain th"><img src="{img(k, 260)}" alt=""></div>' if k else f'<div class="th"><img class="clay" src="{img("dressform", 260)}" alt=""></div>'
    tl += f'<div class="it"><div class="yr">{y}</div><div><h6>{h}</h6><p>{p}</p></div>{th}</div>'
B = f'<div class="tl">{tl}</div>'

C = f"""<div class="letterbox"><div class="letter">
<div class="polaroid"><span class="pin"></span><div class="duo"><img src="{img('cape', 260)}" alt=""></div><span>Forest Fury, '16</span></div>
<p>Dear future student,</p>
<p>I started with a measuring tape and a lot of mistakes. Fifteen years later I still measure twice. In my studio you'll make real blouses and lehengas on real machines, from your first week.</p>
<p>Come and see the studio before you decide.</p>
<div class="sig">Shruti</div>
<div style="margin-top:10px"><span class="ph">draft letter: ideally Shruti writes it by hand and we scan it, with the same text in HTML</span></div>
</div></div>"""

chs = [("01", "The runway", "Forest Fury at the Kerala Fashion League, 2016: a collection built from scratch, shown in Kochi.", "cape"),
       ("02", "The boutique", "12+ years making clothes for real customers in Hubli-Dharwad. What sells, what fits, what lasts.", "floral"),
       ("03", "The method", "Measure, draft, stitch. The same five stages she uses every day are the five stages of the course.", "measure")]
left = "".join(f'<div class="duo grain{" on" if i == 0 else ""}" data-i="{i}"><img src="{img(k, 600)}" alt=""></div>' if k != "measure"
               else f'<div class="duo{" on" if i == 0 else ""}" data-i="{i}" style="mix-blend-mode:normal"><img class="clay" style="filter:none;mix-blend-mode:normal" src="{img(k, 600)}" alt=""></div>'
               for i, (_, _, _, k) in enumerate(chs))
right = "".join(f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}" data-i="{i}"><span class="n">{n}</span><span class="t">{t}</span><p>{p}</p></button>' for i, (n, t, p, _) in enumerate(chs))
D = f'<div class="chap" id="chap"><div class="left">{left}</div><div class="right" role="tablist"><span class="eyebrow">Shruti Mahajan, in three chapters</span>{right}</div></div>'

E = """<div class="trail" id="trail"><svg class="th"><polyline points=""/></svg>
<div class="center"><span class="eyebrow">Move your cursor (or wait)</span><p class="h1">Shruti Mahajan</p><span class="mono">Designer · Founder · Hubballi</span></div></div>"""

TRAIL_IMGS = ["cape", "trio", "curly", "floral", "floral_blue", "lineup", "walk"]

body = "".join([
    option("A", "Editorial profile + pull quote", A,
           "A magazine-style spread: an inked portrait at 4:5, a dateline, a short profile, one big quote in her words, and a contact-sheet row of three runway looks with one circled in grease pencil.",
           "Calm and confident, and it suits the minimal direction best. Photos are either small or duotone, so the low resolution never shows.",
           "Portrait, then text, then quote, then the three thumbnails in a row.",
           [("DesignRush: Vogue Runway", "https://www.designrush.com/best-designs/apps/vogue-runway"), ("Contra: Ralph Lauren runway page", "https://contra.com/p/vYBlYgeU-ralph-lauren"),
            ("Evagria portfolio (contact sheet)", "https://uiuxshowcase.com/portfolio/evagria-portfolio/")],
           rec=True),
    option("B", "Runway-to-academy timeline", B,
           "A vertical ink rule with dated stops: the 2016 show, the press, the award, the boutique, the academy. Each stop has one small treated photo.",
           "Dated facts double as proof and are easy to verify. This is how Polimoda tells its own story.",
           "Already a vertical stack; the thumbnails shrink.",
           [("Polimoda: 70 years history page", "https://www.polimoda.com/70-years-ago"), ("UAL / CSM: Louise Wilson story", "https://www.arts.ac.uk/colleges/central-saint-martins/stories/professor-louise-wilson-obe-1962-to-2014")],
           runner=True),
    option("C", "Letter from the founder", C,
           "A handwritten letter on paper with a polaroid of a Forest Fury look pinned to the corner.",
           "The warmest option. Without testimonials, this is where the human voice comes from.",
           "Ideal on phones. The letter text stays as real HTML even if we show a scan.",
           [("No precedent found: closest is the Polimoda history tone", "https://www.polimoda.com/70-years-ago")],
           original=True),
    option("D", "Sticky portrait, three chapters", D,
           "Three chapters, The runway, The boutique, The method, on the right. Pick one and the image on the left swaps. On the real page it changes as you scroll.",
           "Tells her story one beat at a time, and the third chapter hands off neatly to the course stages.",
           "No pinning: each chapter shows its image inline above the text.",
           [("Codrops: menu image on hover", "https://tympanus.net/codrops/2020/07/01/creating-a-menu-image-animation-on-hover/"), ("Awwwards: Martine Rose", "https://www.awwwards.com/inspiration/hero-scroll-gallery-martine-rose")]),
    option("E", "Thread trail (desktop add-on)", E,
           "Moving the cursor spools out a dashed black thread that drops small inked runway cards behind it. Works as an add-on to A or D.",
           "Playful in the thesuperrco.com way, and the cards are so small the photo quality never matters.",
           "Touch has no cursor, so it becomes an auto-playing loop of five cards (what you see if you leave it alone).",
           [("Codrops: Image Trail Effects", "https://tympanus.net/codrops/2019/08/07/image-trail-effects"), ("Awwwards: Amanda Braga fashion trail", "https://www.awwwards.com/inspiration/cursor-with-trail-effect-amanda-braga-fashion-creative-designer")]),
])
body += """<div class="aside"><h3>Photo rule for this section</h3><p>Only one photo is ever shown large: the portrait, after the ink duotone. Every runway photo stays thumbnail size. The photos page shows all the treatments side by side.</p></div>"""

JS = """
const ch=document.getElementById('chap');
ch.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{const i=b.dataset.i;
 ch.querySelectorAll('button').forEach(x=>x.setAttribute('aria-selected',x===b));
 ch.querySelectorAll('.left .duo').forEach(d=>d.classList.toggle('on',d.dataset.i===i));}));
const tr=document.getElementById('trail'),pl=tr.querySelector('polyline'),srcs=__SRCS__;let pts=[],last=0,k=0,auto=true,t=0;
function drop(x,y){const c=document.createElement('div');c.className='card duo';c.style.left=x+'px';c.style.top=y+'px';c.style.setProperty('--r',(Math.random()*12-6)+'deg');
 c.innerHTML='<img src="'+srcs[k++%srcs.length]+'" alt="">';tr.appendChild(c);setTimeout(()=>c.remove(),2700);}
function add(x,y){pts.push([x,y]);if(pts.length>60)pts.shift();pl.setAttribute('points',pts.map(p=>p.join(',')).join(' '));
 const p=pts[pts.length-2];if(p){last+=Math.hypot(x-p[0],y-p[1]);if(last>120){last=0;drop(x,y);}}}
tr.addEventListener('mousemove',e=>{auto=false;const r=tr.getBoundingClientRect();add(e.clientX-r.left,e.clientY-r.top)});
tr.addEventListener('mouseleave',()=>auto=true);
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
(function loop(){if(auto&&!rm){t+=.025;const w=tr.clientWidth,h=tr.clientHeight;add(w/2+Math.cos(t)*w*.36,h/2+Math.sin(t*2)*h*.3);}requestAnimationFrame(loop)})();
"""
JS = JS.replace("__SRCS__", "[" + ",".join(f'"{img(k, 240)}"' for k in TRAIL_IMGS) + "]")

page("founder.html", "Founder Section Options", "05 / 09", "About the founder",
     "Five ways to tell Shruti's story with the photos we have: 2016 Kerala Fashion League runway shots, two press clippings and the brand-board photo. All facts come from her course PDFs; orange tags are things only she can fill in.",
     body, CSS, JS)
