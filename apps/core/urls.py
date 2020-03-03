from django.urls import path

from apps.core.views import login, reset_password, send_email_retrieve, sign_up, redirect_reset

app_name = "core"

urlpatterns = [
    # signin and signup
    path("", login, name="login"),
    path("sign_up/", sign_up, name="sign_up"),
    path("send_email_retrieve/", send_email_retrieve, name="send_email_retrieve"),
    path("redirect_reset/<uuid:user_uuid>/", redirect_reset, name="redirect_reset"),
    path("reset_password/", reset_password, name="reset_password")
]
