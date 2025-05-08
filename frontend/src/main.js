// // // main.js
// // import { createApp } from 'vue';
// // import App from './App.vue';
// // import router from './router'; // Make sure the path to your router.js is correct

// // const app = createApp(App);
// // app.use(router); // This line is essential
// // app.mount('#app'); // Make sure your root element in index.html has the ID 'app'

// // main.js
// import { createApp } from 'vue';
// import App from './App.vue';
// import router from './router'; // Make sure the path to your router.js is correct
// import * as VueGraph from 'vue-graph';
// const { Graph } = VueGraph;

// const app = createApp(App);

// app.component('Graph', Graph); // Globally register the Graph component

// app.use(router); // This line is essential
// app.mount('#app'); // Make sure your root element in index.html has the ID 'app'

// main.js
// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Make sure the path to your router.js is correct

const app = createApp(App);
app.use(router); // This line is essential
app.mount('#app'); // Make sure your root element in index.html has the ID 'app'