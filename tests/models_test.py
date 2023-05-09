import pytest
from django.db import IntegrityError
from django.utils import timezone

from locnus.models import Account, Client, Server, Status

from .first import hello_world


@pytest.fixture(name="client")
def mastodon_client():
    client = Client(name="pytooterapp", remote_id="remote_id", secret="secret")
    client.save()
    return client


@pytest.mark.django_db
def test_server_in_database(client):
    server = Server(api_base_url="https://example.com", client=client)

    server.save()
    assert server in Server.objects.all()


@pytest.mark.django_db
def test_create_status():
    status_data = {
        "created_at": timezone.now(),
        "id": 123,
        "content": "Hello, world!",
    }
    status = Status(created_at=status_data["created_at"], data=status_data)
    status.save()
    assert status in Status.objects.all()


@pytest.mark.django_db
def test_no_account_without_server():
    account = Account()
    with pytest.raises(IntegrityError):
        account.save()


# @pytest.fixture()
def server(client):
    server = Server(api_base_url="https://example.com", client=client)
    server.save()
    return server


@pytest.mark.django_db
def test_account_in_database(client):
    item = server(client)
    account = Account(server=item, username="alice", access_token="access_token")
    account.save()
    assert item.accounts.count() == 1
    assert len(item.accounts.all()) == 1
    # assert account in Account.objects.all()
    # assert Account.objects.count() == 1


@pytest.mark.django_db
def test_modifies_database(client):
    server = Server(api_base_url="https://example.com", client=client)
    server.save()
    assert server in Server.objects.all()


@pytest.mark.django_db
def test_uses_modified_database(django_db_setup):
    print(Server.objects.all())
    assert False


def test_hello_world(capsys):
    hello_world()
    output = capsys.readouterr().out
    print("output: ", output)
    assert output == "hello world!\n"


def test_with_different_settings(settings):
    settings.ADMIN_ENABLED = False
