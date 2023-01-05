import { createWebHistory, createRouter } from "vue-router";
import Home from "./views/Home.vue";
import LoginPage from "./views/Login.vue";
import SignupPage from "./views/Signup.vue";
import UsersPage from "./views/Users.vue";
import ProfilePage from "./views/Profile.vue";
import ExercisesPage from "./views/Exercises.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/home",
        component: Home,
    },
    {
        path: "/users",
        component: UsersPage,
    },
    {
        path: "/exercises",
        component: ExercisesPage,
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