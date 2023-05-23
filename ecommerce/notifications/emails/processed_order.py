from .base import BaseEmail


class ProcessedOrder(BaseEmail):

    subject = "Your Order has been processed."

    def generate_message(self, meta):
        status = meta.get("status")
        return f"Your order has {status.lower()}."
