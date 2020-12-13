<template>
  <div class="relative">
    <div class="fixed inset-x-0 bottom-0 z-20 w-full bg-white border-t">
      <div class="p-4">
        <div class="w-64 mx-auto btn-order" @click="goOrder">
          ดูออเดอร์ของคุณ
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: Number
  },
  methods: {
    goOrder() {
      this.$router.push('/order/' + this.id)
    }
  }
}
</script>

<style lang="postcss" scoped>
.btn-order {
  @apply p-2 max-w-xl w-full text-lg text-center text-white bg-green-500 transition duration-500 rounded-lg hover:bg-green-600;
}
</style>
