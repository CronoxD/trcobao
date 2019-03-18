<template>
    <router-link :to="'maestros'" class="btn-back" >Regresar</router-link>
</template>

<script>
export default {
    name: 'button-back'
}
</script>

<style scoped>
    .btn-back {
        color: white;
        background: rgb(228, 70, 70);
        border: none;
        text-decoration: none;
        border-radius: 9px;
        padding: 10px;
        margin: 10px;
    }
</style>

