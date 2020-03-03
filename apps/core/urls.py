from django.urls import path
<<<<<<< HEAD

from apps.core.views import login, reset_password, send_email_retrieve, sign_up, redirect_reset
=======
from apps.core.views import login, sign_up, reset_password, new_password
>>>>>>> f6daf384f14cb6a09b5159b28f7e2e7a30dbba47

app_name = "core"

urlpatterns = [
    # signin and signup
    path("", login, name="login"),
    path("sign_up/", sign_up, name="sign_up"),
<<<<<<< HEAD
    path("send_email_retrieve/", send_email_retrieve, name="send_email_retrieve"),
    path("redirect_reset/<uuid:user_uuid>/", redirect_reset, name="redirect_reset"),
    path("reset_password/", reset_password, name="reset_password")
=======
    path("reset_password/", reset_password, name="reset_password"),
    path("new_password/<uuid:user_uuid>/", new_password, name="new_password")
>>>>>>> f6daf384f14cb6a09b5159b28f7e2e7a30dbba47
]
