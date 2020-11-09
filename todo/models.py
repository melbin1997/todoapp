from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    parent = models.IntegerField(default=-1)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
