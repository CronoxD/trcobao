
import HomeTeachers from '../views/HomeTeachers.vue'

const teacherRoutes = {
    path: '/maestros',
    name: 'teachers',
    component: HomeTeachers,
    meta: { 
        requiresAuth: true
    }
}

export default teacherRoutes