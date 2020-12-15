<template>
  <div class="my-3">
    <button v-if="open" @click="clickClose" class="btn btn-state btn-error">
      ปิดร้าน
    </button>
    <button v-else @click="clickOpen" class="btn btn-state btn-primary">
      เปิดร้าน
    </button>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  props: {
    open: Boolean
  },
  methods: {
    clickClose() {
      Axios.post('/merchant/state/close').then(() => {})
    },
    clickOpen() {
      Axios.post('/merchant/state/open').then(() => {})
    }
  }
}
</script>

<style lang="postcss" scoped>
.btn-state {
  @apply w-full text-xl p-4 !important;
}
</style>
