import json
from channels.generic.websocket import AsyncWebsocketConsumer
from binance.client import Client
from django.conf import settings
from binance import BinanceSocketManager

class BinanceWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'binance'
        self.room_group_name = f"binance_{self.room_name}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        message = json.loads(text_data)
        # Example: Subscribe to live market price updates (adjust according to needs)
        if 'symbol' in message:
            symbol = message['symbol']
            price_data = await self.get_binance_price(symbol)
            await self.send(text_data=json.dumps({'price': price_data}))

    async def get_binance_price(self, symbol):
        client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)
        price = client.get_symbol_ticker(symbol=symbol)
        return price['price']
    
    async def get_binance_price2(self, symbol):
        client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)
        bm = BinanceSocketManager(client)
        ts = bm.trade_socket(symbol)
        async with ts as tscm:
            res = await tscm.recv()
            return res['p']  # `p` is the price in Binance's trade message
