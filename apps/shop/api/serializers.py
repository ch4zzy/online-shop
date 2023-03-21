from rest_framework import serializers

# Local 
from ..models import Category, Product, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )
