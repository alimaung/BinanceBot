<template>
    <v-app-bar 
      app 
      scroll-behavior="hide"
      class="pl-6 pr-6"
    >
    <template v-slot:prepend>
      <div link to="/">
        <img src="~/public/img/logo.png" class="logo">
      </div>
    </template>

    <template v-slot:default>
    <div class="app-bar">
        <v-btn 
            class= "app-bar-btn" 
            variant="text"
            link to="/tvchart"
            >Markets
        </v-btn>
        <v-menu
            open-on-hover
            v-model="menuOpen"
            >
            <template v-slot:activator="{ props }">
                <v-btn
                class= "app-bar-btn" 
                variant="text"
                v-bind="props"
                >Trade
                <span class="material-symbols-rounded">{{ menuOpen ? 'arrow_drop_up' : 'arrow_drop_down' }}</span>
                </v-btn>
            </template>

            <v-card class="menu-card" color="white">
                <div class="menu-items ma-3">
                        <v-row>
                                <v-card 
                                    width="100%"
                                    class= "bot-card" 
                                    color="blue ma-2" 
                                    prepend-icon="mdi-account"
                                    title="Manage Bots"
                                    subtitle="Edit and configure your trading bots"
                                    >
                                </v-card>
                        </v-row>
                        <v-row>
                                <v-card 
                                    width="100%"
                                    class= "bot-card" 
                                    color="red ma-2" 
                                    prepend-icon="mdi-account"
                                    title="Bot Status"
                                    subtitle="Monitor the status of your bots"
                                    >
                                </v-card>
                        </v-row>
                    </div>
            </v-card>
        </v-menu>


        <v-btn class= "app-bar-btn" variant="text" link to="/strategy-settings">Strategy</v-btn>
        <v-btn class= "app-bar-btn" variant="text" link to="/account" >Account</v-btn>
        <v-btn class= "app-bar-btn" variant="text" link to="/bots-overview" >API</v-btn>
        <v-btn class= "app-bar-btn" variant="text" link to="/docs" >Docs</v-btn>
        <v-btn class= "app-bar-btn" variant="text" link to="/template" >Settings</v-btn>  
    </div>
    
    </template> 

      <template v-slot:append>
        <v-btn icon="mdi-magnify"></v-btn>
        <v-btn icon="mdi-cog" link to="/settings"></v-btn>
        <v-btn icon="mdi-account" @click="dialog = true"></v-btn>
        <v-btn icon="mdi-wallet"></v-btn>
        <v-btn 
            icon="mdi-earth"
            ><v-menu
                open-on-hover
                v-model="localesOpen"
                >
                <template v-slot:activator="{ props }">
                    <span v-bind="props" class="material-symbols-rounded">globe</span>
                </template>

                <v-card class="menu-card" color="white">
                    <div class="menu-items ma-3">
                            <v-row>
                                    <v-card 
                                        width="100%"
                                        class= "bot-card" 
                                        color="blue ma-2" 
                                        prepend-icon="mdi-account"
                                        title="Manage Bots"
                                        subtitle="Edit and configure your trading bots"
                                        @click="setLocale('en')"
                                        >
                                    </v-card>
                            </v-row>
                            <v-row>
                                    <v-card 
                                        width="100%"
                                        class= "bot-card" 
                                        color="red ma-2" 
                                        prepend-icon="mdi-account"
                                        title="Bot Status"
                                        subtitle="Monitor the status of your bots"
                                        @click="setLocale('de')"
                                        >
                                    </v-card>
                            </v-row>
                        </div>
                </v-card>
            </v-menu>
        </v-btn>

        

        <v-btn @click="toggleTheme" icon>
            <v-icon>{{ darkMode ? 'mdi-white-balance-sunny' : 'mdi-moon-waning-crescent' }}</v-icon>
        </v-btn>
        <v-dialog
      v-model="dialog"
      width="auto"
      class="custom-dialog"
    >
      <login />
    </v-dialog>


      </template>
    </v-app-bar>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useTheme } from 'vuetify'

// Reactive state variables
const dialog = ref(false)
const menuOpen = ref(false)
const localesOpen = ref(false)

const theme = useTheme()

function toggleTheme () {
  theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
}

// Use the i18n API
const { setLocale } = useI18n()
</script>

<style scoped>
.logo {
  height: 64px;
  width: 120px;
  margin-right: 12px;
}

.app-bar {
    width: 100%;
    display: flex;
    justify-content: left;
    align-items: left;
}

.app-bar-btn {
  font-family: Binance PLEX;
  font-size: 14px;
  text-transform: none;
  padding-left: 12px;
  padding-right: 12px;
  height: 64px;
}

.app-bar-btn:hover {
  color: #F0B90B;
  text-decoration: none;
  cursor: pointer;
}

.menu-items {
  width: 300px;
  display: flex;
  flex-direction: column;
  
}

.bot-btn {
  font-family: Binance PLEX;
  font-size: 14px;
  text-transform: none;
  text-align: left;
}

:hover.v-btn {
  color: #F0B90B;
  text-decoration: none;
  cursor: pointer;
}


</style>