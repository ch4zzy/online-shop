from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework import viewsets

from apps.account.api.permissions import IsAdminOrReadOnly
from apps.account.api.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for User model.
    """

    queryset: "QuerySet[User]" = User.objects.all()
    serializer_class: "AccountSerializer" = AccountSerializer
    permission_classes: "tuple[type[IsAdminOrReadOnly]]" = (IsAdminOrReadOnly,)
