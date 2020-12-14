<template>
  <div>
    <div v-if="!shop"></div>
    <div v-else>
      <div class="my-6">
        <span class="mr-4 text-3xl font-bold">{{ shop.name }}</span>
        <button
          v-if="isMerchant"
          class="p-2 px-4 text-xl text-center text-gray-700 transition duration-500 border rounded-lg"
          v-on:click="goMerchant"
        >
          จัดการร้าน</button
        ><span class="float-right"
          ><button
            class="p-2 px-4 text-xl text-center text-gray-700 transition duration-500 border rounded-lg"
            v-on:click="goHome"
          >
            กลับ
          </button></span
        >
      </div>

      <div class="flex items-center border rounded-lg">
        <div class="w-full">
          <div class="flex justify-center">
            <lottie-animation
              class="-mr-16"
              :path="
                !shop.open
                  ? 'close.json'
                  : shop.waiting > 0
                  ? 'cooking.json'
                  : 'lazy_cat.json'
              "
              :loop="true"
              :autoPlay="true"
              :speed="1"
              :height="300"
            ></lottie-animation>
          </div>
          <div class="py-10 text-center">
            <div class="text-4xl font-bold">
              <span v-if="!shop.open">ร้านปิด</span>
              <span v-else-if="shop.queue == 'no queue'">ร้านนี้ไม่มีคิว</span>
              <span v-else>ออเดอร์ คิวที่ {{ shop.queue }} </span>
            </div>
            <div v-if="shop.waiting > 0" class="mt-2 text-gray-500">
              เหลืออีก {{ shop.waiting }} คิว
            </div>
          </div>
        </div>
      </div>

      <order :menus="menus" v-if="menus.length" />
      <queue v-if="shop.order" :id="shop.order.id" />

      <div v-if="shop.open">
        <div class="my-6 text-2xl font-bold">เมนูอาหาร</div>
        <div class="grid grid-cols-2 gap-4 sm:grid-cols-3">
          <menu-item
            v-for="menu in shop.menus"
            :key="menu.id"
            :name="menu.name"
            :img="menu.img"
            @click.native="selectMenu(menu)"
          />
        </div>
        <menu-select
          v-if="showSelect"
          v-bind="select"
          @close="showSelect = false"
          @selected="selectedMenu"
        />
      </div>
    </div>
  </div>
</template>

<script>
import LottieAnimation from 'lottie-vuejs/src/LottieAnimation.vue'
import axios from 'axios'
import MenuItem from '../components/shop/MenuItem.vue'
import Order from '../components/shop/Order.vue'
import MenuSelect from '../components/shop/MenuSelect.vue'
import Queue from '../components/shop/Queue.vue'

const setIntervalAsync = (fn, ms) => {
  fn().then(() => {
    setTimeout(() => setIntervalAsync(fn, ms), ms)
  })
}

export default {
  components: {
    LottieAnimation,
    MenuItem,
    Order,
    MenuSelect,
    Queue
  },
  data() {
    return {
      shop: null,
      select: null,
      showSelect: false,
      menus: [],
      interval: null
    }
  },
  computed: {
    isMerchant() {
      let user = JSON.parse(localStorage.getItem('user'))
      if (user) {
        return user.id == this.shop.owner_id
      }
      return false
    }
  },
  methods: {
    goHome() {
      this.$router.push('/')
    },
    goMerchant() {
      this.$router.push('/merchant')
    },
    selectMenu(menu) {
      if (!this.shop.order) {
        this.select = menu
        this.showSelect = true
      }
    },
    selectedMenu(data) {
      this.menus.push(data)
      this.showSelect = false
    },
    fetchData() {
      return axios
        .get('shops/' + this.$route.params.id)
        .then(res => (this.shop = res.data.shop))
    }
  },
  created() {
    this.fetchData().finally(() => {
      this.interval = setIntervalAsync(this.fetchData, 2000)
    })
  },
  beforeDestroy() {
    clearInterval(this.interval)
  }
}
</script>

<style scoped lang="postcss">
.name-menu {
  @apply p-2 mx-2 mt-2 bg-white rounded-lg;
}
</style>
