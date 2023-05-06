from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Login, Server


@admin.register(Server)
class ServerModelAdmin(ModelAdmin):
    list_display = ("api_base_url",)
    fields = ("api_base_url", "client_name", "client_id", "client_secret")


@admin.register(Login)
class LoginModelAdmin(ModelAdmin):
    list_display = ("server", "username")
    fields = ("server", "username", "access_token")
