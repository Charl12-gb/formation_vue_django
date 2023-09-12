import axios from 'axios';
import { BASE_API_URL } from '../services/api';
import axiosWithHeaders from '../services/api';
import router from '../router/index'

const state = {
  accessToken: null,
  refreshToken: null,
  currentUser: null
};

const getters = {
  getAccessToken: (state) => state.accessToken,
  getRefreshToken: (state) => state.refreshToken,
  getCurrentUser: (state) => state.currentUser
};

const mutations = {
  setTokens(state, { access, refresh }) {
    state.accessToken = access;
    state.refreshToken = refresh;
    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
    localStorage.setItem('user', true);
  },

  removeTokens(state) {
    state.accessToken = null;
    state.refreshToken = null;
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user');
  },

  setCurrentUser(state, user ){
    state.currentUser = user
  }

};

const dataLogout = {
  refresh_token: localStorage.getItem('refresh_token')
}

const actions = {

  // User
  login({ commit }, loginData) {
    return new Promise((resolve, reject) => {
      axios.post(BASE_API_URL + 'login', loginData)
        .then(response => {
          console.log(response)
          commit('setTokens', response.data);
          commit('refreshToken', response.data);
          commit('setCurrentUser', response.data.user)
          resolve(response.data);
        })
        .catch(error => {
          reject(error.response.data);
        });
    });
  },
  
  logout({ commit, dispatch, state }) {
    return new Promise((resolve, reject) => {
      axiosWithHeaders.delete('logout', dataLogout)
        .then(response => {
          commit('removeTokens');
          router.push('/login')
        })
        .catch(error => {
          reject(error.response);
          router.push('/login')
        });
    });
  },

  registerUser({ commit, dispatch, state }, userData) {
    return new Promise((resolve, reject) => {
      axios.post('register', userData)
        .then(response => {
          resolve(response.data);
        })
        .catch(error => {
          reject(error.response.data);
        });
    });
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
};
