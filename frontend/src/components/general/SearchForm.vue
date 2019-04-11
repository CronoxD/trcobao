<template lang="pug">
form.search(v-on:submit.prevent="search")
	input.formInput(type="search", placeholder="Buscar", v-model="toSearch")
	button.fas.fa-search.searchButton
</template>

<script>
export default {
	name: "search-form",
	data() {
		return {
			toSearch: ''
		}
	},
	methods: {
		search() {
			console.log(this.toSearch)
		}
	}
};
</script>

<style scoped>
	.search {
		position: relative;
	}
	.formInput {
		width: 100%;
		padding: 9px;
		font-size: 16px;
		border: 1px solid gray;
		border-radius: 8px;
		background: #f1f3f5;
	}
	.searchButton {
		background: #f1f3f5;
    border: none;
    position: absolute;
    right: 1%;
    top: 22%;
    font-size: 18px;
    color: gray;
		cursor: pointer;
	}
</style>
