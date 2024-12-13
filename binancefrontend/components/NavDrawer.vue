<template> 
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

        <v-list-item prepend-icon="mdi-chart-line" title="Tradingview Chart" value="tvchart" link to="/tvchart"></v-list-item>
        <v-list-item prepend-icon="mdi-cogs" title="Strategy Settings" value="strategy-settings" link to="/strategy-settings"></v-list-item>
        <v-list-item prepend-icon="mdi-currency-usd" title="Account Balance" value="account-balance" link to="/account-balance"></v-list-item>
        <v-list-item prepend-icon="mdi-alarm-check" title="Trade Alerts" value="trade-alerts" link to="/trade-alerts"></v-list-item>
        <v-list-item prepend-icon="mdi-bell-ring" title="Notification Settings" value="notification-settings" link to="/notification-settings"></v-list-item>
        <v-list-item prepend-icon="mdi-android" title="Bots Overview" value="bots-overview" link to="/bots-overview"></v-list-item>

        <v-list-item prepend-icon="mdi-logout" title="Logout" value="logout" link to="/logout"></v-list-item>
      </v-list>
  
    </v-navigation-drawer>
    
</template>

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