<template>
    <div>
      <img alt="Vue logo" src="@/assets/logo.png">
      <HelloWorld msg="Welcome to TODO LIST"/>
    </div>
  </template>
  
  <script>
  import HelloWorld from '@/components/HelloWorld.vue'
  
  export default {
    name: 'HomeView',
    components: {
      HelloWorld
    }
  }
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  