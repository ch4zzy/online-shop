from django.db.models.query import QuerySet
from rest_framework import viewsets

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

    queryset: "QuerySet[Category]" = Category.objects.all()
    serializer_class: "CategorySerializer" = CategorySerializer
    permission_classes: "tuple[type[IsAdminOrReadOnly]]" = (IsAdminOrReadOnly,)


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Product model.
    """

    queryset: "QuerySet[Product]" = Product.objects.all()
    serializer_class: "ProductSerializer" = ProductSerializer
    permission_classes: "tuple[type[IsAdminOrReadOnly]]" = (IsAdminOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Comment model.
    """

    queryset: "QuerySet[Comment]" = Comment.objects.all()
    serializer_class: "CommentSerializer" = CommentSerializer
    permission_classes: "tuple[type[IsOwnerOrReadOnly]]" = (IsOwnerOrReadOnly,)
