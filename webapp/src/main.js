import { createApp } from 'vue'
import axios from 'axios';

import App from './App.vue'
import router from './router';
import store from './store';


axios.defaults.headers.common['Authorization'] = `Bearer ${store.getters.isAuthenticated.access_token}`;
axios.defaults.baseURL = 'http://localhost:8081/';

createApp(App)
  .use(router)
  .use(store)
  .mount('#app')
