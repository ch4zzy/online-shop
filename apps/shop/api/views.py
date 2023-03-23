from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.forms import model_to_dict
# Local
from ..models import Category, Product, Comment
from .serializers import CategorySerializer, ProductSerializer, CategorySerializer2

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

class CategoryAPIView(APIView):
    def get(self, request):
        cat = Category.objects.all()
        return Response({'category': CategorySerializer2(cat, many=True).data})
    
    def post(self, request):
        serializer = CategorySerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'category': serializer.data})




'''
class CategoryCreateView(APIView):
    def post(self, request):
        new_cat = Category.objects.create(
            name = request.data['name'],
            slug = request.data[slugify('name')].lower(),
        )
        return Response({'category': model_to_dict(new_cat)})
    

class CategoryDeleteView(APIView):
    def post(self, request):
        del_cat = Category.objects.filter(
            id = request.data['id'],
        )
        return Response(del_cat.delete())
'''
