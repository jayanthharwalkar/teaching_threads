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

## Shot list, weeks 1-3

| # | What the student sees | Moment |
|---|---|---|
| 1 | Close to the dress form; clay hands wrap the tape around the bust and pull it snug; tilt down to read the number | Week 1: take a measurement |
| – | Whip pan right | |
| 2 | Seated at the sewing machine, looking down at the needle; hands feed fabric, needle runs a black stitch line | Week 2: meet the machine |
| – | Whip pan right | |
| 3 | Looking down at a sheet of fabric on a tabletop; hand draws a chalk line, then cuts along it with the kainchi | Week 3: mark and cut |

## How to build it

1. One still per scene (ChatGPT or Nano Banana), all with the same backdrop, light and clay look.
2. Animate each still into a 4-6 s clip (image-to-video).
3. Export each clip as a frame sequence; the page scrubs through scenes and transitions as one continuous shot.

## Status (2026-10-25)

- Prototype: `prototypes/course.html`, published at https://claude.ai/artifact/XzfP8atzkSRExcZZzP7nWy (private; share from the page's Share menu before sending to Arun).
- Stills for weeks 1-3 made in ChatGPT (`chat gpt images/`); week 2 uses `week 2 .1.png` (industrial machine). Week 3 kainchi grip could be better.
- Kling clips done for weeks 1 and 2 (`kling videos/`), live in the prototype as scroll-scrubbed frame sequences (`prototypes/assets/week-1/`, `week-2/`). Week 3 is still a still with a slow push-in.
- Scene changes in the prototype still use the old timed whip pan. Once transition clips exist, replace it with one continuous scroll-scrubbed sequence: scene, transition, scene, transition, scene.
- Kling Standard plan: 660 credits/month. Audio off on every clip.
- Prompts, settings and the processing recipe: `video-prompts.md`.

## Next

1. Transition 1 -> 2 test in Kling (keyframes ready in `kling videos/`).
2. Week 3 clip (optionally fix the kainchi grip first), then transition 2 -> 3.
3. Join everything into one continuous scrubbed shot on the page; drop the timed whip pan.
4. Share with Arun and Shruti, then confirm scenes for the remaining modules (blouse, lehenga, design, aari, finishing, branding) and repeat.
5. Rest of the website: kainchi hero, teacher section, fees and dates, WhatsApp enquiry, frame loading on phones.
