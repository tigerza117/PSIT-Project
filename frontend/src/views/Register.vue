<template>
  <div class="max-w-md mx-auto my-20 shadow-xl rounded-2xl">
    <div class="p-5 md:bg-white-100 rounded-xl">
      <p class="topic">Sign Up</p>
      <form v-on:submit.prevent="register" class="pt-6 space-y-4 text-center">
        <div class="flex-box">
          <input
            v-model="auth.fname"
            type="text"
            placeholder="Firstname"
            class="w-full input"
          />
        </div>
        <div class="flex-box">
          <input
            v-model="auth.lname"
            type="text"
            placeholder="Lastname"
            class="w-full input"
          />
        </div>
        <div class="flex-box">
          <input
            v-model="auth.email"
            type="email"
            placeholder="Email"
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
                placeholder="Password"
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
            placeholder="Confirm password"
            class="w-full input"
          />
        </div>
        <button
          class="w-full btn btn-blue disabled:opacity-50"
          :disabled="strength < 4"
        >
          Sign up
        </button>
        <p class="text-sm text-center text-gray-600">
          Already member?
          <a href="/login" class="text-blue-400 underline hover:text-blue-800"
            >Sign in</a
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
        /[a-zA-Z0-9]{8,}/.test(val) +
        /[^\p{L}\d\s@#]/u.test(val)
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
