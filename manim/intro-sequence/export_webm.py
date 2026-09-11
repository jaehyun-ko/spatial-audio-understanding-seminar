"""Browser-compatible WebM plus six sections with aligned keyframes."""
import json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2];public=root/'public/animations/intro-sequence'
meta=json.loads((public/'slides.json').read_text())
full=public/'intro-sequence.webm'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(public/'intro-sequence.mp4'),'-vf','scale=1704:606','-an','-c:v','libvpx-vp9','-crf','26','-b:v','0','-deadline','realtime','-cpu-used','6','-row-mt','1','-threads','4','-g','120','-force_key_frames',','.join(str(s['start']) for s in meta),'-pix_fmt','yuv420p',str(full)],check=True)
for s in meta:
 subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(s['start']),'-i',str(full),'-t',str(s['duration']),'-map','0:v:0','-c','copy',str(public/(s['id']+'.webm'))],check=True)
print('Published 1704×606, 60 fps WebM and six keyframe-aligned sections')
