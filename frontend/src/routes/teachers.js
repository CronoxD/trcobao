
import HomeTeachers from '../views/HomeTeachers.vue'

const teacherRoutes = {
    path: '/maestros/:element',
    name: 'teachers',
    component: HomeTeachers,
    meta: { 
        requiresAuth: true
    }
}

export default teacherRoutes