from django.db import models

class TradingBot(models.Model):
    name = models.CharField(max_length=255)
    trading_pair = models.CharField(max_length=20)
    strategy = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    binance_api_key = models.CharField(max_length=255)
    binance_api_secret = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class TradingStrategy(models.Model):
    name = models.CharField(max_length=255)
    parameters = models.JSONField()
    script = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name