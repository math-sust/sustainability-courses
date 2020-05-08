<template>
  <div class="faculty">
    <h1>Faculty Resources Page</h1>
    <p>
      If you would like to incorporate sustainability in the classroom, you may
      find the following resources helpful:
    </p>

    <div>
      <md-button
        href="https://www.wpi.edu/offices/sustainability"
        class="md-raised md-primary"
        >WPI Office of sustainablity</md-button
      >
      <md-button
        href="https://web.wpi.edu/Images/CMS/Facilities/WPI_Sustainability_Plan.pdf"
        class="md-raised md-primary"
        >WPI Sustainability Plan
      </md-button>
    </div>
    <div id="faculty-content" class="md-elevation-2">
      <h2>Faculty Resources</h2>
      <md-tabs
        class="md-transparent"
        md-alignment="fixed"
        style="min-height: 80vh;"
      >
        <md-tab id="tab-findings" md-label="Our Findings">
          We also wanted to provide faculty with information regarding student
          interest in learning about specific Sustainable Development Goals, and
          their desired delivery methods. We surveyed 101 students across 11
          sustainability themed courses and received the following results. To
          read more about our findings and our methodology, see our paper (in
          'About the Project').
          <img src="../assets/studentinterestsdg.jpg" />
          <br /><br />
          <img src="../assets/studentinterestdelivery.jpg" />
          <p></p>
        </md-tab>
        <md-tab id="tab-resources" md-label="Sustainability Resources">
          Here are some of the resources other faculty sent us which may help
          incorporate sustainability in the classroom.
          <md-table>
            <md-table-row>
              <md-table-head>Title</md-table-head>
              <md-table-head>Description</md-table-head>
            </md-table-row>
            <md-table-row>
              <md-table-cell>Engineering Unleashed</md-table-cell>
              <md-table-cell>A website with </md-table-cell>
            </md-table-row>
            <md-table-row>
              <md-table-cell
                ><a
                  href="https://hub.aashe.org/browse/publication/15675/A-Guide-for-Applied-Sustainability-Learning-Projects-Advancing-sustainability-outcomes-on-campus-and-in-the-community"
                >
                  A Guide for Applied Sustainability Learning Projects:
                  Advancing sustainability outcomes on campus and in the
                  community
                </a></md-table-cell
              >
              <md-table-cell
                >This guide provides a step-by-step framework for how a new or
                existing applied learning for sustainability program can be
                systematically designed, built and scaled
              </md-table-cell>
            </md-table-row>
          </md-table>
        </md-tab>
      </md-tabs>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped>
.faculty {
  max-width: 1000px;
}
#faculty-content {
  margin-top: 20px;
  background-color: white;
  padding: 20px;
}

#tab-resources {
  text-align: left;
}

.md-tab {
  min-height: 800px;
}
</style>
