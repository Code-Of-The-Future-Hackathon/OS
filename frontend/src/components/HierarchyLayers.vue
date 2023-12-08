
<template>
    <div class="w-[15%] h-screen bg-[#ffffff70] fixed">
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

    let layers = ref([
        {
            id: 0,
            name: 'rainfall',
            isChecked: true,
            color: 'bg-blue-500',
        },
        {
            id: 1,
            name: 'temperature',
            isChecked: true,
            color: 'bg-red-500',
        },
        {
            id: 2,
            name: 'wind',
            isChecked: true,
            color: 'bg-green-500'
        }
    ])

    const check = (layerIndex) => {
        layers.value[layerIndex].isChecked = !layers.value[layerIndex].isChecked
    }
</script>