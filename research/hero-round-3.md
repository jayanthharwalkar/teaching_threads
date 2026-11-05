# Hero round 3 (2026-11-02)

## Page plan (reset)

1. **Hero**: a wow moment that makes visitors scroll. Not photo-led, because there are few good photos.
2. **Numbers + outcomes**: e.g. "20 students, 17 had never touched a stitching machine, 15 opened their own boutiques, 4 work elsewhere in fashion", ideally with photos. The numbers must be real and approved by Shruti. Student counts are fine; earnings and fees are still out. Student photos need consent (boutique shopfronts are a fallback).
3. **What you will learn**: the "click a tool, read how it's used" idea fits here, not in the hero.
4. **Founder**: Shruti and her work, with photos.

## Hero decision

- Workstation/table hero: **rejected**, it didn't look nice enough.
- The user liked all the references below. The direction combines **lusion.co** and **Apple (apple.com/airpods-pro)**:
  - From Lusion: floating 3D objects, plus the **blue line that comes in from the left**. In our version that line becomes a **thread** running across the hero.
  - From Apple: one central object (the dress form) that turns and reveals more as you scroll.
- Core idea: dress form in the middle, clay-white tools floating around it (chalk, scissors, tape, spool, pins, thimble), a thread drawing in from the left, and scrolling drives the scene.

## 3D model budget

Meshy has about 80 credits left (~4 tries). Build the simple shapes in code (chalk, spool, thimble, pins), and spend Meshy only on the hard ones (scissors, tape), or try Tripo / Hunyuan3D or CC0 models from Poly Pizza or Sketchfab. Untextured clay-white suits the look.

## References shown (all liked)

Floating objects: lusion.co, shopify.com/editions, igloo.inc, landonorris.com, Awwwards elements (ELEF floating hero, KOOKIE 3D objects, Vegter hero 3D on scroll).
Workstation / click to explore: thread-and-mesh.com, craftball.loewe.com (The Atelier), my-room-in-3d.vercel.app, henryheffernan.com, andriibabintsev.com, bruno-simon.com.
Central object on scroll: apple.com/airpods-pro, teenage.engineering.

## Next step

Build hero artifacts that combine Lusion and Apple: the thread line from the left plus the floating tools and the scroll-driven dress form.

## Status (2026-11-05)

### Hero: built (`prototypes/hero3/`, `build.py` turns `template.html` into `hero3.html`)
- **Layout:** Lusion style. The logo and "Connect on WhatsApp" sit on top, with one headline under them ("Learn to make your own clothes."). Below is a rounded frame whose left and right edges sit about 10% in from the screen edges. The frame grows to full screen on scroll.
- **Scene:**
  - The camera is close, so the dress form overflows the frame.
  - The tools are code-made clay: kainchi, L-square, French curve, fabric swatch, hanger, seam ripper, buttons, pins, needle, thimble, pincushion and chalk.
  - A measuring tape unrolls from a roll on the right and wraps the bust as the form turns.
  - A spool on the left spins with scroll and wobbles (its tilt travels round the axis). Its thread waves off the left edge of the screen.
- **Backups:** earlier versions are kept as `template-v1-thread.html` to `template-v6.html`.
- **Published:** the public link (https://claude.ai/artifact/Ph5MTA7x5RVM7afHVJw19b) still shows the hero before the button section was added. The latest is https://claude.ai/artifact/Q14MmPxcFTp8pC7RT9WdYn.
- **Waiting on:**
  - Meshy models (330 credits), which wait for Arun's approval.
  - The background contrast decision, which waits for the real models.

### Section 2: numbers + outcomes
- **Rule:** never flood visitors with text. Either show the point, or reveal one line at a time.
- **First try (not stunning enough):** 20 clay buttons on the thread, with the beginners turning ink and the rest sewn onto "boutique" and "fashion jobs" cards. This is in the hero3 template.
- **Current tests in `prototypes/section2/`:**
  - **A:** `embroidered-numbers.html`, a needle satin-stitches each number into a hoop. https://claude.ai/artifact/NMCs1zt3shgXezMKCn9wjv
  - **B:** `thread-numbers.html`, a cord writes each number and dives under the cloth between digits. https://claude.ai/artifact/BJHwswzxXdTiHLqsnxZS2h
- **Numbers:** samples only (20 / 17 / 15 / 4). They need Shruti's real figures.
- **Ideas not built yet:** a miniature clay boutique street, a dress-form runway, numbers cut from cloth, a tape-measure ride.
