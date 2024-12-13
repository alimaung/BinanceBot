<template>
  <v-card class="pa-4 ma-4" style="border-radius:12px">
    <div class="container">
      <h2>Trading Bots</h2>
      <div v-if="loading">Loading...</div>
      <div v-if="bots.length">
        <ul>
          <li v-for="bot in bots" :key="bot.id">
            {{ bot.name }} - {{ bot.trading_pair }} - {{ bot.is_active ? 'Active' : 'Inactive' }}
          </li>
        </ul>
      </div>
      <div v-else>
        <p>No bots found.</p>
      </div>
    </div>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const bots = ref([])
const loading = ref(true)

const fetchBots = async () => {
  try {
    const response = await $fetch('http://127.0.0.1:8000/api/bots/')
    console.log('Fetched bots:', response)
    bots.value = response
  } catch (error) {
    console.error('Error fetching bots:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchBots()
})
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Binance PLEX;
}
</style>