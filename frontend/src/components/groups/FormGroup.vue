<template lang="pug">
	form.card.center-flex(@submit.prevent='_handleSubmit')
		label(for='groupName') Nombre del grupo
		input#groupName.input-form(v-model='courseName', type='text')
		p(v-bind:class='{ messageError: error, messageSuccess: !error }') {{ message }}
		.btn-container
			button-back
			input(:class='{btnPrimary : courseId, btnSuccess : !courseId}', type='submit', :value='valueBtn')
</template>

<script>
import Service from "../../utils/services";
import ButtonBack from "../general/ButtonBack.vue";

export default {
  name: "formGroup",
  components: {
    ButtonBack
  },
  data() {
    return {
      courseName: "",
      courseId: undefined,
      service: null,
      message: null,
      error: false,
      valueBtn: "Enviar"
    };
  },
  methods: {
    _handleSubmit() {
      // if there is an ID UPDATE the current course's Data.
      if (this.courseId !== undefined) {
        //UPDATE the current course's data
        this.service.put(`courses/${this.courseId}/`, {courseName: this.courseName})
					.then(this.setResp);
      } else {
        this.service.post('courses/', {courseName: this.courseName})
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
    this.courseId = this.$route.params.id;

    this.service = new Service();
    // if there is an ID get the course's Data.
    if (this.courseId !== undefined) {
      //Get the course data
      this.service
        .get(`courses/${this.courseId}/`)
        .then(res => {
          this.courseName = res.data.name;
          this.valueBtn = "Editar";
        })
        .catch(() => {this.$router.go(-1); this.courseId=undefined});
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
