<template>
  <div class="pa-1">
    <div class="container">
      <v-card class="ma-1">
        <TickerTape :options="{
          colorTheme: 'dark',
          showSymbolLogo: true,
          isTransparent: false,
          displayMode: 'adaptive',
          locale: 'en',
          symbols: [
            {
              proName: 'BINANCE:BTCUSDT',
              title: 'Bitcoin/USDT',
            },
            {
              proName: 'BINANCE:BTCUSDC',
              title: 'Bitcoin/USDC',
            },
            {
              proName: 'SOLUSDT',
              title: 'Solarna/USDT',
            },
            {
              proName: 'ETHUSD',
              title: 'Ethereum/USD',
            },
            {
              proName: 'XRPUSD',
              title: 'Ripple/USD',
            },
          ],
        }"/>
      </v-card>

      <v-card class="ma-1 mt-2">
      <Chart :options="{
      width: '100%',
      height: '600',
      symbol: 'BINANCE:BTCUSDC',
      interval: '5',
      timezone: 'Europe/Berlin',
      theme: 'dark',
      style: '8',
      backgroundColor: '#0C0C0D',
      locale: 'en',
      enable_publishing: false,
      allow_symbol_change: false,
      withdateranges: true,
      hide_side_toolbar: false,
      details: false,
      hotlist: false,
      calendar: false,
      studies: [
        'STD;MA%1Cross', 
        'STD;RSI'
        ]
      }"/>
      </v-card>

      <!-- <CompanyProfile :options="{
        width: 400,
        height: 550,
        isTransparent: false,
        colorTheme: 'dark',
        symbol: 'NASDAQ:BBBY',
        locale: 'en',
      }"/> -->

      <!-- <CryptoHeatMap :options="{
        dataSource: /* 'Crypto' */ /* 'CryptoWithoutBTC' */ 'CryptoWithoutStable' /* 'CryptoDeFi' */,
        width: '100%',
        height: 550,
        colorTheme: 'dark',
        blockSize: 'market_cap_calc',
        blockColor: 'change',
        locale: 'en',
        symbolUrl: '',
        hasTopBar: true,
        isDataSetEnabled: false,
        isZoomEnabled: true,
        hasSymbolTooltip: true,
      }"/> -->
      <v-card class="ma-1 mt-2">
      <CryptoMarket :options="{
          width: '100%',
          height: 250,
          colorTheme: 'dark',
        }"/>
      </v-card>
      <!-- <EconomicCalendar /> -->
      <!-- <ForexCrossRates /> -->
      <!-- <ForexHeatMap /> -->
      <!-- <FundamentalData /> -->
      <!-- <MarketData /> -->
      <!-- <MarketOverview /> -->

      <!-- <MiniChart :options="{
        width: '100%',
        height: 200,
        colorTheme: 'dark',
        symbol: 'BINANCE:BTCUSDC',
        locale: 'en',
        dateRange: '12M',
        isTransparent: false,
        autosize: false,
        largeChartUrl: '',
      }"/> -->
      
      <!-- <Screener /> -->

      <!-- <SingleTicker :options="{
        colorTheme: 'dark',
        symbol: 'BINANCE:BTCUSDC',
        width: 350,
        isTransparent: false,
        locale: 'en',
      }"/> -->

      <!-- <StockMarket /> -->
      <!-- <StockHeatMap /> -->
      
      <!-- <SymbolInfo :options="{
        width: '100%',
        colorTheme: 'dark',
        symbol: 'BINANCE:BTCUSDC',
        locale: 'en',
        isTransparent: false,
      }"/> -->

      <!-- <SymbolOverview :options="{
        width: '100%',
        height: 450,
        colorTheme: 'dark',
        symbols: [
          ['Apple', 'BINANCE:BTCUSDC|1D'],
          ['Google', 'GOOGL|1D'],
          ['Microsoft', 'MSFT|1D'],
        ],
        chartOnly: false,
        locale: 'en',
        autosize: false,
        showVolume: false,
        showMA: false,
        hideDateRanges: false,
        hideMarketStatus: false,
        hideSymbolLogo: false,
        scalePosition: 'right',
        scaleMode: 'Normal',
        fontFamily:
          '-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif',
        fontSize: '10',
        noTimeScale: false,
        valuesTracking: '1',
        changeMode: 'price-and-percent',
        chartType: 'area',
        maLineColor: '#2962FF',
        maLineWidth: 1,
        maLength: 9,
        lineWidth: 2,
        lineType: 0,
        dateRanges: ['1d|1', '1m|30', '3m|60', '12m|1D', '60m|1W', 'all|1M'],
      }"/> -->
      <v-card class="ma-1 mt-2">
      <TechnicalAnalysis :options="{
        width: '100%',
        height: 450,
        colorTheme: 'dark',
        interval: '1m',
        isTransparent: false,
        symbol: 'BINANCE:BTCUSDC',
        showIntervalTabs: true,
        displayMode: 'single',
        locale: 'en',
      }"/>
      </v-card>
      <!-- <Ticker :options="{
        colorTheme: 'dark',
        symbols: [
            {
              proName: 'BINANCE:BTCUSDC',
              title: 'BTCUSDC',
            },
            {
              proName: 'BINANCE:BTCUSDT',
              title: 'BTCUSDT',
            },
            {
              proName: 'FX_IDC:EURUSD',
              title: 'EUR to USD',
            },
            {
              proName: 'BITSTAMP:BTCUSD',
              title: 'Bitcoin',
            },
            {
              proName: 'BITSTAMP:ETHUSD',
              title: 'Ethereum',
            },
          ],
          isTransparent: false,
          showSymbolLogo: true,
          locale: 'en',
      }"/> -->

      <!-- <TopStories :options="{
        width: '100%',
        height: 450,
        colorTheme: 'dark',
        feedMode: 'all_symbols',
        isTransparent: false,
        displayMode: 'regular',
        locale: 'en',
      }"/> -->

    </div>
  </div>
</template>

<style scoped>
.container {
  background-color: transparent;
  margin: 1px;
}

.pa-4 {
  background-color: transparent;
  margin: 1px;

}

.pa-1 {
  background-color: transparent;
  margin-bottom: 12px;
}

</style>