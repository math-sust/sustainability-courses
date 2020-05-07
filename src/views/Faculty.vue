<template>
  <div class="faculty">
    <h1>Faculty Resources Page</h1>
    <p>
      If you would like to contribute to have sustainability-related topics in your course, you may find the following links and information helpful:
    </p>

    <div>
      <md-button href="https://www.wpi.edu/offices/sustainability" class="md-raised md-primary">WPI Office of sustainablity</md-button>
      <md-button href="https://web.wpi.edu/Images/CMS/Facilities/WPI_Sustainability_Plan.pdf" class="md-raised md-primary">WPI Sustainability Plan </md-button>
    </div>
    <div id="faculty-content" class="md-elevation-2">
      <h2>Faculty Resources</h2>
      <md-tabs class="md-transparent" md-alignment="fixed">
        <md-tab id="tab-websites" md-label="Our Findings">
          We also wanted to provide faculty with information regarding student interest in learning about specific
          Sustainable Development Goals, and their desired delivery methods.
          We surveyed 101 students across 11 sustainability themed courses and received the following results.


        </md-tab>
        <md-tab id="tab-books" md-label="Sustainability Resources">
          Here are some of the resources other faculty sent us which may help one teach sustainability.
          <md-table>
            <md-table-row>
              <md-table-head>Title</md-table-head>
              <md-table-head>Description</md-table-head>
            </md-table-row>
            <md-table-row>
              <md-table-head>Engineering Unleashed</md-table-head>
              <md-table-head>A website with </md-table-head>
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
  #faculty-content{
    margin-top: 20px;
    background-color: white;
    padding: 20px;
  }
</style>
