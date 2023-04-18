# Local 
from apps.shop.models import Category, Comment, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.

    Fields:
    -------
    id : int
        The ID of the category.
    name : str
        The name of the category.
    slug : str
        The slug of the category.
    """
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.

    Fields:
    -------
    id : int
        The ID of the product.
    category : int
        The ID of the category to which the product belongs.
    name : str
        The name of the product.
    slug : str
        The slug of the product.
    image : str
        The URL of the image of the product.
    description : str
        The description of the product.
    price : decimal
        The price of the product.
    available : bool
        A flag indicating whether the product is available or not.
    created : datetime
        The date and time when the product was created.
    updated : datetime
        The date and time when the product was last updated.
    """
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model.

    Fields:
    -------
    id : int
        The ID of the comment.
    post : int
        The ID of the post to which the comment belongs.
    user : int
        The ID of the user who wrote the comment.
    name : str
        The name of the user who wrote the comment.
    email : str
        The email of the user who wrote the comment.
    body : str
        The body of the comment.
    created : datetime
        The date and time when the comment was created.
    active : bool
        A flag indicating whether the comment is active or not.
    """
    class Meta:
        model = Comment
        fields = "__all__"
