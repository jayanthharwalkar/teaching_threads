"""Hero round 3: dress form turns on scroll, clay tools float around it, a thread comes in from the left,
(v2: a measuring tape unrolls from a floating roll and wraps the bust; v1 thread kept in template-v1-thread.html). Builds hero3.html from template.html (GLB inlined)."""
import base64, os
D = os.path.dirname(os.path.abspath(__file__))
glb = base64.b64encode(open(os.path.join(D, "..", "section-options", "assets", "dress-form.glb"), "rb").read()).decode()
s = open(os.path.join(D, "template.html")).read().replace("__GLB__", "data:model/gltf-binary;base64," + glb)
open(os.path.join(D, "hero3.html"), "w").write(s)
print("hero3.html", len(s) // 1024, "KB")
