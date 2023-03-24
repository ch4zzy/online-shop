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
        return Response({'category': CategorySerializer2(cat, many=True).data,})
    
    def post(self, request):
        serializer = CategorySerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'category': serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method delete not allowed"})
        try:
            instance = Category.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exist"})
        return Response({"category": "Successfully delete" + str(pk)})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})
        try:
            instance = Category.objects.get(pk=pk)
        except:
            return Response({"error": "Method put not allowed"})
        
        serializer = CategorySerializer2(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"category": serializer.data})

