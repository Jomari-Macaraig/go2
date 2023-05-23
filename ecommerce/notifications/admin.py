from django.contrib import admin

from ecommerce.core.admin import AuditModelAdmin
from .models import Notification


class NotificationAdmin(AuditModelAdmin):
    list_display = (
        "recipient",
        "created_time",
        "notification_type",
        "event",
        "status",
    )


admin.site.register(Notification, NotificationAdmin)
