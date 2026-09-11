#!/usr/bin/env node
/** Render with an isolated font configuration; never change global font settings. */
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {spawnSync} from 'node:child_process';
const input=path.resolve(process.argv[2]||'output/pptx/spatial-audio-understanding.pptx');
const out=path.resolve(process.argv[3]||'tmp/final-pptx-qa');
await fs.mkdir(out,{recursive:true});
const xml=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
const dirs=process.platform==='darwin'?[path.join(os.homedir(),'Library/Fonts'),'/System/Library/Fonts','/System/Library/Fonts/Supplemental']:['/usr/share/fonts',path.join(os.homedir(),'.local/share/fonts')];
const fontConfig=path.join(out,'fonts.conf');
await fs.writeFile(fontConfig,`<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd"><fontconfig>${dirs.map(d=>'<dir>'+xml(d)+'</dir>').join('')}<cachedir>${xml(path.join(out,'font-cache'))}</cachedir></fontconfig>`);
const result=spawnSync('soffice',['--headless','--convert-to','pdf','--outdir',out,input],{stdio:'inherit',env:{...process.env,FONTCONFIG_FILE:fontConfig}});
if(result.status!==0)process.exit(result.status||1);
const pdf=path.join(out,path.basename(input,'.pptx')+'.pdf');
const r=spawnSync('pdftoppm',['-scale-to','1280','-png',pdf,path.join(out,'slide')],{stdio:'inherit'});
process.exitCode=r.status||0;
