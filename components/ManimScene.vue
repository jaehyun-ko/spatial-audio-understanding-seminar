<script setup lang="ts">
import { usePreferredReducedMotion } from '@vueuse/core'
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  src: string
  webm?: string
  poster: string
  printPoster?: string
  description: string
  controls?: boolean
}>(), {
  controls: false,
})

const reducedMotion = usePreferredReducedMotion()
const autoplay = computed(() => reducedMotion.value !== 'reduce')
const screenPoster = computed(() => autoplay.value ? props.poster : (props.printPoster ?? props.poster))
const printPoster = computed(() => props.printPoster ?? props.poster)
</script>

<template>
  <figure class="seminar-manim">
    <SlidevVideo
      class="seminar-manim-video"
      :autoplay="autoplay"
      autoreset="slide"
      :poster="screenPoster"
      :print-poster="printPoster"
      :controls="props.controls"
      :aria-label="props.description"
      muted
      playsinline
      preload="metadata"
    >
      <source v-if="props.webm" :src="props.webm" type="video/webm">
      <source :src="props.src" type="video/mp4">
    </SlidevVideo>
  </figure>
</template>
