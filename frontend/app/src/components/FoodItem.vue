<script setup>
import { ref } from 'vue'

defineProps({
  food: Object,
})

/*
calcium_mg
: 
24
carb_g
: 
0.06
copper_mcg
: 
0
descrip
: 
"butter with salt"
energy_kcal
: 
717
fat_g
: 
81.11
fiber_g
: 
0
folate_mcg
: 
3
iron_mg
: 
0.02
magnesium_mg
: 
2
manganese_mg
: 
0
ndb_no
: 
"1001"
niacin_mg
: 
0.042
phosphorus_mg
: 
24
potassium_mg
: 
24
protein_g
: 
0.85
riboflavin_mg
: 
0.034
saturated_fats_g
: 
51.368
selenium_mcg
: 
1
sodium_mg
: 
643
sugar_g
: 
0.06
thiamin_mg
: 
0.005
vita_mcg
: 
684
vitb6_mg
: 
0.003
vitb12_mcg
: 
0.17
vitc_mg
: 
0
vitd2_mcg
: 
0
vite_mg
: 
2.32
zinc_mg
: 
0.09
*/
</script>

<template>
  <div class="bg-slate-500 p-1 m-2 w-1/4 max-h-20">
    <div class="font-bold capitalize truncate h-1/2">{{ food.descrip }}</div>
    <div class="flex">
        <div>{{ Math.round(food.energy_kcal) }}kcal</div>
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
