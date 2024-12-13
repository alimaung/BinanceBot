<template>
    <v-footer :class="colorClass" style="padding-bottom: 70px;">
      <v-row 
        justify="center" 
        no-gutters
      >
        <v-btn
          v-for="link in links"
          :key="link"
          class="mx-2"
          color="white"
          rounded="xl"
          variant="text"
        >
          {{ link }}
        </v-btn>
        <v-col class="text-center mt-4" cols="12">
          {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
        </v-col>
      </v-row>
    </v-footer>

</template>

<script>
  export default {
    data() {
      return {
        rail: true, // Initially in collapsed (icons-only) mode
        value: 0,   // Tracks the selected bottom navigation item
        links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Blog',
        'Contact Us',
      ],
      };
    },

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