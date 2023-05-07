from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import LoginForm, ServerForm
from .models import Login, Server


@require_GET
def server_list(request):
    servers = Server.objects.all()
    return render(request, "server_list.html", context={"servers": servers})


@require_POST
def post_create_server(request):
    form = ServerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("locnus:server-list")
    else:
        return render(request, "create_server.html", context={"form": form})


@require_GET
def get_create_server(request):
    form = ServerForm()
    return render(request, "create_server.html", context={"form": form})


@require_GET
def get_login_list(request, server_pk):
    server = Server.objects.get(pk=server_pk)
    logins = server.logins.all()
    return render(request, "login_list.html", context={"server": server, "logins": logins})


@require_GET
def get_create_login(request):
    form = LoginForm()
    return render(request, "create_login.html", context={"form": form})


@require_POST
def post_create_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("locnus:login-list", server_pk=form.instance.server.pk)
    else:
        return render(request, "create_login.html", context={"form": form})


@require_GET
def get_personal_timeline(request, login_pk):
    login = Login.objects.get(pk=login_pk)
    toots = login.personal_timeline()
    return render(request, "timeline.html", context={"login": login, "toots": toots})


@require_GET
def get_public_timeline(request, server_pk):
    server = Server.objects.get(pk=server_pk)
    toots = server.public_timeline()
    return render(request, "timeline.html", context={"server": server, "toots": toots})
