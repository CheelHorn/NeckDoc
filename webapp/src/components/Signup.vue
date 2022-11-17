<template>
    <div>
        <form @submit.prevent="signup">
          <div>
            <label for="username">Username:</label>
            <input type="text" name="username" v-model="form.username" />
          </div>
          <div>
            <label for="password">Password:</label>
            <input type="password" name="password" v-model="form.password" />
          </div>
          <button type="submit">Sign Up</button>
        </form>
        <div v-if="message">
            {{ message }}
        </div>
    </div>
</template>

<script>
export default {
  name: 'SignupPage',
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
    getUsers() {
      return this.$store.state.users;
    }
  },
  mounted() {
    if (this.currentUser) {
      this.$router.push('/home');
    }
  },
  methods: {
    async signup() {
      const user = {
        'email': this.form.username,
        'password': this.form.password
      };

      try {
        await this.$store.dispatch('signup', user);
        this.$router.push('/login');
      } catch (error) {
        this.message = error.toString();
      }
      
    }
  }
}
</script>