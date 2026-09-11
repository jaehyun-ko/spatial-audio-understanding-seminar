<template>
  <div class="slidev-layout seminar seminar-cover">
    <div class="seminar-cover-identity"><slot name="identity" /></div>
    <main class="seminar-cover-title"><slot /></main>
    <div class="seminar-cover-subtitle"><slot name="subtitle" /></div>
    <footer class="seminar-source" data-source><slot name="source" /></footer>
  </div>
</template>
