<template>
  <div>
    <div class="nav-page">
      <!--Logo-->
      <div class="text-4xl font-bold text-white cursor-pointer" @click="home">
        LME
      </div>
      <!--menu-->
      <div>
        <ul class="flex space-x-4">
          <li>
            <button v-if="isAdmin" class="btn btn-white" @click="admin">
              ระบบหลังบ้าน
            </button>
          </li>
          <li>
            <button class="btn btn-error" @click="logout">
              ออกจากระบบ
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
    isAdmin() {
      let isAdmin = false
      let user = JSON.parse(localStorage.getItem('user'))
      if (user) {
        isAdmin = user.role == 'admin'
      }
      return !(this.$route.path == '/admin') && isAdmin
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
