<template lang="pug">
	.content-view-groups
		group-students.card.studentsList(:groupId="groupId")
		items-list(@itemClick="itemClick", title='Grupos', :items="courses")
</template>

<script>
// Utils
import Service from "../../utils/services";
// Components
import ItemsList from "../general/ItemsList.vue";
import GroupStudents from './GroupStudents.vue';

export default {
	name: "view-groups",
	data () {
		return {
			groupId: undefined,
			service: undefined,
			courses: []
		}
	},
  components: {
		ItemsList,
		GroupStudents
	},
	methods: {
		itemClick(e) {
			this.groupId = e
		}
	},
  mounted: function() {
    this.service = new Service();
    this.service.get("courses/").then(resp => (this.courses = resp.data));
  }
};
</script>

<style scoped>
.content-view-groups {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  grid-column-gap: 10px;
}
.studentsList {
  grid-column: 2 span;
}
</style>