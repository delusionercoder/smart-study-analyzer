// import { createApp } from 'vue'
// import App from './App.vue'
// import './assets/main.css' // or main.scss if you're using SCSS

// createApp(App).mount('#app')


import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css' // or main.scss if you're using SCSS

// Import the router configuration
import router from './router'

// Create the Vue app and use the router
createApp(App)
  .use(router) // Add the router to the app
  .mount('#app')
