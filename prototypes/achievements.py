"""Achievements gallery for the home page: one draggable row of tall cards, each opening with its story.

build_home.py inserts SECTION between the hero and the stages, and adds CSS and JS.
"""
import base64, io, os
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# file, crop (l,t,r,b fractions) or None, card focus (object-position), kicker, title, story
ITEMS = [
    ("photos/Header Pic.jpg.jpeg", None, "62% 50%", "Kerala Fashion League · 2016", "Forest Fury on the ramp in Kochi",
     "Shruti showed her collection Forest Fury at the Kerala Fashion League, one of the biggest fashion events in South India, alongside more than 20 designers from across the country. Her name is on the screen behind the line-up."),
    ("photos/Show 1.jpg.jpeg", (0.015, 0.178, 0.985, 0.99), "50% 30%", "Her label · Kochi, 2016", "Shruti Mahajans Designer Wear",
     "Shruti (right) takes her bow on the KFL ramp beside her model in a floral lehenga from the collection."),
    ("photos/IMG-20160306-WA0002.jpg.jpeg", None, "50% 30%", "Forest Fury · 2016", "Made from upholstery fabric",
     "Every look in Forest Fury was cut from upholstery fabric, the kind used for curtains and sofas. Actress Radhika Chetan wore one of the designs on the ramp."),
    ("photos/IMG-20160316-WA0003.jpg.jpeg", None, "50% 40%", "Deccan Herald · 2016", "“Hubballi designer shines at Kerala Fashion League”",
     "The Deccan Herald covered the show. Shruti told them: “These kind of events helped to understand the fashion industry, which is not taught by the books.”"),
    ("photos/IMG-20160313-WA0005.jpg.jpeg", None, "40% 50%", "Kannada press · 2016", "In the Kannada papers too",
     "The Kerala Fashion League show was also covered in the Kannada press, with Shruti photographed between her two models."),
    ("photos/IMG-20160424-WA0035.jpg.jpeg", None, "50% 40%", "On the ramp", "Walking out with her model",
     "Shruti walks the ramp with her model at the end of a show. Designers only walk out at the end, to take the applause for the collection."),
    (None, None, None, "Recognition", "Youngest female entrepreneur, Times of India",
     "The Times of India named Shruti its youngest female entrepreneur. Today she has 15 years in fashion and has run her own boutique in Hubli-Dharwad for more than 12."),
]


def uri(path, crop):
    im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, path))).convert("RGB")
    if crop:
        W, H = im.size
        im = im.crop((int(crop[0] * W), int(crop[1] * H), int(crop[2] * W), int(crop[3] * H)))
    im.thumbnail((1000, 1000))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


cards = []
for i, (path, crop, focus, kicker, title, story) in enumerate(ITEMS):
    num = f"{i + 1:02d}"
    if path:
        face = f'<img src="{uri(path, crop)}" alt="{title}" style="object-position:{focus}" draggable="false">'
    else:
        face = f'<div class="ach-type"><b>{title}</b></div>'
    cards.append(f'''<li><button type="button" class="ach-card" data-k="{kicker}" data-t="{title}" data-s="{story}" aria-label="{title}: open the story">
  {face}<span class="ach-cap"><span>{num}</span>{kicker}</span></button></li>''')

SECTION = f'''<section class="ach" aria-labelledby="ach-h">
  <div class="wrap ach-head">
    <div><p class="eyebrow">Shruti's work</p><h2 id="ach-h">On the ramp, <em>in the papers.</em></h2></div>
    <p class="ach-hint">Drag to look through · tap a photo for its story</p>
  </div>
  <div class="ach-rail" id="achRail"><ul class="ach-row">{"".join(cards)}</ul></div>
  <div class="wrap"><div class="ach-prog"><i id="achProg"></i></div></div>
</section>
<div class="ach-lb" id="achLb" hidden role="dialog" aria-modal="true" aria-labelledby="achLbT">
  <button type="button" class="ach-x" id="achX" aria-label="Close">×</button>
  <div class="ach-lb-in">
    <div class="ach-lb-pic" id="achLbPic"></div>
    <div class="ach-lb-txt"><p class="eyebrow" id="achLbK"></p><h3 id="achLbT"></h3><p id="achLbS"></p>
      <div class="ach-lb-nav"><button type="button" id="achPrev" aria-label="Previous">←</button><span id="achN"></span><button type="button" id="achNext" aria-label="Next">→</button></div></div>
  </div>
</div>'''

CSS = """
/* achievements: one row of tall cards, dragged sideways; a card opens with its story */
.ach{border-bottom:1px solid var(--line);padding-block:88px 72px}
.ach-head{display:flex;justify-content:space-between;align-items:flex-end;gap:16px 32px;flex-wrap:wrap;margin-bottom:36px}
.ach-hint{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.ach-rail{overflow-x:auto;scrollbar-width:none;cursor:grab;overscroll-behavior-x:contain}
.ach-rail::-webkit-scrollbar{display:none}
.ach-rail.drag{cursor:grabbing}
.ach-row{list-style:none;margin:0;display:flex;gap:clamp(12px,1.6vw,20px);width:max-content;
  padding-left:max(16px,env(safe-area-inset-left,0px),calc((100vw - 1240px) / 2 + 16px));padding-right:max(16px,env(safe-area-inset-right,0px),calc((100vw - 1240px) / 2 + 16px))}
.ach-card{display:block;position:relative;width:clamp(230px,24vw,330px);aspect-ratio:3/4.4;padding:0;border:0;background:var(--studio);cursor:pointer;overflow:hidden;
  transform:skewX(var(--sk,0deg)) scale(var(--sc,1));transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.ach-rail.drag .ach-card{cursor:grabbing}
.ach-card img{width:100%;height:100%;object-fit:cover;display:block;pointer-events:none;user-select:none;transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.ach-card:hover img,.ach-card:focus-visible img{transform:scale(1.05)}
.ach-cap{position:absolute;left:0;right:0;bottom:0;display:flex;gap:10px;padding:40px 14px 12px;background:linear-gradient(transparent,rgba(10,10,10,.72));color:#F3F1EC;
  font-size:11px;letter-spacing:.14em;text-transform:uppercase;text-align:left}
.ach-cap span{opacity:.6}
.ach-type{position:absolute;inset:0;background:var(--ink);color:var(--paper);display:flex;align-items:center;padding:24px;text-align:left}
.ach-type b{font-family:var(--f-display);font-weight:500;font-size:clamp(30px,2.8vw,40px);line-height:1}
.ach-prog{height:1px;background:var(--line);margin-top:28px;position:relative}
.ach-prog i{position:absolute;left:0;top:-1px;height:3px;width:20%;background:var(--ink)}
.ach-lb{position:fixed;inset:0;z-index:40;background:var(--paper);overflow-y:auto;
  padding:calc(64px + env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) calc(32px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px))}
.ach-lb[hidden]{display:none}
.ach-lb-in{max-width:1180px;margin:0 auto;min-height:100%;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:32px 56px;align-items:center}
.ach-lb-pic{height:min(78vh,820px);display:flex;align-items:center;justify-content:center;background:var(--studio)}
.ach-lb-pic img{max-width:100%;max-height:100%;object-fit:contain;display:block}
.ach-lb-pic .ach-type{position:static;width:100%;height:100%}
.ach-lb-txt{display:flex;flex-direction:column;gap:16px;min-width:0}
.ach-lb-txt h3{margin:0;font-family:var(--f-display);font-weight:500;font-size:clamp(32px,3.4vw,48px);line-height:1;text-wrap:balance}
.ach-lb-txt p:not(.eyebrow){color:var(--body);max-width:30em}
.ach-lb-nav{display:flex;align-items:center;gap:14px;margin-top:12px;font-size:13px;letter-spacing:.14em;color:var(--muted)}
.ach-lb-nav button,.ach-x{width:44px;height:44px;border-radius:50%;border:1px solid var(--ink);background:transparent;color:var(--ink);cursor:pointer;font:inherit;font-size:18px}
.ach-x{position:fixed;top:calc(14px + env(safe-area-inset-top,0px));right:calc(14px + env(safe-area-inset-right,0px));font-size:22px;background:var(--paper)}
@media (max-width:900px){
  .ach{padding-block:64px 56px}
  .ach-head{margin-bottom:24px}
  .ach-lb-in{grid-template-columns:1fr;align-items:start;gap:24px}
  .ach-lb-pic{height:auto;max-height:62vh;aspect-ratio:4/5}
}
@media (max-width:640px){.ach-card{width:72vw}}
@media (prefers-reduced-motion:reduce){.ach-card,.ach-card img{transition:none;transform:none!important}}
"""

JS = r"""
(function () {
  const rail = document.getElementById('achRail'), cards = [...rail.querySelectorAll('.ach-card')], prog = document.getElementById('achProg');
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // the cards lean with the speed of the row and settle when it stops
  let last = rail.scrollLeft, settle = 0;
  function onScroll() {
    const dx = rail.scrollLeft - last; last = rail.scrollLeft;
    const max = rail.scrollWidth - rail.clientWidth, k = max > 0 ? rail.scrollLeft / max : 0;
    prog.style.width = (20 + 80 * k) + '%';
    if (calm) return;
    const sk = Math.max(-5, Math.min(5, -dx * 0.25));
    cards.forEach(c => { c.style.setProperty('--sk', sk.toFixed(2) + 'deg'); c.style.setProperty('--sc', (1 - Math.min(0.04, Math.abs(dx) * 0.002)).toFixed(3)); });
    clearTimeout(settle);
    settle = setTimeout(() => cards.forEach(c => { c.style.setProperty('--sk', '0deg'); c.style.setProperty('--sc', '1'); }), 90);
  }
  rail.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // mouse drag with a little momentum (touch scrolls natively)
  let drag = null, moved = false, vel = 0;
  rail.addEventListener('pointerdown', e => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    drag = { x: e.clientX, s: rail.scrollLeft, lx: e.clientX }; moved = false; vel = 0;
  });
  addEventListener('pointermove', e => {
    if (!drag) return;
    const dx = e.clientX - drag.x;
    if (Math.abs(dx) > 5) { moved = true; rail.classList.add('drag'); }
    vel = e.clientX - drag.lx; drag.lx = e.clientX;
    rail.scrollLeft = drag.s - dx;
  });
  addEventListener('pointerup', () => {
    if (!drag) return;
    drag = null; rail.classList.remove('drag');
    (function glide() { if (Math.abs(vel) < 0.5 || calm) return; rail.scrollLeft -= vel; vel *= 0.92; requestAnimationFrame(glide); })();
  });

  // open a card with its story
  const lb = document.getElementById('achLb'), pic = document.getElementById('achLbPic'), K = document.getElementById('achLbK'),
    T = document.getElementById('achLbT'), S = document.getElementById('achLbS'), N = document.getElementById('achN'), X = document.getElementById('achX');
  let cur = 0, opener = null;
  function show(i) {
    cur = (i + cards.length) % cards.length;
    const c = cards[cur], im = c.querySelector('img');
    pic.innerHTML = im ? '<img src="' + im.src + '" alt="' + im.alt.replace(/"/g, '&quot;') + '">' : c.querySelector('.ach-type').outerHTML;
    K.textContent = c.dataset.k; T.textContent = c.dataset.t; S.textContent = c.dataset.s;
    N.textContent = String(cur + 1).padStart(2, '0') + ' / ' + String(cards.length).padStart(2, '0');
  }
  function close() { lb.hidden = true; document.documentElement.style.overflow = ''; if (opener) opener.focus(); }
  cards.forEach((c, i) => c.addEventListener('click', e => {
    if (moved) { moved = false; e.preventDefault(); return; }
    opener = c; show(i); lb.hidden = false; document.documentElement.style.overflow = 'hidden'; X.focus();
  }));
  X.addEventListener('click', close);
  document.getElementById('achPrev').addEventListener('click', () => show(cur - 1));
  document.getElementById('achNext').addEventListener('click', () => show(cur + 1));
  addEventListener('keydown', e => {
    if (lb.hidden) return;
    if (e.key === 'Escape') close(); else if (e.key === 'ArrowLeft') show(cur - 1); else if (e.key === 'ArrowRight') show(cur + 1);
  });
})();
"""
