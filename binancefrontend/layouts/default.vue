<template>
  <v-app>    
    <!-- Navigation Drawer -->
    <!-- <NavDrawer /> -->

    <!-- App Bar -->
    <AppBar />

    
    <!-- Content -->
    <v-main>
      <nuxt-page />
    </v-main>

    <!-- Footer -->
    <v-footer style="padding: 70px; height: 100px;">
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

  </v-app>
</template>
  
<script>
export default {
  
  data() {
    return {
      dialog: false,
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

<style scoped>
.navbar {
  border: none !important; /* Removes the border */
  box-shadow: none; /* Removes any shadow if present */
  
  
}

.material-symbols-outlined {
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 48;
}

.custom-dialog {
  border-radius: 0px;
}

.login-card {
  width: 100%;
  max-width: 450px;
  margin: 40px auto;
  border-radius: 16px;
}
</style>
