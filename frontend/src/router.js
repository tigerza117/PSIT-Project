import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Logout from './views/Logout.vue'
import Register from './views/Register.vue'
import Shops from './views/Shops.vue'
import Merchant from './views/Merchant.vue'
import Order from './views/Order.vue'
import Admin from './views/Admin.vue'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home,
      name: 'home'
    },
    {
      path: '/login',
      component: Login,
      name: 'login',
      meta: {
        guest: true
      }
    },
    {
      path: '/logout',
      component: Logout,
      name: 'logout',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/register',
      component: Register,
      name: 'register',
      meta: {
        guest: true
      }
    },
    {
      path: '/shops',
      component: Shops,
      name: 'shops',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/merchant',
      component: Merchant,
      name: 'merchant',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/order',
      component: Order,
      name: 'order',
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/admin',
      component: Admin,
      name: 'admin',
      meta: {
        requiresAuth: true
      }
    }
  ]
})

//AuthRouter controller
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('jwt') == null) {
      next({
        path: '/login',
        query: { nextUrl: to.fullPath }
      })
    } else {
      let user = JSON.parse(localStorage.getItem('user'))
      if (to.matched.some(record => record.meta.is_admin)) {
        if (user.is_admin == 1) {
          next()
        } else {
          next({ name: 'home' })
        }
      } else {
        next()
      }
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem('jwt') == null) {
      next()
    } else {
      next({ name: 'home' })
    }
  } else {
    next()
  }
})

export default router
