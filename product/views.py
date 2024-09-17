from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "sku"]

    def perform_create(self, serializer):
        if serializer.validated_data["stock"] <= 0:
            raise ValidationError({"stock": "Stock must be greater than zero."})
        serializer.save()

    def perform_update(self, serializer):
        if serializer.validated_data["stock"] <= 0:
            raise ValidationError({"stock": "Stock must be greater than zero."})
        serializer.save()
