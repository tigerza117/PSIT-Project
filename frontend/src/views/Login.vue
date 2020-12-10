<template>
  <div class="w-full max-w-md p-10 m-auto mt-24 bg-white rounded-xl">
    <p class="mb-2 text-2xl text-gray-600">Sing In</p>
    <form v-on:submit.prevent="login">
      <div class="mb-3">
        <input
          class="input"
          id="email"
          name="email"
          type="text"
          autocomplete="email"
          placeholder="Email"
          v-model="auth.email"
        />
      </div>
      <div class="mb-3">
        <input
          class="input"
          id="password"
          name="password"
          type="password"
          autocomplete="current-password"
          placeholder="Password"
          v-model="auth.password"
        />
      </div>
      <div class="flex items-center justify-between mb-4">
        <button class="btn btn-blue" type="submit">
          Sign In
        </button>
      </div>
      <div class="mb-4">
        <p class="text-sm text-center text-gray-600">or sign in with</p>
      </div>
      <button class="btn btn-blue">
        GOOGLE
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
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
      axios.post('login', this.auth).then(res => {
        let data = res.data
        if (data.access_token) {
          console.log(data.access_token)
          localStorage.setItem('jwt', data.access_token)
          let next = this.$route.query.nextUrl ? this.$route.query.nextUrl : '/'
          this.$router.push(next)
        }
      })
    }
  }
}
</script>
