<template>
  <div class="my-3">
    <button
      v-if="open"
      @click="clickClose"
      class="w-full p-4 text-2xl text-white bg-red-500"
    >
      ปิดร้าน
    </button>
    <button
      v-else
      @click="clickOpen"
      class="w-full p-4 text-2xl text-white bg-green-500"
    >
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
