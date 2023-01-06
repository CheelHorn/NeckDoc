<template>
    <div>
        <ExerciseForm :exercise="exercise"/>
    </div>
</template>

<script>
import ExerciseForm from '@/components/ExerciseForm.vue';
import ExerciseService from '@/services/ExerciseService';

export default {
    name: 'ExerciseView',
    components: {
        ExerciseForm
    },
    props: ['id'],
    data() {
        return {
            exercise: null
        };
    },
    computed: {
        currentUser() {
            return this.$store.getters.getCurrentUser;
        },
    },
    async created() {
        if (!this.currentUser) {
            this.$router.push('/login');
        }

        this.exercise = await ExerciseService.getExerciseById(this.id)
    }
}
</script>
