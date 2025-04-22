from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    SKU = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
