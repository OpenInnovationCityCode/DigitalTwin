<template>
  <div class="map">
    <div id="map"/>
    <div class="search">
      <input type="search" adressomat-autocomplete="name" adressomat-autofill="attributes.street"
             placeholder="Strasse"/>
    </div>
  </div>
</template>

<script>
import {AdressOMatInput} from "@/js/AdressOMatInput.js";

export default {
  name: 'Map',
  data() {
    return {
      map: undefined
    }
  },
  mounted() {
    this.initMap()
    this.initAutoComplete()
  },
  methods: {
    initMap(){
      // TO MAKE THE MAP APPEAR YOU MUST
      // ADD YOUR ACCESS TOKEN FROM
      // https://account.mapbox.com
      window.mapboxgl.accessToken = 'pk.eyJ1IjoianVsdHVlIiwiYSI6ImNqbmYxa2F1cDA5dTEza3BheXhieXBjaWUifQ.U0O1Y3TKXr05adK81oG6Aw';
      this.map = new window.mapboxgl.Map({
        container: 'map', // container ID
        style: 'mapbox://styles/mapbox/streets-v11', // style URL
        center: [-68.137343, 45.137451], // starting position
        zoom: 5 // starting zoom
      });

      this.map.on('load', () => {
// Add a data source containing GeoJSON data.
        this.map.addSource('maine', {
          'type': 'geojson',
          'data': {
            'type': 'Feature',
            'geometry': {
              'type': 'Polygon',
// These coordinates outline Maine.
              'coordinates': [
                [
                  [-67.13734, 45.13745],
                  [-66.96466, 44.8097],
                  [-68.03252, 44.3252],
                  [-69.06, 43.98],
                  [-70.11617, 43.68405],
                  [-70.64573, 43.09008],
                  [-70.75102, 43.08003],
                  [-70.79761, 43.21973],
                  [-70.98176, 43.36789],
                  [-70.94416, 43.46633],
                  [-71.08482, 45.30524],
                  [-70.66002, 45.46022],
                  [-70.30495, 45.91479],
                  [-70.00014, 46.69317],
                  [-69.23708, 47.44777],
                  [-68.90478, 47.18479],
                  [-68.2343, 47.35462],
                  [-67.79035, 47.06624],
                  [-67.79141, 45.70258],
                  [-67.13734, 45.13745]
                ]
              ]
            }
          }
        });

// Add a new layer to visualize the polygon.
        this.map.addLayer({
          'id': 'maine',
          'type': 'fill',
          'source': 'maine', // reference the data source
          'layout': {},
          'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
          }
        });
// Add a black outline around the polygon.
        this.map.addLayer({
          'id': 'outline',
          'type': 'line',
          'source': 'maine',
          'layout': {},
          'paint': {
            'line-color': '#000',
            'line-width': 3
          }
        });
      });
    },
    initAutoComplete() {
      AdressOMatInput.init({
        key: "110541a0c770c328ce040a11f2fe55ecd889cd13",
        callbacks: {
          "clickResult": function ({data}) {
            let coordinates = data.coordinates
            console.log({
              longitude: coordinates.long,
              latitude: coordinates.lat,
              duration: 3500,
              zoom: 11
            })
            this.map.flyTo({
              center: [
                coordinates.long,
                coordinates.lat,
              ],
              duration: 7500,
              zoom: 16.5
            })
          }.bind(this)
        },
        configuration: {
          "showLogo": true
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

div.map {
  position: absolute;
  top: 0;
  right: 0;
  width: 70%;
  float: right;
  height: 100vh;
  overflow: hidden;
}

#map {
  z-index: 1;
  position: absolute;
  width: 100%;
  height: 100vh;
}

div.map .search {
  z-index: 2;
  position: absolute;
  top: 20px;
  left: 20px;
}

div.map .search input {
  width: 300px;
  -webkit-appearance: none;
  outline: none;
  padding: 13px;
  font-family: inherit;
  font-size: .9rem;
  font-weight: 400;
  box-sizing: border-box;
  position: relative;
  border-radius: 7px;
  resize: none;
  transition: border .25s, background 1s, color 1s;
  background: #fff;
  border: none;
}
</style>
