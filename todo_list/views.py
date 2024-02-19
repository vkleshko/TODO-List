from django.views import generic

from todo_list.models import Task


class TaskListView(generic.ListView):
    queryset = Task.objects.all()
    context_object_name = "task_list"
    template_name = "todo_list/task_list.html"
