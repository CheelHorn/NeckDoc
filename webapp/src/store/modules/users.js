import UserService from '@/services/UserService';

const state = {
    users: null,
  };

const actions = {
    getUsers: async ({ commit }) => {
        const users = await UserService.getAllUsers();
        commit('set_users', users);
        return await Promise.resolve(users);
    }
};

const mutations = {
    set_users: (state, users) => {
        state.users = users;
    },
};

export default {
  state,
  actions,
  mutations
};