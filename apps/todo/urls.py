from django.urls import path, include
from apps.todo.views import todo_index

app_name = "todo"

urlpatterns = [
    # path("", index, name="index"),
    path("", todo_index, name="todo_index")
]
