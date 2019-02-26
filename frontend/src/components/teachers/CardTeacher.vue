<template>
    <section class="card">
        <div class="content-title">
            <h2 class="subtitle">{{ title }}</h2>

            <router-link :to="'grupos'" class="btn-success m-left" >AGREGAR</router-link>
            
            <p class="m-left"></p>
        </div>

        <div class="content-body">
            <ul>
                <li v-for="item in items" :key="item.id"> 
                    {{ item.name }}
                    <div class="icons-container">
                        <i class="far fa-trash-alt button-delete"></i>
                        <i class="far fa-edit button-edit"></i>
                    </div>
                </li>
            </ul>
        </div>
    </section>
</template>

<script>
export default {
    name: 'cardTeacher',
    props: [ 'title', 'items']
}
</script>

<style >
.content-portada {
    position: relative;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.content-title{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    border-bottom: 1px solid darkgray;
}

.m-left {
    margin-left: 25px;
}

.icons-container {
    margin-left: 2%;
    display: inline-block;
}

.button-delete {
    color: #F78181;
    cursor: pointer;
}
.button-edit {
    color: #28a745;
    cursor: pointer;
}

.icons-container .button-edit {
    margin-left: 10px;
}

.subtitle {
    font-size: 20px;
}
</style>
