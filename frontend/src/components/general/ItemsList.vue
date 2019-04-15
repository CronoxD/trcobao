<template lang="pug">
	.card.list-content
		h1 {{ title }}
		search-form(@search="search")
		transition-group(
			name="staggered-fade",
			tag="ul",
			v-bind:css="false",
			v-on:before-enter="beforeEnter",
			v-on:enter="enter",
			v-on:leave="leave"
		)
			li(v-for='(item, index) in computedItems', :key='item.id', :data-index='index', @click="itemClick(item.id)")
				| {{item.name}}
</template>

<script>
// Components
import SearchForm from "../general/SearchForm.vue";

export default {
  name: "items-list",
  props: ['title', 'items'],
  data() {
    return {
      toSearch: ""
    };
  },
  components: {
    SearchForm
  },
  methods: {
    search(e) {
      this.toSearch = e;
    },
    itemClick(id) {
      this.$emit('itemClick', id)
    },
    beforeEnter: function(el) {
      el.style.opacity = 0;
      el.style.height = 0;
    },
    enter: function(el, done) {
      const delay = el.dataset.index * 150;
      setTimeout(function() {
        Velocity(el, { opacity: 1, height: "1.6em" }, { complete: done });
      }, delay);
    },
    leave: function(el, done) {
      const delay = el.dataset.index * 150;
      setTimeout(function() {
        Velocity(el, { opacity: 0, height: 0 }, { complete: done });
      }, delay);
    }
	},
	computed: {
    computedItems: function () {
      const _this = this
      return this.items.filter( item => {
        return item.name.toLowerCase().indexOf(_this.toSearch.toLowerCase()) !== -1
      })
    }
  }
};
</script>

<style scoped>
.list-content {
  min-height: 300px;
}
ul li {
  cursor: pointer;
}
h1 {
  margin: 0 0 10px 0;
  text-align: center;
  font-size: 23px;
  color: #0b0b3b;
}

</style>
