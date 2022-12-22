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

    async updateUser(userId, user) {
        console.log(user)
        const response = await axios
            .post(API_URL + userId, user);

        return response.data
    }
}

export default new UserService();