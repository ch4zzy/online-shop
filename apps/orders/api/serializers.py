from rest_framework import serializers

# Local
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
