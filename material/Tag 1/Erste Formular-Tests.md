```python forms_test.py
import pytest

from locnus import forms  
  
  
def test_server_form_empty_invalid():  
	form = forms.ServerForm()  
	assert not form.is_valid()


def test_server_form_invalid_url():  
	form = forms.ServerForm({"api_base_url": "invalid"})  
	assert not form.is_valid()


@pytest.mark.django_db  
def test_server_form_valid():  
	form = forms.ServerForm({"api_base_url": "https://example.com"})  
	assert form.is_valid()
```