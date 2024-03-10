<script setup>
import { ref } from 'vue'

defineProps({
  food: Object
})
</script>

<template>
  <div class="bg-slate-500 w-full max-h-20 rounded p-3 mb-3">
    <div class="font-bold capitalize truncate h-1/2">{{ food.descrip }}</div>
    <div class="flex justify-between">
        <div>{{ Math.round((food.energy_kcal + Number.EPSILON) * 100) / 100 }}kcal</div>
        <div v-if="food.nutrient_score !== undefined">Nutrient score: {{ Math.round((food.nutrient_score + Number.EPSILON) * 100) / 100 }}</div>
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
