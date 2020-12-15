<template>
  <div class="menu-box">
    <img class="img-menu" :src="img" />
    <!--Card-->
    <div class="absolute top-0">
      <div>
        <div class="p-2 mx-2 mt-2 bg-white rounded">
          <div class="text-base">
            {{ name }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    img: String,
    price: Number,
    extra_price: Number,
    description: String,
    category: String,
    category_id: Number
  }
}
</script>
