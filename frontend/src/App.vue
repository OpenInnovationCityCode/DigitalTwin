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
html, body{
  padding: 0;
  margin: 0;
}
#app {
  width: 100%;
  height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
