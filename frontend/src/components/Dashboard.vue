<template>
  <div class="main">
    <Menu/>
    <Map/>
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
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
