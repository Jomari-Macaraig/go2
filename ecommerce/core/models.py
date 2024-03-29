from django.db import models
from django.conf import settings


class Statuses(models.TextChoices):
    PENDING = "PENDING", "PENDING"
    FAILED = "FAILED", "FAILED"
    COMPLETED = "COMPLETED", "COMPLETED"


class Audit(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserAudit(Audit):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True
