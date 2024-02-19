from django.views import generic
from django.urls import reverse_lazy

from todo_list.forms import TaskForm
from todo_list.models import Task


class TaskListView(generic.ListView):
    queryset = Task.objects.all()
    context_object_name = "task_list"
    template_name = "todo_list/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"

