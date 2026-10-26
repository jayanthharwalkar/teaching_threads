from common import *

PHONE = "93535 62706"

CSS = """
.vis{display:grid;grid-template-columns:1.2fr .8fr;min-height:420px}
.vis .side{padding:28px;display:grid;gap:12px;align-content:center;border-left:1px solid var(--rule)}
@container (max-width:620px){.vis{grid-template-columns:1fr}.vis .side{border-left:0;border-top:1px solid var(--rule)}}
.map{position:relative;background-color:#f0eee7;background-image:linear-gradient(#e0dccf 1px,transparent 1px),linear-gradient(90deg,#e0dccf 1px,transparent 1px);background-size:20px 20px}
.map svg{width:100%;height:100%;display:block;min-height:340px}
.map .road{stroke:var(--ink);stroke-width:1.5;stroke-dasharray:8 5;fill:none}
.map .road.main{stroke-width:2.4;stroke-dasharray:none}
.map .gl{stroke:var(--ink);stroke-width:1;fill:none;marker-end:url(#arr)}
.map text{font-family:var(--mono);font-size:9px;letter-spacing:.1em;fill:var(--ink);text-transform:uppercase}
.map .lbl-s{font-family:var(--serif);font-size:18px;letter-spacing:0;text-transform:none}
.map .pinhead{fill:var(--ink)}
.map .pinglow{fill:none;stroke:var(--ink);animation:ping 2s ease-out infinite;transform-origin:center;transform-box:fill-box}
@keyframes ping{from{opacity:.8;transform:scale(.6)}to{opacity:0;transform:scale(2.2)}}
.addr{font-family:var(--serif);font-size:24px;line-height:1.15}
.sel{user-select:all;font-family:var(--mono);font-size:13px}

.hrs{display:grid;grid-template-columns:1fr 1fr;gap:24px;padding:34px 28px;align-items:center}
.care2{background:#fbfaf6;border:1px solid #cfcabe;padding:24px 22px;position:relative;font-family:var(--mono);font-size:12px;line-height:1.7;text-transform:uppercase;letter-spacing:.05em}
.care2::before,.care2::after{content:"";position:absolute;left:8px;right:8px;border-top:1.5px dashed var(--ink)}
.care2::before{top:8px}.care2::after{bottom:8px}
.care2 h6{font-family:var(--serif);font-size:30px;font-weight:400;text-transform:none;letter-spacing:0;margin:0 0 10px;line-height:1}
.store{aspect-ratio:4/5;border:1.5px dashed var(--pencil);display:grid;place-content:center;text-align:center;gap:8px;padding:20px;color:var(--pencil)}
@container (max-width:560px){.hrs{grid-template-columns:1fr}}

.appt{padding:36px 28px;display:flex;justify-content:center}
.card{width:min(560px,100%);background:#fbfaf6;border:1.5px solid var(--ink);padding:24px;display:grid;gap:16px;position:relative}
.card::before{content:"";position:absolute;left:-1.5px;right:-1.5px;top:-8px;height:8px;background:radial-gradient(circle at 6px 8px,var(--paper) 4px,transparent 4.5px) 0 0/12px 8px repeat-x}
.card h6{margin:0;font-family:var(--serif);font-weight:400;font-size:30px;line-height:1}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chips button{all:unset;cursor:pointer;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--ink);padding:8px 11px;border-radius:999px}
.chips button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.chips button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
.msg{background:#e6f2df;border-radius:10px 10px 10px 2px;padding:12px 14px;font-size:14px;line-height:1.45;max-width:44ch;color:#1d2b17}
.msg small{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#4d6343;margin-bottom:4px}
.row2{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;border-top:1px solid var(--rule);padding-top:12px;font-size:13px}

.walk{position:relative;height:440px}
.walk .play{position:absolute;inset:0;display:grid;place-content:center;gap:12px;text-align:center}
.walk .play span:first-child{width:76px;height:76px;border-radius:50%;background:var(--paper);border:1.5px solid var(--ink);display:grid;place-content:center;margin:auto;font-size:22px}
.walk .lab{position:absolute;left:16px;bottom:16px;background:var(--paper);border:1px solid var(--rule);padding:10px 12px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase}
"""

A = f"""<div class="vis"><div class="map">
<svg viewBox="0 0 520 380" role="img" aria-label="Illustrative map of the studio">
<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#161514"/></marker></defs>
<path class="road main" d="M0 250 C 140 240, 300 260, 520 220"/>
<path class="road" d="M180 0 C 190 120, 200 200, 210 380"/><path class="road" d="M360 0 L 380 380"/><path class="road" d="M0 110 C 160 120, 360 90, 520 100"/>
<path class="gl" d="M40 330 H 140"/><text x="40" y="320">grainline</text>
<text x="20" y="240">Piece A · main road</text><text x="216" y="40">Piece B</text><text x="388" y="60">Piece C</text>
<g transform="translate(300 175)"><circle class="pinglow" r="14"/><circle class="pinhead" r="7"/><path d="M0 7 V 40" stroke="#161514" stroke-width="2"/></g>
<text class="lbl-s" x="316" y="170">Teaching Threads</text><text x="316" y="186">studio · cut here ✂</text>
</svg></div>
<div class="side"><span class="eyebrow">Visit the studio</span><p class="addr"><span class="ph">studio address</span><br>Hubballi (Hubli), Karnataka</p>
<span class="btn">Get directions</span><span class="mono" style="color:var(--pencil)">Opens Google Maps · two-wheeler route</span>
<span class="sel">{PHONE}</span></div></div>"""

B = f"""<div class="hrs"><div class="care2"><h6>Studio hours</h6>
MON–SAT · <span class="ph">10–1 / 4–7?</span><br>SUNDAY · CLOSED<br>BATCHES · MORNING / EVENING<br>HAND WASH ONLY · DO NOT TUMBLE DRY<br><br>
<span style="text-transform:none" class="sel">Call {PHONE}</span></div>
<div class="store"><span class="mono">Storefront photo</span><span style="font-size:13px">A real photo of the door or street helps first-timers find it. We don't have one yet.</span></div></div>"""

C = f"""<div class="appt"><div class="card" id="appt">
<span class="eyebrow">Book a studio visit</span><h6>Your first fitting at Teaching Threads</h6>
<div><div class="mono" style="margin-bottom:6px;color:var(--pencil)">Day</div><div class="chips" data-k="day">
<button type="button" aria-pressed="false">Monday</button><button type="button" aria-pressed="false">Tuesday</button><button type="button" aria-pressed="false">Wednesday</button><button type="button" aria-pressed="true">Thursday</button><button type="button" aria-pressed="false">Friday</button><button type="button" aria-pressed="false">Saturday</button></div></div>
<div><div class="mono" style="margin-bottom:6px;color:var(--pencil)">Time</div><div class="chips" data-k="time"><button type="button" aria-pressed="false">morning</button><button type="button" aria-pressed="true">evening</button></div></div>
<div><div class="mono" style="margin-bottom:6px;color:var(--pencil)">Course</div><div class="chips" data-k="course"><button type="button" aria-pressed="true">3-month</button><button type="button" aria-pressed="false">6-month</button><button type="button" aria-pressed="false">not sure yet</button></div></div>
<div class="msg" id="apptMsg"><small>Your WhatsApp message</small><span></span></div>
<span class="btn" style="justify-self:start">Send on WhatsApp</span>
<div class="row2"><span><span class="ph">studio address</span> · Hubballi</span><span class="sel">{PHONE}</span></div></div></div>"""

D = f"""<div class="walk"><img class="clay" src="{img('dressform', 900)}" alt="Clay dress form, studio interior">
<div class="play"><span>▶</span><span class="mono">A short POV walk from the street to the cutting table</span></div>
<div class="lab">Teaching Threads · <span class="ph">address</span></div></div>"""

body = "".join([
    option("A", "Map as a pattern sheet", A,
           "A hand-drawn map styled like a pattern sheet: roads as dashed cutting lines, a grainline arrow, streets labelled \"Piece A, B, C\", and a pulsing dressmaker's pin on the studio. One button opens directions.",
           "On brand and costs nothing to load. A real Google Maps embed is heavy and hurts page speed.",
           "The drawing scales down; the Get directions button gets big.",
           [("Google Maps URLs (no API key, two-wheeler mode)", "https://developers.google.com/maps/documentation/urls/get-started"),
            ("CoreWebVitals.io: why map embeds are slow", "https://www.corewebvitals.io/pagespeed/google-maps-100-percent-pagespeed")],
           original=True),
    option("B", "Hours as a care label + storefront", B,
           "Opening hours and batches written like care instructions, next to a real photo of the studio door or street.",
           "A storefront photo removes the \"will I find it?\" fear before the first visit.",
           "Label first, photo below.",
           [("Packaging of the World: Derrick Lin labels", "https://packagingoftheworld.com/?p=26130")],
           runner=True),
    option("C", "Fitting-appointment card", C,
           "Pick a day, a time and a course, and the card writes the WhatsApp message for you. Address and phone underneath. Try the chips.",
           "The highest-intent option: Shruti receives a structured message (day, time, course) with no form or backend.",
           "Thumb-sized chips; the best fit for phones.",
           [("Pearl Academy: WhatsApp + Call as first-class CTAs", "https://pearlacademy.com/programs/certificate-courses/fashion/fashion-design-womenswear"),
            ("Bird: WhatsApp click-to-chat links", "https://bird.com/explained/whatsapp/what-is-a-whatsapp-click-to-chat-link")],
           rec=True, original=True),
    option("D", "POV walk-in", D,
           "A short clay-POV Kling clip from the street, through the door, to the cutting table, ending on the address.",
           "Continues the video language of the course section and shows what's inside.",
           "A poster frame; tap to play a muted loop.",
           [("GreenSock image-sequence scrub", "https://codepen.io/GreenSock/pen/RwvrNqN")]),
])
body += """<div class="aside"><h3>Notes</h3><ul><li>My pick is C with A's map beside it.</li>
<li>Needed from Shruti: exact address, hours, batch timings, and ideally one photo of the door.</li>
<li>The phone number shown is from her PDFs.</li></ul></div>"""

JS = """
const ap=document.getElementById('appt'),out=document.querySelector('#apptMsg span');
function val(k){const b=ap.querySelector('.chips[data-k="'+k+'"] [aria-pressed="true"]');return b?b.textContent:''}
function upd(){out.textContent='Hi Shruti, I\\'d like to visit the studio on '+val('day')+' '+val('time')+'. Course: '+val('course')+'.'}
ap.querySelectorAll('.chips').forEach(g=>g.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
 g.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));upd()}));upd();
"""
page("visit.html", "Visit The Studio Options", "07 / 09", "Visit the studio",
     "Most people will want to see the place before paying. These options take away the \"where is it, when can I come\" doubt without a slow Google Maps embed.",
     body, CSS, JS)
