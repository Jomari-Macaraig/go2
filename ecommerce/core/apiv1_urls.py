from django.urls import path

from ..products.api import views as product_views

urlpatterns = [
    path(
        route="products/",
        view=product_views.ProductListAPIView.as_view(),
        name="products"
    ),
    path(
        route="products/<str:sku>",
        view=product_views.ProductRetrieveAPIView.as_view(),
        name="products"
    ),
]