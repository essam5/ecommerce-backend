from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

schema_view = get_schema_view(
    openapi.Info(
        title="E-commerce API",
        default_version="v1",
        description="API documentation for E-commerce Backend",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(OAuth2Authentication,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("product.urls")),
    path("api/", include("order.urls")),
    path("api/", include("notification.urls")),
    # OAuth2 authentication
    path("auth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    # Swagger documentation URLs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
