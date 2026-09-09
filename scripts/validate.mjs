import fs from 'node:fs'
import path from 'node:path'

const root = path.resolve(new URL('..', import.meta.url).pathname)
const slidesPath = path.join(root, 'slides.md')
const text = fs.readFileSync(slidesPath, 'utf8')
const errors = []

if (!text.startsWith('---\n')) errors.push('slides.md must start with YAML frontmatter')
if (!/^---\n[\s\S]*?\n---\n/.test(text)) errors.push('frontmatter is not closed')

const slides = text.split(/\n---\n(?=(?:layout:|class:|#|<))/g)
if (slides.length < 28) errors.push(`expected at least 28 slides, found ${slides.length}`)
if (slides.length > 44) errors.push(`expected at most 44 slides, found ${slides.length}`)

const fences = [...text.matchAll(/```/g)].length
if (fences % 2 !== 0) errors.push(`unbalanced fenced code blocks: ${fences}`)

const imageRefs = [...text.matchAll(/src="\/(.*?)"/g)].map(m => m[1])
for (const rel of imageRefs) {
  const p = path.join(root, 'public', rel)
  if (!fs.existsSync(p)) errors.push(`missing public asset: ${rel}`)
}

const requiredPapers = [
  'IPDnet', 'Neural-SRP', 'AGG-RL', 'MC-SimCLR', 'CCSR', 'SFD', 'GRAM',
  'BAT', 'DSpAST', 'PhaseCoder', 'OWL', 'ST-AudioLM', 'Spatial-Omni', 'SARL', 'BMLD'
]
for (const paper of requiredPapers) {
  if (!text.includes(paper)) errors.push(`missing required paper: ${paper}`)
}

for (const term of ['Linear probe', 'small MLP', 'physics-aware decoder']) {
  if (!text.toLowerCase().includes(term.toLowerCase())) errors.push(`missing readout term: ${term}`)
}

if (!text.includes('입력') || !text.includes('학습') || !text.includes('출력') || !text.includes('평가')) {
  errors.push('input / learning / output / evaluation framing is incomplete')
}

if (errors.length) {
  console.error('Validation failed:')
  for (const e of errors) console.error(`- ${e}`)
  process.exit(1)
}

console.log(`OK: ${slides.length} slide chunks, ${imageRefs.length} image refs, ${requiredPapers.length} required papers`)
