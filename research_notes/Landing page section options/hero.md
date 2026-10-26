# Hero Section Concepts — Teaching Threads Fashion Academy (Hubballi)

Research date: 2026-10-26. Method note: link checks used web search results (a URL returned by search = exists) plus `curl` status codes. tympanus.net (Codrops), jacquemus.com, ssense.com, esmod.com and arts.ac.uk return HTTP 403 to automated fetches (bot protection), so I could not read those pages' content. Codrops URLs below are only listed when the exact URL appeared in search results. WebFetch returns page text, not visuals, so descriptions of brand/school heroes are based on their markup and copy, not on screenshots.

## What are the most striking hero patterns (2024-2026) on fashion, design-school, atelier and editorial sites?

### Takeaway
The recurring high-craft patterns are: scroll-scrubbed image/frame sequences on a pinned canvas, giant kinetic/split typography (often with image or video inside letters), cursor image trails, scroll-driven galleries/sticky grids, and SVG line drawing on scroll. All of them can be done on an off-white page with black type. What makes the work high-craft is restraint plus one signature motion, not stacking effects.

### Cited Findings
- Scroll-scrubbed frame sequences are a standard technique. GreenSock's official helper scrubs an array of frames and draws the current one to a `<canvas>` with ScrollTrigger (`scrub: true`). — [GreenSock CodePen: Scroll-based Image Sequence](https://codepen.io/GreenSock/pen/RwvrNqN)
- In a typical implementation the container pins, frames draw to canvas as you scroll, and reduced-motion users see the first frame statically. — [GSAP Vault: Apple-style scroll image sequences](https://gsapvault.com/blog/scroll-image-sequence-tutorial)
- An open-source alternative decodes a single MP4 with the VideoDecoder API instead of shipping hundreds of JPGs. Its README includes a 300vh hero example. — [GitHub: kerimcharfi/frame-scroll-animation](https://github.com/kerimcharfi/frame-scroll-animation)
- The best-known real-world reference for a scroll-scrubbed product hero is still Apple product pages (URL live, HTTP 200). — [apple.com/airpods-pro](https://www.apple.com/airpods-pro/)
- Fashion brand with a scroll-driven hero gallery, featured on Awwwards (tags: hero, gallery, scroll, fashion). The site is martine-rose.com. — [Awwwards: Hero scroll gallery – Martine Rose](https://www.awwwards.com/inspiration/hero-scroll-gallery-martine-rose)
- Cursor image trail used by a fashion creative, on Awwwards (tags: trail effect, cursor, fashion). — [Awwwards: Cursor with trail effect – Amanda Braga](https://www.awwwards.com/inspiration/cursor-with-trail-effect-amanda-braga-fashion-creative-designer)
- Other Awwwards cursor/image-trail heroes: [OSI 90th anniversary loader + hero](https://www.awwwards.com/inspiration/loader-hero-section-osi-90th-anniversary), [Micha Brandt custom cursor hero slideshow](https://www.awwwards.com/inspiration/custom-cursor-controls-for-hero-slideshow-micha-brandt)
- Sticky hero that fades out on scroll (Awwwards element). — [Awwwards: Fade-out on scrolldown sticky hero](https://www.awwwards.com/inspiration/fade-out-on-scrolldown-sticky-hero-section-dixie-raiz-pacheco)
- Video playing inside headline type ("video text mask") is common enough to be packaged as off-the-shelf components. One approach uses an SVG of the text as a CSS `mask-image` over a video container. — [Mintlify video-text component](https://www.mintlify.com/SikandarJODD/animations/components/video-text); [Framer Video Text Mask](https://www.framer.com/marketplace/components/video-text-mask/); [Webflow: Text Masked Video Scroll Animation](https://webflow.com/made-in-webflow/website/text-masked-video-scroll-animation)
- SVG "draw on scroll" works by setting `stroke-dasharray`/`stroke-dashoffset` to `path.getTotalLength()` and animating the offset to 0, tied to scroll. — [CSS-Tricks](https://css-tricks.com/?p=163222); [GeeksforGeeks: draw on scroll with SVG](https://geeksforgeeks.org/how-to-draw-on-scroll-using-javascript-and-svg)
- Scissor-cut-along-dashed-line technique: duplicate the cut path, give it a dashed stroke, and reveal or erase it with an animated mask that tracks the scissors. — [Adobe community answer](https://community.adobe.com/t5/animate-discussions/simple-scissor-animation-removing-dash-marks-where-scissor-cuts/m-p/11049819/highlight/true)
- Client reference thesuperrco.com: the top is a scattered grid of product and prop images (filenames include "float"). The site has playful interaction copy ("Drag the line to look around", "Grab a khakhra. Fling it. Tap for more.") and a cheeky closing CTA ("That's enough scrolling. Eat the crisps."). There is no prominent button in the hero; the nearest CTA is the "Shop" link. — [thesuperrco.com](https://thesuperrco.com/)

### Inferences
- What the client likes about Superr is probably the tone (floating objects, playful verbs, humour), not conversion design. Our hero should borrow the floating-object playfulness and still add the explicit offer and CTA that Superr lacks.
- Frame-sequence scrubbing fits the existing Kling clay-POV pipeline directly: Kling clip → extract about 60-120 frames → WebP/AVIF → canvas scrub. The MP4 + VideoDecoder route cuts the payload, which matters for Hubballi mobile data.
- Each pattern maps onto a tailoring metaphor: frame scrub = the machine "sewing" as you scroll; SVG dash draw = running stitch / chalk line; clip-path reveal = scissors cutting the pattern paper; cursor trail = thread or tape following the hand; ruler ticks = measuring tape.

### Gaps
- I could not visually verify Godly picks: godly.website now redirects to recent.design (`curl` shows `https://recent.design/?ref=godly`), so I cite no Godly entries.
- I could not open or screen-record any of the Awwwards elements, so motion descriptions there come from tags only.
- I found no real-world site that uses a tape-measure ruler as the hero scroll indicator. The concept below is original and has no precedent link.

## Which patterns keep the message clear and the CTA obvious on mobile?

### Takeaway
Patterns that keep the headline and CTA as real HTML text in the first viewport (sticky headline + pinned media, split/stacked layout) stay clear on mobile. Patterns that hide the message inside motion (text only legible mid-animation, cursor trails that need a mouse, video-in-text at small sizes) need a fallback.

### Cited Findings
- Reduced-motion users should get the first frame statically, and the pin + canvas pattern supports that. — [GSAP Vault](https://gsapvault.com/blog/scroll-image-sequence-tutorial)
- Framer's Volumen Scroll Video offers a plain looping video or static photo fallback for mobile, which shows the frame-scrub hero is commonly degraded on phones. — [Framer: Volumen Scroll Video](https://www.framer.com/marketplace/components/volumen-scroll-video/)
- Full-screen imagery with minimal centered copy is described as suited to visually led products such as fashion. — [doortoonline: hero section designs 2025](https://doortoonline.com/blog/website-hero-section-designs-2025) (vendor blog, opinion)
- Indian fashion school Pearl Academy surfaces mobile-friendly conversion CTAs near the top: "Apply Now", "Call Us", "Connect on Whatsapp", "Download Brochure", and a top banner reading "2027 Admission Open!". — [pearlacademy.com](https://www.pearlacademy.com/)

### Inferences
- Cursor trails do nothing on touch. On mobile, swap them for a touch-drag trail or an auto-playing loop.
- Video-in-letters needs huge, heavy letterforms (one or two short words) to read at 375px wide. Keep the real H1 as normal text below it.
- In every concept: pin a WhatsApp pill (bottom-right or bottom bar) on mobile from the first frame. Never make the CTA depend on scroll progress.
- Keep the frame sequence to 2-3 screen-heights of scroll on mobile so the CTA and "what this is" are never more than one swipe away.

### Gaps
- I found no measured conversion data comparing these hero patterns on mobile. Claims above are design guidance, not A/B results.

## What do real fashion schools, ateliers and fashion brands do in the hero?

### Takeaway
Schools mostly run conventional news or announcement carousels with programme CTAs. Indian brands run collection carousels with "Shop Now". None of the schools checked uses a crafted, metaphor-driven hero, which leaves room for Teaching Threads to stand out. The useful thing to borrow from the schools is their CTA set (Apply / Visit / Info kit / WhatsApp).

### Cited Findings
- **Polimoda (Florence):** a rotating slideshow of three stories, each with a category label, headline, teaser and "Discover" button. The page closes with "Your Polimoda journey starts here" and three buttons, Apply / Connect / Visit, plus "Register to the next open day". — [polimoda.com](https://www.polimoda.com)
- **Domus Academy (Milan):** headline "Turn your ideas into what is next", eyebrow "New Bachelor of Arts", CTA "DISCOVER THE PROGRAMMES". Header buttons are "GET YOUR INFO KIT" and "Book an orientation". The hero image file is named OPENFITTING-HP with alt "Fashion graduate". — [domusacademy.com](https://www.domusacademy.com/)
- **Istituto Marangoni:** the hero is a news announcement ("ISTITUTO MARANGONI RIYADH BECOMES A BRANCH UNIVERSITY") with CTAs "Four Year BA Degrees" and "Master's Degree". — [istitutomarangoni.com/en](https://www.istitutomarangoni.com/en)
- **Pearl Academy (India):** "2027 Admission Open!" banner, the section "School of Complete Professionals", a stats row ("150+ International Awards", "15K+ Successful Alumni"…), and CTAs including "Connect on Whatsapp". — [pearlacademy.com](https://www.pearlacademy.com/)
- **NIFT:** site live (HTTP 200), but I did not analyse the hero content. — [nift.ac.in](https://nift.ac.in/)
- **Parsons / CSM / ESMOD:** bot-blocked (429/403), so I could not analyse them. — [newschool.edu/parsons](https://www.newschool.edu/parsons/), [arts.ac.uk CSM](https://www.arts.ac.uk/colleges/central-saint-martins), [esmod.com](https://www.esmod.com/en)
- **Sabyasachi:** full-width looping video hero with the headline "BENGAL BYZANTINE BROADWAY", a "WATCH NOW" CTA and the quote "For culture to be relevant, it needs to be dynamic." Below it, the heading + "EXPLORE" + media pattern repeats. — [sabyasachi.com](https://sabyasachi.com/)
- **Raw Mango:** a four-slide still-image carousel (BHITTI CHITRA, DIWALI EDIT, READY TO SHIP, LEHENGAS), each with "SHOP NoW", and separate desktop and mobile crops. — [rawmango.com](https://rawmango.com/)
- **Anavila:** a rotating image carousel with separate desktop and mobile banners, no headline, the tagline "In between the pink and the blue", and category tiles below. — [anavila.com](https://www.anavila.com/)
- **Bode:** a seasonal illustrated banner ("Pumpkin Tees", CTA "SHOP PUMPKIN TEES"), so its hero is a merchandising slot. — [bode.com](https://bode.com/)
- **The Row:** live (HTTP 200), not analysed in detail. — [therow.com](https://www.therow.com/)

### Inferences
- The pattern "headline + one primary CTA + secondary 'Book a visit/orientation'" from Domus and Polimoda translates directly into "WhatsApp us" + "Book a studio visit".
- The Sabyasachi pattern (big serif headline over looping craft video, plus a one-line quote) is the closest luxury-Indian precedent for putting a founder quote in the hero.
- Separate desktop and mobile crops (Raw Mango, Anavila) are standard practice. Plan separate portrait Kling renders for mobile rather than cropping landscape.

### Gaps
- I could not see Jacquemus or SSENSE (403), Péro (the domain I tried did not resolve), Parsons, CSM or ESMOD, so I make no claims about their heroes.

## Which Codrops demos are relevant?

### Takeaway
There are Codrops tutorials for every building block: on-scroll typography, SVG clip-path text, letter stagger reveals, SVG shape/line animation on scroll, image trails, sticky grid scroll, layered zoom, and 2026 typographic "ghost trails". These are the build references for the concepts below.

### Cited Findings (URLs confirmed via search results; pages 403 to automated fetch)
- Image Trail Effects (2019, cursor-follow images, five variants): https://tympanus.net/codrops/2019/08/07/image-trail-effects
- Some More On-Scroll Typography Animations (Feb 2023, perspective/sequenced type): https://tympanus.net/codrops/2023/02/22/some-more-on-scroll-typography-animations
- 4 Exclusive Demos: Slideshows & Typographic Animations (Jun 2023, includes an on-scroll letter animation modelled on EPIC's site): https://tympanus.net/codrops/2023/06/16/4-exclusive-demos-slideshows-typographic-animations/
- Double Image Hover Effects with Clip-Path Animations (Mar 2023): https://tympanus.net/codrops/2023/03/01/double-image-hover-effects-with-clip-path-animations/
- Experimental On-Scroll Text Animations with SVG Clip-Path (Jan 2024, knockout text, letters moving on scroll): https://tympanus.net/codrops/2024/01/10/experimental-on-scroll-text-animations-with-svg-clip-path/
- Making Stagger Reveal Animations for Text (2020, GSAP + Splitting.js): https://tympanus.net/codrops/2020/06/17/making-stagger-reveal-animations-for-text/
- How to Animate SVG Shapes on Scroll (2022): https://tympanus.net/codrops/2022/06/08/how-to-animate-svg-shapes-on-scroll/
- Dynamic CSS Masks with Custom Properties and GSAP (2021): https://tympanus.net/codrops/2021/05/04/dynamic-css-masks-with-custom-properties-and-gsap/
- How to Create (Animated) Text Fills (2015, image/video inside type): https://tympanus.net/codrops/2015/02/16/create-animated-text-fills/
- Building a Layered Zoom Scroll Effect with GSAP ScrollSmoother and ScrollTrigger (Oct 2025): https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/
- How to Build Cinematic 3D Scroll Experiences with GSAP (Nov 2025): https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/
- Building a Scroll-Driven Dual-Wave Text Animation with GSAP (Jan 2026): https://tympanus.net/codrops/2026/01/15/building-a-scroll-driven-dual-wave-text-animation-with-gsap/
- Building a Scroll-Revealed WebGL Gallery with GSAP, Three.js, Astro and Barba.js (Feb 2026): https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/
- Sticky Grid Scroll: Building a Scroll-Driven Animated Grid (Mar 2026): https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/
- Typography That Leaves a Trace: Scroll-Driven Ghost Trails with GSAP (Oct 2026; each letter built from a filled glyph and an outlined version, drawn on canvas): https://tympanus.net/codrops/2026/10/13/scroll-driven-ghost-trails/
- Codrops demo hub, scroll tag: https://tympanus.net/codrops/hub/tag/scroll/
- Codrops also published a write-up on DICH™, a digital fashion experience by BL/S built with Webflow, GSAP and Spline. The search surfaced it, but I did not obtain the exact URL. (Awwwards shows DICH™ Fashion with a SOTD badge dated 9 June 2025, but that pairing was ambiguous in the listing.)

### Inferences
- "Ghost trails" (filled + outline glyph) is the closest existing demo to "chalk outline → sewn letter": the outline is the tailor's chalk mark, the fill is the finished seam.
- "Experimental SVG clip-path text" plus "Dynamic CSS masks" give the "scissors cut opens the page" mechanic.

### Gaps
- "Ideas for Image Motion Trail Animations" (Codrops, Oct 2023) is cited by other sites, but I could not confirm its exact URL, so it is not linked.

## What are 5-7 concrete hero concepts for Teaching Threads?

### Takeaway
Seven concepts follow, ordered from most to least recommended. Every one keeps the same fixed information layer. This layer is plain HTML, visible at load, and never gated by animation:
- Eyebrow: "Teaching Threads Fashion Academy · Hubballi"
- H1
- One line naming "3-month & 6-month courses · Measure → Draft → Stitch → Blouse → Lehenga"
- Primary CTA: "Enquire on WhatsApp"
- Secondary CTA: "Book a studio visit"

On mobile, a sticky WhatsApp pill also sits bottom-right from the first frame.

### Cited Findings (inspiration per concept; mechanics sourced above)

**Concept 1 — "The Seam" (scroll-scrubbed sewing machine POV, sticky headline).** *Recommended primary.*
- **What the visitor sees:** off-white page, black serif H1 at left and top. A clay-white sewing machine POV sits centre-right on the same page colour. As you scroll, the Kling clip scrubs frame by frame: the needle runs and a black running-stitch line exits the presser foot. The line becomes an SVG dashed stroke that keeps drawing across the page (stroke-dashoffset tied to the same ScrollTrigger) and underlines the H1, then continues down into the course section as the thread connecting the five stages.
- **Explains the offer:** the H1 and stage line are static. As the seam passes each stage label (Measure · Draft · Stitch · Blouse · Lehenga), that label ticks from grey to black.
- **CTA:** two buttons under the subline, both visible at load. The stitch line ends at the WhatsApp button "knot" at the end of the hero pin.
- **Photos/video:** Kling clay POV only. No runway photos here; they come later.
- **Type:** large high-contrast serif H1 (Fraunces / Instrument Serif style), small mono or grotesk eyebrow.
- **Inspiration:** [GreenSock image sequence](https://codepen.io/GreenSock/pen/RwvrNqN); [Apple AirPods Pro](https://www.apple.com/airpods-pro/); [Codrops SVG shapes on scroll](https://tympanus.net/codrops/2022/06/08/how-to-animate-svg-shapes-on-scroll/); [Awwwards sticky hero fade](https://www.awwwards.com/inspiration/fade-out-on-scrolldown-sticky-hero-section-dixie-raiz-pacheco)
- **Mobile:** portrait Kling render, 2 screen-heights of pin max, first frame as poster.

**Concept 2 — "Kainchi Cut" (scissors cut open the pattern paper).**
- **What the visitor sees:** the load screen is a sheet of pattern paper: off-white with a faint 1cm grid, chalk notches and a dashed cutting line drawn in a blouse-front curve. The H1 is printed on the paper like pattern markings ("CUT 2 · ON FOLD" grain-line labels as micro-type). On scroll or after 1.2s, clay-white kainchi (Kling POV loop) travel along the dashed line. The dashes erase behind the blades, the paper piece lifts away (clip-path follows the cut), and a Kling clay dress form appears underneath, wearing that cut piece.
- **Explains the offer:** grain-line annotations are real copy, e.g. "3 MONTHS · 6 MONTHS", "HUBBALLI STUDIO", "BEGINNERS WELCOME".
- **CTA:** on the paper, styled as a pattern label/tag. It remains after the cut.
- **Photos/video:** Kling kainchi + dress form.
- **Type:** mono or stencil caps for pattern notes, serif for H1.
- **Inspiration:** [Codrops SVG clip-path text](https://tympanus.net/codrops/2024/01/10/experimental-on-scroll-text-animations-with-svg-clip-path/); [Codrops dynamic CSS masks](https://tympanus.net/codrops/2021/05/04/dynamic-css-masks-with-custom-properties-and-gsap/); [Adobe dashed-line scissor mask method](https://community.adobe.com/t5/animate-discussions/simple-scissor-animation-removing-dash-marks-where-scissor-cuts/m-p/11049819/highlight/true)
- **Mobile:** the cut auto-plays once on load (no scroll gating). Reduced-motion users get the post-cut state.

**Concept 3 — "Chalk to Stitch" kinetic headline.**
- **What the visitor sees:** a giant two-line H1 ("Learn to make / what you wear.") first appears as a tailor's-chalk outline only: dusty, slightly broken stroke. On scroll the outline is overstitched: a running-stitch fill sews along each glyph, and the fill turns solid black ink. A small clay POV of a needle and thread pulls the stitch along (Kling loop, positioned at the leading letter).
- **Explains the offer:** the subline and the five-stage list are static below.
- **CTA:** buttons fixed below the H1.
- **Type:** an outline/fill pair of the same display face (filled + outlined glyph), exactly as in the Codrops ghost-trails build.
- **Inspiration:** [Codrops Ghost Trails (Oct 2026)](https://tympanus.net/codrops/2026/10/13/scroll-driven-ghost-trails/); [Codrops stagger text reveal](https://tympanus.net/codrops/2020/06/17/making-stagger-reveal-animations-for-text/); [Codrops on-scroll typography](https://tympanus.net/codrops/2023/02/22/some-more-on-scroll-typography-animations)
- **Mobile:** works well because it is type-only and lightweight.

**Concept 4 — "Inchi Tape" (measuring-tape ruler hero + scroll indicator).**
- **What the visitor sees:** a clay-white measuring tape (Kling POV) unrolls horizontally across the hero as you scroll. Its tick marks are live HTML and become the progress bar for the page. Numbers on the tape mark the stages: 0" Measure, 12" Draft, 24" Stitch, 36" Blouse, 48" Lehenga, and the 3-month and 6-month points are flagged on the tape. The H1 sits above the tape: "Every garment starts with a measurement."
- **Explains the offer:** the tape is the course timeline.
- **CTA:** the tape end-tab (the metal tip) is the WhatsApp button.
- **Inspiration:** no direct precedent found (see Gaps). Mechanics from [Codrops Sticky Grid Scroll](https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/) and [Codrops Layered Zoom Scroll](https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/); playful object handling from [thesuperrco.com](https://thesuperrco.com/)
- **Mobile:** the tape runs vertically down the right edge as a scroll ruler.

**Concept 5 — "Thread Trail" (cursor/touch trail of the founder's work).**
- **What the visitor sees:** a minimal static hero: H1, sub, CTAs, and a clay dress form POV at rest. Moving the cursor spools out a black thread, and along it drop small cards. The cards show Forest Fury runway shots (treated as duotone ink on off-white to hide the low-res, dark WhatsApp origin), student blouses, and zardozi close-ups. The thread is the physical link between the visitor's hand and the work.
- **Explains the offer:** a text card follows the cursor: "Shruti Mahajan · Kerala Fashion League 2016 · now teaching in Hubballi".
- **CTA:** static.
- **Photos:** the best use of the low-res runway photos, because small trail thumbnails (~180px) hide resolution limits.
- **Inspiration:** [Codrops Image Trail Effects](https://tympanus.net/codrops/2019/08/07/image-trail-effects); [Awwwards fashion cursor trail – Amanda Braga](https://www.awwwards.com/inspiration/cursor-with-trail-effect-amanda-braga-fashion-creative-designer); [Awwwards OSI image trail hero](https://www.awwwards.com/inspiration/loader-hero-section-osi-90th-anniversary)
- **Mobile:** a touch-drag trail, or an auto-play thread that loops a 5-card sequence.

**Concept 6 — "Through the Needle's Eye" (type mask zoom).**
- **What the visitor sees:** the giant word "THREADS" (or "SILAI") fills the viewport in black. Inside the letters plays the Kling clay POV loop (machine → dress form → lehenga). On scroll, the camera zooms through the counter of a letter, framed like the eye of a needle, and lands on the full-bleed clay studio scene with the H1 and CTAs.
- **Explains the offer:** the H1 + subline appear at the end of the zoom. To keep the message clear, the eyebrow and CTA stay pinned top and bottom during the zoom.
- **Inspiration:** [Codrops animated text fills](https://tympanus.net/codrops/2015/02/16/create-animated-text-fills/); [Codrops Layered Zoom Scroll](https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/); [Webflow text-masked video scroll](https://webflow.com/made-in-webflow/website/text-masked-video-scroll-animation)
- **Mobile risk:** highest of all seven concepts. Use a 1-word mask at 40vw+ letter height.

**Concept 7 — "Lookbook Split" (founder credibility + course).**
- **What the visitor sees:** split screen. Left: off-white, black serif H1, offer, CTAs (static, pinned). Right: a sticky stack of images that swap on scroll: Forest Fury runway (dark, framed like a printed magazine plate with a caption "Forest Fury, Kerala Fashion League, 2016"), then clay POV stage stills, then a student's first blouse. This alternates the founder's runway credentials with the beginner journey.
- **Explains the offer:** most directly of all seven: credentials + course in one view.
- **Inspiration:** [Awwwards Martine Rose hero scroll gallery](https://www.awwwards.com/inspiration/hero-scroll-gallery-martine-rose); [Codrops Sticky Grid Scroll](https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/); [Sabyasachi headline + quote over media](https://sabyasachi.com/)
- **Mobile:** stacks into headline → image card swiper → CTA.

### Inferences
- Best combination: Concept 1 (The Seam) as the hero, with Concept 3's chalk-to-stitch H1 treatment applied to the headline and Concept 4's tape as the mobile scroll indicator. Use Concept 5's thread trail for an "About Shruti" section rather than the hero, so the runway photos are used where their low resolution is hidden.
- The dark, low-res runway photos clash with the off-white clay direction if shown large. Use them small, as printed "plates" with captions, or as duotone thumbnails.
- One signature motion per hero. Concepts 2 and 6 are the most "wow" but carry the most risk to clarity and load time.

### Gaps
- No load-time or bandwidth testing has been done for the frame sequences on Indian mid-range Android. Recommend a test against a ~1.5MB hero budget for first paint.

## What hero copy patterns (headline formulas) work for course/academy sites?

### Takeaway
Lead with the outcome, add an honest timeframe and a credibility or locality signal, and state the format plainly in the subline. Academy precedent (Domus: "Turn your ideas into what is next") uses aspiration in the H1 and puts specifics in the eyebrow and CTA.

### Cited Findings
- Formula: specific outcome + timeframe + credibility signal (e.g. "Master Food Photography in 30 Days"). — [Teachery](https://www.teachery.co/blog/online-course-landing-page-examples)
- "Get [specific result] in [timeframe]": the timeframe must be honest and concrete, not "in minutes". — [Landing Doctor: hero headline formulas](https://landingdoctors.com/guides/hero-headline-formulas)
- A strong headline combines a clear offer, a specific benefit and a hook (number, timeframe, pain point). Write 3-5 variants and test them. — [Personizely](https://www.personizely.net/glossary/landing-page-headline)
- Lead with the result, not "Online course on…". — [FreshLearn](https://blog.freshlearn.com/blog/sales-landing-page-for-online-course)
- Real academy examples: Domus "Turn your ideas into what is next" + "DISCOVER THE PROGRAMMES" / "Book an orientation" ([domusacademy.com](https://www.domusacademy.com/)); Polimoda "Your Polimoda journey starts here" + Apply / Connect / Visit ([polimoda.com](https://www.polimoda.com)); Pearl "2027 Admission Open!" + "Connect on Whatsapp" ([pearlacademy.com](https://www.pearlacademy.com/))

### Inferences (draft headlines for Teaching Threads; my own copy)
- Outcome + timeframe: "Stitch your first blouse in 3 months." / "From measuring tape to lehenga in 6 months."
- Aspiration + specific subline: "Learn to make what you wear." Sub: "3- and 6-month fashion design & tailoring courses in Hubballi, taught by designer Shruti Mahajan."
- Process-as-promise (matches the five stages): "Measure. Draft. Stitch. Wear it."
- Credibility-led: "From the Kerala Fashion League runway to your first stitch."
- Beginner reassurance in the eyebrow or microcopy: "No experience needed · Small batches · Hubballi studio".
- CTA labels: "Enquire on WhatsApp" (primary), "Book a studio visit" (secondary). Optionally offer Kannada/Hindi microcopy for the local audience.

### Gaps
- I found no source with measured conversion data for course-site headline formulas. The sources are vendor and marketing blogs, so treat them as illustrative.
