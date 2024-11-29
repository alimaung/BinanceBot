from binance.client import Client
from django.conf import settings

from .models import TradingBot
from .binance_service import BinanceService
from binance.enums import *

class BinanceService:
    def __init__(self):
        self.client = Client(
            settings.BINANCE_API_KEY,
            settings.BINANCE_API_SECRET,
        )

    def get_account_balance(self):
        return self.client.get_server_time()



import time
import pandas as pd
from binance.client import Client

class TradingBotService:
    def __init__(self, bot_id):
        # Retrieve bot configuration
        self.bot = TradingBot.objects.get(id=bot_id)
        # Initialize Binance service (must include API/secret setup in BinanceService)
        self.binance = BinanceService()
        self.symbol = 'BTCUSDC'  # Default trading pair
        self.interval = Client.KLINE_INTERVAL_5MINUTE  # 5-minute candlesticks

    def get_candlestick_data(self, symbol, interval, limit=100):
        """
        Fetch recent candlestick (OHLCV) data for the specified symbol and interval.
        """
        candles = self.binance.client.get_klines(
            symbol=symbol,
            interval=interval,
            limit=limit
        )
        return candles

    def calculate_ma(self, prices, period):
        """
        Calculate the moving average (MA) for the given period.
        """
        return prices.rolling(window=period).mean().iloc[-1]

    def calculate_rsi(self, prices, period=14):
        """
        Calculate the Relative Strength Index (RSI) for the given period.
        """
        delta = prices.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]

    def execute_trade_logic(self):
        """
        Execute the main trading logic every 5 minutes.
        """
        while True:
            # Fetch 5-minute candlestick data
            candles = self.get_candlestick_data(self.symbol, self.interval)
            df = pd.DataFrame(candles, columns=[
                'time', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                'taker_buy_quote_asset_volume', 'ignore'
            ])
            df['close'] = df['close'].astype(float)

            # Calculate indicators
            close_prices = df['close']
            ma25 = self.calculate_ma(close_prices, 25)
            ma99 = self.calculate_ma(close_prices, 99)
            rsi = self.calculate_rsi(close_prices)

            # Log calculated values
            print(f"MA25: {ma25}, MA99: {ma99}, RSI: {rsi}")

            # Get the latest close price
            current_price = close_prices.iloc[-1]

            # Apply trading logic based on indicators
            if ma25 > ma99 and rsi < 30:
                print("Buy Signal Detected")
                self.place_order(self.symbol, 'BUY', current_price)
            elif ma25 < ma99 and rsi > 70:
                print("Sell Signal Detected")
                self.place_order(self.symbol, 'SELL', current_price)
            else:
                print("No trade signal.")

            # Wait for the next 5-minute interval
            time.sleep(300)

    def place_order(self, symbol, side, price):
        """
        Place a market order for the specified side (BUY or SELL).
        """
        # This is a placeholder for actual order execution logic.
        # Replace with self.binance.client.order_market() or similar for live trading.
        print(f"Placing {side} order for {symbol} at {price}.")

