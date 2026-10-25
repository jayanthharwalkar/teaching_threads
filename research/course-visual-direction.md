# Course section: visual direction

Decided 2026-10-25. Prompts are in `nano-banana-prompts.md`; prototype is `prototypes/course.html` (https://claude.ai/artifact/XzfP8atzkSRExcZZzP7nWy).

## What we're making

A first-person (POV) shot of a student working through the course, played as the reader scrolls through the modules. The reader is the student: measure on the dress form, sit at the machine and sew, then cut. Quick whip pans carry them from one object to the next.

## Decisions

- **No room.** The warm brown studio (Prototype 05) clashed with the site, and a clay-white room (tried 2026-10-25, `nano banana images/image.png`) still looked ugly: walls, doorway and window add clutter. Objects float in an endless backdrop in the site's own colours.
- **Flat backdrop, no shadows.** Background is the page colour (#F3F1EC) everywhere, with no floor, no horizon and no cast or contact shadows, so the section merges into the page. Objects keep soft shading on their own surfaces so they still read as 3D.
- **Whip pans between objects.** Transitions don't need to be continuous or exact: a fast pan with motion blur hides the cut. That means each object is its own still and clip, with no floor plan to keep consistent. The whip can be done in the browser (blur + slide between frame sequences), so the video tool only has to make clean clips.
- **Video, not live 3D.** Stills in Nano Banana, animated with an image-to-video tool (Veo / Kling), played on the site as a scroll-scrubbed frame sequence (WebP frames on a canvas, not a scrubbed `<video>`).
- **Clay-white objects.** Matte off-white, smooth, no wood grain or metal shine.
- **Black only on what the student uses:** tape markings (week 1), thread (week 2), kainchi handles and chalk line (week 3).
- **Clay hands** in frame, not real skin: consistent with the objects, avoids bad AI hands, and the student could be anyone.
- **9:16 vertical** for every frame and clip. The picture panel is portrait on desktop and phone.
- **Slow, steady camera inside each scene.** Speed lives only in the whip pans.

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

1. One still per scene in Nano Banana, all with the same backdrop, light and clay look.
2. Animate each still into a 4-6 s clip (image-to-video).
3. Export each clip as a frame sequence; the page scrubs through them on scroll and whip-pans between them.

## Status

- Scene 1 dress-form still (v2, not POV) works: flat #EEEDE8 background, used in the prototype panel. Needs a higher-res version.
- Next: POV stills for scenes 1-3.
