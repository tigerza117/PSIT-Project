<template>
  <div class="relative">
    <div class="fixed inset-x-0 bottom-0 z-20 w-full bg-white border-t">
      <div class="p-4">
        <div class="w-64 mx-auto btn-order" @click="showModal = true">
          สั่งอาหาร
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
          class="w-full p-4 mt-2 border rounded"
          v-model="note"
          placeholder="โน๊ต..."
        >
        </textarea>
      </div>
      <div slot="footer">
        <button
          @click="order"
          class="w-full p-3 text-lg text-center text-white transition duration-500 bg-green-500 rounded-lg hover:bg-green-600"
        >
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
      console.log(this.menus)
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

<style lang="postcss" scoped>
.btn-order {
  @apply p-2 max-w-xl w-full text-lg text-center text-white bg-green-500 transition duration-500 rounded-lg hover:bg-green-600;
}
</style>
