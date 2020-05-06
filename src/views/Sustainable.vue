<template>
    <div class="sustainable">
        <h1>Sustainability-Related Courses</h1>


        <div id="filters" width="30%">
            <md-tabs class="md-primary" md-alignment="centered" >
                <md-tab id="tab-sdg" md-label="Sustainable Development Goals">
                    <div class="sdgs">
                        <md-button v-on:click="selectAllSDG" class="md-raised md-primary"
                        >Select All
                        </md-button
                        >
                        <md-button v-on:click="selectNoneSDG" class="md-raised md-primary"
                        >Select None
                        </md-button
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

                </md-tab>
                <md-tab id="tab-subjects" md-label="Subjects"></md-tab>
            </md-tabs>


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
                                :md-close-on-select="false">
                            <md-button class="md-raised md-primary" md-menu-trigger>Filter by Subject</md-button>
                            <md-menu-content>
                                <div id="toggleSearch">
                                    <md-button class="md-raised md-accent" v-on:click="swapALL">{{ ALLText}}</md-button><p/>
                                    <md-button class="md-raised md-accent" v-on:click="swapHU">{{HUText}}</md-button><p/>
                                    <md-button class="md-raised md-accent" v-on:click="swapSS">{{SSText}}</md-button><p/>
                                </div>
                                <div v-for="subject in subjects" :key="subject.name">
                                    <md-checkbox type="checkbox" v-model="subject.active" @change="searchOnTable" true-value="true" false-value="false">{{subject.name}}</md-checkbox><label></label>

                                    <input type="checkbox" v-model="subject.active" @change="searchOnTable"><label>{{subject.name}}</label>
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
                        }}
                    </md-table-cell>
                    <md-table-cell md-label="Subject" md-sort-by="Subject">{{
                        item.Subject
                        }}
                    </md-table-cell>
                    <md-table-cell md-label="Number" md-sort-by="Number">{{
                        item.Number
                        }}
                    </md-table-cell>
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
                                {{selected.SDGs}}

                            </p>
                        </md-tab>

                        <md-tab md-label="Details">
                            <p>
                                {{selected.Description}}
                            </p>
                        </md-tab>
                    </md-tabs>

                    <md-dialog-actions>
                        <md-button class="md-primary" @click="showDialog = false"
                        >Close
                        </md-button
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

    const searchByName = (items, term, sdgs, subjects) => {
        var results = items;
        if (term) {
            results = items.filter((item) =>
                toLower(item.Name).includes(toLower(term))
            );
        }
        var activeSDGs = [];
        //console.log(sdgs);
        for (var i = 0; i < 17; i++) {
            if (sdgs[i].active == 1) {
                activeSDGs.push(i + 1);
            }
        }
        //console.log("active SDGS");
        //console.log(activeSDGs);
        //console.log(results[0].SDGs.some((r) => activeSDGs.indexOf(r) >= 0));


        var subjectDict = {};
        subjects.forEach((s) => subjectDict[s.name] = s.active)

        //console.log(subjectDict);

        results = results.filter((r) =>
            r.SDGs.some((r) => (activeSDGs.indexOf(r) >= 0)) && subjectDict[r.Subject]
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

    const getSubjects = (courses) => {
        var ret = [];
        courses.forEach(c => ret.filter(r => r.name == c.Subject).length == 0 && ret.push({
            name: c.Subject,
            active: 1
        }));
        return ret.sort(function (a, b) {
            return ('' + a.name).localeCompare(b.name)
        });
    };

    const setSubjectState = (subjects, state, which) => {

        subjects.forEach(s => which.includes(s.name) ? s.active = state : null);

    }


    const SocialScience = ["ECON", "ENV", "GOV", "PSY", "SD", "SOC", "SS", "STS"];
    const Humanities = ["AR", "EN", "TH", "MU", "AB", "CN", "GN", "SP", "WR", "RH", "HI", "HU", "INTL", "PY", "RE"];


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
            humanities: true,
            socialScience: true,
            subjects: getSubjects(course_list),
            ALLText: "De-Select ALL",
            HUText: "De-Select All Humanities",
            SSText: "De-Select All Social Sciences",
            ALLActive: 1,
            HUActive: 1,
            SSActive: 1



        }),
        methods: {
            searchOnTable() {
                console.log("searchin")
                this.searched = searchByName(this.courses, this.search, this.sdgs, this.subjects);
            },
            selectAllSDG() {
                this.sdgs.forEach((sdg) => (sdg.active = 1));
                this.searchOnTable();
            },
            selectNoneSDG() {
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

            swapALL(){
                if (this.ALLActive) {
                    this.ALLActive = 0;
                    this.ALLText = "Select All";
                    this.subjects.forEach(s => s.active = 0);
                } else {
                    this.ALLActive = 1;
                    this.ALLText = "De-Select All";
                    this.subjects.forEach(s => s.active = 1);

                }
                this.searchOnTable();
            },

            swapHU() {
                if (this.HUActive) {
                    this.HUActive = 0;
                    this.HUText = "Select All Humanities";
                    setSubjectState(this.subjects, 0, Humanities);
                } else {
                    this.HUActive = 1;
                    this.HUText = "De-Select All Humanities";
                    setSubjectState(this.subjects, 1, Humanities);

                }
                this.searchOnTable();
            },
            swapSS() {
                if (this.SSActive) {
                    this.SSActive = 0;
                    this.SSText = "Select All Social Sciences";
                    setSubjectState(this.subjects, 0, SocialScience);
                } else {
                    this.SSActive = 1;
                    this.SSText = "De-Select All Social Sciences";
                    setSubjectState(this.subjects, 1, SocialScience);

                }
                this.searchOnTable();
            }

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
