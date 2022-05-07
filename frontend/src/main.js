import { createApp } from 'vue'
import App from './App.vue'
import VueFeather from 'vue-feather';

const app = createApp(App)

// add components
app.component(VueFeather.name, VueFeather);

// mount app
app.mount('#app')