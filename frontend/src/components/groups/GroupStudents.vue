
<template lang="pug">
  .card
    div(v-if="groupId !== undefined")
      h3 {{ groupName }}
      .studentList(v-if="students.length > 0") 
        p Alumnos:
        ol
          li(v-for="student in students")
            | {{student.name}} - {{student.status}} - 
            a(:href="'mailto: '+student.email") {{ student.email }}
      .showEmpty(v-else)
        p No hay alumnos en éste curso
    .showEmpty(v-else)
      p De clic en un curso para obtener más información
</template>

<script>

// Components
import ItemsList from "../general/ItemsList.vue";
// Utils
import Service from "../../utils/services";

export default {
  name: "group-students",
  props: ["groupId"],
  components: {
    ItemsList
  },
  data() {
    return {
      service: undefined,
      groupName: "",
      students: []
    };
  },
  mounted: function() {
    this.service = new Service();
  },
  watch: {
    groupId: function() {
      this.service
        .get(`courses/${this.groupId}/`)
        .then(resp => (this.groupName = resp.data.name));

      this.service
        .get(`courses/${this.groupId}/students/`)
        .then(resp => {
          if (resp.data.length > 0) {
            const students = resp.data.map(item => {
              item['name'] = `${item.first_name} ${item.last_name}`;
              return item;
            })
            this.students = students
          }
          else {
            this.students = []
          }
          
        })
    }
  }
};
</script>

<style scoped>
	h3 {
		margin: 0 0 10px 0;
    text-align: center;
    font-size: 23px;
    color: #0b0b3b;
	}
  .studentList p{
    font-size: 18px;
    margin: 0;
    font-weight: bold;
  }
  .studentList ol {
    margin: 5px 0;
  }
  .showEmpty {
    padding: 10px;
    font-size: 16px;
    border: 1px solid gray;
    border-radius: 8px;
    background: #f1f3f5;
    color: gray;
  }
</style>