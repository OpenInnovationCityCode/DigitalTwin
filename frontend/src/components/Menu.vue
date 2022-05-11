<template>
  <div class="menu">
    <div>
      <img class="logo" src="@/assets/logo.png" alt="logo"/>
    </div>
    <div class="layer_holder">
      <h2>Ebene</h2>
      <div :class="'layer' + (selected === 'CO2' ? ' active' : '')" @click="select('CO2')">
        <vue-feather type="cloud"></vue-feather>
        CO2
      </div>
      <div :class="'layer' + (selected === 'humidity' ? ' active' : '')" @click="select('humidity')">
        <vue-feather type="droplet"></vue-feather>
        Bodenfeuchte
      </div>
      <div :class="'layer' + (selected === 'ph' ? ' active' : '')" @click="select('ph')">
        <vue-feather type="activity"></vue-feather>
        Boden pH
      </div>
      <div :class="'layer' + (selected === 'volume' ? ' active' : '')" @click="select('volume')">
        <vue-feather type="volume-2"></vue-feather>
        Lautstärke
      </div>
      <div :class="'layer' + (selected === 'dust' ? ' active' : '')" @click="select('dust')">
        <vue-feather type="cloud-snow"></vue-feather>
        Feinstaub
      </div>
      <div :class="'layer' + (selected === 'temperatur' ? ' active' : '')" @click="select('temperatur')">
        <vue-feather type="thermometer"></vue-feather>
        Temperatur
      </div>
    </div>
    <div class="layer_holder">
      <h2>Pflanzen</h2>
      <div class="drop_holder">
        <div class="drop"><img src="/icons/laubbaum.png" @mouseup="alert(22)" alt="tree"/></div>
        <div class="drop" draggable><img src="/icons/tanne.png" alt="tree"/></div>
        <div class="drop" draggable><img src="/icons/hecke.png" alt="tree"/></div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Menu',
  data() {
    return {
      selected: null
    }
  },
  mounted() {
  },
  methods: {
    select(selected) {
      this.selected = selected
      this.$emit('change-layer', selected)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.menu {
  position: absolute;
  top: 0;
  left: 0;
  width: 30%;
  float: left;
  height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.menu img.logo {
  width: 200px;
  max-width: 60%;
}

.layer_holder {
  margin-top: 5vh;
}
.layer_holder:first-of-type {
  margin-top: 7.5vh;
}

.layer {
  position: relative;
  display: inline-block;
  box-sizing: border-box;
  border-radius: 12px;
  border: 3px solid #dfdfdf;
  color: #a4a4a4;
  font-weight: bold;
  width: calc(50% - 12px);
  margin-right: 12px;
  margin-bottom: 12px;
  cursor: pointer;
  transition: all .25s;
  padding: 13px 20px 13px 40px;
}

.layer:hover {
  transform: scale(0.975);
}

.layer.active {
  color: #000000;
  border: 3px solid #000000;
}
.layer i{
  position: absolute;
  left: 10px;
  top: 12px;
}

.drop_holder {

}

.drop {
  position: relative;
  width: 30px !important;
  height: 30px !important;
  display: inline-block;
  padding: 12px;
  background: #dfdfdf;
  border-radius: 12px;
  margin-bottom: 12px;
  margin-right: 12px;
  transition: all .25s;
  cursor: pointer;
}

.drop:hover {
  transform: scale(0.975);
}

.drop img{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30px;
}
</style>
