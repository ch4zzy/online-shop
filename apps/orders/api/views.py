from rest_framework import generics, viewsets

# Local
from apps.orders.models import Order
from apps.orders.api.serializers import OrderSerializer
from apps.orders.api.permissions import IsAdminOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for orders.

    Methods:
    - GET: Retrieve one or many orders.
    - POST: Create a new order.
    - PUT: Update an existing order.
    - DELETE: Delete an order.

    Attributes:
    - queryset: The queryset of orders to operate on.
    - serializer_class: The serializer to use for (de)serializing orders.
    - permission_classes: The permission classes to use for accessing the viewset.

    Permissions:
    - Users with admin privileges can perform any operation.
    - Other users can only retrieve orders (read-only).
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly, )
