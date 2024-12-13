<template>
    <div>
     <v-card class="pa-4 ma-4">
      <h1>{{ $t('djangoAPI') }}</h1>
      <div  v-if="pending">Loading...</div>
      <div v-else-if="error">Error: {{ error.message }}</div>
      <ul class="tex" v-else>
        <li v-for="(item, index) in data" :key="index">
          {{ item }}
        </li>
      </ul>
    </v-card>

    <v-card class="pa-4 ma-4">
        <span class="material-symbols-outlined">settings</span> <!-- Outlined -->
        <span class="material-symbols-rounded">settings</span>  <!-- Rounded -->
        <span class="material-symbols-sharp">settings</span>    <!-- Sharp -->
    </v-card>
    </div>
  </template>
  
  <script setup>
  const { data, pending, error } = useFetch('http://localhost:8000/test-binance/')

  const localePath = useLocalePath()
  </script>
  
<style scoped>

.pa-4 {
  max-width: 100%;
  margin: 10px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.tex {
  margin: 10px;
  padding: 10px;
}

.material-symbols-outlined {
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 48;
  font-size: 40px;
}

</style>