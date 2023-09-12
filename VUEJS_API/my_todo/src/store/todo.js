import axios from 'axios';
import {
    BASE_API_URL
} from '../services/api';

const state = {};

const getters = {};

const mutations = {};


const actions = {
    dotoList({
        commit,
        dispatch,
        state
    }) {
        return new Promise((resolve, reject) => {
            axios.get(BASE_API_URL + 'todo-list')
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
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
