from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.forms import model_to_dict
# Local
from ..models import Category, Product, Comment
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryCreateView(APIView):
    def post(self, request):
        new_cat = Category.objects.create(
            name = request.data['name'],
            slug = request.data[slugify('name')],
        )
        return Response({'category': model_to_dict(new_cat)})

