from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import AccountForm, ServerForm
from .models import Account, Server


@require_GET
def index(request):
    toots = []
    account = Account.objects.first()
    if account is not None:
        toots = account.personal_timeline()
    return render(request, "index.html", context={"toots": toots})


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
def get_account_list(request, server_pk):
    server = Server.objects.get(pk=server_pk)
    accounts = server.accounts.all()
    return render(request, "account_list.html", context={"server": server, "accounts": accounts})


@require_GET
def get_create_account(request):
    form = AccountForm()
    return render(request, "create_account.html", context={"form": form})


@require_POST
def post_create_account(request):
    form = AccountForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("locnus:account-list", server_pk=form.instance.server.pk)
    else:
        return render(request, "create_account.html", context={"form": form})


@require_GET
def get_personal_timeline(request, account_pk):
    account = Account.objects.get(pk=account_pk)
    toots = account.personal_timeline()
    return render(request, "timeline.html", context={"account": account, "toots": toots})


@require_GET
def get_public_timeline(request, server_pk):
    server = Server.objects.get(pk=server_pk)
    toots = server.public_timeline()
    return render(request, "timeline.html", context={"server": server, "toots": toots})
