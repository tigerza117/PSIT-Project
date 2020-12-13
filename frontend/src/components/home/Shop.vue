<template>
  <div class="menu-box" v-on:click="goShop">
    <img class="object-cover w-full h-64 rounded-lg" :src="img" />
    <!--Card-->
    <div class="absolute inset-x-0 bottom-0 w-full">
      <div class="p-4 mx-2 mb-2 bg-white rounded-lg">
        <div class="text-lg font-semibold">{{ name }}</div>
        <div class="text-sm text-gray-600">{{ description }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    name: String,
    description: String,
    img: String
  },
  methods: {
    goShop() {
      this.$router.push('shops/' + this.id)
    }
  }
}
</script>
