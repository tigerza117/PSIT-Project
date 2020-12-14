<template>
  <div>
    <button class="p-2 m-2 border" @click="showModal = true">ตั้งค่า</button>
    <modal v-if="showModal">
      <div slot="header">
        ตั้งค่าร้านค้า
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
        <input placeholder="ลิ้งรูปภาพ" v-model="shop.img" class="w-full p-2" />
      </div>
      <div slot="footer">
        <button
          @click="add"
          class="w-full p-3 text-lg text-center text-white transition duration-500 bg-green-500 rounded-lg hover:bg-green-600"
        >
          ตั้งค่า
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
    name: String,
    description: String,
    img: String
  },
  data() {
    return {
      showModal: false,
      shop: { name: '', description: '', img: '' }
    }
  },
  created() {
    this.shop.name = this.name
    this.shop.description = this.description
    this.shop.img = this.img
  },
  methods: {
    add() {
      axios
        .patch('/merchant/shop', this.shop)
        .then(
          () => swal.fire('สำเร็จ', 'แก้ไขร้านค้า!', 'success'),
          (this.showModal = false)
        )
        .catch(error => {
          let res = error.response
          if (res) {
            if (400 === res.status) {
              let data = res.data
              swal.fire('ไม่สำเร็จ', data.message, 'error')
            }
          }
        })
    }
  }
}
</script>
