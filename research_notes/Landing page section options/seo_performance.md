# SEO and Performance for a Scroll-Animated Local Fashion Academy Landing Page (Teaching Threads, Hubballi)

Research date: 2026-10-26. Google documentation was fetched in this session unless marked "(not fetched)". The biggest change since 2024 is that Google has **removed both the Course Info and FAQ rich results**. Details are in Q4.

---

## Q1. How canvas, frame-sequence and scroll animation and heavy video affect crawling, indexing and Core Web Vitals, and how Apple-style sequences are optimised

### Takeaway
Googlebot doesn't scroll or interact, and it indexes only what is in the rendered HTML. Anything painted into a `<canvas>` is invisible to it, and `<canvas>` is not an LCP candidate. The frame sequence is therefore SEO-neutral **provided** every word of real content sits in HTML around it. The real risk is performance. Hundreds of JPG/WebP frames compete for bandwidth with the true LCP element, and scroll handlers can cause long tasks that hurt INP. Preload only the first frame and the first section, stream the rest by section with IntersectionObserver, cap frame counts and resolution on mobile, and give reduced-motion users a static fallback.

### Cited Findings
**Crawling and indexing**
- Googlebot queues every 200-status page for rendering. A page "may stay on this queue for a few seconds, but it can take longer than that." "Google can only see content that's visible in the rendered HTML… If the content isn't visible in the rendered HTML, Google won't be able to index it." — [Google: JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- "Google can only discover your links if they are `<a>` HTML elements with an `href` attribute." Use the History API, not fragments, to load different content. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- "Google Search does not interact with your page." Lazy loading must not depend on scrolling or clicking. Load content "whenever it is visible in the viewport" using native lazy loading or IntersectionObserver. "Don't add lazy-loading to content that is likely to be immediately visible." Check image and video URLs in `src` with URL Inspection. — [Google: Fix lazy-loaded content](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading)
- "Google won't load content that requires user interactions (for example, swiping, clicking, or typing) to load." "Don't lazy-load primary content upon user interaction." — [Google: Mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- Google doesn't index CSS background images. It discovers images from `<img src>`. — [Google Image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)

**LCP**
- LCP candidates are `<img>`, `<image>` inside `<svg>`, `<video>` (poster load or first frame, whichever comes first), elements with a `url()` background image, and block-level text elements. `<canvas>` is not listed. Chromium excludes elements with opacity 0, low-entropy placeholder images, and full-viewport elements, which are "likely treated as background." Good is ≤2.5 s and poor is >4.0 s, measured at p75. — [web.dev: LCP](https://web.dev/articles/lcp)

**CLS**
- Animating `top`/`left` causes layout shifts even on the element's own layer. Composited `transform: translate` animations "don't count toward CLS." Always set `width`/`height` or CSS `aspect-ratio` on images and video. Shifts within 500 ms of a discrete input are excluded, **but shifts during scrolling are not excluded**. Web-font swaps can shift layout. Mitigate with `font-display: optional`, a close fallback, or preload. — [web.dev: Optimize CLS](https://web.dev/articles/optimize-cls)

**INP**
- Good INP is ≤200 ms at p75, and the web.dev figure marks >500 ms as poor. The interactions counted are click, keypress and tap, and scrolling isn't listed. Long tasks from large scripts delay responses. Yield with `setTimeout`, or with `requestAnimationFrame` plus `setTimeout` for non-critical work. A large DOM makes rendering updates expensive. — [web.dev: Optimize INP](https://web.dev/articles/optimize-inp)

**How Apple-style sequences work and are tuned**
- Apple product pages use a `<canvas>` fed pre-extracted frames that are drawn on scroll. Seeking a `<video>` via `currentTime` asks the decoder to seek arbitrary frames in real time, while drawing a cached image is near-instant. This is a secondhand teardown, not Apple documentation. — [DEV: AirPods scroll animation](https://dev.to/bekbrace/creating-a-scrolling-animation-for-apple-airpods-1g0m); [CSS-Tricks: Apple-style scroll animations](https://css-tricks.com/?p=308477)
- A GSAP forum answer recommends `drawImage` on a canvas over swapping `img.src`, driven by a ScrollTrigger `scrub` tween of a frame index. — [GSAP forum: AirPods image sequence with ScrollTrigger](https://gsap.com/community/forums/topic/25188-airpods-image-sequence-animation-using-scrolltrigger/)
- Frames must be preloaded because each new image is a new network request. Scroll progress maps to a frame index and is redrawn in `requestAnimationFrame`. — [setproduct: AirPods-style 3D scroll](https://setproduct.com/blog/how-to-3d-animate-scroll)
- **Video-scrub alternative.** Stutter comes from encoding. Normal encodes place a keyframe every 2–10 s, so seeks snap. Re-encode all-intra with `ffmpeg -g 1` (H.264 MP4 for Safari, VP9 WebM for Firefox), or use a compromise such as `-g 6 -keyint_min 6`. Then set `video.currentTime = self.progress * duration` in ScrollTrigger `onUpdate`. — [hontran.dev: scroll-scrubbed video stutters fix](https://www.hontran.dev/blog/scroll-scrubbed-video-stutters-fix); [GSAP forum: can ScrollTrigger scrub a video](https://gsap.com/community/forums/topic/38762-can-gsap-scrolltrigger-scrub-a-video-on-scroll/)
- Codrops has an article (OPTIKKA) on moving from HTML5 video to frame sequences for scroll sync because of video drawbacks. The fetch returned 403, so the specifics are not verified. — [Codrops: OPTIKKA, HTML5 video to frame sequences](https://tympanus.net/codrops/?p=103024)

### Inferences
- **The hero LCP can't be the canvas.** If the hero is canvas only, LCP falls to the biggest text block or image, which is usually fine. Better is a real `<img>` of frame 0 (or a `<video poster>`) with `fetchpriority="high"`, layered under the canvas and hidden only once the canvas has drawn. Don't hide it with opacity 0, which is excluded from LCP. Don't let it cover the full viewport, since full-viewport elements may also be excluded.
- **Practical budget for each sequence:** about 60–120 frames at 24–30 fps of source, which Kling 5–10 s clips give. Use WebP (AVIF where the decode cost is acceptable, since AVIF decodes more slowly on low-end Android), about 1280–1600 px wide on desktop and about 720–900 px on mobile, at quality ~60–70. Aim for 20–60 KB per frame and well under 3–5 MB per sequence on mobile. These are working heuristics, not sourced figures.
- **Loading order:** (1) Load frame 0 of section 1 as the HTML `<img>`. (2) After `load` or idle, fetch section-1 frames progressively, every 4th frame first and then filling the gaps, so scrubbing works early at a lower frame rate. (3) Use IntersectionObserver with `rootMargin: "100% 0px"` to start fetching section N+1 when section N enters view. (4) Decode with `createImageBitmap` or `img.decode()` off the scroll path. (5) Release bitmaps of far-away sections on low-memory devices (`navigator.deviceMemory` ≤ 4).
- **Sprite sheets** cut the request count but force large single decodes and hold more memory. With HTTP/2 or HTTP/3 on a CDN, separate frames are usually fine. A middle ground is a few sheets of 10–20 frames.
- **Mobile and low-data fallback:** on `prefers-reduced-motion: reduce`, `navigator.connection.saveData`, or narrow viewports, swap each sequence for 1–3 key stills or a short muted autoplay `<video playsinline>` loop, and keep the same HTML text.
- **INP and smoothness:** do only `drawImage` inside rAF, keep work out of scroll listeners (ScrollTrigger already batches), and use `transform`/`opacity` for kinetic typography. A pinned section that animates `height`, `top` or margins will register CLS during scroll.
- **WebGL photo effects:** lazy-initialise the context per section, keep the underlying `<img>` in the DOM as the source and the SEO asset, and never draw the only copy of an image into WebGL.

### Gaps
- No primary Apple engineering source was found. Frame counts, sizes and formats used by Apple are not documented officially.
- No benchmark comparing AVIF and WebP decode cost for scroll sequences on mid-range Android was found.
- The Codrops OPTIKKA article content couldn't be retrieved (403).

---

## Q2. Real HTML text, heading hierarchy, the hero LCP element, and font loading

### Takeaway
Ship every heading, course detail, fee, duration, address and FAQ as static HTML in the initial response, with one `<h1>` containing the target phrase. Canvas, WebGL and video are presentation layered over or behind that text. Self-host one or two WOFF2 display fonts, subset them, preload only the hero font, use `font-display: swap` for the brand face (or `optional` for body text), and add a size-adjusted fallback to limit CLS.

### Cited Findings
- Only rendered-HTML content is indexable. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Use the same clear, meaningful headings on mobile and desktop. The mobile content is what gets indexed. — [Mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- Block-level text elements are LCP candidates. — [web.dev: LCP](https://web.dev/articles/lcp)
- Fonts:
  - "preload ignores unicode-range declarations" and should be used for a single format only.
  - Cross-origin fonts need `crossorigin`.
  - `font-display: optional` delays text "no longer than 100ms" with no swap shift.
  - `swap` "delays text render the least" but shifts.
  - A mix is fine: swap for branding, optional for body.
  - Use `size-adjust` on the fallback to reduce CLS.
  - Subset to cut file size.
  - Use WOFF2 only, since it "compresses 30% better than WOFF."
  - Self-hosting vs Google Fonts is "less clear cut," and self-hosting helps mainly on a CDN with HTTP/2.

  — [web.dev: Font best practices](https://web.dev/articles/font-best-practices)
- GSAP SplitText `autoSplit` re-splits after fonts load or the width changes, so put animations in `onSplit()`. — [GSAP SplitText docs](https://gsap.com/docs/v3/Plugins/SplitText/)

### Inferences
- **Suggested outline:**
  - `<h1>` Fashion Designing & Tailoring Courses in Hubballi (with "Teaching Threads Fashion Academy" as the brand line)
  - `<h2>` per section:
    - About Shruti Mahajan
    - The 5 stages of the course
    - 3-Month Course
    - 6-Month Course
    - Student work / Runway
    - Fees & Batches
    - Visit us in Hubballi
    - FAQs
  - `<h3>` for each stage
- **Hero LCP element:** a large HTML text block (the `<h1>`) or a real `<img>` of the first frame or runway photo with `fetchpriority="high"`, width/height set and no `loading="lazy"`. If the h1 is the LCP, its font must not block, so preload that one WOFF2 and use `swap`.
- Example fallback metrics: `@font-face{font-family:"Display Fallback";src:local("Arial");size-adjust:105%;ascent-override:90%;descent-override:22%;line-gap-override:0%}`. Tune the values with a tool such as Fontaine or Capsize. `ascent-override` and the other overrides are widely supported, but web.dev's page doesn't cover them.
- Kannada text needs a font with Kannada glyphs (for example Noto Sans Kannada / Noto Serif Kannada). Load it with a `unicode-range` limited to U+0C80–0CFF so English pages never download it.

### Gaps
- No Google statement found on how heavily Google weights `<h1>`. Heading guidance is best practice, not a stated ranking factor.

---

## Q3. Local SEO: Google Business Profile, NAP consistency, Hubli vs Hubballi, Indian citations, reviews, Kannada

### Takeaway
For "fashion designing course near me" and "... in Hubballi," the Google Business Profile (GBP) and its reviews matter more than anything on the page. Google ranks local results by relevance, distance and prominence (reviews plus links), and ranking can't be bought. Use the real-world name with no keywords and the most specific category, keep the exact same NAP on the site, GBP, Justdial, Sulekha and education directories, and target both "Hubballi" and "Hubli" (plus "Hubli-Dharwad" and ಹುಬ್ಬಳ್ಳಿ) in on-page copy.

### Cited Findings
- Local results are "mainly based on relevance, distance, and popularity [prominence]." Prominence depends partly on how many websites link to the business and on review count. "More reviews and positive ratings can help your business's local ranking." Replying to reviews is encouraged. There is "no way to request or pay for a better local ranking." — [Google Business Profile Help: local ranking](https://support.google.com/business/answer/7091)
- GBP guidelines:
  - The name "should reflect your business's real-world name." Taglines and service or location keywords in the name are not permitted.
  - Use a precise address. No P.O. boxes or virtual offices. One profile per location.
  - "Use as few categories as possible," following the pattern "This business IS a…"
  - Google also detects categories from the website and mentions across the web.

  — [GBP guidelines](https://support.google.com/business/answer/3038177)
- The city is officially "Hubballi" (the article cites a 1 Nov 2014 Economic Times report on the renaming of 12 Karnataka cities). Kannada: ಹುಬ್ಬಳ್ಳಿ. Hubli–Dharwad is a twin city. HDMC dates from 1962, and on 2 Jan 2025 the Karnataka cabinet approved a separate Dharwad corporation. — [Wikipedia: Hubli](https://en.wikipedia.org/wiki/Hubli)
- Indian citation practice:
  - Consistency matters more than volume.
  - Justdial, Sulekha and IndiaMart are priority directories, and Sulekha is noted for education services.
  - A different phone number on Justdial or an old address on Sulekha can lower local rankings.
  - Audit and clean old or duplicate listings first.
  - Shiksha and CollegeDunia are listed for educational institutions.

  These are agency blogs and practitioner opinion. — [onecity.co.in: Local citation building (Bangalore)](https://onecity.co.in/blog/local-citation-building-for-bangalore-businesses/); [crawlvision: Local citation building 2026](https://crawlvision.com/blog/local-citation-building-seo-2026/); [Ranktracker: Local SEO in India](https://www.ranktracker.com/fr/blog/a-complete-guide-for-doing-local-seo-in-india/)

### Inferences
- **GBP checklist:**
  - Name: exactly what is on the signboard, for example "Teaching Threads Fashion Academy."
  - Primary category: probably "Fashion design school." Check the available list. Alternatives are "Sewing school" or "Vocational school," with one secondary category at most.
  - Add the exact pin, hours, phone, website with UTM (`?utm_source=gbp`), and a description mentioning the 3- and 6-month courses.
  - Add photos of the studio, students and founder, and post weekly.
  - Use Services/Products entries for each course with its price.
  - Seed the Q&A, and collect reviews after each batch through the GBP short review link (QR code in the studio). Reply to every review.
  - Never offer incentives for reviews. This is a known Google policy, but the policy page wasn't fetched here.
- **Naming:**
  - Postal address: "Hubballi, Karnataka 5800xx."
  - Body copy and title: "Hubballi (Hubli)" once, plus "Hubli-Dharwad" and nearby localities (Vidyanagar, Gokul Road, Keshwapur, Deshpande Nagar, Dharwad) where true.
  - Users search both spellings. Search volume per spelling wasn't verified (see Gaps).
- **Citations to create or claim:**
  - Justdial, Sulekha, UrbanPro (tutor and institute marketplace), IndiaMart (low priority)
  - Shiksha / CollegeDunia only if they list certificate courses
  - Facebook, Instagram (already likely the main channel), YouTube
  - Bing Places and Apple Business Connect
  - The local press or chamber listings in Hubballi
  - Keep the NAP strings identical, using the same phone format: +91-XXXXX-XXXXX.
- **Kannada keyword ideas** (Kannada-script phrases are unverified for volume):
  - ಫ್ಯಾಷನ್ ಡಿಸೈನಿಂಗ್ ಕೋರ್ಸ್ ಹುಬ್ಬಳ್ಳಿ (fashion designing course Hubballi)
  - ಟೈಲರಿಂಗ್ ತರಗತಿಗಳು (tailoring classes)
  - ಹೊಲಿಗೆ ತರಬೇತಿ (stitching training)
  - ಬ್ಲೌಸ್ ಡಿಸೈನಿಂಗ್ ಕ್ಲಾಸ್ (blouse designing class)
  - Many users type Kannada intent in Latin script ("tailoring class Hubli," "stitching class near me"), so the English page should include "stitching," "blouse designing," "boutique course" and "ladies tailoring."

### Gaps
- UrbanPro's local SEO value for institutes wasn't confirmed by any source found.
- Search volumes for "Hubli" vs "Hubballi" and for Kannada-script queries weren't available. Check Google Keyword Planner or Search Console after launch.
- The exact GBP category list for India wasn't verified ("Fashion design school" is likely but unconfirmed).

---

## Q4. Structured data: EducationalOrganization/LocalBusiness, Course/CourseInstance, FAQPage, Person, BreadcrumbList

### Takeaway
**Deprecations:**
- **Course Info** rich results were retired. They were announced on 12 Jun 2025, the docs were removed on 9 Sep 2025, and they are "no longer shown."
- **FAQ** rich results were limited to government and health sites in Aug–Sep 2023 and then **retired fully on 7 May 2026**. The docs were removed on 15 Jun 2026.
- **Course list** (carousel) rich results are still documented, but they need **3 or more courses** plus an ItemList, and they are English only.

What still earns value is LocalBusiness/Organization markup (it supports knowledge panel and local data understanding), BreadcrumbList and Course markup. Course markup is cheap, harmless and machine-readable for other engines and AI systems. Keep FAQ content as visible HTML. FAQPage JSON-LD is optional and gives no Google rich result.

### Cited Findings
- 12 Jun 2025: Google is phasing out Book Actions, **Course Info**, Claim Review, Estimated Salary, Learning Video, Special Announcement and Vehicle Listing. Google says rankings are not affected. From 9 Sep 2025 these were removed from Search Console reports and the Rich Results Test. — [Google Search Central blog: Simplifying the search results page](https://developers.google.com/search/blog/2025/06/simplifying-search-results); [Search Engine Land](https://searchengineland.com/google-drops-reporting-on-several-structured-data-types-461744); [Search Engine Journal](https://www.searchenginejournal.com/google-retires-7-structured-data-features-to-streamline-search-results/548952/)
- Changelog: 12 Jun 2025, banners were added to course info. 9 Sep 2025, course info documentation was removed and the type is "no longer shown in Google Search results." — [Google: course-info URL / changelog](https://developers.google.com/search/docs/appearance/structured-data/course-info)
- FAQ: Aug 2023 restriction to "well-known, authoritative government and health websites." A deprecation notice was added on 8 May 2026: "This feature will no longer appear in Google Search starting May 7, 2026." The documentation was removed on 15 Jun 2026. — [Google: FAQPage URL / changelog](https://developers.google.com/search/docs/appearance/structured-data/faqpage); [Google blog: Changes to HowTo and FAQ rich results (Aug 2023)](https://developers.google.com/search/blog/2023/08/howto-faq-changes)
- **Course list** (still live, page updated 2026-09-08):
  - "Available in English in all regions."
  - Required: `Course.name` and `Course.description` (60-character display limit).
  - `provider` is effectively required by the technical guidelines.
  - Needs at least 3 courses plus `ItemList`/`ListItem.position`/`url`.
  - Courses need an explicit educational outcome, instructors and a student roster. Promotional or event listings don't qualify, and violations can lead to a manual action.

  — [Google: Course list structured data](https://developers.google.com/search/docs/appearance/structured-data/course)
- LocalBusiness (page updated 2026-09-08):
  - Required: `name`, `address`.
  - Recommended: `geo` with lat/long at ≥5 decimal places, `openingHoursSpecification` (hh:mm:ss), `telephone` with country code, `url`, `priceRange` (<100 chars).
  - Use the most specific subtype. Multiple types go in an array, and `additionalType` isn't supported.
  - `aggregateRating`/`review` apply only to sites reviewing *other* businesses, so **don't self-mark star ratings**.

  — [Google: LocalBusiness structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- Mobile and desktop must have the same structured data. — [Mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)

### Inferences — JSON-LD (one `@graph` in the `<head>` of the home page)
Use `["EducationalOrganization","LocalBusiness"]` as the type array. schema.org also has `School` (EducationalOrganization) and LocalBusiness subtypes, but there is no single "fashion school" type, so the array is the clean option within Google's rule. The values below are placeholders, so replace them with the real NAP.

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["EducationalOrganization", "LocalBusiness"],
      "@id": "https://www.example.in/#org",
      "name": "Teaching Threads Fashion Academy",
      "alternateName": "Teaching Threads",
      "url": "https://www.example.in/",
      "logo": "https://www.example.in/img/teaching-threads-logo.png",
      "image": ["https://www.example.in/img/teaching-threads-studio-hubballi.jpg"],
      "description": "Fashion designing and tailoring academy in Hubballi offering 3-month and 6-month courses led by Shruti Mahajan.",
      "telephone": "+91-XXXXXXXXXX",
      "email": "hello@example.in",
      "priceRange": "₹₹",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "…",
        "addressLocality": "Hubballi",
        "addressRegion": "Karnataka",
        "postalCode": "5800XX",
        "addressCountry": "IN"
      },
      "geo": { "@type": "GeoCoordinates", "latitude": 15.36470, "longitude": 75.12390 },
      "areaServed": ["Hubballi", "Dharwad", "Hubli-Dharwad"],
      "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
        "opens": "10:00:00", "closes": "18:00:00"
      }],
      "founder": { "@id": "https://www.example.in/#shruti" },
      "sameAs": [
        "https://www.instagram.com/…",
        "https://www.facebook.com/…",
        "https://g.page/…",
        "https://www.justdial.com/…"
      ]
    },
    {
      "@type": "Person",
      "@id": "https://www.example.in/#shruti",
      "name": "Shruti Mahajan",
      "jobTitle": "Founder & Lead Instructor",
      "worksFor": { "@id": "https://www.example.in/#org" },
      "image": "https://www.example.in/img/shruti-mahajan-founder.jpg",
      "sameAs": ["https://www.instagram.com/…"]
    },
    {
      "@type": "Course",
      "@id": "https://www.example.in/#course-6m",
      "name": "6-Month Fashion Design & Tailoring Course",
      "description": "Pattern making, garment construction and a final runway collection.",
      "provider": { "@id": "https://www.example.in/#org" },
      "inLanguage": ["en", "kn"],
      "educationalCredentialAwarded": "Certificate",
      "offers": { "@type": "Offer", "category": "Paid", "price": "XXXXX", "priceCurrency": "INR" },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "courseMode": "Onsite",
        "location": { "@id": "https://www.example.in/#org" },
        "courseSchedule": { "@type": "Schedule", "duration": "PT3H", "repeatFrequency": "Daily", "repeatCount": 120 },
        "instructor": { "@id": "https://www.example.in/#shruti" }
      }
    },
    {
      "@type": "Course",
      "@id": "https://www.example.in/#course-3m",
      "name": "3-Month Tailoring & Stitching Course",
      "description": "Foundation tailoring: measurements, blouse, kurta and basic patterns.",
      "provider": { "@id": "https://www.example.in/#org" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.example.in/" },
        { "@type": "ListItem", "position": 2, "name": "Courses", "item": "https://www.example.in/courses/" }
      ]
    }
  ]
}
</script>
```

Notes on the snippet:
- BreadcrumbList only makes sense on inner pages, for example `/courses/6-month-fashion-design/`. On a one-page site, omit it.
- If there are 3 or more distinct courses (for example 3-month, 6-month and a short workshop such as blouse designing or Aari work), add an `ItemList` on `/courses/` to be eligible for the Course list carousel (English only).
- `FAQPage` can stay as harmless markup, but it gives no Google rich result since May 2026. The visible FAQ HTML is the asset that matters, both for ranking on long-tail questions and for AI answer engines.
- Validate with the Schema Markup Validator (validator.schema.org) for the retired types. The Rich Results Test no longer reports them.

### Gaps
- `Course`/`CourseInstance` property expectations (courseMode, courseSchedule, offers) come from the removed Course Info doc and schema.org. Google no longer documents them, so treat them as schema.org-valid, not Google-required.
- Google's Organization structured data page (developers.google.com/search/docs/appearance/structured-data/organization) wasn't fetched this session.

---

## Q5. Image SEO and video SEO (decorative vs content video)

### Takeaway
Runway and student-work photos should be real `<img>` (or `<picture>`) elements with descriptive filenames, useful alt text, explicit dimensions, srcset with AVIF/WebP and a `src` fallback, and lazy loading below the fold. Frame-sequence frames and decorative scroll videos aren't SEO assets. Give them empty alt or `aria-hidden` and keep them out of sitemaps. Only a page whose main purpose is a single video (for example a "Studio tour / Student runway 2026" watch page) can get video indexing.

### Cited Findings
- Google doesn't index CSS background images. Use `<img src>`, and use `srcset`/`<picture>` with a `src` fallback. Supported formats include JPEG, PNG, WebP, AVIF and SVG, and the extension must match the file type. Alt text is "the most important" image metadata, and keyword stuffing "may cause your site to be seen as spam." Filenames should be "short, but descriptive" (`my-new-black-kitten.jpg`, not `IMG00023.JPG`). Image sitemaps can list CDN-hosted URLs. — [Google Image SEO](https://developers.google.com/search/docs/appearance/google-images)
- Video indexing:
  - The video must be embedded on a watch page whose "main purpose is to show users a single video."
  - It must be discoverable via `<video>`, `<embed>`, `<iframe>` or `<object>` and not hidden behind other elements.
  - It needs a valid thumbnail at a stable URL (≥60×30).
  - Use unique `thumbnailUrl`, `name` and `description` in VideoObject.
  - Where video is "complementary to the rest of the content on the page," the page is not a watch page.

  — [Google: Video SEO best practices](https://developers.google.com/search/docs/appearance/video)
- Learning Video rich results were also retired in 2025. — [Simplifying search results (Jun 2025)](https://developers.google.com/search/blog/2025/06/simplifying-search-results)

### Inferences
- Filenames: `teaching-threads-student-runway-lehenga-hubballi-2026.webp`, `shruti-mahajan-founder-teaching-threads.jpg`.
- Alt examples:
  - "Student models a hand-embroidered black lehenga at the Teaching Threads runway show, Hubballi."
  - "Shruti Mahajan demonstrating pattern drafting to students."
  - Mention Hubballi once or twice, not in every alt.
- For canvas sequences, add `role="img"` and an `aria-label` describing the scene, or mark the canvas `aria-hidden="true"` when the adjacent HTML already says it. Never put meaningful words only inside the frames.
- Decorative `<video>`: `muted playsinline loop preload="none"` with a lightweight poster, no VideoObject, and pause it when off-screen via IntersectionObserver.
- Put the real Kling showcase videos and a student runway video on YouTube, with titles like "Fashion Design Course in Hubballi — Student Runway 2026," embed them on a dedicated page, and add VideoObject there. YouTube results surface separately for local queries.
- ImageObject is optional. Use it for the founder photo (Person.image) and the logo. Google's image metadata support (creator, license) applies to licensable images, so it is low priority here.

### Gaps
- Google's image license metadata doc and the VideoObject reference weren't fetched this session.

---

## Q6. Stack, hosting for India, meta/OG tags, sitemap, hreflang

### Takeaway
A static site is ideal. Astro is the best fit: zero JS by default, islands for the GSAP/canvas sections, built-in image optimisation, and Markdown for courses and FAQ. Plain HTML is also fine for a single page. Next.js static export works but ships React runtime for no benefit. Host on Cloudflare Pages, which has Indian PoPs (confirmed Mumbai, Chennai and New Delhi since 2015), or on Netlify/Vercel. Serve frame assets from the same CDN with long-lived immutable caching. For Kannada, use a separate `/kn/` URL with reciprocal hreflang (`en-IN`, `kn-IN`, `x-default`).

### Cited Findings
- Cloudflare launched Mumbai, Chennai and New Delhi PoPs in 2015, claiming under 50 ms latency in the subcontinent. A third-party list adds Bangalore, which is unverified, so check cloudflare.com/network for the current map. — [Cloudflare blog: launch in India](https://blog.cloudflare.com/cloudflare-launches-in-india-with-data-centers-in-mumbai-chennai-and-new-delhi/); [getdeploying: data centers in India](https://getdeploying.com/datacenters-in-india)
- hreflang:
  - ISO 639-1 language codes, plus an optional ISO 3166-1 alpha-2 region.
  - A region code alone is invalid.
  - Each version must list itself and all others, and the tags are ignored without return links.
  - `x-default` is the fallback.
  - The HTML `<link>`, HTTP header and sitemap methods are equivalent.
  - "Google doesn't use hreflang or the HTML lang attribute to detect the language of a page," so the content itself must actually be in Kannada.

  — [Google: Localized versions / hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)
- Self-hosted fonts help mainly on a CDN with HTTP/2. — [web.dev: Font best practices](https://web.dev/articles/font-best-practices)

### Inferences
- **Head template:**
```html
<html lang="en-IN">
<title>Fashion Designing & Tailoring Course in Hubballi | Teaching Threads</title>
<meta name="description" content="3- and 6-month fashion design and tailoring courses in Hubballi (Hubli-Dharwad) with Shruti Mahajan. Small batches, hands-on stitching, final runway show. Enrol now.">
<link rel="canonical" href="https://www.example.in/">
<link rel="alternate" hreflang="en-IN" href="https://www.example.in/">
<link rel="alternate" hreflang="kn-IN" href="https://www.example.in/kn/">
<link rel="alternate" hreflang="x-default" href="https://www.example.in/">
<meta property="og:type" content="website">
<meta property="og:title" content="Teaching Threads Fashion Academy, Hubballi">
<meta property="og:description" content="Fashion design & tailoring courses in Hubballi.">
<meta property="og:image" content="https://www.example.in/og/teaching-threads-1200x630.jpg">
<meta property="og:locale" content="en_IN">
<meta property="og:locale:alternate" content="kn_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preload" as="font" type="font/woff2" href="/fonts/display.woff2" crossorigin>
<link rel="preload" as="image" href="/img/hero-frame-0.avif" fetchpriority="high">
```
- Since WhatsApp is the main share channel in India, test the OG image there. It needs an absolute URL, about 1200×630, and a small file (under about 300 KB), which is a common practitioner recommendation.
- **Sitemap:** `sitemap.xml` with `/`, `/courses/...`, `/about/`, `/contact/`, `/kn/...` and their hreflang `xhtml:link` entries. Exclude frame folders, and add `Disallow` for nothing important (don't block JS or CSS). Submit it in Search Console and Bing Webmaster Tools.
- **Caching:** frame files get a hashed path plus `Cache-Control: public, max-age=31536000, immutable`, and HTML gets a short TTL. Use Brotli for HTML/CSS/JS. HTTP/3 is on by default at Cloudflare.
- **Page split for ranking breadth:** home (brand plus Hubballi), `/courses/6-month-fashion-design-course-hubballi/`, `/courses/3-month-tailoring-course-hubballi/`, `/about/shruti-mahajan/`, `/contact/` (map embed plus NAP), and `/kn/` mirrors. One long scroll page can rank, but separate course pages target the "tailoring classes" vs "fashion designing course" intents better.
- Measure with PageSpeed Insights / CrUX (field data, p75 mobile), and test on a mid-range Android over throttled 4G, which is typical of Hubballi users.

### Gaps
- Current Vercel/Netlify edge PoPs in India and comparative TTFB from Hubballi weren't verified.
- I didn't verify whether Astro's current major version changes the image or islands APIs.

---

## Q7. Which "cool" techniques are SEO-safe and which are risky

### Takeaway
Safe: anything that animates real HTML via CSS or JS transforms, split text with proper ARIA, content in accordions (if it is in the DOM on load), and horizontal scroll implemented as a vertical-scroll-driven transform of in-DOM content. Risky: text that exists only in canvas, WebGL or images, content loaded only after interaction, CSS-background-only images, and links that aren't `<a href>`.

### Cited Findings
- Only rendered HTML is indexed. Links must be `<a href>`. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Google doesn't interact, so content needing a swipe, click or type to *load* won't be seen. Accordions and tabs are acceptable on mobile, and Google suggests them as a way to save space. — [Mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing); [Lazy-loading](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading)
- CSS background images aren't indexed. — [Google Image SEO](https://developers.google.com/search/docs/appearance/google-images)
- SplitText's `aria: "auto"` (the default) adds an `aria-label` with the full text to the parent and `aria-hidden` to the generated char, word and line spans. For nested links, use `aria: "none"` plus a screen-reader-only copy. `revert()` restores the original innerHTML. — [GSAP SplitText docs](https://gsap.com/docs/v3/Plugins/SplitText/)
- Scroll-time layout shifts count toward CLS. Use transforms. — [web.dev: Optimize CLS](https://web.dev/articles/optimize-cls)

### Inferences — Safe / Caution / Risky table
| Technique | Verdict | Why / how |
|---|---|---|
| Canvas frame sequence with HTML text overlaid | Safe | Canvas is decorative and the text is in the DOM. Give the canvas `aria-hidden` or `role="img"` with a label. |
| Headline or course text drawn only in canvas or WebGL | **Risky** | Not indexed and not accessible. Keep an HTML copy (visually layered), not a `display:none` duplicate. |
| Text baked into Kling frames or images (for example "Stage 1: Sketch") | **Risky** | Not reliably indexed. Repeat it as HTML text. |
| Split letters or words into spans (GSAP SplitText) | Safe with ARIA | Google sees the concatenated text. Screen readers read letters one by one without `aria-label`/`aria-hidden` (SplitText `aria:"auto"`). Split after fonts load (`autoSplit`). Don't split body paragraphs. |
| Kinetic type animating `transform`/`opacity` | Safe | Animating `top`, `left`, `width` or `font-size` during scroll counts as CLS. |
| FAQ or course details in accordions (`<details>` or hidden-in-DOM) | Safe | Content is present on load. Avoid fetching the answers on click. |
| Content injected only when a section scrolls into view (JS fetch) | Caution | Googlebot doesn't scroll. Render the text in the HTML and lazy-load only the media. |
| Horizontal-scroll gallery (pinned, translateX driven by vertical scroll) | Safe | All items are in the DOM. Give a keyboard alternative, and on mobile fall back to a native swipe row with `scroll-snap`. |
| Scroll-jacking or smooth-scroll libraries (Lenis) | Caution | Not an SEO issue in itself, but it can hurt INP and accessibility. Respect `prefers-reduced-motion`. |
| Hero as full-viewport video or canvas only | Caution | Canvas isn't an LCP candidate and full-viewport elements may be excluded. Pair it with an HTML h1 or img. |
| Images as CSS backgrounds (parallax) | **Risky for image search** | Not indexed. Use `<img>` with `object-fit` and transforms. |
| Nav links as JS click handlers or `<div>`s | **Risky** | Not crawled. Use `<a href>`. |
| WebGL distortion on photos | Safe if the `<img>` stays in the DOM | Use the `<img>` as the texture source and keep its alt. Lazy-init the WebGL per section. |
| Autoplaying background video | Safe for SEO, costly for performance | Use `preload="none"`, a poster, pause off-screen, and don't make it the only carrier of meaning. |

### Gaps
- No primary Google statement was found specifically on SplitText-style per-letter spans. It is inferred safe because Google indexes rendered DOM text, but it hasn't been tested here.
- No current Google statement (2025–2026) was found on whether content in collapsed accordions gets full ranking weight. The mobile-first doc implies acceptance but doesn't say "full weight."
