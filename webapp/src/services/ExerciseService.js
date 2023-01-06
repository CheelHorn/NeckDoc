import axios from "axios";

const API_URL = 'http://localhost:8081/exercises/'

class ExerciseService {
    async getAllExercises() {
        const response = await axios
            .get(API_URL);
        return response.data;
    }

    async getExerciseById(exerciseId) {
        const response = await axios
            .get(API_URL + exerciseId);
        return response.data;
    }

    async createExercise(exercise) {
        const response = await axios
            .post(API_URL, exercise);
        return response.data;
    }

    async updateExercise(exerciseId, exercise) {
        const response = await axios
            .patch(API_URL + exerciseId, exercise);
        return response.data;
    }

    async deleteExercise(exerciseId) {
        const response = await axios
            .delete(API_URL + exerciseId);
        return response;
    }

    async getExerciseImage(exerciseId) {
        const response = await axios
            .get(API_URL + exerciseId + '/image', { responseType: 'blob' });
        return response.data;
    }
}

export default new ExerciseService();