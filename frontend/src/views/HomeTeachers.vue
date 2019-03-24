<template>
    <div class="content">
        <cardTeacher :title="'Grupos'" :items="groups" :toLinkAdd="'grupos'"> </cardTeacher>
        <cardTeacher :title="'Actividades'" :items="activities" :toLinkAdd="'actividades'"> </cardTeacher>
    </div>
</template>

<script>

import CardTeacher from '../components/teachers/CardTeacher.vue'
import { URL_API } from '../utils';

export default {
    name :'HomeTeachers',
    data () {
        return {
            groups: [],
            activities: []
        }
    },
    components: { CardTeacher },
    methods: {
        getGroups: function() {
            fetch(URL_API+'courses/', { credentials: 'include'})
                .then(resp => resp.json())
                .then(data => this.groups = data.data)
        },
        getActivities: function() {
            fetch(URL_API+'activities/', { credentials: 'include'})
                .then(resp => resp.json())
                .then(data => this.activities = data.data)
        }
    },
    mounted: function() {
        this.getGroups()
        this.getActivities()
    }
}
</script>

<style scoped>

</style>
