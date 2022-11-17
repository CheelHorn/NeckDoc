<template>
    <div v-for="user in getUsers" :key="user">
        {{user}}
    </div>
</template>

<script>
export default {
  name: 'App',
  components: {

  },
  data() {
    return {};
  },
  computed: {
    currentUser() {
      return this.$store.getters.getCurrentUser;
    },
    istAuthenticated() {
      return this.$store.getters.istAuthenticated;
    },
    getUsers() {
      return this.$store.state.users
    }
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
    this.$store.dispatch('getUsers');
  }
};
</script>