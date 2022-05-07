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
    // init map
    this.initMap(function () {
      // init autocomplete
      this.initAutoComplete()

      // draw heatmap
      this.renderHeatmap({
        id: 1,
        feature: {
          geometry: {"type": "Point", "coordinates": [8.526771, 52.020077]},
        },
        size: 2,
        color: {r: 255, g: 244, b: 0},
      })
      this.renderHeatmap({
        id: 2,
        feature: {
          geometry: {"type": "Point", "coordinates": [8.526771, 52.120277]},
        },
        size: 1,
        color: {r: 255, g: 0, b: 0},
      })
    }.bind(this))
  },
  methods: {
    /**
     * init the map
     * @param callback
     */
    initMap(callback) {
      // init mapbox
      window.mapboxgl.accessToken = 'pk.eyJ1IjoianVsdHVlIiwiYSI6ImNqbmYxa2F1cDA5dTEza3BheXhieXBjaWUifQ.U0O1Y3TKXr05adK81oG6Aw';
      this.map = new window.mapboxgl.Map({
        container: 'map', // container ID
        style: 'mapbox://styles/mapbox/streets-v11', // style URL
        center: [8.526771, 52.020077], // starting position
        zoom: 16 // starting zoom
      });

      // call callback
      this.map.on('load', callback)
    },

    /**
     * init the autocomplete
     */
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
    },

    /**
     * render a heatmap
     */
    renderHeatmap({id, feature, color, size}) {
      // Add a geojson point source.
// Heatmap layers also work with a vector tile source.
      this.map.addSource('earthquakes'+id, {
        'type': 'geojson',
        'data': {
          "type": "FeatureCollection",
          "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
          "features": [
            feature
          ]
        }
      });

      this.map.addLayer(
          {
            'id': 'earthquakes-heat'+id,
            'type': 'heatmap',
            'source': 'earthquakes'+id,
            'maxzoom': 20,
            'paint': {
// Increase the heatmap weight based on frequency and property magnitude
              'heatmap-weight': [
                'interpolate',
                ['linear'],
                ['get', 'mag'],
                0,
                0,
                10,
                5
              ],
// Increase the heatmap color weight weight by zoom level
// heatmap-intensity is a multiplier on top of heatmap-weight
              'heatmap-intensity': [
                'interpolate',
                ['linear'],
                ['zoom'],
                0,
                1,
                9,
                3
              ],
// Color ramp for heatmap.  Domain is 0 (low) to 1 (high).
// Begin color ramp at 0-stop with a 0-transparancy color
// to create a blur-like effect.
              'heatmap-color': [
                'interpolate',
                ['linear'],
                ['heatmap-density'],
                0,
                `rgba(${color.r},${color.g},${color.b},0)`,
                0.3,
                `rgba(${color.r},${color.g},${color.b},0.2)`,
                1,
                `rgba(${color.r},${color.g},${color.b},0.8)`,
              ],
// Adjust the heatmap radius by zoom level
              'heatmap-radius': [
                'interpolate',
                ['linear'],
                ['zoom'],
                0,
                size * 10,
                20,
                size * 10
              ],
// Transition from heatmap to circle layer by zoom level
              'heatmap-opacity': [
                'interpolate',
                ['linear'],
                ['zoom'],
                15,
                1,
                25,
                0
              ]
            }
          },
          'waterway-label'
      );


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
