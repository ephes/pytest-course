from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Client, Account, Server


@admin.register(Client)
class ClientModelAdmin(ModelAdmin):
    list_display = ("server", "name")
    fields = ("name", "remote_id", "secret")


@admin.register(Server)
class ServerModelAdmin(ModelAdmin):
    list_display = ("api_base_url",)
    fields = ("api_base_url", "client")


@admin.register(Account)
class AccountModelAdmin(ModelAdmin):
    list_display = ("server", "username")
    fields = ("server", "username", "access_token")
