from django.apps import AppConfig


class AccountConfig(AppConfig):
    """
    AppConfig for the 'account' app.

    This class defines the configuration for the 'account' app. It sets the app name and
    specifies any signals that should be connected when the app is ready.

    Attributes:
        name (str): The name of the app ('apps.account')
    """
    name = 'apps.account'
