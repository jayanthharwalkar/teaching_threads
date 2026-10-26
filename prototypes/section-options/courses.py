from common import *

ROWS = [("Duration", "3 months", "6 months"), ("Fee", '<span class="ph">₹ to confirm</span>', '<span class="ph">₹ to confirm</span>'),
        ("Batch timings", '<span class="ph">to confirm</span>', '<span class="ph">to confirm</span>'),
        ("Measurement, machine practice, cutting, piping, darts, bodice block", "✓", "✓"),
        ("Kurta drafts", "2", "4"), ("Sleeve types", "3", "6"), ("Blouses", "6", "8 <small>+ Katori, shirt collar</small>"),
        ("Lehenga", "Panel, umbrella, pleated", "+ Fishcut, knot skirt"), ("Gowns", "Panel, umbrella", "Panel, umbrella + cape"),
        ("Design basics, finishing, branding", "✓", "✓"), ("Aari work <small>pearl, beads, zardozi, thread</small>", "—", "✓"),
        ("Boutique management", "—", "✓"), ("Fabrics &amp; local market visit", "—", "✓")]

CSS = """
.cwrap{padding:32px 28px;display:grid;gap:22px}
@container (max-width:560px){.cwrap{padding:22px 12px}}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@container (max-width:560px){.pair{gap:8px}}

/* A envelopes */
.env{perspective:1200px;cursor:pointer;min-height:430px}
.env .in{position:relative;width:100%;height:100%;min-height:430px;transition:transform .7s;transform-style:preserve-3d}
.env.flip .in{transform:rotateY(180deg)}
.env .face{position:absolute;inset:0;backface-visibility:hidden;border:1.5px solid var(--ink);background:#fbfaf6;padding:16px;display:flex;flex-direction:column;gap:10px}
.env .back{transform:rotateY(180deg);overflow:auto}
.env .num{font-family:var(--serif);font-size:clamp(64px,14cqi,120px);line-height:.8}
.env .top{display:flex;justify-content:space-between;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;border-bottom:1px solid var(--ink);padding-bottom:8px;gap:6px;flex-wrap:wrap}
.env svg{flex:1;min-height:0;width:100%;stroke:var(--ink);fill:none;stroke-width:1.3}
.env .facts{font-family:var(--mono);font-size:10.5px;line-height:1.5;text-transform:uppercase;letter-spacing:.05em}
.env .back h6{margin:0;font-family:var(--serif);font-weight:400;font-size:22px}
.env .back ul{margin:0;padding-left:16px;font-size:12.5px;line-height:1.45}
.env .back b{font-weight:700}
.hint{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil);text-align:center}

/* B care labels */
.labels{display:flex;justify-content:center;gap:clamp(12px,5cqi,48px);align-items:flex-start}
.strip{width:min(220px,46%);background:#fbfaf6;border:1px solid #cfcabe;padding:22px 14px 26px;position:relative;
  background-image:repeating-linear-gradient(0deg,rgba(0,0,0,.025) 0 1px,transparent 1px 3px)}
.strip::before,.strip::after{content:"";position:absolute;left:8px;right:8px;border-top:1.5px dashed var(--ink)}
.strip::before{top:8px}.strip::after{bottom:8px}
.strip h6{margin:0 0 4px;font-family:var(--serif);font-weight:400;font-size:40px;line-height:.9;text-align:center}
.strip .s{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;text-align:center;margin-bottom:12px;color:var(--pencil)}
.strip ol{margin:0;padding:0;list-style:none;font-family:var(--mono);font-size:10.5px;line-height:1.3;text-transform:uppercase;letter-spacing:.03em;display:grid;gap:7px}
.strip ol li{border-top:1px solid var(--rule);padding-top:6px}
.strip ol li.x{font-weight:700}
.strip .wa{margin-top:16px;width:100%;justify-content:center}

/* C swing tags */
.tags{position:relative;padding-top:40px}
.tags .string{position:absolute;left:4%;right:4%;top:14px;height:2px;background:var(--ink)}
.swing{display:grid;grid-template-columns:1fr 1fr;gap:16px;justify-items:center}
.stag{width:min(230px,100%);background:#ece5d6;border:1px solid #c9bfa9;border-radius:6px 6px 4px 4px;clip-path:polygon(50% 0,100% 16%,100% 100%,0 100%,0 16%);
  padding:46px 16px 18px;text-align:center;transform-origin:50% -26px;animation:sway 4s ease-in-out infinite;position:relative}
.stag:nth-child(2){animation-delay:-2s}
.stag::before{content:"";position:absolute;top:18px;left:50%;width:12px;height:12px;border-radius:50%;background:var(--paper);border:1px solid #c9bfa9;transform:translateX(-50%)}
@keyframes sway{0%,100%{transform:rotate(-2.5deg)}50%{transform:rotate(2.5deg)}}
.stag .mono{color:#6b6150}
.stag .size{font-family:var(--serif);font-size:44px;line-height:.9;margin:8px 0}
.stag .price{font-family:var(--mono);font-size:13px;margin-top:6px}
.spec{border-top:1px solid var(--ink);display:grid;grid-template-columns:1fr auto auto;font-size:13px}
.spec div{padding:8px 6px;border-bottom:1px solid var(--rule)}
.spec .h{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}

/* D size chart */
.chart{width:100%;border-collapse:collapse;font-size:13px}
.chart th,.chart td{padding:10px 8px;border-bottom:1px solid var(--rule);text-align:left;vertical-align:top}
.chart td:nth-child(n+2),.chart th:nth-child(n+2){width:28%;font-family:var(--mono);font-size:12px}
.chart thead th{position:sticky;top:0;background:var(--paper);border-bottom:1.5px solid var(--ink);vertical-align:bottom}
.chart .envh{display:grid;gap:4px}
.chart .envh span:first-child{font-family:var(--serif);font-size:clamp(44px,8cqi,72px);line-height:.8;font-weight:400}
.chart .envh span:last-child{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil);font-weight:400}
.chart tr.x td{font-weight:600}
.chart tr.x td:first-child::before{content:"6-month only · ";font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil);font-weight:400}
.chart small{display:block;font-size:11px;color:var(--pencil);font-weight:400}
.chart tfoot td{border:0;padding-top:16px}
@container (max-width:560px){.chart{font-size:12px}.chart td:first-child{width:44%}}

.tapeband{height:30px;position:relative;border:1px solid #cfc9bc;background:#ebe7dc;background-image:repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 4.1666%);}
.tapeband i{position:absolute;top:0;bottom:0;left:0;width:50%;background:rgba(22,21,20,.18);animation:grow 5s ease-in-out infinite alternate}
.tapeband b{position:absolute;top:34px;font-family:var(--mono);font-size:10px;letter-spacing:.1em;font-weight:400}
@keyframes grow{from{width:50%}to{width:100%}}
"""

blouse = '<svg viewBox="0 0 120 90"><path d="M30 14 L48 8 Q60 18 72 8 L90 14 L104 34 L90 40 L86 32 L86 80 L34 80 L34 32 L30 40 L16 34 Z"/><path d="M48 8 Q60 30 72 8" stroke-dasharray="3 3"/></svg>'
both = '<svg viewBox="0 0 120 90"><path d="M42 6 L54 3 Q60 8 66 3 L78 6 L84 18 L76 20 L76 28 L44 28 L44 20 L36 18 Z"/><path d="M44 32 L76 32 L100 86 L20 86 Z"/><path d="M60 32 L60 86 M40 60 Q60 66 80 60" stroke-dasharray="3 3"/><circle cx="92" cy="12" r="5"/><path d="M89 12h6M92 9v6"/></svg>'

def env(num, title, art, facts, spec):
    return f"""<div class="env" tabindex="0" role="button" aria-label="Flip the {num}-month pattern envelope"><div class="in">
<div class="face"><div class="top"><span>Pattern No. TT-{num}</span><span>Beginner</span></div><div class="num">{num}</div>
<div class="mono">{title}</div>{art}<div class="facts">Fee <span class="ph">₹ ?</span> · Batches <span class="ph">am / pm ?</span></div>
<span class="btn" style="justify-content:center">Choose this pattern</span></div>
<div class="face back"><h6>You will make</h6><ul>{spec}</ul></div></div></div>"""

A = f"""<div class="cwrap"><div class="pair">
{env("03", "Months · fashion design", blouse, "", "<li>Measurement &amp; industrial machine practice</li><li>Bodice block, darts, piping</li><li>2 kurtas · 3 sleeves</li><li>6 blouses: one-dart to boat neck</li><li>Lehenga: panel, umbrella, pleated</li><li>Gowns · finishing · branding</li>")}
{env("06", "Months · design + Aari + boutique", both, "", "<li>Everything in 03, plus:</li><li><b>4 kurtas · 6 sleeves</b></li><li><b>Katori &amp; shirt-collar blouses</b></li><li><b>Fishcut &amp; knot-skirt lehenga · cape</b></li><li><b>Aari: pearl, beads, zardozi, thread</b></li><li><b>Boutique management</b></li><li><b>Fabrics &amp; local market visit</b></li>")}
</div><div class="hint">Tap an envelope to flip it to the back</div></div>"""

common_items = ["Measurement", "Machine practice", "Cutting &amp; piping", "Darts &amp; bodice block", "Kurtas", "Sleeves", "Blouses", "Lehenga", "Gowns", "Design basics", "Finishing", "Branding"]
extras = ["+2 kurtas · +3 sleeves", "Katori &amp; shirt collar", "Fishcut · knot skirt · cape", "Aari work", "Boutique management", "Market visit"]
B = f"""<div class="cwrap"><div class="labels">
<div class="strip"><h6>03</h6><div class="s">months</div><ol>{''.join(f'<li>{i}</li>' for i in common_items)}</ol><span class="btn wa">WhatsApp</span></div>
<div class="strip"><h6>06</h6><div class="s">months</div><ol>{''.join(f'<li>{i}</li>' for i in common_items)}{''.join(f'<li class="x">{i}</li>' for i in extras)}</ol><span class="btn wa">WhatsApp</span></div>
</div></div>"""

C = """<div class="cwrap"><div class="tags"><div class="string"></div><div class="swing">
<div class="stag"><div class="mono">Style TT-03</div><div class="size">3 months</div><div class="mono">Fashion design</div><div class="price"><span class="ph">₹ ?</span></div></div>
<div class="stag"><div class="mono">Style TT-06</div><div class="size">6 months</div><div class="mono">Design + Aari + boutique</div><div class="price"><span class="ph">₹ ?</span></div></div>
</div></div>
<div class="spec"><div class="h"></div><div class="h">3 mo</div><div class="h">6 mo</div>
<div>Kurta drafts</div><div>2</div><div>4</div><div>Sleeves</div><div>3</div><div>6</div><div>Blouses</div><div>6</div><div>8</div>
<div>Aari work</div><div>—</div><div>✓</div><div>Boutique management</div><div>—</div><div>✓</div></div></div>"""

rows = ""
for r in ROWS:
    cls = ' class="x"' if r[1] == "—" else ""
    rows += f"<tr{cls}><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>"
D = f"""<div class="cwrap">
<div><div class="tapeband"><i></i><b style="left:0">0</b><b style="left:48%">12 wks</b><b style="right:0">24 wks</b></div></div>
<div style="overflow-x:auto;margin-top:18px"><table class="chart"><thead><tr><th><span class="eyebrow">Size chart · what you'll learn</span></th>
<th><div class="envh"><span>03</span><span>months · TT-03</span></div></th><th><div class="envh"><span>06</span><span>months · TT-06</span></div></th></tr></thead>
<tbody>{rows}</tbody><tfoot><tr><td></td><td><span class="btn">WhatsApp</span></td><td><span class="btn">WhatsApp</span></td></tr></tfoot></table></div></div>"""

body = "".join([
    option("A", "Two pattern envelopes", A,
           "Two vintage-style sewing-pattern envelopes side by side, \"03\" and \"06\", each with a line drawing of what you'll make. Tap to flip to the back, which lists what's inside like a real pattern back.",
           "A pattern envelope already is a spec sheet: promise on the front, details on the back. It reads editorial, not SaaS.",
           "Two narrow envelopes at half width each. Since flipping hides content, duration, fee and timings stay on the front.",
           [("Tilly and the Buttons: pattern envelope evolution", "https://www.tillyandthebuttons.com/blogs/sewing/sewing-pattern-envelopes"),
            ("Old Design Shop: vintage pattern envelopes", "https://olddesignshop.com/2014/11/vintage-skirt-pattern-envelope-free-graphics/")]),
    option("B", "Two care labels", B,
           "Two long woven-label strips listing the modules. The 6-month label is physically longer, and its extra rows are bold.",
           "Length = duration, with zero explanation. Small footprint, very on-brand.",
           "Two vertical strips fit a 375px phone naturally.",
           [("Packaging of the World: Derrick Lin labels", "https://packagingoftheworld.com/?p=26130"), ("Fonts In Use: Ahluwalia", "https://www.fontsinuse.com/uses/41898/ahluwalia-e-commerce")],
           runner=True, original=True),
    option("C", "Two swing tags + spec panel", C,
           "Two kraft price tags swaying on one black thread, with style number, size \"3 months\" / \"6 months\" and price. A short shared spec panel underneath.",
           "A price tag is the universal \"what does it cost\" signal, and fees are the top question for Indian course buyers.",
           "Tags stay side by side; the panel stacks below.",
           [("Awwwards: Atwww Studio pricing", "https://www.awwwards.com/inspiration/pricing-page-atwww-studio"), ("Awwwards: Artboard Studio pricing", "https://www.awwwards.com/inspiration/pricing-page-artboard-studio")],
           original=True),
    option("D", "Size-chart spec sheet", D,
           "A tailor's size chart. Column heads are the two envelope numbers; rows line up every difference straight from the PDFs. A tape across the top grows from 12 to 24 weeks.",
           "Row alignment is the most honest comparison, everything is real text Google can read, and it's the only format that stays truly side by side on a phone.",
           "Two short columns of values at 375px, with the header row sticky while you scroll.",
           [("Pearl Academy: key-facts strip", "https://pearlacademy.com/programs/certificate-courses/fashion/fashion-design-womenswear"),
            ("Awwwards: Dora Alpha 2.0 comparison", "https://www.awwwards.com/inspiration/pricing-page-dora-alpha-2-0"),
            ("Framer: Scroll Stack (tape band)", "https://www.framer.com/marketplace/components/scroll-stack/")],
           rec=True),
])
body += """<div class="aside"><h3>Notes</h3><ul>
<li>My pick is D with A's envelope fronts as the column heads: you get the charm of A and the clarity of D.</li>
<li>No toggle between 3 and 6 months: with only two options, a toggle hides half the answer.</li>
<li>Every row comes from Shruti's two PDFs. Fees and batch timings are the only gaps.</li></ul></div>"""

JS = """document.querySelectorAll('.env').forEach(e=>{const f=()=>e.classList.toggle('flip');e.addEventListener('click',f);e.addEventListener('keydown',k=>{if(k.key==='Enter'||k.key===' '){k.preventDefault();f()}})});"""
page("courses.html", "Course Comparison Options", "04 / 09", "Courses, side by side",
     "Four ways to put the 3-month and 6-month courses next to each other. Both teach the same five stages; the 6-month adds Aari work, boutique management, a market visit and more garment variations. All facts are from Shruti's PDFs.",
     body, CSS, JS)
