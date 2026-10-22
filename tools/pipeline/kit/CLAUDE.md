# Reel kit: instructions for Claude

You are helping the user make a vertical reel (1080×1920, 30 fps) with this kit, the way aixsam.dev makes its reels:
script → voice → word timings → talking mascot → web page → video. The user decides; you do the work.
Be honest above everything: never invent a number, a feature or a quote for the reel.

## Files
- `script.txt`: exactly what the voice says. Numbers written as words. Hinglish in English letters, as it sounds.
- `build.py`: `python3 build.py check` prints what the recording says; `python3 build.py` writes `data.js` (word times + mouth per frame).
- `reel.html`: the reel. Any element with `data-at="@word"` pops in when that word is spoken, `data-out="@word"` hides it,
  `@word#2` = the second time the word is said. `setT(t)` draws the frame at t seconds.
- `render.py`: `python3 render.py` → `reel.mp4`. `python3 render.py shots 2,5,9` saves test frames shot_2.0.jpg… for checking.
- `mascot-closed.png` / `mascot-open.png`: the character (placeholder face until the user uploads their own pair).
- `vo.wav`: the voice (you make it from the user's MP3).

## 0. Setup (do this first, quietly)
1. Unzip the kit if it's a zip; work in that folder.
2. Check `python3 --version`, `ffmpeg -version`, and `python3 -c "import pocketsphinx, numpy, playwright"`.
   Install what's missing: `pip install pocketsphinx numpy playwright` and `python3 -m playwright install chromium`
   (add `--break-system-packages` if pip refuses; ffmpeg via brew / apt / winget).
3. If something can't be installed where you are running (no internet, no browser), say so in one line and keep going:
   you will still write every file, and the user runs the last commands on their own computer.
4. Then ask the user, in one message, for:
   - the reference reel: its transcript, the video, or screenshots (what makes it work: hook, beats, length)
   - the tool / topic link (GitHub repo, official page)
   - language (English or Hinglish), the comment keyword, and their handle
   - optional: their two mascot pictures (mouth closed / mouth open, same pose)

## 1. Research
Read the tool's README / official page (web search or fetch; for GitHub also try raw.githubusercontent.com/<owner>/<repo>/main/README.md).
Write down every fact you might use with where it came from. If the reference reel claims something the source doesn't support, drop it.

## 2. Script (wait for approval)
- 35–45 seconds, about 90–110 words, one idea per sentence, simple words. Follow the reference's beats and rhythm, not its words.
- First sentence = hook with: subject (you / I / developers), action, result, and a TRUE before → after contrast from the sources.
- End with: Comment "<KEYWORD>" and I'll send you the link.
- Show the user: the script, one line under the hook naming subject · action · result · contrast, and the list of facts with sources.
- STOP and wait until the user approves or edits it.

## 3. Voice (wait for the MP3)
- Save the approved script to `script.txt` (numbers as words).
- Give the user the exact text to paste into their voice tool (ElevenLabs, any TTS, or to read themselves) and wait for the audio file.
- Never generate the voice yourself unless the user asks.
- When the MP3 arrives: `ffmpeg -y -i <file> -ac 1 -ar 44100 vo.wav`. If it's longer than ~50 s, offer `-af atempo=1.15`.
- Run `python3 build.py check` and compare with `script.txt`. AI voices sometimes add, drop or change words: make `script.txt` match what was actually said.
- Run `python3 build.py`. If it says "matched X of Y words", fix `script.txt` and run it again.

## 4. Mascot
If the user uploaded two pictures: save them as `mascot-closed.png` and `mascot-open.png` (same size, about 800×800, transparent or plain background).
If the face jumps between the two, copy only the mouth area of the open one onto the closed one (Pillow, a soft ellipse mask) and save that as the open picture.

## 5. Animation (reel.html)
Replace the example cards with cards for this script:
- One card per beat, popping in on the word that introduces it; hide the previous one with `data-out` so the screen never stacks up.
- Real content only: the repo name, the real numbers with their source in small text, real commands. Label illustrations "example".
- Readable on a phone: text at least 60px, short lines, keep everything above `top:900px` (captions and mascot live below).
- Something on screen at every moment, but only one idea at a time. A big stamp for the payoff number; the keyword big on the CTA.
- Each cue word must be in `script.txt`; use `@word#2` for a repeated word. The page throws an error for a wrong cue.

## 6. Check, then render
- `python3 render.py shots <a time inside every beat>` and look at the frames: overlaps, cut-off text, a card showing before its word, empty gaps. Fix and repeat.
- `python3 render.py` → `reel.mp4`. Give the user the file.
- If you couldn't render here: give the user the whole folder (zip) and these two commands to run in it: `python3 build.py` then `python3 render.py`.

## 7. Caption
Write the post caption: first line = the hook with the contrast (under ~125 characters), one emoji line per feature,
one honest line (the catch / limits), `Comment "<KEYWORD>"`, and 5 hashtags. In the reel's language.
