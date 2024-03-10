<script setup>
import Paginator from './components/Paginator.vue'
import FoodItem from './components/FoodItem.vue'
import Dialog from './components/Dialog.vue'
import { ref, onMounted, watch } from 'vue'
import {} from './style.css'

const backendUrl = import.meta.env.VITE_BACKEND_URL ? import.meta.env.VITE_BACKEND_URL : 'http://0.0.0.0:8000';

const foodItems = ref([])
const page = ref(1)
const size = ref(10)
const foodName = ref('')

const foodStats = ref([])

const healthyList = ref([])
const healthyListPage = ref(1)
const healthyListSize = ref(10)

const showDialog = ref(false)
const activeFood = ref(null)

function closeDialog() {
  showDialog.value = false
}

function openDialog(food) {
  activeFood.value = food
  showDialog.value = true
}

const submitHandler = ()=>{
  //here you do whatever
}

onMounted(async () => {
  let response = await fetch(`${backendUrl}/objects/?skip=${page.value - 1}&limit=${size.value}`)
  foodItems.value = await response.json()

  let stats = await fetch(`${backendUrl}/stats/`)
  foodStats.value = await stats.json()

  let healthy = await fetch(`${backendUrl}/healthy-foods/?skip=${healthyListPage.value - 1}&limit=${healthyListSize.value}`)
  healthyList.value = await healthy.json()
  console.log(healthyList.value)
});

watch(() => size.value, async (newSize) => {
  let filter = `?`
  let search = `objects`

  if (foodName.value.length > 0) {
    search = `object`
    filter += `name=${foodName.value}&`
  }

  if (newSize) {
    filter += `skip=${(page.value-1) * newSize}&limit=${newSize}`
  }

  let response = await fetch(`${backendUrl}/${search}/${filter}`)
  foodItems.value = await response.json()
});

watch(() => page.value, async (newPage) => {
  let filter = `?`
  let search = `objects`

  if (foodName.value.length > 0) {
    search = `object`
    filter += `name=${foodName.value}&`
  }

  if (size.value) {
    filter += `skip=${(newPage-1) * size.value}&limit=${size.value}`
  }

  
  let response = await fetch(`${backendUrl}/${search}/${filter}`)
  foodItems.value = await response.json()
});

watch(() => healthyListSize.value, async (newSize) => {
  let filter = `?`
  let search = `healthy-foods`

  if (newSize) {
    filter += `skip=${(healthyListPage.value-1) * newSize}&limit=${newSize}`
  }

  let response = await fetch(`${backendUrl}/${search}/${filter}`)
  healthyList.value = await response.json()
});

watch(() => healthyListPage.value, async (newPage) => {
  let filter = `?`
  let search = `healthy-foods`

  if (healthyListSize.value) {
    filter += `skip=${(newPage-1) * healthyListSize.value}&limit=${healthyListSize.value}`
  }

  
  let response = await fetch(`${backendUrl}/${search}/${filter}`)
  healthyList.value = await response.json()
});

watch(() => foodName.value, async (newText) => {
  let filter = `?`
  let search = `objects`

  if (newText.length > 0) {
    search = `object`
    filter += `name=${newText}&`
  }

  if (size.value) {
    filter += `skip=${(page.value-1) * size.value}&limit=${size.value}`
  }

  
  let response = await fetch(`${backendUrl}/${search}/${filter}`)
  foodItems.value = await response.json();
});
</script>

<template>
  <nav class="w-full fixed bg-slate-800 flex space-x-2 justify-center">
    <a href="#food_list" class="p-2 hover:text-slate-400 hover:cursor-pointer">Food List</a>
    <a href="#food_stats" class="p-2 hover:text-slate-400 hover:cursor-pointer">Food Statistics</a>
    <a href="#healthy_food_list" class="p-2 hover:text-slate-400 hover:cursor-pointer">Healthy Food List</a>
  </nav>
  <div class="w-full flex flex-col justify-center items-center p-6 mt-20" id="food_list">
    <span class="mb-3 font-medium text-3xl">Search Food List</span>
    <input type="text" v-model="foodName" class="p-2 mb-10 rounded w-1/2">
    <div class="w-full columns-2 gap-8">
      <FoodItem v-if="foodItems && foodItems.length > 0" :food="food" v-for="food in foodItems" :key="food.ndb_no" @click="openDialog(food)" />
    </div>
    <Transition name="fade">
      <div v-if="!(foodItems && foodItems.length > 0)" class="font-bold w-full">
        Food not found 😭
      </div>
    </Transition>
    <Transition name="fade">
      <Paginator v-if="foodItems && foodItems.length > 0" :page="page" :size="size" @sizeChange="(value) => size = value" @next="page++" @prev="page--"/>
    </Transition>
  </div>
  <Dialog :isOpen="showDialog" @modal-close="closeDialog" @submit="submitHandler" :food="activeFood" name="first-modal">
  </Dialog>
  <div class="w-full flex flex-col justify-center items-center p-6 mt-10" id="food_stats">
    <div class="font-bold text-3xl mb-4">Food Statistics</div>
    <div class="flex-col w-full">
      <div class="font-bold text-xl mb-4">
        Average nutrients
      </div>
      <div class="columns-2 bg-slate-500 p-3 mx-10 rounded">
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Energy kcal</div>
          <div>{{ Math.round((foodStats.average_nutrients?.energy_kcal + Number.EPSILON) * 100) / 100 }} kcal</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Proteins g</div>
          <div>{{ Math.round((foodStats.average_nutrients?.protein_g + Number.EPSILON) * 100) / 100 }} g</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Fats g</div>
          <div>{{ Math.round((foodStats.average_nutrients?.fat_g + Number.EPSILON) * 100) / 100 }} g</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Carbohydrates g</div>
          <div>{{  Math.round((foodStats.average_nutrients?.carb_g + Number.EPSILON) * 100) / 100 }} g</div>
        </div>
      </div>
    </div>

    <div class="flex-col w-full mt-10">
      <div class="font-bold text-xl mb-4">
        Minimal nutrients
      </div>
      <div class="columns-2 bg-slate-500 p-3 mx-10 rounded">
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Energy kcal</div>
          <div>{{ foodStats.min_nutrients?.energy_kcal }} kcal</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Proteins g</div>
          <div>{{ foodStats.min_nutrients?.protein_g }} g</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Fats g</div>
          <div>{{ foodStats.min_nutrients?.fat_g }} g</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Carbohydrates g</div>
          <div>{{ foodStats.min_nutrients?.carb_g }} g</div>
        </div>
      </div>
    </div>

    <div class="flex-col w-full mt-10">
      <div class="font-bold text-xl mb-4">
        Maximal nutrients
      </div>
      <div class="columns-2 bg-slate-500 p-3 mx-10 rounded">
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Energy kcal</div>
          <div>{{ foodStats.max_nutrients?.energy_kcal }} kcal</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Proteins g</div>
          <div>{{ foodStats.max_nutrients?.protein_g }} g</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Fats g</div>
          <div>{{ foodStats.max_nutrients?.fat_g }} g</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Carbohydrates g</div>
          <div>{{ foodStats.max_nutrients?.carb_g }} g</div>
        </div>
      </div>
    </div>

    <div class="flex-col w-full mt-10">
      <div class="font-bold text-xl mb-4">
        Energy density distribution
      </div>
      <div class="columns-2 bg-slate-500 p-3 mx-10 rounded">
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">High</div>
          <div>{{ foodStats.energy_density_distribution?.high }}</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Medium</div>
          <div>{{ foodStats.energy_density_distribution?.medium }}</div>
        </div>
        <div class="flex space-x-2 justify-between">
          <div class="font-bold">Low</div>
          <div>{{ foodStats.energy_density_distribution?.low }}</div>
        </div>
      </div>
    </div>
  </div>
  <div class="w-full flex flex-col justify-center items-center p-6 mt-10" id="food_stats">
    <div class="font-bold text-3xl mb-4" id="healthy_food_list">Healthy Food List</div>
    <div class="w-full columns-2 gap-8">
      <FoodItem v-if="healthyList && healthyList.length > 0" :food="food" v-for="food in healthyList" :key="food.ndb_no" @click="openDialog(food)" />
    </div>
    <Transition name="fade">
      <div v-if="!(healthyList && healthyList.length > 0)" class="font-bold w-full">
        Healthy food not found 😭
      </div>
    </Transition>
    <Transition name="fade">
      <Paginator v-if="healthyList && healthyList.length > 0" :page="healthyListPage" :size="healthyListSize" @sizeChange="(value) => healthyListSize = value" @next="healthyListPage++" @prev="healthyListPage--"/>
    </Transition>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
