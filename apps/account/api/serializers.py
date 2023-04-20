from django.contrib.auth.models import User
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    """
    A serializer for the User model in Django's authentication system. Serializes all fields.

    Attributes:
        Meta: Metadata for this serializer, including the model and fields to include.
            model (django.contrib.auth.models.User): The User model to serialize.
            fields (str[]): A list of all fields to include in the serialized output.
                In this case, "__all__" is used to include all fields.
    """

    class Meta:
        model: type = User
        fields: list[str] = "__all__"
