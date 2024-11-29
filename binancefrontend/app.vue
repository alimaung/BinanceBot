<template>
  <div>
    <header>
      <nav>
        <ul>
          <li><NuxtLink to="/bots">Trading Bots</NuxtLink></li>
        </ul>
      </nav>
    </header>

    <main>
      <NuxtPage />  <!-- This will load the current page -->
    </main>

    <footer>
      <p>&copy; 2024 My Trading Bot App</p>
    </footer>
  </div>
</template>

<script setup>
  // No need for any setup logic here unless you have global data
</script>

<style scoped>
  /* Basic styles for header and footer navigation */
  header {
    background-color: #333;
    color: white;
    padding: 1rem;
  }

  header nav ul {
    list-style: none;
    display: flex;
  }

  header nav ul li {
    margin-right: 20px;
  }

  header nav ul li a {
    color: white;
    text-decoration: none;
  }

  footer {
    text-align: center;
    margin-top: 20px;
    padding: 1rem;
    background-color: #333;
    color: white;
  }
</style>
