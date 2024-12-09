// nuxt.config.ts
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'


export default defineNuxtConfig({
  // No proxy needed
  build: {
    transpile: ['vuetify'],
  },

  devtools: { enabled: true },

  compatibilityDate: '2024-11-01',

  css: ['vuetify/styles'],

  modules: [
    'nuxt-tradingview',

    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },

  ],

  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
})