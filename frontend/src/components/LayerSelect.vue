
<template>
    <div class="w-full flex py-3 duration-100 px-6 hover:bg-gray-500 cursor-pointer" @click="props.check(props.layer.id)">

        <div v-if="!props.layer.isChecked" class="w-[20%] border-2 duration-100 border-gray-500"></div>
        <div v-if="props.layer.isChecked" class="w-[20%]" :class="props.layer.color"></div>

        <div class="w-full h-full flex items-end justify-end">
           <h1 class="uppercase">{{props.layer.name}}</h1> 
        </div>
    </div>
</template>

<script setup>
    const props = defineProps({
        layer: {
            name: String,
            isChecked: Boolean,
            color: String 
        },
        check: Function,
    })
</script>