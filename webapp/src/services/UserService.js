import axios from "axios";

const API_URL = 'http://localhost:8081/users/'


class UserService {
    async getAllUsers() {
        const response = await axios
            .get(API_URL);
        return response.data;
    }

    async getUserById(userId) {
        const response = await axios
            .get(API_URL + userId);
        return response.data;
    }

    async updateUser(userId, user) {
        const response = await axios
            .patch(API_URL + userId, user);
        return response.data;
    }
}

export default new UserService();