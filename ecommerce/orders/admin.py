from django.contrib import admin

from ecommerce.core.admin import AuditModelAdmin
from .models import Order, OrderProduct


class OrderProductInline(AuditModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
        "product_price"
    )


class OrderAdmin(AuditModelAdmin):
    list_display = (
        "order_number",
        "status",
        "customer",
    )

    def customer(self, obj):
        return obj.customer.name


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductInline)
