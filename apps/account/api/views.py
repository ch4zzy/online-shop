from apps.account.api.permissions import IsAdminOrReadOnly
# Local
from apps.account.api.serializers import AccountSerializer
from django.contrib.auth.models import User
from rest_framework import generics, viewsets


class AccountViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for User model.
    """
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminOrReadOnly, )
