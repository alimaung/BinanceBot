<template>
  <v-card class="pa-4">
    <v-card-text>
      <v-row>
        <v-col>
          <v-btn color="primary" @click="addBox">Add Box</v-btn>
        </v-col>
        <v-col>
          <v-btn color="error" @click="removeBox" :disabled="boxes.length <= 1">Remove Box</v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>

  <v-card class="boxes-container pa-4">
    <v-card 
      v-for="(box, index) in boxes" 
      :key="index" 
      class="box-card"
    >
      Box {{ index + 1 }}
    </v-card>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'

// Reactive array to store boxes
const boxes = ref([
  { id: 1 },
  { id: 2 },
  { id: 3 },
  { id: 4 }
])

// Method to add a new box
const addBox = () => {
  // Limit the number of boxes to 10
    boxes.value.push({ id: boxes.value.length + 1 })
}

// Method to remove the last box
const removeBox = () => {
  if (boxes.value.length > 1) {
    boxes.value.pop()
  }
}
</script>
  
<style scoped>
.pa-4 {
  margin: auto;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  margin: 16px;
  background-color: aliceblue;
}

.boxes-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  align-items: center;
}

.box-card {
  background-color: azure;
  text-align: center;
  border: 1px solid #ddd;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
  width: 100px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 0;
  flex-shrink: 0;
}

.box-card:hover {
  transform: scale(1.05);
  background-color: rgba(231, 252, 252, 0.562);
}
</style>