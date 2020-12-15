<template>
  <div>
    <button class="w-full btn btn-primary md:w-auto" @click="showModal = true">
      เพิ่มร้านค้า
    </button>
    <modal v-if="showModal">
      <div slot="header">
        เพิ่มร้านค้า
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body" class="space-y-3">
        <input placeholder="ชื่อร้าน" v-model="shop.name" class="w-full input" />
        <input
          placeholder="คำอธิบาย"
          v-model="shop.description"
          class="w-full input"
        />
        <input placeholder="อีเมล" v-model="shop.email" class="w-full input" />
        <input placeholder="ลิ้งรูปภาพ" v-model="shop.img" class="w-full input" />
      </div>
      <div slot="footer">
        <button
          @click="add"
          class="w-full btn btn-primary"
        >
          เพิ่มร้านค้า
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
      shop: { name: '', description: '', email: '', img: '' }
    }
  },
  methods: {
    add() {
      axios
        .put('/admin/shops', this.shop)
        .then(() => {
          swal.fire('สำเร็จ', 'เพิ่มร้านสำเร็จ!', 'success')
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
