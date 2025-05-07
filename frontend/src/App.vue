<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/schedule">Study Schedule</router-link> |
      <router-link to="/add-topic">Add Topic</router-link> |
      <router-link to="/show-topics">Show Topics</router-link>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}

main {
  margin-top: 20px;
}
</style>