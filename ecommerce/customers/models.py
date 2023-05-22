from django.db import models

from ecommerce.core.models import Audit


class Customer(Audit):
    email = models.EmailField(max_length=258, primary_key=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=258)

    def __str__(self):
        return self.name
