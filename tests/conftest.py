import pytest
from django.utils import timezone

from locnus import models


@pytest.fixture()
def server():
    server = models.Server(api_base_url="https://example.com")
    server.save()
    return server


@pytest.fixture()
def mastodon_client():
    client = models.Client(name="pytooterapp", remote_id="remote_id", secret="secret")
    client.save()
    return client


@pytest.fixture()
def account(server):
    account = models.Account(server=server, username="alice", access_token="access_token")
    account.save()
    return account


@pytest.fixture()
def status_data():
    """Some raw status data from the Mastodon API."""
    return {
        "created_at": timezone.now(),
        "id": 123,
        "content": "Hello, world!",
    }


@pytest.fixture()
def status(server, request, status_data):
    m = request.node.get_closest_marker("num_toots")
    if m is not None and len(m.args) > 0:
        num_toots = m.args[0]
        for num in range(num_toots):
            status = models.Status(id=num, created_at=status_data["created_at"], data=status_data)
            status.save()
    else:
        status = models.Status(id=0, created_at=status_data["created_at"], data=status_data)
        status.save()
    return status
