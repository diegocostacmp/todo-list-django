from django.urls import path, include
from apps.todo.views import index

app_name="todo"

urlpatterns = [
    path("", index, name="index"),
]
