# Local
from apps.orders.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """
    A serializer for the Order model.
    """
    class Meta:
        model = Order
        fields = "__all__"
