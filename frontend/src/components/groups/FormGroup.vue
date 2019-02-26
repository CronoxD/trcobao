<template>
    <form @submit.prevent="_handleSubmit" class="card center-flex">

        <label for="groupName">Nombre del grupo</label>
        <input v-model="courseName" class="input-form" type="text" id="groupName">

        <input class="btn-success" type="submit" value="Enviar">
    </form>
</template>

<script>
export default {
    name: 'formGroup',
    data() {
        return {
            courseName: ''
        }
    },
    methods: {
        _handleSubmit: function() {
            const API_URL = 'http://localhost:8000/api/';

            const payload = {
                courseName: this.courseName
            }

            const settings = {
                method: 'POST',
                body: JSON.stringify(payload),
                credentials: 'include',
                headers: {
                    'X-CSRFToken' : 'GySrL3P1pbRxamJRUpnr5C4jid1b4NNEU3Lcj7BhC9VDcJTl1BjnTd9YeLWqWhog'
                }
            }

            fetch(API_URL+'courses/', settings)
                .then(resp=> resp.json())
                .then(json => {
                    console.log(json)
                })
        }
    }
}
</script>

<style scoped>
    .center-flex {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .center-flex label, .center-flex input {
        margin: 10px;
        font-size: 18px;
    }

</style>
