<template>
  <Dashboard/>
</template>

<script>
import Dashboard from './components/Dashboard.vue'

export default {
  name: 'App',
  components: {
    Dashboard
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,500;1,600;1,700;1,800&display=swap');
html, body{
  padding: 0;
  margin: 0;
  font-family: 'Open Sans', sans-serif;
}
#app {
  width: 100%;
  height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
