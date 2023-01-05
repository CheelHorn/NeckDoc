import AuthService from "@/services/AuthService";
import axios from "axios";

const state = {
    current_user: null,
    token: null,
};

const getters = {
    isAuthenticated: (state) => {
        return state.token;
    },
    getCurrentUser: state => {
        return state.current_user;
    }
};

const actions = {
    login: async ({ commit }, loginData) => {

        const token = await AuthService.login(loginData);
        commit('set_token', token);

        axios.defaults.headers.common['Authorization'] = `Bearer ${token.access_token}`;

        const user = await AuthService.me();
        commit('set_current_user', user);
    },

    logout: ({ commit }) => {
        commit('set_token', null);
        commit('set_current_user', null);

        axios.defaults.headers.common['Authorization'] = ``;
    },

    // eslint-disable-next-line
    signup: async ({ commit }, signupData) => {
        await AuthService.signup(signupData);
    }
};

const mutations = {
    set_token: (state, token) => {
        state.token = token;
    },
    set_current_user: (state, user) => {
        state.current_user = user;
    },
};

export default {
  state,
  getters,
  actions,
  mutations
};