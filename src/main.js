import { createApp } from "vue"
import App from "./App.vue"
import LayoutHeader from "./components/layouts/Header.vue"
import LayoutFooter from "./components/layouts/Footer.vue"
import router from "./router"
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

import jQuery from "jquery"
window.$ = jQuery

import "./assets/css/style.css"

const app = createApp(App)
app.component("layout-header", LayoutHeader)
app.component("layout-footer", LayoutFooter)

app.use(router).mount("#app")
