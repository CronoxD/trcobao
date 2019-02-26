import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

// Check authenticacion
import isAuthenticated from './auth_config'
router.beforeEach(isAuthenticated)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
