from django.shortcuts import render


def login(request):
    template_name = "registration/login.html"
    return render(request, template_name, {})
