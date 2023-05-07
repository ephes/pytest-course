from django.urls import path

from . import views

app_name = "client"

urlpatterns = [
    # home
    path("", views.index, name="home"),
    # client
    path("server-list/", views.server_list, name="server-list"),
    path("server-create/", views.get_create_server, name="get-create-server"),
    path("client-post-create/", views.post_create_server, name="post-create-server"),
    # account
    path("account-list/<int:server_pk>", views.get_account_list, name="account-list"),
    path("account-create/", views.get_create_account, name="get-create-account"),
    path("account-post-create/", views.post_create_account, name="post-create-account"),
    path("personal-timeline/<int:account_pk>", views.get_personal_timeline, name="personal-timeline"),
    # timeline
    path("public-timeline/<int:server_pk>", views.get_public_timeline, name="public-timeline"),
]
