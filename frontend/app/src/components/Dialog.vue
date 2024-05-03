<script setup>
import { ref, watch } from "vue";
import {onClickOutside} from '@vueuse/core'

const props = defineProps({
  isOpen: Boolean,
  food: Object,
  noEdit: Boolean,
  add: Boolean
})

const emptyFoodObject = {
  'calcium_mg': 0.0,
  'carb_g': 0.0,
  'copper_mcg': 0.0,
  'descrip': "New product",
  'energy_kcal': 0.0,
  'fat_g': 0.0,
  'fiber_g': 0.0,
  'folate_mcg': 0.0,
  'iron_mg': 0.0,
  'magnesium_mg': 0.0,
  'manganese_mg': 0.0,
  'ndb_no': null,
  'niacin_mg': 0.0,
  'phosphorus_mg': 0.0,
  'potassium_mg': 0.0,
  'protein_g': 0.0,
  'riboflavin_mg': 0.0,
  'saturated_fats_g': 0.0,
  'selenium_mcg': 0.0,
  'sodium_mg': 0.0,
  'sugar_g': 0.0,
  'thiamin_mg': 0.0,
  'vita_mcg': 0.0,
  'vitb6_mg': 0.0,
  'vitb12_mcg': 0.0,
  'vitc_mg': 0.0,
  'vitd2_mcg': 0.0,
  'vite_mg': 0.0,
  'zinc_mg': 0.0
}

const backendUrl = import.meta.env.VITE_BACKEND_URL ? import.meta.env.VITE_BACKEND_URL : 'http://0.0.0.0:8000';
const emit = defineEmits(["modal-close"])

const target = ref(null)
onClickOutside(target, ()=>emit('modal-close'))

const getFoodLabels = () => {
    return Object.entries(props.food).filter((item) => item[0] !== "descrip" && item[0] !== "ndb_no" && item[0] !== "nutrient_score")
}

const editMode = ref(false)
const editData = ref(emptyFoodObject)
const editFood = async () => {
    let response = await fetch(`${backendUrl}/object/${editData.value.ndb_no}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(editData.value)
    })
    editMode.value = false
    emit('modal-close')
}

const addFood = async () => {
    let response = await fetch(`${backendUrl}/object/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(editData.value)
    })
    editMode.value = false
    emit('modal-close')
}

watch(() => editMode.value, (newValue) => {
  editData.value = props.food
})

</script>

<template>
  <div v-if="isOpen" class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container bg-slate-600 rounded p-3 relative" ref="target">
        <div class="modal-header font-bold text-xl mb-2 flex justify-center gap-3">
            <div class="font-normal absolute left-0 top-0 bg-slate-800 p-1 rounded-tl-sm">{{ food.ndb_no }}</div>
            <div class="font-bold capitalize" v-if="!editMode && !add">{{ food.descrip }}</div>
            <input type="text" v-else v-model="editData.descrip" class="px-1">
            <div v-if="food.nutrient_score === undefined && !add" class="flex font-normal text-sm gap-1 items-center absolute right-0 top-0 p-2 bg-slate-800 rounded-tr-sm">
                <label for="edit" class="select-none">Edit</label>
                <input type="checkbox" name="edit" id="edit" v-model="editMode">
            </div>
        </div>
        <div class="modal-body mb-2">
          <div class="columns-3 gap-3">
            <div class="columns-2 gap-2 mb-1" v-for="[label, value] in getFoodLabels()" :key="label">
                <div class="capitalize text-left font-bold">{{ label }}</div>
                <div class="text-right" v-if="!editMode && !add">{{ Math.round((value + Number.EPSILON) * 100) / 100 }}</div>
                <div v-else class="flex justify-end">
                    <input type="number" :name="label" v-model="editData[label]" :id="label" class="w-[60%] rounded px-1">
                </div>
            </div>
            
          </div>
          <div v-if="food.nutrient_score !== undefined" class="flex justify-center space-x-3 mt-3">
            <div class="font-bold">Nutrient Score</div>
            <div>
              {{ Math.round((food.nutrient_score + Number.EPSILON) * 100) / 100 }}
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <slot name="footer">
            <div v-if="food.nutrient_score === undefined">
              <button v-if="!add" :disabled="!editMode || !!noEdit" @click.stop="editFood()">Save edit</button>
              <button v-else :disabled="!add" @click.stop="addFood()">Add +</button>
            </div>
          </slot>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-container {
  width: 80%;
  margin: 35vh auto;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
}

</style>