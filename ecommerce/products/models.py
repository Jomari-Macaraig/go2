from django.db import models
from ecommerce.core.models import UserAudit


class Product(UserAudit):
    sku = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=17, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()

    @property
    def status(self):
        return True if self.quantity else False

    def __str__(self):
        return self.name