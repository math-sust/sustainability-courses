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
        <div class="md-toolbar-section-start">
          <md-menu md-direction="bottom-end">
            <md-button md-menu-trigger>SDGs</md-button>
            <md-menu-content>
              <p>Sustainable Development Goals</p>

              <div class="sdgs">
                <!--                        <img src="../assets/sdgs/E-WEB-Goal-1.png" v-on:click="toggleSDG(1)" width="100">-->

                <div class="sdgs">
                  <button v-on:click="selectAllSDG">Select All</button>
                  <button v-on:click="selectNoneSDG">Select None</button>
                  <div v-for="SDG in sdgs" :key="SDG.num">
                    <div class="sdg" width="30%">
                      <img v-bind:src="SDG.src" v-on:click="toggleSDG(1)" />
                    </div>
                  </div>
                </div>
                <!--                        <img v-bind:src=SDG.src v-on:click="toggleSDG(1)" width="100">-->
              </div>
            </md-menu-content>
          </md-menu>
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
const toLower = text => {
  return text.toString().toLowerCase();
};

const searchByName = (items, term) => {
  if (term) {
    return items.filter(item => toLower(item.title).includes(toLower(term)));
  }

  return items;
};

const SDGS = () => {
  var ret = [];
  for (var i = 1; i < 18; i++) {
    ret.push({
      num: i,
      src: require("../assets/sdgs/E-WEB-Goal-" + i + ".png")
    });
  }
  return ret;
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
    sdgs: SDGS()
  }),
  methods: {
    searchOnTable() {
      this.searched = searchByName(this.courses, this.search);
    },
    selectAllSDG() {
      console.log("TODO");
    },
    selectNoneSDG() {
      console.log("TODO");
    },
    toggleSDG(num) {
      console.log("TODO" + num);
    }
  },
  created() {
    this.searched = this.courses;
  }
};
</script>

<style lang="scss" scoped>
.md-field {
  max-width: 300px;
}

/* Three image containers (use 25% for four, and 50% for two, etc) */
.sdg {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}

.md-app {
  max-height: 400px;
  border: 1px solid rgba(#000, 0.12);
}

.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}

.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
