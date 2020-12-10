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
    <div class="container mx-auto mt-24 mb-4">
      <!--Body-->
      <div class="grid gap-4 px-4 mt-4 md:grid-cols-2 xl:grid-cols-3">
        <div
          class="relative transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-105"
        >
          <img
            class="object-cover w-full h-64 rounded-lg"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute inset-x-0 bottom-0 w-full">
            <div class="p-4 mx-2 mb-2 bg-white rounded-lg">
              <div class="text-lg font-semibold">ร้านป้าน้อย</div>
              <div class="text-sm text-gray-600">อร่อยทุกอย่าง</div>
            </div>
          </div>
        </div>
        <div
          class="relative transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-105"
        >
          <img
            class="object-cover w-full h-64 rounded-lg"
            src="https://img.taste.com.au/00ptu0Py/taste/2016/11/linguine-with-prawns-chilli-garlic-rocket-95151-1.jpeg"
          />
          <!--Card-->
          <div class="absolute inset-x-0 bottom-0 w-full">
            <div class="p-4 mx-2 mb-2 bg-white rounded-lg">
              <div class="text-lg font-semibold">ร้านน้องไทเกอร์</div>
              <div class="text-sm text-gray-600">ทำด้วยใจ ใส่ใจทุกบริการ</div>
            </div>
          </div>
        </div>
        <div
          class="relative transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-105"
        >
          <img
            class="object-cover w-full h-64 rounded-lg"
            src="https://www.lifelinescreening.com/-/media/project/life-line-screening/life-line-screening/6-health-education/articles/diet-and-nutrition/fruits-and-vegetables.jpg"
          />
          <!--Card-->
          <div class="absolute inset-x-0 bottom-0 w-full">
            <div class="p-4 mx-2 mb-2 bg-white rounded-lg">
              <div class="text-lg font-semibold">ร้านน้อนมิ้ง</div>
              <div class="text-sm text-gray-600">น่ารักมาก</div>
            </div>
          </div>
        </div>
        <div
          class="relative transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-105"
        >
          <img
            class="object-cover w-full h-64 rounded-lg"
            src="https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/chilli-prawn-linguine-4e6a5cd0.jpg"
          />
          <!--Card-->
          <div class="absolute inset-x-0 bottom-0 w-full">
            <div class="p-4 mx-2 mb-2 bg-white rounded-lg">
              <div class="text-lg font-semibold">ร้านมุกมาก</div>
              <div class="text-sm text-gray-600">ดุที่สุดอร่อยมากๆ</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
