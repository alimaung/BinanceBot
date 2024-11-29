from rest_framework.views import APIView
from rest_framework.response import Response
from .services import BinanceService


from rest_framework import viewsets
from .models import TradingBot
from .serializers import TradingBotSerializer


class TestBinanceView(APIView):
    def get(self, request):
        binance = BinanceService()
        account_info = binance.get_account_balance()
        return Response(account_info)
    

class TradingBotViewSet(viewsets.ModelViewSet):
    queryset = TradingBot.objects.all()
    serializer_class = TradingBotSerializer