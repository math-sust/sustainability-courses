<template>
  <div id="app">
    <div id="nav">
      <md-tabs md-sync-route md-alignment="centered">
        <md-tab id="tab-home" md-label="Home" to="/" exact></md-tab>
        <md-tab id="tab-about" md-label="About" to="/about"></md-tab>
        <md-tab
          id="tab-sustainable"
          md-label="Sustainable Courses"
          to="/sustainable"
        ></md-tab>
        <md-tab id="tab-faculty" md-label="Faculty Page" to="/faculty"></md-tab>
      </md-tabs>
    </div>
    <div id="content">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
@import "~vue-material/dist/theme/engine"; // Import the theme engine

@include md-register-theme(
  "default",
  (
    primary: md-get-palette-color(green, 300),
    // The primary color of your application
      accent: md-get-palette-color(cyan, 200) // The accent or secondary color,
  )
);

@import "~vue-material/dist/theme/all"; // Apply the theme

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#content {
  display: flex;
  margin: 3% auto;
  justify-content: center;
}
#nav a {
  font-weight: bold;
   color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}

Html, body {
  background-image: url('assets/bridge.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
