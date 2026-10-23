# Teaching Threads: Competitor & Design Research

_October 2026. Research for the Teaching Threads Fashion Academy website._

**Client brief:** practical, hands-on learning. Make students ready for industry. Help them start their own clothing business. Slightly premium feel. Some interactivity, but SEO must not suffer.

---

## 1. Who we looked at

| Tier | Academy | What it's known for |
|---|---|---|
| European prestige | **Polimoda** (Florence) | Editorial look, "legacy of excellence" |
| | **Istituto Marangoni** (Milan + 9 cities) | Global reach, rankings, AI positioning |
| | **Central Saint Martins / UAL** (London) | Experimental, gallery/exhibition feel |
| | **IED** (Italy/Spain/Brazil) | Student projects as the main visual |
| | **Domus Academy** (Milan) | Design + fashion + business, industry briefs |
| Indian admissions-led | **Pearl Academy** | "India's No.1", placements, lots of lead forms |
| | **JD Institute** | Admissions, 38 years of history, many branches |
| Entrepreneur-led (closest to our brief) | **Jimmy Choo Academy (JCA)**, London | "Design, Create and Launch", shop, pop-ups |
| | **IFA Paris** short courses + Startup Incubator | Short practical courses, mini-collections |
| | **Australian Fashion Business Academy** | "First paying client in 6–10 weeks" |

Parsons, FIT, ESMOD, Vogue College and BoF Education blocked automated fetching, so they're left out of the page-by-page analysis.

---

## 2. The three vibes in this market

### A. Editorial prestige (Polimoda, Marangoni, CSM, IED, Domus)
- **Feels like** a fashion magazine. Big photography, lots of white space, black/white with a few accents, serif or sharp grotesk type.
- **Uses student work as the hero.** IED and CSM credit every image (student name and photographer). Domus labels each project with its brand partner (Pepsico, Google, Bulgari).
- **Has its own magazine.** Marangoni has *Maze35* ("Unfiltered creativity powered by students"), Domus has *The Envisioner*, Polimoda has its *Journal*. The editorial content doubles as SEO content.
- **Proves itself with rankings and numbers.** Marangoni: "91% employability, QS #45, Vogue Business Top 10". IED: "93% placement rate, 100,000+ alumni".
- **Main CTAs:** Open Day, Apply, Book orientation, Info kit.
- **Tone:** aspirational and future-facing. "A new generation of creators" (Polimoda), "Turn your ideas into what is next" (Domus), "The future is looking for you" (IED).

### B. Admissions machine (Pearl, JD Institute)
- **Feels like** conversion first. "Apply Now" everywhere, brochure downloads, WhatsApp, a helpline, enquiry forms with OTP.
- **Proves itself with big numbers that carry asterisks.** Pearl shows "99%* placement" with "T&Cs apply". JD's own page says both "20+ branches" and "38+ centres".
- **Packs in** lots of carousels, video testimonials, Instagram embeds and long logo strips.
- **Tone:** confident and salesy. H1s like "Best Design College in Bangalore".
- **Takeaway:** these sites convert in the Indian market, but they feel mass-market. That's the opposite of premium.

### C. Founder / entrepreneur (JCA, IFA incubator, AFBA)
- **Feels like** a boutique. JCA has a "Shop Dresses" strip that sells student work on the academy site.
- **Pitches the business directly.** "Design, Create and Launch", "From concept to high street", "Get Straight to Business", "Creativity, Commerce, Confidence".
- **Proves it with** pop-up shops, a retail gallery store, live briefs, and graduates selling through the academy's e-commerce site.
- **The gap: nobody shows real outcomes.** JCA's entrepreneur page names no student brands and gives no sales figures or case studies. AFBA is the only one that makes a measurable promise ("first paying client").

> **Positioning opportunity:** Teaching Threads can take **vibe A's look** with **vibe C's promise**, and back it with **proof none of them show**: named student labels, real garments, real numbers.

---

## 3. The layout almost everyone uses

Most fashion school homepages follow this order:

1. Utility bar (Open Day / admissions open)
2. Header: logo · mega-menu · language · **Apply**
3. Hero **carousel** with 3–4 slides of news, rankings and open days
4. Stats band (placement %, alumni, nationalities)
5. Programmes / areas of study (cards)
6. Student work carousel
7. Industry partner logo strip
8. Alumni and mentors
9. Events and news
10. Magazine / journal
11. Admissions links + lead form
12. Fat footer sitemap + floating WhatsApp/phone

**What's tired or broken here, and what we should skip:**
- **Hero carousels.** Every site has one. Only slide 1 gets seen, they slow down the largest-contentful-paint (LCP) score, and the message gets muddled.
- **Stats with asterisks.** They erode trust.
- **Course list pages that are just prose.** IFA shows no price, no start dates and no outcomes per course.
- **Missing alt text and placeholder images** (seen on JCA, Pearl and Domus). That hurts both SEO and accessibility.
- **Navigation organised around the school** ("About / Research / Newsroom") rather than the student ("What will I make? What will it cost? What happens after?").

---

## 4. What the logo tells us

- **Wordmark:** classic high-contrast roman capitals (Trajan/Cormorant-like). Couture, heritage, premium.
- **Subline:** widely tracked geometric sans ("FASHION ACADEMY"). Modern and clean.
- **Mark:** a needle and thread forming a "T", with a looping thread flourish. **The thread is our signature motif.**
- **Colour:** pure black on white. The palette should stay restrained.

**Suggested system**
- Type: a display serif for headlines (e.g. *Cormorant Garamond*, *Fraunces* at low optical size, or a licensed Trajan-adjacent face), plus a tracked sans for labels and UI (e.g. *Jost*, *Manrope*, *Inter* for body text).
- Colour: ink `#111`, paper/off-white `#F6F3EE` (linen/calico tone, not stark white), one "thread" accent used sparingly (deep oxblood, muted brass, or indigo denim, chosen with the client).
- Texture: real fabric macro shots, chalk pattern lines, tape measure, pattern paper grid. These say "workshop" rather than "runway".

---

## 5. Creative direction: "Atelier, not auditorium"

The big schools sell **prestige**. Indian schools sell **placement numbers**. Teaching Threads should sell **the making itself, and the business at the end of it**.

**Positioning line ideas**
- "From first stitch to first sale."
- "Learn it. Make it. Sell it."
- "Industry-ready. Business-ready."
- "Thread by thread, a label of your own."

**Proof to collect from the client now** (this drives the whole site):
- Student-made garments, with good photos of the pieces themselves, not stock images
- Student labels that have launched (name, Instagram, first-sale story)
- Studio/machine photos, batch size, hours of hands-on work vs. theory
- Industry tie-ups: factories, boutiques, export houses, internships
- Course price/fee range and durations. Being transparent here sets us apart from every competitor.

---

## 6. The "middle ground": interactive without hurting SEO

**Rule: every word and image is in the server-rendered HTML. JavaScript only adds polish.** If JS fails, the page is still complete and in the right order.

**Stack:** Astro (static output, zero JS by default, "islands" for the few interactive bits), or Next.js with SSG if the team prefers React. Host on a CDN. Use a headless CMS or markdown for courses, student labels and journal posts.

### Interactions worth building (cheap, SEO-safe, on brand)
| Idea | How | Why it fits |
|---|---|---|
| **The running thread**: a single SVG thread line that "stitches" down the homepage as you scroll, looping around section headings like the logo flourish | SVG `stroke-dashoffset` driven by CSS scroll-driven animations (`animation-timeline: view()`), with a small JS fallback; static line if `prefers-reduced-motion` | Signature moment, straight from the logo, zero content hidden |
| **Sketch → Pattern → Sample → On the rack** process strip | Pinned/sticky section where the image swaps as you scroll; all 4 steps exist as real HTML/`<img>` (stacked on mobile) | Shows "practical" in 5 seconds |
| **Before/after slider**: student's sketch vs. finished garment | Tiny island (~2 KB), with both images in the HTML | Proof of skill |
| **Stitched underline hovers** on links/buttons, dashed "seam" borders on cards | Pure CSS | Craft detail, premium feel |
| **Page transitions** | View Transitions API (cross-document), progressive | App-like smoothness on a static site |
| **Course "what you'll make" reveal** | `<details>`/accordion, content in the DOM | Indexable, scannable |
| **Fee/duration comparison** | Plain HTML table with sticky header | Transparency, and a high-intent SEO page |

### Avoid
- WebGL/3D garment viewers on landing pages (heavy, poor INP, nothing for SEO). Put them on a sub-page if ever needed.
- Scroll-jacking and full-screen intro animations or loaders
- Content injected client-side (reviews widgets, Instagram embeds) on key pages. Render a static grid at build time instead.
- Carousels for anything that matters

### SEO structure
- **One page per course** with `Course` + `CourseInstance` schema (duration, mode, price), plus an FAQ section with `FAQPage` schema
- `EducationalOrganization` + `LocalBusiness` schema with address and Google Business Profile
- **Student label pages** (`/labels/<brand>`): unique, linkable content that competitors don't have
- **Journal** for long-tail search: "how to start a clothing brand in [city]", "cost of making a first collection", "pattern making course near me", "how to find a garment manufacturer"
- Watch Core Web Vitals: LCP < 2.5s (no hero carousel, AVIF/WebP, preload the hero image), INP < 200ms (minimal JS)

---

## 7. Proposed homepage outline

1. **Slim bar:** "Next batch starts [date] · Book a studio visit"
2. **Header:** logo · Courses · Student Labels · The Studio · Journal · Fees · **Book a visit** (primary) · WhatsApp (secondary, important for an Indian audience if applicable)
3. **Hero (single, not a carousel):** big serif line "From first stitch to first sale." A short muted video loop or one strong photo of hands at a machine. Two CTAs: *Explore courses* / *See student labels*. The thread line starts here.
4. **Three-pillar promise:** Learn the craft · Work like the industry · Launch your label (each links deeper)
5. **The process (sticky scroll):** Sketch → Pattern → Sample → On the rack → Sold
6. **Courses:** 3–4 cards showing *duration · hands-on hours · what you'll make · from ₹/$*. No vague prose.
7. **Student labels:** editorial grid of real brands, "Founded by [name], batch of 2025", each linking to a case-study page. This is our version of JCA's "Shop" strip, with more proof.
8. **The studio:** machines, batch size, a photo grid. "Small batches. Real machines. Real fabric."
9. **Industry:** partner factories, boutiques, internships. Logo strip + one quote.
10. **Mentor / founder note:** the founder's story in their own words (JCA does this well).
11. **Journal teasers:** 3 posts targeting brand-starting searches
12. **FAQ:** fees, eligibility, batch timings, placement and business support (schema-marked)
13. **Final CTA band:** "Your label starts with one thread." *Book a studio visit*
14. **Footer:** courses, address/map, socials, contact

---

## Sources
- Polimoda: https://www.polimoda.com
- Istituto Marangoni: https://www.istitutomarangoni.com/en
- Central Saint Martins: https://www.arts.ac.uk/colleges/central-saint-martins
- IED: https://www.ied.edu
- Domus Academy: https://www.domusacademy.com
- Pearl Academy: https://www.pearlacademy.com
- JD Institute: https://www.jdinstitute.edu.in
- Jimmy Choo Academy: https://www.jca.ac.uk · https://www.jca.ac.uk/entrepreneur-ready
- IFA Paris short courses: https://ifaparis.com/short-courses
- Australian Fashion Business Academy (via training.com.au): https://www.training.com.au/?p=160950
- Hawthorn Academy: https://hawthornacademy.teachable.com
- Outlook-ICARE 2026 rankings: https://www.outlookindia.com/education/outlook-icare-rankings-2026-top-17-government-fashion-design-institutes
- Performance cost of motion: https://www.jacobtyler.com/blog/tag/page-speed/
- Motion UI on education sites: https://colorwhistle.com/motion-ui-student-engagement/
