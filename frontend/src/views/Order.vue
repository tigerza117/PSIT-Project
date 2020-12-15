<template>
  <div>
    <div v-if="!shop"></div>
    <div v-else>
      <div class="my-6 text-4xl font-bold">
        {{ shop.name
        }}<span class="float-right"
          ><button
            class="p-2 px-4 text-xl text-center text-gray-700 transition duration-500 border rounded"
            v-on:click="goShop"
          >
            กลับไปร้าน
          </button></span
        >
      </div>

      <div class="flex items-center border rounded">
        <div class="w-full">
          <div class="flex justify-center">
            <lottie-animation
              class="-mr-16"
              :path="animation"
              :loop="true"
              :autoPlay="true"
              :speed="1"
              :height="300"
            ></lottie-animation>
          </div>
          <div class="py-10 text-center">
            <div class="text-4xl font-bold">
              <span v-if="order.status == 'finished'" class="text-green-500"
                >เสร็จแล้ว!
                <div class="text-base font-normal text-gray-700">
                  ไปรับออเดอร์ที่คุณสั่งไว้ได้เลยที่ร้าน
                </div></span
              >
              <span v-else-if="shop.queue == 'no queue'">ยังไม่ทำออเดอร์</span>
              <span v-else>ออเดอร์คิวที่ {{ shop.queue }}</span>
            </div>
            <div v-if="shop.waiting > 0" class="mt-2 text-gray-500">
              เหลืออีก {{ shop.waiting }} คิว
            </div>
          </div>
        </div>
      </div>

      <div v-if="order" class="mt-2">
        <div class="p-4 border rounded">
          <div class="text-xl">
            <h2>คิว : {{ order.queue }}</h2>
            <h3>สถานะ : {{ status() }}</h3>
            <p class="break-words">โน๊ต : {{ order.note }}</p>
          </div>
          <hr class="mt-3" />
          <div>
            <div
              class="w-full mt-3 text-lg"
              v-for="menu in order.menus"
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
                  order.menus.reduce(
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
        <button
          v-if="order.status == 'ordering'"
          class="w-full p-3 mt-2 text-lg text-white bg-red-500 rounded"
          @click="delOrder"
        >
          ยกเลิกออเดอร์
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import LottieAnimation from 'lottie-vuejs/src/LottieAnimation.vue'
import axios from 'axios'

const setIntervalAsync = (fn, ms) => {
  fn().then(() => {
    setTimeout(() => setIntervalAsync(fn, ms), ms)
  })
}

const stateAnimation = sta => {
  switch (sta) {
    case 'waiting':
      return 'cooking3'
    case 'finished':
      return 'done'
    default:
      return 'cooking'
  }
}

export default {
  components: {
    LottieAnimation
  },
  data() {
    return {
      animation: 'ok.json',
      order: null,
      interval: null,
      interval_shop: null,
      shop: null
    }
  },
  watch: {
    order: {
      handler(val) {
        if (val.status == 'cancelled') {
          this.goShop()
        }
        this.animation = stateAnimation(val.status) + '.json'
      }
    }
  },
  methods: {
    goShop() {
      this.$router.push('/shops/' + this.order.shop_id)
    },
    fetchData() {
      return axios
        .get('orders/' + this.$route.params.id)
        .then(res => (this.order = res.data.order))
    },
    fetchShop() {
      return axios
        .get('shops/' + this.order.shop_id)
        .then(res => (this.shop = res.data.shop))
    },
    status() {
      switch (this.order.status) {
        case 'waiting':
          return 'กำลังรออาหาร'
        case 'finished':
          return 'เสร็จแล้ว'
        default:
          return 'กำลังรอคิว'
      }
    },
    delOrder() {
      axios.delete('/orders/' + this.order.id).then(() => this.goShop())
    }
  },
  created() {
    this.fetchData()
      .then(() => this.fetchShop())
      .finally(() => {
        this.loading = false
        this.interval = setIntervalAsync(this.fetchData, 2000)
        this.interval_shop = setIntervalAsync(this.fetchShop, 2000)
      })
  },
  beforeDestroy() {
    clearTimeout(this.interval)
    clearTimeout(this.interval_shop)
  }
}
</script>

<style scoped lang="postcss">
.name-menu {
  @apply p-2 mx-2 mt-2 bg-white rounded;
}
</style>
