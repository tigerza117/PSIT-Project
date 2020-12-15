<template>
  <div class="block mt-3 space-x-0 space-y-3 md:flex md:space-y-0 md:space-x-3">
    <button @click="finish" class="btn btn-primary btn-state">
      เสร็จออเดอร์
    </button>
    <button @click="next" class="btn btn-warning btn-state">
      ออเดอร์ถัดไป
    </button>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  methods: {
    finish() {
      Axios.post('/merchant/orders/finish').then(() => {})
    },
    next() {
      Axios.post('/merchant/orders/next').then(() => {})
    }
  }
}
</script>

<style lang="postcss" scoped>
.btn-state {
  @apply w-full text-xl  md:w-1/2 p-4 !important;
}
</style>
