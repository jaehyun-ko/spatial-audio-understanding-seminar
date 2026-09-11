#!/usr/bin/env node
/** Export rendered Slidev geometry as native PowerPoint text and tables.
 * Original paper figures remain images; no full-slide screenshots are used.
 * Uses the Codex bundled Artifact Tool runtime. Run against a Slidev server.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright-chromium';
import { parseSync } from '@slidev/parser';

const arg = (name, fallback) => { const i=process.argv.indexOf(name); return i<0?fallback:process.argv[i+1] };
const source = arg('--source','slides.md');
const base = arg('--url','http://localhost:3037');
const out = path.resolve(arg('--out','tmp/finalization/candidate.pptx'));
const limit = Number(arg('--limit','1000'));
const runtime = process.env.RUNTIME_NODE_MODULES || path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules');
const { Presentation, PresentationFile } = await import(pathToFileURL(path.join(runtime,'@oai/artifact-tool/dist/artifact_tool.mjs')));
const parsed = parseSync(await fs.readFile(source,'utf8'));
const deck = Presentation.create({slideSize:{width:1280,height:720}});
const audit=[];
await fs.mkdir(path.dirname(out),{recursive:true});

// Serializable browser-side extractor. Original image bytes are read later.
function extract(root) {
  const r0 = root.getBoundingClientRect();
  const scale = 1280/r0.width;
  const rect = r => ({left:(r.x-r0.x)*scale,top:(r.y-r0.y)*scale,width:r.width*scale,height:r.height*scale});
  const visible = el => {
    for(let p=el;p;p=p.parentElement){ const s=getComputedStyle(p); if(s.display==='none'||s.visibility==='hidden'||Number(s.opacity)===0)return false }
    const r=el.getBoundingClientRect();return r.width>0&&r.height>0;
  };
  const color = s => { if(!s||s==='none'||s==='transparent')return null;const v=s.match(/[\d.]+/g)?.map(Number);if(!v||v.length<3||(v[3]??1)===0)return null;return '#'+v.slice(0,3).map(v=>Math.round(v).toString(16).padStart(2,'0')).join('') };
  const style = el => {const c=getComputedStyle(el);return {fontSize:parseFloat(c.fontSize),bold:Number(c.fontWeight)>=600,italic:c.fontStyle==='italic',color:color(c.color),letterSpacing:parseFloat(c.letterSpacing)||0,alignment:c.textAlign==='right'?'right':c.textAlign==='center'?'center':'left',lineHeight:parseFloat(c.lineHeight)||parseFloat(c.fontSize)*1.2}};
  const tables = [...root.querySelectorAll('table')].filter(visible).map(el=>({
    ...rect(el.querySelector('tr').getBoundingClientRect()), width:el.getBoundingClientRect().width*scale,
    rows:[...el.rows].map(tr=>({height:tr.getBoundingClientRect().height*scale,cells:[...tr.cells].map(td=>{
      const c=getComputedStyle(td);return {text:td.querySelector('.seminar-math')?'':td.innerText,...rect(td.getBoundingClientRect()),style:style(td),fill:color(c.backgroundColor),margins:{left:parseFloat(c.paddingLeft),right:parseFloat(c.paddingRight),top:parseFloat(c.paddingTop),bottom:parseFloat(c.paddingBottom)},borderBottom:color(c.borderBottomColor),borderTop:parseFloat(c.borderTopWidth)>0?color(c.borderTopColor):null}
    })}))
  }));
  const rectangles=[];
  for(const el of [...root.querySelectorAll('*')].filter(visible)) {
    if(el.closest('table,svg,.katex'))continue;
    const c=getComputedStyle(el), r=rect(el.getBoundingClientRect());
    if(color(c.backgroundColor))rectangles.push({...r,fill:color(c.backgroundColor)});
    for(const [side,x,y,w,h] of [['Top',r.left,r.top,r.width,parseFloat(c.borderTopWidth)],['Bottom',r.left,r.top+r.height-parseFloat(c.borderBottomWidth),r.width,parseFloat(c.borderBottomWidth)],['Left',r.left,r.top,parseFloat(c.borderLeftWidth),r.height],['Right',r.left+r.width-parseFloat(c.borderRightWidth),r.top,parseFloat(c.borderRightWidth),r.height]]) {
      if(w>0&&h>0&&color(c['border'+side+'Color'])&&c['border'+side+'Style']!=='none')rectangles.push({left:x,top:y,width:w,height:h,fill:color(c['border'+side+'Color'])});
    }
  }
  const texts=[];
  const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
  while(walker.nextNode()) {
    const node=walker.currentNode,el=node.parentElement;
    if(!node.textContent.trim()||!visible(el)||el.closest('svg,script,style,.katex'))continue;
    // Math cells use native positioned prose plus formula images, so the native
    // table does not duplicate KaTeX's HTML/MathML text or disturb inline spacing.
    const cell=el.closest('td,th');
    if(cell&&!cell.querySelector('.seminar-math'))continue;
    const s=style(el),rows=[]; let at=0;
    // Split by actual rendered lines, preserving natural Korean line breaks.
    for(const char of node.textContent){ const start=at;at+=char.length; const range=document.createRange();range.setStart(node,start);range.setEnd(node,at);const rr=range.getBoundingClientRect();if(!rr.width||!rr.height)continue;
      let line=rows.find(l=>Math.abs(l.top-rr.top)<2);if(!line){line={top:rr.top,left:rr.left,right:rr.right,height:rr.height,text:''};rows.push(line)}
      line.text+=char;line.left=Math.min(line.left,rr.left);line.right=Math.max(line.right,rr.right);
    }
    for(const line of rows)if(line.text.trim())texts.push({text:line.text.replace(/[ \t\r\n]+/g,' '),left:(line.left-r0.left)*scale,top:(line.top-r0.top)*scale,width:(line.right-line.left)*scale,height:line.height*scale,style:s,link:el.closest('a')?.href||null});
  }
  const images=[...root.querySelectorAll('img')].filter(visible).map(el=>({src:el.currentSrc||el.src,alt:el.alt,...rect(el.getBoundingClientRect()),naturalWidth:el.naturalWidth,naturalHeight:el.naturalHeight}));
  for(const el of [...root.querySelectorAll('video')].filter(visible))images.push({src:el.poster,videoSrc:el.querySelector('source[type="video/mp4"]')?.src||el.currentSrc,alt:el.getAttribute('aria-label')||'설명 애니메이션 마지막 프레임',...rect(el.getBoundingClientRect()),naturalWidth:el.videoWidth,naturalHeight:el.videoHeight});
  // Inline KaTeX spans have the surrounding line height. Fractions, powers,
  // and stretchy delimiters can extend beyond it; include the actual bases.
  const formula=[...root.querySelectorAll('.katex')].filter(visible).map(el=>{
    const boxes=[el,...el.querySelectorAll('.katex-html > .katex-base, .katex-html > .base')].map(e=>e.getBoundingClientRect());
    const x=Math.min(...boxes.map(b=>b.left))-1,y=Math.min(...boxes.map(b=>b.top))-1;
    const right=Math.max(...boxes.map(b=>b.right))+1,bottom=Math.max(...boxes.map(b=>b.bottom))+1;
    return {...rect({x,y,width:right-x,height:bottom-y}),text:el.querySelector('annotation')?.textContent||el.textContent};
  });
  const cover=root.classList.contains('seminar-cover'),section=root.classList.contains('seminar-section'),focus=root.classList.contains('seminar--focus');
  const footer=[...document.querySelectorAll('.global-page-number')].find(el=>visible(el)&&el.getBoundingClientRect().right>0&&el.getBoundingClientRect().left<1280);
  if(footer&&visible(footer))texts.push({text:footer.innerText,...rect(footer.getBoundingClientRect()),style:style(footer)});
  // Shared template rules and background artwork are preserved independently.
  const rootBarColor=color(getComputedStyle(root,'::before').backgroundColor);
  if(rootBarColor)rectangles.push({left:0,top:48,width:5,height:56,fill:rootBarColor});
  const takeaway=root.querySelector('.seminar-takeaway');
  if(takeaway?.textContent.trim()){const r=rect(takeaway.getBoundingClientRect()),fill=color(getComputedStyle(takeaway,'::before').backgroundColor);if(fill)rectangles.push({left:r.left,top:r.top+(r.height-24)/2,width:5,height:24,fill})}
  return {background:color(getComputedStyle(root).backgroundColor),cover,section,focus,rectangles,texts,images,tables,formula};
}

const browser=await chromium.launch({headless:true});
try{
  const context=await browser.newContext({viewport:{width:1280,height:720},deviceScaleFactor:2,reducedMotion:'reduce'});
  const page=await context.newPage();
  for(let n=1;n<=Math.min(parsed.slides.length,limit);n++){
    const captureUrl=new URL(base);
    captureUrl.searchParams.set('export-slide',String(n));
    captureUrl.hash=`/${n}`;
    await page.goto(captureUrl.href,{waitUntil:'networkidle'});
    const root=page.locator(`.slidev-page[data-slidev-no="${n}"] .slidev-layout:visible`).first();
    await root.waitFor();
    await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))});
    await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
    const data=await root.evaluate(extract);
    const slide=deck.slides.add();slide.background.fill=data.background;
    if(data.cover||data.section){
      // Decorative template background only, never a screenshot of the slide.
      let svg=await fs.readFile('public/cover-wave-light.svg','utf8');
      svg=svg.replace(/(<svg[^>]*>)/,'$1<g opacity="'+(data.cover?'.50':'.2')+'">').replace('</svg>','</g></svg>');
      slide.images.add({blob:new TextEncoder().encode(svg),contentType:'image/svg+xml',alt:'공간 파동 배경',position:data.cover?{left:590,top:352,width:760,height:350}:{left:760,top:100,width:820,height:360},fit:'contain'});
    }
    for(const r of data.rectangles)slide.shapes.add({geometry:'rect',position:r,fill:r.fill,line:{fill:'none',width:0}});
    for(const im of data.images){
      if(!im.src)continue;
      const u=new URL(im.src);let rel=decodeURIComponent(u.pathname),bytes;
      // LibreOffice misreads the nested SVG clip/use structure in this figure.
      // This PNG is a Chromium rendering of the exact original SVG, not a redrawn chart.
      if(rel==='/research/p1-gram-doa.svg')rel='/research/p1-gram-doa-compat.png';
      // Lecture diagrams contain SVG glyph paths and clipping. Use the identical
      // 2x plot render for consistent PowerPoint/LibreOffice display; PDF keeps SVG.
      if(rel.startsWith('/diagrams/')&&rel.endsWith('.svg')) {
        const png=rel.replace(/\.svg$/,'.png');
        if(await fs.stat(path.join('public',png)).then(()=>true,()=>false))rel=png;
      }
      if(u.protocol==='data:')bytes=Buffer.from(u.href.split(',')[1],'base64');else bytes=await fs.readFile(path.join('public',rel));
      const ext=rel.split('.').pop().toLowerCase();
      const contentType=ext==='svg'?'image/svg+xml':ext==='jpg'||ext==='jpeg'?'image/jpeg':ext==='webp'?'image/webp':'image/png';
      const ratio=im.naturalWidth/im.naturalHeight;
      let w=im.width,h=im.height;if(Number.isFinite(ratio)){if(w/h>ratio)w=h*ratio;else h=w/ratio}
      slide.images.add({blob:bytes,contentType,alt:im.alt,position:{left:im.left+(im.width-w)/2,top:im.top+(im.height-h)/2,width:w,height:h},fit:'contain'});
    }
    for(const t of data.tables){
      const table=slide.tables.add({rows:t.rows.length,columns:t.rows[0].cells.length,left:t.left,top:t.top,width:t.width,height:t.rows.reduce((s,r)=>s+r.height,0),columnWidths:t.rows[0].cells.map(c=>c.width),values:t.rows.map(r=>r.cells.map(c=>c.text))});
      table.styleOptions={headerRow:false,bandedRows:false,firstColumn:false};
      table.borders.assign({fill:'none',width:0});
      for(let r=0;r<t.rows.length;r++){
        table.rows[r].height=t.rows[r].height;
        for(let c=0;c<t.rows[r].cells.length;c++){
          const d=t.rows[r].cells[c],cell=table.getCell(r,c);
          cell.fill=d.fill||data.background;
          cell.text.style={fontSize:d.style.fontSize,typeface:'Pretendard',bold:d.style.bold,color:d.style.color,alignment:d.style.alignment,verticalAlignment:'middle',autoFit:'none',insets:d.margins};
          table.cells.block({row:r,column:c,rowCount:1,columnCount:1}).assign({margins:d.margins,anchor:'center'});
        }
      }
      // Table rules are visible native line elements; cells remain editable.
      for(const row of t.rows)for(const c of row.cells){
        for(const [top,fill] of [[c.top+c.height,c.borderBottom],[c.top,c.borderTop]])if(fill)slide.shapes.add({geometry:'line',position:{left:c.left,top,width:c.width,height:0},fill:'none',line:{fill,width:1}});
      }
    }
    // Add 2× formula PNGs after tables so opaque cell fills cannot cover them.
    for(let i=0;i<data.formula.length;i++){
      const f=data.formula[i];
      const rootBox=await root.boundingBox();const scale=rootBox.width/1280;
      const bytes=await page.screenshot({clip:{x:rootBox.x+f.left*scale,y:rootBox.y+f.top*scale,width:f.width*scale,height:f.height*scale},omitBackground:true,scale:'device'});
      slide.images.add({blob:bytes,contentType:'image/png',alt:f.text,position:f,fit:'contain'});
    }
    for(const t of data.texts){
      const sh=slide.shapes.add({geometry:'textbox',name:`text-${n}-${slide.shapes.items.length}`,position:{left:t.left,top:t.top,width:Math.min(1280-t.left,Math.max(t.width+8,15)),height:t.height+4},fill:'none',line:{fill:'none',width:0}});
      sh.text=t.text;
      sh.text.style={typeface:'Pretendard',fontSize:t.style.fontSize,bold:t.style.bold,italic:t.style.italic,color:t.style.color,alignment:'left',verticalAlignment:'top',autoFit:'none',wrap:'none',insets:{left:0,right:0,top:0,bottom:0}};
      if(t.link)sh.text.get(t.text).link={uri:t.link,isExternal:true};
      t.shapeName=sh.name;
    }
    slide.speakerNotes.textFrame.setText(parsed.slides[n-1].note||'');
    audit.push({number:n,...data});
    console.log(`Native PPTX ${n}/${Math.min(parsed.slides.length,limit)}: ${data.texts.length} text runs, ${data.tables.length} tables, ${data.images.length} images, ${data.formula.length} formulas`);
  }
  await (await PresentationFile.exportPptx(deck)).save(out);
  await fs.writeFile(out+'.geometry.json',JSON.stringify(audit,null,2));
  console.log(`Saved ${out}`);
}finally{await browser.close()}
