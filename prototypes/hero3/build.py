"""Hero round 3: dress form turns on scroll, clay tools float around it, a thread comes in from the left,
(v2: a measuring tape unrolls from a floating roll and wraps the bust; v1 thread kept in template-v1-thread.html). Builds hero3.html from template.html (GLB inlined)."""
import base64, os
D = os.path.dirname(os.path.abspath(__file__))
glb = base64.b64encode(open(os.path.join(D, "..", "section-options", "assets", "dress-form.glb"), "rb").read()).decode()
s = open(os.path.join(D, "template.html")).read().replace("__GLB__", "data:model/gltf-binary;base64," + glb)
# numbers section photos (placeholders until student photos come in)
for k in ("P2", "P3", "P4", "P5"):
    img = base64.b64encode(open(os.path.join(D, "..", "section2", "simple", "img", k.lower() + ".jpg"), "rb").read()).decode()
    s = s.replace("__%s__" % k, "data:image/jpeg;base64," + img)
# the five stages: embed every frame and still the page uses, so it publishes as one file
import re
A = os.path.join(D, "..")
F = {}
for prefix, n in re.findall(r'data-seq="(assets/[^"]+)" data-count="(\d+)"', s):
    for i in range(1, int(n) + 1):
        k = "%s%03d.webp" % (prefix, i)
        F[k] = "data:image/webp;base64," + base64.b64encode(open(os.path.join(A, k), "rb").read()).decode()
for k in set(re.findall(r'src="(assets/[^"]+\.webp)"', s)):
    s = s.replace('src="%s"' % k, 'src="data:image/webp;base64,%s"' % base64.b64encode(open(os.path.join(A, k), "rb").read()).decode())
s = s.replace("<script>\n(function () {\n  // the stages section", "<script>window.__F=" + __import__("json").dumps(F) + ";</script>\n<script>\n(function () {\n  // the stages section", 1)
assert "window.__F=" in s, "frame map not injected"
# Shruti's work: the wall's list (thumbnails and full photos stay separate files, loaded only when needed)
W = [{k: w[k] for k in ("t", "f", "a", "c")} for w in __import__("json").load(open(os.path.join(D, "work", "list.json")))]
s = s.replace("__WORK__", __import__("json").dumps(W), 1)
open(os.path.join(D, "hero3.html"), "w").write(s)
print("hero3.html", len(s) // 1024, "KB")
