import UserService from '@/services/UserService';

const state = {
    users: null,
  };

const actions = {
    getUsers: async ({ commit }) => {
        const users = await UserService.getAllUsers();
        commit('set_users', users);
        return await Promise.resolve(users);
    },

    updateUser: async( { commit }, [userId, user]) => {
        
        const updatedUser = await UserService.updateUser(userId, user);
        console.log(updatedUser)
        commit('set_current_user', updatedUser, { root: true });

        return await Promise.resolve(updatedUser);
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