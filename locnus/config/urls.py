from django.contrib import admin
from django.urls import include, path

from apps.client import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("clients/", include("apps.client.urls"), name="clients"),
]
