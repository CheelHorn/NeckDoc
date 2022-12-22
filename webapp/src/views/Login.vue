<template>
  <div>
    <form @submit.prevent="login">
      <div class="form-group row">
        <label for="username" class="col-sm-2 col-form-label">Username:</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" name="username" v-model="form.username" />
        </div>
      </div>
      <div class="form-group row">
        <label for="password" class="col-sm-2 col-form-label">Password:</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" name="password" v-model="form.password" />
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Log in</button>
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