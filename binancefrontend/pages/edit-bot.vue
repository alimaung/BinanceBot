<template>
    <div>
      <h1>Edit Bot: {{ bot.name }}</h1>
      <form @submit.prevent="updateBot">
        <label for="name">Bot Name:</label>
        <input v-model="bot.name" id="name" type="text" required />
  
        <label for="trading_pair">Trading Pair:</label>
        <input v-model="bot.trading_pair" id="trading_pair" type="text" required />
  
        <label for="strategy">Strategy:</label>
        <input v-model="bot.strategy" id="strategy" type="text" required />
  
        <label for="is_active">Active:</label>
        <input type="checkbox" v-model="bot.is_active" id="is_active" />
  
        <button type="submit">Update Bot</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  // Bot data
  const bot = ref({
    id: null,
    name: '',
    trading_pair: '',
    strategy: '',
    is_active: true,
  })
  
  // Fetch the bot details
  const fetchBot = async (id) => {
    try {
      // Use `useFetch` to fetch the bot data from the backend
      const { data, error } = await useFetch(`http://127.0.0.1:8000/api/bots/${id}/`)
  
      if (error.value) {
        console.error('Error fetching bot data:', error.value)
      } else {
        bot.value = data.value  // Store the fetched bot data
      }
    } catch (err) {
      console.error('Error fetching bot data:', err)
    }
  }
  
  // Update bot details
  const updateBot = async () => {
    try {
      // Use `useFetch` to send a PUT request for updating the bot
      const { data, error } = await useFetch(`http://127.0.0.1:8000/api/bots/${bot.value.id}/`, {
        method: 'PUT',
        body: bot.value,  // Send the updated bot data
      })
  
      if (error.value) {
        console.error('Error updating bot:', error.value)
        alert('Failed to update bot')
      } else {
        alert('Bot updated successfully!')
        // Redirect to bots list after successful update
        useRouter().push('/')
      }
    } catch (err) {
      console.error('Error updating bot:', err)
      alert('Failed to update bot')
    }
  }
  
  // Fetch the bot data when the component is mounted
  onMounted(() => {
    const botId = useRoute().params.id  // Get the bot ID from the route params
    fetchBot(botId)
  })
  </script>
  