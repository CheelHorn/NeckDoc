import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from './modules/auth';
import users from './modules/users';

const store = createStore({
  modules: {
    auth,
    users,
  },
  plugins: [createPersistedState()]
});

export default store;
