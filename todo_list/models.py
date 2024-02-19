from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"[{self.content}]; {self.tags}"

    def get_absolute_url(self):
        return reverse("todo_list:index")

    class Meta:
        ordering = ["done"]
