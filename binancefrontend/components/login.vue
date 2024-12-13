<template>
    <v-card class="login-card elevation-4" border-radius="16px">
      <v-card-text class="login-header text-center">
        <span class="material-symbols-outlined">chart_data</span>
        
        <h1 class="login-title text-h5 mt-3 mb-2">
          Welcome Back!
        </h1>
        
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
          <v-checkbox
            label="Remember me"
            density="compact"
            hide-details
          ></v-checkbox>
  
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
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { 
    GoogleSignInButton, 
    type CredentialResponse 
  } from "vue3-google-signin";
  
  // State management
  const email = ref('');
  const password = ref('');
  const showPassword = ref(false);
  
  // Validation rules
  type ValidationRule = (value: string | null | undefined) => boolean | string;
  
  const rules: Record<string, ValidationRule> = {
    required: (v: string | null | undefined) => !!v || 'This field is required',
    email: (v: string | null | undefined) => 
      /.+@.+\..+/.test(v || '') || 'Please enter a valid email address',
    password: (v: string | null | undefined) =>
      (v && v.length >= 8) || 'Password must be at least 8 characters long'
  };
  
  // Password visibility toggle
  const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
  };
  
  // Login handlers
  const handleLogin = () => {
    // Implement login logic here
    // You might want to add form validation before submission
    console.log('Login attempted');
  };
  
  const handleLoginSuccess = (response: CredentialResponse) => {
    const { credential } = response;
    console.log("Google Sign-In Successful", credential);
    // Add your success handling logic
  };
  
  const handleLoginError = () => {
    console.error("Google Sign-In Failed");
    // Add your error handling logic
  };
  </script>
  
  <style scoped>
  .material-symbols-outlined {
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 48;
  font-size: 120px;
    }

  .login-card {
    width: 100%;
    max-width: 450px;
    margin: 40px auto;
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