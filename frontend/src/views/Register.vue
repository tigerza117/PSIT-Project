<template>
  <div class="max-w-md mx-auto mt-24 mb-4 shadow-2xl rounded-2xl">
    <!--Body-->
    <figure class="p-5 md:bg-white-100 rounded-xl">
      <p class="text-left mb-0.5 mt-5 ml-1 font-bold">Sign Up</p>
      <!--        <img
          class="w-16 h-16 mx-auto"
          src="logo_green.png"
          alt=""
          width="384"
          height="512"
        />-->
      <div class="pt-6 space-y-4 text-center">
        <div class="relative flex flex-wrap items-stretch w-full mb-3">
          <span
            class="absolute z-10 items-center justify-center w-8 h-full py-3 pl-3 text-base font-normal leading-snug text-center text-gray-400 bg-transparent rounded"
          >
            <i class="fas fa-lock"></i>
          </span>
          <input
            type="text"
            placeholder="Full name"
            class="relative w-full px-3 py-3 pl-10 text-sm text-gray-700 placeholder-gray-400 bg-white border outline-none rounded-xl focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="relative flex flex-wrap items-stretch w-full mb-3">
          <span
            class="absolute z-10 items-center justify-center w-8 h-full py-3 pl-3 text-base font-normal leading-snug text-center text-gray-400 bg-transparent rounded-xl"
          >
            <i class="fas fa-lock"></i>
          </span>
          <input
            type="text"
            placeholder="Email"
            class="relative w-full px-3 py-3 pl-10 text-sm text-gray-700 placeholder-gray-400 bg-white border outline-none rounded-xl focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="relative flex flex-wrap items-stretch w-full mb-3">
          <span
            class="absolute z-10 items-center justify-center w-8 h-full py-3 pl-3 text-base font-normal leading-snug text-center text-gray-400 bg-transparent rounded-xl"
          >
            <i class="fas fa-lock"></i>
          </span>
          <input
            type="text"
            placeholder="Password"
            class="relative w-full px-3 py-3 pl-10 text-sm text-gray-700 placeholder-gray-400 bg-white border outline-none rounded-xl focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="relative flex flex-wrap items-stretch w-full mb-3">
          <span
            class="absolute z-10 items-center justify-center w-8 h-full py-3 pl-3 text-base font-normal leading-snug text-center text-gray-400 bg-transparent rounded-xl"
          >
            <i class="fas fa-lock"></i>
          </span>
          <input
            type="text"
            placeholder="Confirm password"
            class="relative w-full px-3 py-3 pl-10 text-sm text-gray-700 placeholder-gray-400 bg-white border outline-none rounded-xl focus:outline-none focus:shadow-outline"
          />
        </div>

        <button
          class="w-full px-24 py-2 mb-0 font-semibold text-white bg-blue-500 shadow-md rounded-xl hover:bg-blue-700"
        >
          Sign in
        </button>
        <p class="mt-1 text-lg font-light">or sign in with</p>
        <button
          class="w-full px-24 py-2 font-semibold text-white bg-gray-300 shadow-md rounded-xl hover:bg-gray-500"
        >
          GOOGLE
        </button>
        <p class="text-lg font-light">
          Already member? <a href="#" class="hover:text-blue">sign in</a>
        </p>
      </div>
    </figure>
  </div>
</template>
