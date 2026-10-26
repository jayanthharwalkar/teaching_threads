from common import *

FONTS_T = ("https://fonts.googleapis.com/css2?family=Instrument+Sans:wdth,wght@75..100,400..700&family=Instrument+Serif:ital@0;1"
           "&family=IBM+Plex+Mono:wght@400;500&family=Anek+Kannada:wdth,wght@75..125,300..700&family=Anek+Devanagari:wdth,wght@75..125,300..700"
           "&family=Caveat:wght@500&family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Inter+Tight:wght@400;600"
           "&family=DM+Mono&family=Tiro+Kannada&family=Tiro+Devanagari+Hindi&family=Fraunces:opsz,wght,SOFT,WONK@9..144,100..900,0..100,0..1"
           "&family=Hanken+Grotesk:wght@400;600&family=Martian+Mono:wdth,wght@75..112,400&family=Noto+Serif+Kannada:wght@400;600"
           "&family=Anton&family=Archivo:wdth,wght@62..125,400..800&family=Baloo+Tamma+2:wght@500;700&family=Hind+Mysuru:wght@400;600"
           "&family=Hind:wght@400;600&family=Hubballi&family=Cormorant+Garamond:ital,wght@0,300;0,500;1,300&family=Jost:wght@400;500"
           "&family=DM+Serif+Display&family=Manrope:wght@400;600&family=Space+Mono&display=swap")

CSS = """
.spec{padding:30px 28px;display:grid;gap:20px}
.spec .disp{font-size:clamp(44px,8.4cqi,92px);line-height:.95;margin:0;text-wrap:balance}
.spec .grid{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:start}
.spec .bodyt{font-size:15px;line-height:1.6;margin:0;max-width:52ch;color:#34322e}
.spec .ann{font-size:11px;letter-spacing:.12em;text-transform:uppercase;display:flex;gap:14px;flex-wrap:wrap;border-top:1px dashed var(--ink);border-bottom:1px dashed var(--ink);padding:8px 0}
.spec .scripts{display:grid;gap:8px}
.spec .kn{font-size:30px;line-height:1.5}
.spec .hi{font-size:26px;line-height:1.5}
.spec .who{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil);display:grid;gap:3px}
.spec .ui{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.spec .ui .b{background:var(--ink);color:var(--paper);padding:10px 15px;border-radius:999px;font-size:13px;font-weight:600}
@container (max-width:620px){.spec .grid{grid-template-columns:1fr}.spec{padding:22px 16px}}
.wonk{transition:font-variation-settings .2s}
.axes{display:flex;gap:14px;flex-wrap:wrap;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--pencil)}
.axes label{display:flex;gap:6px;align-items:center}
.axes input{width:110px;accent-color:#161514}
.hub{padding:30px 28px;display:grid;gap:10px}
.hub .big{font-family:"Hubballi",sans-serif;font-size:clamp(40px,8cqi,80px);line-height:1}
.tech{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px;background:var(--rule)}
.tech>div{background:var(--paper);padding:24px;display:grid;gap:10px;align-content:start;min-height:220px}
.tech h6{margin:0;font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--pencil);font-weight:400}
.photo-type{font-family:"Anton",sans-serif;font-size:clamp(56px,13cqi,120px);line-height:.85;background-size:cover;background-position:center 30%;-webkit-background-clip:text;background-clip:text;color:transparent;filter:grayscale(1) contrast(1.3)}
.tapenums{display:flex;border:1px solid #cfc9bc;background:#ebe7dc;font-family:"Martian Mono",monospace;font-variant-numeric:tabular-nums;font-size:11px;font-variation-settings:"wdth" 75;overflow:hidden}
.tapenums span{flex:1;border-left:1px solid var(--ink);padding:16px 3px 3px;background:repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 25%) 0 0/100% 8px no-repeat}
.microlabel{font-family:var(--mono);font-size:10px;letter-spacing:.11em;text-transform:uppercase;line-height:1.6;border:1px solid #cfcabe;padding:12px 14px;background:#fbfaf6;max-width:260px}
.split span{display:inline-block;animation:rise 2.8s cubic-bezier(.3,.7,.2,1) infinite both}
@keyframes rise{0%{transform:translateY(60%);opacity:0}25%,80%{transform:none;opacity:1}100%{opacity:0}}
@container (max-width:620px){.tech{grid-template-columns:1fr}}
"""

def spec(disp_css, body_css, mono_css, kn_css, hi_css, disp="Learn to make <em>what you wear.</em>", who="", extra=""):
    return f"""<div class="spec">
<p class="disp" style="{disp_css}">{disp}</p>
<div class="ann" style="{mono_css}"><span>Cut 2 on fold</span><span>TT-03 · Front bodice</span><span>Seam 1.5 cm</span><span>₹ 12,500</span></div>
<div class="grid"><div style="display:grid;gap:14px"><p class="bodyt" style="{body_css}">Three and six-month fashion design &amp; tailoring courses in Hubballi. Measure, draft, stitch, then make your first blouse and lehenga on industrial machines, taught by designer Shruti Mahajan.</p>
<div class="ui" style="{body_css}"><span class="b">Enquire on WhatsApp</span><span style="{mono_css};font-size:11px;letter-spacing:.1em;text-transform:uppercase">Stage 01 / 05 · Measure</span></div>{extra}</div>
<div class="scripts"><span class="kn" style="{kn_css}">ಹೊಲಿಗೆ ಕಲಿಯಿರಿ · ಹುಬ್ಬಳ್ಳಿ</span><span class="hi" style="{hi_css}">सिलाई सीखें · हुबली</span><div class="who">{who}</div></div></div></div>"""

O = spec("font-family:'Cormorant Garamond',serif;font-weight:300", "font-family:'Jost',sans-serif", "font-family:'Jost',sans-serif", "font-family:var(--kn)", "font-family:'Anek Devanagari',sans-serif",
         who="Cormorant Garamond / Jost<span>No Kannada or Hindi in either; the browser falls back</span>")
A = spec("font-family:'Bodoni Moda',serif;font-variation-settings:'opsz' 96;font-weight:500", "font-family:'Inter Tight',sans-serif", "font-family:'DM Mono',monospace", "font-family:'Tiro Kannada',serif", "font-family:'Tiro Devanagari Hindi',serif",
         who="Bodoni Moda / Inter Tight / DM Mono<span>Kannada: Tiro Kannada · Hindi: Tiro Devanagari</span>")
B = spec("font-family:'Instrument Serif',serif", "font-family:'Instrument Sans',sans-serif", "font-family:'IBM Plex Mono',monospace", "font-family:'Anek Kannada',sans-serif;font-weight:500", "font-family:'Anek Devanagari',sans-serif;font-weight:500",
         who="Instrument Serif / Instrument Sans / IBM Plex Mono<span>Kannada: Anek Kannada · Hindi: Anek Devanagari</span>")
C = spec("font-family:'Fraunces',serif;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-weight:400", "font-family:'Hanken Grotesk',sans-serif", "font-family:'Martian Mono',monospace;font-variation-settings:'wdth' 75", "font-family:'Noto Serif Kannada',serif", "font-family:serif",
         who="Fraunces / Hanken Grotesk / Martian Mono<span>Kannada: Noto Serif Kannada</span>",
         extra='<div class="axes"><label>Soft <input type="range" min="0" max="100" value="100" data-ax="SOFT"></label><label>Wonk <input type="range" min="0" max="1" step="1" value="1" data-ax="WONK"></label><label>Weight <input type="range" min="100" max="900" value="400" data-ax="wght"></label></div>')
C = C.replace('class="disp"', 'class="disp wonk" id="fr"', 1)
D = spec("font-family:'Anton',sans-serif;text-transform:uppercase;line-height:.92;letter-spacing:.005em", "font-family:'Archivo',sans-serif", "font-family:'Caveat',cursive;font-size:20px;letter-spacing:0;text-transform:none", "font-family:'Baloo Tamma 2',sans-serif;font-weight:700", "font-family:'Anek Devanagari',sans-serif;font-weight:700",
         disp="Learn to make what you wear.", who="Anton / Archivo / Caveat (tailor's chalk notes)<span>Kannada: Baloo Tamma 2 or Anek condensed</span>")
E = spec("font-family:'Cormorant Garamond',serif;font-weight:300;letter-spacing:-.02em", "font-family:'Manrope',sans-serif", "font-family:'Space Mono',monospace", "font-family:'Anek Kannada',sans-serif", "font-family:'Anek Devanagari',sans-serif",
         who="PP Editorial New / PP Neue Montreal (paid)<span>Stand-ins shown: Cormorant + Manrope. Preview the real faces on pangrampangram.com</span>")
F = spec("font-family:'DM Serif Display',serif", "font-family:'Manrope',sans-serif", "font-family:'Space Mono',monospace", "font-family:'Hind Mysuru',sans-serif;font-weight:600", "font-family:'Hind',sans-serif;font-weight:600",
         who="Gambarino or Boska / General Sans or Satoshi / Space Mono<span>Fontshare fonts can't load here; stand-ins DM Serif Display + Manrope. Kannada: Hind Mysuru (ITF)</span>")

HUB = """<div class="hub"><span class="eyebrow">A free Google font named after the city</span><div class="big">Made in Hubballi · ಹುಬ್ಬಳ್ಳಿಯಲ್ಲಿ ತಯಾರಿಸಲಾಗಿದೆ</div>
<p class="sub" style="font-family:'Hubballi',sans-serif;font-size:18px">Kannada + Latin, one weight. Use it for small labels: address, "Made in Hubballi", footer. A nice story for the brand.</p>
<span class="ph" style="justify-self:start">Kannada lines on this page need a native speaker's check</span></div>"""

TECH = f"""<div class="tech">
<div><h6>Split-letter reveal (GSAP SplitText, free since 2025)</h6><p class="h2 split">{''.join(f'<span style="animation-delay:{i*0.04:.2f}s">{c if c != " " else "&nbsp;"}</span>' for i, c in enumerate("Measure. Draft. Stitch."))}</p></div>
<div><h6>Photo inside type</h6><div class="photo-type" style="background-image:url({img('cape', 700)})">FOREST FURY</div></div>
<div><h6>Tape-measure numerals (Martian Mono, narrow)</h6><div class="tapenums">{''.join(f'<span>{i}</span>' for i in range(0, 48, 4))}</div></div>
<div><h6>Care-label micro type (9-11px mono caps, wide tracking)</h6><div class="microlabel">100% Hubballi made<br>Shruti Mahajan · Est. 20__<br>Hand finish · Do not rush</div></div>
</div>"""

body = "".join([
    option("0", "What the prototype uses now", O,
           "Cormorant Garamond for headlines, Jost for text.",
           "Elegant and safe, but you see it on many boutique sites.",
           "Fine, but neither font has Kannada, so Kannada text falls back to whatever the phone has.",
           [("Google Fonts: Cormorant Garamond", "https://fonts.google.com/specimen/Cormorant+Garamond")]),
    option("A", "Atelier Didone", A,
           "Bodoni Moda, the high-contrast fashion-magazine serif, with Inter Tight and a mono.",
           "Instantly reads \"couture\". It's the Vogue/Bazaar language.",
           "Fine hairlines break at small sizes, so only use it big. Risk: every Indian bridal site looks like this unless it's set huge and cropped.",
           [("Fonts In Use: Harper's Bazaar 2021", "https://fontsinuse.com/uses/43467/harper-s-bazaar-2021-redesign"), ("TypeTogether: Fino for Vogue", "https://www.type-together.com/2021-fino-vogue"),
            ("Google Fonts: Bodoni Moda", "https://fonts.google.com/specimen/Bodoni+Moda/about")]),
    option("B", "Pattern Paper", B,
           "Instrument Serif headlines (with a lovely italic), Instrument Sans text, IBM Plex Mono for pattern-style notes like \"CUT 2 ON FOLD\". Anek Kannada matches the sans in width.",
           "Calm, modern atelier. Closest to off-white + ink + clay, and the Kannada companion is designed to sit with Latin.",
           "Works well small. Instrument Sans has a width axis, so headings can tighten on phones.",
           [("Figma: Instrument Serif", "https://www.figma.com/fonts/instrument-serif/"), ("EkType: Anek", "https://github.com/EkType/Anek"),
            ("Google Fonts: Anek Kannada", "https://fonts.google.com/specimen/Anek+Kannada")],
           rec=True),
    option("C", "Kinetic Serif", C,
           "Fraunces, a variable serif with \"soft\" and \"wonk\" dials, plus Hanken Grotesk and Martian Mono. Drag the sliders: on the real page these could move with scroll, like fabric draping.",
           "Warm, a little quirky, and the best for type that animates.",
           "Fine. Keep the wonky letters to the hero; it's common on startup sites.",
           [("Codrops: Exat variable-font microsite", "https://tympanus.net/codrops/?p=113526"), ("Google Fonts: Fraunces", "https://fonts.google.com/specimen/Fraunces")]),
    option("D", "Superr-style Poster", D,
           "Anton in tall caps, Archivo for text, Caveat as handwritten \"tailor's chalk\" notes. This is what thesuperrco.com actually uses (Anton + Plus Jakarta Sans + a handwritten accent).",
           "The literal match if Arun says \"make it like Superr\". Loud, young, Instagram-native.",
           "Strong on phones; condensed caps fit long words.",
           [("thesuperrco.com", "https://thesuperrco.com/"), ("thesuperrco.com CSS (their fonts)", "https://thesuperrco.com/css/base.css"), ("Google Fonts: Anton", "https://fonts.google.com/specimen/Anton")],
           runner=True),
    option("E", "Foundry Editorial (paid)", E,
           "PP Editorial New with PP Neue Montreal, the classic Awwwards studio look. Shown here with free stand-ins because the real fonts can't load in this preview.",
           "Very polished, very \"designed\".",
           "Fine. Needs a paid web licence priced by monthly pageviews.",
           [("Typewolf: Neue Montreal", "https://www.typewolf.com/neue-montreal"), ("Pangram Pangram licence FAQ", "https://pangrampangram.com/pages/faq")]),
    option("F", "Indian Type Foundry", F,
           "Gambarino or Boska serif with General Sans or Satoshi, from Fontshare (free, by Indian Type Foundry), plus Hind Mysuru for Kannada. Shown with stand-ins.",
           "\"An Indian foundry for an Indian academy\" is a nice story.",
           "Fine. Fontshare may require loading fonts from their servers instead of self-hosting.",
           [("ITF: introducing Fontshare", "https://www.indiantypefoundry.com/news/introducing-fontshare"), ("Fontshare", "https://www.fontshare.com/"), ("Google Fonts: Hind Mysuru", "https://fonts.google.com/specimen/Hind+Mysuru")]),
])
body += f"""<section class="opt"><div class="opt-head"><span class="opt-letter">+</span><h2 class="opt-name">Bonus: the "Hubballi" font</h2><div class="opt-tags"><span class="tag">Works with any system</span></div></div>
<div class="mock">{HUB}</div><div class="links"><span class="kicker">Source</span>{links_html([("Google Fonts: Hubballi", "https://fonts.google.com/specimen/Hubballi")])}</div></section>
<section class="opt"><div class="opt-head"><span class="opt-letter">✂</span><h2 class="opt-name">Type techniques that fit tailoring</h2></div>
<div class="mock">{TECH}</div><div class="links"><span class="kicker">Inspiration</span>{links_html([("GSAP 3.13 SplitText", "https://gsap.com/blog/3-13/"), ("Codrops: animated text fills", "https://tympanus.net/Tutorials/AnimatedTextFills/index.html"), ("CSS-Tricks: SVG line drawing", "https://css-tricks.com/?p=163222"), ("Codrops: on-scroll letter animations", "https://tympanus.net/codrops/2024/01/10/experimental-on-scroll-text-animations-with-svg-clip-path/")])}</div></section>
<div class="aside"><h3>Rules for Kannada and speed</h3><ul>
<li>Use Kannada for emotional moments (tagline, founder quote, address), not every paragraph. Never fake-bold it, and don't stack the Kannada name right under the English logo.</li>
<li>Load at most three families, preload only the hero display font, and split Kannada into its own file so English visitors never download it.</li>
<li>No verified English + Kannada fashion website was found, so doing this well would be a genuine first.</li></ul>
<p>Sources: <a href="https://ultrasparky.org/blog/?p=2706" target="_blank" rel="noopener">UltraSparky on Bangalore signs</a> · <a href="https://web.dev/articles/font-best-practices" target="_blank" rel="noopener">web.dev font best practices</a></p></div>"""

JS = """
const fr=document.getElementById('fr'),ax={SOFT:100,WONK:1,wght:400};
document.querySelectorAll('[data-ax]').forEach(i=>i.addEventListener('input',()=>{ax[i.dataset.ax]=i.value;
 fr.style.fontVariationSettings=`'SOFT' ${ax.SOFT},'WONK' ${ax.WONK},'opsz' 144`;fr.style.fontWeight=ax.wght}));
"""
page("typography.html", "Typography Options", "Type", "Typography",
     "Six type systems plus what the prototype uses today, each set with the same real content: a headline, a pattern annotation, body text, a button, and Kannada and Hindi lines. Pick the one that feels like Teaching Threads.",
     body, CSS, JS, extra_fonts=FONTS_T)
