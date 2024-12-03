# binanceapp/admin.py
from django.contrib import admin
from .models import TradingBot, TradingStrategy, User

admin.site.register(TradingBot)
admin.site.register(TradingStrategy)
admin.site.register(User)
