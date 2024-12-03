from rest_framework.views import APIView
from rest_framework.response import Response
from .services import BinanceService


from rest_framework import viewsets
from .models import TradingBot, TradingStrategy, User
from .serializers import TradingBotSerializer, TradingStrategySerializer, UserSerializer


class TestBinanceViewSet(APIView):
    def get(self, request):
        binance = BinanceService()
        account_info = binance.get_account_balance()
        return Response(account_info)
    
class TradingBotViewSet(viewsets.ModelViewSet):
    queryset = TradingBot.objects.all()
    serializer_class = TradingBotSerializer

class TradingStrategyViewSet(viewsets.ModelViewSet):
    queryset = TradingStrategy.objects.all()
    serializer_class = TradingStrategySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
