# goldpresentprice/models.py

from django.db import models

class GoldPrice(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Gold Price on {self.date}: ${self.price}"
