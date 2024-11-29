from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from datetime import datetime



# Initialize the client with your API key and secret
api_key = '2Sa01h31SChZG1bpH3SmsINHUKhAubbXELDGEZ1Mr7R8TfprXpWYz0G6v9v9of3w'
api_secret = 'iSekrpsI7niyWiUOwlRPPm7YsXtCe624IrQFchv6ytgZgmdOJpf41NwegPib8D2U'

client = Client(api_key, api_secret)

def main():
    try:
        # 1. Get server time
        server_time = client.get_server_time()
        print("Server Time:", server_time)

        # 3. Get current market price of a symbol
        price = client.get_symbol_ticker(symbol="BTCUSDC")
        print("BTCUSDC Price:", price)

        candles = client.get_klines(symbol='BTCUSDC', interval=Client.KLINE_INTERVAL_5MINUTE, limit=5)
        print(candles)



    except BinanceAPIException as e:
        print(f"Binance API Exception: {e}")
    except BinanceOrderException as e:
        print(f"Binance Order Exception: {e}")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    main()
