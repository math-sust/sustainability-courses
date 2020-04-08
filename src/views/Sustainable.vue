<template>
  <div class="student">
    <div>Filter by keywords: <input /></div>
    <div>
      Select by category:
      <select>
        <option>Water reourses</option>
        <option>Carbon emissions</option>
      </select>
    </div>
    <div v-for="c in courses" :key="c">
      <Course
        :title="c.title"
        :course="c.course"
        :CRN="c.CRN"
        :description="c.description"
      />
    </div>
  </div>
</template>

<script>
import Course from "@/components/Course.vue";
import course_list from "@/assets/courses.json";
export default {
  name: "Sustainable",
  components: {
    Course,
  },
  data: function() {
    return {
      courses: course_list,
    };
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
