<template>
  <div class="w-full max-w-md p-10 m-auto mt-24 bg-white rounded-xl">
    <p class="mb-2 text-2xl text-gray-600">Sing In</p>
    <form v-on:submit.prevent="login">
      <div class="mb-3">
        <input
          class="w-full px-3 py-2 mt-5 border border-blue-100 rounded-lg appearance-none text-grey-darker"
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
          class="w-full px-3 py-2 mb-3 border border-blue-100 rounded-lg appearance-none text-grey-darker"
          id="password"
          name="password"
          type="password"
          autocomplete="current-password"
          placeholder="Password"
          v-model="auth.password"
        />
      </div>
      <div class="flex items-center justify-between mb-4">
        <button
          class="w-full py-3 text-xs font-bold text-white bg-blue-500 rounded-lg hover:bg-blue-dark"
          type="submit"
        >
          Sign In
        </button>
      </div>
      <div class="mb-4">
        <p class="text-sm text-center text-gray-600">or sign in with</p>
      </div>
      <button
        class="w-full py-2 text-xs font-bold text-gray-600 rounded-lg bg-gray-50 hover:bg-blue-dark"
      >
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
