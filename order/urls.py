from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SalesOrderViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register("sales", SalesOrderViewSet)
router.register("purchases", PurchaseOrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
