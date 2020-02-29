# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from apps.todo.models import TodoList, Category
import datetime

def index(request):
	todos = TodoList.objects.all()
	categories = Category.objects.all()
	if request.method == "POST": 
		if "taskAdd" in request.POST: 
			title = request.POST["description"] 
			category = request.POST["category_select"] 
			Todo = TodoList(title=title, category=Category.objects.get(name=category))
			Todo.save() 
			return redirect("todo:index") 
		
		if "taskDelete" in request.POST:
			checkedlist = request.POST["checkedbox"] 
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) 
				todo.delete() 

	return render(request, "index.html", {"todos": todos, "categorias":categories})

