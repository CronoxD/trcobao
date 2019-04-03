<template lang="pug">
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
</template>

<script>
import SearchForm from './SearchForm.vue';

export default {
	name: 'aside-nav',
	components: {
		SearchForm
	}
};
</script>

<style scoped>
.navAdmin {
  background: #0b0b3b;
}
.searchBox {
  margin: 10px;
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
