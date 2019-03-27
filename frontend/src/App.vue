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
.content {
    margin: 106px 8% 0;
}

.card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    background: white;
    margin: 40px 0;
    padding: 20px;
    border-radius: 8px;
}

.input-form {
    border-radius: 9px;
    border: 1px solid #ced4da;
    padding: 8px;
    font-size: 16px;
    color: darkslategray;
}

.btnPrimary {
    border: none;
    padding: 10px;
    border-radius: 9px;
    color: #fff;
    background-color: #17a2b8;
    border-color: #17a2b8;
    cursor: pointer;
    text-decoration: none;
}

.btnSuccess {
    border: none;
    padding: 10px;
    border-radius: 9px;
    color: #fff;
    background-color: #28a745;
    border-color: #28a745;
    cursor: pointer;
    text-decoration: none;
}

.btnSuccess:hover {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.btn-container {
    display: flex;
    width: 100%;
    justify-content: space-evenly;
}
</style>
