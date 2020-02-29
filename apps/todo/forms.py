from django import forms
from .models import TodoList

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Submit,
    Row,
    Column,
    Div,
    ButtonHolder,
    Field,
)


class todoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(todoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field("title"),
                Field("category")
            )
        )
    class Meta:
        model = TodoList
        sequence = ["title", "category"]
        exclude = ["created"]
