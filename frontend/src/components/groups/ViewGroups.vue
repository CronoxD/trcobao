<template lang="pug">
	div
		cardTeacher(
			:title="'Grupos'",
			:items="groups",
			:toLinkAdd="'grupos'"
		)
		FormGroup
</template>

<script>
import FormGroup from "./FormGroup.vue";
import CardTeacher from "../teachers/CardTeacher.vue";
import Service from "../../utils/services";

export default {
	name: "view-groups",
	data() {
		return {
			groups: [],
			service: null
		}
	},
  components: {
		FormGroup,
		CardTeacher
	},
	methods: {
		getGroups: function() {
			this.service.get("courses/").then(data => (this.groups = data.data));
		}
	},
	mounted: function() {
		this.service = new Service();
    this.getGroups();
	}
};
</script>

<style scoped>
</style>