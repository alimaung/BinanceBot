from rest_framework import serializers
from .models import TradingBot

class TradingBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingBot
        fields = ['id', 'name', 'trading_pair', 'strategy', 'is_active', 'created_at']
