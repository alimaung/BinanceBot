<template>
      <v-bottom-navigation
        v-model="value"
        :class="colorClass"
        mode="shift"
        style="position: fixed; bottom: 0; left: 0; right: 0; z-index: 10;"
      >
        <v-btn>
          <v-icon>mdi-television-play</v-icon>
          <span>Video</span>
        </v-btn>
        <v-btn>
          <v-icon>mdi-music-note</v-icon>
          <span>Music</span>
        </v-btn>
        <v-btn>
          <v-icon>mdi-book</v-icon>
          <span>Book</span>
        </v-btn>
        <v-btn>
          <v-icon>mdi-image</v-icon>
          <span>Image</span>
        </v-btn>
      </v-bottom-navigation>
</template>

<script>
  export default {
    

    computed: {
      color() {
        switch (this.value) {
          case 0: return 'blue-grey';
          case 1: return 'teal';
          case 2: return 'brown';
          case 3: return 'indigo';
          default: return 'grey';
        }
      },

      colorClass() {
        return `bg-${this.color}`; // Generates Vuetify color class
      },
    },
  };
</script>

<style scoped>

</style>
