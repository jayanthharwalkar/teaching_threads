# Course section: visual direction

Decided 2026-10-25. Prompts are in `nano-banana-prompts.md`; prototype is `prototypes/course.html` (https://claude.ai/artifact/XzfP8atzkSRExcZZzP7nWy).

## What we're making

A first-person (POV) shot of a student working through the course, played as the reader scrolls through the modules. The reader is the student: measure on the dress form, sit at the machine and sew, then cut. Slow camera moves carry them from one object to the next.

## Decisions

- **No room.** The warm brown studio (Prototype 05) clashed with the site, and a clay-white room (tried 2026-10-25, `nano banana images/image.png`) still looked ugly: walls, doorway and window add clutter. Objects float in an endless backdrop in the site's own colours.
- **Flat backdrop, no shadows.** Background is the page colour (#F3F1EC) everywhere, with no floor, no horizon and no cast or contact shadows, so the section merges into the page. Objects keep soft shading on their own surfaces so they still read as 3D.
- **Camera moves between objects, not whip pans** (changed 2026-10-25). A whip pan felt like an edit cut. Instead the camera pulls back from one object, drifts across the empty backdrop and settles on the next, like a person turning to the next tool. Made in Kling with start and end frames: start = last frame of the previous clip, end = first frame of the next, one simple move per prompt. Cheaper model (2.5 Turbo) for transitions, better model for the scene clips. All clips and transitions join into one continuous shot that the scroll scrubs.
- **Video, not live 3D.** Stills in Nano Banana, animated with an image-to-video tool (Veo / Kling), played on the site as a scroll-scrubbed frame sequence (WebP frames on a canvas, not a scrubbed `<video>`).
- **Clay-white objects.** Matte off-white, smooth, no wood grain or metal shine.
- **Black only on what the student uses:** tape markings (week 1), thread (week 2), kainchi handles and chalk line (week 3).
- **Clay hands** in frame, not real skin: consistent with the objects, avoids bad AI hands, and the student could be anyone.
- **9:16 vertical** for every frame and clip. The picture panel is portrait on desktop and phone.
- **Slow, steady camera inside each scene.** Transitions are smooth pull-back-and-drift moves, also scrubbed by scroll.

## Layout

- Desktop: picture panel on the left (pinned, bleeds to the screen edge), course contents on the right.
- Phone: picture on top, modules below.
- Course contents come from the two course PDFs, with a 3 months / 6 months toggle; 6-month-only items are tagged "6 mo".

## Shot list: five stages (decided 2026-10-25)

Stages, not weeks: the course PDFs have modules, not a weekly schedule, and "Week 1 of 12 / of 26" would be invented. The same five stages serve both courses; 6-month extras stay in the syllabus with their "6 mo" tag.

| # | Stage | What the student sees | Syllabus |
|---|---|---|---|
| 1 | Measure | Hands pull the tape snug around the dress form | Body measurements |
| 2 | Draft the pattern | Looking down at pattern paper; ruler and pencil trace a bodice block | Basic bodice block, kurta and sleeve drafts |
| 3 | Stitch | At the industrial machine, the needle runs a black seam | Machine practice, piping, darts |
| 4 | Your first blouse | The blouse on the dress form; hands pin the neckline | Blouses, finishing |
| 5 | Lehenga | Pull back to the full form wearing a flared lehenga | Lehenga and gowns |

Left out: cutting (a step, not an outcome), aari (6-month only), design basics (abstract). Optional 6th "Your own label" if Arun wants the branding angle.

## How to build it

1. One still per scene (ChatGPT or Nano Banana), all with the same backdrop, light and clay look.
2. Animate each still into a 4-6 s clip (image-to-video).
3. Export each clip as a frame sequence; the page scrubs through scenes and transitions as one continuous shot.

## Status (2026-10-26)

- Prototype 07 (`prototypes/course.html`, https://claude.ai/artifact/XzfP8atzkSRExcZZzP7nWy, shared by link) shows the five stages: stage 1 → 2 → 3 → 4 as one scroll-scrubbed shot (scene clips plus the 1→2, 2→3 and 3→4 camera moves), then stage 5 as the still `stage 5.1.png` with a slow push-in, joined to stage 4 by the old whip pan until the 4→5 clip exists.
- Stage 2 (drafting) and stage 4 (fastening the blouse hooks) clips done. Stage 4's action changed from one pin to the hooks: a single pin in a finished neckline isn't something a tailor does.
- Stage 5 changed from hands lifting the hem to tying the lehenga's dori (tassel making is in the finishing module). Start still `stage 5.1.png` done; end still 5b (full lehenga, no hands, dori tied) still to make from `stage 5.png`.
- Kling: about 250 credits left (2026-10-26), about 35-40 per clip; 2 clips to go.
- Clip-by-clip status and prompts: `video-prompts.md`.

## Next

1. Stage 5 end still (5b) in ChatGPT, then the stage 5 clip in Kling with start + end frames (`video-prompts.md`).
2. Claude makes the 4→5 end frame from the stage 5 clip's first frame; then the 4→5 transition clip.
3. Swap stage 5 and 4→5 into the page, drop the last whip pan, then tune all transitions together (speed, focus heights).
4. Share with Arun and Shruti.
5. Rest of the website: kainchi hero, teacher section, fees and dates, WhatsApp enquiry, frame loading on phones.
