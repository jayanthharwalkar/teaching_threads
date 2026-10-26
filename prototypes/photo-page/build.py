"""Photo-led landing page: her runway work on a clothes rail, the press clipping, then the course.

Fills template.html with the owner's photos (embedded, since artifacts can't load local images) and writes runway.html.
Run: python3 prototypes/photo-page/build.py
"""
import base64, io, os
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# name: (file, crop as fractions l,t,r,b or None, longest side)
SRC = {
    "founder": ("photos/Show 1.jpg.jpeg", (0.015, 0.178, 0.985, 0.99), 1100),
    "cape": ("photos/IMG-20160306-WA0002.jpg.jpeg", None, 900),
    "lineup": ("photos/Header Pic.jpg.jpeg", None, 1100),
    "blue": ("photos/IMG-20161122-WA0019.jpg.jpeg", None, 900),
    "curly": ("photos/IMG-20160424-WA0007.jpg.jpeg", None, 900),
    "floral": ("photos/IMG-20170322-WA0005.jpg.jpeg", None, 900),
    "trio": ("photos/IMG-20160317-WA0000.jpg.jpeg", None, 900),
    "walk": ("photos/IMG-20160424-WA0035.jpg.jpeg", None, 900),
    "news_en": ("photos/IMG-20160316-WA0003.jpg.jpeg", None, 1040),
    "news_kn": ("photos/IMG-20160313-WA0005.jpg.jpeg", None, 1200),
    "s1": ("prototypes/assets/week-1-measure.webp", None, 420),
    "s2": ("prototypes/assets/stage-2/f040.webp", None, 420),
    "s3": ("prototypes/assets/week-2-machine.webp", None, 420),
    "s4": ("prototypes/assets/stage-4/f040.webp", None, 420),
    "s5": ("prototypes/assets/stage-5-lehenga.webp", None, 420),
}

# the rail, in hanging order: photo, tag line 1, tag line 2, alt text
RAIL = [
    ("cape", "Forest Fury", "Kerala Fashion League, 2016", "A model in a black crop top and skirt under a long floral cape"),
    ("lineup", "Forest Fury", "The full line-up on the ramp", "Models in the Forest Fury collection lined up on the Kerala Fashion League ramp"),
    ("curly", "Forest Fury", "Floral gown", "A model with curly hair in a dark floral gown on the ramp"),
    ("trio", "Forest Fury", "Three looks, one print", "Three models in dark floral dresses under blue stage light"),
    ("blue", "Kerala Fashion League", "Printed gown", "A model in a blue gown with a bright floral bodice"),
    ("floral", "Kerala Fashion League", "Lehenga and blouse", "A model in a floral lehenga skirt and an embellished blouse"),
    ("walk", "On the ramp", "Shruti with her model", "Shruti Mahajan walks the ramp beside a model in a sheer yellow outfit"),
]


def uri(name):
    path, crop, side = SRC[name]
    im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, path))).convert("RGB")
    if crop:
        W, H = im.size
        im = im.crop((int(crop[0] * W), int(crop[1] * H), int(crop[2] * W), int(crop[3] * H)))
    im.thumbnail((side, side))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode(), im.size


html = open(os.path.join(HERE, "template.html")).read()
for name in SRC:
    key = "{{" + name + "}}"
    if key in html:
        u, (w, h) = uri(name)
        html = html.replace(key, f'src="{u}" width="{w}" height="{h}"')

items = []
for i, (name, t1, t2, alt) in enumerate(RAIL, 1):
    u, (w, h) = uri(name)
    items.append(f'''<li class="item" style="--ar:{w}/{h}">
  <svg class="hook" viewBox="0 0 24 36" aria-hidden="true"><path d="M12 36V25c0-4-8-6-8-13a8 8 0 1 1 16 0"/></svg>
  <div class="bar" aria-hidden="true"><i></i><i></i></div>
  <button class="photo" type="button" aria-label="View larger: {alt}"><img src="{u}" width="{w}" height="{h}" alt="{alt}" draggable="false"></button>
  <div class="tag" aria-hidden="true"><span>No. {i:02d}</span><b>{t1}</b><span>{t2}</span></div>
</li>''')
html = html.replace("{{RAIL}}", "\n".join(items))
assert "{{" not in html, html[html.index("{{"):html.index("{{") + 40]

out = os.path.join(HERE, "runway.html")
open(out, "w").write(html)
print("wrote", out, len(html) // 1024, "KB")
