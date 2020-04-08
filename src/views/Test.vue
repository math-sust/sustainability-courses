<template>
  <div class="md-layout md-gutter md-alignment-top-center">
    <div class="md-layout-item md-size-25 md-medium-size-33 md-small-size-50 md-xsmall-size-100">
      <span><li>123</li> ipsum dolor sit amet.</span>
    </div>
    <div class="md-layout-item md-size-25 md-medium-size-33 md-small-size-50 md-xsmall-size-100">
      <span>Lorem ipsum dolor sit amet.</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "TestPage"
};
</script>

<style lang="scss" scoped>
@import "~vue-material/dist/theme/engine";

.md-layout-item {
  min-height: 40px;
  // transition: .3s $md-transition-stand-timing;

  span {
    width: 100%;
    height: 100%;
    padding: 8px;
    display: block;
    background: md-get-palette-color(blue, 200);
  }
}
</style>