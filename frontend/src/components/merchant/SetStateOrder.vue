<template>
  <div class="block mt-3 space-x-0 space-y-3 md:flex md:space-y-0 md:space-x-3">
    <button
      @click="finish"
      class="w-full p-4 text-2xl text-white bg-green-500 md:w-1/2"
    >
      เสร็จออเดอร์
    </button>
    <button
      @click="next"
      class="w-full p-4 text-2xl text-white bg-yellow-500 md:w-1/2"
    >
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
