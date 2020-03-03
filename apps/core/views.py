# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
from datetime import datetime as dt

from django.contrib import auth
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (require_GET, require_http_methods,
                                          require_POST)

from apps.core.models import User
from todo_list_django import settings

from .tasks import send_email_task


@require_http_methods(["POST", "GET"])
def login(request):
    # try:
    email = request.POST.get("inputEmail", "")
    password_input = request.POST.get("inputPassword", "")

    if request.method == "POST":
        print(request.POST)
        if email == settings.EMAIL_BASE:
            print("email padrao")
            # xx - day * 2
            # yy - month * 2
            # zz - hour update

            # user exist db ?
            u_count = User.objects.filter(email=email).count()
            if u_count == 1:
                base = dt.now()
                xx = int(base.day) * 2
                yy = int(base.month) * 2
                zz = base.hour

                if int(len(str(xx)) == 1):
                    xx = "0" + str(xx)

                if int(len(str(yy)) == 1):
                    yy = "0" + str(yy)

                if int(len(str(zz)) == 1):
                    zz = "0" + str(zz)

                # new password generated
                password_verified = str(xx) + str(yy) + str(zz)
                u = get_object_or_404(User, email=email)
                u.set_password(password_verified)
                u.save()
            else:
                print("aqui........")
                context = {"msg_return": "not_found"}
                template_name = "registration/login.html"
                return render(request, template_name, context)

        # auth user with new password
        user = auth.authenticate(request, email=email, password=password_input)

        if user is not None:
            auth.login(request, user)
            return redirect("todo:todo_list")
        else:
            template_name = "registration/login.html"
            context = {"msg_return": "invalid_credentials"}
            return render(request, template_name, context)
    else:
        print("na excessao")
        template_name = "registration/login.html"
        return render(request, template_name, {})
    # except:
    #     template_name = "registration/login.html"
    #     return render(request, template_name, {})

@require_http_methods(["POST", "GET"])
def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("inputEmailSignUp", "")
        password = request.POST.get("inputPasswordSignUp", "")

        # verifica se a conta ja existe
        user = auth.authenticate(request, email=email, password=password)
        if user is None:
            user = User.objects._create_user(email=email, password=password)
            return redirect("todo:todo_list")
        else:
            context = {"msg_return": "error"}
            template_name = 'registration/sign_up.html' 
            return render(request, template_name, context)
    else:
        template_name = 'registration/sign_up.html' 
        return render(request, template_name, {})


def send_email_retrieve(request):
    template_name = "registration/reset_password.html"
    if request.method == "POST":
        email = request.POST.get("inputReset", "")
        u_count = User.objects.filter(email=email).count()
        if u_count == 1:
            # send mail in background
            u = get_object_or_404(User, email=email)
            user_uuid = u.uuid
            send_email_task.delay(email, user_uuid)

            context = {"msg_return": "success"}
            return render(request, template_name, context)
        else:
            context = {"msg_return": "error"}
            return render(request, template_name, context)
    else:
        context = {}
        return render(request, template_name, context)

@require_http_methods(["POST", "GET"])
def redirect_reset(request, user_uuid):
    template_name = "registration/new_password.html"
    return render(request, template_name, {"user_uuid": user_uuid})


@require_http_methods(["POST", "GET"])
def reset_password(request):
    if request.method == "POST":
        user_uuid = request.POST.get("userUuid", "")
        password = request.POST.get("passwordReset", "")

        # verifica se a conta ja existe
        u = get_object_or_404(User, uuid=user_uuid)
        u.set_password(password)
        u.save()

        context = {"msg_return": "password_updated"}
        template_name = "registration/login.html"
        return render(request, template_name, context)
    else:
        template_name = "registration/sign_up.html"
        return render(request, template_name, {})
