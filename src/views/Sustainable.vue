<template>
  <div class="sustainable">
    <h1>Sustainability-Related Courses</h1>
    <div id="filters" width="30%">
      <div class="sdgs">
        <md-button v-on:click="selectAllSDG" class="md-raised md-primary"
          >Select All</md-button
        >
        <md-button v-on:click="selectNoneSDG" class="md-raised md-primary"
          >Select None</md-button
        >
        <div v-for="SDG in sdgs" :key="SDG.num" v-on:click="toggleSDG(SDG.num)">
          <div class="sdg" width="50%">
            <img
              ref="sdgz"
              v-bind:src="SDG.src"
              v-bind:class="['' + SDG.num, SDG.active ? `active` : `inactive`]"
            />
          </div>
        </div>
      </div>
    </div>
    <div id="sustainable-table">
      <md-table v-model="searched" md-sort="title" md-sort-order="asc" md-card>
        <md-table-toolbar>
          <div class="md-toolbar-section-start">
            <h1 class="md-title">Sustainable Courses</h1>
          </div>
          <div class="md-toolbar-section-start">
            <md-menu
              md-direction="bottom-end"
              md-size="auto"
              :md-close-on-click="false"
              :md-close-on-select="false"
            >
              <md-button class="md-raised md-primary" md-menu-trigger
                >SDG Filter</md-button
              >
              <md-menu-content>
                <p>Sustainable Development Goals</p>

                <div class="sdgs">
                  <div class="sdgs">
                    <md-button
                      v-on:click="selectAllSDG"
                      class="md-dense md-primary"
                      >Select All</md-button
                    >
                    <md-button
                      v-on:click="selectNoneSDG"
                      class="md-dense md-primary"
                      >Select None</md-button
                    >
                    <div
                      v-for="SDG in sdgs"
                      :key="SDG.num"
                      v-on:click="toggleSDG(SDG.num)"
                    >
                      <div class="sdg" width="33%">
                        <img
                          ref="sdgz"
                          v-bind:src="SDG.src"
                          v-bind:class="[
                            '' + SDG.num,
                            SDG.active ? `active` : `inactive`,
                          ]"
                        />
                      </div>
                    </div>
                  </div>
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
            `No course found for this query. Try selecting more SDGs or using a different search keyword.`
          "
        >
        </md-table-empty-state>

        <md-table-row
          slot="md-table-row"
          slot-scope="{ item }"
          @click="showDetails(item)"
        >
          <md-table-cell md-label="Name" md-sort-by="Name">{{
            item.Name
          }}</md-table-cell>
          <md-table-cell md-label="Subject" md-sort-by="Subject">{{
            item.Subject
          }}</md-table-cell>
          <md-table-cell md-label="Number" md-sort-by="Number">{{
            item.Number
          }}</md-table-cell>
        </md-table-row>
      </md-table>

      <div>
        <md-dialog :md-active.sync="showDialog">
          <md-dialog-title>Course Details</md-dialog-title>

          <md-tabs md-dynamic-height v-if="selected">
            <md-tab md-label="General">
              <p>
                {{ selected.Name }}
              </p>
            </md-tab>

            <md-tab md-label="SDGs">
              <p>
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam
                mollitia dolorum dolores quae commodi impedit possimus qui,
                atque at voluptates cupiditate. Neque quae culpa suscipit
                praesentium inventore ducimus ipsa aut.
              </p>
            </md-tab>

            <md-tab md-label="Details">
              <p>
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam
                mollitia dolorum dolores quae commodi impedit possimus qui,
                atque at voluptates cupiditate. Neque quae culpa suscipit
                praesentium inventore ducimus ipsa aut.
              </p>
            </md-tab>
          </md-tabs>

          <md-dialog-actions>
            <md-button class="md-primary" @click="showDialog = false"
              >Close</md-button
            >
            <!-- <md-button class="md-primary" @click="showDialog = false"
            >Save</md-button
          > -->
          </md-dialog-actions>
        </md-dialog>
      </div>
    </div>
  </div>
</template>

<script>
import course_list from "@/assets/courses.json";
const toLower = (text) => {
  return text.toString().toLowerCase();
};

const searchByName = (items, term, sdgs) => {
  var results = items;
  if (term) {
    results = items.filter((item) =>
      toLower(item.Name).includes(toLower(term))
    );
  }
  var activeSDGs = [];
  console.log(sdgs);
  for (var i = 0; i < 17; i++) {
    if (sdgs[i].active == 1) {
      activeSDGs.push(i + 1);
    }
  }
  console.log("active SDGS");
  console.log(activeSDGs);
  console.log(results[0].SDGs.some((r) => activeSDGs.indexOf(r) >= 0));
  results = results.filter((r) =>
    r.SDGs.some((r) => activeSDGs.indexOf(r) >= 0)
  );

  return results;
};

const SDGS = () => {
  var ret = [];
  for (var i = 1; i < 18; i++) {
    ret.push({
      num: i,
      src: require("../assets/sdgs/E-WEB-Goal-" + i + ".png"),
      active: 1,
    });
  }
  return ret;
};

export default {
  name: "Sustainable",
  data: () => ({
    showDialog: false,
    selected: null,
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
    sdgs: SDGS(),
  }),
  methods: {
    searchOnTable() {
      this.searched = searchByName(this.courses, this.search, this.sdgs);
    },
    selectAllSDG() {
      this.sdgs.forEach((sdg) => (sdg.active = 1));
      this.searchOnTable();
    },
    selectNoneSDG() {
      console.log("TODO");
      this.sdgs.forEach((sdg) => (sdg.active = 0));
      this.searchOnTable();
    },
    toggleSDG(num) {
      //console.log(num-1);
      //console.log(this.sdgs[num-1])
      if (this.sdgs[num - 1].active === 1) {
        // this.$refs.sdgz[num-1].classList.remove("active");
        this.sdgs[num - 1].active = 0;
      } else {
        // this.$refs.sdgz[num-1].setAttribute('style','filter:brightness(100%)');
        this.sdgs[num - 1].active = 1;
      }
      this.searchOnTable();
      //console.log(this.$refs.sdgz[num-1]);
    },
    showDetails(item) {
      this.selected = item;
      this.showDialog = true;
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

.md-table-cell {
  max-width: 400px;
}

.sdg {
  float: left;
  width: 33%;
  padding: 5px;
}

.sdgs {
  width: 30%;
}

.active {
  filter: brightness(100%);
}

.inactive {
  filter: brightness(50%);
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

table {
  width: 800px;
}

.md-table-row {
  cursor: pointer;
}
</style>
