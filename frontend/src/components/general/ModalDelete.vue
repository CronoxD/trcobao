<template>
    <div class="modal-container" v-bind:class="{ show: isShowModal, hidde: !isShowModal}">
        <div class="modal">
            <i class="fas fa-exclamation"></i>
            <h3>¿Estas seguro que quieres eliminar {{itemToDelete}}?</h3>
            <div class="modal-buttons">
                <i class="fas fa-check option" v-on:click="sendResponse({resp: true, itemId})"></i>
                <i class="fas fa-times option" v-on:click="sendResponse({resp: false, itemId})"></i>
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    name: 'modal-delete',
    props: ['itemToDelete', 'isShowModal', 'itemId'],
    methods: {
        sendResponse(obj) {
            this.$emit('onClickModal', obj)
        }
    }
}
</script>

<style scoped>
    .show {
        opacity: 1;
        z-index: 0;
    }

    .hidde {
        opacity: 0;
        z-index: -1;
    }
    .modal-container {
        position: fixed;
        background-color: rgba(0, 0, 0, 0.5);
        width: 100%;
        height: 100vh;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: opacity 0.3s ease-out;
    }

    .modal {
        background: white;
        border-radius: 9px;
        padding: 5% 20%;
        text-align: center;
    }

    .modal-buttons {
        display: flex;
        justify-content: space-around;
    }

    .modal h3 {
        font-size: 20px;
    }

    .fas.fa-exclamation {
        color: coral;
        font-size: 100px;
        background: gray;
        border-radius: 50%;
        width: 100px;
        height: 100px;
        padding: 15px;
    }
    .option {
        color: white;
        font-size: 40px;
        border-radius: 50%;
        height: 50px;
        width: 50px;
        line-height: 50px;
        padding: 10px;
        cursor: pointer;
    }
    .fas.fa-check {
        background: #28a745;
    }

    .fas.fa-times {
        background: #F78181;
    }
</style>
