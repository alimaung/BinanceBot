// nuxt.config.ts
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  // No proxy needed
  build: {
    transpile: ['vuetify'],
  },

  devtools: { enabled: true },

  compatibilityDate: '2024-11-01',

  css: ['vuetify/styles', '~/assets/css/fonts.css'],

  modules: [
    'nuxt-tradingview',
    'nuxt-vue3-google-signin',
    '@nuxtjs/i18n',

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

  googleSignIn: {
    clientId: '109310560315-e3281h1uk9ar3iqoev0mknkskd40dpph.apps.googleusercontent.com',
  },
  i18n: {
    vueI18n: './i18n.config.ts',
    locales: [
      { code: 'en', iso: 'en-US', name: 'English', file: 'en.json' },
      { code: 'de', iso: 'de-DE', name: 'Deutsch', file: 'de.json' },
    ], // used in URL path prefix
    defaultLocale: 'en', // default locale of your project for Nuxt pages and routings
    strategy: 'prefix',
  }
})