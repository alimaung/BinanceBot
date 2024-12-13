<template>
    <v-card class="pa-4 ma-4" style="border-radius:12px; height: 2000px;">
      <button class="button" @click="setLocale('en')">en</button>
      <button class="button" @click="setLocale('de')">de</button>
      <p>{{ $t('welcome') }}</p>
    </v-card>
  </template>
  
  <style scoped>
  v-card {
    max-width: 800px;
    margin: auto;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  }

  .button {
    background-color: #EAF1FB;
    color: #041E49;
    padding: 8px 16px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin: 8px;
  }
  </style>

<script setup>

const { setLocale } = useI18n()

</script>
  