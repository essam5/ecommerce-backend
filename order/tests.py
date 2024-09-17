from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import SalesOrder, PurchaseOrder, Product, Customer
from .serializers import SalesOrderSerializer, PurchaseOrderSerializer


class SalesOrderViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Product 1", stock=100, price=10.0)
        self.customer = Customer.objects.create(
            username="Customer 1", email="customer1@example.com"
        )
        self.sales_order = SalesOrder.objects.create(
            product=self.product, customer=self.customer, quantity=5
        )

    def test_get_sales_orders(self):
        """
        Test retrieving sales orders
        """
        url = reverse("salesorder-list")
        response = self.client.get(url)
        sales_orders = SalesOrder.objects.all()
        serializer = SalesOrderSerializer(sales_orders, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_sales_order(self):
        """
        Test creating a new sales order
        """
        url = reverse("salesorder-list")
        data = {
            "product": self.product.id,
            "customer": self.customer.id,
            "quantity": 10,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SalesOrder.objects.count(), 2)


class PurchaseOrderViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Product 1", stock=100, price=10.0)
        self.purchase_order = PurchaseOrder.objects.create(
            product=self.product, quantity=20
        )

    def test_get_purchase_orders(self):
        """
        Test retrieving purchase orders
        """
        url = reverse("purchaseorder-list")
        response = self.client.get(url)
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_purchase_order(self):
        """
        Test creating a new purchase order
        """
        url = reverse("purchaseorder-list")
        data = {"product": self.product.id, "quantity": 50}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)
