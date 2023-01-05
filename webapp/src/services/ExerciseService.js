import axios from "axios";

const API_URL = 'http://localhost:8081/exercises/'

class ExerciseService {
    getAllExercises() {
        return axios
            .get(API_URL)
            .then(response => response.data);
    }

    getExerciseById(exerciseId) {
        return axios
            .get(API_URL + exerciseId)
            .then(response => response.data);
    }

    createExercise(exercise) {
        return axios
            .post(API_URL, exercise)
            .then(response => response.data)
    }

    updateExercise(exerciseId, exercise) {
        return axios
            .patch(API_URL + exerciseId, exercise)
            .then(response => response.data);
    }

    deleteExercise(exerciseId) {
        return axios
            .delete(API_URL + exerciseId)
            .then(response => response);
    }

    async getExerciseImage(exerciseId) {
        const response = await axios
            .get(API_URL + exerciseId + '/image', { responseType: 'blob' });
        return response.data;
    }
}

export default new ExerciseService();