from django.urls import path
from apps.core.views import login, sign_up, reset_password, new_password

app_name = "core"

urlpatterns = [
    # signin and signup
    path("", login, name="login"),
    path("sign_up/", sign_up, name="sign_up"),
    path("reset_password/", reset_password, name="reset_password"),
    path("new_password/<uuid:user_uuid>/", new_password, name="new_password")
]
