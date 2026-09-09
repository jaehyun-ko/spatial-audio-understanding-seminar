<template>
  <div
    class="global-page-number"
    :class="{ 'is-cover': $slidev.nav.currentPage === 1 }"
  >
    {{ $slidev.nav.currentPage }}
  </div>
</template>
