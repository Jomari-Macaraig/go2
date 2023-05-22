from django.db import models

from ecommerce.core.models import Audit
from ecommerce.customers.models import Customer
from ecommerce.products.models import Product


class Order(Audit):
    class Statuses(models.TextChoices):
        PENDING = "PENDING", "PENDING"
        FAILED = "FAILED", "FAILED"
        COMPLETED = "COMPLETED", "COMPLETED"

    order_number = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Statuses.choices, default=Statuses.PENDING)
    products = models.ManyToManyField(
        Product,
        through='OrderProduct'
    )

    def __str__(self):
        return str(self.order_number)


class OrderProduct(Audit):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=17, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.product_price
