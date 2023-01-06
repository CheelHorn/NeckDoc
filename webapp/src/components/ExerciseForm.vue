<template>
    <div>
        <form @submit.prevent="update">
            <div class ="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" ref="input_name" :value="exercise.name"/>
            </div>
            <button type="submit" class="btn btn-primary">Update</button>
        </form>
        <div v-if="message">
            {{ message }}
        </div>
    </div>
</template>

<script>
import ExerciseService from '@/services/ExerciseService';

export default {
    name: 'ExerciseForm',
    props: ['exercise'],
    methods: {
        async update() {
            const exercise = {
                'name': this.$refs.input_name.value
            };
            
            try {
                const updatedExercise = await ExerciseService.updateExercise(this.exercise.id, exercise)
                this.$router.push('/exercise', updatedExercise.id);
            } catch (error) {
                this.message = error.toString();
            }
        }
    }
}
</script>
