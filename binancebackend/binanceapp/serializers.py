from rest_framework import serializers
from .models import TradingBot, TradingStrategy, User, Docs

class TradingBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingBot
        fields = ['id', 'name', 'trading_pair', 'strategy', 'is_active', 'created_at']

class TradingStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingStrategy
        fields = ['id', 'name', 'parameters', 'script', 'description', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'created_at', 'binance_api_key', 'binance_api_secret']

class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ['id', 'name', 'created_at', 'content']