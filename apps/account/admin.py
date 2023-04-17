"""
Module: admin_views

This module contains Django admin views for managing user profiles.

Decorators:
    admin.register: A decorator that registers the Profile model with the ProfileAdmin class.

Classes:
    ProfileAdmin: A Django admin view for managing user profiles.

"""

from django.contrib import admin

# Local
from apps.account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Django admin view for managing user profiles.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.

    """
    list_display = ['user', 'date_of_birth', 'photo']
