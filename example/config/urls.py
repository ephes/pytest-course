from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/client-list/"), name="home"),
    path("", include("client.urls", namespace="client")),
]
