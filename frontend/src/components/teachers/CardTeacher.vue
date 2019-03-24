<template>
    <section class="card">
        <div class="content-title">
            <h2 class="subtitle">{{ title }}</h2>

            <router-link :to="toLinkAdd" class="btn-success m-left" >AGREGAR</router-link>
            
            <p class="m-left"></p>
        </div>

        <div class="content-body">
            <ul>
                <li v-for="item in items" :key="item.id" :id="item.id"> 
                    {{ item.name }}
                    <div class="icons-container">
                        <i v-on:click="showModal(item.id, item.name)" class="far fa-trash-alt button-delete"></i>
                        <i class="far fa-edit button-edit"></i>
                    </div>
                </li>
            </ul>
        </div>
        <modal-delete
            :isShowModal="showModalDelete.status"
            :itemToDelete="showModalDelete.name"
            :itemId="showModalDelete.id"
            v-on:onClickModal="responseModal">
        </modal-delete>
    </section>
</template>

<script>

import { getToken } from '../../utils'
import { URL_API } from '../../utils'
import ModalDelete from '../general/ModalDelete.vue'

export default {
    name: 'cardTeacher',
    props: [ 'title', 'items', 'toLinkAdd'],
    components: {
        ModalDelete
    },
    data () {
        return {
            token: '',
            showModalDelete: {
                status: false,
                name: '',
                id: null
            }
        }
    },
    methods: {
        showModal: function (itemId, itemName) {

            this.showModalDelete = {
                status: true,
                name: itemName,
                id: itemId
            }
            

        },
        responseModal(resp) {
            this.showModalDelete.status = false
            if (resp.resp) {
                const settings = {
                    method: 'DELETE',
                    credentials: 'include',
                    headers: {
                        'X-CSRFToken': this.token
                    }
                }

                fetch(URL_API+`${this.toLinkAdd}/${resp.itemId}/`, settings)
                    .then(resp => resp.json())
                    .then(data => {
                        if (data.code == 200) {
                            document.getElementById(resp.itemId).style.display = 'none'
                        }
                    })
            }
        }
    },
    mounted: function () {
        this.token = getToken()
    }
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
