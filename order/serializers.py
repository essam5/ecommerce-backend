from rest_framework import serializers
from .models import SalesOrder, PurchaseOrder


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ["id", "product", "customer", "quantity", "total_price", "created_at"]

    def validate(self, data):
        product = data.get("product")
        quantity = data.get("quantity")
        if product.stock < quantity:
            raise serializers.ValidationError("Not enough stock available.")
        return data


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["id", "product", "quantity", "total_price", "created_at"]
