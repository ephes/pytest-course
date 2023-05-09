import pytest

from locnus import models


@pytest.fixture()
def server():
    server = models.Server(api_base_url="https://example_from_api_conftest.com")
    return server
