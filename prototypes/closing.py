"""The end of the home page after the five stages: the two courses in short, the studio visit and the footer.

build_home.py inserts SECTION after the stages and adds CSS and JS. The full syllabus lives on its own page.
"""

WA = "https://wa.me/919353562706"

SECTION = f'''
<section class="crs" id="courses" aria-labelledby="crs-h"><div class="wrap">
  <div class="crs-head"><p class="eyebrow">Two courses</p><h2 id="crs-h">Choose how deep <em>you go.</em></h2></div>
  <div class="crs-grid">
    <article class="crs-card"><p class="crs-dur">3<span>months</span></p><p>Measuring, pattern drafting and machine stitching. Kurtas, sleeves, blouses, lehengas and gowns. Finishing, the basics of design, and how to brand and sell your work.</p></article>
    <article class="crs-card"><p class="crs-dur">6<span>months</span></p><p>Everything in the 3-month course, plus more drafts like the katori blouse and fishcut lehenga, aari work with beads and zardozi, boutique management, and a visit to the local fabric market.</p></article>
  </div>
  <div class="crs-foot"><p>Both courses run in the studio on industrial machines. Ask on WhatsApp for fees and the next batch date.</p><a href="#" onclick="return false">Full course details →</a></div>
</div></section>

<section class="vis" id="visit" aria-labelledby="vis-h"><div class="wrap vis-grid">
  <div><p class="eyebrow">Visit the studio</p><h2 id="vis-h">Come and see the machines <em>before you join.</em></h2></div>
  <div class="vis-side">
    <p>Teaching Threads Fashion Academy, Hubballi, Karnataka</p>
    <p>WhatsApp or call <b id="visPhone">93535 62706</b><button type="button" class="vis-copy" id="visCopy">Copy</button></p>
    <a class="btn vis-btn" href="{WA}" target="_blank" rel="noopener">Open WhatsApp</a>
  </div>
</div></section>
<footer class="site-foot"><div class="wrap"><span>Teaching Threads Fashion Academy</span><span>Hubballi, Karnataka</span><span>3D model made with Meshy</span></div></footer>
'''

CSS = """
/* courses in short, the visit band and the footer */
.crs .wrap{display:flex;flex-direction:column;gap:36px;padding-block:96px}
.crs-head{display:flex;flex-direction:column;gap:14px}
.crs-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.crs-card{display:flex;flex-direction:column;gap:14px;padding:28px;border:1px solid var(--ink)}
.crs-dur{font-family:var(--f-display);font-weight:500;font-size:76px;line-height:.9}
.crs-dur span{font-size:28px;font-style:italic;margin-left:8px}
.crs-card p:not(.crs-dur){color:var(--body)}
.crs-foot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:12px 32px;font-size:15px;color:var(--body)}
.crs-foot a{color:var(--ink);font-weight:400;text-underline-offset:4px}
.vis{background:var(--ink);color:var(--paper)}
.vis .eyebrow{color:#A8A49C}
.vis h2{margin-top:14px}
.vis-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:32px 72px;align-items:end;padding-block:96px}
.vis-side{display:flex;flex-direction:column;gap:16px;min-width:0;color:#D6D2CA}
.vis-side b{font-weight:400;color:var(--paper);user-select:all;font-variant-numeric:tabular-nums}
.vis-copy{margin-left:10px;padding:5px 12px;border:1px solid #6B6862;background:transparent;color:var(--paper);font:inherit;font-size:13px;cursor:pointer}
.vis-btn{align-self:flex-start;background:var(--paper);color:var(--ink);border-color:var(--paper)}
.site-foot{background:var(--ink);color:#A8A49C;border-top:1px solid #2E2D2B;font-size:12px;letter-spacing:.14em;text-transform:uppercase}
.site-foot .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px 24px;padding-block:22px 28px}
@media (max-width:900px){
  .crs .wrap,.vis-grid{padding-block:64px}
  .crs-grid,.vis-grid{grid-template-columns:1fr}
  .crs-dur{font-size:62px}
  .crs-card{padding:22px}
}
"""

JS = r"""
(function () {
  const b = document.getElementById('visCopy');
  b.addEventListener('click', () => {
    navigator.clipboard.writeText('+91 93535 62706').then(() => { b.textContent = 'Copied'; setTimeout(() => b.textContent = 'Copy', 1600); }, () => {
      const r = document.createRange(); r.selectNodeContents(document.getElementById('visPhone'));
      const s = getSelection(); s.removeAllRanges(); s.addRange(r);
    });
  });
})();
"""
