import pytest
from django.urls import reverse

from locnus import views


def test_get_create_server(client):
    url = reverse("locnus:get-create-server")
    response = client.get(url)
    assert response.status_code == 200
    assert "form" in response.context
    assert isinstance(response.context["form"], views.ServerForm)


@pytest.mark.django_db
def test_post_create_server(client):
    url = reverse("locnus:post-create-server")
    response = client.post(url, data={"api_base_url": "https://example-foo.com"})
    assert response.status_code == 302
    assert response.url == reverse("locnus:server-list")
    assert len(views.Server.objects.all()) == 1


@pytest.mark.django_db
def test_get_public_timeline_missing_server(client):
    non_existent_server_pk = 999
    url = reverse("locnus:public-timeline", args=[non_existent_server_pk])
    response = client.get(url)
    assert response.status_code == 404


@pytest.fixture(params=["locnus:server-list", "locnus:get-create-server", "locnus:get-create-account"])
def view_name(request):
    return request.param


@pytest.fixture(params=[200, 201])
def response_status_code(request):
    return request.param


@pytest.mark.django_db
def test_get_views(client, view_name, response_status_code):
    url = reverse(view_name)
    r = client.get(url)
    assert r.status_code == response_status_code
