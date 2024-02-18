from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False)
    done = models.BooleanField(default=False)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    def __str__(self):
        return f"[{self.content}]; {self.tag}"

    class Meta:
        ordering = ["created"]
