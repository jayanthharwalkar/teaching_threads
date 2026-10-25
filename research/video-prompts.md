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

Plan: Kling Standard, 660 credits/month. Budget for the whole site: about 9 scenes + 8 transitions.

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

## Scene clips

| Week | Start frame | Status |
|---|---|---|
| 1 Measure | `chat gpt images/week 1.png` | Done: `kling videos/kling_20261025_VIDEO_The_two_cl_4587_0.mp4` |
| 2 Machine | `chat gpt images/week 2 .1.png` | Done: `kling videos/kling_20261025_VIDEO_The_sewing_4512_0.mp4` |
| 3 Cut | `chat gpt images/week 3.png` (grip fixed) | Done: `kling videos/kling_20261025_VIDEO_The_right__4779_0.mp4` |

### Week 1: Take a measurement

```
The two clay-white hands slowly pull the measuring tape snug around the dress form's bust. The tape tightens and lies flat against the form, the loose ends hanging below lift slightly and sway. Near the end, the camera tilts down very slightly toward the point where the hands hold the tape, as if reading the measurement. Slow, smooth, calm motion. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

### Week 2: Meet the machine

```
The sewing machine runs: the needle moves up and down quickly and steadily, the black thread twitches as it feeds from the spool. The clay-white hands gently guide the fabric, which slides smoothly under the presser foot, and the black stitch line grows longer. Camera completely steady, seated point of view. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

### Week 3: Mark and cut

```
The right hand closes the black-handled shears in a slow, clean cut along the line, opens them, moves forward and cuts again. The cut edge of the fabric lifts and curls away from the blades. The left hand stays flat and still on the fabric. Camera completely steady, looking down. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

Week 3 grip fix (ChatGPT, same chat as the stills):

```
Same image, but the right hand holds large tailor's shears properly: thumb through the small upper ring, fingers through the large lower ring, long blades, black handles. Keep everything else the same.
```

---

## Transitions

The camera pulls back from one object, drifts across the empty backdrop and settles on the next, like a person turning to the next tool. One simple move per clip.

Keyframes come from the clips themselves, cropped exactly like the page frames, so scene → transition → scene joins without a jump. Claude makes them (see "Processing").

| Transition | Start frame | End frame | Status |
|---|---|---|---|
| 1 → 2 | `kling videos/transition-1-2-start.png` | `kling videos/transition-1-2-end.png` | Done: `kling videos/kling_20261025_Image_to_Video_The_camera_4651_0.mp4` → `prototypes/assets/trans-1-2/` (processed **without** the crop, see Processing) |
| 2 → 3 | `kling videos/transition-2-3-start.png` | `kling videos/transition-2-3-end.png` | Done: `kling videos/kling_20261025_Image_to_Video_The_camera_4784_0.mp4` → `prototypes/assets/trans-2-3/` (standard crop) |

### Transition 1 → 2: dress form to machine

```
The camera slowly pulls back from the dress form, then drifts to the right through the empty off-white space and settles on the sewing machine. One smooth continuous camera move, no cuts. Everything stays matte clay-white, the background stays flat and empty, no room, no shadows.
```

### Transition 2 → 3: machine to cutting table

```
The camera slowly rises and pulls back from the sewing machine, then drifts to the right through the empty off-white space and tilts down onto the fabric and shears on the cutting table. One smooth continuous camera move, no cuts. Everything stays matte clay-white, the background stays flat and empty, no room, no shadows.
```

---

## If it goes wrong

- **Hands melt or grow fingers:** shorten the motion ("one slow movement") and regenerate.
- **Colours or skin appear:** add "monochrome, everything is white clay like a sculpture".
- **Camera wanders in a scene clip:** add "locked-off tripod shot".
- **Transition crossfades instead of moving:** make sure "fade, dissolve" are in the negative prompt; add "the camera physically moves, the objects never fade".
- **Too fast:** add "slow motion, half speed".
- With few credits, don't re-roll an "okay" clip; a good clip for every week beats a perfect one for a single week.

---

## Processing (Claude)

ffmpeg comes from the `imageio_ffmpeg` Python package (`python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`); there is no system ffmpeg.

- **Standard crop for every clip:** `crop=1100:1650:38:0` (exact 2:3, removes the KlingAI watermark strip at the bottom, identical framing across clips).
- **Frame sequence:** every 2nd frame, scaled to 720×1080, WebP quality 72, audio dropped → 61 frames (~0.9 MB) per 5 s clip, saved as `prototypes/assets/week-N/f001.webp …`.
  `-an -vf "select='not(mod(n\,2))',crop=1100:1650:38:0,scale=720:1080" -fps_mode vfr -c:v libwebp -quality 72`
- **Transition keyframes:** last frame of clip A (`-sseof -0.05`) and first frame of clip B, **full frame, no crop**, as PNG at Kling's output size (1176×1764). The transition clip then gets the standard crop like every other clip, so its ends match the scene frames exactly.
  Don't crop the keyframes, or the zoom is applied twice: the 1 → 2 keyframes were cropped and scaled back up, so that transition is the one exception, framed like the cropped scenes already. Its frames are made from the full watermark-free frame with no crop (`-vf "select='not(mod(n\,2))',scale=720:1080"`).
- **On the page** (`prototypes/course.html`): each video scene is a `.shot` with `data-seq`, `data-count` and a focus height `data-fy` / `--fy` (week 1 0.62, week 2 0.72, week 3 0.62) so the crop keeps the action in view. Frames draw to a canvas, scrubbed by scroll; the still shows until the frames load.
- **Transitions on the page:** a `.shot.tr` between the two weeks, with `data-fy` / `data-fy-end` (the focus height eases from one scene's value to the next), `data-span="0.25"` (a quick move, a quarter of a week's scroll; the frames ease in-out so the middle rushes by) and `data-week` set to the week it arrives at. Swaps into and out of a `.tr` shot skip the whip pan; the caption changes halfway through the move.
- Test in headless Chromium (Playwright is installed) before publishing.
