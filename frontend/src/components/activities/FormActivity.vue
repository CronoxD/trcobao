<template>
    <form @submit.prevent="_handleSubmit" class="card center-flex">

        <label for="activityName">Nombre de la actividad</label>
        <input v-model="activityName" class="input-form" type="text" id="activityName">
        <p v-bind:class="{ messageError: error, messageSuccess: !error }">{{ message }}</p>

        <div class="btn-container">
            <button-back></button-back>
            <input class="btn-success" type="submit" value="Enviar">
        </div>
    </form>
</template>

<script>

import { URL_API } from '../../utils'
import { getToken } from '../../utils'
import ButtonBack from '../general/ButtonBack.vue'

export default {
    name: 'formActivity',
    components: {
        ButtonBack
    },
    data() {
        return {
            activityName: '',
            token: '',
            message: null,
            error: false
        }
    },
    methods: {
        _handleSubmit: function() {

            const payload = {
                activityName: this.activityName
            }

            const settings = {
                method: 'POST',
                body: JSON.stringify(payload),
                credentials: 'include',
                headers: {
                    'X-CSRFToken' : this.token
                }
            }

            fetch(URL_API+'activities/', settings)
                .then(resp=> resp.json())
                .then(json => {
                    this.message = json.message
                    if( json.code != 201 ) {
                        this.error = true
                    } else {
                        this.error = false
                    }
                })
        }
    },
    mounted: function() {
        this.token = getToken()
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
    .messageError {
        color: rgb(228, 70, 70);
    }
    .messageSuccess {
        color: rgb(69, 192, 69);
    }
</style>