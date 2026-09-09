import fs from 'node:fs'
import path from 'node:path'

const root = path.resolve(new URL('..', import.meta.url).pathname)
const text = fs.readFileSync(path.join(root, 'slides.md'), 'utf8')
const errors = []
const warnings = []

const banned = [
  '계보상의 의미',
  '새로운 전환점',
  '아직 동시에 해결되지 않은',
  '강한 방법 논문',
  'Open gap',
  '아직 아무도',
  '완전한 범용',
]
for (const phrase of banned) {
  if (text.includes(phrase)) errors.push(`banned slop phrase: ${phrase}`)
}

const slideChunks = text.split(/\n---\n(?=(?:layout:|class:|#|<))/g)
if (slideChunks.length > 38) warnings.push(`deck is long: ${slideChunks.length} slide chunks`)

for (let i = 1; i < slideChunks.length; i++) {
  const chunk = slideChunks[i]
    .replace(/^layout:[\s\S]*?\n---\n/, '')
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/[#*_`|]/g, ' ')
  const words = chunk.split(/\s+/).filter(Boolean)
  if (words.length > 125) warnings.push(`slide ${i + 1} is text-heavy: ${words.length} tokens`)
}

const factualTemplate = ['입력', '학습', '출력', '평가']
const paperNames = ['IPDnet', 'AGG-RL', 'MC-SimCLR', 'CCSR', 'SFD', 'GRAM', 'BAT', 'PhaseCoder', 'SARL', 'BMLD']
for (const paper of paperNames) {
  const idx = slideChunks.findIndex(s => s.includes(paper))
  if (idx < 0) errors.push(`missing paper: ${paper}`)
}

if (errors.length) {
  console.error('Anti-slop lint failed:')
  for (const e of errors) console.error(`- ${e}`)
  process.exit(1)
}

console.log(`Anti-slop lint OK: ${slideChunks.length} slides`)
if (warnings.length) {
  console.log('Warnings:')
  for (const w of warnings) console.log(`- ${w}`)
}
