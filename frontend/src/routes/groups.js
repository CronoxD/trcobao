import HomeGroup from '../views/HomeGroup.vue'


const groupRoutes = {
    path: '/grupos',
    name: 'groups',
    component: HomeGroup,
    meta: { 
        requiresAuth: true
    },
    children: [
        {
            path: ':id',
            name: 'groupsId',
            component: HomeGroup,
            meta: { 
                requiresAuth: true
            }
        }
    ]
}

export default groupRoutes