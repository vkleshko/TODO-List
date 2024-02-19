from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteOrUndoView,
    TagListView,
)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="index"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"),
    path(
        "task/update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/complete_or_undo/<int:pk>/",
        TaskCompleteOrUndoView.as_view(),
        name="task-complete-or-undo"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"),

]

app_name = "todo_list"
