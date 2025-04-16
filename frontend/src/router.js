import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import StudySchedule from './components/StudySchedule.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/schedule',
    name: 'StudySchedule',
    component: StudySchedule,
  },
  
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
