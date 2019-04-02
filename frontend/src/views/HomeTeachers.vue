<template>
    <div class="content">
        <cardTeacher :title="'Grupos'" :items="groups" :toLinkAdd="'grupos'"> </cardTeacher>
        <cardTeacher :title="'Actividades'" :items="activities" :toLinkAdd="'actividades'"> </cardTeacher>
    </div>
</template>

<script>

import CardTeacher from '../components/teachers/CardTeacher.vue'
import Service from '../utils/services';

export default {
    name :'HomeTeachers',
    data () {
        return {
            groups: [],
            activities: [],
            service: null
        }
    },
    components: { CardTeacher },
    methods: {
        getGroups: function() {
            this.service.get('courses/')
                .then(data => this.groups = data.data)
        },
        getActivities: function() {
            this.service.get('activities/')
                .then(data => this.activities = data.data)
        }
    },
    mounted: function() {
        this.service = new Service()
        this.getGroups()
        this.getActivities()
    }
}
</script>

<style scoped>

</style>
