import axios from 'axios';

export const BASE_API_URL = "http://127.0.0.1:8000/api/";

const axiosWithHeaders = axios.create({
  baseURL: BASE_API_URL
});

// Ajoutez un intercepteur de requête pour inclure le jeton d'accès dans chaque requête
axiosWithHeaders.interceptors.request.use(
  config => {
    const accessToken = localStorage.getItem('access_token');
    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosWithHeaders;