<template>
  <div>
    <button class="p-2 m-2 border" @click="showModal = true">
      เพิ่มเมนู
    </button>
    <modal v-if="showModal">
      <div slot="header">
        เพิ่มเมนู
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body">
        <input placeholder="ชื่อร้าน" v-model="menu.name" class="w-full p-2" />
        <input
          placeholder="คำอธิบาย"
          v-model="menu.description"
          class="w-full p-2"
        />
        <input
          placeholder="ราคาธรรมดา"
          v-model="menu.price"
          class="w-full p-2"
        />
        <input
          placeholder="ราคาพิเศษ"
          v-model="menu.extra_price"
          class="w-full p-2"
        />
        <input placeholder="ลิ้งรูปภาพ" v-model="menu.img" class="w-full p-2" />
      </div>
      <div slot="footer">
        <button
          @click="add"
          class="w-full p-3 text-lg text-center text-white transition duration-500 bg-green-500 rounded-lg hover:bg-green-600"
        >
          เพิ่ม
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
      menu: { name: '', description: '', price: 0, extra_price: 0, img: '' }
    }
  },
  methods: {
    add() {
      console.log(this.menu)
    }
  }
}
</script>
