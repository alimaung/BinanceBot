// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css'
import 'material-symbols';

import { createVuetify } from 'vuetify'
import GoogleSignInPlugin from "vue3-google-signin"
import colors from 'vuetify/util/colors'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    theme: {
      themes: {
        light: {
          dark: true,
          colors: {
            primary: "#FCD535",
            secondary: colors.green.lighten4,
            accent: colors.indigo.base,
            error: colors.red.accent3,
            dark: "#181A20",
            light: "#FFFFFF",
            text: "#1E2329",
            active_nav: "#2B3139",
            border: "#FCD535",
            active_btn: "#CFAF30",
            dark_font: "#EAECEF",
            dark_inactive_nav_font: "#848E9C",
          },
        },
      },
    },
    defaults: {
      global: {
        style: {
          fontFamily: 'Binance PLEX, sans-serif',
        },
      },
    },
  });

  app.vueApp.use(vuetify);
});