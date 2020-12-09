<template>
  <div></div>
</template>

<script>
export default {
  mounted() {
    localStorage.removeItem('jwt')
    window.location.reload()
  }
}
</script>
