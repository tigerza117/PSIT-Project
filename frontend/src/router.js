import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

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
      component: Home,
    },
    {
      path: "/register",
      component: Home,
    },
    {
      path: "/merchant",
      component: Home,
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
