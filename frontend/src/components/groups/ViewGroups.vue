<template lang="pug">
	.content-view-groups
		.tmp-students.card
		items-list
</template>

<script>

// Utils
import Service from "../../utils/services";
// Components
import ItemsList from '../general/ItemsList.vue'

export default {
	name: "view-groups",
  components: {
		ItemsList
	}
};
</script>

<style scoped>
	.content-view-groups {
		display: grid;
		grid-template-columns: repeat(3,1fr);
		grid-template-rows: repeat(3, 1fr);
		grid-column-gap: 10px;
	}
	.tmp-students {
		grid-column: 2 span;
	}
</style>