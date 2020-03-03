from __future__ import absolute_import, unicode_literals
from celery import shared_task 
from django.core.mail import send_mail


@shared_task
def send_email_task(email, user_uuid):
<<<<<<< HEAD
    url = "http://127.0.0.1:8000/redirect_reset/" + str(user_uuid) + "/"
=======
    url = "http://127.0.0.1:8000/new_password/" + str(user_uuid) + "/"
>>>>>>> f6daf384f14cb6a09b5159b28f7e2e7a30dbba47
    send_mail('E-mail de recuperação We Can Do!',
    url,
    'biomehubtest@gmail.com',
    [email])
    return None