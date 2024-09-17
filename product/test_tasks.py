from django.test import TestCase
from .models import Product
from notification.models import Notification
from .tasks import check_low_stock


class CheckLowStockTaskTests(TestCase):
    def setUp(self):
        self.product_1 = Product.objects.create(name="Product 1", stock=3)
        self.product_2 = Product.objects.create(name="Product 2", stock=7)

    def test_check_low_stock_creates_notifications(self):
        """
        Test that notifications are created when stock is below the threshold
        """
        check_low_stock(threshold=5)
        low_stock_notifications = Notification.objects.filter(
            message__contains="low stock"
        )
        self.assertEqual(low_stock_notifications.count(), 1)
        self.assertIn(self.product_1.name, low_stock_notifications.first().message)

    def test_no_notifications_if_stock_above_threshold(self):
        """
        Test that no notifications are created if stock is above the threshold
        """
        check_low_stock(threshold=2)
        low_stock_notifications = Notification.objects.filter(
            message__contains="low stock"
        )
        self.assertEqual(low_stock_notifications.count(), 0)
