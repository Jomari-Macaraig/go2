from celery import shared_task
from .models import Order, OrderProduct
from django.db import transaction
from ecommerce.customers.models import Customer
from ecommerce.products.models import Product


@shared_task
@transaction.atomic
def process_order(order_number):
    order = Order.objects.get(order_number=order_number)
    meta_data = order.meta

    customer_meta = meta_data.get("customer", {})
    items = meta_data.get("items", [])

    customer, _ = Customer.objects.get_or_create(
        email=customer_meta.get("email"),
        name=customer_meta.get("name"),
        address=customer_meta.get("address"),
    )

    for item in items:
        sku = item.get("sku")
        quantity = item.get("quantity", 0)

        product = Product.objects.get(sku=sku)
        product.decrease_stock(orders=quantity)

        order_product = OrderProduct(
            order=order,
            product=product,
            quantity=quantity,
            product_price=product.price
        )
        order_product.save()

    order.customer = customer
    order.meta = None
    order.status = Order.Statuses.COMPLETED
    order.save()