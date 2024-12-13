<template>
    <v-dialog v-model="dialog" max-width="500" persistent>
      <template #activator="{ props }">
        <!-- Optional activator button, you can remove this -->
        <v-btn v-bind="props" color="primary" @click="openDialog">
          Open Login
        </v-btn>
      </template>
  
      <v-card class="login-card elevation-4">
        <v-card-text class="login-header text-center">
          <span class="material-symbols-outlined">chart_data</span>
          <h1 class="login-title text-h5 mt-3 mb-2">Welcome Back!</h1>
          <p class="login-subtitle text-body-2 text-medium-emphasis">
            Please log in to access your dashboard
          </p>
        </v-card-text>
  
        <v-form 
          class="login-form px-4 pb-4 ml-5 mr-5"
          @submit.prevent="handleLogin"
        >
          <v-text-field
            v-model="email"
            label="Email"
            type="email"
            variant="outlined"
            :rules="[rules.required, rules.email]"
            class="mb-2"
          ></v-text-field>
  
          <v-text-field
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            label="Password"
            variant="outlined"
            :rules="[rules.required]"
            class="mb-2"
          >
            <template #append-inner>
              <v-btn
                icon
                variant="text"
                size="small"
                @click="togglePasswordVisibility"
              >
                <v-icon>
                  {{ showPassword ? 'mdi-eye-off' : 'mdi-eye' }}
                </v-icon>
              </v-btn>
            </template>
          </v-text-field>
  
          <div class="login-actions d-flex justify-space-between align-center my-4">
            <v-checkbox label="Remember me" density="compact" hide-details />
            <v-btn 
              variant="text" 
              color="primary"
              @click="$router.push('/forgot-password')"
            >
              Forgot Password?
            </v-btn>
          </div>
  
          <v-btn 
            type="submit"
            block 
            color="primary" 
            size="large" 
            class="login-submit-btn mb-4"
          >
            Login
          </v-btn>
  
          <v-divider class="my-4">
            <span class="text-body-2 text-medium-emphasis px-3 bg-white">
              Or continue with
            </span>
          </v-divider>
  
          <div class="text-center mt-3 mb-2">
            <GoogleSignInButton
              @success="handleLoginSuccess"
              @error="handleLoginError"
            ></GoogleSignInButton>
          </div>
        </v-form>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { 
    GoogleSignInButton, 
    type CredentialResponse 
  } from "vue3-google-signin";
  
  const dialog = ref(false);
  const email = ref('');
  const password = ref('');
  const showPassword = ref(false);
  
  const rules = {
    required: (v: string | null | undefined) => !!v || 'This field is required',
    email: (v: string | null | undefined) => 
      /.+@.+\..+/.test(v || '') || 'Please enter a valid email address',
  };
  
  const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
  };
  
  const handleLogin = () => {
    console.log('Login attempted', { email: email.value, password: password.value });
  };
  
  const handleLoginSuccess = (response: CredentialResponse) => {
    console.log("Google Sign-In Successful", response.credential);
  };
  
  const handleLoginError = () => {
    console.error("Google Sign-In Failed");
  };
  
  const openDialog = () => {
    dialog.value = true;
  };
  </script>
  
  <style scoped>
  .material-symbols-outlined {
    font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 48;
    font-size: 120px;
  }
  
  .login-card {
    border-radius: 16px;
  }
  
  .login-title {
    color: #333;
    font-weight: 600;
  }
  
  .login-submit-btn {
    text-transform: none;
    font-weight: 600;
  }
  </style>
  