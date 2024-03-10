<script setup>
import Paginator from './components/Paginator.vue'
import FoodItem from './components/FoodItem.vue'
import Dialog from './components/Dialog.vue'
import { ref, onMounted, watch } from 'vue'
import {} from './style.css'

const foodItems = ref([])
const page = ref(1)
const size = ref(10)
const foodName = ref('')
const backendUrl = import.meta.env.VITE_BACKEND_URL ? import.meta.env.VITE_BACKEND_URL : 'http://0.0.0.0:8000';
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
  <div class="w-full flex flex-col justify-center items-center">
    <span class="mb-3 font-medium text-2xl">Search</span>
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
