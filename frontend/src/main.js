import Vue from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
//import Axios from 'axios'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

Axios.interceptors.request.use(request => {
  let token = localStorage.getItem('jwt')
  if (token) {
    request.headers.Authorization = `Bearer ${token}`
  }
  return request
})

Axios.defaults.baseURL = 'http://localhost:5000/'

Vue.prototype.$http = Axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
