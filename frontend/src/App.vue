<template>
  <div id="app">
    <component :is="layout">
      <router-view></router-view>
    </component>
  </div>
</template>

<script>
export default {
  computed: {
    layout() {
      let layout = this.$route.meta.layout
      return layout ? 'layout-' + layout : 'layout-default'
    }
  },
  mounted() {
    console.log()
  },
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
  @apply flex items-center;
}
.topic {
  @apply mb-2 text-2xl text-gray-500;
}
.menu-box {
  @apply relative transition duration-500 ease-in-out transform;
}
.nav-page {
  @apply fixed top-0 z-20 flex flex-wrap items-center w-full p-4 px-6 m-auto bg-green-500 place-content-between;
}
.btn-nav {
  @apply p-2 transition duration-500 bg-white rounded hover:bg-red-500;
}
.img-menu {
  @apply object-cover w-full h-64 rounded-lg;
}
</style>
