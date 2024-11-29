from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradingBotViewSet, TestBinanceView

router = DefaultRouter()
router.register(r'bots', TradingBotViewSet)

urlpatterns = [
    path('test-binance/', TestBinanceView.as_view(), name='test-binance'),
    path('api/', include(router.urls)),
]