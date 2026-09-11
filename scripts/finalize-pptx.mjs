#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {pathToFileURL} from 'node:url';
const arg=(flag,fallback)=>{const i=process.argv.indexOf(flag);return i<0?fallback:process.argv[i+1]};
const workspaceDir=path.resolve('.');
const runtimeRoot=path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies');
process.env.RUNTIME_NODE_MODULES ||=path.join(runtimeRoot,'node/node_modules');
const skill=process.env.PRESENTATIONS_SKILL_DIR||path.join(os.homedir(),'.codex/plugins/cache/openai-primary-runtime/presentations/26.909.12148/skills/presentations');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
const candidatePath=path.resolve(arg('--candidate','tmp/finalization/candidate.pptx'));
const finalPath=path.resolve(arg('--out','output/pptx/spatial-audio-understanding.pptx'));
const geometry=JSON.parse(await fs.readFile(candidatePath+'.geometry.json','utf8'));
const tableOwners=geometry.filter(d=>d.tables.length).map(d=>d.number);
await fs.mkdir(path.dirname(finalPath),{recursive:true});
const result=await finalizePresentation({
 workspaceDir,candidatePath,finalPath,
 explicitTotalSlideCount:geometry.length,
 pythonExecutable:path.join(runtimeRoot,'python/bin/python3'),
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],
 requiredNativeTableOwnerSlides:tableOwners,
 fontPolicy:{basis:'design',families:['Pretendard']},
 verifyArtifactToolImport:true,
 receiptPath:path.resolve('tmp/finalization',path.basename(finalPath)+'.validation.json')
});
console.log(JSON.stringify({file:result.finalPath,slides:result.packageIntegrity.slide_count,integrity:result.packageIntegrity.status,layout:result.presentationLayout.findingCount,nativeTables:result.nativeTableArithmetic.native_table_count,importPassed:result.firstPartyImport.passed,receipt:result.receiptPath},null,2));
