from django.shortcuts import render
from django.views.decorators.http import require_GET

from client.forms import ClientForm

from .models import Client


@require_GET
def index(request):
    clients = Client.objects.all()
    return render(request, "index.html", context={"clients": clients})


def create(request):
    form = ClientForm()
    return render(request, "create.html", context={"form": form})
