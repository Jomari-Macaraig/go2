from django.core.validators import MinValueValidator
from django.db import models

from ecommerce.core.models import Audit
from ecommerce.customers.models import Customer
from ecommerce.products.models import Product


class Order(Audit):
    class Statuses(models.TextChoices):
        PENDING = "PENDING", "PENDING"
        FAILED = "FAILED", "FAILED"
        COMPLETED = "COMPLETED", "COMPLETED"

    order_number = models.PositiveIntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=Statuses.choices, default=Statuses.PENDING)
    products = models.ManyToManyField(
        Product,
        through="OrderProduct"
    )
    meta = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.order_number)


class OrderProduct(Audit):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=17, decimal_places=2, validators=[MinValueValidator(0.0)])

    @property
    def total_price(self):
        return self.quantity * self.product_price
