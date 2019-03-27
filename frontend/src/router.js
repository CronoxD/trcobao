import Vue from 'vue'
import Router from 'vue-router'

// Local

// Routes
import groupRoutes from './routes/groups'
import activitiesRoutes from './routes/activities'
import teacherRoutes from './routes/teachers'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    groupRoutes,
    activitiesRoutes,
    teacherRoutes,
    {
      path: '/',
      name: 'root',
      meta: {
        requiresAuth: true
      }
    }
  ]
})
