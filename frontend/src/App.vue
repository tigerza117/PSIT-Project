<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {}
}
</script>

<style lang="postcss">
.btn {
  @apply inline-block font-bold rounded-lg shadow-sm px-6 py-2 w-full;
}
.btn-blue {
  @apply bg-blue-500 text-white;
}
.input {
  @apply w-full px-3 py-2 mb-3 border border-blue-100 rounded-lg appearance-none text-gray-500;
}
</style>
