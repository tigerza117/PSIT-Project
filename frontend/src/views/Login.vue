<template>
  <div class="max-w-md p-4 mx-auto my-20">
    <div class="p-5 md:border md:rounded md:shadow-lg">
      <p class="topic">เข้าสู่ระบบ</p>
      <form v-on:submit.prevent="login" class="pt-6 space-y-4 text-center">
        <div class="mb-3">
          <input
            class="w-full input"
            id="email"
            name="email"
            type="email"
            autocomplete="email"
            placeholder="อีเมล"
            v-model="auth.email"
          />
        </div>
        <div class="mb-3">
          <input
            class="w-full input"
            id="password"
            name="password"
            type="password"
            autocomplete="current-password"
            placeholder="รหัสผ่าน"
            v-model="auth.password"
          />
        </div>
        <div class="flex items-center justify-between mb-4">
          <button class="w-full btn btn-primary" type="submit">
            เข้าสู่ระบบ
          </button>
        </div>
      </form>
      <div class="mt-6">
        <p class="text-sm text-center text-gray-600">
          คุณมีบัญชีผู้ใช้หรือยัง?
          <a
            href="/register"
            class="text-blue-400 underline hover:text-blue-800"
            >ลงทะเบียน</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert2'
export default {
  data() {
    return {
      auth: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    login() {
      axios
        .post('login', this.auth)
        .then(res => {
          let data = res.data
          if (data.access_token) {
            localStorage.setItem('jwt', data.access_token)
            let next = this.$route.query.nextUrl
              ? this.$route.query.nextUrl
              : '/'
            axios
              .get('profile')
              .then(res =>
                localStorage.setItem('user', JSON.stringify(res.data))
              )
              .then(() => this.$router.push(next))
          }
        })
        .catch(error => {
          let res = error.response
          if (res) {
            if (400 === res.status) {
              let data = res.data
              swal.fire('เข้าสู่ระบบไม่สำเร็จ', data.message, 'error')
            }
          }
        })
    }
  }
}
</script>
