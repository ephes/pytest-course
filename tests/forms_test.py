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
    invalid_data = {"server": "", "username": "", "password": ""}
    form = forms.AccountForm(data=invalid_data)
    assert not form.is_valid()
