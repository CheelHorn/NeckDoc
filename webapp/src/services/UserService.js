import axios from "axios";

class UserService {
    getAllUsers() {
        return axios
            .get('http://localhost:8081/users/')
            .then(response => response.data);
    }
}

export default new UserService();