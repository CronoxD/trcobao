import HomeActivity from '../views/HomeActivity.vue'

const activitiesRoutes = {
    path: '/actividades',
    name: 'activities',
    component: HomeActivity,
    meta: { 
        requiresAuth: true
    }
}

export default activitiesRoutes