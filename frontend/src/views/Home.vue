<template>
  <div>
    <div class="flex justify-center mb-16">
      <img class="h-64 justify-self-center" src="../assets/food.svg" />
    </div>
    <div class="grid gap-4 mt-4 md:grid-cols-2 xl:grid-cols-3">
      <Shop
        v-for="shop in shops"
        :key="shop.id"
        :id="shop.id"
        :name="shop.name"
        :description="shop.description"
        :img="shop.img"
      />
    </div>
  </div>
</template>

<script>
import Shop from '../components/home/Shop.vue'
import axios from 'axios'
export default {
  components: {
    Shop
  },
  mounted() {
    axios.get('shops').then(response => (this.shops = response.data))
  },
  data() {
    return {
      shops: []
    }
  }
}
</script>

<style scoped lang="postcss"></style>
