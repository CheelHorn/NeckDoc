<template>
  <div>
    <h1 class="text-3xl font-bold underline">
      Hello world!!!
    </h1>
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
    }
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
  }
};
</script>