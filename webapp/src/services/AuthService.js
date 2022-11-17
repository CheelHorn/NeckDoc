import axios from "axios";

const API_URL = 'http://localhost:8081/auth/'

class AuthService {
    async login(user) {
        const response = await axios
            .post(API_URL + 'login', user, { 
                headers: { 
                    "Content-Type": "application/x-www-form-urlencoded"
                }
              });

        return response.data;
    }

    async signup(user) {
        const response = await axios
            .post(API_URL + 'signup', user);

        return response.data;
    }

    async me() {
        const response = await axios
            .get(API_URL + 'me');

        return response.data;
    }
}

export default new AuthService();