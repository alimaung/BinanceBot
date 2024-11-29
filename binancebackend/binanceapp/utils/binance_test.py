from binance.client import Client
from django.conf import settings

def test_binance_connection():
    client = Client(
        settings.BINANCE_API_KEY, 
        settings.BINANCE_API_SECRET,
        testnet=settings.BINANCE_TESTNET
    )
    account_info = client.get_server_time()
    print(account_info)
