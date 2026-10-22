"""Turns your voice into timings for the reel.
  python3 build.py check   -> prints what the recording actually says (catch a voice AI that changed your words)
  python3 build.py         -> data.js: when every word is spoken + when the mouth is open (30 fps)
Needs: script.txt (exactly what the voice says, numbers written as words) and vo.wav."""
import json, re, subprocess, sys
import numpy as np
from pocketsphinx import Decoder

FPS = 30
pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', 'vo.wav', '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                     capture_output=True, check=True).stdout

if sys.argv[1:] == ['check']:  # free listening, 5 seconds at a time; compare with script.txt by eye
    d = Decoder(samprate=16000)
    for i in range(0, len(pcm), 160000):
        d.start_utt(); d.process_raw(pcm[i:i + 160000], full_utt=True); d.end_utt()
        print(f'{i // 32000:3d}s', ' '.join(s.word.split('(')[0] for s in d.seg() if s.word[0] not in '<['))
    sys.exit()

# 1. word timings: force-align the script to the recording
shown = open('script.txt', encoding='utf-8').read().split()           # words as they appear in captions
words = [re.sub(r"[^a-z']", '', w.lower()) for w in shown]
assert all(words), 'write numbers as words in script.txt (3 -> three)'
G2P = [('chh', 'CH'), ('aa', 'AA'), ('ai', 'EH'), ('au', 'AO'), ('ee', 'IY'), ('oo', 'UW'), ('ei', 'EY'), ('kh', 'K'),
       ('gh', 'G'), ('ch', 'CH'), ('sh', 'SH'), ('th', 'T'), ('dh', 'D'), ('bh', 'B'), ('ph', 'F'), ('jh', 'JH'),
       ('a', 'AH'), ('e', 'EY'), ('i', 'IH'), ('o', 'OW'), ('u', 'UH'), ('y', 'Y'), ('k', 'K'), ('g', 'G'), ('j', 'JH'),
       ('t', 'T'), ('d', 'D'), ('n', 'N'), ('p', 'P'), ('b', 'B'), ('m', 'M'), ('r', 'R'), ('l', 'L'), ('v', 'V'),
       ('w', 'W'), ('s', 'S'), ('h', 'HH'), ('z', 'Z'), ('f', 'F'), ('c', 'K'), ('q', 'K'), ('x', 'K S')]
def g2p(w):  # rough spelling -> sounds, for Hindi/Hinglish words and names the English dictionary doesn't know
    w, out, i = w.replace("'", ''), [], 0
    while i < len(w):
        for k, p in G2P:
            if w.startswith(k, i): out.append(p); i += len(k); break
        else: i += 1
    return ' '.join(out)
d = Decoder(samprate=16000, bestpath=False)
keys = []
for w in words:
    if d.lookup_word(w) is None:
        if d.lookup_word('x_' + w) is None: d.add_word('x_' + w, g2p(w), True)
        w = 'x_' + w
    keys.append(w)
d.set_align_text(' '.join(keys))
d.start_utt(); d.process_raw(pcm, full_utt=True); d.end_utt()
times = [(s.start_frame / 100, (s.end_frame + 1) / 100) for s in d.seg() if s.word not in ('<s>', '</s>', '<sil>', '(NULL)')]
assert len(times) == len(words), f'matched {len(times)} of {len(words)} words: run "python3 build.py check" and fix script.txt'

# 2. mouth: open on the loud peak of each syllable, closed in the dips and silences
a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
hop = 16000 // FPS
rms = np.array([np.sqrt(np.mean(a[i:i + hop] ** 2)) for i in range(0, len(a), hop)])
rms /= np.percentile(rms[rms > .01], 90)
peak = np.array([rms[max(0, i - 3):i + 4].max() for i in range(len(rms))])
mouth = ''.join('o' if r > .12 and r / (p + 1e-6) > .6 else 'c' for r, p in zip(rms, peak))

data = {'words': [[round(s, 2), round(e, 2), w] for (s, e), w in zip(times, shown)], 'mouth': mouth,
        'duration': round(len(a) / 16000 + 1, 2)}
open('data.js', 'w').write('window.DATA=' + json.dumps(data) + ';')
print(f"ok: {len(words)} words, {data['duration']}s, mouth open {mouth.count('o') * 100 // len(mouth)}% of frames")
