# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TodoList, Category


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "uuid")


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Category, CategoryAdmin)
