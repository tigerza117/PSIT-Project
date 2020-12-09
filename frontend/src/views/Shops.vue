<template>
  <div>
    {{ info }}
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      info: null
    }
  },
  mounted() {
    axios.get('shops').then(response => (this.info = response))
  }
}
</script>
