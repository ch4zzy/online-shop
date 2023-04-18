from rest_framework import generics, viewsets

from apps.shop.api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from apps.shop.api.serializers import (
    CategorySerializer,
    CommentSerializer,
    ProductSerializer,
)

# Local
from apps.shop.models import Category, Comment, Product


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Category model.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Product model.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Comment model.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
