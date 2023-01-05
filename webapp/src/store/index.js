import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from './modules/auth';
import users from './modules/users';
import exercises from './modules/exercises';

const store = createStore({
  modules: {
    auth,
    users,
    exercises,
  },
  plugins: [createPersistedState()]
});

export default store;
