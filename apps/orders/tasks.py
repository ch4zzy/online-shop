# Local
from celery import shared_task
from django.core.mail import send_mail

from apps.orders.models import Order


@shared_task
def order_created(order_id):
    """
    Sends an email notification to the customer when an order is created.

    Args:
        order_id (int): The ID of the order.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name},\n\n\
          You have successfully placed an order.\
          Your order id is {order.id}."
    mail_sent = send_mail(subject, message, "admin@marketplace.com", [order.email])
    return mail_sent
