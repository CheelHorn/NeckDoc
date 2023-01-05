<template>
  <div>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
        </tr>
      </thead>
      <tbody v-for="user in users" :key="user.id" v-on:click="clickUser(user)">
        <tr class='clickable-row'>
            <td> {{ user.id }} </td>
            <td> {{ [user.firstname, user.lastname].filter(Boolean).join(" ") }} </td>
            <td> {{ user.email }} </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'UsersPage',
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
    users() {
      return this.$store.state.users.users
    }
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
    this.$store.dispatch('getUsers');
  },
  methods: {
    clickUser (user) {
      console.log("Clicked " + user.id);
    }
  }
};
</script>