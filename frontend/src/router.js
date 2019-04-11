import Vue from 'vue'
import Router from 'vue-router'

// Local

// Routes
import teacherRoutes from './routes/teachers'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
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
