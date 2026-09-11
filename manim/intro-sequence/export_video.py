"""Add the existing slide frame to the continuous Manim body for a shareable movie."""
import json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2]
meta=json.loads((root/'public/animations/intro-sequence/slides.json').read_text())
texts=root/'tmp/intro-sequence/video-text';texts.mkdir(parents=True,exist_ok=True)
reg=Path.home()/'Library/Fonts/Pretendard-Regular.otf'
bold=Path.home()/'Library/Fonts/Pretendard-Bold.otf'
filters=['scale=1704:606','pad=1920:1080:108:252:color=0xF6F8FA','drawbox=x=0:y=72:w=8:h=84:color=0x008B9A:t=fill','drawbox=x=108:y=882:w=1704:h=1:color=0xD4DDE7:t=fill','drawbox=x=108:y=904:w=7:h=36:color=0x008B9A:t=fill']
for s in meta:
 for key,font,size,x,y,col in [('title',bold,66,108,72,'142233'),('takeaway',reg,40,144,902,'142233'),('source',reg,21,108,1016,'586879'),('number',reg,21,1829,1031,'586879')]:
  file=texts/f'{s["id"]}-{key}.txt';file.write_text(str(s[key]))
  enable=f'gte(t,{s["start"]})*lt(t,{s["end"]})'
  filters.append(f"drawtext=fontfile='{font}':textfile='{file}':fontsize={size}:fontcolor=0x{col}:x={x}:y={y}:enable='{enable}'")
script=root/'tmp/intro-sequence/video-frame.filter';script.write_text(',\n'.join(filters))
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(root/'public/animations/intro-sequence/intro-sequence.mp4'),'-filter_script:v',str(script),'-an','-c:v','libx264','-preset','veryfast','-crf','20','-threads','4','-pix_fmt','yuv420p','-movflags','+faststart',str(root/'output/intro-sequence/intro-02-07.mp4')],check=True)
print('Exported 1920×1080, 60 fps, 59.25 s presentation movie')
