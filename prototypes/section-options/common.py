"""Shared frame for the section-option pages. Each page = intro + options, each option = live mock + notes + links."""
import base64, io, os
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.dirname(os.path.abspath(__file__))

PHOTOS = {
    "lineup": "photos/Header Pic.jpg.jpeg",
    "cape": "photos/IMG-20160306-WA0002.jpg.jpeg",
    "news_kn": "photos/IMG-20160313-WA0005.jpg.jpeg",
    "news_en": "photos/IMG-20160316-WA0003.jpg.jpeg",
    "trio": "photos/IMG-20160317-WA0000.jpg.jpeg",
    "curly": "photos/IMG-20160424-WA0007.jpg.jpeg",
    "walk": "photos/IMG-20160424-WA0035.jpg.jpeg",
    "floral_blue": "photos/IMG-20161122-WA0019.jpg.jpeg",
    "floral": "photos/IMG-20170322-WA0005.jpg.jpeg",
    "brand": "photos/Show 1.jpg.jpeg",
    "dressform": "prototypes/assets/scene-1-dress-form.webp",
    "lehenga": "prototypes/assets/stage-5-lehenga.webp",
    "measure": "prototypes/assets/week-1-measure.webp",
    "machine": "prototypes/assets/week-2-machine.webp",
    "cut": "prototypes/assets/week-3-cut.webp",
}
# crop boxes as fractions (l, t, r, b)
CROPS = {"portrait": ("brand", (0.52, 0.24, 0.98, 0.93))}

_cache = {}


def img(name, w=520, q=72):
    key = (name, w)
    if key in _cache:
        return _cache[key]
    if name in CROPS:
        src, (l, t, r, b) = CROPS[name]
        im = Image.open(os.path.join(ROOT, PHOTOS[src]))
        im = ImageOps.exif_transpose(im).convert("RGB")
        W, H = im.size
        im = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
    else:
        im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, PHOTOS[name]))).convert("RGB")
    im.thumbnail((w, w * 2))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=q, optimize=True)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    _cache[key] = uri
    return uri


def T(s, **kw):
    for k, v in kw.items():
        s = s.replace("{{" + k + "}}", str(v))
    return s


FONTS = ("https://fonts.googleapis.com/css2?family=Instrument+Sans:wdth,wght@75..100,400..700"
         "&family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500&family=Anek+Kannada:wdth,wght@75..125,300..700"
         "&family=Caveat:wght@500&display=swap")

GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E"
         "%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E"
         "%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

BASE_CSS = """
:root{
  /* Layout: a spec-sheet page; each option is a live brand mock with notes beneath. Chrome follows theme, mocks keep the brand paper. */
  --bg:#ebeae6; --fg:#1b1a18; --muted:#66635d; --line:#d3d0c9; --card:#f8f7f4; --chip:#dedbd4;
  --paper:#f5f4f0; --ink:#161514; --pencil:#8c887f; --rule:#d8d4cc;
  --serif:"Instrument Serif", "Iowan Old Style", Georgia, serif;
  --sans:"Instrument Sans", "Helvetica Neue", Arial, sans-serif;
  --mono:"IBM Plex Mono", ui-monospace, Menlo, monospace;
  --kn:"Anek Kannada", "Noto Sans Kannada", "Tunga", sans-serif;
  --hand:"Caveat", "Bradley Hand", cursive;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141413;--fg:#ebe9e4;--muted:#9d9a93;--line:#34332f;--card:#1c1c1a;--chip:#2b2a27;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#141413;--fg:#ebe9e4;--muted:#9d9a93;--line:#34332f;--card:#1c1c1a;--chip:#2b2a27;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:15px;line-height:1.55;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px}
.wrap{max-width:1080px;margin:0 auto;display:flex;flex-direction:column;gap:56px}
a{color:inherit;text-underline-offset:3px;text-decoration-thickness:1px}
a:focus-visible,button:focus-visible{outline:2px solid currentColor;outline-offset:2px}
header.page{display:grid;gap:14px;border-bottom:1px solid var(--line);padding-bottom:28px}
.kicker{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
header.page h1{font-family:var(--serif);font-weight:400;font-size:clamp(40px,7vw,76px);line-height:.98;margin:0;letter-spacing:-.01em;text-wrap:balance}
header.page p{max-width:64ch;margin:0;color:var(--muted)}
.legend{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;color:var(--muted)}
.tag{display:inline-flex;align-items:center;gap:6px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
  padding:3px 8px;border-radius:2px;background:var(--chip);color:var(--fg);white-space:nowrap}
.tag.rec{background:var(--fg);color:var(--bg)}
.tag.orig{background:transparent;border:1px dashed var(--muted)}
section.opt{display:grid;gap:16px}
.opt-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.opt-letter{font-family:var(--serif);font-size:54px;line-height:.8}
.opt-name{font-family:var(--serif);font-size:30px;line-height:1.05;margin:0;font-weight:400}
.opt-tags{display:flex;gap:6px;flex-wrap:wrap}
.notes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;font-size:14px}
.notes h4{margin:0 0 4px;font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:500}
.notes p{margin:0}
.links{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13.5px;align-items:baseline;border-top:1px solid var(--line);padding-top:12px}
.links .kicker{margin-right:4px}
.links a::after{content:" ↗";font-size:11px;color:var(--muted)}
.aside{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:18px 20px;font-size:14px;display:grid;gap:8px}
.aside h3{margin:0;font-family:var(--serif);font-weight:400;font-size:24px}
.aside p,.aside ul{margin:0}
.aside ul{padding-left:18px}
@media (max-width:720px){.notes{grid-template-columns:1fr;gap:12px}.opt-letter{font-size:42px}.opt-name{font-size:25px}}

/* ---------- the brand mock ---------- */
.mock{background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:4px;overflow:hidden;position:relative;
  container-type:inline-size;font-family:var(--sans)}
.mock .chrome{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 16px;border-bottom:1px solid var(--rule);
  font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--pencil)}
.mock .chrome b{color:var(--ink);font-weight:500}
.mock .eyebrow{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--pencil)}
.mock .h1{font-family:var(--serif);font-weight:400;font-size:clamp(34px,6.2cqi,64px);line-height:.96;margin:0;letter-spacing:-.01em;text-wrap:balance}
.mock .h2{font-family:var(--serif);font-weight:400;font-size:clamp(28px,4.6cqi,46px);line-height:1;margin:0}
.mock .sub{font-size:14px;line-height:1.5;max-width:44ch;margin:0;color:#3d3b37}
.mock .btn{display:inline-flex;align-items:center;gap:8px;background:var(--ink);color:var(--paper);font-size:13px;font-weight:600;
  padding:11px 16px;border-radius:999px;border:1px solid var(--ink);white-space:nowrap;cursor:pointer;font-family:var(--sans)}
.mock .btn.ghost{background:transparent;color:var(--ink)}
.mock .ctas{display:flex;gap:8px;flex-wrap:wrap}
.mock .mono{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase}
.mock .ph{font-family:var(--mono);font-size:10px;letter-spacing:.06em;color:#9a5b2e;background:#f1e6da;padding:1px 5px;border-radius:2px;text-transform:none}
.mock img{display:block;max-width:100%}
.duo{background:var(--paper);position:relative;overflow:hidden}
.duo img{filter:grayscale(1) contrast(1.18) brightness(1.06);mix-blend-mode:multiply;width:100%;height:100%;object-fit:cover}
.duo.grain::after{content:"";position:absolute;inset:0;background-image:""" + GRAIN + """;opacity:.14;mix-blend-mode:multiply;pointer-events:none}
.clay{width:100%;height:100%;object-fit:cover}
@media (prefers-reduced-motion: reduce){.mock *,.mock *::before,.mock *::after{animation:none!important;transition:none!important}}
"""


def links_html(links):
    return "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in links)


def option(letter, name, mock, see, why, mobile, links, rec=False, original=False, runner=False):
    tags = ""
    if rec:
        tags += '<span class="tag rec">Recommended</span>'
    if runner:
        tags += '<span class="tag">Runner-up</span>'
    if original:
        tags += '<span class="tag orig">Original idea</span>'
    return f"""
<section class="opt" id="opt-{letter.lower()}">
  <div class="opt-head"><span class="opt-letter">{letter}</span><h2 class="opt-name">{name}</h2><div class="opt-tags">{tags}</div></div>
  <div class="mock">{mock}</div>
  <div class="notes">
    <div><h4>What you see</h4><p>{see}</p></div>
    <div><h4>Why it works</h4><p>{why}</p></div>
    <div><h4>On mobile</h4><p>{mobile}</p></div>
  </div>
  <div class="links"><span class="kicker">Inspiration</span>{links_html(links)}</div>
</section>"""


def page(fname, title, num, section, intro, body, css="", js="", extra_fonts=""):
    fonts = FONTS if not extra_fonts else extra_fonts
    html = f"""<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<style>{BASE_CSS}{css}</style>
<div class="wrap">
<header class="page">
  <span class="kicker">Teaching Threads · Landing page options · {num}</span>
  <h1>{section}</h1>
  <p>{intro}</p>
  <div class="legend"><span><span class="tag rec">Recommended</span> my pick</span><span><span class="tag orig">Original idea</span> no real-world example found, the links are the closest techniques</span><span><span class="ph">orange</span> = placeholder to confirm with Shruti</span></div>
</header>
{body}
</div>
<script>{js}</script>
"""
    path = os.path.join(OUT, fname)
    with open(path, "w") as f:
        f.write(html)
    print(fname, round(len(html) / 1024), "KB")
