from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Client, Login


@admin.register(Client)
class ClientModelAdmin(ModelAdmin):
    list_display = ("api_base_url", "name")
    fields = ("api_base_url", "remote_id", "name", "secret")


@admin.register(Login)
class ClientUserModelAdmin(ModelAdmin):
    list_display = ("client", "username")
    fields = ("client", "username", "access_token")
