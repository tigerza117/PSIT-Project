<template>
  <div>
    <div v-if="!shop"></div>
    <div v-else>
      <div>
        <div class="items-center my-6 text-2xl font-bold md:text-4xl">
          จัดการร้านค้า
          <span class="float-right"
            ><button class="text-base btn btn-outline" v-on:click="goShop">
              กลับไปร้าน
            </button></span
          >
        </div>
      </div>

      <set-state-shop :open="shop.open" @fetch="fetchMenus" />

      <div class="items-center block border rounded">
        <div class="w-full">
          <div class="flex justify-center">
            <lottie-animation
              class="-mr-16"
              path="merchant.json"
              :loop="true"
              :autoPlay="true"
              :speed="1"
              :height="300"
            ></lottie-animation>
          </div>
          <div class="pb-10 text-center">
            <div class="text-4xl font-bold">
              <span v-if="shop.queue == 'no queue'">กำลังรอออเดอร์</span>
              <span v-else>ออเดอร์คิวที่ {{ shop.queue }}</span>
            </div>
            <div v-if="shop.waiting > 0" class="mt-2 text-gray-500">
              เหลืออีก {{ shop.waiting }} คิว
            </div>
          </div>
        </div>
        <button
          v-if="shop.queue == 'no queue' && shop.waiting > 0"
          @click="nextOrder"
          class="w-full p-4 text-lg rounded-b btn-none btn-primary"
        >
          รับออเดอร์
        </button>
      </div>

      <div v-if="shop.order" class="mt-2">
        <div class="p-4 border rounded">
          <div class="text-xl">
            <h3>โน๊ต : {{ shop.order.note }}</h3>
          </div>
          <hr class="mt-3" />
          <div>
            <div
              class="w-full mt-3 text-lg"
              v-for="menu in shop.order.menus"
              :key="menu.id"
            >
              {{ menu.name }} x{{ menu.total }}
              <div class="float-right">
                {{ (menu.extra ? menu.extra_price : menu.price) * menu.total }}
                บาท
              </div>
            </div>
            <hr class="mt-3" />
            <div class="w-full mt-3 text-lg ">
              รวม
              <div class="float-right">
                {{
                  shop.order.menus.reduce(
                    (a, b) =>
                      +a + +(b.extra ? b.extra_price : b.price) * b.total,
                    0
                  )
                }}
                บาท
              </div>
            </div>
          </div>
        </div>

        <set-state-order />
      </div>

      <div class="flex my-6 text-2xl font-bold">
        จัดการเมนู <add-menu class="ml-3" />
      </div>
      <div class="space-y-3 ">
        <div
          v-for="menu in menus"
          :key="menu.id"
          class="border rounded md:flex"
        >
          <div>
            <img
              :src="menu.img"
              class="object-cover w-full h-48 rounded md:w-96"
            />
          </div>
          <div
            class="relative w-full p-2 overflow-hidden text-sm truncate pb-14 overflow-ellipsis"
          >
            <div class="text-xl font-semibold">{{ menu.name }}</div>
            <div class="text-gray-500 ">{{ menu.description }}</div>
            <div class="absolute inset-x-0 bottom-0 p-2 text-lg">
              <span
                >ธรรมดา: {{ menu.price }} บาท พิเศษ:
                {{ menu.extra_price }} บาท</span
              >
            </div>
          </div>
          <edit-menu class="p-2" v-bind="menu" @fetch="fetchMenus" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LottieAnimation from 'lottie-vuejs/src/LottieAnimation.vue'
import axios from 'axios'
import SetStateOrder from '../components/merchant/SetStateOrder.vue'
import SetStateShop from '../components/merchant/SetStateShop.vue'
import EditMenu from '../components/merchant/EditMenu.vue'
import AddMenu from '../components/merchant/AddMenu.vue'
const setIntervalAsync = (fn, ms) => {
  fn().then(() => {
    setTimeout(() => setIntervalAsync(fn, ms), ms)
  })
}
export default {
  components: {
    LottieAnimation,
    SetStateOrder,
    SetStateShop,
    EditMenu,
    AddMenu
  },
  data() {
    return {
      shop: null,
      menus: [],
      interval: null
    }
  },
  created() {
    this.fetchMenus()
    this.interval = setIntervalAsync(this.fetchShop, 2000)
  },
  beforeDestroy() {
    clearInterval(this.interval)
  },
  methods: {
    goShop() {
      this.$router.push('/shops/' + this.shop.id)
    },
    fetchMenus() {
      axios.get('/merchant/menus').then(res => (this.menus = res.data.menus))
    },
    nextOrder() {
      axios.post('/merchant/orders/next')
    },
    fetchShop() {
      return axios
        .get('/merchant/shop')
        .then(res => (this.shop = res.data.shop))
    }
  }
}
</script>
