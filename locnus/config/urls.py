from django.contrib import admin
from django.urls import include, path

# from client.urls import urlpatterns as client_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("client.urls", namespace="client")),
    # path("client-list/", include("apps.client.urls")),
]  # + client_urlpatterns
