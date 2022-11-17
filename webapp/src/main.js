import { createApp } from 'vue'
import axios from 'axios';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import App from './App.vue'
import router from './router';
import store from './store';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

axios.defaults.headers.common['Authorization'] = `Bearer ${store.state.token}`;
axios.defaults.baseURL = 'http://localhost:8081/';

createApp(App)
  .use(router)
  .use(store)
  .use(BootstrapVue)
  .use(IconsPlugin)
  .mount('#app')
