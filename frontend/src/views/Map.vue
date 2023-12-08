
<template>
    <GMapMap
      :center="{ lat: 45.00, lng: 0.1276 }"
      :zoom="5" 
      class="w-screen h-screen absolute top-0 left-0 z-[-1]"
      map-type-id="terrain" 
      :options="{
        disableDefaultUI: true,
      }"
    />

    <HierarchyLayers />
</template>

<script setup>
    import HierarchyLayers from '../components/HierarchyLayers.vue';
</script>