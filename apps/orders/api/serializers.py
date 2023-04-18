# Local
from rest_framework import serializers

from apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    A serializer for the Order model.
    """

    class Meta:
        model = Order
        fields = "__all__"
