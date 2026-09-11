"""Numerical checks of the explicitly illustrated geometry and rendered media."""
import importlib.util,json,subprocess
from pathlib import Path
import numpy as np
import av
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('intro',Path(__file__).with_name('intro.py'))
intro=importlib.util.module_from_spec(spec);spec.loader.exec_module(intro)
checks=0
for a in np.linspace(20,160,29):
 for d in [.6,1.2,1.8]:
  p=intro.spherical(3.8,np.deg2rad(a),np.deg2rad(25))
  assert np.isclose(np.linalg.norm(p),3.8)
  m1=np.array([-d/2,0.,0.]);m2=-m1
  tau=(np.linalg.norm(p-m2)-np.linalg.norm(p-m1))/343
  if a<90:assert tau<0
  elif a>90:assert tau>0
  else:assert abs(tau)<1e-12
  for mic in [m1,m2]:
   hit,length=intro.reflect(p,mic)
   assert np.isclose(hit[1],3.8)
   assert np.isclose(length,np.linalg.norm(hit-p)+np.linalg.norm(mic-hit))
   inc=(hit-p)/np.linalg.norm(hit-p);out=(mic-hit)/np.linalg.norm(mic-hit)
   normal=np.array([0.,1.,0.]);assert np.allclose(out,inc-2*np.dot(inc,normal)*normal)
  checks+=1
public=root/'public/animations/intro-sequence'
meta=json.loads((public/'slides.json').read_text())
continuity=[];previous=None
for s in meta:
 container=av.open(str(public/(s['id']+'.mp4')))
 first=None;last=None;count=0
 for f in container.decode(video=0):
  if first is None:first=f.to_ndarray(format='rgb24')
  last=f;count+=1
 last=last.to_ndarray(format='rgb24')
 if previous is not None:
  diff=np.abs(first.astype(float)-previous.astype(float));continuity.append(dict(boundary=s['id'],mean_abs_difference=float(diff.mean()),pixel_p99=float(np.percentile(diff,99))))
 previous=last;container.close()
 assert first.shape==(808,2272,3)
# Check the background at every frame, including transitions, without full-frame conversion.
raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(public/'intro-sequence.mp4'),'-vf','crop=8:8:0:0,format=rgb24','-f','rawvideo','-'])
corners=np.frombuffer(raw,dtype=np.uint8).reshape(-1,8,8,3)
assert corners.min()>235
bounds=[]
for checkpoint in json.loads((root/'tmp/intro-sequence/checkpoints.json').read_text()):
 for l in checkpoint['labels']:
  x,y,_=l['center']
  if abs(x)+l['width']/2>7.1 or abs(y)+l['height']/2>2.525:bounds.append(l)
assert not bounds
assert max(c['mean_abs_difference'] for c in continuity)<2
report=dict(geometry_cases=checks,light_frames=len(corners),min_background_channel=int(corners.min()),continuity=continuity,text_bounds_violations=bounds)
(root/'tmp/intro-sequence/physics-and-media.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
