import Vue from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
//import Axios from 'axios'
import Vuex from 'vuex'
import Axios from 'axios'

import Default from './layouts/Default.vue'
import Private from './layouts/Private.vue'
import Modal from './components/Modal.vue'

import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

Vue.component('layout-default', Default)
Vue.component('layout-private', Private)
Vue.component('modal', Modal)

Vue.use(Vuex)
Vue.use(NProgress)

Axios.interceptors.request.use(request => {
  let token = localStorage.getItem('jwt')
  if (token) {
    request.headers.Authorization = `Bearer ${token}`
  }
  return request
})

Axios.interceptors.response.use(
  respone => {
    return respone
  },
  error => {
    let res = error.response
    if (res) {
      if (401 === res.status && localStorage.getItem('jwt')) {
        localStorage.removeItem('jwt')
        window.location = '/login'
      }
    }
    return Promise.reject(error)
  }
)

Axios.defaults.baseURL = 'https://api.tigerza117.xyz/'

Vue.prototype.$http = Axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
