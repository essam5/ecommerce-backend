from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    stock = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )  # Ensure stock is non-negative

    def __str__(self):
        return self.name

    def is_low_stock(self, threshold=5):
        return self.stock < threshold
