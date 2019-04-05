<template lang="pug">
div.mainContent
	aside-nav
	.content
			transition(name="fade", mode="out-in")
				view-groups(
					v-if="elementRoute=='grupos'"
				)
				view-activities(
					v-if="elementRoute=='actividades'",
				)
</template>

<script>
// Views
import ViewGroups from '../components/groups/ViewGroups.vue';
import ViewActivities from '../components/activities/ViewActivities.vue';

// Aside Nav
import AsideNav from '../components/general/AsideNav.vue';

export default {
  name: "HomeTeachers",
  data() {
    return {
			elementRoute: 'groups' //default groups
    };
  },
  components: {
		ViewGroups,
		ViewActivities,
		AsideNav
	},
	watch: {
		'$route' (to, from) {
			this.elementRoute = to.params.element
		}
	},
  mounted: function() {
		this.elementRoute = this.$route.params.element
  }
};
</script>

<style scoped>

	/* Animations */
	.fade-enter-active, .fade-leave-active {
		transition: all .4s;
	}
	.fade-enter {
		transform: translateY(150px);
		opacity: 0;
	}
	.fade-leave-to {
		transform: translateY(-50px);
		opacity: 0;
	}
	/* Styles */
	.mainContent {
		display: grid;
    grid-template-columns: 300px 1fr;
    grid-template-rows: 1fr;
    height: 100vh;
    position: fixed;
    top: 57px;
    bottom: 0;
    left: 0;
    right: 0;
	}
</style>
