<template>
  <div>
    <button
      class="w-full p-2 text-sm border md:w-auto"
      @click="showModal = true"
    >
      เพิ่มร้านค้า
    </button>
    <modal v-if="showModal">
      <div slot="header">
        เพิ่มร้าค้า
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body">
        <input placeholder="ชื่อร้าน" v-model="shop.name" class="w-full p-2" />
        <input
          placeholder="คำอธิบาย"
          v-model="shop.description"
          class="w-full p-2"
        />
        <input placeholder="อีเมล" v-model="shop.email" class="w-full p-2" />
        <input placeholder="ลิ้งรูปภาพ" v-model="shop.img" class="w-full p-2" />
      </div>
      <div slot="footer">
        <button
          @click="add"
          class="w-full p-3 text-lg text-center text-white transition duration-500 bg-green-500 rounded-lg hover:bg-green-600"
        >
          เพิ่มร้านค้า
        </button>
      </div>
    </modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      shop: { name: '', description: '', email: '', img: '' }
    }
  },
  methods: {
    add() {
      console.log(this.shop)
    }
  }
}
</script>
