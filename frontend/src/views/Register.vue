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
            class="input"
          />
        </div>
        <div class="flex-box">
          <input
            v-model="auth.lname"
            type="text"
            placeholder="Lastname"
            class="input"
          />
        </div>
        <div class="flex-box">
          <input
            v-model="auth.email"
            type="text"
            placeholder="Email"
            class="input"
          />
        </div>
        <div class="flex-box">
          <VuePassword
            v-model="password"
            id="password"
            :strength="strength"
            type="text"
          >
            <template
              v-slot:password-input="props"
              class="control has-icons-left"
            >
              <input
                type="password"
                placeholder="Password"
                :value="props.value"
                @input="props.updatePassword"
                class="input"
              />
            </template>
          </VuePassword>
        </div>
        <div class="flex-box">
          <input
            type="text"
            placeholder="Confirm password"
            class="input"
          />
        </div>
        <button
          class="btn"
        >
          Sign in
        </button>
        <p class="text-sm text-center text-gray-600">
          or sign in with
        </p>
        <button
          class="btn-gray"
        >
          GOOGLE
        </button>
        <p class="text-sm text-center text-gray-600">
          Already member? <a href="#" class="underline text-blue-400 hover:text-blue-800">Sign in</a>
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
  components: {
    VuePassword
  },
  methods: {
    register() {
      console.log(this.auth)
      axios.put('register', this.auth).then(res => {
        let data = res.data
        if (data.success) {
          swal.fire('Register Scuess', '', 'success')
          this.$router.push('/login')
        }
      })
    }
  }
}
</script>

<style lang="postcss" scoped>
</style>
