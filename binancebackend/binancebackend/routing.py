from django.urls import path
from binanceapp.consumers import BinanceWebSocketConsumer

websocket_urlpatterns = [
    path('ws/binance/', BinanceWebSocketConsumer.as_asgi()),
]