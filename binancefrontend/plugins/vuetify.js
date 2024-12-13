// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css'
import 'material-symbols';

import { createVuetify } from 'vuetify'
import colors from 'vuetify/util/colors'

const myCustomLightTheme = {
  dark: false,
  colors: {
    background: '#FFFFFF',
    surface: '#FFFFFF',
    'surface-bright': '#FFFFFF',
    'surface-light': '#EEEEEE',
    'surface-variant': '#424242',
    'on-surface-variant': '#EEEEEE',
    primary: '#1867C0',
    'primary-darken-1': '#1F5592',
    secondary: '#48A9A6',
    'secondary-darken-1': '#018786',
    error: '#B00020',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
  },
  variables: {
    'border-color': '#000000',
    'border-opacity': 0.12,
    'high-emphasis-opacity': 0.87,
    'medium-emphasis-opacity': 0.60,
    'disabled-opacity': 0.38,
    'idle-opacity': 0.04,
    'hover-opacity': 0.04,
    'focus-opacity': 0.12,
    'selected-opacity': 0.08,
    'activated-opacity': 0.12,
    'pressed-opacity': 0.12,
    'dragged-opacity': 0.08,
    'theme-kbd': '#212529',
    'theme-on-kbd': '#FFFFFF',
    'theme-code': '#F5F5F5',
    'theme-on-code': '#000000',
  }
}

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    theme: {
      defaultTheme: 'dark',
      themes: {
        themeone: {
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
        themetwo: {
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
        light: {
          dark: false,
          colors: {
            primary: '#1976D2',
            secondary: '#424242',
            background: '#ffffff',
            surface: '#f5f5f5',
            accent: '#FF4081',  // Custom accent color for light theme
          },
        },
        dark: {
          dark: true,
          colors: {
            primary: '#90CAF9',
            secondary: '#757575',
            background: '#121212',
            surface: '#1d1d1d',
            accent: '#FF4081',  // Custom accent color for dark theme
          },
        },
        myCustomLightTheme,
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