import ExerciseService from '@/services/ExerciseService';

export default {
    state: {
        exercises: [],
    },
    actions: {
        getExercises: async ({ commit }) => {
            const exercises = await ExerciseService.getAllExercises();
            commit('set_exercises', exercises);
        }
    },
    mutations: {
        set_exercises: (state, exercises) => {
            state.exercises = exercises;
        }
    }
};