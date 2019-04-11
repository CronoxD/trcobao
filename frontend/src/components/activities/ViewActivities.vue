<template lang="pug">
	div
		cardTeacher(
			:title="'Actividades'",
			:items="activities",
			:toLinkAdd="'actividades'"
	)
</template>

<script>
import FormActivity from "./FormActivity.vue";
import CardTeacher from "../teachers/CardTeacher.vue";
import Service from "../../utils/services";

export default {
  name: "view-activities",
  data() {
    return {
			activities: [],
			service: null
		}
  },
  components: {
    FormActivity,
    CardTeacher
  },
  methods: {
    getActivities: function() {
      this.service
        .get("activities/")
        .then(data => (this.activities = data.data));
    }
	},
	mounted: function () {
		this.service = new Service();
    this.getActivities();
	}
};
</script>

<style scoped>
</style>