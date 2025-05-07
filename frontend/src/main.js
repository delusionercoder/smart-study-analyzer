// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Make sure the path to your router.js is correct

const app = createApp(App);
app.use(router); // This line is essential
app.mount('#app'); // Make sure your root element in index.html has the ID 'app'