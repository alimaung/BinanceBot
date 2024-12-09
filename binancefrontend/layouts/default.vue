<template>
  <v-app :class="colorClass">
    <!-- Navigation Drawer -->
    <v-navigation-drawer
      permanent
      expand-on-hover
      rail
      rail-width="70"
      location="left"
      app
      class="navbar"
    >
      <v-list-item 
        prepend-icon="mdi-menu" 
        style="height: 64px; 
        margin-left: 6px;"
      >
      </v-list-item>

      <v-list-item
        style="height: 60px; margin-left: 6px;"
        prepend-avatar="https://randomuser.me/api/portraits/women/68.jpg"
        title="John Leider"
        link to="/users"
      >
      </v-list-item>

      <v-list 
        class="elements" 
        density="compact" 
        nav
      >

        <v-divider></v-divider>

        <v-list-item prepend-icon="mdi-cogs" title="Strategy Settings" value="strategy-settings" link to="/strategy-settings"></v-list-item>
        <v-list-item prepend-icon="mdi-currency-usd" title="Account Balance" value="account-balance" link to="/account-balance"></v-list-item>
        <v-list-item prepend-icon="mdi-chart-line" title="Tradingview Chart" value="tvchart" link to="/tvchart"></v-list-item>
        <v-list-item prepend-icon="mdi-alarm-check" title="Trade Alerts" value="trade-alerts" link to="/trade-alerts"></v-list-item>
        <v-list-item prepend-icon="mdi-bell-ring" title="Notification Settings" value="notification-settings" link to="/notification-settings"></v-list-item>
        <v-list-item prepend-icon="mdi-play-circle" title="Start Trading" value="start-trading" link to="/start-trading"></v-list-item>
        <v-list-item prepend-icon="mdi-stop-circle" title="Stop Trading" value="stop-trading" link to="/stop-trading"></v-list-item>
        <v-list-item prepend-icon="mdi-clock-outline" title="Trade History" value="trade-history" link to="/trade-history"></v-list-item>
        <v-list-item prepend-icon="mdi-chart-box" title="Portfolio Overview" value="portfolio-overview" link to="/portfolio-overview"></v-list-item>
        <v-list-item prepend-icon="mdi-clipboard-text" title="Transaction Logs" value="transaction-logs" link to="/transaction-logs"></v-list-item>
        <v-list-item prepend-icon="mdi-book-open-page-variant" title="Documentation" value="documentation" link to="/documentation"></v-list-item>
        <v-list-item prepend-icon="mdi-server" title="API Settings" value="api-settings" link to="/api-settings"></v-list-item>
        <v-list-item prepend-icon="mdi-palette" title="Theme Settings" value="theme-settings" link to="/theme-settings"></v-list-item>
        <v-list-item prepend-icon="mdi-logout" title="Logout" value="logout" link to="/logout"></v-list-item>
      </v-list>
  
    </v-navigation-drawer>
    
    <!-- App Bar -->
    <v-app-bar 
      app 
      scroll-behavior="hide"
      color= #EAF1FB
    >
      <v-app-bar-title>BinanceBot</v-app-bar-title>
      <template v-slot:append>
        <v-btn icon="mdi-magnify"></v-btn>
        <v-btn icon="mdi-cog"></v-btn>
        <v-btn icon="mdi-account"></v-btn>
      </template>
    </v-app-bar>
  
    <!-- Content -->
    <v-main>
      <nuxt-page />
    </v-main>

    <!-- Bottom Navigation -->
    <v-layout>
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
    </v-layout>

    <!-- Footer -->
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

  </v-app>
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

<style scoped>
.navbar {
  background: #EAF1FB;
  width: 70px;
  border: none !important; /* Removes the border */
  box-shadow: none; /* Removes any shadow if present */
  color: #041E49;
  
}

.elements {
  padding-top: 8px;
  margin-left: 6px;
  color: #041E49;
}
</style>
