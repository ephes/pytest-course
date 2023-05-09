import pytest

from locnus import models


@pytest.fixture()
def server():
    server = models.Server(api_base_url="https://example.com")
    return server
