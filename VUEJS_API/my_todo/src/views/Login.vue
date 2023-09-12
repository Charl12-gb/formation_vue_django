<template>
    <div class="container mt-5">
        <h2 class="mb-4">Connexion</h2>
        <form @submit.prevent="loginUser">
            <div class="mb-3">
                <label for="email" class="form-label">Email:</label>
                <input type="text" class="form-control" id="username" v-model="userFormData.username" />
            </div>

            <div class="mb-3">
                <label for="password" class="form-label">Mot de passe:</label>
                <input type="password" class="form-control" id="password" v-model="userFormData.password" />
            </div>

            <button class="btn btn-primary" type="submit">Se connecter</button>
        </form>
    </div>
</template>
  
<script>
import { mapActions } from 'vuex'
export default {
    name: "LoginViews",
    data() {
        return {
            userFormData:{
                username: "",
                password: ""
            }
        };
    },
    methods: {
        ...mapActions('auth', ['login']),
        async loginUser() {
            await this.login(this.userFormData).then((data)=>{
                console.log(data)
                this.$router.push({ name: "Home" });
            }).catch((error)=>{
                console.log(error)
            })
        },
    },
};
</script>
  