from django.core.mail import EmailMessage

from .base import BaseChannel


class EmailChannel(BaseChannel):

    def __call__(self, notification, *args, **kwargs):
        EmailMessage(
            subject="subject",
            body="message",
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



