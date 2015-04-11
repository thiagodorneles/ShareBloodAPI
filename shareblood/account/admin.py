from django.contrib import admin

from custom_user.admin import EmailUserAdmin
from .models import CustomAccount


class CustomUserAdmin(EmailUserAdmin):
    pass

admin.site.register(CustomAccount, CustomUserAdmin)
