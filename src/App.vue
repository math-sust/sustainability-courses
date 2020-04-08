<template>
  <div class="page-container">
    <md-app md-waterfall md-mode="fixed">
      <md-app-toolbar class="md-primary">
        <span class="md-title">My Title</span>
      </md-app-toolbar>

      <md-app-drawer md-permanent="full">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>move_to_inbox</md-icon>
            <router-link to="/">Home</router-link>
          </md-list-item>

          <md-list-item>
            <md-icon>send</md-icon>
            <router-link to="/about">About</router-link>
          </md-list-item>

          <md-list-item>
            <md-icon>delete</md-icon>
            <router-link to="/sustainable">Sustainable Courses</router-link>
          </md-list-item>

          <md-list-item>
            <md-icon>error</md-icon>
            <router-link to="/faculty">For Faculty</router-link>
          </md-list-item>
      </md-app-drawer>

      <md-app-content>
        <router-view />
      </md-app-content>
    </md-app>
  </div>
</template>



<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
