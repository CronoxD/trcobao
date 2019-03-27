<template lang="pug">
section.card
  .content-title
    h2.subtitle {{ title }}
    router-link.btnSuccess.m-left(:to='toLinkAdd') AGREGAR
    p.m-left
  .content-body
    ul
      li(v-for='item in items', :key='item.id', :id='item.id')
        | {{ item.name }}
        .icons-container
          i.far.fa-trash-alt.button-delete(v-on:click='showModal(item.id, item.name)')
          router-link.far.fa-edit.button-edit(:to="`/${toLinkAdd}/${item.id}`", replace)
  modal-delete(
		:isShowModal='showModalDelete.status',
		:itemToDelete='showModalDelete.name',
		:itemId='showModalDelete.id',
		v-on:onClickModal='responseModal'
	)

</template>

<script>
import { getToken } from "../../utils";
import { URL_API } from "../../utils";
import ModalDelete from "../general/ModalDelete.vue";

export default {
  name: "cardTeacher",
  props: ["title", "items", "toLinkAdd"],
  components: {
    ModalDelete
  },
  data() {
    return {
      token: "",
      showModalDelete: {
        status: false,
        name: "",
        id: null
      }
    };
  },
  methods: {
    showModal: function(itemId, itemName) {
      this.showModalDelete = {
        status: true,
        name: itemName,
        id: itemId
      };
    },
    responseModal(resp) {
      this.showModalDelete.status = false;
      if (resp.resp) {
        const settings = {
          method: "DELETE",
          credentials: "include",
          headers: {
            "X-CSRFToken": this.token
          }
        };

        fetch(URL_API + `${this.toLinkAdd}/${resp.itemId}/`, settings)
          .then(resp => resp.json())
          .then(data => {
            if (data.code == 200) {
              document.getElementById(resp.itemId).style.display = "none";
            }
          });
      }
    }
  },
  mounted: function() {
    this.token = getToken();
  }
};
</script>

<style >
.content-portada {
  position: relative;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-title {
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
  color: #f78181;
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
