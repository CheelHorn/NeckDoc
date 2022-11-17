import { createWebHistory, createRouter } from "vue-router";
import Home from "./components/Home.vue";
import LoginPage from "./components/Login.vue";
import SignupPage from "./components/Signup.vue";


const routes = [
    {
        path: "/",
        name: "home",
        component: Home,
    },
    {
        path: "/home",
        component: Home,
    },
    {
        path: "/login",
        component: LoginPage,
    },
    {
        path: "/signup",
        component: SignupPage,
    },
]


const router = createRouter({
    history: createWebHistory(),
    routes,
    });

export default router