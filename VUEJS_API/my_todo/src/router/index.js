import { createRouter, createWebHistory } from 'vue-router'
import jwt_decode from 'jwt-decode'
import Login from '../views/Login.vue';
import HomeView from '../views/Home.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      requiresAuth: false
    }
  },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

function isTokenValid(token) {
  if (!token) {
    return false
  }

  const decoded = jwt_decode(token)
  const currentTime = Date.now() / 1000

  return decoded.exp > currentTime
}

router.beforeEach(async (to, from, next) => {
  const token = localStorage.getItem('access_token')
  if (to.matched.some(record => record.meta.requiresAuth) && !isTokenValid(token)) {
    // Si la page nécessite une authentification et qu'il n'y a pas de token ou que le token est invalide, rediriger vers la page de connexion
    return next('/login')
  }
  return next()
})

export default router
