<script setup>
import Paginator from './components/Paginator.vue'
import FoodItem from './components/FoodItem.vue'
import { ref, onMounted, watch } from 'vue'
import {} from './style.css'

const foodItems = ref([])
const page = ref(1)
const size = ref(10)
const foodName = ref('')
const backendUrl = import.meta.env.VITE_BACKEND_URL ? import.meta.env.VITE_BACKEND_URL : 'http://0.0.0.0:8000';

onMounted(async () => {
  let response = await fetch(`${backendUrl}/objects/?skip=${page.value - 1}&limit=${size.value}`)
  foodItems.value = await response.json()
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
  <div class="w-full flex flex-col justify-center">
    <span class="mr-3">Search</span>
    <input type="text" v-model="foodName" class="p-2 mb-10">
    <div class="flex flex-wrap justify-center w-full">
      <FoodItem :food="food" v-for="food in foodItems" :key="food.ndb_no" />
    </div>
    <Paginator :page="page" :size="size" @sizeChange="(value) => size = value" @next="page++" @prev="page--"/>
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
</style>
