# Typography directions for Teaching Threads Fashion Academy (minimal editorial, tailoring-led, English + Kannada/Hindi)

Research date: 2026-10-26. Font metadata (designers, variable axes, scripts, date added) was checked directly against the Google Fonts metadata endpoint (https://fonts.google.com/metadata/fonts) and the Fontshare API (https://api.fontshare.com/v2/fonts). The thesuperrco.com font stack was read from its live CSS (https://thesuperrco.com/css/base.css).

---

## Q1. What type pairings do fashion brands, fashion magazines and fashion schools use, and which 5-6 type systems fit Teaching Threads?

### Takeaway
Fashion print uses a high-contrast Didone or editorial serif for display, a neutral grotesk for text and UI, and often a third utility face. The reference site the client likes (thesuperrco.com) does not use a serif. It uses a condensed poster sans (Anton), a friendly grotesk (Plus Jakarta Sans) and a handwriting accent (Reenie Beanie), all free Google Fonts that it hosts itself. Every system below can be built free from Google Fonts or Fontshare, with Kannada and Devanagari companions that are confirmed to exist on Google Fonts.

### Cited Findings

**What the reference site and the fashion world actually use**
- thesuperrco.com hosts three Google-origin families itself: `--display: 'Anton', 'Arial Narrow'`, `--body: 'Plus Jakarta Sans', 'Segoe UI', system-ui` and `--hand: 'Reenie Beanie', 'Bradley Hand', cursive`. Display text is uppercase with `letter-spacing: .5px; line-height: 1.02`. It uses `font-display: swap` and ships a separate one-glyph WOFF2 just for the rupee sign (`unicode-range: U+20B9`), because the Latin subsets have no ₹. — [thesuperrco.com base.css](https://thesuperrco.com/css/base.css) (checked live; homepage [thesuperrco.com](https://thesuperrco.com))
- Harper's Bazaar (2021 redesign) uses NewParis, a Didone, as its main titling face, SangBleu OG Serif for body text, and an unidentified grotesk (a commenter suggests Helvetica Now). — [Fonts In Use: Harper's Bazaar 2021 redesign](https://fontsinuse.com/uses/43467/harper-s-bazaar-2021-redesign)
- Vogue Taiwan set headlines in Fino, a Didone, and small callouts in Fino Sans, a matched serif and sans from the same family. — [TypeTogether: Fino in Vogue Taiwan](https://www.type-together.com/2021-fino-vogue)
- Didone hairlines break down at small sizes, so these faces should stay at display sizes. — [MadeGood Designs: Bodoni font pairing](https://madegooddesigns.com/bodoni-font-pairing/)
- Central Saint Martins uses "CSM Shifts", a custom typeface made with Colophon Foundry. It has three styles (historic, contemporary, futuristic) that a coded algorithm swaps between. — [Design Week](https://www.designweek.co.uk/central-saint-martins-new-identity/)
- Parsons / The New School uses "Neue", a bespoke Pentagram typeface. It mixes regular, extended and very extended widths of one font in the same setting. — [Pentagram: The New School](https://www.pentagram.com/work/the-new-school/story); [designboom](https://www.designboom.com/design/the-new-school-identity-by-pentagram/)
- Typewolf lists PP Neue Montreal on many Site of the Day picks. Several pair it with PP Editorial New (The Haircut, Camille Luang, Garoa, the last also with Anonymous Pro mono) or Editorial Old (Elena Scott, Dec 2025). Others pair it with GT Alpina, Times Now or Domaine Display. Typewolf's suggested pairing is Editorial New. — [Typewolf: Neue Montreal](https://www.typewolf.com/neue-montreal)
- Pangram Pangram (maker of Editorial New and Neue Montreal) lets anyone try every font free for personal or non-commercial use: portfolios, client pitches and proofing. Commercial web licences are priced by total monthly pageviews and can be upgraded with credit for what was already paid. The FAQ gives no fixed prices. — [Pangram Pangram FAQ](https://pangrampangram.com/pages/faq)
- Instrument Serif (Rodrigo Fuenzalida and Jordan Egstad, 2023) is licensed under the SIL OFL. It was made for large sizes as a contemporary take on old-style serif traits. — [Figma fonts: Instrument Serif](https://www.figma.com/fonts/instrument-serif/). Directory listings show it mostly on tech, SaaS and hospitality sites (Northzone, Buci Hotel, Grace and Favour), not on fashion brands. — [maxibestof.one: Instrument Serif](https://maxibestof.one/typefaces/instrument-serif)
- Fontshare (Indian Type Foundry) mixes two licences: ITF Free Font License fonts (closed source, free for personal and commercial use) and SIL OFL fonts. — [ITF: Introducing Fontshare](https://www.indiantypefoundry.com/news/introducing-fontshare). One third-party note says the Satoshi EULA bans redistributing the font files, for example on public servers, and expects them to be served from ITF's own servers or API. Check the EULA before self-hosting. — [Adom theme font licences](https://wiki.adom.inc/api/pages/adom/adom-theme/files/fonts/LICENSES.md)

**Font facts checked against Google Fonts and Fontshare metadata (all free)**

| Font | Source / licence | Designer | Variable axes / styles | Notes |
|---|---|---|---|---|
| Bodoni Moda | Google Fonts, OFL | Owen Earl | opsz 6-96, wght 400-900 | Real optical sizes, so the hairlines thicken at small sizes. Bodoni Moda SC (small caps) added 2024 |
| Playfair (2023 version, not Playfair Display) | Google Fonts, OFL | Claus Eggers Sørensen | opsz 5-1200, wdth 87.5-112.5, wght 300-900 | Very wide optical-size range. Good for animating on scroll |
| Fraunces | Google Fonts, OFL | Undercase Type, Phaedra Charles, Flavia Zimbardi | SOFT 0-100, WONK 0-1, opsz 9-144, wght 100-900 | The best axes for kinetic type |
| Instrument Serif / Instrument Sans | Google Fonts, OFL | Fuenzalida, Egstad | Serif: 2 static styles. Sans: wdth 75-100, wght 400-700 | Two families made as a set |
| Newsreader | Google Fonts, OFL | Production Type | opsz 6-72, wght 200-800 | Editorial text serif |
| Inter Tight | Google Fonts, OFL | Rasmus Andersson | wght 100-900 | Tighter-spaced Inter for display sizes |
| Hanken Grotesk / Schibsted Grotesk / Geist | Google Fonts, OFL | various | wght variable | Free stand-ins for Neue Montreal |
| Archivo | Google Fonts, OFL | Omnibus-Type | wdth 62-125, wght 100-900 | Condensed to expanded in one file, like Parsons' mixed widths |
| Mona Sans / Hubot Sans | Google Fonts, OFL (added Nov 2024) | GitHub, Degarism | wdth 75-125, wght 200-900 | Width axis for scroll stretching |
| Anton | Google Fonts, OFL | Vernon Adams | 1 static style | The Superr display face |
| Big Shoulders | Google Fonts, OFL (added Feb 2025) | Patric King | opsz 10-72, wght 100-900 | Condensed display |
| Bebas Neue / Six Caps / Antonio / Oswald | Google Fonts, OFL | various | mostly static | Other condensed options |
| DM Mono / Space Mono | Google Fonts, OFL | Colophon Foundry | static | Labels and care-tag text |
| IBM Plex Mono / Geist Mono / JetBrains Mono / Red Hat Mono | Google Fonts, OFL | various | static or wght | Labels and measurement numerals |
| Martian Mono | Google Fonts, OFL | Roman Shamin, Evil Martians | wdth 75-112.5, wght 100-800 | A mono with a width axis |
| Reenie Beanie / Caveat / Homemade Apple | Google Fonts, OFL | various | Caveat: wght 400-700 | Tailor's-chalk handwriting accents |
| Gambarino | Fontshare, ITF FFL | Théo Guillard | 1 style | "Condensed, single-weight serif face for headlines" |
| Boska | Fontshare, ITF FFL | Barbara Bigosinska | 14 styles | "High-contrast 'modern', or Didone-style … for headlines in editorial design" |
| Zodiak / Erode / Gambetta / Sentient / Bespoke Serif | Fontshare, ITF FFL | Erode: Nikhil Ranganathan. Sentient: Noopur Choksi | 12-14 styles each | Erode is named after a city in Tamil Nadu, and two of these are by Indian designers |
| General Sans / Satoshi / Switzer / Supreme / Cabinet Grotesk | Fontshare, ITF FFL | Frode Helland / Deni Anggara / Jérémie Hornus | 12-20 styles | General Sans is a "rationalist sans", Switzer a "neo-grotesk" |
| Tanker / Panchang | Fontshare, ITF FFL | Ruosi Huang / Bigosinska and Hitesh Malaviya | Tanker 1 style, Panchang 8 styles | Tanker is condensed caps, Panchang ultra-wide |

Sources: [Google Fonts metadata](https://fonts.google.com/metadata/fonts), [Fontshare API](https://api.fontshare.com/v2/fonts), [Google Fonts: Bodoni Moda](https://fonts.google.com/specimen/Bodoni+Moda/about). Fontshare's catalogue (first 100 families checked) lists Latin script only, so Fontshare has no Kannada fonts. Indic support has to come from Google Fonts.

**Kannada and Devanagari fonts on Google Fonts (all OFL)**
- Every Google Fonts family with a Kannada subset: Akaya Kanadaka (display; Vaishnavi Murthy, Juan Luis Blanco), Anek Kannada (Ek Type; variable wdth 75-125, wght 100-800), Baloo Tamma 2 (Ek Type; wght 400-800), Benne (serif; John Harrington), Hind Mysuru (Indian Type Foundry), **Hubballi** (sans; Erin McLaughlin; 1 style; Kannada and Latin), Noto Sans Kannada (wdth 62.5-100, wght 100-900), Noto Serif Kannada (wght 100-900), Padyakke Expanded One (serif; James Puckett), Tiro Kannada (Tiro Typeworks, John Hudson, Fiona Ross; 2 styles). — [Google Fonts metadata](https://fonts.google.com/metadata/fonts); [Google Fonts: Hubballi](https://fonts.google.com/specimen/Hubballi)
- Tiro Kannada's subscript letters are drawn generously large for legibility, and it is open source. — [Tiro Typeworks](https://www.tiro.com/fonts/tiro-kannada); [Adobe Fonts](https://fonts.adobe.com/fonts/tiro-kannada)
- Anek covers 10 scripts, Kannada and Latin among them. It is a single variable family under the OFL, designed with a shared set of visual features plus influences specific to each script. Maithili Shingre and Vaishnavi Murthy did Kannada and Yesha Goshar did Latin. It won a TDC Certificate of Typographic Excellence and a D&AD Graphite Pencil. — [GitHub: EkType/Anek](https://github.com/EkType/Anek); [Fontsource: Anek Kannada](https://fontsource.org/fonts/anek-kannada/about)
- Devanagari options confirmed: Tiro Devanagari Hindi (2 styles), Noto Serif Devanagari (wdth 62.5-100, wght 100-900), Noto Sans Devanagari, Anek Devanagari (wdth 75-125, wght 100-800), Mukta (Ek Type, 7 styles), Gotu (Ek Type, 1 style), Yatra One (display), Rozha One (ITF, high-contrast display), Hind, Poppins, Kalam (ITF handwriting), Akshar (Tall Chai; CTRS and wght axes). — [Google Fonts metadata](https://fonts.google.com/metadata/fonts)

### Inferences — six type systems

**System A: "Atelier Didone"** (the classic fashion-magazine look; safest, most "Vogue")
- Display: **Bodoni Moda** (use opsz 96 for hero sizes; italic for single accent words such as *Threads*). Text and UI: **Inter Tight** (or Hanken Grotesk). Utility: **DM Mono** in caps with letter-spacing, for course codes and care-label lines ("100% COTTON · 3 MONTHS · HUBBALLI").
- Kannada: **Noto Serif Kannada**, or **Tiro Kannada** for warmer, calligraphic contrast. Hindi: **Tiro Devanagari Hindi** or **Noto Serif Devanagari**.
- Cost: free (Google Fonts, OFL). Paid upgrade: Boska (free, Fontshare) or a licensed Didone.
- Mood: luxury magazine, couture. It follows the Harper's Bazaar Didone-plus-grotesk structure. Risk: it looks like every bridal or boutique site in India. To make it feel like a school, set it at huge sizes, crop it at the edges and keep it monochrome.

**System B: "Pattern Paper"** (contemporary editorial; the recommended default)
- Display: **Instrument Serif** (regular plus italic only: elegant, light, made for large sizes). Text: **Instrument Sans** (wdth 75-100 lets labels go condensed without a second family). Utility: **Geist Mono** or **IBM Plex Mono** for pattern-piece annotations ("FRONT BODICE — CUT 2 ON FOLD", "SEAM ALLOWANCE 1.5 CM").
- Kannada: **Anek Kannada**. Its 75-125 width axis matches Instrument Sans, so labels in both scripts can sit together at the same width. Hindi: **Anek Devanagari**.
- Cost: free. Mood: modern atelier, Kinfolk/Cereal-style calm. Closest to the "off-white plus black ink plus clay objects" direction.

**System C: "Soft Tailoring / Kinetic Serif"** (best for scroll animation)
- Display: **Fraunces** (animate `opsz`, `wght`, `SOFT` and `WONK` on scroll, so the type "softens" the way fabric drapes). Text: **Schibsted Grotesk** or **Hanken Grotesk**. Utility: **Martian Mono** (its width axis can stretch tape-measure numerals).
- Kannada: **Noto Serif Kannada** (variable wght, so it can follow weight animation) or **Benne**. Hindi: **Noto Serif Devanagari** (variable wdth and wght).
- Cost: free. Mood: warm, crafted, slightly quirky, approachable for beginners. Risk: Fraunces is widely used on startup sites. Keep WONK off for body text and use it only in a few hero moments.

**System D: "Superr-style Poster Condensed"** (closest to the client's reference)
- Display: **Big Shoulders** (variable, 2025) or **Anton** (what Superr uses), in uppercase with tight leading (~1.0). Text: **Archivo** (wdth 62-125 gives condensed captions and normal body from one file) or Plus Jakarta Sans. Hand accent: **Caveat** or **Reenie Beanie** as "tailor's chalk" notes beside the clay objects ("mark here", arrows, circled measurements).
- Kannada: **Anek Kannada** at its condensed widths (closest to a condensed poster look); **Baloo Tamma 2** for a rounder, friendlier display. Hindi: **Anek Devanagari** condensed, or **Yatra One** for display.
- Cost: free. Mood: loud, youthful, Instagram-native. This is what makes Superr stand out. It is less "luxury" than A or B but more memorable. If the client says "like Superr", this is the literal match. Pair it with off-white and black, not Superr's colours.

**System E: "Foundry Editorial" (paid, premium)**
- Display: **PP Editorial New** (thin or ultralight italic). Text: **PP Neue Montreal**. Utility: PP Neue Montreal Mono or Anonymous Pro (Garoa's pairing per Typewolf).
- Kannada and Hindi: Anek Kannada / Anek Devanagari or Tiro Kannada / Tiro Devanagari Hindi (Pangram has no Indic scripts).
- Cost: free trial for pitches and prototypes ([Pangram FAQ](https://pangrampangram.com/pages/faq)). A commercial web licence is required before launch, priced by pageviews. The founder's site will be low traffic, so this is probably the smallest tier, but prices could not be verified.
- Mood: the Awwwards/Typewolf "design studio" look. Free approximation: Instrument Serif plus Inter Tight (System B).

**System F: "Indian Type Foundry / Fontshare"** (free, India-made story)
- Display: **Gambarino** (condensed, single weight, post-modern serif; very fashion) or **Boska** (Didone with a calligraphic flourish). Text: **General Sans** or **Satoshi** (or **Switzer** for a neutral neo-grotesk). Utility: **Space Mono** / **DM Mono** from Google.
- Kannada: **Hind Mysuru** (ITF, Google Fonts), so the Indic companion comes from the same foundry. Hindi: **Hind** or **Poppins** (both ITF).
- Cost: free under ITF FFL. Self-hosting may be restricted, so it may need Fontshare's CDN (see Satoshi EULA note). The story is easy to sell to the client: an Indian foundry for an Indian academy.

**Bonus (works with any system): "Hubballi" the typeface.** Google Fonts has a free Kannada and Latin sans literally called **Hubballi** (Erin McLaughlin). Using it for the bilingual tagline, the address or care-label lines ("Made in Hubballi") gives the brand a story it can repeat. It has a single weight, so keep it to small or utility text.

**Tailoring-specific type details (apply to any system)**
- Tape-measure numerals: `font-variant-numeric: tabular-nums` in a mono, with tick marks drawn in CSS or SVG. Use them for stage numbers (01-05), course durations ("3 / 6 MONTHS") and section counters.
- Care-label micro type: 9-11px mono caps, letter-spacing 0.08-0.12em, inside a thin-bordered box with care symbols.
- Pattern-paper annotations: italic serif plus mono, with dashed lines (`border-style: dashed`), as cut lines and notches.
- Size chart and spec sheet: a mono table with hairline rules, for the fees and timetable section.

### Gaps
- Fonts In Use pages for PP Editorial New and Instrument Serif returned 404, and no verified fashion brand using Instrument Serif or Gambarino was found. Fashion use of these two is inferred from their style, not documented.
- No current prices were found for Pangram Pangram web licences; the FAQ lists none. No licence terms were found for Displaay or Collletttivo. Velvetyne (https://velvetyne.fr/) and Collletttivo (https://www.collletttivo.it/) are live free/open-source foundries, but no specific family names or licences were checked.
- Fonts used by major Indian fashion schools (NIFT, Pearl Academy) and Indian designer labels were not researched.
- I Love Typography's "Ask ILT: fashion fonts" (https://ilovetypography.com/2021/07/15/ask-ilt-fashion-fonts/) returned 403, so its contents were not read.

---

## Q2. Which creative and kinetic typography techniques fit a tailoring theme, and where are the tutorials?

### Takeaway
All the requested effects have proven tutorials: variable-axis scroll animation, "stitched" dashed-stroke text, video or photo inside letters, split-letter reveals and oversized cropped type. GSAP, including SplitText, has been free for commercial use since 2025, which removes the old licensing barrier for split-letter reveals.

### Cited Findings
- GSAP is 100% free, including the formerly paid Club plugins (SplitText, MorphSVG), for commercial use. Webflow acquired GSAP in fall 2024. In 3.13, SplitText was rewritten to be about 50% smaller, with built-in screen-reader accessibility and easy line masking for reveals. — [Webflow: GSAP becomes free](https://webflow.com/blog/gsap-becomes-free); [GSAP 3.13 release notes](https://gsap.com/blog/3-13/)
- Codrops: "From SplitText to MorphSVG: 5 Creative Demos Using Free GSAP Plugins". — [Codrops](https://tympanus.net/codrops/?p=93244)
- Codrops: "On-Scroll Letter Animations" (2021) covers scroll-driven letter-by-letter effects. — [Codrops](https://tympanus.net/codrops/2021/01/20/on-scroll-letter-animations)
- Codrops: Exat microsite case study. A variable-font showcase where scrolling structures the page and hovering morphs the specimen between weights and widths in real time. — [Codrops: The Exat Microsite](https://tympanus.net/codrops/?p=113526)
- Codrops: "4 Exclusive Demos: Slideshows & Typographic Animations" (2023), with GSAP letter and line hover effects. — [Codrops](https://tympanus.net/codrops/2023/06/16/4-exclusive-demos-slideshows-typographic-animations/)
- Codrops "Animated Text Fills" demo set, including "SVG text with animated dashed stroke pattern" (the basis for "stitched" text), "SVG with HTML5 video text fill" and "background-clip: text with animated gradient". — [Codrops Animated Text Fills demos](https://tympanus.net/Tutorials/AnimatedTextFills/index.html)
- Draw-on technique: set `stroke-dasharray` longer than the path, then animate `stroke-dashoffset` to 0 with `animation-fill-mode: forwards`. CSS-Tricks credits Jake Archibald with the technique. — [CSS-Tricks: How SVG line animation works](https://css-tricks.com/?p=163222). Vivus is a JS library for the same "drawn" effect on SVG paths. — [Vivus (GitHub mirror)](https://github.com/openstacks/vivus)
- Text with an image or texture inside: Codrops "Techniques for Creating Textured Text" (`-webkit-background-clip: text`, with fallbacks) — [Codrops](https://tympanus.net/codrops/?p=17424). Codrops "Experiments with background-clip: text" — [Codrops](https://tympanus.net/codrops/?p=6872). Codrops background-clip tag hub — [Codrops](https://tympanus.net/codrops/hub/tag/background-clip)
- SuperHi "Experimental Typography for the Web" course (6 hours) covers adding, animating and scroll-driving variable fonts. — [SuperHi](https://www.superhi.com/courses/experimental-typography-for-the-web)

### Inferences — mapping techniques to the Teaching Threads story
- **"Stitched" headline**: convert the display word (e.g. "Threads" in Instrument Serif italic) to SVG outlines. Give it a dashed stroke (`stroke-dasharray: 6 4`) and a second solid "thread" path that draws on as the user scrolls. The Codrops dashed-stroke demo is the starting point. Text converted to paths must keep a real HTML heading (visually hidden) for SEO and screen readers.
- **Variable-axis "drape"**: tie Fraunces `SOFT`/`wght`, Bodoni Moda `opsz` or Archivo/Mona Sans `wdth` to scroll progress. A word "stretches like fabric" as the dress-form video plays. Use CSS scroll-driven animations (`animation-timeline: view()`) where supported, with GSAP ScrollTrigger as the fallback.
- **Video inside type**: put the existing Kling stage videos inside giant letters ("STITCH", "ಹೊಲಿಗೆ") with an SVG `<mask>`/`clipPath` or `background-clip: text` on a canvas or poster frame. Keep it to one hero moment for performance.
- **Split-letter reveals**: GSAP SplitText (free) with line masks for section titles. Its built-in aria handling keeps headings readable to screen readers.
- **Oversized cropped type**: a full-bleed wordmark ("TEACHING THREADS") at `font-size: 22vw` with `overflow: hidden`, cut off at the bottom edge like fabric off the bolt. This works best with condensed faces (System D) or Gambarino (System F).
- **Vertical type**: `writing-mode: vertical-rl` for side labels ("EST. HUBBALLI", stage numbers), like a selvedge edge. Do not set Kannada vertically, because Kannada conjuncts do not stack well (inference).
- **Tape-measure scroller**: a horizontal ruler of mono tabular numerals with CSS-gradient ticks that slides with scroll progress. It can work as the progress bar for the five-stage course section.
- **Care-label cards**: course facts as woven-label or care-tag components (mono micro type, care icons, a "fold" shadow).

### Gaps
- Codrops pages returned 403 to automated fetching, so the code inside each demo was not read. Titles and topics come from search snippets and URLs.
- No Awwwards, Godly or Siteinspire fashion-school examples with stitched-text effects were verified.
- No support data for CSS `animation-timeline` (scroll-driven animations) was checked here. Check caniuse before relying on it in Safari.

---

## Q3. Are there good examples of bilingual English + Kannada typography?

### Takeaway
There is plenty of good Kannada type design, notably Ek Type's Anek system and Tiro Kannada. I found no documented bilingual English and Kannada fashion website. The best-supported approach is a multi-script superfamily (Anek, Noto or Tiro) so both scripts share weight, width and colour, with Kannada as a deliberate typographic layer rather than a translation placed under the logo.

### Cited Findings
- Bilingual signage is mandatory in Karnataka (and Maharashtra), so brands must rework their shopfront names in the local script. — [Yellowslice: Designing in a multiscript country](https://yellowslice.in/bed/?p=11115)
- A type-design blog reviewed Kannada versions of Bangalore brand signs. It judged McDonald's Kannada an acceptable equivalent and Domino's "fussy" and artificially bolded, and advised against putting the Kannada name directly under the English logotype. — [UltraSparky: A Type Nerd's Time in India](https://ultrasparky.org/blog/?p=2706)
- Ek Type (Mumbai) runs workshops on multi-script brand identities. — [Typoday 2017](https://www.typoday.in/2017/sarang.html)
- Anek was designed as harmonised multi-script type: shared features chosen together, plus traits specific to each script, and equal value for each of nine Indian writing systems and Latin. — [GitHub: EkType/Anek](https://github.com/EkType/Anek); [Fonts In Use: Anek Latin](https://www.fontsinuse.com/typefaces/201245/anek-latin)
- Maya Eapen's Parsons thesis "Bangalore Display" is a bold, playful Kannada display face drawn from hand-lettered Bangalore street signs and aimed at younger audiences. — [Parsons BFA CD: Maya Eapen](https://bfacd.parsons.edu/2021/maya-eapen)
- An RCA research project built a systematic bilingual layout for English translations of Indian texts, including Kannada, using facing pages and an Indic typographic hierarchy. — [RCA Research Online](https://researchonline.rca.ac.uk/4117/)
- Tiro Kannada and Tiro Devanagari Hindi were both designed by John Hudson and Fiona Ross (Tiro Typeworks) and released on Google Fonts together, on the same date (2022-05-25). — [Google Fonts metadata](https://fonts.google.com/metadata/fonts)

### Inferences
- Use Kannada for emotional and local moments: the hero tagline, the founder's quote, the "ಹೊಲಿಗೆ" (stitch) motif and the address. Keep long course text in English with Kannada summaries, rather than doubling every paragraph.
- Match **optical size, not point size**. Kannada has tall vowel signs and subscript conjuncts, so it usually needs about 1.1-1.2x the Latin font size and more line-height (about 1.6-1.8). Set the Kannada `:lang(kn)` block with its own `line-height`. This is standard practice for Indic text, not a sourced figure.
- Use `lang="kn"` / `lang="hi"` on elements so browsers pick the right font through `:lang()`, and so search engines see a correct language signal.
- Ready-made pairings: Instrument Sans + Anek Kannada (both have width axes); Bodoni Moda + Tiro Kannada (both high-contrast and calligraphic); Fraunces + Noto Serif Kannada; Anton/Big Shoulders + Anek Kannada Condensed; Hind (ITF) + Hind Mysuru. Hubballi works for small bilingual labels.
- Do not fake-bold Kannada; that is the Domino's mistake. Use a family with real weights (Anek, Noto, Baloo Tamma 2).

### Gaps
- No Indian fashion brand or academy website with strong English and Kannada typography was found and verified. Kannada-language news sites and Karnataka cultural institutions were not reviewed.
- No guidance from a font maker on exact size ratios between Latin and Kannada was found.

---

## Q4. What matters for performance and SEO: font-display, subsetting, variable fonts, weights and layout shift?

### Takeaway
Use 2-3 families at most and variable fonts where they exist. Self-host WOFF2 subsets split by `unicode-range` (Latin, Kannada and Devanagari as separate files, so English-only visitors never download Indic glyphs). Use `font-display: swap`, preload only the hero display font, and add metric-matched fallbacks (`size-adjust`, `ascent-override`) so swapping fonts does not shift the layout.

### Cited Findings
- `size-adjust`, `ascent-override`, `descent-override` and `line-gap-override` let a local font imitate the web font's dimensions, which reduces or removes layout shift when fonts swap. — [Chrome for Developers: Improved font fallbacks](https://developer.chrome.com/blog/font-fallbacks)
- Next.js `next/font` (from v13) applies metric overrides and `size-adjust` fallbacks automatically. Nuxt has `@nuxtjs/fontaine`. Fontaine is a framework-agnostic library that generates these fallbacks, with Vite and Webpack plugins. — [Chrome: Framework tools for font fallbacks](https://developer.chrome.com/blog/framework-tools-font-fallback); [GitHub: unjs/fontaine](https://github.com/unjs/fontaine)
- Metric overrides fix vertical metrics, but different glyph widths can still change line wraps. Use `size-adjust` for width and an explicit `line-height` for height. — [Shopify: Reduce CLS from font swapping](https://shopify.dev/docs/storefronts/themes/best-practices/performance/reduce-cls-font-swapping)
- With proportional fonts a perfect fallback match is impossible, but hand-tuned overrides get close. — [Vincent Bernat: Fixing layout shifts caused by web fonts (2024)](https://vincent.bernat.ch/en/blog/2024-cls-webfonts)
- In practice (thesuperrco.com): self-hosted WOFF2 files, `font-display: swap`, a variable weight range on one file (`font-weight: 200 800` for Plus Jakarta Sans), and a one-glyph rupee file loaded only when needed through `unicode-range: U+20B9`. — [thesuperrco.com base.css](https://thesuperrco.com/css/base.css)
- Fontshare's ITF licence may require serving fonts from Fontshare's own servers rather than self-hosting (Satoshi EULA note, secondary source). — [Adom font licences](https://wiki.adom.inc/api/pages/adom/adom-theme/files/fonts/LICENSES.md)

### Inferences
- **Budget**: about 3 font files on first load: the display font (one weight or a variable file), the text font (variable), and the mono (one weight). Load Kannada and Devanagari subsets only when the page has that text. `unicode-range` handles this automatically.
- **Indian rupee sign**: copy Superr's trick. Check that the chosen Latin subset includes ₹ (U+20B9). If it does not, add a one-glyph subset, since fees are shown in rupees.
- **Self-host the Google Fonts** (download with google-webfonts-helper or Fontsource) to avoid the cross-origin connection and for privacy. OFL allows this.
- **Preload** only the hero display WOFF2 (`<link rel="preload" as="font" type="font/woff2" crossorigin>`). Do not preload the Indic files.
- **Variable vs static**: variable files are larger than one static weight. If the design uses only two weights and no axis animation, static subsets are lighter. Use variable files only for the face that is animated (Fraunces, Bodoni Moda opsz, Archivo wdth).
- **SEO**: keep real HTML text for headings, even when they are drawn as stitched SVG or placed over video (visually hidden `<h1>`, or `aria-label` with `role="img"` on the SVG). Text inside video or images is invisible to search engines. Use `lang` attributes for Kannada and Hindi text.
- **Fallback stacks**: serif display → `Georgia, 'Times New Roman', serif` with `size-adjust`; condensed display → `'Arial Narrow', Impact, sans-serif` (as Superr does); Kannada → `'Noto Sans Kannada', 'Kannada Sangam MN', 'Tunga', sans-serif`. Tunga is the Windows Kannada system font and Kannada Sangam MN the macOS/iOS one. This is from general knowledge and was not verified in this research.

### Gaps
- The WOFF2 file sizes of the Kannada fonts (Noto Serif Kannada, Anek Kannada variable, Tiro Kannada) were not measured. They are needed to set the font budget.
- Google Fonts' own documentation on the Kannada `unicode-range` split and `text=` subsetting was not fetched.
- No caniuse data for `size-adjust` or `font-palette` was checked. Current support should be confirmed before relying on them.
