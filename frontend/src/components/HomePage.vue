<template>
  <div>
    <h1>Welcome to Smart Study Analyzer!</h1>
    <p>Track your study patterns and improve your learning.</p>
    <router-link to="/schedule">Go to Study Schedule</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
h1 {
  color: #333;
}
</style>
