import pytest
from django.db import IntegrityError
from django.utils import timezone

from locnus.models import Account, Client, Server, Status, Timeline

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
    # assert False
    assert True


def test_hello_world(capsys):
    hello_world()
    output = capsys.readouterr().out
    print("output: ", output)
    assert output == "hello world!\n"


def test_with_different_settings(settings):
    settings.ADMIN_ENABLED = False


@pytest.fixture()
def status_data():
    """Some raw status data from the Mastodon API."""
    return {
        "created_at": timezone.now(),
        "id": 123,
        "content": "Hello, world!",
    }


@pytest.fixture()
def status(status_data):
    status = Status(id=1, created_at=status_data["created_at"], data=status_data)
    status.save()
    return status


@pytest.mark.django_db
def test_create_status(status):
    assert status in Status.objects.all()


@pytest.fixture(params=[Timeline.Tag.PUBLIC, Timeline.Tag.LOCAL])
def timeline_tag(request):
    return request.param


@pytest.fixture(params=[Server.timeline_public, Server.timeline_local])
def get_timeline(request):
    return request.param


@pytest.mark.django_db
def test_tagged_status_in_appropriate_timeline_via_fixture_params(timeline_tag, get_timeline, status, server):
    item = Timeline(status=status, server=server, tag=timeline_tag)
    item.save()
    timeline_qs = get_timeline(server)
    status_pks = {x.status.pk for x in timeline_qs}
    should_be_in_timeline = timeline_tag.name.lower() in str(get_timeline)
    if should_be_in_timeline:
        assert status.pk in status_pks
    else:
        assert status.pk not in status_pks


@pytest.mark.django_db
@pytest.mark.parametrize(
    "tag, get_timeline, should_be_in_timeline",
    [
        (Timeline.Tag.PUBLIC, Server.timeline_public, True),
        (Timeline.Tag.LOCAL, Server.timeline_public, False),
        (Timeline.Tag.LOCAL, Server.timeline_local, True),
        (Timeline.Tag.PUBLIC, Server.timeline_local, False),
    ],
)
def test_tagged_status_in_appropriate_timeline(tag, get_timeline, should_be_in_timeline, status, server):
    item = Timeline(status=status, server=server, tag=tag)
    item.save()
    timeline_qs = get_timeline(server)
    status_pks = {x.status.pk for x in timeline_qs}
    if should_be_in_timeline:
        assert status.pk in status_pks
    else:
        assert status.pk not in status_pks


@pytest.mark.django_db
def test_add_status_for_home_timeline(status, account):
    item = Timeline(status=status, account=account, server=account.server, tag=Timeline.Tag.HOME)
    item.save()
    home_qs = account.timeline_home()
    status_pks = {x.status.pk for x in home_qs}
    assert status.pk in status_pks


@pytest.mark.parametrize(
    "first, last",
    [
        # ("Alice", "Alice"),
        ("Alice", "Smith"),
        ("Bob", "Smith"),
        ("Alice", "Jones"),
    ],
)
def test_combinations(first, last):
    assert first != last
