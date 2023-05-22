from django.contrib import admin

from ecommerce.core.admin import AuditModelAdmin
from .models import Customer


class CustomerAdmin(AuditModelAdmin):
    list_display = (
        "email",
        "name",
    )


admin.site.register(Customer, CustomerAdmin)
