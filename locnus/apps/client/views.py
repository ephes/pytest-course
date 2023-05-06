from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import ClientForm, LoginForm
from .models import Client, Login


@require_GET
def client_list(request):
    clients = Client.objects.all()
    return render(request, "client_list.html", context={"clients": clients})


@require_POST
def post_create_client(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("client:client-list")
    else:
        return render(request, "create.html", context={"form": form})


@require_GET
def get_create_client(request):
    form = ClientForm()
    return render(request, "create_client.html", context={"form": form})


@require_GET
def get_login_list(request, client_pk):
    client = Client.objects.get(pk=client_pk)
    logins = client.login_set.all()
    return render(request, "login_list.html", context={"client": client, "logins": logins})


@require_GET
def get_create_login(request):
    form = LoginForm()
    return render(request, "create_login.html", context={"form": form})


@require_POST
def post_create_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("client:login-list", client_pk=form.instance.client.pk)
    else:
        return render(request, "create_login.html", context={"form": form})


@require_GET
def get_login_detail(request, login_pk):
    toots = [
        {"id": 1, "content": "Hello, world!"},
    ]
    login = Login.objects.get(pk=login_pk)
    return render(request, "login_detail.html", context={"login": login, "toots": toots})


@require_GET
def get_timeline(request, client_pk):
    client = Client.objects.get(pk=client_pk)
    toots = client.public_timeline()
    return render(request, "timeline.html", context={"client": client, "toots": toots})
