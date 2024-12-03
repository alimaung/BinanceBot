<template>
    <div>
      <h3>Live Market Data</h3>
      <div>
        <label for="symbol">Trading Pair:</label>
        <input v-model="symbol" id="symbol" type="text" placeholder="e.g., BTCUSDC" />
        <button @click="subscribeToMarketData">Subscribe</button>
      </div>
      <div v-if="price">
        <p>Current Price of {{ symbol }}: {{ price }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import io from 'socket.io-client';
  
  export default {
    data() {
      return {
        symbol: 'BTCUSDC',  // Default symbol
        price: null,
        socket: null,
      };
    },
    methods: {
      subscribeToMarketData() {
        if (this.socket) {
          this.socket.disconnect();
        }
        // Connect to the WebSocket server
        this.socket = io('ws://127.0.0.1:8000/ws/binance/');
        this.socket.on('connect', () => {
          console.log('Connected to WebSocket');
          this.socket.emit('subscribe', { symbol: this.symbol });
        });
        this.socket.on('price', (data) => {
          this.price = data.price;
        });
      }
    },
  };
  </script>
  