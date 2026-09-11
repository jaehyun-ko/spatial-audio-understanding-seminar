from pathlib import Path
import re, html
import mistune

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / 'slides.md').read_text(encoding='utf-8')
# Legacy HTML preview only. Actual layout/component verification uses Slidev.
style = '\n'.join((ROOT / 'styles' / name).read_text(encoding='utf-8')
                  for name in ['tokens.css', 'legacy.css', 'seminar.css'])
style = style.replace('.slidev-layout', '.slide').replace("url('/fonts/", "url('../public/fonts/")

# Remove global frontmatter
m = re.match(r'^---\n[\s\S]*?\n---\n', text)
if not m:
    raise SystemExit('frontmatter not found')
body = text[m.end():]
chunks = re.split(r'\n---\n(?=(?:layout:|class:|#|<))', body)
md = mistune.create_markdown(escape=False, plugins=['table'])

out_dir = ROOT / 'preview'
out_dir.mkdir(exist_ok=True)

base_css = f"""
{style}
html, body {{ margin:0; padding:0; background:#dfe5eb; }}
body {{ font-family: Pretendard, 'Noto Sans KR', sans-serif; }}
.slide {{ width:1280px; height:720px; overflow:hidden; position:relative; margin:0; }}
.preview-two {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; }}
pre.diagram {{ white-space:pre-wrap; font-size:15px; background:#f0f5f9; border:1px solid #d9e2ec; padding:18px; }}
.page-no {{ position:absolute; right:24px; bottom:16px; color:#8a97a5; font-size:12px; }}
"""

def parse_chunk(chunk: str):
    meta = {}
    if chunk.startswith(('layout:', 'class:')):
        mm = re.match(r'^([\s\S]*?)\n---\n', chunk)
        if mm:
            for line in mm.group(1).splitlines():
                if ':' in line:
                    k,v=line.split(':',1); meta[k.strip()] = v.strip()
            chunk = chunk[mm.end():]
    return meta, chunk.strip()

def render_markdown(source: str):
    # Replace mermaid with visible, compact diagram source in preview.
    source = re.sub(r'```mermaid\n([\s\S]*?)```', lambda m: '<pre class="diagram">'+html.escape(m.group(1).strip())+'</pre>', source)
    if '::right::' in source:
        left, right = source.split('::right::', 1)
        return f'<div class="preview-two"><div>{md(left)}</div><div>{md(right)}</div></div>'
    return md(source)

index_items=[]
for i, chunk in enumerate(chunks, 1):
    meta, source = parse_chunk(chunk)
    classes = ['slide']
    if meta.get('layout') == 'section': classes.append('section')
    if meta.get('class'): classes.extend(meta['class'].split())
    content = render_markdown(source).replace('src="/', 'src="../public/')
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>{base_css}</style></head>
<body><section class="{' '.join(classes)}">{content}<div class="page-no">{i}/{len(chunks)}</div></section></body></html>'''
    path = out_dir / f'slide-{i:02d}.html'
    path.write_text(doc, encoding='utf-8')
    title = next((ln[2:] for ln in source.splitlines() if ln.startswith('# ')), f'Slide {i}')
    index_items.append(f'<li><a href="slide-{i:02d}.html">{i:02d}. {html.escape(title)}</a></li>')

index = f'''<!doctype html><html><head><meta charset="utf-8"><style>body{{font:16px sans-serif;max-width:900px;margin:40px auto}}li{{margin:8px}}</style></head><body><h1>Slide preview</h1><ol>{''.join(index_items)}</ol></body></html>'''
(out_dir/'index.html').write_text(index, encoding='utf-8')
print(f'generated {len(chunks)} preview slides')
