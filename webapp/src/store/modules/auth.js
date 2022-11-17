import AuthService from "@/services/AuthService";
import axios from "axios";

const state = {
    user: null,
    token: null,
};

const getters = {
    isAuthenticated: (state) => {
        return state.token;
    },
    getCurrentUser: state => {
        return state.user;
    }
};

const actions = {
    login: async ({ commit }, loginData) => {

        const token = await AuthService.login(loginData);
        commit('set_token', token);

        const user = await AuthService.me();
        commit('set_current_user', user);

        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

        return await Promise.resolve(loginData);
    },
    logout: ({ commit }) => {
        commit('set_token', null);
        commit('set_current_user', null);
    },

    // eslint-disable-next-line
    signup: async ({ commit }, signupData) => {
        const user = await AuthService.signup(signupData);

        return await Promise.resolve(user);
    }
};

const mutations = {
    set_token: (state, token) => {
        state.token = token;
    },
    set_current_user: (state, user) => {
        state.user = user;
    },
};

export default {
  state,
  getters,
  actions,
  mutations
};