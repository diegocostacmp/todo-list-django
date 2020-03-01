from django.urls import path, include
from apps.todo.views import todo_list, todo_edit, todo_retrieve

app_name = "todo"

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path("todo_retrieve/", todo_retrieve, name="todo_retrieve"),
]
