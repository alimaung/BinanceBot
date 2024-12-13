from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradingBotViewSet, TestBinanceViewSet, TradingStrategyViewSet, UserViewSet, DocsViewSet

router = DefaultRouter()
router.register(r'bots', TradingBotViewSet)
router.register(r'users', UserViewSet)
router.register(r'strategy', TradingStrategyViewSet)
router.register(r'docs', DocsViewSet)


urlpatterns = [
    path('test-binance/', TestBinanceViewSet.as_view(), name='test-binance'),
    path('api/', include(router.urls)),
]