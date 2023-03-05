from celery import task
from django.core.mail import send_mail
# Local
from .models import Order


