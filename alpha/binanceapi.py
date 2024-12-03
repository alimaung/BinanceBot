from binance.client import Client
from binance.enums import *
import os

# Set up your Binance API keys
api_key = '2Sa01h31SChZG1bpH3SmsINHUKhAubbXELDGEZ1Mr7R8TfprXpWYz0G6v9v9of3w'
api_secret = 'iSekrpsI7niyWiUOwlRPPm7YsXtCe624IrQFchv6ytgZgmdOJpf41NwegPib8D2U'

# Initialize the Binance Client
client = Client(api_key, api_secret)

# Define the symbol for BTC/USDC
symbol = 'BTCUSDC'

# Function to get the balance of USDC
def get_balance(asset):
    balance = client.get_asset_balance(asset)
    return float(balance['free']) if balance else 0.0

# Function to place a market buy order for BTC using USDC
def buy_btc_with_usdc():
    usdc_balance = get_balance('USDC')
    
    if usdc_balance <= 0:
        print("Insufficient USDC balance.")
        return
    
    # Place market order to buy BTC with all available USDC
    try:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=round(usdc_balance, 2)  # Buying with the full available balance
        )
        print("Buy order placed:", order)
    except Exception as e:
        print(f"Error placing buy order: {e}")

# Function to place a market sell order for BTC to get USDC
def sell_btc_for_usdc():
    btc_balance = get_balance('BTC')

    if btc_balance <= 0:
        print("Insufficient BTC balance.")
        return

    # Place market order to sell BTC for USDC
    try:
        order = client.order_market_sell(
            symbol=symbol,
            quantity=round(btc_balance, 2)  # Selling all BTC
        )
        print("Sell order placed:", order)
    except Exception as e:
        print(f"Error placing sell order: {e}")

# Call the functions to place the orders
# You can either call buy_btc_with_usdc() to buy or sell_btc_for_usdc() to sell
# Example: Buy BTC with all USDC
#buy_btc_with_usdc()
#usdc = get_balance('USDC')
#time_res = client.get_server_time()
#status = client.get_system_status()
#info = client.get_symbol_info('BNBBTC')
account = client.get_my_trades(symbol='BTCUSDC')
print(account)

# Example: Sell BTC for USDC
# sell_btc_for_usdc()
