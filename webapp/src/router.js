import { createWebHistory, createRouter } from "vue-router";
import Home from "./views/Home.vue";
import LoginPage from "./views/Login.vue";
import SignupPage from "./views/Signup.vue";
import ProfilePage from "./views/Profile.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: Home,
    },
    {
        path: "/home",
        name: "name",
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
    {
        path: "/profile",
        component: ProfilePage,
    },
    {
        path: "/user/:id",
        component: ProfilePage,
    },
]


const router = createRouter({
    history: createWebHistory(),
    routes,
    });

export default router