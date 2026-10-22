"""python3 render.py -> reel.mp4 (1080x1920, 30 fps). A browser draws every frame of reel.html, ffmpeg glues them + vo.wav.
   python3 render.py shots 2,5,9 -> shot_2.0.jpg ... test frames to check before the full render."""
import sys
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

FPS = 30
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1080, 'height': 1920})
    errors = []; page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(Path('reel.html').resolve().as_uri()); page.wait_for_load_state('networkidle')
    assert not errors, errors
    if sys.argv[1:2] == ['shots']:
        for t in sys.argv[2].split(','):
            page.evaluate(f'setT({t})'); page.screenshot(path=f'shot_{float(t):.1f}.jpg', type='jpeg', quality=85)
        browser.close(); sys.exit('saved test frames')
    n = int(page.evaluate('DURATION') * FPS)
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-c:v', 'mjpeg', '-r', str(FPS), '-i', '-',
                           '-i', 'vo.wav', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-af', 'apad', '-c:a', 'aac',
                           '-b:a', '192k', '-shortest', '-movflags', '+faststart', 'reel.mp4'], stdin=subprocess.PIPE)
    for i in range(n):
        page.evaluate(f'setT({i / FPS})')
        ff.stdin.write(page.screenshot(type='jpeg', quality=92))
        if i % 150 == 0: print(f'frame {i}/{n}')
    ff.stdin.close(); ff.wait(); browser.close()
print('done: reel.mp4')
