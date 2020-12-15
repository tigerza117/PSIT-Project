<template>
  <div>
    <div class="flex space-x-2 border rounded">
      <div class="w-1/4 h-16 lg:h-28">
        <img class="object-cover w-full h-full rounded-l-lg" :src="img" />
      </div>
      <!--Card-->
      <div class="relative w-3/4 p-2 pr-10">
        <div class="text-sm font-bold lg:text-xl">
          {{ name }}
          <span class="text-xs font-normal">
            <span v-if="is_extra">พิเศษ</span>
            <span v-else>ธรรมดา</span>
          </span>
        </div>
        <p class="overflow-hidden text-xs text-gray-600 lg:text-sm">
          {{ description }}
        </p>
        <div
          class="absolute inset-y-0 right-0 flex items-center justify-center pr-4 my-auto space-x-2 text-center"
        >
          <button class="btn btn-outline btn-small" @click="$emit('decrease')">
            -
          </button>
          <span>{{ total }}</span>
          <button class="btn btn-outline btn-small" @click="$emit('increase')">
            +
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    name: String,
    img: String,
    price: Number,
    extra_price: Number,
    description: String,
    category: String,
    category_id: Number,
    total: Number,
    is_extra: Boolean
  }
}
</script>
