// router.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue'; // Adjust paths if necessary
import OneDayStudyPlan from './components/OneDayStudyPlan.vue'; // Adjust paths if necessary
import AddTopic from './components/AddTopic.vue'; // Adjust paths if necessary
import ShowTopics from './components/ShowTopics.vue'; // Adjust paths if necessary

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/schedule',
    name: 'OneDayStudyPlan',
    component: OneDayStudyPlan,
  },
  {
    path: '/add-topic',
    name: 'AddTopic',
    component: AddTopic,
  },
  {
    path: '/show-topics',
    name: 'ShowTopics',
    component: ShowTopics,
  },
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;