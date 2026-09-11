"""Publish only the newly rendered intro media; never rebuild the rest of the deck."""
import json,subprocess,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[2]
base=root/'tmp/intro-sequence/media-final/videos/intro/808p60'
public=root/'public/animations/intro-sequence'
public.mkdir(parents=True,exist_ok=True)
sections=json.loads((base/'sections/intro-sequence.mp4.json').read_text())
meta=json.loads((Path(__file__).parent/'slides.json').read_text())
assert [s['name'] for s in sections]==[s['id'] for s in meta]
def ff(*args): subprocess.run(['ffmpeg','-y','-loglevel','error',*map(str,args)],check=True)
ff('-i',base/'intro-sequence.mp4','-c','copy','-movflags','+faststart',public/'intro-sequence.mp4')
time=0
for row,s in zip(meta,sections):
    src=base/'sections'/s['video']
    ff('-i',src,'-c','copy','-movflags','+faststart',public/f'{s["name"]}.mp4')
    ff('-i',src,'-frames:v','1',public/f'{s["name"]}-start.png')
    ff('-sseof','-0.25','-i',src,'-frames:v','1',public/f'{s["name"]}-end.png')
    duration=float(s['duration'])
    row.update(start=round(time,6),end=round(time+duration,6),duration=duration)
    time+=duration
(public/'slides.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
(root/'output/intro-sequence/slides.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
print(f'Published {len(meta)} sections, {time:.2f} seconds, 2272×808 at 60 fps')
