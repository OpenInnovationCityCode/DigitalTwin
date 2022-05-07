<template>
  <div class="map">
    <div id="map"/>
    <div class="search">
      <input type="search" adressomat-autocomplete="name" adressomat-autofill="attributes.street"
             placeholder="Adresse (z.B. Obernstraße 50, Bielefeld)"/>
    </div>
  </div>
</template>

<script>
import {AdressOMatInput} from "@/js/AdressOMatInput.js";

export default {
  name: 'Map',
  props: ["layer"],
  data() {
    return {
      map: undefined,
      data: {},
      measureStations: [],
      area: [
        [8.526634863791713, 52.02036389315646],
        [8.527185982109273, 52.02113321541481],
        [8.527208256393124, 52.02114121113124],
        [8.527369744950448, 52.02113207316961],
        [8.52727322305418, 52.02060333089511],
        [8.52735077318249, 52.01967119039685],
        [8.527317361756218, 52.01963920647202],
        [8.5272635322371, 52.01961978764953],
        [8.52721155890805, 52.019610649377114],
        [8.527150304627696, 52.019610649377114],
        [8.527111324631193, 52.01961750308189],
        [8.527066776063435, 52.01963235277117],
        [8.527029652257909, 52.01965519843759],
        [8.527005521783025, 52.019679186374645],
        [8.526862595129387, 52.019681470939105],
        [8.526862595129387, 52.01982425600593],
        [8.526975822737882, 52.019825398284496],
        [8.527001809401867, 52.020359981512655],
        [8.526634863791713, 52.02036389315646],
      ],
    }
  },
  watch: {
    "layer": function () {
      this.clearMap()
      if (this.layer === "CO2") {
        this.renderCircles({circles: this.data.measurements, color: {r: 255, g: 0, b: 0}, size: 25})
      } else if (this.layer === "humidity") {
        this.renderArea({area: this.area, color: "#256798"})
      } else if (this.layer === "ph") {
        this.renderArea({area: this.area, color: "#59369d"})
      } else if (this.layer === "volume") {
        this.renderCircles({circles: this.data.measurements, color: {r: 227, g: 136, b: 21}, size: 20})
      } else if (this.layer === "dust") {
        this.renderCircles({circles: this.data.measurements, color: {r: 94, g: 94, b: 94}, size: 60})
      } else if (this.layer === "temperatur") {
        this.renderCircles({circles: this.data.measurements, color: {r: 255, g: 47, b: 21}, size: 40})
      }
      console.log("LAYER CHANGED", this.layer)
    }
  },
  async mounted() {
    // load data from server
    const data = await window.fetch("http://localhost:5000/api/get_world")
    this.data = (await data.json()).data

    // init map
    this.initMap(function () {
      // init autocomplete
      this.initAutoComplete()

      // render boxes on map
      this.renderBoxes({boxes: this.data.measurements})
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
     * clears the whole map
     */
    clearMap() {
      if (this.map.getLayer('area') !== undefined)
        this.map.removeLayer('area')

      if (this.map.getLayer('area-outline') !== undefined)
        this.map.removeLayer('area-outline')

      if (this.map.getLayer('layer-heatmap1') !== undefined)
        this.map.removeLayer('layer-heatmap1')

      if (this.map.getLayer('layer-heatmap2') !== undefined)
        this.map.removeLayer('layer-heatmap2')

      if (this.map.getSource('area') !== undefined)
        this.map.removeSource('area')

      if (this.map.getSource('layer-heatmap1') !== undefined)
        this.map.removeSource('layer-heatmap1')

      if (this.map.getSource('layer-heatmap2') !== undefined)
        this.map.removeSource('layer-heatmap2')
    },

    /**
     * render boxes
     */
    renderBoxes({boxes}) {
      this.map.loadImage(
          '/icons/box.png',
          function (error, image) {
            if (error) throw error;

            // Add the image to the map style.
            this.map.addImage('box', image);

            // Add a data source containing one point feature.
            let points = []
            boxes.forEach((box) => {
              points.push({
                'type': 'Feature',
                'geometry': {
                  'type': 'Point',
                  'coordinates': [box.longitude, box.latitude]
                }
              })
            })
            this.map.addSource('point', {
              'type': 'geojson',
              'data': {
                'type': 'FeatureCollection',
                'features':
                points
              }
            });

            // Add a layer to use the image to represent the data.
            this.map.addLayer({
              'id': 'points',
              'type': 'symbol',
              'source': 'point', // reference the data source
              'layout': {
                'icon-image': 'box', // reference the image
                'icon-size': 0.025
              }
            });
          }.bind(this)
      );
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
     * renders an area based on polygons
     * @param area
     */
    renderArea({area, color}) {
      // Add a data source containing GeoJSON data.
      this.map.addSource('area', {
        'type': 'geojson',
        'data': {
          'type': 'Feature',
          'geometry': {
            'type': 'Polygon',
// These coordinates outline Maine.
            'coordinates': [
              area
            ]
          }
        }
      });

// Add a new layer to visualize the polygon.
      this.map.addLayer({
        'id': 'area',
        'type': 'fill',
        'source': 'area', // reference the data source
        'layout': {},
        'paint': {
          'fill-color': color, // blue color fill
          'fill-opacity': 0.75
        }
      });
// Add a black outline around the polygon.
      this.map.addLayer({
        'id': 'area-outline',
        'type': 'line',
        'source': 'area',
        'layout': {},
        'paint': {
          'line-color': '#000000',
          'line-width': 3
        }
      });
    },

    renderCircles({circles, color, size}) {
      circles.forEach((circle, idx) => {
        this.renderHeatmap({
          id: idx + 1,
          feature: {
            geometry: {"type": "Point", "coordinates": [circle.longitude, circle.latitude]},
          },
          size: size,
          color: color,
        })
      })
    },

    /**
     * render a heatmap
     */
    renderHeatmap({id, feature, color, size}) {
      // Add a geojson point source.
// Heatmap layers also work with a vector tile source.
      this.map.addSource('layer-heatmap' + id, {
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
            'id': 'layer-heatmap' + id,
            'type': 'heatmap',
            'source': 'layer-heatmap' + id,
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
