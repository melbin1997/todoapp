from django.contrib import admin
from . import models

class TodoListAdmin(admin.ModelAdmin):
    list_display=("id", "title", "parent", "completed")

admin.site.register(models.TodoList, TodoListAdmin)
