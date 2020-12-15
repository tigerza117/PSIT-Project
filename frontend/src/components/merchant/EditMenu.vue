<template>
  <div>
    <button class="w-full p-2 border md:w-auto" @click="showModal = true">
      แก้ไข
    </button>
    <modal v-if="showModal">
      <div slot="header">
        แก้ไขเมนู
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
        />
        <input
          placeholder="ราคาพิเศษ"
          v-model.number="menu.extra_price"
          class="w-full p-2"
        />
        <input placeholder="ลิ้งรูปภาพ" v-model="menu.img" class="w-full p-2" />
      </div>
      <div slot="footer">
        <button
          @click="edit"
          class="w-full p-3 text-lg text-center text-white transition duration-500 bg-green-500 rounded-lg hover:bg-green-600"
        >
          แก้ไข
        </button>
      </div>
    </modal>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert2'
export default {
  props: {
    id: Number,
    name: String,
    description: String,
    price: Number,
    extra_price: Number,
    img: String
  },
  data() {
    return {
      showModal: false,
      menu: { name: '', description: '', price: 0, extra_price: 0, img: '' }
    }
  },
  created() {
    this.menu.name = this.name
    this.menu.description = this.description
    this.menu.price = this.price
    this.menu.extra_price = this.extra_price
    this.menu.img = this.img
  },
  methods: {
    edit() {
      axios
        .patch('/merchant/menus/' + this.id, this.menu)
        .then(() => {
          swal.fire('สำเร็จ', 'แก้ไขเมนูสำเร็จ!', 'success')
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
