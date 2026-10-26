# Kling prompts

How the course videos are made. Direction and decisions: `course-visual-direction.md`. Still prompts: `nano-banana-prompts.md` (stills are now made in ChatGPT; same prompts plus the tweaks noted there).

## Workflow

1. **Still** in ChatGPT (2:3 portrait, all scenes in one chat for a consistent look). Saved in `chat gpt images/`.
2. **Scene clip** in Kling: keyframe mode, still as the **start frame only**, scene prompt below.
3. **Transition clip** in Kling: keyframe mode with **start and end frames** (made by Claude from the clips, see below), transition prompt below.
4. Download the MP4s to `kling videos/`. Claude turns each into a frame sequence for the page.

Use **keyframe**, never omni reference (omni reference reinterprets the image and breaks the match with the page).

## Settings (every clip)

- Length: **5 s**
- Aspect: match input (2:3) or 9:16
- **Audio: OFF** (the site never plays sound; audio costs extra credits)
- Watermark removal on (paid plan). If a download still shows the KlingAI watermark, download it again without; the standard crop removes it either way
- Models: scene clips on the better model (3.0 or 2.6); transitions on the cheaper model (2.5 Turbo) if it supports start and end frames. Check the credit cost on the Generate button.

Plan: Kling Standard, 660 credits/month. The course section needs 5 scenes + 4 transitions; 2 scenes are done, so 3 scenes + 4 transitions to go.

### Negative prompt: scene clips

```
camera shake, handheld, cuts, zoom, colour, skin tones, real skin, room, walls, floor, text, logo, extra fingers, morphing hands, new objects, flicker
```

### Negative prompt: transitions

```
cuts, fade, dissolve, morphing objects, camera shake, colour, skin tones, room, walls, floor, text, logo, extra fingers
```

("fade" and "dissolve" stop Kling from cheating with a crossfade instead of moving the camera.)

---

## The five stages

Decided 2026-10-25: the course section shows 5 stages, not weeks (the course PDFs have modules, not a weekly schedule). Same stages for the 3- and 6-month courses. Cutting was dropped (a step inside every garment, not something a student pictures learning); aari stays out because it is 6-month only.

The dress form comes back in stages 1, 4 and 5 and gets dressed as the course goes: bare, then a blouse, then a lehenga.

## Scene clips

| Stage | Start frame | Status |
|---|---|---|
| 1 Measure | `chat gpt images/week 1.png` | Done: `kling videos/kling_20261025_VIDEO_The_two_cl_4587_0.mp4` |
| 2 Draft the pattern | `chat gpt images/stage 2.png` | Done: `kling videos/kling_20261026_VIDEO_The_right__1298_0.mp4` → `prototypes/assets/stage-2/` (graded, see Processing) |
| 3 Stitch | `chat gpt images/week 2 .1.png` | Done: `kling videos/kling_20261025_VIDEO_The_sewing_4512_0.mp4` |
| 4 Your first blouse | `chat gpt images/stage 4.2.png` | Done: `kling videos/kling_20261026_VIDEO_The_right__1492_0.mp4` → `prototypes/assets/stage-4/` |
| 5 Lehenga | `chat gpt images/stage 5.1.png` (start) + `chat gpt images/stage 5b.png` (end) | To do: keyframe mode with **start and end frames** |

### Stage 1: Measure (done)

```
The two clay-white hands slowly pull the measuring tape snug around the dress form's bust. The tape tightens and lies flat against the form, the loose ends hanging below lift slightly and sway. Near the end, the camera tilts down very slightly toward the point where the hands hold the tape, as if reading the measurement. Slow, smooth, calm motion. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

### Stage 2: Draft the pattern

```
The right clay-white hand slowly draws the pencil straight down along the ruler's right edge, leaving a thin black line on the paper behind it. The left hand holds the ruler flat and completely still. Near the end, the pencil lifts off the paper. Camera completely steady, looking down at the table. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

### Stage 3: Stitch (done)

```
The sewing machine runs: the needle moves up and down quickly and steadily, the black thread twitches as it feeds from the spool. The clay-white hands gently guide the fabric, which slides smoothly under the presser foot, and the black stitch line grows longer. Camera completely steady, seated point of view. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

### Stage 4: Your first blouse

The student fastens the last hook of the finished blouse on the form: it's done and it fits. Indian blouses close at the centre front with hooks and eyes, and the syllabus names them. (The first take, `kling videos/kling_20261026_VIDEO_The_two_cl_1424_0.mp4`, pushed one pin into a finished neckline. That isn't something a tailor does: pins are for fitting, in a row along a seam, before the garment is finished. Rejected.)

```
The right clay-white hand slowly fastens the top hook into its eye at the blouse's neckline, the left hand holds the two edges together. Then both hands let go and smooth the blouse flat down the front. Camera completely steady, very slow push-in. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

### Stage 5: Lehenga

The student ties the lehenga's dori and the camera pulls back to show the finished outfit, the last shot of the section. Start and end frames (`stage 5.1.png` → `stage 5b.png`), so Kling only has to tie the knot and pull back; the full lehenga is fixed by the end frame.

```
The two clay-white hands pull the black drawstring into a small bow at the side of the lehenga's waist, then let go and move out of the frame. The black tassels swing gently and settle. The camera slowly pulls back to show the whole dress form wearing the blouse and the full lehenga, the skirt's folds settling. One smooth continuous move. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

Take 1, `kling videos/kling_20261026_Image_to_Video_The_two_cl_3908_0.mp4`: good, except the two tasselled cords keep growing longer after the hands let go, during the pull-back. Fix prompt (v2):

```
The two clay-white hands finish pulling the black drawstring into a small bow at the side of the lehenga's waist, then let go and move out of the frame. After the hands leave, the bow and its two short tasselled ends stay exactly as they are: the same size and the same length, hanging still just below the waistband, with only a tiny settling sway. The camera slowly pulls back to show the whole dress form wearing the blouse and the full lehenga. The drawstring never gets longer; it only looks smaller because the camera moves away. One smooth continuous move. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

Negative prompt addition: `drawstring growing, cords getting longer, strings stretching, tassels sliding down, extra strings, ribbon unrolling, morphing`. If it still drifts, split into two clips: (a) tie + hands leave with the camera still, (b) pull-back from (a)'s last frame to `stage 5b.png`.

---

## Transitions

The camera pulls back from one object, drifts across the empty backdrop and settles on the next, like a person turning to the next tool. One simple move per clip.

Keyframes come from the clips themselves (start = last frame of the scene before, end = first frame of the scene after). Claude makes them once both scene clips exist (see "Processing").

| Transition | Start frame | End frame | Status |
|---|---|---|---|
| 1 → 2 | `kling videos/transition-1-2-start.png` | `kling videos/transition-1-2-end.png` | Done: `kling videos/kling_20261026_Image_to_Video_The_camera_1328_0.mp4` → `prototypes/assets/trans-1-2/` (standard crop) |
| 2 → 3 | `kling videos/transition-2-3-start.png` | `kling videos/transition-2-3-end.png` | Take 1: `kling videos/kling_20261026_Image_to_Video_The_camera_1361_0.mp4` → `prototypes/assets/trans-2-3/` (kept: the paper morphs into the fabric and the ruler and pencil vanish, read as "your pattern becomes the fabric"). Take 2 with the v2 prompt, `kling videos/kling_20261026_VIDEO_The_clay_w_1402_0.mp4`, rejected: the end frame wasn't used, so it ends on a different, domestic machine and jumps at the join |
| 3 → 4 | `kling videos/transition-3-4-start.png` | `kling videos/transition-3-4-end.png` | Done: `kling videos/kling_20261026_Image_to_Video_The_camera_1506_0.mp4` → `prototypes/assets/trans-3-4/` (standard crop; a faint shadow under the machine table mid-move, left as is) |
| 4 → 5 | `kling videos/transition-4-5-start.png` | `kling videos/transition-4-5-end.png` | Both frames ready (end = `stage 5.1.png` scaled and centre-cropped to 1176×1764, made 2026-10-26) |

(`transition-1-2-*` and `transition-2-3-*` were remade 2026-10-26 for the new order; the old ones went form → machine → cutting.)

### Transition 1 → 2: dress form to drafting table

```
The camera slowly pulls back from the dress form, then drifts to the right through the empty off-white space and tilts down onto the pattern paper and ruler lying on the table. One smooth continuous camera move, no cuts. Everything stays matte clay-white, the background stays flat and empty, no room, no shadows.
```

### Transition 2 → 3: drafting table to machine

v2, tried once and rejected because the end frame didn't take; if re-rolling, check both start and end frames are attached (take 1 with the v1 prompt morphed the paper into the fabric and made the ruler and pencil vanish; v2 keeps the table separate from the machine):

```
The clay-white hands lift off the paper and move out of the bottom of the frame. The camera rises straight up from the table, the pattern paper, ruler and pencil stay where they are and slide out of the bottom of the frame unchanged. The camera then drifts to the right through the empty off-white space to a separate sewing machine standing on its own, and lowers to look down at the needle as the hands come back in to rest on the fabric. One smooth continuous camera move, no cuts. Everything stays matte clay-white, the background stays flat and empty, no room, no shadows.
```

Add to the transitions negative prompt for this one: `paper turning into fabric, objects disappearing, ruler vanishing`.

### Transition 3 → 4: machine to the blouse on the dress form

```
The camera slowly rises and pulls back from the sewing machine, then drifts to the right through the empty off-white space and settles close on the dress form wearing the finished blouse. One smooth continuous camera move, no cuts. Everything stays matte clay-white, the background stays flat and empty, no room, no shadows.
```

### Transition 4 → 5: blouse to the lehenga's waist

Start: last frame of stage 4 (`transition-4-5-start.png`, ready). End: `transition-4-5-end.png` (`stage 5.1.png` scaled to the clip size, ready). A short, simple move: the dress form is the same, only the lehenga appears below the blouse.

```
The clay-white hands let go of the blouse and move out of the frame. The camera slowly tilts down and moves to the left side of the dress form's waist, where the form now wears a lehenga below the blouse, and the hands come back in holding the ends of a black drawstring. One smooth continuous camera move, no cuts. Everything stays matte clay-white, the background stays flat and empty, no room, no shadows.
```

---

## Archive

Retired 2026-10-25 when cutting was dropped:

- Week 3 cut still `chat gpt images/week 3.png` and clip `kling videos/kling_20261025_VIDEO_The_right__4779_0.mp4`. Prompt: "The right hand closes the black-handled shears in a slow, clean cut along the line, opens them, moves forward and cuts again. The cut edge of the fabric lifts and curls away from the blades. The left hand stays flat and still on the fabric. Camera completely steady, looking down. …"
- Transition form → machine `kling videos/kling_20261025_Image_to_Video_The_camera_4651_0.mp4` (its frames in `prototypes/assets/trans-1-2/` were replaced 2026-10-26) and machine → cutting table `kling videos/kling_20261025_Image_to_Video_The_camera_4784_0.mp4` (its frames in `prototypes/assets/trans-2-3/` were replaced 2026-10-26).

---

## If it goes wrong

- **Hands melt or grow fingers:** shorten the motion ("one slow movement") and regenerate.
- **Colours or skin appear:** add "monochrome, everything is white clay like a sculpture".
- **Camera wanders in a scene clip:** add "locked-off tripod shot".
- **Transition crossfades instead of moving:** make sure "fade, dissolve" are in the negative prompt; add "the camera physically moves, the objects never fade".
- **Too fast:** add "slow motion, half speed".
- With few credits, don't re-roll an "okay" clip; a good clip for every stage beats a perfect one for a single stage.

---

## Processing (Claude)

ffmpeg comes from the `imageio_ffmpeg` Python package (`python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`); there is no system ffmpeg.

- **Standard crop for every clip:** `crop=1100:1650:38:0` (exact 2:3, removes the KlingAI watermark strip at the bottom, identical framing across clips).
- **Frame sequence:** every 2nd frame, scaled to 720×1080, WebP quality 72, audio dropped → 61 frames (~0.9 MB) per 5 s clip, saved as `prototypes/assets/week-N/f001.webp …`.
  `-an -vf "select='not(mod(n\,2))',crop=1100:1650:38:0,scale=720:1080" -fps_mode vfr -c:v libwebp -quality 72`
- **Stage 2 grade:** the pattern paper came out warmer and darker than the page (#E6DFD8). Its frames get `curves=all='0/0 0.86/0.91 1/1',hue=s=0.8` before the crop, which brings the paper to about #F0ECE8. Stage 2's side of each transition keyframe gets the same grade, so the transitions match without grading the whole transition clip.
- **Transition keyframes:** last frame of clip A (`-sseof -0.05`) and first frame of clip B, **full frame, no crop**, as PNG at Kling's output size (1176×1764). The transition clip then gets the standard crop like every other clip, so its ends match the scene frames exactly.
  Don't crop the keyframes, or the zoom is applied twice (the retired form → machine transition had that problem).
- **On the page** (`prototypes/course.html`): each video scene is a `.shot` with `data-seq`, `data-count` and a focus height `data-fy` / `--fy` (measure 0.62, stitch 0.72; set the new stages after processing) so the crop keeps the action in view. Frames draw to a canvas, scrubbed by scroll; the still shows until the frames load.
- **Transitions on the page:** a `.shot.tr` between the two weeks, with `data-fy` / `data-fy-end` (the focus height eases from one scene's value to the next), `data-span="0.25"` (a quick move, a quarter of a week's scroll; the frames ease in-out so the middle rushes by) and `data-week` set to the week it arrives at. Swaps into and out of a `.tr` shot skip the whip pan; the caption changes halfway through the move.
- Test in headless Chromium (Playwright is installed) before publishing.
