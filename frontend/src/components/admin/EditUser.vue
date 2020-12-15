<template>
  <div>
    <button
      class="w-full btn btn-outline whitespace-nowrap "
      @click="showModal = true"
    >
      ตั้งค่า
    </button>
    <modal v-if="showModal">
      <div slot="header">
        แก้ไขบัญชีผู้ใช้
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body" class="space-y-3">
        <input
          placeholder="ชื่อจริง"
          v-model="user.fname"
          class="w-full input"
        />
        <input
          placeholder="นามสกุล"
          v-model="user.lname"
          class="w-full input"
        />
        <input placeholder="อีเมล" v-model="user.email" class="w-full input" />
        <input
          placeholder="รหัสผ่าน"
          v-model="user.password"
          class="w-full input"
          type="password"
        />
      </div>
      <div slot="footer">
        <button @click="edit" class="w-full btn btn-primary">
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
          swal.fire('สำเร็จ', 'แก้ไขบัญชีผู้ใช้สำเร็จ!', 'success')
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
