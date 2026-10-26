"""Prototype 08: the chosen cover hero (Meshy dress form) on top of the five-stage course page.

Reads course.html and the hero's CSS/markup/JS from section-options/hero_cover.py, writes home.html.
Run from anywhere: python3 prototypes/build_home.py
"""
import base64, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OPT = os.path.join(HERE, "section-options")

# take CSS, MOCK and JS from the hero option without running its page build
src = open(os.path.join(OPT, "hero_cover.py")).read()
ns = {}
exec(src[src.index('CSS = """'):src.index('body = f"""')], ns)
css, mock, js = ns["CSS"], ns["MOCK"], ns["JS"]

# the hero sits on the course page's type and colours, not the option pages'
css = css.replace(".cover{", ".hero-cover{container-type:inline-size;border-bottom:1px solid var(--line);"
                  "--serif:var(--f-display);--mono:var(--f-body);--pencil:var(--muted);--rule:var(--line);--paper:#F3F1EC}\n.cover{", 1)
css += """
.cover .mast{font-weight:500;font-size:9.4cqi;top:30px}
.cover .cl{max-width:330px}
.cover .ctas{display:flex;gap:8px;flex-wrap:wrap}
.cover .btn{padding:13px 20px;font-size:13px}
.cover .mono{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase}
.cover .ph{font-size:10px;letter-spacing:.06em;color:#9a5b2e;background:#f1e6da;padding:1px 5px;border-radius:2px;text-transform:none}
.cover .cl span,.cover .issue,.cover .hs span{font-weight:400}
@media (prefers-reduced-motion:reduce){.cover *{transition:none!important}}
"""
# split hero: what you'll learn on the left, the dress form on the right, so nothing covers the name in the header
# (credentials are from the course PDFs)
mock = """<div class="wrap">
<div class="copy">
  <p class="eyebrow">Fashion academy · Hubballi</p>
  <h1>Learn to make blouses, kurtas and lehengas <em>with your own hands.</em></h1>
  <p class="lede">3 and 6-month courses with designer Shruti Mahajan, on industrial machines in her studio. You start with a measuring tape and finish with a lehenga you stitched yourself.</p>
  <div class="acts"><a class="btn" href="#" onclick="return false">Enquire on WhatsApp</a><a class="btn ghost" href="#stages">See what you'll learn</a></div>
  <ul class="facts">
    <li><b>15 years</b>as a registered fashion designer</li>
    <li><b>12+ years</b>running her boutique in Hubli-Dharwad</li>
    <li><b>Times of India</b>youngest female entrepreneur award</li>
  </ul>
</div>
<div class="cover" id="cov">
  <div class="stage3d" id="stage"></div><div class="loading">Loading the dress form…</div>
  <div class="readout" id="ro"><span class="mono" style="font-size:9.5px;color:var(--pencil)">Try your first lesson</span><b>Tap bust, waist or hip</b></div>
  <span class="credit">3D model made with Meshy</span>
</div>
</div>"""
css += """
.hero-cover .wrap{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:40px;align-items:center;min-height:calc(100svh - 120px);padding-block:40px}
.hero-cover h1{margin:16px 0 20px;font-family:var(--f-display);font-weight:500;font-size:clamp(42px,5.2vw,76px);line-height:1;text-wrap:balance}
.hero-cover h1 em{font-style:italic}
.hero-cover .lede{margin-bottom:28px}
.hero-cover .acts{display:flex;flex-wrap:wrap;gap:12px}
.facts{list-style:none;margin:40px 0 0;padding:20px 0 0;border-top:1px solid var(--line);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;font-size:13px;line-height:1.4;color:var(--muted)}
.facts b{display:block;font-family:var(--f-display);font-weight:500;font-size:24px;line-height:1.1;color:var(--ink);margin-bottom:4px}
.hero-cover .cover{height:min(700px,82svh);min-height:520px}
.hero-cover .readout{bottom:auto;top:66%;left:50%;right:auto;transform:translateX(-50%);white-space:nowrap}  /* sits across the pole, between torso and base */
.hero-cover .credit{right:0;top:auto;bottom:16px}
@media (max-width:900px){
  .hero-cover .wrap{grid-template-columns:1fr;min-height:0;gap:8px;padding-block:32px 16px}
  .hero-cover .cover{height:520px;min-height:0}
  .facts{gap:12px;margin-top:28px}
  .facts b{font-size:20px}
  .hero-cover .credit{display:none}
  .hero-cover .facts{display:none}  /* phones: the form follows the words; the credentials are in her work below */
}
@media (max-width:480px){.facts{grid-template-columns:1fr;gap:10px}.facts li{display:flex;gap:10px;align-items:baseline}.facts b{margin:0;flex:0 0 7.5em}}
"""

glb = base64.b64encode(open(os.path.join(OPT, "assets", "dress-form.glb"), "rb").read()).decode()
# artifacts can't serve .glb and block fetching data: URLs, so decode the embedded model and parse it; the site loads the file
js = js.replace("new THREE.GLTFLoader().load('dress-form.glb',g=>{",
                "const GLB='" + glb + "';\nnew THREE.GLTFLoader().parse(Uint8Array.from(atob(GLB),c=>c.charCodeAt(0)).buffer,'',g=>{")
js = js.replace("st.classList.add('ready')});",
                "st.classList.add('ready')},e=>{document.querySelector('.cover .loading').textContent='Could not load the dress form';console.error(e)});")
js = js.replace("const narrow=w<700", "const narrow=w<480")  # the form sits in a half-width column here
js = js.replace("C.fov=narrow?30:24;C.position.set(0,-.35,narrow?8.2:7.4);C.lookAt(0,narrow?-.62:-.45,0)",
                "C.fov=24;C.position.set(0,-.35,narrow?7.2:7.4);C.lookAt(0,narrow?-.55:-.45,0)")  # phones: frame the form as close as desktop
assert "narrow?7.2:7.4" in js
# the form only renders while it is on screen, so it never competes with the stages film for the GPU
a = "(function loop(){if(!drag)"
assert a in js and js.count("R.render(S,C);requestAnimationFrame(loop)})();") == 1
js = js.replace(a, "let seen=true,looping=true;new IntersectionObserver(es=>{seen=es[0].isIntersecting;if(seen&&!looping){looping=true;requestAnimationFrame(loop)}}).observe(st);\nfunction loop(){if(!seen){looping=false;return}if(!drag)", 1)
js = js.replace("R.render(S,C);requestAnimationFrame(loop)})();", "R.render(S,C);requestAnimationFrame(loop)}\nloop();", 1)
# on phones the form sits below the words: when it scrolls into view, measure the bust once so people see what tapping does
js += """
if (matchMedia('(max-width: 900px)').matches) {
  const cov = document.getElementById('cov');
  const io = new IntersectionObserver(es => {
    if (!es[0].isIntersecting) return;
    io.disconnect();
    setTimeout(() => { const b = cov.querySelector('.hs'); if (b && !cov.querySelector('.hs.on')) b.click(); }, 900);
  }, { threshold: 0.6 });
  io.observe(cov);
}
"""
assert "GLTFLoader().parse(" in js and "w<480" in js and "Could not load" in js

page = open(os.path.join(HERE, "course.html")).read()
page = re.sub(r'<section class="hero".*?</section>', '<section class="hero-cover" aria-label="Teaching Threads">' + mock + '</section>',
              page, count=1, flags=re.S)
# the full syllabus gets its own page; this page ends with the stages
page = re.sub(r'<section class="syllabus".*?</section>\s*', '', page, count=1, flags=re.S)
page = re.sub(r"  const syl = document.getElementById\('syllabus'\).*?set\('3'\);\n", "", page, count=1, flags=re.S)
# her achievements between the hero and the stages
import achievements
page = page.replace('<section class="stages"', achievements.SECTION + '\n\n<section class="stages"', 1)
css += achievements.CSS
# after the stages: courses in short, the visit band, the footer; the header links point at them
import closing
i = page.index('id="stages"'); j = page.index('</section>', i) + len('</section>')
page = page[:j] + "\n" + closing.SECTION + page[j:]
css += closing.CSS
page = page.replace('<nav class="nav" aria-label="Main"><a href="#" onclick="return false">Courses</a><a href="#" onclick="return false">Your teacher</a><a href="#" onclick="return false">Fees &amp; dates</a><a class="cta" href="#" onclick="return false">WhatsApp us</a></nav>',
                    '<nav class="nav" aria-label="Main"><a href="#stages">The course</a><a href="#ach-h">Her work</a><a href="#courses">Courses</a><a class="cta" href="' + closing.WA + '" target="_blank" rel="noopener">WhatsApp us</a></nav>')
assert 'href="#courses"' in page
page = page.replace('<a class="btn" href="#" onclick="return false">Enquire on WhatsApp</a>', '<a class="btn" href="' + closing.WA + '" target="_blank" rel="noopener">Enquire on WhatsApp</a>', 1)
page = page.replace("Prototype 07 · Hero placeholder + five stages", "Prototype 08 · Home page so far")
page = page.replace("<title>Teaching Threads Course</title>", '<meta charset="utf-8">\n<title>Teaching Threads Home</title>')
page = page.replace("/* Layout: placeholder hero,", "/* Layout: cover hero (3D dress form, tap to measure),")
page = page.replace("</style>", css + "</style>", 1)
page = page.replace("<script>",
                    '<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/build/three.min.js"></script>'
                    '<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/examples/js/loaders/GLTFLoader.js"></script>'
                    "<script>\n(function () {" + js + "})();\n</script>\n<script>" + achievements.JS + closing.JS + "</script>\n<script>", 1)
open(os.path.join(HERE, "home.html"), "w").write(page)
print("wrote home.html", len(page) // 1024, "KB")
