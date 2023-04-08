from rest_framework import serializers

# Local
from ..models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
