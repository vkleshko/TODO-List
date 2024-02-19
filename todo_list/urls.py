from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create")
]

app_name = "todo_list"
