<template>
  <div class="faculty">
    <h1>Here is where we'd store information for faculty</h1>
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
        <md-tab id="tab-websites" md-label="Websites">
          TODO for websites
        </md-tab>
        <md-tab id="tab-books" md-label="Books">
          TODO for books
        </md-tab>
        <md-tab id="tab-media" md-label="Media">
          TODO for media
        </md-tab>
        <md-tab id="tab-others" md-label="Others">
          TODO for others
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
  /* .faculty {
    max-width: 1000px;
  } */
  #faculty-content{
    margin-top: 20px;
    background-color: white;
    padding: 20px;
  }
</style>
