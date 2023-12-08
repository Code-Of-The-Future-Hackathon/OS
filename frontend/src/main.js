import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router.js"
import VueGoogleMaps from '@fawmi/vue-google-maps'

let app = createApp(App)
app.use(VueGoogleMaps, {
    load: {
        key: import.meta.env.VITE_GOOGLE_API,
        libraries: 'places',
    },
})
app.use(router)
app.mount('#app')
