<template>
  <div class="slidev-layout seminar seminar-section">
    <div class="seminar-section-context"><slot name="context" /></div>
    <main class="seminar-section-title"><slot /></main>
    <div class="seminar-section-bridge"><slot name="bridge" /></div>
    <footer class="seminar-source" data-source><slot name="source" /></footer>
  </div>
</template>
