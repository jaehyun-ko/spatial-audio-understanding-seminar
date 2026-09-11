import { chromium } from 'playwright-chromium';
import {mkdir,writeFile} from 'node:fs/promises';
const out='tmp/intro-sequence/review-qa';await mkdir(out,{recursive:true});
const browser=await chromium.launch({headless:true});
try{
 const page=await browser.newPage({viewport:{width:1312,height:836},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto('http://localhost:3037/animations/intro-sequence/review.html',{waitUntil:'networkidle'});
 await page.waitForFunction(()=>window.introReady===true);
 await page.evaluate(async()=>{await Promise.all([...document.images].map(x=>x.decode()));document.querySelector('video').playbackRate=4});
 await page.click('#play');await page.waitForFunction(()=>document.querySelector('video').paused&&document.querySelector('video').currentTime>8,null,{timeout:15000});
 const firstStop=await page.evaluate(()=>({current:window.introCurrent,time:document.querySelector('video').currentTime,end:window.introSlides[0].end}));
 if(firstStop.current!==0||Math.abs(firstStop.time-firstStop.end)>.2)throw Error('Chapter stop failed');
 await page.click('#next');await page.waitForFunction(()=>window.introCurrent===1);await page.waitForTimeout(150);await page.click('#play');
 await page.click('#all');await page.waitForFunction(()=>window.introCurrent===5&&document.querySelector('video').ended,null,{timeout:25000});
 const fullStop=await page.evaluate(()=>({current:window.introCurrent,time:document.querySelector('video').currentTime,ended:document.querySelector('video').ended}));
 const bounds=[];
 for(let i=0;i<6;i++){
  await page.evaluate(i=>{document.querySelector('video').hidden=true;document.querySelectorAll('.frame').forEach((f,j)=>f.classList.toggle('active',i===j));},i);
  const frame=page.locator('.frame.active');
  bounds.push(await frame.evaluate(root=>{const a=root.getBoundingClientRect();return [...root.querySelectorAll('h1,.takeaway,.source')].map(x=>{const b=x.getBoundingClientRect();return {text:x.textContent,overflow:b.left<a.left||b.right>a.right+1||b.bottom>a.bottom+1,scrollOverflow:x.scrollHeight>x.clientHeight+1}})}));
  await frame.screenshot({path:`${out}/slide-${String(i+2).padStart(2,'0')}.png`});
 }
 await page.pdf({path:'output/intro-sequence/intro-02-07.pdf',preferCSSPageSize:true,printBackground:true});
 if(errors.length||bounds.flat().some(x=>x.overflow||x.scrollOverflow))throw Error(JSON.stringify({errors,bounds}));
 const report={sections:6,firstStop,fullStop,errors,bounds};await writeFile(out+'/report.json',JSON.stringify(report,null,2));console.log('Preview playback, chapter stops, 6 slide layouts and PDF export passed.');
}finally{await browser.close()}
