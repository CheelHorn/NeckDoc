<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <div v-if="!currentUser" class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link to="/login" class="nav-link">
                Login
              </router-link>
            </li>
          </div>
          <div v-if="currentUser" class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link to="/home" class="nav-link">
                Home
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/users" class="nav-link">
                Users
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/exercises" class="nav-link">
                Exercises
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/profile" class="nav-link">
                Profile
              </router-link>
            </li>
            <li class="nav-item">
              <button class="btn btn-outline-danger" @click.prevent="logOut">LogOut</button>
            </li>
          </div>
        </ul>
      </div>
    </nav>
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
