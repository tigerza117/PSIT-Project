<template>
  <div class="max-w-md mx-auto my-20 shadow-xl rounded-2xl">
    <div class="p-5 md:bg-white-100 rounded-xl">
      <p class="topic">Sign In</p>
      <form v-on:submit.prevent="login" class="pt-6 space-y-4 text-center">
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
          <button class="btn" type="submit">
            Sign In
          </button>
        </div>
        <div class="mb-4">
          <p class="text-sm text-center text-gray-600">or sign in with</p>
        </div>
        <button class="btn-gray">
          GOOGLE
        </button>
      </form>
      <div class="mt-6">
        <p class="text-sm text-center text-gray-600">
          Don't have an account yet?
          <a href="#" class="text-blue-400 underline hover:text-blue-800"
            >Sign up</a
          >
        </p>
      </div>
    </div>
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
