import pytest

from locnus import forms


def test_server_form_empty_invalid():
    form = forms.ServerForm()
    assert not form.is_valid()


@pytest.mark.django_db
def test_server_form_invalid_url():
    form = forms.ServerForm({"api_base_url": "foo"})
    assert not form.is_valid()


@pytest.mark.django_db
def test_server_form_valid_url():
    form = forms.ServerForm({"api_base_url": "https://example.com"})
    assert form.is_valid()

    form.save()
    assert len(forms.Server.objects.all()) == 1


@pytest.mark.django_db
def test_account_form_invalid_data():
    form = forms.AccountForm()
    assert not form.is_valid()


@pytest.fixture(params=(forms.AccountForm, forms.ServerForm))
def empty_invalid_form(request):
    return request.param()


@pytest.mark.django_db
def test_empty_form_invalid(empty_invalid_form):
    assert not empty_invalid_form.is_valid()
