from common import *

PHOTOS["stage5final"] = "prototypes/section-options/stage5-final.jpg"
PHOTOS["blouse"] = "chat gpt images/stage 4.2.png"

CSS = """
.hero{display:grid;grid-template-columns:1fr 1fr;min-height:520px}
.hero .txt{padding:36px 32px;display:flex;flex-direction:column;gap:18px;justify-content:center;position:relative;z-index:2}
@container (max-width:640px){.hero{grid-template-columns:1fr}.hero .txt{padding:26px 20px}}
.stage3d{position:relative;min-height:520px;touch-action:pan-y;cursor:grab;border-left:1px solid var(--rule)}
.stage3d:active{cursor:grabbing}
.stage3d canvas{position:absolute;inset:0;width:100%!important;height:100%!important;display:block}
@container (max-width:640px){.stage3d{min-height:440px;border-left:0;border-top:1px solid var(--rule)}}
.hs{position:absolute;z-index:3;transform:translate(-50%,-50%);display:flex;align-items:center;gap:6px;cursor:pointer;background:none;border:0;padding:0;font:inherit;color:var(--ink)}
.hs i{width:14px;height:14px;border-radius:50%;background:var(--paper);border:1.5px solid var(--ink);display:block;position:relative}
.hs i::after{content:"";position:absolute;inset:3px;border-radius:50%;background:var(--ink)}
.hs span{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;background:var(--paper);padding:2px 5px;border:1px solid var(--rule)}
.hs.on span{background:var(--ink);color:var(--paper)}
.hs.back{opacity:.25;pointer-events:none}
.readout{position:absolute;left:16px;bottom:16px;z-index:3;background:var(--paper);border:1px solid var(--ink);padding:10px 12px;display:grid;gap:2px;min-width:170px}
.readout b{font-family:var(--serif);font-weight:400;font-size:30px;line-height:1}
.drag{position:absolute;right:14px;bottom:14px;z-index:3;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}

.cover{position:relative;min-height:640px;overflow:hidden;touch-action:pan-y}
.cover .mast{position:absolute;left:0;right:0;top:34px;text-align:center;font-family:var(--serif);font-size:13cqi;line-height:.8;letter-spacing:-.02em;white-space:nowrap;z-index:0}
.cover .mast small{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.3em;line-height:1;margin-top:14px}
.cover .stage3d{position:absolute;inset:60px 0 0;border:0;min-height:0;z-index:1}
.cover .lines{position:absolute;inset:0;z-index:2;pointer-events:none;padding:0 28px 28px}
.cover .cl{position:absolute;max-width:22ch}
.cover .cl b{display:block;font-family:var(--serif);font-weight:400;font-size:clamp(22px,3.4cqi,34px);line-height:1}
.cover .cl span{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase}
.cover .ctas{position:absolute;left:28px;bottom:28px;z-index:3}
.cover .cov-ro{left:50%;bottom:28px;transform:translateX(-50%);z-index:4}
.cover .cov-ro b{font-size:22px}
.cover .stage3d .hs{z-index:4}
.cover .issue{position:absolute;right:28px;bottom:28px;z-index:3;text-align:right;font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase}
@container (max-width:640px){.cover .cov-ro{bottom:96px}.cover{min-height:700px}.cover .cl.r{display:none}.cover .ctas{right:20px;left:20px}.cover .issue{display:none}}

.cmpw{position:relative;min-height:520px;overflow:hidden;user-select:none;touch-action:pan-y}
.cmpw .side{position:absolute;inset:0}
.cmpw .side img{width:100%;height:100%;object-fit:cover}
.cmpw .runway{clip-path:inset(0 calc(100% - var(--x,50%)) 0 0);z-index:2}
.cmpw .divider{position:absolute;top:0;bottom:0;left:var(--x,50%);width:0;z-index:3;border-left:2px dashed var(--ink)}
.cmpw .knob{position:absolute;top:50%;left:var(--x,50%);transform:translate(-50%,-50%);z-index:4;width:52px;height:52px;border-radius:50%;background:var(--paper);border:1.5px solid var(--ink);display:grid;place-content:center;font-size:20px;cursor:ew-resize}
.cmpw .tag2{position:absolute;bottom:14px;z-index:4;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;background:var(--paper);padding:5px 8px;border:1px solid var(--rule)}
.cmpw .tag2.l{left:14px}.cmpw .tag2.r{right:14px}

.dress{position:relative;min-height:520px;border-left:1px solid var(--rule)}
.dress figure{position:absolute;inset:0;margin:0;opacity:0;transition:opacity .7s}
.dress figure.on{opacity:1}
.dress figure img{width:100%;height:100%;object-fit:contain;background:#f1efeb}
.steps{display:flex;gap:6px;flex-wrap:wrap}
.steps button{all:unset;cursor:pointer;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--ink);padding:8px 12px;border-radius:999px}
.steps button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.steps button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
.steps-cap{font-size:13px;color:#4a4843;min-height:3em;margin:0}
@container (max-width:640px){.dress{min-height:420px;border-left:0;border-top:1px solid var(--rule)}}

.meshy{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.meshy .aside ol{margin:0;padding-left:18px;display:grid;gap:6px}
.meshy code{font-family:var(--mono);font-size:12.5px;background:var(--chip);padding:1px 5px;border-radius:2px}
.prompt{font-family:var(--mono);font-size:12.5px;line-height:1.55;background:var(--card);border:1px solid var(--line);padding:14px 16px;border-radius:3px;white-space:pre-wrap}
@media (max-width:760px){.meshy{grid-template-columns:1fr}}
"""

TXT = """<span class="eyebrow">Teaching Threads Fashion Academy · Hubballi (Hubli)</span>
<h3 class="h1">{{h1}}</h3><p class="sub">{{sub}}</p>
<div class="ctas"><span class="btn">Enquire on WhatsApp</span><span class="btn ghost">Book a studio visit</span></div>"""

F = f"""<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="hero"><div class="txt">{T(TXT, h1="Every garment starts with a measurement.", sub="Turn the form. Tap bust, waist or hip to take your first measurement. 3- and 6-month fashion design &amp; tailoring courses, taught by designer Shruti Mahajan.")}</div>
<div class="stage3d" id="sF"><div class="readout" id="roF"><span class="mono" style="font-size:9.5px;color:var(--pencil)">Stage 01 · Measure</span><b>Tap a point</b></div><span class="drag">← drag to turn →</span></div></div>"""

G = """<div class="cover" id="cov">
<div class="mast"><small style="margin:0 0 12px">Fashion Academy · Hubballi · Est. <span class="ph">20__</span></small>TEACHING THREADS</div>
<div class="stage3d" id="sG"></div>
<div class="lines">
 <div class="cl" style="left:28px;top:34%"><span>The course</span><b>3 &amp; 6 months, from tape to lehenga</b></div>
 <div class="cl" style="left:28px;top:54%"><span>Your teacher</span><b>Shruti Mahajan, Kerala Fashion League designer</b></div>
 <div class="cl r" style="right:28px;top:34%;text-align:right"><span>Inside</span><b>Measure · Draft · Stitch · Blouse · Lehenga</b></div>
 <div class="cl r" style="right:28px;top:54%;text-align:right"><span>Plus</span><b>Aari work &amp; boutique management</b></div>
</div>
<div class="ctas"><span class="btn">Enquire on WhatsApp</span><span class="btn ghost">Book a studio visit</span></div>
<div class="readout cov-ro" id="roG"><span class="mono" style="font-size:9.5px;color:var(--pencil)">Your first lesson</span><b>Tap bust, waist or hip</b></div>
<div class="issue">Batch starting <span class="ph">month?</span><br>₹ <span class="ph">fee?</span></div>
</div>"""

H = f"""<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="hero"><div class="txt">{T(TXT, h1="From her runway to your first lehenga.", sub="Drag the seam. On the left, Shruti's Forest Fury collection at the Kerala Fashion League, 2016. On the right, what you'll make in her studio.")}</div>
<div class="cmpw" id="cmp" style="border-left:1px solid var(--rule)">
 <div class="side"><img class="clay" src="{img('stage5final', 900)}" alt="Clay lehenga and blouse on a dress form"></div>
 <div class="side runway duo grain"><img src="{img('floral', 900)}" alt="Runway look by Shruti Mahajan"></div>
 <div class="divider"></div><div class="knob" aria-hidden="true">✂</div>
 <span class="tag2 l">Shruti · KFL 2016</span><span class="tag2 r">You · your first lehenga</span>
</div></div>"""

I = f"""<div class="chrome"><b>Teaching Threads</b><span>Courses · Shruti · Visit · FAQ</span></div>
<div class="hero"><div class="txt">{T(TXT, h1="Dress the form.", sub="Three steps from an empty dress form to a full lehenga: the whole course in one picture.")}
<div class="steps" id="steps"><button type="button" aria-pressed="true" data-i="0">01 Measure</button><button type="button" aria-pressed="false" data-i="1">04 Blouse</button><button type="button" aria-pressed="false" data-i="2">05 Lehenga</button></div>
<p class="steps-cap" id="stepcap">Start with an empty form and a tape. Measurement and industrial-machine practice come first.</p></div>
<div class="dress" id="dress">
 <figure class="on"><img src="{img('dressform', 900)}" alt="Bare clay dress form with tape"></figure>
 <figure><img src="{img('blouse', 900)}" alt="Clay blouse being fastened on the form"></figure>
 <figure><img src="{img('stage5final', 900)}" alt="Clay blouse and lehenga on the form"></figure>
</div></div>"""

body = "".join([
    option("F", "Turn the form (3D)", F,
           "A 3D dress form you can drag to turn. Tap Bust, Waist or Hip and a tape wraps around that point with a reading, like the first lesson. This is a stand-in model I built in code; the real one would come from Meshy, matched to our clay dress form.",
           "Rotation alone is a toy. Measuring gives it a reason: the visitor does the first thing a student does. It explains the course by touch.",
           "Only sideways drags turn the form, so the page still scrolls normally. It turns slowly on its own when idle. A still image shows until the 3D loads, and people with reduced motion just get the still.",
           [("Google model-viewer (hotspots, poster, AR)", "https://modelviewer.dev/"), ("model-viewer hotspot examples", "https://modelviewer.dev/examples/annotations/"),
            ("Framer: 3D Hero Builder Pro", "https://www.framer.com/marketplace/components/3d-hero-builder-pro/"), ("thesuperrco.com (drag the line)", "https://thesuperrco.com/")],
           runner=True),
    option("G", "The cover (3D + masthead)", G,
           "Your pick, now with F's measuring built in: tap Bust, Waist or Hip on the central form. A fashion-magazine cover. TEACHING THREADS is set huge as the masthead and the 3D form stands in front of it, overlapping the letters. Cover lines around it explain the offer: course lengths, teacher, stages, extras. Batch date and fee where a magazine puts its price.",
           "Cover lines are the most natural way to explain a lot in a fashion voice. It is the most \"fashion\" of all the hero options and looks like nothing else in Hubballi.",
           "The masthead still spans the screen; two cover lines hide; the form turns on its own.",
           [("Vogue covers archive (masthead behind model)", "https://www.vogue.com/archive"), ("Fonts In Use: Harper's Bazaar masthead", "https://fontsinuse.com/uses/43467/harper-s-bazaar-2021-redesign"),
            ("Codrops: Layered Zoom scroll", "https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/")],
           rec=True, original=True),
    option("H", "Runway ↔ clay slider", H,
           "A before/after slider. Shruti's real runway look on one side, the finished clay lehenga on the other. Drag the stitched seam to wipe between them.",
           "Uses her real photos in the very first screen, and the story is instant: learn from someone who's done this.",
           "Drag the knob; it starts at the middle so both halves show.",
           [("Codrops: dynamic CSS masks", "https://tympanus.net/codrops/2021/05/04/dynamic-css-masks-with-custom-properties-and-gsap/"), ("Awwwards: hero scroll gallery (Martine Rose)", "https://www.awwwards.com/inspiration/hero-scroll-gallery-martine-rose")]),
    option("I", "Dress the form", I,
           "Three buttons, Measure, Blouse, Lehenga. Each one dresses the form a step further. With Meshy, these would be three 3D models (bare, blouse, lehenga) that swap on the same turning form.",
           "The whole course in one picture, and it reuses the stills we already have.",
           "The buttons sit under the image.",
           [("Shopify: 3D product configurators", "https://www.freecodecamp.org/news/how-webgl-and-threejs-power-interactive-online-stores/")]),
])

body += """<div class="aside"><h3>Can Meshy make a dress form this good?</h3>
<p>Mostly yes, and a dress form is close to the easiest thing you could ask it for: one smooth, solid object with no thin parts except the pole. Two things work in our favour. First, our look is plain matte clay-white, so we can throw away Meshy's texture (its weakest part) and light the model with a simple clay material in the browser. Second, the bare form has no fabric folds, which AI 3D still gets wrong.</p>
<p>What to expect it to get wrong: a lumpy or slightly asymmetric torso, a bent or melted stand pole, a soft neck knob, and the draped tape in our still turning into a blob. That's why the tape should be added in code, as it is in the demo, never baked into the model.</p></div>
<div class="meshy">
<div class="aside"><h3>How I'd do it</h3><ol>
<li>Make a clean input image first: the dress form alone, no tape, front three-quarter view, flat light background. Better still, make front, side and back views with ChatGPT and use Meshy's multi-image-to-3D.</li>
<li>Generate with the newest model (Meshy 6, or 7 if your account shows it). Turn texture off, or ignore it.</li>
<li>Remesh to quads for a smooth surface, about 30-50k faces. Smart Topology also works.</li>
<li>Download as GLB. In Blender: straighten the pole (or replace it with a perfect cylinder), mirror the torso for symmetry, smooth shading, then compress to under 2 MB.</li>
<li>On the site: Google's &lt;model-viewer&gt; or three.js, a still poster image first, 3D loaded after the page is ready.</li></ol></div>
<div class="aside"><h3>Cost and licence</h3><ul>
<li>Image-to-3D is about 20-25 credits a try. Budget 4-6 tries for a good one.</li>
<li>The free plan (100 credits a month) is licensed CC BY 4.0, so you'd need to credit Meshy. Pro ($20/month) gives full commercial use. One month of Pro is enough for this.</li>
<li>Check current numbers on <a href="https://www.meshy.ai/pricing" target="_blank" rel="noopener">meshy.ai/pricing</a>; third-party sites disagree.</li></ul>
<h3 style="margin-top:8px">Speed and SEO</h3><ul><li>three.js is about 150 KB plus the model. With a poster image as the first thing on screen, Google sees a normal fast page; the 3D is a bonus on top.</li></ul></div></div>
<div class="aside"><h3>Meshy prompt (if you use text or need to describe the image)</h3>
<div class="prompt">A professional tailor's dress form, female torso with natural bust, waist and hips, smooth matte clay-white surface, a small round knob at the neck, mounted on a single straight vertical pole with a flat round base. Perfectly symmetrical, clean smooth surfaces, no fabric, no tape, no seams, no text. Studio product model, realistic proportions, not cartoon, not stylised.</div>
<p>Negative / avoid: cartoon, toy, chibi, stylised, exaggerated proportions, mannequin head, arms, legs, clothing, tape measure, bent pole, texture noise.</p></div>
"""

JS = r"""
const INK=0x161514;
function makeForm(el,opts){
 opts=opts||{};const R=new THREE.WebGLRenderer({antialias:true,alpha:true});R.setPixelRatio(Math.min(devicePixelRatio,2));
 R.outputEncoding=THREE.sRGBEncoding;el.prepend(R.domElement);
 const S=new THREE.Scene(),C=new THREE.PerspectiveCamera(28,1,.1,50);C.position.set(0,.35,opts.dist||6.4);C.lookAt(0,opts.look||.35,0);
 S.add(new THREE.HemisphereLight(0xffffff,0xb9b2a5,.5));const d=new THREE.DirectionalLight(0xffffff,.62);d.position.set(-3,2.5,3);S.add(d);
 const d2=new THREE.DirectionalLight(0xffffff,.25);d2.position.set(3,1,-2);S.add(d2);
 const mat=new THREE.MeshStandardMaterial({color:0xe6e1d8,roughness:.9,metalness:0});
 const prof=[[0,0],[.34,0],[.39,.03],[.43,.12],[.445,.2],[.43,.3],[.38,.42],[.335,.5],[.34,.58],[.38,.7],[.42,.82],[.43,.9],[.42,.98],[.41,1.06],[.37,1.13],[.27,1.19],[.16,1.23],[.115,1.27],[.11,1.36],[.13,1.38],[0,1.385]];
 const pts=prof.map(p=>new THREE.Vector2(p[0],p[1]));const g=new THREE.LatheGeometry(pts,96);
 const pos=g.attributes.position;
 for(let i=0;i<pos.count;i++){let x=pos.getX(i),y=pos.getY(i),z=pos.getZ(i);z*=.7;
  const sh=Math.max(0,1-Math.abs(y-1.08)/.14);x*=1+.12*sh;
  if(z>0){const b=Math.exp(-((y-.86)**2)/.007)*(Math.exp(-((x-.17)**2)/.01)+Math.exp(-((x+.17)**2)/.01))*.07;z+=b;}
  else{z*=1-.06*Math.exp(-((y-.85)**2)/.05);}
  pos.setXYZ(i,x,y,z);}
 g.computeVertexNormals();
 const form=new THREE.Group();const torso=new THREE.Mesh(g,mat);form.add(torso);
 const knob=new THREE.Mesh(new THREE.CylinderGeometry(.07,.09,.08,40),mat);knob.position.y=1.42;form.add(knob);
 const cap=new THREE.Mesh(new THREE.SphereGeometry(.075,32,16,0,Math.PI*2,0,Math.PI/2),mat);cap.position.y=1.46;form.add(cap);
 const collar=new THREE.Mesh(new THREE.CylinderGeometry(.07,.08,.1,32),mat);collar.position.y=-.05;form.add(collar);
 const pole=new THREE.Mesh(new THREE.CylinderGeometry(.028,.028,1.25,24),mat);pole.position.y=-.7;form.add(pole);
 const base=new THREE.Mesh(new THREE.CylinderGeometry(.36,.38,.05,64),mat);base.position.y=-1.33;form.add(base);
 // centre-front seam and waist tape line, sampled from the surface
 function frontZ(y,x){const rc=new THREE.Raycaster(new THREE.Vector3(x,y,3),new THREE.Vector3(0,0,-1));const h=rc.intersectObject(torso);return h.length?h[0].point.z:0}
 const seam=[];for(let y=.04;y<1.2;y+=.03)seam.push(new THREE.Vector3(0,y,frontZ(y,0)+.004));
 form.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(seam),80,.004,6),new THREE.MeshBasicMaterial({color:INK})));
 function ringAt(y){const rc=new THREE.Raycaster(),out=[];for(let a=0;a<64;a++){const t=a/64*Math.PI*2,dir=new THREE.Vector3(Math.sin(t),0,Math.cos(t));
   rc.set(new THREE.Vector3(0,y,0).addScaledVector(dir,3),dir.clone().negate());const h=rc.intersectObject(torso);if(h.length)out.push(h[0].point.addScaledVector(dir,.012));}
  return new THREE.CatmullRomCurve3(out,true);}
 S.add(form);
 // measuring tape texture
 const cv=document.createElement('canvas');cv.width=1024;cv.height=32;const cx=cv.getContext('2d');cx.fillStyle='#ebe5d3';cx.fillRect(0,0,1024,32);cx.fillStyle='#161514';
 for(let i=0;i<1024;i+=8){cx.fillRect(i,0,1,i%40?8:16)}cx.font='10px monospace';for(let i=0;i<1024;i+=40)cx.fillText(i/40|0,i+2,28);
 const tex=new THREE.CanvasTexture(cv);tex.wrapS=THREE.RepeatWrapping;tex.encoding=THREE.sRGBEncoding;
 const tapes={};let active=null,grow=0;
 function tape(y){if(tapes[y])return tapes[y];const m=new THREE.Mesh(new THREE.TubeGeometry(ringAt(y),128,.02,4,true),new THREE.MeshBasicMaterial({map:tex,side:THREE.DoubleSide}));
  m.geometry.setDrawRange(0,0);form.add(m);tapes[y]=m;return m}
 (opts.marks||[]).forEach(m=>tape(m[1]));
 const hsPts=(opts.marks||[]).map(m=>({x:.06,y:m[1],z:frontZ(m[1],.06)+.02,m}));
 let rot=opts.rot||-.5,vel=0,drag=false,lx=0,idle=0;
 el.addEventListener('pointerdown',e=>{drag=true;lx=e.clientX;idle=0;el.setPointerCapture(e.pointerId)});
 el.addEventListener('pointermove',e=>{if(!drag)return;const dx=e.clientX-lx;lx=e.clientX;vel=dx*.008;rot+=vel});
 el.addEventListener('pointerup',()=>drag=false);el.addEventListener('pointercancel',()=>drag=false);
 const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
 function size(){const w=el.clientWidth,h=el.clientHeight;R.setSize(w,h,false);C.aspect=w/h;C.updateProjectionMatrix()}
 new ResizeObserver(size).observe(el);size();
 const api={form,C,R,el,measure(y){if(active)active.geometry.setDrawRange(0,0);active=tape(y);grow=0},hs:[],hsPts};
 (function loop(){if(!drag){rot+=vel;vel*=.94;idle++;if(idle>120&&!rm){const tgt=Math.sin(performance.now()/2600)*.55;rot+=(tgt-rot)*.01}}form.rotation.y=rot;
  if(active&&grow<1){grow=Math.min(1,grow+.025);active.geometry.setDrawRange(0,Math.floor(grow*active.geometry.index.count/6)*6)}
  api.hs.forEach(h=>{const v=new THREE.Vector3(h.x,h.y,h.z);form.localToWorld(v);const n=v.clone().sub(new THREE.Vector3(0,v.y,0)).normalize();
   const toCam=C.position.clone().sub(v).normalize();const front=n.dot(toCam)>.1;v.project(C);
   h.el.style.left=((v.x+1)/2*el.clientWidth)+'px';h.el.style.top=((1-v.y)/2*el.clientHeight)+'px';h.el.classList.toggle('back',!front)});
  R.render(S,C);requestAnimationFrame(loop)})();
 api.frontZ=frontZ;return api;}

if(window.THREE){
 const marks=[['Bust',.86,'34″'],['Waist',.5,'28″'],['Hip',.2,'38″']];
 function hotspots(id,ro,opts){const st=document.getElementById(id),f=makeForm(st,Object.assign({marks},opts||{}));
  f.hsPts.forEach(p=>{const [n,y,val]=p.m;const b=document.createElement('button');b.type='button';b.className='hs';
   b.innerHTML='<i></i><span>'+n+'</span>';st.appendChild(b);p.el=b;f.hs.push(p);
   b.addEventListener('pointerdown',e=>e.stopPropagation());
   b.addEventListener('click',e=>{e.stopPropagation();f.measure(y);st.querySelectorAll('.hs').forEach(x=>x.classList.toggle('on',x===b));
    ro.innerHTML='<span class="mono" style="font-size:9.5px;color:var(--pencil)">Stage 01 · Measure · '+n+'</span><b>'+val+'</b><span class="ph" style="justify-self:start">sample reading</span>'})});
  return f}
 hotspots('sF',document.getElementById('roF'));
 hotspots('sG',document.getElementById('roG'),{dist:5.6,look:.25,rot:.6});
}
const cmp=document.getElementById('cmp');let cd=false;
function setX(e){const r=cmp.getBoundingClientRect();cmp.style.setProperty('--x',Math.max(4,Math.min(96,(e.clientX-r.left)/r.width*100))+'%')}
cmp.addEventListener('pointerdown',e=>{cd=true;cmp.setPointerCapture(e.pointerId);setX(e)});cmp.addEventListener('pointermove',e=>cd&&setX(e));cmp.addEventListener('pointerup',()=>cd=false);
const caps=['Start with an empty form and a tape. Measurement and industrial-machine practice come first.','Draft, cut and stitch your first blouse: darts, piping, hooks.','Finish with a lehenga, tie the dori, and the form is dressed.'];
document.querySelectorAll('#steps button').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('#steps button').forEach(x=>x.setAttribute('aria-pressed',x===b));
 document.querySelectorAll('#dress figure').forEach((f,i)=>f.classList.toggle('on',i==b.dataset.i));document.getElementById('stepcap').textContent=caps[b.dataset.i]}));
"""

html_head = '<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/build/three.min.js"></script>'
page("hero2.html", "Hero Options Round 2", "01b / 09", "Hero, round 2",
     "Four stronger hero ideas built around the dress form itself. F and G use a working 3D dress form (drag it). It's a rough stand-in I modelled in code to show the interaction; Meshy would give the real one, matched to the clay form in the course section. Notes on Meshy are at the bottom.",
     body, CSS, JS)
p = os.path.join(OUT, "hero2.html")
s = open(p).read().replace("<script>", html_head + "<script>", 1)
open(p, "w").write(s)
