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
              Sign-In
            </button>
          </li>
        </ul>
      </div>
    </div>
    <div class="max-w-4xl px-4 mx-auto mt-24 mb-4">
      <!--Body-->
      <slot />
    </div>
  </div>
</template>
