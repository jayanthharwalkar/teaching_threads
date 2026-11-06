"""Builds the home page draft: hero3.html from template.html, plus the files it loads after it shows.

The page itself stays small so the first screen paints fast. Heavy parts are separate files, loaded when needed:
  model/dress-form.js     the hero's 3D dress form (base64 GLB as a script: the artifact host blocks fetch and .glb)
  stages/<clip>.js        each stage clip's frames (base64 webp), fetched once the visitor reaches section 2
  assets/*.webp           the stage posters (first frames), lazy
  work/p*.jpg             the prints in section 2, lazy
  work/t*.webp, f*.jpg    Shruti's wall: thumbnails as cells appear, full photo on tap (made separately; list.json)
"""
import base64, json, os, re, shutil

D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, "..")  # prototypes/
s = open(os.path.join(D, "template.html")).read()

# hero model
os.makedirs(os.path.join(D, "model"), exist_ok=True)
glb = base64.b64encode(open(os.path.join(P, "section-options", "assets", "dress-form.glb"), "rb").read()).decode()
open(os.path.join(D, "model", "dress-form.js"), "w").write("__got('model',%s)" % json.dumps(glb))

# section 2 prints (placeholders until student photos come in)
for k in ("p2", "p3", "p4", "p5"):
    shutil.copy(os.path.join(P, "section2", "simple", "img", k + ".jpg"), os.path.join(D, "work", k + ".jpg"))

# stage clips: one script of frames per clip, and the posters the page shows before frames arrive
os.makedirs(os.path.join(D, "stages"), exist_ok=True)
for prefix, n in re.findall(r'data-seq="(assets/[^"]+)" data-count="(\d+)"', s):
    clip = prefix.split("/")[1]
    frames = [base64.b64encode(open(os.path.join(P, "%s%03d.webp" % (prefix, i)), "rb").read()).decode() for i in range(1, int(n) + 1)]
    open(os.path.join(D, "stages", clip + ".js"), "w").write("__got(%s,%s)" % (json.dumps(clip), json.dumps(frames)))
POSTERS = sorted(set(re.findall(r'src="(assets/[^"]+\.webp)"', s)))
for k in POSTERS:
    os.makedirs(os.path.dirname(os.path.join(D, k)), exist_ok=True)
    shutil.copy(os.path.join(P, k), os.path.join(D, k))

# Shruti's wall
W = [{k: w[k] for k in ("t", "f", "a", "c")} for w in json.load(open(os.path.join(D, "work", "list.json")))]
s = s.replace("__WORK__", json.dumps(W), 1)

assert "__" + "GLB__" not in s and "__P" not in s and "__WORK__" not in s
open(os.path.join(D, "hero3.html"), "w").write(s)
# the list publish_files needs
files = ["index.html"] + ["model/dress-form.js"] + ["stages/" + f for f in sorted(os.listdir(os.path.join(D, "stages")))] + POSTERS \
    + ["work/" + f for f in sorted(os.listdir(os.path.join(D, "work"))) if f != "list.json"]
json.dump([{"as": f, "path": os.path.join(D, "hero3.html" if f == "index.html" else f)} for f in files], open(os.path.join(D, "publish.json"), "w"))
print("hero3.html", len(s) // 1024, "KB;", len(files), "files to publish")
