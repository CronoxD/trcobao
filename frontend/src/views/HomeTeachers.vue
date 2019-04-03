<template lang="pug">
div.mainContent
	aside.navAdmin
		search-form.searchBox
		router-link.itemButton(:to="'/maestros/user'") Mi perfil
			i.fas.fa-user.mLeft
		router-link.itemButton(:to="'/maestros/dashboard'") Dashboard
			i.fas.fa-tachometer-alt.mLeft
		router-link.itemButton(:to="'/maestros/grupos'") Grupos
			i.fas.fa-users.mLeft
		router-link.itemButton(:to="'/maestros/actividades'") Actividades
			i.fas.fa-book-open.mLeft
		router-link.itemButton(:to="'/maestros/reportes'") Reportes
			i.fas.fa-file-invoice.mLeft
	.content
			transition(name="fade", mode="out-in")
				cardTeacher(
					key="groups",
					v-if="elementRoute=='grupos'",
					:title="'Grupos'", :items="groups",
					:toLinkAdd="'grupos'"
				)
				cardTeacher(
					key="activities"
					v-if="elementRoute=='actividades'",
					:title="'Actividades'",
					:items="activities",
					:toLinkAdd="'actividades'"
				)
</template>

<script>
import CardTeacher from "../components/teachers/CardTeacher.vue";
import SearchForm from '../components/general/SearchForm.vue';
import Service from "../utils/services";

export default {
  name: "HomeTeachers",
  data() {
    return {
      groups: [],
      activities: [],
			service: null,
			elementRoute: 'groups' //default groups
    };
  },
  components: {
		CardTeacher,
		SearchForm
	},
  methods: {
    getGroups: function() {
      this.service.get("courses/").then(data => (this.groups = data.data));
    },
    getActivities: function() {
      this.service
        .get("activities/")
        .then(data => (this.activities = data.data));
    }
	},
	watch: {
		'$route' (to, from) {
			this.elementRoute = to.params.element
		}
	},
  mounted: function() {
		this.elementRoute = this.$route.params.element
    this.service = new Service();
    this.getGroups();
    this.getActivities();
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
	.navAdmin {
		background: #0B0B3B;
	}
	.searchBox {
		margin: 10px;
	}
	.itemsContent {
		margin: 0 10px;
	}
	.itemButton {
		display: block;
		color: white;
		font-size: 25px;
		border-bottom: 1px solid rgba(255, 255, 255, 0.2);
		transition: background-color 0.6s ease;
		text-align: center;
		text-decoration: none;
		line-height: 65px;
	}

	.itemButton:hover {
		background-color: rgba(255, 255, 255, 0.2);
	}
	.mLeft {
		margin-left: 10px;
	}
</style>
