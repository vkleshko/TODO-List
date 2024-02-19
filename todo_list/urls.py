from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),

]

app_name = "todo_list"
