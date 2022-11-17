<template>
  <div>
    <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
  <div v-for="user in getUsers" :key="user">
        {{user}}
  </div>
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
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
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