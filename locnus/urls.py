from django.urls import path

from . import views

app_name = "client"

urlpatterns = [
    # client
    path("server-list/", views.server_list, name="server-list"),
    path("server-create/", views.get_create_server, name="get-create-server"),
    path("client-post-create/", views.post_create_server, name="post-create-server"),
    # login
    path("login-list/<int:server_pk>", views.get_login_list, name="login-list"),
    path("login-create/", views.get_create_login, name="get-create-login"),
    path("login-post-create/", views.post_create_login, name="post-create-login"),
    path("personal-timeline/<int:login_pk>", views.get_personal_timeline, name="personal-timeline"),
    # timeline
    path("public-timeline/<int:server_pk>", views.get_public_timeline, name="public-timeline"),
]
