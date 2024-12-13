// nuxt.config.ts
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  build: {
    transpile: ['vuetify'],
  },

  devtools: { enabled: true },

  compatibilityDate: '2024-11-01',

  css: ['vuetify/styles', '~/assets/css/fonts.css'],

  modules: [
    'nuxt-tradingview',
    'nuxt-vue3-google-signin',
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
    '@nuxtjs/i18n',
    'nuxt-tiptap-editor'
  ],

  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },

  googleSignIn: {
    clientId: process.env.GOOGLE_CLIENT_ID
  },

  i18n: {
    vueI18n: './i18n.config.ts',
    locales: [
      { code: 'en', iso: 'en-US', name: 'English', file: 'en.json' },
      { code: 'de', iso: 'de-DE', name: 'Deutsch', file: 'de.json' },
    ],
    defaultLocale: 'en',
    strategy: 'prefix',
  },

  tiptap: {
    prefix: 'Tiptap', //prefix for Tiptap imports, composables not included
  },

})