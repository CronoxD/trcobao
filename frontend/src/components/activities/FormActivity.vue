<template lang="pug">
form.card.center-flex(@submit.prevent='_handleSubmit')
	label(for='activityName') Nombre de la actividad
	input#activityName.input-form(v-model='activityName', type='text')
	p(v-bind:class='{ messageError: error, messageSuccess: !error }') {{ message }}
	.btn-container
		button-back
		input(:class='{btnPrimary : acitivityId, btnSuccess : !acitivityId}', type='submit', :value='valueBtn')

</template>

<script>
import Service from "../../utils/services";
import ButtonBack from "../general/ButtonBack.vue";

export default {
  name: "formActivity",
  components: {
    ButtonBack
  },
  data() {
    return {
      activityName: "",
			acitivityId: undefined,
      service: null,
      message: null,
			error: false,
			valueBtn: 'Enviar'
    };
  },
  methods: {
    _handleSubmit: function() {
      // if there is an ID UPDATE the current course's Data.
      if (this.acitivityId !== undefined) {
        //UPDATE the current course's data
        this.service.put(`activities/${this.acitivityId}/`, {activityName: this.activityName})
					.then(this.setResp);
      } else {
        this.service.post('activities/', {activityName: this.activityName})
					.then(this.setResp);
      }
		},
		setResp(resp) {
      this.message = resp.message;

      if (resp.code != 201) {
        this.error = true;
      } else {
        this.error = false;
        this.courseName = "";
      }
    }
  },
  mounted: function() {
    this.acitivityId = this.$route.params.id;

    this.service = new Service();
    // if there is an ID get the course's Data.
    if (this.acitivityId !== undefined) {
      //Get the course data
      this.service
        .get(`activities/${this.acitivityId}/`)
        .then(res => {
          this.activityName = res.data.name;
          this.valueBtn = "Editar";
        })
        .catch(() => {this.$router.go(-1); this.acitivityId=undefined});
    }
  }
};
</script>

<style scoped>
.center-flex {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.center-flex label,
.center-flex input {
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