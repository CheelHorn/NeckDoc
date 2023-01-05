import UserService from '@/services/UserService';

const state = {
    user: null,
    users: null,
};

const actions = {
    getUsers: async ({ commit }) => {
        const users = await UserService.getAllUsers();
        commit('set_users', users);
    },

    getUserById : async ({ commit }, [userId]) => {
        const user = await UserService.getUserById(userId);
        commit('set_user', user);
    },

    updateUser: async( { commit }, [userId, user]) => {
        const updatedUser = await UserService.updateUser(userId, user);
        commit('set_current_user', updatedUser, { root: true });
    }
};

const mutations = {
    set_users: (state, users) => {
        state.users = users;
    },
    set_user: (state, user) => {
        state.user = user;
    }
};

export default {
  state,
  actions,
  mutations
};