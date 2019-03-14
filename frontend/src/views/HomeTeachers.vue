<template>
    <div class="content">
        <cardTeacher :title="'Grupos'" :items="groups"> </cardTeacher>
    </div>
</template>

<script>

import CardTeacher from '../components/teachers/CardTeacher.vue'
import { URL_API } from '../utils';

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
            fetch(URL_API+'courses/', { credentials: 'include'})
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
