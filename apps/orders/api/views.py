from rest_framework import generics, viewsets

# Local
from apps.orders.models import Order, OrderItem
from .serializers import OrderSerializer
from .permissions import IsAdminOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly, )
