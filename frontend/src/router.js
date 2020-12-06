import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Merchant from "./views/Merchant.vue";
import Order from "./views/Order.vue";
import Admin from "./views/Admin.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/login",
      component: Login,
    },
    {
      path: "/register",
      component: Register,
    },
    {
      path: "/merchant",
      component: Merchant,
    },
    {
      path: "/order",
      component: Order,
    },
    {
      path: "/admin",
      component: Admin,
    },
  ],
});
