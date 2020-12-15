<template>
  <div>
    <div class="max-h-screen mb-6 overflow-y-auto">
      <div class="flex items-center">
        <div class="mr-4 text-2xl font-bold">ร้านค้า</div>
        <add-shop />
      </div>
      <hr class="my-3" />
      <div class="space-y-3 ">
        <div
          v-for="shop in shops"
          :key="shop.id"
          class="border rounded md:flex"
        >
          <div>
            <img
              :src="shop.img"
              class="object-cover w-full h-48 rounded md:w-96"
            />
          </div>
          <div
            class="relative w-full p-2 overflow-hidden text-sm truncate overflow-ellipsis"
          >
            <div class="text-xl font-semibold">{{ shop.name }}</div>
            <div class="text-gray-500 ">{{ shop.description }}</div>
          </div>
          <edit-shop class="p-2" v-bind="shop" @fetch="fetchShops" />
        </div>
      </div>
    </div>
    <div class="max-h-screen overflow-y-auto">
      <div class="flex items-center">
        <div class="text-2xl font-bold">ผู้ใช้งาน</div>
      </div>
      <hr class="my-3" />
      <div class="space-y-3 ">
        <div
          v-for="user in users"
          :key="user.id"
          class="border rounded md:flex"
        >
          <div
            class="w-full p-2 overflow-hidden text-sm truncate overflow-ellipsis"
          >
            <div class="font-semibold">
              {{ user.fname + ' ' + user.lname }}
            </div>
            <div class="text-gray-500 ">{{ user.email }}</div>
          </div>
          <edit-user class="p-2" v-bind="user" @fetch="fetchUsers" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import AddShop from '../components/admin/AddShop.vue'
import EditShop from '../components/admin/EditShop.vue'
import EditUser from '../components/admin/EditUser.vue'
export default {
  components: { AddShop, EditShop, EditUser },
  created() {
    this.fetchUsers()
    this.fetchShops()
  },
  data() {
    return {
      users: [],
      shops: []
    }
  },
  methods: {
    fetchUsers() {
      axios.get('/admin/users').then(res => {
        if (res.data.success) {
          this.users = res.data.users
        }
      })
    },
    fetchShops() {
      axios.get('/admin/shops').then(res => {
        if (res.data.success) {
          this.shops = res.data.shops
        }
      })
    }
  }
}
</script>
