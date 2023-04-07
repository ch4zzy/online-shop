from rest_framework import generics, viewsets
from django.contrib.auth.models import User

# Local
from .serializers import AccountSerializer
from .permissions import IsAdminOrReadOnly


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminOrReadOnly, )
