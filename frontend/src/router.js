import { createRouter,  createWebHistory } from "vue-router"

import Home from "./views/Home.vue"
import Map from "./views/Map.vue"

const routes = [
    { path: "/", component: Home },
    { path: "/map", component: Map }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router