from django.core.cache import cache
from .models import Product


def get_cached_product_list():
    products = cache.get("products_list")
    if not products:
        products = Product.objects.all()
        cache.set("products_list", products, 60 * 15)  # Cache for 15 minutes
    return products
