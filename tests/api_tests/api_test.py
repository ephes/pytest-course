import pytest

from locnus import models


@pytest.fixture()
def server(server):
    print(server.api_base_url)
    server = models.Server(api_base_url="https://example_from_api_module.com")
    return server


def test_api_client(server):
    print(server)
    assert False
