from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.IntegerField(default=0)


class Payment(models.Model):
    payor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payors", verbose_name="плательщик"
        )
    payee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payee", verbose_name="получатель платежа"
        )
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Сумма")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.amount
