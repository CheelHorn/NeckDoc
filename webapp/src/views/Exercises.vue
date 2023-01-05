<template>
  <div>
    <ExerciseCard
      v-for="exercise in exercises"
      :key="exercise"
      :exercise="exercise"
    ></ExerciseCard>
  </div>
</template>

<script>
import ExerciseCard from '@/components/ExerciseCard.vue';

export default {
  name: 'ExercisesPage',
  components: {
    ExerciseCard
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
    exercises() {
      return this.$store.state.exercises.exercises
    }
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
    this.$store.dispatch('getExercises');
  }
};
</script>