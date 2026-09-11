#!/usr/bin/env python3
"""Preserve CSS tracking and table rules in the native Artifact Tool export.
Does not rasterize text/tables. Uses measured DOM styles, not inferred content.
Video posters remain static for PPTX portability; the original MP4 is
delivered separately and the Slidev source retains live animation.
"""
import sys, json, zipfile, os
from xml.etree import ElementTree as E
from pathlib import Path
p=Path(sys.argv[1]); slides=json.loads(Path(str(p)+'.geometry.json').read_text())
A='http://schemas.openxmlformats.org/drawingml/2006/main'
P='http://schemas.openxmlformats.org/presentationml/2006/main'
E.register_namespace('a',A);E.register_namespace('p',P)
ns={'a':A,'p':P}
def tracking(parent,style):
    for r in parent.findall('.//a:rPr',ns)+parent.findall('.//a:defRPr',ns)+parent.findall('.//a:endParaRPr',ns):
        r.set('spc',str(round(style['letterSpacing']*75)))
        r.set('lang','ko-KR')
with zipfile.ZipFile(p) as z:
    entries={n:z.read(n) for n in z.namelist()}
for i,data in enumerate(slides,1):
    name=f'ppt/slides/slide{i}.xml'; root=E.fromstring(entries[name]); texts={t['shapeName']:t for t in data['texts']}
    for sh in root.findall('.//p:sp',ns):
        props=sh.find('p:nvSpPr/p:cNvPr',ns)
        if props is not None and props.get('name') in texts:tracking(sh,texts[props.get('name')]['style'])
    for table,d in zip(root.findall('.//a:tbl',ns),data['tables']):
        # Suppress the runtime's default table border style explicitly.
        for row,dr in zip(table.findall('a:tr',ns),d['rows']):
            for cell,dc in zip(row.findall('a:tc',ns),dr['cells']):
                tracking(cell,dc['style'])
                pr=cell.find('a:tcPr',ns)
                if pr is None:pr=E.SubElement(cell,f'{{{A}}}tcPr')
                for side in ['lnL','lnR','lnT','lnB','lnTlToBr','lnBlToTr']:
                    for old in pr.findall(f'a:{side}',ns):pr.remove(old)
                    line=E.SubElement(pr,f'{{{A}}}{side}',{'w':'0'})
                    E.SubElement(line,f'{{{A}}}noFill')
                for para in cell.findall('a:txBody/a:p',ns):
                    ppr=para.find('a:pPr',ns)
                    if ppr is None:ppr=E.Element(f'{{{A}}}pPr');para.insert(0,ppr)
                    for old in ppr.findall('a:lnSpc',ns):ppr.remove(old)
                    spacing=E.SubElement(ppr,f'{{{A}}}lnSpc')
                    E.SubElement(spacing,f'{{{A}}}spcPts',{'val':str(round(dc['style']['lineHeight']*75))})
    entries[name]=E.tostring(root,encoding='utf-8',xml_declaration=True)
with zipfile.ZipFile(str(p)+'.tmp','w',zipfile.ZIP_DEFLATED) as z:
    for name,b in entries.items():z.writestr(name,b)
os.replace(str(p)+'.tmp',p)
print(f'Preserved native typography and cell rules on {len(slides)} slides.')
