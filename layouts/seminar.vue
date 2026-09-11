<script setup lang="ts">
withDefaults(defineProps<{
  variant?: 'focus' | 'figure' | 'method' | 'result' | 'compare' | 'closing'
  chapter?: string
}>(), { variant: 'focus' })
</script>
<template>
  <div class="slidev-layout seminar" :class="`seminar--${variant}`">
    <p v-if="chapter" class="seminar-position">{{ chapter }}</p>
    <header class="seminar-header"><slot /></header>
    <main class="seminar-body">
      <div class="seminar-primary"><slot name="body" /></div>
      <aside v-if="$slots.aside" class="seminar-aside"><slot name="aside" /></aside>
    </main>
    <div class="seminar-takeaway"><slot name="takeaway" /></div>
    <footer class="seminar-source" data-source><slot name="source" /></footer>
  </div>
</template>
