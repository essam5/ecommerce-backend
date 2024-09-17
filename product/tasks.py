from celery import shared_task
from .models import Product
from notification.models import Notification


@shared_task
def check_low_stock(threshold=5):
    low_stock_products = Product.objects.filter(stock__lt=threshold)

    if low_stock_products.exists():
        notifications = []
        for product in low_stock_products:
            message = (
                f"Product '{product.name}' has low stock ({product.stock} units left)."
            )
            notifications.append(Notification(message=message))

        # Create all notifications in bulk to reduce DB hits
        Notification.objects.bulk_create(notifications)
