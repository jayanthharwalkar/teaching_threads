from common import *

PHONE = "93535 62706"

CSS = """
.fa{padding:40px 0 0;display:grid;gap:26px;overflow:hidden}
.fa .cta{padding:0 28px;display:flex;justify-content:space-between;align-items:end;gap:18px;flex-wrap:wrap}
.fa .stitch{height:10px;margin:0 28px}
.fa .stitch path{stroke:var(--ink);stroke-width:2;stroke-dasharray:10 7;fill:none;animation:run 1.6s linear infinite}
@keyframes run{to{stroke-dashoffset:-34}}
.fa .util{padding:0 28px;display:flex;flex-wrap:wrap;gap:8px 24px;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.ruler{height:22px;border-top:1px solid var(--ink);background:repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 10px) 0 0/100% 8px no-repeat,repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 50px) 0 0/100% 16px no-repeat}
.word{font-family:var(--serif);font-size:12.2cqi;line-height:.74;letter-spacing:-.02em;white-space:nowrap;margin:0 0 -2.2cqi -.6cqi}

.nl{padding:40px 24px;display:grid;gap:22px;justify-items:center}
.neck{width:min(620px,100%);background:#161514;color:#f2efe8;padding:26px 30px;position:relative;text-align:center;display:grid;gap:6px;
  clip-path:polygon(0 0,100% 0,96% 50%,100% 100%,0 100%,4% 50%)}
.neck .w{font-family:var(--serif);font-size:clamp(34px,6.4cqi,56px);line-height:.95}
.neck .m{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;opacity:.85}
.neck .ic{display:flex;gap:16px;justify-content:center;margin-top:8px}
.neck .ic span{font-family:var(--mono);font-size:10px;letter-spacing:.1em;border:1px solid #f2efe8;padding:4px 7px;border-radius:2px}
.cutrow{position:relative;width:min(620px,100%);height:30px}
.cutrow .line{position:absolute;left:0;right:0;top:50%;border-top:1.5px dashed var(--ink)}
.cutrow .k{position:absolute;top:50%;left:0;font-size:24px;transform:translate(-50%,-55%);transition:left 1.2s cubic-bezier(.5,0,.3,1)}
.cutrow.cut .k{left:100%}
.cutrow .done{position:absolute;left:0;top:50%;height:2px;background:var(--paper);width:0;transition:width 1.2s cubic-bezier(.5,0,.3,1);transform:translateY(-1px)}
.cutrow.cut .done{width:100%}

.chit2{padding:38px 24px;display:flex;justify-content:center}
.torn{width:min(520px,100%);background:#fbfaf6;border:1px solid #cfc9bc;padding:24px 24px 26px;display:grid;gap:14px;position:relative;
  -webkit-mask:linear-gradient(#000,#000) top/100% calc(100% - 10px) no-repeat,radial-gradient(circle at 7px 0,transparent 6px,#000 6.5px) bottom/14px 10px repeat-x;
  mask:linear-gradient(#000,#000) top/100% calc(100% - 10px) no-repeat,radial-gradient(circle at 7px 0,transparent 6px,#000 6.5px) bottom/14px 10px repeat-x}
.torn h6{margin:0;font-family:var(--serif);font-weight:400;font-size:30px;line-height:1}
.torn .f{display:grid;grid-template-columns:70px 1fr;align-items:end;gap:10px}
.torn label{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--pencil)}
.torn input,.torn select{font:inherit;font-family:var(--hand);font-size:22px;border:0;border-bottom:1px solid var(--ink);background:transparent;color:var(--ink);padding:0 2px;width:100%}
.torn input:focus,.torn select:focus{outline:none;border-bottom-width:2px}
.msg{background:#e6f2df;border-radius:10px 10px 10px 2px;padding:12px 14px;font-size:14px;line-height:1.45;color:#1d2b17}
.msg small{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#4d6343;margin-bottom:4px}

.phonebox{padding:30px;display:flex;justify-content:center;gap:40px;flex-wrap:wrap;align-items:center}
.phone{width:250px;height:470px;border:9px solid #161514;border-radius:34px;position:relative;overflow:hidden;background:var(--paper)}
.phone .scr{position:absolute;inset:0;overflow-y:auto;padding:16px 14px 70px;display:grid;gap:12px;align-content:start}
.phone .blk{background:#e8e5dd;border-radius:3px}
.phone .bar{position:absolute;left:0;right:0;bottom:0;display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--ink);background:var(--paper);transition:transform .3s}
.phone .bar span{padding:14px 0;text-align:center;font-size:13px;font-weight:600}
.phone .bar span:first-child{background:var(--ink);color:var(--paper)}
.phone .bar.hide{transform:translateY(100%)}
.spool{display:grid;gap:10px;justify-items:center;text-align:center;max-width:220px}
.spool .s{width:64px;height:64px;border-radius:50%;background:var(--ink);color:var(--paper);display:grid;place-content:center;font-size:11px;font-weight:700;position:relative;
  background-image:repeating-linear-gradient(0deg,#161514 0 3px,#2e2c29 3px 5px)}
"""

A = f"""<div class="fa"><div class="cta"><p class="h2" style="max-width:16ch">Come and see the studio.</p>
<div class="ctas"><span class="btn">WhatsApp Shruti</span><span class="btn ghost">Book a studio visit</span></div></div>
<svg class="stitch" viewBox="0 0 1000 10" preserveAspectRatio="none"><path d="M0 5 H1000"/></svg>
<div class="util"><span><span class="ph">address</span> · Hubballi (Hubli), Karnataka</span><span>{PHONE}</span><span>Instagram</span><span>Made in Hubballi</span></div>
<div class="ruler"></div><div class="word">TEACHING THREADS</div></div>"""

B = f"""<div class="nl"><p class="h2" style="text-align:center">Ready to start?</p>
<div class="neck"><span class="w">Teaching Threads</span><span class="m">Fashion Academy · Est. <span class="ph" style="opacity:1">20__</span> · Hubballi, Karnataka</span>
<div class="ic"><span>IG</span><span>WA</span><span>CALL</span><span>MAP</span></div></div>
<div class="cutrow" id="cutrow"><div class="line"></div><div class="done"></div><span class="k">✂</span></div>
<button class="btn" type="button" id="cutbtn">Book a studio visit</button></div>"""

C = """<div class="chit2"><form class="torn" id="chitf" onsubmit="return false"><span class="eyebrow">Studio visit · No. 0___</span><h6>Tear off and send</h6>
<div class="f"><label for="cn">Name</label><input id="cn" value="Priya"></div>
<div class="f"><label for="cd">Day</label><select id="cd"><option>Monday</option><option>Wednesday</option><option selected>Saturday</option></select></div>
<div class="f"><label for="cb">Batch</label><select id="cb"><option>Morning</option><option selected>Evening</option></select></div>
<div class="msg"><small>Your WhatsApp message</small><span id="chitOut"></span></div>
<span class="btn" style="justify-self:start">Send on WhatsApp</span></form></div>"""

D = """<div class="phonebox"><div class="phone"><div class="scr" id="scr">
<div class="blk" style="height:150px"></div><div class="blk" style="height:20px;width:70%"></div><div class="blk" style="height:220px"></div>
<div class="blk" style="height:160px"></div><div class="blk" style="height:200px"></div>
<div style="background:var(--ink);color:var(--paper);padding:18px;border-radius:3px;font-family:var(--serif);font-size:22px;line-height:1.05" id="finalcta">Come and see the studio.<br><small style="font-family:var(--mono);font-size:9px">final CTA: bar hides here</small></div>
<div class="blk" style="height:80px"></div></div>
<div class="bar" id="bar"><span>WhatsApp</span><span>Call</span></div></div>
<div class="spool"><div class="s">WA</div><span class="mono">Desktop: a small thread-spool button, bottom right</span><span style="font-size:13px;color:var(--pencil)">Scroll inside the phone; the bar hides when the final CTA is on screen.</span></div></div>"""

body = "".join([
    option("A", "Giant wordmark + tape edge", A,
           "\"Come and see the studio\" with both buttons, a running stitch that keeps sewing across the page, the contact line, then a tape-measure ruler and TEACHING THREADS set edge to edge, bleeding off the bottom.",
           "Bookends the hero's stitch line, and the wordmark is the brand moment people screenshot.",
           "Wordmark at ~16vw so it still spans the screen; buttons stack.",
           [("footer.design: Large Type", "https://www.footer.design/"), ("Abduzeedo: footer inspiration", "https://abduzeedo.com/footer-design-inspiration-only-gallery-earth"),
            ("21st.dev: Kiln wordmark footer", "https://21st.dev/@kedhareswer/components/kiln-wordmark-footer.md"), ("Northeast Tomato", "https://northeasttomato.com/")],
           rec=True),
    option("B", "Neck-label footer + kainchi CTA", B,
           "The footer is one big woven neck label with the brand, \"Est.\" and the city, and social links as care icons. Press the button and a kainchi cuts along the dashed line.",
           "Ties back to the kainchi prototype on this branch and the label language used elsewhere.",
           "The label scales; the cut plays on tap.",
           [("The Design Society", "https://www.thedesignsociety.fr/"), ("Nothin'", "https://www.noth.in/")],
           runner=True, original=True),
    option("C", "Appointment chit", C,
           "A torn-off slip with Name, Day, Batch filled in handwriting. Filling it writes the WhatsApp message.",
           "Continues the order-book idea from the FAQ. It overlaps with Visit option C, so pick one of the two.",
           "Thumb-friendly fields.",
           [("Bird: WhatsApp click-to-chat", "https://bird.com/explained/whatsapp/what-is-a-whatsapp-click-to-chat-link")],
           original=True),
    option("D", "Sticky WhatsApp + Call bar (goes with any)", D,
           "On phones, a bar fixed to the bottom with WhatsApp and Call. It appears after the hero and hides when the final CTA is on screen. On desktop, a small thread-spool button.",
           "Pearl Academy treats WhatsApp and Call as first-class buttons. It's plain links, no heavy chat widget.",
           "This one is mostly for mobile.",
           [("Pearl Academy", "https://pearlacademy.com/programs/certificate-courses/fashion/fashion-design-womenswear")]),
])
body += """<div class="aside"><h3>My pick</h3><p>A for the footer, with D running on phones across the whole page.</p></div>"""

JS = """
const cr=document.getElementById('cutrow');document.getElementById('cutbtn').addEventListener('click',()=>{cr.classList.remove('cut');void cr.offsetWidth;cr.classList.add('cut')});
const f=document.getElementById('chitf'),o=document.getElementById('chitOut');
const u=()=>o.textContent='Hi Shruti, this is '+(f.cn.value||'…')+'. I\\'d like to visit the studio on '+f.cd.value+', '+f.cb.value.toLowerCase()+' batch.';f.addEventListener('input',u);u();
const sc=document.getElementById('scr'),bar=document.getElementById('bar'),fc=document.getElementById('finalcta');
new IntersectionObserver(e=>bar.classList.toggle('hide',e[0].isIntersecting),{root:sc}).observe(fc);
"""
page("footer.html", "Footer CTA Options", "09 / 09", "Final CTA + footer",
     "The last thing people see. One more clear push to WhatsApp or a studio visit, then the practical details.",
     body, CSS, JS)
