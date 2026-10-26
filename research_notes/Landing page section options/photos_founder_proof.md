# Photo Treatments, Founder Section and Proof Strip — Teaching Threads (Shruti Mahajan, Forest Fury / KFL 2016)

Scope note: 17 tool calls (searches plus one fetch). Links marked "verified via search" appeared in search results with matching titles. Not every page was fetched in full. Inferences are labelled as such. The source photos are low-res WhatsApp JPEGs of a dark runway, plus one header portrait, shown against an off-white and black-ink site.

## (A) How to make low-res, dark runway photos look intentional and premium: 7 treatments

### Takeaway
Hide the low resolution by changing what the image is: dots, ink, grain, a small print or a cut-out shape. Do not try to make it bigger and sharper. Halftone/dither, ink duotone with grain, and small contact-sheet sizing all suit the off-white/ink direction well. Each can be done with CSS or SVG filters and no WebGL. Cursor trails, hover-reveal lists and WebGL distortion are motion layers on top of one of those treatments.

### Cited Findings

**1. Halftone / dither ("reads as embroidery or cross-stitch")**
- What it looks like: the photo is rebuilt from black dots or ordered-dither pixels on off-white, like newsprint or a printed sample of a cross-stitch chart. Dark runway backgrounds turn into dense ink fields, and the figure comes out as a dot pattern.
- Why it hides low resolution: halftones are "tiny dots of varying sizes that trick your eye into seeing continuous shades," so the eye stops looking for detail — [Codrops, Efecto: real-time ASCII and dithering with WebGL shaders (Jan 2026)](https://tympanus.net/codrops/2026/01/04/efecto-building-real-time-ascii-and-dithering-effects-with-webgl-shaders)
- Pure CSS recipe: a blurred radial-gradient dot layer in `::after` with `mix-blend-mode: screen`, and `filter: brightness() blur() contrast(999)` on the container. CMYK layers can be offset — [Lean Rada, Creating a halftone effect with CSS](https://leanrada.com/notes/pure-css-halftone/)
- Three-declaration version using `background-blend-mode: multiply` + `filter: contrast(16)`. It uses mid-grey gradients so dark areas don't crush to solid black, which matters for dark runway photos — [Frontend Masters, Pure CSS Halftone Effect in 3 Declarations](https://frontendmasters.com/blog/pure-css-halftone-effect-in-3-declarations/)
- `mix-blend-mode: multiply` keeps white areas transparent while the dots stay black. Changing the background colour can distort the effect because of the contrast filter, so off-white needs a blend mode — [CSS { In Real Life }, CSS Halftone Patterns](https://css-irl.info/css-halftone-patterns/)
- Photo halftone using a grayscale blurred photo with `hard-light` and a container contrast filter — [Cloud Four, The power of CSS blend modes](https://cloudfour.com/thinks/the-power-of-css-blend-modes/)
- WebGL route: ordered dithering in GLSL with the Post Processing library and Three.js, with optional pixelation and grayscale — [Codrops, Building a Real-Time Dithering Shader (Jun 2025)](https://tympanus.net/codrops/?p=95318). Bayer dithering tutorial (Jul 2025) by Seva Dolgopolov — [Codrops author page](https://tympanus.net/codrops/author/zavalit). Codrops dithering tag hub — [tympanus.net/codrops/hub/tag/dithering](https://tympanus.net/codrops/hub/tag/dithering/)
- No-code option: the Framer "Shader Shift" component bundles Bayer dithering, luminance halftone, pixelation, film grain and liquid warp — [Framer Marketplace, Shader Shift](https://www.framer.com/marketplace/components/shader-shift/)

**2. Ink duotone / monochrome (black ink to off-white paper)**
- What it looks like: the shadows map to the site's ink black and the highlights map to the site's off-white. The photos then look printed on the page, not pasted onto it.
- Implementation: SVG `feColorMatrix` (desaturate) then `feComponentTransfer` (map the gray range to two colours) — [Codrops, SVG Filter Effects: Duotone Images with feComponentTransfer](https://tympanus.net/codrops/?p=37611); a single-matrix duotone, as in Spotify's identity — [José M. Pérez, Duotone using feColorMatrix](https://jmperezperez.com/duotone-using-fecolormatrix/); a CSS-only version with blend-mode pseudo-elements, based on Una Kravets' work and colofilter.css — [José M. Pérez, Duotone using CSS blend modes](https://jmperezperez.com/blog/duotone-using-css-blend-modes); a gradient-map `table` transfer — [Stuff & Nonsense, SVG filters for Emma's website](https://stuffandnonsense.co.uk/blog/svg-filters-for-emmas-website/)
- Why it hides low resolution: removing colour also removes WhatsApp chroma noise and banding (inference). Mapping blacks to the site's ink colour makes the dark backgrounds blend into the page.

**3. Heavy grain / film texture**
- Implementation: SVG `feTurbulence` noise as a background, with CSS brightness/contrast on top — [CSS-Tricks, grainy gradients](https://css-tricks.com/?p=351302); PNG versus inline SVG grain compared — [freeCodeCamp, Grainy CSS backgrounds using SVG filters](https://www.freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/); feTurbulence series (rough-paper textures, displacement) — [Codrops, SVG filter feTurbulence](https://tympanus.net/codrops/?p=37751)
- Parameters: opacity 0.03–0.12, with above 0.15 reading as dirt; numOctaves above 3–4 rarely justifies the performance cost; use `stitchTiles="stitch"` for seamless tiling; animated SVG grain is choppy, so use a canvas noise tile for animation — [skills.sh, noise-grain-texture](https://www.skills.sh/avnehsbhatia/ultraui/noise-grain-texture) (secondary source)
- Why it hides low resolution: uniform grain hides JPEG block artefacts and reads as a film-era runway shot (inference). It pairs well with treatment 2.

**4. Small sizing: contact sheet, polaroid or index card**
- What it looks like: 6–12 looks printed small (about 120–220px wide) in a grid with frame numbers ("FF-01 … FF-12"), look names and a red grease-pencil circle on one frame. Clicking opens one look a little larger, never full-bleed.
- Why it hides low resolution: a WhatsApp JPEG (often about 1280px on the long edge, or less) looks sharp at small display sizes. Small, dense, numbered presentation reads as archive and evidence, not as a hero image (inference; no source found for typical WhatsApp output dimensions).
- Inspiration: monochrome, whitespace-heavy portfolio systems such as Evagria (featured on Awwwards and Mindsparkle) — [UI/UX Showcase, Evagria Portfolio](https://uiuxshowcase.com/portfolio/evagria-portfolio/)

**5. Cut-out subjects on off-white**
- What it looks like: the model and garment are lifted out of the black runway and placed on off-white with a hairline shadow or none. This matches the clay-white POV objects elsewhere on the site. Cut-outs can also carry the halftone treatment.
- Tools: Clipdrop Remove Background API (free key; a third-party review says 15 free uses a month, Pro about $9/month, unverified) — [Cutout.pro on Clipdrop](https://www.cutout.pro/learn/?p=602); Photoroom Remove Background API ("complex edges, transparency"; a secondhand estimate puts it at about $0.02 per image) — [Photoroom API docs](https://docs.photoroom.com); a 2026 ranking rates remove.bg for highest accuracy — [Dupple, Best AI background removers 2026](https://dupple.com/learn/best-ai-background-removers)
- Risk: on dark runway shots, black garments and hair against a black background give poor edges. No source tested fashion-specific edges (see Gaps). Test on the actual Forest Fury frames.

**6. Motion layers: cursor image trail, hover-reveal name list, WebGL distortion**
- Cursor trail: random images follow the mouse. The effect was first seen on VLNC Studio, with 5 variants (scale and fade, drop, squeeze, fullscreen side-restricted, after Ricky Michiels) — [Codrops, Image Trail Effects (2019)](https://tympanus.net/codrops/2019/08/07/image-trail-effects); a GSAP gravity variant where images fall, bounce and disappear — [Codrops, Made With GSAP: Gravity-Based Mouse Trail](https://tympanus.net/codrops/?p=115661); Framer no-code component with trail length and lifespan settings — [Framer, Image Trail Cursor](https://www.framer.com/marketplace/components/image-trail-cursor/)
- Hover-reveal from a list: a menu where each item's image (stored in `data-img`) animates in on hover — [Codrops, Creating a Menu Image Animation on Hover (2020)](https://tympanus.net/codrops/2020/07/01/creating-a-menu-image-animation-on-hover/); link hover effects showing a thumbnail, with the repo at codrops/ImageRevealHover (TweenMax, imagesLoaded; free for commercial use) — [Codrops, Image Reveal Hover Effects](https://tympanus.net/codrops/?p=36588). A good fit is a typeset list of Forest Fury look names or KFL 2016 credits, with a small inked image following the cursor. The images stay small, which hides the low resolution.
- WebGL distortion: displacement-map hover transitions on three.js — [Codrops, WebGL Distortion Hover Effects (2018)](https://tympanus.net/codrops/2018/04/10/webgl-distortion-hover-effects/); distortion, RGB shift, trail and stretch effects using a shared EffectShell class — [Codrops, Motion Hover Effects with Image Distortions using Three.js](https://tympanus.net/codrops/?p=44003); configurator repo — [GitHub, Anemolo/WebGLDistortionConfigurator](https://github.com/Anemolo/WebGLDistortionConfigurator). No dedicated Codrops OGL tutorial was found.

**7. Horizontal runway scroll / film strip**
- An infinite scattered gallery with per-image parallax speeds, GSAP Observer, Flip transitions and SplitText — [Codrops, Infinite GSAP Scroll Gallery with Parallax and Flip (Jul 2026)](https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/); an infinite two-way parallax grid with seamless tiling — [Codrops, Infinite Parallax Grid with GSAP (Jun 2025)](https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/); Codrops infinite tag hub (includes Oct 2025 GSAP Infinite Parallax Carousel) — [tympanus.net/codrops/hub/tag/infinite](https://tympanus.net/codrops/hub/tag/infinite)
- How to adapt it: show the frames as 35mm film strip cells (sprocket holes drawn in CSS) that move horizontally as the page scrolls. Keep each cell at about 30vh tall so the low resolution holds up.

**AI upscaling (pre-processing, not a treatment)**: see the upscaling question below.

### Inferences
- Recommended stack: upscale conservatively (fidelity mode, 2x) → cut out or crop → ink duotone or halftone → grain overlay → display small (contact sheet or hover list). Only the header portrait should be shown large, and only after a duotone.
- The halftone and cross-stitch reading connects runway imagery to "threads" and craft, which gives it a stronger brand rationale than WebGL ripple.
- Photos masked in type (`background-clip: text` with "FOREST FURY" in a heavy display face) works well for dark, textured images because only colour and texture show, not detail. This was not researched or sourced in this session.
- Magazine-spread layout: one look about 40% wide with a hairline caption ("Look 07 — Forest Fury, Kerala Fashion League 2016"), facing a large pull quote. The image size stays modest.

### Gaps
- No sourced live fashion-site examples of halftone or duotone runway imagery were found (all inspirations are technique demos).
- Not found: Awwwards, Godly or Siteinspire pages with specific URLs for designer runway archives (search returned only Wix showcase sites).
- No source tested background-removal quality on dark runway or black-garment photos.
- No source was found for typical WhatsApp JPEG compression dimensions.

## (B) How fashion editorial sites, schools and designer portfolios present runway imagery and founder stories, and 4 founder-section layouts

### Takeaway
Editorial and runway sites lead with full-bleed imagery plus a written review. Schools tell founder or history stories in a plain, text-led way, with dated paragraphs and one archival photo. Teaching Threads can combine the two: restrained text carries the story and treated photos act as evidence.

### Cited Findings
- Vogue Runway uses mostly full-bleed images with white or black text overlays and a dark red accent for navigation. Each show opens to a scrollable image overview, and each collection includes a Vogue writer's review — [DesignRush, Vogue Runway app](https://www.designrush.com/best-designs/apps/vogue-runway)
- A Ralph Lauren runway landing page case study embeds the show video, links collection notes, and mixes designer quotes with close-up detail shots for an editorial feel — [Contra, Ralph Lauren](https://contra.com/p/vYBlYgeU-ralph-lauren)
- Designer portfolio pattern: full-bleed photos on dark backgrounds, collections labelled by body of work, and runway photos paired with press coverage — [Wix showcase, Samantha Tsui](https://www.wix.com/explore/websites/site/samantha-tsui); [Wix showcase, Cecilia Wolf](https://www.wix.com/explore/websites/site/cecilia-wolf)
- Polimoda's History page is a single-column, text-led narrative ("From 1986 to nowadays") organised by year. It has one archival photo of the 1986 New York signing of the founding agreement (Shirley Goodman of FIT and Marquis Emilio Pucci for the City of Florence), followed by link cards (Leadership, Fast facts, Partners) — [Polimoda, 70 years ago / History](https://www.polimoda.com/70-years-ago)
- Central Saint Martins tells faculty stories as tribute "stories" pieces. Example: Louise Wilson, Course Director of MA Fashion from 1992, who taught "a huge proportion of the world's leading fashion designers" — [UAL, Professor Louise Wilson OBE 1962–2014](https://www.arts.ac.uk/colleges/central-saint-martins/stories/professor-louise-wilson-obe-1962-to-2014). The value is framed as who she taught and her lineage, not her CV.

**Four founder-section layouts**
1. **Editorial magazine profile with pull quote**: a two-column spread. The left column holds the duotone header portrait (around 4:5, not full-bleed) with a hairline caption. The right column holds a dateline ("HUBBALLI, KARNATAKA"), a short third-person profile and one large serif pull quote in Shruti's words, then a small contact-sheet row of three Forest Fury looks. Model: the Vogue Runway "image plus writer's review" pairing (source above).
2. **Timeline from runway to academy**: a Polimoda-style dated narrative (source above) as a vertical ink rule with year markers: 2016 Kerala Fashion League, Forest Fury → studio founded → first batch → today. Each node gets one small treated image or a clay POV object. The timeline doubles as part of the proof.
3. **Letter from the founder**: an off-white paper card set in a handwriting font, or better, a scan of her real handwriting, signed with her signature. A small polaroid of Forest Fury is pinned at the corner. This is the warmest option and suits an academy with no testimonials yet. No external example was sourced (inference).
4. **Split story with sticky portrait**: the portrait (or a halftone cut-out of a look) stays pinned on the left while three short chapters scroll on the right: "The runway", "The studio", "The method". The image can swap per chapter using the hover or scroll reveal techniques in section A. This needs a CSS `position: sticky` or GSAP ScrollTrigger pin (implementation inference).

### Inferences
- Schools sell lineage ("who taught whom") and dated history. With no students yet, Shruti's runway credential is the lineage, so lead with KFL 2016 as a dated fact.
- Option 1 or 4 fits the minimal editorial direction best. Option 3 can be added on mobile or as a secondary block.

### Gaps
- Pages from SSENSE Editorial, 032c, AnOther, i-D, System, Document Journal and Vogue Runway web were not fetched. Their layout specifics are unverified, and only the Vogue Runway app review was found.
- NIFT, Pearl Academy and Parsons faculty or founder pages were not researched.

## (C) Proof-strip formats, and which upscaling tools to use (with risks)

### Takeaway
Use a slow monochrome text marquee styled as selvedge print or a measuring tape, or a static garment-care-label block. Both let a few honest facts read as craft rather than an empty-looking stats bar. For upscaling, use fidelity-oriented tools (Topaz, or Real-ESRGAN via Upscayl) at low strength. Avoid creative upscalers (Magnific, Krea at high creativity) on her face and garments, because they invent detail.

### Cited Findings — Proof strip
- Awwwards tracks the text marquee as a recurring trend: continuous right-to-left text now with "rich sets of typographies, glyphs, and icons, and vertically moving content." The collection includes "Another Lora — Fashion Designer" (honourable mention, Sep 2021), Togethxr (multi-direction scrolling) and Sick Agency — [Awwwards, Text Marquee collection](https://www.awwwards.com/awwwards_collections/collections/text-marquee-effect/); [Awwwards, Togethxr scrolling text](https://www.awwwards.com/inspiration/togethxr-scrolling-text)
- Codrops marquee and typography demos: Glowing Text Marquee (Jun 2024, clip-path/SVG), Dual Wave Text Animation on Scroll (Jan 2026, GSAP), and typographic slideshow demos — [Codrops, 4 Exclusive Demos: Slideshows & Typographic Animations](https://tympanus.net/codrops/2023/06/16/4-exclusive-demos-slideshows-typographic-animations/)

**Four formats**
1. **Selvedge or measuring-tape marquee**: a thin band with tick marks every 1cm drawn in CSS (repeating-linear-gradient) and small caps text between them: "SHOWN AT KERALA FASHION LEAGUE 2016 · FOREST FURY · [N] YEARS DESIGNING · [N] STUDENTS TRAINED · HUBBALLI STUDIO, KARNATAKA ·". It moves slowly, pauses on hover and respects `prefers-reduced-motion`. Selvedge-style text (the brand name printed along a fabric edge) gives a textile rationale (inference).
2. **Garment care label**: a static off-white woven-label card in a monospace face with care-symbol glyphs: "CONTENT: 100% studio-taught · ORIGIN: Hubballi, India · SHOWN: Kerala Fashion League 2016 · CARE: small batches, hand-finished". It works on mobile and needs no motion.
3. **Credits roll**: runway-show credits as a vertical or horizontal list ("Designer — Shruti Mahajan / Collection — Forest Fury / Show — Kerala Fashion League 2016 / Studio — Hubballi"). This combines well with the section A hover-reveal so that hovering "Forest Fury" shows an inked look.
4. **Stat counters**: numbers count up on scroll. Use them only for real numbers (years, students). With few students, counters can backfire, so prefer formats 1–3 until the numbers grow (inference).

### Cited Findings — Upscaling and restoration
- Topaz is positioned as the faithful option and Magnific's creativity slider is designed to invent detail. The wrong pick "will either smooth your photo into plastic or invent a face that is not the face in the original" — [Rangy, Topaz vs Magnific vs Crystal](https://rangy.ai/blog/topaz-vs-magnific-vs-crystal) (vendor/affiliate-style blog)
- Low Magnific creativity settings are suggested for adding skin texture, which is still generative — [Chase Jarvis, Topaz vs Magnific](https://chasejarvis.com/blog/topaz-vs-magnific-best-ai-image-scaler/)
- Krea separates fidelity upscalers (enlarge what exists, invent as little as possible, which suits real people) from creative upscalers (generate new detail; "why upscaled portraits grow strange skin") — [Krea, Best AI image upscalers in 2026](https://www.krea.ai/blog/best-ai-image-upscalers-in-2026). The Krea Enhancer has face detection with Face Creativity and Face Strength controls, and a Match colour option — [Krea docs, Enhancer](https://www.krea.ai/docs/de/user-guide/features/enhancer.md). Note that Krea is a vendor ranking its own category.
- Real-ESRGAN is cheap, fast and good on small images with compression artefacts. GFPGAN and CodeFormer are the face-restoration models usually chained with it — [Replicate, Upscale images with AI models](https://replicate.com/docs/guides/run/upscale-images-with-ai-models)
- Upscayl is a free, open-source GUI around pretrained models (Linux, macOS, Windows). An older review noted that GFPGAN face chaining was not built in, so check the current release — [LinuxLinks, Upscayl](https://www.linuxlinks.com/machine-learning-linux-upscayl-image-upscaler/2/)
- Pricing claims conflict: Topaz Photo AI is about $199 perpetual according to one source, and Magnific is SaaS — [Rangy](https://rangy.ai/blog/topaz-vs-magnific-vs-crystal)

### Inferences
- Workflow: first try Real-ESRGAN (Upscayl, free) at 2x for JPEG artefacts. Use Topaz Photo AI only if needed. Never use face restoration on Shruti's header photo without her approval, because GFPGAN and CodeFormer can change identity (general model behaviour; no source in this session). Avoid creative modes on garments, because embroidery and print motifs on Forest Fury could be invented. That would misrepresent the collection.
- Because treatments 1–4 deliberately remove detail, heavy upscaling is often unnecessary. A modest 2x denoise before halftone or duotone is enough.
- Keep the originals and label any restored image internally. Show a "2016 archive" caption to set expectations.

### Gaps
- No independent, rigorous side-by-side test of face or garment hallucination (Topaz vs Magnific vs Krea vs Real-ESRGAN) was found. Available comparisons are vendor or affiliate blogs.
- Clipdrop's upscaler was not evaluated.
- No real fashion-site example of a care-label or measuring-tape proof strip with a URL was found. Those formats are proposals.
