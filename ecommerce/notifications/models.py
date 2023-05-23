
from django.db import models

from ecommerce.core.models import Audit
from ecommerce.core.models import Statuses


class NotificationType(models.TextChoices):
    EMAIL = "EMAIL", "EMAIL"
    SMS = "SMS", "SMS"


class Notification(Audit):

    recipient = models.CharField(max_length=258)
    notification_type = models.CharField(max_length=10, choices=NotificationType.choices)
    status = models.CharField(max_length=10, choices=Statuses.choices, default=Statuses.PENDING)
    event = models.CharField(max_length=64)
    meta = models.JSONField(null=True, blank=True)

    def complete_notification(self):
        self.status = Statuses.COMPLETED
        self.save()
