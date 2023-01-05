import axios from "axios";

const API_URL = 'http://localhost:8081/users/'


class UserService {
    getAllUsers() {
        return axios
            .get(API_URL)
            .then(response => response.data);
    }

    getUserById(userId) {
        return axios
            .get(API_URL + '/' + userId)
            .then(response => response.data);
    }

    updateUser(userId, user) {
        return axios
            .patch(API_URL + userId, user)
            .then(response => response.data);
    }
}

export default new UserService();