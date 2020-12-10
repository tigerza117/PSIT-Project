<template>
  <div>
    <div
      class="fixed top-0 z-20 flex flex-wrap items-center w-full p-4 px-6 m-auto bg-green-500 animated place-content-between"
    >
      <!--Logo-->
      <div class="text-4xl font-bold text-white">LME</div>
      <!--menu-->
      <div>
        <ul class="flex space-x-8">
          <li>
            <button
              class="p-2 transition duration-500 bg-white rounded hover:bg-red-500"
            >
              Sign-In
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
            <lottie-player
              class="-mr-16"
              src="cooking.json"
              background="transparent"
              speed="1"
              style="height: 300px"
              loop
              autoplay
            ></lottie-player>
          </div>
          <div class="py-10 text-center">
            <div class="text-4xl font-bold lg:text-6xl">ขณะนี้คิวที่ A07</div>
            <div class="mt-2 text-gray-500">เหลืออีก 5 คิว</div>
          </div>
        </div>
      </div>
      <div
        class="p-4 mt-6 text-xl text-center text-white bg-green-500 rounded-lg"
      >
        สั่งอาหาร
      </div>
      <div class="my-6 text-2xl font-bold">เมนูอาหาร</div>
      <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div class="relative">
          <img
            class="object-cover w-full h-64 rounded-lg"
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
        <div class="relative">
          <img
            class="object-cover w-full h-64 rounded-lg"
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
        <div class="relative">
          <img
            class="object-cover w-full h-64 rounded-lg"
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
        <div class="relative">
          <img
            class="object-cover w-full h-64 rounded-lg"
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
        <div class="relative">
          <img
            class="object-cover w-full h-64 rounded-lg"
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
      </div>
    </div>
  </div>
</template>
