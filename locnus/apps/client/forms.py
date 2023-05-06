from django.forms import ModelForm

from client.models import Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["api_base_url", "name", "remote_id", "secret"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))  # Add a submit button
