from __future__ import absolute_import, unicode_literals
from celery import shared_task 
from django.core.mail import send_mail


@shared_task
def send_email_task(email, user_uuid):
    url = "http://127.0.0.1:8000/redirect_reset/" + str(user_uuid) + "/"
    send_mail('E-mail de recuperação We Can Do!',
    url,
    'biomehubtest@gmail.com',
    [email])
    return None