import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TasksListView from '../views/TasksListView.vue'
import WeekView from '../views/WeekView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/list',
      name: 'list',
      component: TasksListView
    },
    {
      path: '/week',
      name: 'week',
      component: WeekView
    },
  
  ]
})

export default router
