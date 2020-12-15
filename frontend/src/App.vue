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
