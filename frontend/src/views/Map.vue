
<template>
    <GMapMap
      :center="{ lat: 45.00, lng: 0.1276 }"
      :zoom="5" 
      class="w-screen h-screen absolute top-0 left-0 z-[-1]"
      map-type-id="terrain" 
      :options="{
        disableDefaultUI: true,
      }"
    >
    <GMapMarker 
        v-if="layers[0].isChecked"
        v-for="land in landSlide"
        icon="http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
        :key="1"
        :position="{lat: land.coordinates[0], lng: land.coordinates[1]}"
        :draggable="false"
      >
      </GMapMarker>

      <GMapMarker 
        v-if="layers[1].isChecked"
        v-for="land in drought"
        :key="2"
        icon="http://maps.google.com/mapfiles/ms/icons/red-dot.png"
        :position="{lat: land.coordinates[0], lng: land.coordinates[1]}"
        :draggable="false"
      >
      </GMapMarker>

      <GMapMarker 
          v-if="layers[2].isChecked"
          v-for="land in flood"
          :key="3"
          icon="http://maps.google.com/mapfiles/ms/icons/green-dot.png"
          :position="{lat: land.coordinates[0], lng: land.coordinates[1]}"
          :draggable="false"
        >
      </GMapMarker>

      <GMapMarker 
          v-if="layers[3].isChecked"
          v-for="land in wildfire"
          :key="4"
          icon="http://maps.google.com/mapfiles/ms/icons/purple-dot.png"
          :position="{lat: land.coordinates[0], lng: land.coordinates[1]}"
          :draggable="false"
        >
      </GMapMarker>
    </GMapMap>

    <HierarchyLayers :layers="layers" :check="check"/>
</template>

<script setup>
    import HierarchyLayers from '../components/HierarchyLayers.vue';
    import { ref } from 'vue';
    import axios from 'axios';
    import {onMounted} from 'vue';

    let layers = ref([
        {
            id: 0,
            name: 'Landslides',
            isChecked: true,
            color: 'bg-blue-500',
        },
        {
            id: 1,
            name: 'Drought',
            isChecked: true,
            color: 'bg-red-500',
        },
        {
            id: 2,
            name: 'Flood',
            isChecked: true,
            color: 'bg-green-500'
        },
        {
            id: 3,
            name: 'Wildfire',
            isChecked: true,
            color: 'bg-purple-500'
        }
    ])

    const check = (layerIndex) => {
        layers.value[layerIndex].isChecked = !layers.value[layerIndex].isChecked
    }

    let landSlide = ref([]);

    let flood = ref([]);

    let drought = ref([]);

    let wildfire = ref([]);

    onMounted(() => {
      axios.get('http://localhost:8000/markers/landslide')
        .then(res => {
          landSlide.value = res.data.markers;
        })
        .catch(err => {
          console.log(err);
        })

      axios.get('http://localhost:8000/markers/flood')
        .then(res => {
          flood.value = res.data.markers;
        })
        .catch(err => {
          console.log(err);
        })

      axios.get('http://localhost:8000/markers/drought')
        .then(res => {
          drought.value = res.data.markers;
        })
        .catch(err => {
          console.log(err);
        })

      axios.get('http://localhost:8000/markers/wildfire')
        .then(res => {
          wildfire.value = res.data.markers;
        })
        .catch(err => {
          console.log(err);
        })
    })
</script>