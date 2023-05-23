from celery import shared_task
from django.db import transaction, DatabaseError

from ecommerce.core.models import Statuses
from ecommerce.customers.models import Customer
from ecommerce.notifications.constants import Event
from ecommerce.notifications.models import NotificationType
from ecommerce.notifications.tasks import send_notification
from ecommerce.products.models import Product
from .models import Order, OrderProduct


@shared_task
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
    order.add_customer(customer=customer)

    notification_data = {
        "recipient": customer.email,
        "notification_type": NotificationType.EMAIL,
        "event": Event.PROCESSED_ORDER.value,
        "meta": {
            "name": customer.name,
            "status": None
        }
    }

    try:
        with transaction.atomic():

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

            order.complete_order()
            notification_data["meta"]["status"] = Statuses.COMPLETED
            transaction.on_commit(lambda: send_notification.apply_async(kwargs=notification_data))
    except DatabaseError:
        order.fail_order(meta=meta_data)
        notification_data["meta"]["status"] = Statuses.FAILED
        send_notification.apply_async(kwargs=notification_data)
