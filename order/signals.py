from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import SalesOrder, PurchaseOrder


# Sales Order Signal: Reduces stock when a sales order is placed
@receiver(post_save, sender=SalesOrder)
def update_product_stock_on_sales(sender, instance, created, **kwargs):
    if created:
        instance.product.stock -= instance.quantity
        instance.product.save()


# Purchase Order Signal: Increases stock when a purchase order is placed
@receiver(post_save, sender=PurchaseOrder)
def update_product_stock_on_purchase(sender, instance, created, **kwargs):
    if created:
        instance.product.stock += instance.quantity
        instance.product.save()


# Reverse stock update when a SalesOrder is deleted
@receiver(post_delete, sender=SalesOrder)
def reverse_product_stock_on_sales_delete(sender, instance, **kwargs):
    instance.product.stock += instance.quantity
    instance.product.save()


# Reverse stock update when a PurchaseOrder is deleted
@receiver(post_delete, sender=PurchaseOrder)
def reverse_product_stock_on_purchase_delete(sender, instance, **kwargs):
    instance.product.stock -= instance.quantity
    instance.product.save()
