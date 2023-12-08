
<template>
    <GMapMap
      :center="{ lat: 45.00, lng: 0.1276 }"
      :zoom="5" 
      map-type-id="terrain" 
      style="width: 100vw; height: 100vh; position: absolute; left: 0; top: 0;"
      :options="{
        disableDefaultUI: true,
      }"
    />
</template>