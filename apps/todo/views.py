# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json

from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from apps.todo.models import Category, TodoList
from django.contrib.auth.decorators import login_required

from .forms import todoForm

@login_required
@require_http_methods(["POST", "GET"])
def todo_list(request):
    if "taskAdd" in request.POST:
        if request.POST["taskAdd"] != "":
            todo_edit(request)
            result = todo_index(request)
            context = {"todos": result[1], "categorias": result[2], "form": todoForm()}
        else:
            todo_create(request)
            result = todo_index(request)
            context = {"todos": result[1], "categorias": result[2], "form": todoForm()}
    elif "taskDelete" in request.POST:
        todo_delete(request)
        result = todo_index(request)
        context = {"todos": result[1], "categorias": result[2], "form": todoForm()}
    else:
        result = todo_index(request)
        context = {"todos": result[1], "categorias": result[2], "form": todoForm()}
    return render(request, result[0], context)


def todo_create(request):
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
    return None


@require_POST
def todo_retrieve(request):
    todo_uuid = request.POST.get("todo_uuid", "")
    todo = get_object_or_404(TodoList, uuid=todo_uuid)
    context = {
        "todo_uuid": todo_uuid,
        "title": str(todo.title),
        "category": str(todo.category.pk),
        "edit": True,
    }
    return JsonResponse(context, safe=False)


def todo_edit(request):
    if request.method == "POST":
        uuid = str(request.POST["taskAdd"])
        todo = get_object_or_404(TodoList, uuid=uuid)
        form = todoForm(request.POST or None, instance=todo)
        if form.is_valid():
            form.save()
    return None


@require_POST
def todo_delete(request):
    if request.method == "POST":
        checkedlist = request.POST.getlist("checkedbox")
        for i in checkedlist:
            todo = TodoList.objects.get(uuid=i)
            todo.delete()
    return None


def todo_index(request):
    template_name = "index.html"
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    return template_name, todos, categories
