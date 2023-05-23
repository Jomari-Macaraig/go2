from django.core.mail import EmailMessage

from .base import BaseChannel
from ..factories import email_factory


class EmailChannel(BaseChannel):

    def __call__(self, notification, *args, **kwargs):
        subject, body = email_factory.get(notification.event)(meta=notification.meta)
        EmailMessage(
            subject=subject,
            body=body,
            to=[notification.recipient]
        ).send()
        notification.complete_notification()


class EmailChannelBuilder:

    def __init__(self):
        self._instance = None

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = EmailChannel()
        return self._instance



