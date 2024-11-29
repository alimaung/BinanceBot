from binance.client import Client
from django.conf import settings

class BinanceService:
    def __init__(self):
        self.client = Client(
            settings.BINANCE_API_KEY,
            settings.BINANCE_API_SECRET,
            testnet=settings.BINANCE_TESTNET
        )

    def get_account_balance(self):
        return self.client.get_account()

    def place_order(self, symbol, side, quantity, order_type='MARKET'):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )

    def get_symbol_ticker(self, symbol):
        # Get the latest price for the given symbol (e.g., 'BTCUSDT')
        return self.client.get_symbol_ticker(symbol=symbol)
