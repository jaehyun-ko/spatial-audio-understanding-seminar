<script setup lang="ts">
import { computed } from 'vue'
import katex from 'katex'
import 'katex/dist/katex.min.css'

const props = defineProps<{ tex: string }>()
const rendered = computed(() => katex.renderToString(props.tex, {
  displayMode: false,
  throwOnError: true,
  strict: 'error',
  output: 'htmlAndMathml',
}))
</script>
<template>
  <span class="seminar-math" v-html="rendered" />
</template>
