from django.contrib import admin

from ecommerce.core.admin import AuditModelAdmin
from .models import Product


class ProductAdmin(AuditModelAdmin):
    list_display = (
        "sku",
        "name",
        "price",
        "quantity",
        "status"
    )


admin.site.register(Product, ProductAdmin)
