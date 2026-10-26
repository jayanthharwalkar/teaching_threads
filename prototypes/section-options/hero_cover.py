"""The chosen hero: magazine cover with the Meshy dress form in front of the masthead, plus tap-to-measure."""
from common import *

CSS = """
.cover{position:relative;height:min(760px,92vh);min-height:620px;overflow:hidden;touch-action:pan-y}
.cover .mast{position:absolute;left:0;right:0;top:26px;text-align:center;font-family:var(--serif);font-size:13cqi;line-height:.8;letter-spacing:-.02em;white-space:nowrap;z-index:0}
.cover .mast small{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.3em;line-height:1;margin:0 0 12px}
.stage3d{position:absolute;inset:0;z-index:1;cursor:grab;touch-action:pan-y}
.stage3d:active{cursor:grabbing}
.stage3d canvas{position:absolute;inset:0;width:100%!important;height:100%!important;display:block;opacity:0;transition:opacity .8s}
.stage3d.ready canvas{opacity:1}
.loading{position:absolute;left:50%;top:55%;transform:translate(-50%,-50%);font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--pencil);z-index:1}
.stage3d.ready+.loading{display:none}
.cl{position:absolute;max-width:21ch;z-index:2;pointer-events:none}
.cl b{display:block;font-family:var(--serif);font-weight:400;font-size:clamp(22px,3.3cqi,34px);line-height:1}
.cl span{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase}
.cover .ctas{position:absolute;left:28px;bottom:28px;z-index:3}
.issue{position:absolute;right:28px;bottom:28px;z-index:3;text-align:right;font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;line-height:1.7}
.hs{position:absolute;z-index:4;transform:translate(-50%,-50%);display:flex;align-items:center;gap:6px;cursor:pointer;background:none;border:0;padding:6px;font:inherit;color:var(--ink);transition:opacity .25s}
.hs i{width:14px;height:14px;border-radius:50%;background:var(--paper);border:1.5px solid var(--ink);display:block;position:relative}
.hs i::after{content:"";position:absolute;inset:3px;border-radius:50%;background:var(--ink)}
.hs span{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;background:var(--paper);padding:2px 5px;border:1px solid var(--rule)}
.hs.on span{background:var(--ink);color:var(--paper)}
.hs.back{opacity:0;pointer-events:none}
.readout{position:absolute;left:50%;bottom:28px;transform:translateX(-50%);z-index:4;background:var(--paper);border:1px solid var(--ink);padding:10px 14px;display:grid;gap:2px;min-width:190px}
.readout b{font-family:var(--serif);font-weight:400;font-size:24px;line-height:1}
.credit{position:absolute;right:28px;top:50%;writing-mode:vertical-rl;font-family:var(--mono);font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--pencil);z-index:2}
@container (max-width:700px){
 .cover{height:auto;min-height:760px}
 .cover .mast{top:20px}
 .cover .mast small{font-size:9px;letter-spacing:.16em}
 .cl.r{display:none}
 .cl.l1{top:auto!important;bottom:250px;left:20px!important}
 .cl.l2{display:none}
 .readout{bottom:150px;left:auto;right:20px;transform:none;min-width:0}
 .cover .ctas{left:20px;right:20px;bottom:20px}
 .issue{display:none}.credit{display:none}
}
"""

MOCK = """<div class="cover" id="cov">
<div class="mast"><small>Fashion Academy · Hubballi · Est. <span class="ph">20__</span></small>TEACHING THREADS</div>
<div class="stage3d" id="stage"></div><div class="loading">Loading the dress form…</div>
<div class="cl l1" style="left:28px;top:33%"><span>The course</span><b>3 &amp; 6 months, from tape to lehenga</b></div>
<div class="cl l2" style="left:28px;top:53%"><span>Your teacher</span><b>Shruti Mahajan, Kerala Fashion League designer</b></div>
<div class="cl r" style="right:44px;top:33%;text-align:right"><span>Inside</span><b>Measure · Draft · Stitch · Blouse · Lehenga</b></div>
<div class="cl r" style="right:44px;top:53%;text-align:right"><span>Plus</span><b>Aari work &amp; boutique management</b></div>
<div class="readout" id="ro"><span class="mono" style="font-size:9.5px;color:var(--pencil)">Your first lesson</span><b>Tap bust, waist or hip</b></div>
<div class="ctas"><span class="btn">Enquire on WhatsApp</span><span class="btn ghost">Book a studio visit</span></div>
<div class="issue">Batch starting <span class="ph">month?</span><br>₹ <span class="ph">fee?</span></div>
<span class="credit">3D model made with Meshy</span>
</div>"""

JS = r"""
const MARKS=[['Bust',.27,'34″'],['Waist',-.05,'28″'],['Hip',-.45,'38″']];
const st=document.getElementById('stage'),ro=document.getElementById('ro');
const R=new THREE.WebGLRenderer({antialias:true,alpha:true});R.setPixelRatio(Math.min(devicePixelRatio,2));R.outputEncoding=THREE.sRGBEncoding;st.appendChild(R.domElement);
const S=new THREE.Scene(),C=new THREE.PerspectiveCamera(24,1,.1,50);
S.add(new THREE.HemisphereLight(0xffffff,0xb9b2a5,.5));const key=new THREE.DirectionalLight(0xffffff,.65);key.position.set(-3,2.5,3);S.add(key);
const rim=new THREE.DirectionalLight(0xffffff,.25);rim.position.set(3,1,-2);S.add(rim);
const mat=new THREE.MeshStandardMaterial({color:0xe6e1d8,roughness:.9,metalness:0});
const form=new THREE.Group();S.add(form);
// our own pole and base, continuing Meshy's stub (radius .034, ends at y -.95)
const pole=new THREE.Mesh(new THREE.CylinderGeometry(.034,.034,.95,32),mat);pole.position.y=-1.4;form.add(pole);
const base=new THREE.Mesh(new THREE.CylinderGeometry(.3,.31,.05,72),mat);base.position.y=-1.87;form.add(base);
const edge=new THREE.Mesh(new THREE.TorusGeometry(.305,.012,8,72),mat);edge.rotation.x=Math.PI/2;edge.position.y=-1.845;form.add(edge);
// tape texture
const cv=document.createElement('canvas');cv.width=2048;cv.height=64;const cx=cv.getContext('2d');cx.fillStyle='#161514';cx.fillRect(0,0,2048,64);cx.fillStyle='#f2efe8';
for(let i=0;i<2048;i+=8)cx.fillRect(i,0,2,i%80?12:(i%40?18:24));cx.font='600 20px monospace';for(let i=80;i<2048;i+=80)cx.fillText(i/80|0,i+5,52);
const tex=new THREE.CanvasTexture(cv);tex.encoding=THREE.sRGBEncoding;tex.anisotropy=4;tex.wrapS=THREE.RepeatWrapping;
let torso,hs=[],tapes={},active=null,grow=0;
function ringAt(y){const rc=new THREE.Raycaster(),out=[];for(let a=0;a<96;a++){const t=a/96*Math.PI*2,dir=new THREE.Vector3(Math.sin(t),0,Math.cos(t));
  rc.set(new THREE.Vector3(0,y,0).addScaledVector(dir,3),dir.clone().negate());const h=rc.intersectObject(torso,true);if(h.length)out.push(h[0].point.addScaledVector(dir,.008));}
 return new THREE.CatmullRomCurve3(out,true)}
function ribbon(y){const pts=ringAt(y).getSpacedPoints(256),N=pts.length,pos=[],uv=[],idx=[];let L=0;
 for(let i=0;i<N;i++){if(i)L+=pts[i].distanceTo(pts[i-1]);const p=pts[i],n=new THREE.Vector3(p.x,0,p.z).normalize().multiplyScalar(.006);
  pos.push(p.x+n.x,p.y-.022,p.z+n.z,p.x+n.x,p.y+.022,p.z+n.z);uv.push(L*1.6,0,L*1.6,1)}
 for(let i=0;i<N-1;i++){const a=i*2;idx.push(a,a+2,a+1,a+1,a+2,a+3)}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(pos,3));g.setAttribute('uv',new THREE.Float32BufferAttribute(uv,2));g.setIndex(idx);
 return new THREE.Mesh(g,new THREE.MeshBasicMaterial({map:tex,side:THREE.DoubleSide}))}
function frontPt(y){const rc=new THREE.Raycaster(new THREE.Vector3(.07,y,3),new THREE.Vector3(0,0,-1));const h=rc.intersectObject(torso,true);return h.length?h[0].point:new THREE.Vector3(.07,y,.2)}
new THREE.GLTFLoader().load('dress-form.glb',g=>{torso=g.scene;torso.traverse(c=>{if(c.isMesh)c.material=mat});form.add(torso);const r0=form.rotation.y;form.rotation.y=0;form.updateMatrixWorld(true);
 MARKS.forEach(([n,y,val])=>{const m=ribbon(y);
  m.geometry.setDrawRange(0,0);form.add(m);tapes[n]=m;
  const p=frontPt(y).add(new THREE.Vector3(0,0,.015));const b=document.createElement('button');b.type='button';b.className='hs';b.innerHTML='<i></i><span>'+n+'</span>';
  b.setAttribute('aria-label','Measure the '+n.toLowerCase());st.parentNode.appendChild(b);hs.push({el:b,p});
  b.addEventListener('pointerdown',e=>e.stopPropagation());
  b.addEventListener('click',()=>{if(active)active.geometry.setDrawRange(0,0);active=m;grow=0;hs.forEach(h=>h.el.classList.toggle('on',h.el===b));
   ro.innerHTML='<span class="mono" style="font-size:9.5px;color:var(--pencil)">Stage 01 · Measure · '+n+'</span><b>'+val+'</b><span class="ph" style="justify-self:start">sample reading</span>'})});
 form.rotation.y=r0;st.classList.add('ready')});
let rot=.45,vel=0,drag=false,lx=0,idle=0;const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
st.addEventListener('pointerdown',e=>{drag=true;lx=e.clientX;idle=0;st.setPointerCapture(e.pointerId)});
st.addEventListener('pointermove',e=>{if(!drag)return;const dx=e.clientX-lx;lx=e.clientX;vel=dx*.008;rot+=vel});
['pointerup','pointercancel'].forEach(t=>st.addEventListener(t,()=>drag=false));
function size(){const w=st.clientWidth,h=st.clientHeight;R.setSize(w,h,false);C.aspect=w/h;
 const narrow=w<700;C.fov=narrow?30:24;C.position.set(0,-.35,narrow?8.2:7.4);C.lookAt(0,narrow?-.62:-.45,0);C.updateProjectionMatrix()}
new ResizeObserver(size).observe(st);size();
const v=new THREE.Vector3(),camDir=new THREE.Vector3();
(function loop(){if(!drag){rot+=vel;vel*=.94;idle++;if(idle>120&&!rm){const t=Math.sin(performance.now()/2600)*.55;rot+=(t-rot)*.01}}
 form.rotation.y=rot;form.updateMatrixWorld();
 if(active&&grow<1){grow=Math.min(1,grow+.045);const n=active.geometry.index.count;active.geometry.setDrawRange(0,Math.floor(grow*n/6)*6)}
 const W=st.clientWidth,H=st.clientHeight;
 hs.forEach(h=>{v.copy(h.p);form.localToWorld(v);const nrm=new THREE.Vector3(v.x,0,v.z).normalize();camDir.copy(C.position).sub(v).normalize();
  h.el.classList.toggle('back',nrm.dot(camDir)<.15);v.project(C);h.el.style.left=((v.x+1)/2*W)+'px';h.el.style.top=((1-v.y)/2*H)+'px'});
 R.render(S,C);requestAnimationFrame(loop)})();
"""

body = f"""
<section class="opt"><div class="mock">{MOCK}</div>
<div class="notes">
 <div><h4>What you see</h4><p>The real Meshy dress form (first try, no texture) standing in front of the TEACHING THREADS masthead, with cover lines explaining the course. Drag to turn it. Tap Bust, Waist or Hip and a tape wraps that line with a reading.</p></div>
 <div><h4>What's ours, not Meshy's</h4><p>Meshy made the torso, knob and a short pole stub. The long pole, round base, clay finish, tape and hotspots are drawn in code, so they're perfectly straight and on-brand.</p></div>
 <div><h4>On mobile</h4><p>Sideways drags turn the form; up-down still scrolls the page. Two cover lines and the price line hide, the reading moves to the right, buttons go full width.</p></div>
</div>
<div class="links"><span class="kicker">File</span><span>dress-form.glb · 45k triangles · 640 KB (480 KB gzipped) · cut down from Meshy's 3.6 MB with no visible loss</span></div>
</section>
<div class="aside"><h3>Still to decide</h3><ul>
<li>Real numbers for the readings, or keep them as illustrative sizes.</li>
<li>A still image of the form to show while the 3D loads (for speed and Google). I can render it from the same model so the swap is invisible.</li>
<li>Credit line: on Meshy's free plan the model is CC BY, so "3D model made with Meshy" has to stay somewhere, the footer is fine.</li></ul></div>
"""

page("hero-cover.html", "Cover Hero", "Hero · chosen", "The cover",
     "Option G with F's measuring, now using the real 3D dress form from Meshy.",
     body, CSS, JS)
p = os.path.join(OUT, "hero-cover.html")
s = open(p).read().replace("<script>", '<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/build/three.min.js"></script>'
                           '<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/examples/js/loaders/GLTFLoader.js"></script><script>', 1)
import base64
glb = base64.b64encode(open(os.path.join(OUT, "assets", "dress-form.glb"), "rb").read()).decode()
s = s.replace("load('dress-form.glb'", "load('data:model/gltf-binary;base64," + glb + "'")  # artifacts can't serve .glb; the site loads the file
open(p, "w").write(s)
