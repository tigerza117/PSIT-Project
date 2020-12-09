<script>
export default {
  beforeMount() {
    localStorage.removeItem('jwt')
    window.location.href = '/login'
  }
}
</script>
