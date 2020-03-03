# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User


class CoreAdmin(admin.ModelAdmin):
    list_display = ("email", "password", "is_active")

admin.site.register(User, CoreAdmin)
