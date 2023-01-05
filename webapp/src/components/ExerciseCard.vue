<template>
  <div class="card">
    <div class="card-header">
      Exercise
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ exercise.name }}</h5>
      <p class="card-text">{{ exercise.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['exercise'],
}
</script>

