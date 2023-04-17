from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """
    Authenticates users based on their email address.

    This backend allows users to authenticate with their email address instead of their
    username. It overrides the default `authenticate` method of the Django `BaseBackend`
    class and replaces it with a method that looks up the user by email address.

    Attributes:
        None
    """

    def authenticate(self, request, username=None, password=None):
        """
        Authenticates a user based on their email address and password.

        This method looks up a user by their email address and checks their password
        against the provided password. If the passwords match, it returns the user
        object. If the user cannot be found or the passwords do not match, it returns
        None.

        Args:
            request (HttpRequest): The current request object.
            username (str): The user's email address.
            password (str): The user's password.

        Returns:
            User object if authentication succeeds, None otherwise.
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Retrieves a user object by their ID.

        This method retrieves a user object by their ID. It is used by Django's
        authentication system to retrieve the user object associated with a particular
        session.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            User object if the user is found, None otherwise.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
