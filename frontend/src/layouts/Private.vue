<template>
  <div>
    <div class="nav-page">
      <!--Logo-->
      <div class="text-4xl font-bold text-white" @click="home">LME</div>
      <!--menu-->
      <div>
        <ul class="flex space-x-4">
          <li>
            <button v-if="backend" class="btn-nav" @click="admin">
              ระบบหลังบ้าน
            </button>
          </li>
          <li>
            <button class="btn-nav" @click="logout">
              Logout
            </button>
          </li>
        </ul>
      </div>
    </div>
    <div class="max-w-4xl px-4 mx-auto mt-24 mb-8">
      <!--Body-->
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    backend() {
      let user = JSON.parse(localStorage.getItem('user'))
      if (user) {
        console.log(user)
        return user.role == 'admin'
      }
      return false
    }
  },
  methods: {
    home() {
      if (this.$route.path != '/') {
        this.$router.push('/')
      }
    },
    logout() {
      this.$router.push('/logout')
    },
    admin() {
      this.$router.push('/admin')
    }
  }
}
</script>
