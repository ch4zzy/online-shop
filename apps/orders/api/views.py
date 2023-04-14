from rest_framework import generics, viewsets

# Local
from apps.orders.models import Order, OrderItem
from apps.orders.api.serializers import OrderSerializer
from apps.orders.api.permissions import IsAdminOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly, )
