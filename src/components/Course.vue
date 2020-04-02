<template>
  <div class="course">
    <h1>{{ title }}</h1>
    <h2>{{ subject }}{{ course }}</h2>
    <div>{{ CRN }}</div>
    <div>{{ description }}</div>
  </div>
</template>

<script>
export default {
  name: "Course",
  props: {
    title: String,
    subject: String,
    course: String,
    CRN: Number,
    section: String,
    description: String,
    instructor: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.course {
    margin: 50px;
}
</style>
