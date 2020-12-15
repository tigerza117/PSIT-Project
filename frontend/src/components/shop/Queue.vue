<template>
  <div class="relative">
    <div class="fixed inset-x-0 bottom-0 z-20 w-full bg-white border-t">
      <div class="p-2">
        <div class="w-64 max-w-xl mx-auto" @click="goOrder">
          <button class="w-full btn btn-primary">
            ดูออเดอร์ของคุณ
          </button>
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
