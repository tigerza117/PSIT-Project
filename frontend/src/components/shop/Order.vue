<template>
  <div class="relative">
    <div class="fixed inset-x-0 bottom-0 z-20 w-full bg-white border-t">
      <div class="p-2">
        <div class="w-64 max-w-xl mx-auto" @click="showModal = true">
          <button class="w-full btn btn-primary">
            สั่งอาหาร
          </button>
        </div>
      </div>
    </div>
    <modal v-if="showModal">
      <div slot="header">
        สั่งอาหาร
        <span class="float-right cursor-pointer" @click="showModal = false"
          >X</span
        >
      </div>
      <div slot="body">
        <div class="space-y-4 overflow-y-auto max-h-96">
          <menu-order
            v-for="(menu, index) in menus"
            v-bind="menu"
            :key="menu.id"
            @decrease="decrease(index)"
            @increase="menus[index].total += 1"
          />
        </div>
        <textarea
          class="w-full mt-3 input"
          v-model="note"
          placeholder="โน๊ต..."
        >
        </textarea>
      </div>
      <div slot="footer">
        <button @click="order" class="w-full btn btn-primary">
          ยืนยัน
        </button>
      </div>
    </modal>
  </div>
</template>

<script>
import MenuOrder from './MenuOrder.vue'
import axios from 'axios'
import swal from 'sweetalert2'
export default {
  components: {
    MenuOrder
  },
  props: {
    menus: Array
  },
  data() {
    return {
      showModal: false,
      loading: false,
      note: ''
    }
  },
  methods: {
    order() {
      this.loading = true
      axios
        .put('/shops/' + this.$route.params.id, {
          note: this.note,
          menus: this.menus
        })
        .then(res => {
          let data = res.data
          if (data.success) {
            this.$router.push('/order/' + data.order.id)
          }
        })
        .catch(error => {
          let res = error.response
          if (res) {
            if (400 === res.status) {
              let data = res.data
              swal.fire('สั่งอาหารไม่สำเร็จ', data.message, 'error')
            }
          }
        })
        .finally(() => ((this.showModal = false), (this.loading = false)))
    },
    decrease(idx) {
      let total = this.menus[idx].total
      this.menus[idx].total = total > 1 ? total - 1 : 1
      if (total - 1 == 0) {
        this.menus.splice(idx, 1)
      }
    }
  }
}
</script>
