<template>
  <div class="max-w-md p-4 mx-auto my-20">
    <div class="p-4 md:border md:rounded md:shadow-lg">
      <p class="topic">ลงทะเบียน</p>
      <form v-on:submit.prevent="register" class="pt-6 space-y-4 text-center">
        <div class="flex-box">
          <input
            v-model="auth.fname"
            type="text"
            placeholder="ชื่อจริง"
            class="w-full input"
          />
        </div>
        <div class="flex-box">
          <input
            v-model="auth.lname"
            type="text"
            placeholder="นามสกุล"
            class="w-full input"
          />
        </div>
        <div class="flex-box">
          <input
            v-model="auth.email"
            type="email"
            placeholder="อีเมล"
            class="w-full input"
          />
        </div>
        <div class="flex-box">
          <VuePassword v-model="password" id="password" :strength="strength">
            <template
              v-slot:password-input="props"
              class="control has-icons-left"
            >
              <input
                type="password"
                placeholder="รหัสผ่าน"
                :value="props.value"
                @input="props.updatePassword"
                class="w-full input"
              />
            </template>
          </VuePassword>
        </div>
        <div class="flex-box">
          <input
            v-model="confirm"
            type="password"
            placeholder="ยืนยันรหัสผ่าน"
            class="w-full input"
          />
        </div>
        <button
          class="w-full btn btn-primary disabled:opacity-50"
          :disabled="strength < 4"
        >
          ลงทะเบียน
        </button>
        <p class="text-sm text-center text-gray-600">
          มีบัญชีอยู่แล้ว?
          <a href="/login" class="text-blue-400 underline hover:text-blue-800"
            >เข้าสู่ระบบ</a
          >
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import VuePassword from 'vue-password'
import swal from 'sweetalert2'
import axios from 'axios'
export default {
  data() {
    return {
      auth: {
        email: '',
        password: '',
        fname: '',
        lname: ''
      },
      password: '',
      confirm: '',
      strength: 0
    }
  },
  watch: {
    password: function(val) {
      this.strength =
        /(?=.*[a-z])/.test(val) +
        /(?=.*[A-Z])/.test(val) +
        /(?=.*\d)/.test(val) +
        /(?=.*[!@#$%^&*]){8,}/.test(val)
      this.auth.password = val
    }
  },
  computed: {},
  components: {
    VuePassword
  },
  methods: {
    register() {
      if (this.password != this.confirm) {
        swal.fire('ไม่สำเร็จ', 'รหัสผ่านไม่ตรงกัน', 'error')
        this.password = ''
        this.confirm = ''
        return
      }
      axios
        .put('register', this.auth)
        .then(res => {
          let data = res.data
          if (data.success) {
            swal.fire(
              'สำเร็จ',
              'คุณได้สมัคร Let me eat เรียบร้อยแล้วสามารถ Login ได้ทันที',
              'success'
            )
            this.$router.push('/login')
          }
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
    }
  }
}
</script>

<style lang="postcss" scoped></style>
