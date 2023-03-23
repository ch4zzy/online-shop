from rest_framework import serializers
from django.utils.text import slugify
# Local 
from ..models import Category, Product, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )


class CategorySerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = slugify(name).lower()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'slug', 'description', 'price', 'available', )
