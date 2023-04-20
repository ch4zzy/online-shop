from django.db.models.query import QuerySet
from rest_framework import viewsets

from apps.orders.api.permissions import IsAdminOrReadOnly
from apps.orders.api.serializers import OrderSerializer
from apps.orders.models import Order


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

    queryset: "QuerySet[Order]" = Order.objects.all()
    serializer_class: "OrderSerializer" = OrderSerializer
    permission_classes: "tuple[type[IsAdminOrReadOnly]]" = (IsAdminOrReadOnly,)
