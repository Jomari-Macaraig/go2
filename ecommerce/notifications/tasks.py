from typing import Dict

from celery import shared_task

from .models import Notification, NotificationType
from .factories import channel_factory
from .channels.email import EmailChannelBuilder


channel_factory.register_builder(NotificationType.EMAIL, EmailChannelBuilder())


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