"""Infinity photo gallery test: Shruti's work on a figure-eight loop, or on an endless wall.

Builds infinity.html from template.html. Only 8 photos exist so far, so each one is repeated;
swap PHOTOS for the owner's full set when it arrives.
"""
import base64, io, os
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# file, crop (l,t,r,b fractions) or None. Press clippings are left out: this wall is clothes on people.
PHOTOS = [
    ("photos/Show 1.jpg.jpeg", (0.015, 0.178, 0.985, 0.99)),
    ("photos/IMG-20160306-WA0002.jpg.jpeg", None),
    ("photos/IMG-20160317-WA0000.jpg.jpeg", None),
    ("photos/IMG-20160424-WA0007.jpg.jpeg", None),
    ("photos/IMG-20160424-WA0035.jpg.jpeg", None),
    ("photos/IMG-20161122-WA0019.jpg.jpeg", None),
    ("photos/IMG-20170322-WA0005.jpg.jpeg", None),
    ("photos/Header Pic.jpg.jpeg", (0.25, 0.0, 0.95, 1.0)),
]


def uri(path, crop):
    im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, path))).convert("RGB")
    if crop:
        W, H = im.size
        im = im.crop((int(crop[0] * W), int(crop[1] * H), int(crop[2] * W), int(crop[3] * H)))
    im.thumbnail((720, 720))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=76, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


srcs = ",\n".join(f'"{uri(p, c)}"' for p, c in PHOTOS)
html = open(os.path.join(HERE, "template.html")).read().replace("/*PHOTOS*/", srcs)
open(os.path.join(HERE, "infinity.html"), "w").write(html)
print("wrote infinity.html", len(html) // 1024, "KB")
