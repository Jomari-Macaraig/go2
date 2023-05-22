from django.urls import path

from ecommerce.products.api import views as product_views
from ecommerce.orders.api import views as order_views

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
    path(
        route="orders/",
        view=order_views.CreateOrder.as_view(),
        name="orders"
    ),
]