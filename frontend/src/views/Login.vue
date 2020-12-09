<template>
  <div class="w-full max-w-md p-10 m-auto mt-24 bg-white rounded-xl">
    <p class="mb-2 text-2xl text-gray-600">Sing In</p>
    <div class="mb-3">
      <input
        class="w-full px-3 py-2 mt-5 border border-blue-100 rounded-lg appearance-none text-grey-darker"
        id="Email"
        type="text"
        placeholder="Email"
      />
    </div>
    <div class="mb-3">
      <input
        class="w-full px-3 py-2 mb-3 border border-blue-100 rounded-lg appearance-none text-grey-darker"
        id="password"
        type="password"
        placeholder="Password"
      />
    </div>
    <div class="flex items-center justify-between mb-4">
      <button
        class="w-full py-3 text-xs font-bold text-white bg-blue-500 rounded-lg hover:bg-blue-dark"
        type="button"
      >
        Sign Up
      </button>
    </div>
    <div class="mb-4">
      <p class="text-sm text-center text-gray-600">or sign in with</p>
    </div>
    <button
      class="w-full py-2 text-xs font-bold text-gray-600 rounded-lg bg-gray-50 hover:bg-blue-dark"
      type="button"
    >
      GOOGLE
    </button>
  </div>
</template>
