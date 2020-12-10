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
  @apply w-full px-24 py-2 mb-0 font-semibold text-white bg-blue-500 shadow-md rounded-xl hover:bg-blue-700;
}
.btn-gray {
  @apply w-full px-24 py-2 font-semibold text-white bg-gray-300 shadow-md rounded-xl hover:bg-gray-500;
}
.input {
  @apply w-full px-3 py-2 border border-blue-100 rounded-lg appearance-none text-gray-500 focus:outline-none focus:ring focus:border-blue-300 align-middle;
}
.VuePassword__Container {
  @apply flex items-center ;
}
.topic {
  @apply mb-2 text-2xl text-gray-600
}
.small-text {
  @appl text-sm text-center text-gray-600;
}
</style>
