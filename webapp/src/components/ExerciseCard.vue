<template>
  <div class="card">
    <div class="card-header">
      Exercise {{ exercise.id }}
    </div>
    <img class="card-img-left" style="width:20%" :src="image_url">
    <div class="card-body">
      <h5 class="card-title">{{ exercise.name }}</h5>
      <p class="card-text">{{ exercise.description }}</p>
    </div>
  </div>
</template>

<script>
import ExerciseService from '@/services/ExerciseService';

export default {
  props: ['exercise'],
  data() {
    return {
      image_url: null
    };
  },
  async mounted() {
    const image = await ExerciseService.getExerciseImage(this.exercise.id);
    this.image_url = URL.createObjectURL(image);
  }
}
</script>

