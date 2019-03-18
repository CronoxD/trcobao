<template>
<nav class="navbar background-gray">
    <h1 class="navbar-title"> <a href="#"><span>TR</span>COBAO</a></h1>
    <ul class="navbar-list">
        <template v-if="isLogin">
            <li><a href="#">{{user.first_name }}</a></li>
            <li><a :href="urlLogout">Salir</a></li>
            
        </template>
        
        <template v-else>
            <li> <a href=""> Instrucciones</a></li>
            <li> <a :href="urlLogin"> Ingresar</a></li>
            <li> <a :href="urlSignin"> Registrarse</a></li>
        </template>       
    </ul>
</nav>
</template>

<script>

import { URL_BACK } from '../../utils'

export default {
    name: 'navbar',
    data() {
        return {
            isLogin: false,
            urlLogout: URL_BACK + 'logout/',
            urlLogin: URL_BACK + 'ingresar/',
            urlSignin: URL_BACK + 'registrarse/',
            user: {}
        }
    },
    mounted: function() {
        this.getUserInfo()
    },
    methods: {
        getUserInfo: function() {
            fetch(URL_BACK + 'user/', { credentials: 'include'})
                .then(resp => resp.json())
                .then(data => {
                    if (data.code == 200) {
                        this.user = data.data
                        this.isLogin = true
                    } else {
                        window.location.href= URL_BACK + 'ingresar/'
                    }
                })
        }
    }
}
</script>

<style scoped>
.navbar {
    position: fixed;
    width: 100%;
    z-index: 100;
    top: 0;
    height: 57px;
}
.navbar-title {
    display: inline-block;
    margin: 15px 0 0 40px;
}
.navbar-title a{
    color: white;
    text-decoration: none;
}
.navbar-title span {
    color: black;
    background: #CC3300;
    padding: 15px;

}

.navbar-list {
    margin: 0;
    padding: 0;
    float: right;
    display: inline-block;
}

.navbar-list li{
    display: inline-block;
    margin-right: 25px;
}

.navbar-list a:hover {
    background: rgba(231, 195, 50, 0.7);
    color: black;
}

.navbar-list a {
    color: white;
    text-decoration: none;
    padding: 21px;
    display: block;
}

</style>
