<template>
  <div>
    <button
      class="w-full p-2 border md:w-auto whitespace-nowrap "
      @click="showModal = true"
    >
      ตั้งค่า
    </button>
    <modal v-if="showModal">
      <div slot="header">
        แก้ไข User
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body">
        <input placeholder="ชื่อร้าน" v-model="user.fname" class="w-full p-2" />
        <input placeholder="คำอธิบาย" v-model="user.lname" class="w-full p-2" />
        <input placeholder="อีเมล" v-model="user.email" class="w-full p-2" />
        <input
          placeholder="ลิ้งรูปภาพ"
          v-model="user.password"
          class="w-full p-2"
        />
      </div>
      <div slot="footer">
        <button
          @click="edit"
          class="w-full p-3 text-lg text-center text-white transition duration-500 bg-green-500 rounded-lg hover:bg-green-600"
        >
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
    fname: String,
    lname: String,
    email: String
  },
  data() {
    return {
      showModal: false,
      user: { fname: '', lname: '', email: '', password: '' }
    }
  },
  created() {
    this.user.fname = this.fname
    this.user.lname = this.lname
    this.user.email = this.email
  },
  methods: {
    edit() {
      axios
        .patch('/admin/users/' + this.id, this.user)
        .then(() => {
          swal.fire('สำเร็จ', 'แก้ไขเมนูสำเร็จ!', 'success')
          this.$emit('fetch')
          this.showModal = false
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
