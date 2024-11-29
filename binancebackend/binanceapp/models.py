from django.db import models

class TradingBot(models.Model):
    name = models.CharField(max_length=255)
    trading_pair = models.CharField(max_length=20)  # e.g., 'BTCUSDT'
    strategy = models.CharField(max_length=255)  # Strategy name (e.g., 'RSI', 'EMA')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
