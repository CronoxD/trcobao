<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/general/Navbar.vue'
export default {
  components: {
    Navbar
  }
}
</script>


<style>
body {
    margin: 0;
    background: #EEE;
    font-family: 'Noto Sans TC', sans-serif;
}
.background-white {
    background: rgba(235, 237, 239, 0.2);
}

.background-gray {
    background: rgba(66, 66, 66, 0.8);
}
.background-gray label {
    color: white;
    text-align: center;
}
</style>
