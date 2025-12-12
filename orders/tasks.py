from email import message
from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Задача для отправки э-почты при создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Заказ № {order.id}"
    message = (
        f"Уважаемый(-ая) {order.first_name}.\n\n"
        f"Вы успешно сделали заказ на нашем сайте.\n"
        f"Номер вашего заказа {order.id}"
        )
    mail_send = send_mail(
        subject, message, "admin@myshop.com", [order.email]
    )
    return mail_send