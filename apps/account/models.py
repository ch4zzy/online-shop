from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    Model representing a user profile.

    This model represents a user profile with the user's information and an optional photo.
    It is associated with the `User` model using a one-to-one relationship. The `date_of_birth`
    field is optional.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the `User` model.
        date_of_birth (DateTimeField): The user's date of birth. Optional.
        photo (ImageField): An optional user photo.

    Methods:
        __str__(): Returns a string representation of the profile.

    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.

        This method returns a string representation of the profile object. It uses the
        user's username as a label for the profile.

        Returns:
            str: A string representation of the profile.

        """
        return f"Profile for user {self.user.username}"
