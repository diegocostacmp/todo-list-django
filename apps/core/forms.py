from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Field

from .models import User


class SignInForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field("email", css_class="form-control"),
                Field("password", css_class="form-control"),
            )
        )

    class Meta:
        model = User
        sequence = ["email", "password"]
        exclude = [
            "username",
            "uuid",
            "last_login",
            "is_superuser",
            "full_name",
            "is_active",
            "groups",
            "user_permissions",
        ]
