from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Product
from .serializers import ProductSerializer


class ProductViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name="Product 1", sku="SKU001", stock=100, price=10.0
        )

    def test_get_products(self):
        """
        Test retrieving products
        """
        url = reverse("product-list")
        response = self.client.get(url)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        """
        Test creating a new product
        """
        url = reverse("product-list")
        data = {"name": "Product 2", "sku": "SKU002", "stock": 50, "price": 15.0}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_invalid_stock(self):
        """
        Test creating a product with invalid stock (stock <= 0)
        """
        url = reverse("product-list")
        data = {"name": "Product 3", "sku": "SKU003", "stock": 0, "price": 12.0}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("stock", response.data)

    def test_update_product_stock(self):
        """
        Test updating a product with valid stock
        """
        url = reverse("product-detail", kwargs={"pk": self.product.id})
        data = {"name": "Updated Product", "sku": "SKU001", "stock": 150, "price": 20.0}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 150)

    def test_update_product_invalid_stock(self):
        """
        Test updating a product with invalid stock (stock <= 0)
        """
        url = reverse("product-detail", kwargs={"pk": self.product.id})
        data = {"name": "Updated Product", "sku": "SKU001", "stock": 0, "price": 20.0}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("stock", response.data)
