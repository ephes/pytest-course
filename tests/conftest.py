import pytest

from locnus import models


@pytest.fixture()
def server():
    server = models.Server(api_base_url="https://example.com")
    server.save()
    return server


@pytest.fixture()
def account(server):
    account = models.Account(server=server, username="alice", access_token="access_token")
    account.save()
    return account
