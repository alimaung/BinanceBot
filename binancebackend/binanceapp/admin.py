# binanceapp/admin.py
from django.contrib import admin
from .models import TradingBot, TradingStrategy, User, Docs

admin.site.register(TradingBot)
admin.site.register(TradingStrategy)
admin.site.register(User)
admin.site.register(Docs)