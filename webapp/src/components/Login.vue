<template>
    <div>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" name="username" v-model="form.username" />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" name="password" v-model="form.password" />
        </div>
        <button type="submit">Log in</button>
      </form>
      <div v-if="message">
          {{ message }}
      </div>
      <router-link to="/signup" class="nav-link">
        Sign Up
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  components: {

  },
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      message: '',
    };
  },
  computed: {
    currentUser() {
      return this.$store.getters.getCurrentUser;
    },
  },
  mounted() {
    if (this.currentUser) {
      this.$router.push('/home');
    }
  },
  methods: {
    async login() {
      const user = {
        'username': this.form.username,
        'password': this.form.password
      };

      try {
        await this.$store.dispatch('login', user);
        this.$router.push('/home');
      } catch (error) {
        this.message = error.toString();
      }
      
    }
  }
}
</script>