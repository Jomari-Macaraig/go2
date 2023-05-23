from typing import Dict

from celery import shared_task

from .models import Notification


@shared_task
def send_notification(recipient: str, notification_type: str, event: str, meta: Dict):
    notification = Notification(
        recipient=recipient,
        notification_type=notification_type,
        event=event,
        meta=meta
    )
    notification.save()
