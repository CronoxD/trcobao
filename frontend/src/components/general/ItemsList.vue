<template lang="pug">
	.card.list-content
		h1 Grupos
		search-form
		ul
			li(v-for='item in items', :key='item.id')
				| {{item.name}}
</template>

<script>

// Components
import SearchForm from '../general/SearchForm.vue'
//Utils
import Service from '../../utils/services'

export default {
	name: 'items-list',
	data() {
		return {
			items: [],
			service: undefined
		}
	},
	components: {
		SearchForm
	},
	mounted: function () {
		this.service = new Service()
		this.service.get('courses/')
			.then(resp => this.items=resp.data )
	}
}
</script>

<style scoped>
	.list-content {
		min-height: 300px;
	}
	h1 {
		margin: 0 0 10px 0;
    text-align: center;
    font-size: 23px;
    color: #0b0b3b;
	}
	
</style>
