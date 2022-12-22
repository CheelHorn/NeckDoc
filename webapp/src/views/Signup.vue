<template>
  <div>
    <form @submit.prevent="signup">
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
      <button type="submit" class="btn btn-primary">Sign Up</button>
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