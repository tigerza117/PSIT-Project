<template>
  <div>
    <button
      class="w-full btn btn-outline whitespace-nowrap"
      @click="showModal = true"
    >
      ตั้งค่า
    </button>
    <modal v-if="showModal">
      <div slot="header">
        แก้ไขร้านค้า
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body" class="space-y-3">
        <input
          placeholder="ชื่อร้าน"
          v-model="shop.name"
          class="w-full input"
        />
        <input
          placeholder="คำอธิบาย"
          v-model="shop.description"
          class="w-full input"
        />
        <input placeholder="อีเมล" v-model="shop.email" class="w-full input" />
        <input
          placeholder="ลิ้งรูปภาพ"
          v-model="shop.img"
          class="w-full input"
        />
      </div>
      <div slot="footer">
        <button @click="edit" class="w-full btn btn-primary">
          แก้ไขร้านค้า
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
    owner: Object,
    name: String,
    description: String,
    email: String,
    img: String
  },
  data() {
    return {
      showModal: false,
      shop: { name: '', description: '', email: '', img: '' }
    }
  },
  created() {
    this.shop.name = this.name
    this.shop.description = this.description
    this.shop.email = this.owner.email
    this.shop.img = this.img
  },
  methods: {
    edit() {
      axios
        .patch('/admin/shops/' + this.id, this.shop)
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
