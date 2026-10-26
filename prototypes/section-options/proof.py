from common import *

FACTS = ["Shown at Kerala Fashion League 2016", "Forest Fury collection", "15 years in fashion", "12+ years running a boutique in Hubli-Dharwad",
         "Times of India · youngest female entrepreneur", "Industrial machines", "Hubballi studio"]

CSS = """
.marq{border-block:1px solid var(--ink);overflow:hidden;position:relative;margin:40px 0}
.marq .ticks{height:12px;background:repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 10px),repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 50px);
  background-size:100% 6px,100% 12px;background-repeat:no-repeat}
.marq .track{display:flex;width:max-content;animation:slide 40s linear infinite;padding:14px 0}
.marq:hover .track{animation-play-state:paused}
.marq span{font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;padding-right:28px;white-space:nowrap}
.marq span::after{content:"✕";margin-left:28px;font-size:9px;vertical-align:2px}
@keyframes slide{to{transform:translateX(-50%)}}
.ctx{padding:26px 28px;display:grid;gap:6px}
.ctx .h2{max-width:20ch}

.labelbox{display:flex;justify-content:center;padding:44px 20px}
.care{width:min(360px,100%);background:#fbfaf7;border:1px solid #cfcabe;position:relative;padding:26px 24px 22px;box-shadow:0 1px 0 #cfcabe;
  background-image:repeating-linear-gradient(0deg,rgba(0,0,0,.025) 0 1px,transparent 1px 3px)}
.care::before,.care::after{content:"";position:absolute;left:10px;right:10px;height:0;border-top:1.5px dashed var(--ink)}
.care::before{top:9px}.care::after{bottom:9px}
.care h5{margin:0 0 12px;font-family:var(--serif);font-weight:400;font-size:30px;line-height:1;text-align:center}
.care dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:6px 14px;font-family:var(--mono);font-size:11.5px;line-height:1.35}
.care dt{letter-spacing:.12em;color:var(--pencil)}
.care dd{margin:0;text-transform:uppercase;letter-spacing:.04em}
.care .icons{display:flex;justify-content:center;gap:16px;margin-top:16px}
.care .icons svg{width:24px;height:24px;stroke:var(--ink);fill:none;stroke-width:1.4}

.credits{padding:32px 28px;display:grid;gap:4px;position:relative;min-height:380px}
.credits .row{display:grid;grid-template-columns:140px 1fr;gap:16px;padding:10px 0;border-bottom:1px solid var(--rule);align-items:baseline}
.credits .row span:first-child{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--pencil)}
.credits .row span:last-child{font-family:var(--serif);font-size:clamp(22px,3.6cqi,34px);line-height:1.05}
.credits .hov{cursor:pointer;text-decoration:underline;text-decoration-style:dotted;text-underline-offset:5px;text-decoration-thickness:1px}
.peek{position:absolute;width:130px;aspect-ratio:3/4;pointer-events:none;opacity:0;transition:opacity .2s;z-index:5;border:1px solid var(--rule)}
.peek.on{opacity:1}
@container (max-width:520px){.credits .row{grid-template-columns:1fr;gap:2px}}

.film{background:#1b1a18;padding:18px 0;overflow:hidden}
.film .track{display:flex;gap:6px;width:max-content;animation:slide 36s linear infinite}
.cell{width:190px;background:#1b1a18;padding:16px 0;position:relative;flex:none}
.cell::before,.cell::after{content:"";position:absolute;left:0;right:0;height:9px;background:repeating-linear-gradient(90deg,transparent 0 6px,#f5f4f0 6px 14px,transparent 14px 20px)}
.cell::before{top:3px}.cell::after{bottom:3px}
.cell .duo{aspect-ratio:3/4}
.cell b{position:absolute;left:6px;bottom:20px;font-family:var(--mono);font-size:9px;color:#f5f4f0;letter-spacing:.1em;mix-blend-mode:difference;z-index:2}

.press{display:grid;grid-template-columns:1fr 1fr;gap:28px;padding:40px 32px;align-items:center}
.clips{position:relative;height:420px}
.clip{position:absolute;width:56%;background:#fff;padding:6px;box-shadow:0 8px 20px rgba(0,0,0,.08)}
.clip img{filter:grayscale(1) contrast(1.1)}
.clip::before{content:"";position:absolute;top:-10px;left:35%;width:60px;height:20px;background:rgba(220,214,200,.75);transform:rotate(-4deg)}
.clip.a{left:0;top:10px;transform:rotate(-3deg)}.clip.b{right:0;top:60px;transform:rotate(4deg)}
@container (max-width:620px){.press{grid-template-columns:1fr;padding:24px 18px}.clips{height:360px}}
"""

ICONS = """<div class="icons" aria-hidden="true">
<svg viewBox="0 0 24 24"><path d="M3 8h18l-2 11H5z"/><path d="M7 12c1.5-1 3-1 5 0s3.5 1 5 0"/></svg>
<svg viewBox="0 0 24 24"><path d="M12 4l9 16H3z"/></svg>
<svg viewBox="0 0 24 24"><path d="M4 17h16l-2-7c-.5-2-2-3-4-3H8"/><circle cx="12" cy="13" r="1"/></svg>
<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16"/><circle cx="12" cy="12" r="5"/></svg>
</div>"""

track = "".join(f"<span>{f}</span>" for f in FACTS) * 2
A = f"""<div class="ctx"><span class="eyebrow">Right under the hero</span><p class="h2">Why learn from Shruti Mahajan?</p></div>
<div class="marq"><div class="ticks"></div><div class="track">{track}</div><div class="ticks"></div></div>"""

B = f"""<div class="labelbox"><div class="care">
<h5>Teaching Threads</h5>
<dl><dt>ORIGIN</dt><dd>Hubballi, Karnataka</dd><dt>MAKER</dt><dd>Shruti Mahajan · 15 yrs in fashion</dd>
<dt>SHOWN</dt><dd>Kerala Fashion League 2016</dd><dt>BOUTIQUE</dt><dd>12+ yrs, Hubli-Dharwad</dd>
<dt>AWARD</dt><dd>Times of India · youngest female entrepreneur</dd><dt>CARE</dt><dd>Small batches · industrial machines</dd></dl>
{ICONS}</div></div>"""

rows = [("Designer", "Shruti Mahajan"), ("Collection", '<span class="hov" data-img="cape">Forest Fury</span>'),
        ("Show", '<span class="hov" data-img="lineup">Kerala Fashion League, 2016</span>'),
        ("Press", '<span class="hov" data-img="news_en">"Hubballi designer shines"</span>'),
        ("Recognition", "Times of India · youngest female entrepreneur"), ("Studio", "Hubballi, Karnataka")]
C = '<div class="credits" id="credits">' + "".join(f'<div class="row"><span>{a}</span><span>{b}</span></div>' for a, b in rows)
C += "".join(f'<div class="peek duo" data-k="{k}"><img src="{img(k, 300)}" alt=""></div>' for k in ["cape", "lineup", "news_en"]) + "</div>"

cells = [("cape", "FF-01"), ("trio", "FF-02"), ("curly", "FF-03"), ("lineup", "FF-04"), ("floral_blue", "FF-05"), ("floral", "FF-06"), ("walk", "FF-07")]
celhtml = "".join(f'<div class="cell"><div class="duo grain"><img src="{img(k, 300)}" alt="Runway look {n}"></div><b>{n} · KFL 2016</b></div>' for k, n in cells)
D = f'<div class="film"><div class="track">{celhtml * 2}</div></div><div class="ctx"><span class="eyebrow">Proof as pictures</span><p class="sub">The strip reads as a runway contact roll. Facts sit underneath as one line of mono type.</p></div>'

E = f"""<div class="press"><div style="display:grid;gap:14px">
<span class="eyebrow">In the press · 2016</span><p class="h2">“Hubballi designer shines at Kerala Fashion League”</p>
<p class="sub">Both clippings are already in the photos folder: one English, one Kannada. Real press beats any stat we could write, and the Kannada clipping speaks to local parents.</p></div>
<div class="clips"><div class="clip a"><img src="{img('news_en', 420)}" alt="English newspaper clipping"></div><div class="clip b"><img src="{img('news_kn', 420)}" alt="Kannada newspaper clipping"></div></div></div>"""

body = "".join([
    option("A", "Selvedge / tape marquee", A,
           "A thin band with tape-measure ticks on both edges and Shruti's credentials scrolling slowly in mono caps, like the printed edge of a bolt of fabric.",
           "Marquees are a proven pattern; dressing it as selvedge gives it a textile reason to exist. Pauses on hover.",
           "Works as is. Slow it down and bump the type a size.",
           [("Awwwards: text marquee collection", "https://www.awwwards.com/awwwards_collections/collections/text-marquee-effect/"), ("Awwwards: Togethxr scrolling text", "https://www.awwwards.com/inspiration/togethxr-scrolling-text")],
           runner=True),
    option("B", "Garment care label", B,
           "A woven care label with the facts printed as label fields: origin, maker, shown, award, care. Care symbols at the bottom.",
           "Static, honest and quiet. A handful of real facts reads as craft instead of an empty stats bar.",
           "Ideal on mobile, nothing moves.",
           [("Packaging of the World: Derrick Lin labels", "https://packagingoftheworld.com/?p=26130"), ("Fonts In Use: Ahluwalia (label type)", "https://www.fontsinuse.com/uses/41898/ahluwalia-e-commerce")],
           rec=True, original=True),
    option("C", "Runway credits roll", C,
           "Credits like the end of a show: designer, collection, show, press. Hover the underlined words to see a small inked photo next to the cursor.",
           "Turns the low-res photos into a small reward. They're only ever shown thumbnail size, so resolution never shows.",
           "Tap a line to show its photo, or show one small thumbnail per line.",
           [("Codrops: menu image on hover", "https://tympanus.net/codrops/2020/07/01/creating-a-menu-image-animation-on-hover/"), ("Codrops: image reveal hover effects", "https://tympanus.net/codrops/?p=36588")]),
    option("D", "Film-strip contact roll", D,
           "Seven Forest Fury looks as 35&nbsp;mm frames with sprocket holes and frame numbers, drifting sideways.",
           "The proof is visual, not verbal, and at this size the WhatsApp-quality photos hold up.",
           "A native swipe row with scroll-snap instead of auto-drift.",
           [("Codrops: infinite GSAP scroll gallery (Jul 2026)", "https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/"), ("Codrops: infinite parallax grid", "https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/")]),
    option("E", "Press clippings", E,
           "The two 2016 newspaper clippings from the photos folder, taped to the page at an angle, with the English headline set large beside them.",
           "Third-party proof that already exists, in English and Kannada. New since the report: I found these while picking photos.",
           "Clippings stack under the headline; tap to open one full size.",
           [("Polimoda: history told with archival material", "https://www.polimoda.com/70-years-ago"), ("UAL / CSM: Louise Wilson story", "https://www.arts.ac.uk/colleges/central-saint-martins/stories/professor-louise-wilson-obe-1962-to-2014")],
           original=True),
])
body += """<div class="aside"><h3>What's left out on purpose</h3><ul>
<li>No count-up student numbers: a small new academy can't win that comparison, and we don't have the numbers.</li>
<li>The PDFs claim "130+ Google ratings, 4.9★". It's a rating, not a testimonial. Show it only if Shruti wants it and it matches her live Google profile.</li></ul></div>"""

JS = """
const cr=document.getElementById('credits');
cr.querySelectorAll('.hov').forEach(h=>{const p=cr.querySelector('.peek[data-k="'+h.dataset.img+'"]');
 const mv=e=>{const r=cr.getBoundingClientRect();p.style.left=Math.min(e.clientX-r.left+16,r.width-140)+'px';p.style.top=(e.clientY-r.top-60)+'px'};
 h.addEventListener('mouseenter',e=>{p.classList.add('on');mv(e)});h.addEventListener('mousemove',mv);h.addEventListener('mouseleave',()=>p.classList.remove('on'));
 h.addEventListener('click',e=>{p.classList.toggle('on');mv(e)});});
"""
page("proof.html", "Proof Strip Options", "02 / 09", "Proof strip",
     "The thin band right under the hero that answers \"why should I trust this place?\" No students or testimonials yet, so these use Shruti's real credentials from her course PDFs, her runway photos and two 2016 press clippings.",
     body, CSS, JS)
