from django.contrib import admin

from custom_user.admin import EmailUserAdmin
from .models import CustomAccount


class CustomUserAdmin(EmailUserAdmin):
    """CustomUserAdmin admin integration."""
    list_display = ('name', 'email', 'birth_date')

admin.site.register(CustomAccount, CustomUserAdmin)
