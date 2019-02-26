
function isAuthenticated(to, from, next) {
    
    if (to.meta.requiresAuth) {
        fetch('http://localhost:8000/user/', { credentials: 'include'})
            .then(resp => resp.json())
            .then(json => {
                if(json.code == 200) {
                    next()
                }
                else {
                    window.location.href = 'http://localhost:8000/ingresar'
                }
            })
    }
}

export default isAuthenticated