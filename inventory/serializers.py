from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ['id', 'name', 'SKU', 'price', 'stock_quantity', 'description']
        
    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number or greater than 0.")
        return value
    def validate_name(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Name cannot exceed 100 characters.")
        return value
    