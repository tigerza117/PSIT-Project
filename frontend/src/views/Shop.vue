<template>
  <div>
    <div class="nav-page">
      <!--Logo-->
      <div class="text-4xl font-bold text-white">LME</div>
      <!--menu-->
      <div>
        <ul class="flex space-x-8">
          <li>
            <button class="btn-nav">
              Logout
            </button>
          </li>
        </ul>
      </div>
    </div>
    <div class="px-4 mt-24 mb-4 md:container md:mx-auto">
      <!--Body-->
      <div class="my-6 text-4xl font-bold">ร้าน น้องเสือ</div>
      <div class="flex items-center border rounded-lg">
        <div class="w-full">
          <div class="flex justify-center">
            <lottie-animation
              class="-mr-16"
              path="cooking.json"
              :loop="true"
              :autoPlay="true"
              :speed="1"
              :height="300"
            ></lottie-animation>
          </div>
          <div class="py-10 text-center">
            <div class="text-4xl font-bold lg:text-6xl">ขณะนี้คิวที่ A07</div>
            <div class="mt-2 text-gray-500">เหลืออีก 5 คิว</div>
          </div>
        </div>
      </div>
      <div class="btn-order">
        สั่งอาหาร
      </div>
      <div class="my-6 text-2xl font-bold">เมนูอาหาร</div>
      <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div class="menu-box">
          <img
            class="img-menu"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute top-0">
            <div>
              <div class="p-2 mx-2 mt-2 bg-white rounded-lg">
                Pasta in Tomato Sauce
              </div>
            </div>
          </div>
        </div>
        <div class="menu-box">
          <img
            class="img-menu"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute top-0">
            <div>
              <div class="name-menu">
                Pasta in Tomato Sauce
              </div>
            </div>
          </div>
        </div>
        <div class="menu-box">
          <img
            class="img-menu"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute top-0">
            <div>
              <div class="name-menu">
                Pasta in Tomato Sauce
              </div>
            </div>
          </div>
        </div>
        <div class="menu-box">
          <img
            class="img-menu"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute top-0">
            <div>
              <div class="name-menu">
                Pasta in Tomato Sauce
              </div>
            </div>
          </div>
        </div>
        <div class="menu-box">
          <img
            class="img-menu"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute top-0">
            <div>
              <div class="name-menu">
                Pasta in Tomato Sauce
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LottieAnimation from 'lottie-vuejs/src/LottieAnimation.vue'
export default {
  components: {
    LottieAnimation
  }
}
</script>

<style scoped lang="postcss">
.btn-order {
  @apply p-4 mt-6 text-xl text-center text-white bg-green-500 transition duration-500 rounded-lg hover:bg-green-600;
}
.name-menu {
  @apply p-2 mx-2 mt-2 bg-white rounded-lg;
}
</style>
