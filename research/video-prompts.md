# Video prompts: weeks 1-3

Image-to-video. Upload the week's still as the **start frame**, paste the prompt, generate.
Stills: `chat gpt images/week 1.png`, `week 2 .1.png`, `week 3.png` (also in `prototypes/assets/` as .webp).

## Settings (every clip)

- **Length:** 5 seconds
- **Aspect:** 9:16, or "match input image"
- **Resolution:** the highest the free plan allows (720p minimum, 1080p if possible)
- **Mode:** "high quality" / "professional" if offered
- **Audio:** off
- **Negative prompt** (if the tool has one):

```
camera shake, handheld, cuts, zoom, colour, skin tones, real skin, room, walls, floor, text, logo, extra fingers, morphing hands, new objects, flicker
```

The whip pans between weeks are done in the browser, so each clip should be calm, with a steady camera.

---

## Week 1: Take a measurement

```
The two clay-white hands slowly pull the measuring tape snug around the dress form's bust. The tape tightens and lies flat against the form, the loose ends hanging below lift slightly and sway. Near the end, the camera tilts down very slightly toward the point where the hands hold the tape, as if reading the measurement. Slow, smooth, calm motion. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

## Week 2: Meet the machine

```
The sewing machine runs: the needle moves up and down quickly and steadily, the black thread twitches as it feeds from the spool. The clay-white hands gently guide the fabric, which slides smoothly under the presser foot, and the black stitch line grows longer. Camera completely steady, seated point of view. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

## Week 3: Mark and cut

```
The right hand closes the black-handled shears in a slow, clean cut along the line, opens them, moves forward and cuts again. The cut edge of the fabric lifts and curls away from the blades. The left hand stays flat and still on the fabric. Camera completely steady, looking down. Everything stays matte clay-white, the background stays flat and empty. No cuts, no new objects.
```

---

## If it goes wrong

- **Hands melt or grow fingers:** shorten the motion ("one slow movement") and regenerate. Small motions stay cleaner.
- **Colours or skin appear:** add "monochrome, everything is white clay like a sculpture".
- **Camera wanders:** add "locked-off tripod shot" (weeks 2 and 3).
- **Too fast:** add "slow motion, half speed".

## After generating

Download the MP4s and save them as `videos/week-1.mp4`, `week-2.mp4`, `week-3.mp4`. They get converted to frame sequences so scrolling plays them.
