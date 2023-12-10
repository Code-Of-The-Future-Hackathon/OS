
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
        :position="land"
        :draggable="false"
      >
      </GMapMarker>

      <GMapMarker 
        v-if="layers[1].isChecked"
        v-for="land in drought"
        :key="2"
        icon="http://maps.google.com/mapfiles/ms/icons/red-dot.png"
        :position="land"
        :draggable="false"
      >
      </GMapMarker>

      <GMapMarker 
          v-if="layers[2].isChecked"
          v-for="land in flood"
          :key="3"
          icon="http://maps.google.com/mapfiles/ms/icons/green-dot.png"
          :position="land"
          :draggable="false"
        >
      </GMapMarker>

      <GMapMarker 
          v-if="layers[3].isChecked"
          v-for="land in wildfire"
          :key="4"
          icon="http://maps.google.com/mapfiles/ms/icons/purple-dot.png"
          :position="land"
          :draggable="false"
        >
      </GMapMarker>
    </GMapMap>

    <HierarchyLayers :layers="layers" :check="check"/>
</template>

<script setup>
    import HierarchyLayers from '../components/HierarchyLayers.vue';
    import { ref } from 'vue';

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

    let landSlide = ref([
      { lat: 46.8219, lng: 8.2275 },
      { lat: 51.2394, lng: 3.8085 },
      { lat: 42.5678, lng: 13.3676 },
      { lat: 48.9123, lng: 16.4390 },
      { lat: 37.8912, lng: -5.9987 },
      { lat: 54.6842, lng: -2.9874 },
    ]);

    let flood = ref([
      { lat: 38.9072, lng: -77.0370 },
      { lat: 51.5099, lng: -0.1180 },
      { lat: 52.5200, lng: 13.4050 },
      { lat: 48.8566, lng: 2.3522 },
      { lat: 40.7128, lng: -74.0060 },
      { lat: 34.0522, lng: -118.2437 },
    ]);

    let drought = ref([
      { lat: 40.7128, lng: -74.0060 },
      { lat: 48.8566, lng: 2.3522 },
      { lat: 51.1657, lng: 10.4515 },
      { lat: 41.9028, lng: 12.4964 },
      { lat: 45.9432, lng: 24.9668 },
      { lat: 53.3498, lng: -6.2603 },
    ]);

    let wildfire = ref([
      { lat: 37.7749, lng: -122.4194 },
      { lat: -33.8688, lng: 151.2093 },
      { lat: 48.8566, lng: 2.3522 },
      { lat: -37.8136, lng: 144.9631 },
      { lat: 34.0522, lng: -118.2437 },
      { lat: 40.7128, lng: -74.0060 },
    ]);

</script>