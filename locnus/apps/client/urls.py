from django.urls import path

from . import views

app_name = "client"

urlpatterns = [
    # client
    path("client-list/", views.client_list, name="client-list"),
    path("client-create/", views.get_create_client, name="get-create-client"),
    path("client-post-create/", views.post_create_client, name="post-create-client"),
    # login
    path("login-list/<int:client_pk>", views.get_login_list, name="login-list"),
    path("login-create/", views.get_create_login, name="get-create-login"),
    path("login-post-create/", views.post_create_login, name="post-create-login"),
    path("login-detail/<int:login_pk>", views.get_login_detail, name="login-detail"),
    # timeline
    path("timeline/<int:client_pk>", views.get_timeline, name="timeline"),
]
