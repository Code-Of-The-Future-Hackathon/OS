
<template>
    <div class="w-[15%] h-screen bg-[#ffffff70] duration-100 fixed">
        <div class="flex flex-col items-center">
            <LayerSelect
                v-for="layer in layers"
                :layer="layer"
                :check="check"
                :id="layer.id"
            />
        </div>
    </div>
</template>

<script setup>
    import LayerSelect from './LayerSelect.vue'
    import {ref} from 'vue'

    defineProps({
        layers: {
            type: Array,
            required: true
        },
        check: Function
    }) 
</script>