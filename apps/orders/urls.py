from django.urls import path

# Local
from . import views

app_name = 'orders'

urlpatterns = [
    path('orders/', views.order_create, name='order_create'),
]
