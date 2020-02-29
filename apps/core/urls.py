from django.urls import path
from apps.core.views import login

app_name = "core"

urlpatterns = [
    path("", login, name="login"),
]
