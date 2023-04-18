# Local
from django import forms
from django.contrib.auth.models import User

from apps.account.models import Profile


class LoginForm(forms.Form):
    """
    Form for user login.

    This form provides fields for the user's username and password, and uses the
    `CharField` and `PasswordInput` widgets provided by Django's form API.

    Attributes:
        username (CharField): The user's username.
        password (CharField): The user's password.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistration(forms.ModelForm):
    """
    Form for user registration.

    This form provides fields for the user's username, first name, email, and password,
    as well as a confirmation field for the password. It uses the `ModelForm` provided
    by Django to automatically generate the form fields from the `User` model.

    Attributes:
        password (CharField): The user's password.
        password2 (CharField): A confirmation field for the user's password.
    """

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        """
        Validates the user's password.

        This method checks whether the user's password matches the confirmation password.
        If they do not match, it raises a `ValidationError`.

        Returns:
            str: The user's password if validation succeeds.

        Raises:
            forms.ValidationError: If the user's passwords do not match.
        """
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords dont match.")
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    """
    Form for editing a user's profile.

    This form provides fields for the user's first name, last name, and email. It uses the
    `ModelForm` provided by Django to automatically generate the form fields from the `User`
    model.

    Attributes:
        None
    """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    """
    Form for editing a user's profile.

    This form provides fields for the user's date of birth and photo. It uses the
    `ModelForm` provided by Django to automatically generate the form fields from the
    `Profile` model.

    Attributes:
        None
    """

    class Meta:
        model = Profile
        fields = ("date_of_birth", "photo")
