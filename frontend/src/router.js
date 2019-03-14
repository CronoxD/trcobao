import Vue from 'vue'
import Router from 'vue-router'

// Local
import HomeTeachers from './views/HomeTeachers.vue'
import HomeGroup from './views/HomeGroup.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/grupos',
      name: 'groups',
      component: HomeGroup,
      meta: { 
        requiresAuth: true
      }
    },
    {
      path: '/maestros',
      name: 'teachers',
      component: HomeTeachers,
      meta: { 
        requiresAuth: true
      }
    },
    {
      path: '/',
      name: 'root',
      meta: {
        requiresAuth: true
      }
    }
  ]
})
