import { createRouter, createWebHashHistory } from "vue-router"
import Index from "../views/Index.vue"
import Guide1 from "../views/Guide1.vue"
import Guide2 from "../views/Guide2.vue"
import Guide3 from "../views/Guide3.vue"
import WebsiteLogin from "../views/Login.vue"

const routes = [
  {
    path: "/",
    name: "index",
    component: Index
  },
  {
    path: "/login",
    name: "login",
    component: WebsiteLogin
  },
  {
    path: "/guide-1",
    name: "guide-1",
    component: Guide1
  },
  {
    path: "/guide-2",
    name: "guide-2",
    component: Guide2
  },
  {
    path: "/guide-3",
    name: "guide-3",
    component: Guide3
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
