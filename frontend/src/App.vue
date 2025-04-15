<template>
  <div id="app">
    <h1>Smart Study Analyzer</h1>
    <p>Welcome! Let’s start building your smart study planner 🧠📚</p>

    <!-- Add a router-link to navigate -->
    <router-link to="/home">Go to Home Page</router-link>
    <router-link to="/about">Go to About Page</router-link>

    <!-- This is where route content will be injected -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style scoped>
#app {
  font-family: 'Segoe UI', sans-serif;
  padding: 2rem;
  text-align: center;
  background-color: #f0f4f8;
  color: #333;
  min-height: 100vh;
}
</style>
