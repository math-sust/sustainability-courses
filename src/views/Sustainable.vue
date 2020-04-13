<template>
  <div>
    <md-table
      v-model="searched"
      md-sort="title"
      md-sort-order="asc"
      md-card
      md-fixed-header
    >
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Sustainable Courses</h1>
        </div>

        <md-field md-clearable class="md-toolbar-section-end">
          <md-input
            placeholder="Search by name..."
            v-model="search"
            @input="searchOnTable"
          />
        </md-field>
      </md-table-toolbar>

      <md-table-empty-state
        md-label="No course found"
        :md-description="
          `No course found for this '${search}' query. Try a different search keyword.`
        "
      >
      </md-table-empty-state>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Title" md-sort-by="title">{{
          item.title
        }}</md-table-cell>
        <md-table-cell md-label="Number" md-sort-by="subject">{{
          item.subject + item.course
        }}</md-table-cell>
        <md-table-cell md-label="CRN" md-sort-by="CRN">{{
          item.CRN
        }}</md-table-cell>
        <md-table-cell md-label="Instructor" md-sort-by="instructor">{{
          item.instructor
        }}</md-table-cell>
        <md-table-cell md-label="Section" md-sort-by="section" md-numeric>{{
          item.section
        }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import course_list from "@/assets/courses.json";
const toLower = (text) => {
  return text.toString().toLowerCase();
};

const searchByName = (items, term) => {
  if (term) {
    return items.filter((item) => toLower(item.title).includes(toLower(term)));
  }

  return items;
};

export default {
  name: "Sustainable",
  data: () => ({
    search: null,
    searched: [],
    courses: course_list,
    /*
    Example
    {
        "title": "Machine Learning",
        "subject": "CS",
        "CRN": 11111,
        "course": "453X",
        "instructor": "Jacob Whitehill",
        "section": "D01",
        "description": "This course covers sustainability topics such as..."
    },
     */
  }),
  methods: {
    searchOnTable() {
      this.searched = searchByName(this.courses, this.search);
    },
  },
  created() {
    this.searched = this.courses;
  },
};
</script>

<style lang="scss" scoped>
.md-field {
  max-width: 300px;
}
</style>
