<template>
    <div class="content">
        <cardTeacher :title="'Grupos'" :items="groups"> </cardTeacher>
    </div>
</template>

<script>

import CardTeacher from '../components/teachers/CardTeacher.vue'

const API_URL = 'http://localhost:8000/api/';

export default {
    name :'HomeTeachers',
    data () {
        return {
            groups: []
        }
    },
    components: { CardTeacher },
    methods: {
        getGroups: function() {
            fetch(API_URL+'courses/', { credentials: 'include'})
                .then(resp => resp.json())
                .then(data => this.groups = data.data)
        }
    },
    mounted: function() {
        this.getGroups()
    }
}
</script>

<style scoped>

</style>
