# Local
from apps.orders.models import Order
from django import forms


class OrderCreateForm(forms.ModelForm):
    """
    A form for creating a new Order instance with the required fields.

    Fields:
    -------
    first_name : str
        First name of the customer who placed the order.
    last_name : str
        Last name of the customer who placed the order.
    email : str
        Email address of the customer who placed the order.
    address : str
        Shipping address of the customer who placed the order.
    postal_code : str
        Postal code of the shipping address of the customer who placed the order.
    city : str
        City of the shipping address of the customer who placed the order.
    """
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']
