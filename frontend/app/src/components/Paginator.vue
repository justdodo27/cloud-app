<script setup>
const emit = defineEmits(['sizeChange', 'next', 'prev'])

defineProps({
  page: Number,
  size: Number,
})

function onSizeChange(event) {
    emit('sizeChange', parseInt(event.target.value))
}
</script>

<template>
    <div class="flex w-full justify-center mt-10">
        <button v-if="page > 1" @click="emit('prev')"><</button>
        <div class="p-4 bg-slate-700 rounded mx-2">{{ page }}</div>
        <button @click="emit('next')">></button>
        <select name="" id="" class="rounded ml-5 pl-3" @change="onSizeChange">
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="100">100</option>
            <option value="200">200</option>>
            <option value="1000">1000</option>
            <option value="">All</option>
        </select>
    </div>
</template>

<style scoped>
</style>