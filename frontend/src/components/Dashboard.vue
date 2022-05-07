<template>
  <div class="main">
    <Menu @change-layer="changeLayer"/>
    <Map :layer="layer"/>
  </div>
</template>

<script>

import Menu from "@/components/Menu.vue";
import Map from "@/components/Map.vue";

export default {
  name: 'HelloWorld',
  components: {
    Menu,
    Map,
  },
  data () {
    return {
      layer: undefined,
    }
  },
  props: {
    msg: String
  },
  methods: {
    changeLayer(layer) {
      this.layer = layer
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
