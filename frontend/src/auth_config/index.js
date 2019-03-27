
import { URL_BACK } from '../utils'

function isAuthenticated(to, from, next) {
    
    if (to.meta.requiresAuth) {
        fetch(URL_BACK+'user/', { credentials: 'include'})
            .then(resp => resp.json())
            .then(json => {
                if(json.code == 200) {
                    if(json.data.type == 'teacher' && to.name === 'root') {
                        next({name: 'teachers'})
                    }
                    else {
                        next()
                    }
                }
                else {
                    window.location.href = URL_BACK+'ingresar'
                }
            })
    } else {
        next()
    }
}

export default isAuthenticated