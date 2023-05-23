from typing import Dict

from celery import shared_task

from .channels.email import EmailChannelBuilder
from .constants import Event
from .emails.processed_order import ProcessedOrder
from .factories import channel_factory, email_factory
from .models import Notification, NotificationType

channel_factory.register_builder(NotificationType.EMAIL, EmailChannelBuilder())

email_factory.register_builder(Event.PROCESSED_ORDER.value, ProcessedOrder)


@shared_task
def send_notification(recipient: str, notification_type: str, event: str, meta: Dict):
    notification = Notification(
        recipient=recipient,
        notification_type=notification_type,
        event=event,
        meta=meta
    )
    notification.save()
    channel = channel_factory.get(key=notification_type)
    channel(notification=notification)