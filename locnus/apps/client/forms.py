from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm, PasswordInput

from .models import Client, Login


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["api_base_url", "name", "remote_id", "secret"]
        widgets = {
            "secret": PasswordInput(),  # Set the widget for the secret field to be a password input
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["client", "username", "access_token"]
        widgets = {
            "access_token": PasswordInput(),  # Set the widget for the secret field to be a password input
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))
