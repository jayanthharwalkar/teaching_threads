from common import *

CSS = """
.cmp{display:grid;grid-template-columns:200px 1fr;gap:1px;background:var(--rule)}
.cmp>div{background:var(--paper);padding:20px;display:grid;gap:8px;align-content:start}
.cmp .orig img{width:100%;aspect-ratio:3/4;object-fit:cover}
.cmp .cap{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}
.cmp .res{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.cmp .res .duo,.cmp .res canvas{width:100%;aspect-ratio:3/4;display:block}
.ctrl{display:flex;gap:12px;align-items:center;flex-wrap:wrap;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}
.ctrl input{width:150px;accent-color:#161514}
@container (max-width:620px){.cmp{grid-template-columns:1fr}.cmp .orig img{max-width:160px}}
.sheet{padding:26px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;background:#efede6}
.sheet .duo{aspect-ratio:3/4;position:relative}
.sheet b{position:absolute;left:5px;bottom:4px;font-family:var(--mono);font-size:9px;font-weight:400;z-index:2;background:var(--paper);padding:0 3px}
.sheet .circ::before{content:"";position:absolute;inset:8% 6%;border:2.5px solid #b0472f;border-radius:50%;z-index:3;transform:rotate(-8deg)}
.sheet .x::before{content:"✕";position:absolute;right:6px;top:2px;z-index:3;color:#b0472f;font-size:22px}
@container (max-width:520px){.sheet{grid-template-columns:repeat(3,1fr)}}
.hl{padding:30px 28px;position:relative;min-height:400px}
.hl ul{list-style:none;margin:0;padding:0}
.hl li{font-family:var(--serif);font-size:clamp(28px,5cqi,46px);line-height:1.1;border-bottom:1px solid var(--rule);padding:8px 0;display:flex;justify-content:space-between;align-items:baseline;cursor:pointer;transition:padding .3s}
.hl li:hover,.hl li.on{padding-left:14px}
.hl li span{font-family:var(--mono);font-size:10px;letter-spacing:.1em;color:var(--pencil)}
.hl .peek{position:absolute;right:8%;top:50%;width:min(210px,40%);aspect-ratio:3/4;transform:translateY(-50%) rotate(3deg);opacity:0;transition:opacity .25s}
.hl .peek.on{opacity:1}
.film{background:#1b1a18;padding:18px 0;overflow:hidden}
.film .track{display:flex;gap:6px;width:max-content;animation:slide 36s linear infinite}
@keyframes slide{to{transform:translateX(-50%)}}
.cell{width:170px;padding:16px 0;position:relative;flex:none}
.cell::before,.cell::after{content:"";position:absolute;left:0;right:0;height:9px;background:repeating-linear-gradient(90deg,transparent 0 6px,#f5f4f0 6px 14px,transparent 14px 20px)}
.cell::before{top:3px}.cell::after{bottom:3px}
.cell .duo{aspect-ratio:3/4}
.ptype{padding:30px 24px;display:grid;gap:10px}
.ptype .t{font-family:"Anton",sans-serif;font-size:clamp(70px,19cqi,190px);line-height:.82;background-size:cover;background-position:center 35%;-webkit-background-clip:text;background-clip:text;color:transparent;filter:grayscale(1) contrast(1.35)}
.tools{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.tools div{border:1px solid var(--line);background:var(--card);padding:14px;border-radius:3px;font-size:13.5px}
.tools b{display:block;font-family:var(--serif);font-weight:400;font-size:21px}
@media (max-width:720px){.tools{grid-template-columns:1fr}}
"""

def cmp(orig_key, cap, right, ctrl=""):
    return f"""<div class="cmp"><div class="orig"><span class="cap">Original (WhatsApp JPEG)</span><img src="{img(orig_key, 400)}" alt="Original photo"></div>
<div><span class="cap">{cap}</span><div class="res">{right}</div>{ctrl}</div></div>"""

A = cmp("cape", "Halftone, two dot sizes", '<canvas class="ht" data-src="cape" data-step="7"></canvas><canvas class="ht" data-src="trio" data-step="5"></canvas>',
        '<label class="ctrl">Dot size <input type="range" min="3" max="14" value="7" id="htStep"></label>')
B = cmp("floral", "Ink duotone + grain", f'<div class="duo grain" id="g1"><img src="{img("floral", 500)}" alt=""></div><div class="duo grain" id="g2"><img src="{img("cape", 500)}" alt=""></div>',
        '<label class="ctrl">Grain <input type="range" min="0" max="40" value="14" id="grainR"></label>')
sheet_keys = [("cape", "FF-01", ""), ("trio", "FF-02", "x"), ("curly", "FF-03", ""), ("lineup", "FF-04", ""), ("floral_blue", "FF-05", ""), ("floral", "FF-06", "circ"), ("walk", "FF-07", ""), ("brand", "FF-08", "")]
C = '<div class="sheet">' + "".join(f'<div class="duo grain {c}"><img src="{img(k, 280)}" alt=""><b>{n}</b></div>' for k, n, c in sheet_keys) + "</div>"
D = cmp("floral", "Rough cut-out: dark background keyed to paper", '<canvas class="ko" data-src="floral"></canvas><canvas class="ko" data-src="floral_blue"></canvas>',
        '<label class="ctrl">Key threshold <input type="range" min="10" max="90" value="38" id="koT"></label><span class="ctrl">Real version: Photoroom / Clipdrop</span>')
looks = [("Forest Fury cape", "cape"), ("Night gown, gold leaf", "trio"), ("Floral column", "floral_blue"), ("Garden lehenga", "floral")]
E = '<div class="hl" id="hl"><ul>' + "".join(f'<li data-k="{k}">{n}<span>FF-0{i + 1}</span></li>' for i, (n, k) in enumerate(looks)) + "</ul>"
E += "".join(f'<div class="peek duo grain" data-k="{k}"><img src="{img(k, 400)}" alt=""></div>' for _, k in looks) + "</div>"
cells = "".join(f'<div class="cell"><div class="duo grain"><img src="{img(k, 280)}" alt=""></div></div>' for k, _, _ in sheet_keys)
F = f'<div class="film"><div class="track">{cells * 2}</div></div>'
G = f'<div class="ptype"><span class="eyebrow">Shruti Mahajan · Kerala Fashion League 2016</span><div class="t" style="background-image:url({img("cape", 900)})">FOREST<br>FURY</div></div>'

body = "".join([
    option("A", "Halftone / dither", A,
           "The photo rebuilt from black dots on off-white, like newsprint or a cross-stitch chart. Drag the dot size.",
           "The eye stops looking for detail, so low resolution disappears. The dots read as embroidery.",
           "Fine; bigger dots on small screens.",
           [("Frontend Masters: CSS halftone in 3 declarations", "https://frontendmasters.com/blog/pure-css-halftone-effect-in-3-declarations/"), ("Lean Rada: CSS halftone", "https://leanrada.com/notes/pure-css-halftone/"),
            ("Codrops: dithering shader", "https://tympanus.net/codrops/?p=95318")],
           runner=True),
    option("B", "Ink duotone + grain", B,
           "Shadows become the site's ink, highlights become its paper, with a light film grain on top. Drag the grain.",
           "Removes the noisy WhatsApp colour, and the dark runway backgrounds melt into the page. Grain hides JPEG blocks. Keep grain between 3% and 12%; above 15% it looks like dirt.",
           "Fine, it's just CSS.",
           [("Codrops: duotone with feComponentTransfer", "https://tympanus.net/codrops/?p=37611"), ("José M. Pérez: duotone", "https://jmperezperez.com/duotone-using-fecolormatrix/"),
            ("CSS-Tricks: grainy gradients", "https://css-tricks.com/?p=351302")],
           rec=True),
    option("C", "Contact sheet / small prints", C,
           "Eight looks at thumbnail size with frame numbers, one circled and one crossed out in grease pencil, like a designer editing a shoot.",
           "Small photos always look sharp, and the marks make it feel like an archive.",
           "Three per row.",
           [("Evagria portfolio", "https://uiuxshowcase.com/portfolio/evagria-portfolio/")]),
    option("D", "Cut-out on off-white", D,
           "The model lifted off the black runway and placed on paper, matching the clay objects. This preview is a rough brightness key; the real version uses a background remover.",
           "Removes the dark background completely, so runway and clay share one world.",
           "Fine. Risk: black garments on black backgrounds give poor edges, so test the cape look first.",
           [("Photoroom API", "https://docs.photoroom.com"), ("Dupple: AI background removers 2026", "https://dupple.com/learn/best-ai-background-removers")]),
    option("E", "Hover-reveal list", E,
           "Look names set as a big typeset list. Hover one to reveal its inked photo.",
           "Type leads and photos are a small reward, so their quality never matters.",
           "Tap a name; or show a small thumbnail beside each.",
           [("Codrops: menu image on hover", "https://tympanus.net/codrops/2020/07/01/creating-a-menu-image-animation-on-hover/"), ("Codrops: Image Trail Effects", "https://tympanus.net/codrops/2019/08/07/image-trail-effects")]),
    option("F", "Film strip", F,
           "35&nbsp;mm frames with sprocket holes drifting sideways.",
           "Reads as a runway roll; frames stay small.",
           "Swipe row with snap.",
           [("Codrops: infinite GSAP scroll gallery", "https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/")]),
    option("G", "Photo inside type", G,
           "\"FOREST FURY\" in a heavy condensed face, filled with the cape photo.",
           "Dark, busy photos make great type fills, and nobody judges resolution inside letters.",
           "Two lines, still huge.",
           [("Codrops: animated text fills", "https://tympanus.net/codrops/2015/02/16/create-animated-text-fills/")],
           original=True),
])
body += """<div class="aside"><h3>Before any treatment: clean-up</h3><p>Use a fidelity upscaler gently (2x). Avoid creative upscalers: they invent faces and embroidery, which would misrepresent Shruti's collection.</p></div>
<div class="tools">
<div><b>Upscayl (Real-ESRGAN)</b>Free. Good with JPEG artefacts. Try first at 2x. <a href="https://www.krea.ai/blog/best-ai-image-upscalers-in-2026" target="_blank" rel="noopener">Krea comparison ↗</a></div>
<div><b>Topaz Photo AI</b>Paid, faithful. Use if Upscayl isn't enough. <a href="https://rangy.ai/blog/topaz-vs-magnific-vs-crystal" target="_blank" rel="noopener">Topaz vs Magnific ↗</a></div>
<div><b>Avoid: Magnific, Krea high creativity, face restore</b>They change faces and garments. Only with Shruti's approval.</div></div>"""

SRC = {k: img(k, 500) for k in ["cape", "trio", "floral", "floral_blue"]}
JS = """
const SRC=__SRC__;const PAPER=[245,244,240],INK=[22,21,20];
function load(k){return new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=SRC[k]})}
async function halftone(c,step){const im=await load(c.dataset.src);const W=360,H=480;c.width=W;c.height=H;const x=c.getContext('2d');
 const o=document.createElement('canvas');o.width=W;o.height=H;const ox=o.getContext('2d');const s=Math.max(W/im.width,H/im.height);
 ox.drawImage(im,(W-im.width*s)/2,(H-im.height*s)/2,im.width*s,im.height*s);const d=ox.getImageData(0,0,W,H).data;
 x.fillStyle='rgb('+PAPER+')';x.fillRect(0,0,W,H);x.fillStyle='rgb('+INK+')';
 for(let y=0;y<H;y+=step)for(let X=((y/step)%2?step/2:0);X<W;X+=step){const i=((y|0)*W+(X|0))*4;const l=(d[i]*.3+d[i+1]*.59+d[i+2]*.11)/255;
  const r=(1-l)*step*.62;if(r>.3){x.beginPath();x.arc(X,y,r,0,7);x.fill()}}}
const hts=[...document.querySelectorAll('canvas.ht')];hts.forEach(c=>halftone(c,+c.dataset.step));
document.getElementById('htStep').addEventListener('input',e=>hts.forEach((c,i)=>halftone(c,+e.target.value-(i?2:0)||3)));
document.getElementById('grainR').addEventListener('input',e=>{document.querySelectorAll('#g1,#g2').forEach(g=>g.style.setProperty('--g',e.target.value/100))});
async function key(c,t){const im=await load(c.dataset.src);const W=360,H=480;c.width=W;c.height=H;const x=c.getContext('2d');const s=Math.max(W/im.width,H/im.height);
 x.drawImage(im,(W-im.width*s)/2,(H-im.height*s)/2,im.width*s,im.height*s);const id=x.getImageData(0,0,W,H),d=id.data;
 for(let i=0;i<d.length;i+=4){const l=(d[i]*.3+d[i+1]*.59+d[i+2]*.11);const g=l;const a=Math.min(1,Math.max(0,(l-t)/22));
  const gg=Math.min(255,g*1.05);for(let j=0;j<3;j++)d[i+j]=PAPER[j]*(1-a)+(gg/255*PAPER[j]+(1-gg/255)*INK[j])*a}x.putImageData(id,0,0)}
const kos=[...document.querySelectorAll('canvas.ko')];kos.forEach(c=>key(c,38));
document.getElementById('koT').addEventListener('input',e=>kos.forEach(c=>key(c,+e.target.value)));
const hl=document.getElementById('hl');hl.querySelectorAll('li').forEach(li=>{const p=hl.querySelector('.peek[data-k="'+li.dataset.k+'"]');
 const on=()=>{hl.querySelectorAll('.peek,li').forEach(z=>z.classList.remove('on'));p.classList.add('on');li.classList.add('on')};
 li.addEventListener('mouseenter',on);li.addEventListener('click',on)});hl.querySelector('li').dispatchEvent(new Event('mouseenter'));
"""
JS = JS.replace("__SRC__", "{" + ",".join(f'"{k}":"{v}"' for k, v in SRC.items()) + "}")
CSS += ".duo.grain::after{opacity:var(--g,.14)}"
page("photos.html", "Runway Photo Treatments", "Photos", "Photo treatments",
     "Shruti's 2016 runway photos are dark, low-res WhatsApp JPEGs. Making them bigger doesn't work. Each treatment below changes what the image is (dots, ink, grain, small prints) so the resolution stops mattering. All of these use her real photos.",
     body, CSS, JS, extra_fonts=FONTS + "&family=Anton")
