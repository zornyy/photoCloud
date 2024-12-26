import { createRouter, createWebHistory } from '@ionic/vue-router';
import HomePage from '../pages/HomePage.vue'
import Login from '../pages/Login.vue'
import Signin from '../pages/Signin.vue'

const routes = [
    {
        path: '/',
        redirect: '/login',
      },
      {
        path: '/login',
        name: 'Login',
        component: Login,
      },
      {
        path: '/signin',
        name: 'Signin',
        component: Signin,
      },
      {
        path: '/home',
        name: 'Home',
        component: HomePage,
      },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;