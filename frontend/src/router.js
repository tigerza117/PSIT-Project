import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Merchant from "./views/Merchant.vue";

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
      component: Home,
    },
    {
      path: "/admin",
      component: Home,
    },
  ],
});
