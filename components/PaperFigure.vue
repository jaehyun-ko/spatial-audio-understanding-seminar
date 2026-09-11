<script setup lang="ts">
defineProps<{ src: string; alt: string; caption?: string }>()
</script>
<template>
  <figure class="seminar-figure">
    <div class="seminar-figure-art"><img :src="src" :alt="alt" /></div>
    <figcaption v-if="caption || $slots.caption"><slot name="caption">{{ caption }}</slot></figcaption>
  </figure>
</template>
