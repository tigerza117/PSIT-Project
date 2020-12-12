import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Logout from './views/Logout.vue'
import Register from './views/Register.vue'
import Shop from './views/Shop.vue'
import Order from './views/Order.vue'
import Admin from './views/Admin.vue'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home,
      name: 'home',
      meta: {
        requiresAuth: true,
        layout: 'private'
      }
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
      path: '/shops/:id',
      component: Shop,
      name: 'shop',
      meta: {
        requiresAuth: true,
        layout: 'private'
      }
    },
    {
      path: '/order',
      component: Order,
      name: 'order',
      meta: {
        requiresAuth: true,
        layout: 'private'
      }
    },
    {
      path: '/admin',
      component: Admin,
      name: 'admin',
      meta: {
        requiresAuth: true,
        layout: 'private'
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
