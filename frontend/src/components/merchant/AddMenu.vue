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
          v-model.number="menu.price"
          class="w-full p-2"
          type="number"
        />
        <input
          placeholder="ราคาพิเศษ"
          v-model.number="menu.extra_price"
          class="w-full p-2"
          type="number"
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
import axios from 'axios'
import swal from 'sweetalert2'
export default {
  data() {
    return {
      showModal: false,
      menu: { name: '', description: '', price: 0, extra_price: 0, img: '' }
    }
  },
  methods: {
    add() {
      axios
        .put('/merchant/menus', this.menu)
        .then(() => {
          swal.fire('สำเร็จ', 'เพิ่มเมนูสำเร็จ!', 'success')
          this.$emit('fetch')
        })
        .catch(error => {
          let res = error.response
          if (res) {
            if (400 === res.status) {
              let data = res.data
              swal.fire('ไม่สำเร็จ', data.message, 'error')
            }
          }
        })
        .finally(() => (this.showModal = false))
    }
  }
}
</script>
