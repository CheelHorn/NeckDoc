<template>
  <div>
    <div v-if="!currentUser" class="navbar-nav ml-auto">
      <li class="nav-item">
        <router-link to="/login" class="nav-link">
          <font-awesome-icon icon="sign-in-alt" /> Login
        </router-link>
      </li>
    </div>
    <div v-if="currentUser" class="navbar-nav ml-auto">
      <li class="nav-item">
        <router-link to="/home" class="nav-link">
          <font-awesome-icon icon="user" />
          {{ currentUser.username }}
        </router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" @click.prevent="logOut">
          <font-awesome-icon icon="sign-out-alt" /> LogOut
        </a>
      </li>
    </div>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    currentUser() {
      return this.$store.getters.getCurrentUser
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
    }
  }
}
</script>
