<template>
  <div>
    <button class="text-lg btn btn-primary" @click="showModal = true">
      เพิ่มเมนู
    </button>
    <modal v-if="showModal">
      <div slot="header">
        เพิ่มเมนู
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body" class="space-y-3">
        <input
          placeholder="ชื่อร้าน"
          v-model="menu.name"
          class="w-full input"
        />
        <input
          placeholder="คำอธิบาย"
          v-model="menu.description"
          class="w-full input"
        />
        <input
          placeholder="ราคาธรรมดา"
          v-model.number="menu.price"
          class="w-full input"
          type="number"
        />
        <input
          placeholder="ราคาพิเศษ"
          v-model.number="menu.extra_price"
          class="w-full input"
          type="number"
        />
        <input
          placeholder="ลิ้งรูปภาพ"
          v-model="menu.img"
          class="w-full input"
        />
      </div>
      <div slot="footer">
        <button @click="add" class="w-full btn btn-primary">
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
      menu: {
        name: '',
        description: '',
        price: null,
        extra_price: null,
        img: ''
      }
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
