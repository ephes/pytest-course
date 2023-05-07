from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Client, Login, Server


@admin.register(Client)
class ClientModelAdmin(ModelAdmin):
    list_display = ("server", "name")
    fields = ("name", "remote_id", "secret")


@admin.register(Server)
class ServerModelAdmin(ModelAdmin):
    list_display = ("api_base_url",)
    fields = ("api_base_url", "client")


@admin.register(Login)
class LoginModelAdmin(ModelAdmin):
    list_display = ("server", "username")
    fields = ("server", "username", "access_token")
