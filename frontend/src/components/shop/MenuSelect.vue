<template>
  <div>
    <modal>
      <div slot="header">
        เลือกอาหาร
        <span class="float-right cursor-pointer" @click="$emit('close')"
          >X</span
        >
      </div>
      <div slot="body" class="space-y-2">
        <div>
          <img class="object-cover w-full h-48 rounded" :src="img" />
        </div>
        <div class="text-lg font-bold">
          {{ name }}
        </div>
        <p class="text-sm text-gray-600">
          {{ description }}
        </p>
        <div>
          <select
            class="w-full p-2 border rounded outline-none"
            @change="onChange($event)"
          >
            <option value="normal">ธรรมดา - {{ price }} บาท</option>
            <option value="extra">พิเศษ - {{ extra_price }} บาท</option>
          </select>
        </div>
        <div class="w-full space-x-3 text-center">
          <button
            class="btn btn-outline btn-small"
            @click="total = total > 1 ? total - 1 : 1"
          >
            -
          </button>
          <span>{{ total }}</span>
          <button class=" btn btn-outline btn-small" @click="total += 1">
            +
          </button>
        </div>
      </div>
      <div slot="footer">
        <button
          class="w-full btn btn-primary"
          @click="$emit('selected', selected)"
        >
          เลือก
        </button>
      </div>
    </modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      is_extra: false,
      total: 1
    }
  },
  props: {
    id: Number,
    name: String,
    img: String,
    price: Number,
    extra_price: Number,
    description: String,
    category: String,
    category_id: Number
  },
  computed: {
    selected() {
      return { ...this.$props, is_extra: this.is_extra, total: this.total }
    }
  },
  methods: {
    onChange(event) {
      this.is_extra = event.target.value == 'extra'
    }
  }
}
</script>

<style lang="postcss" scoped>
.btn-count {
  @apply p-2 px-4 border rounded;
}
</style>

<style scoped>
select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  text-align: center;
  text-align-last: center;
  text-align: -moz-center;
  text-align: -webkit-center;
}
</style>
