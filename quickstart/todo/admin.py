from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    """Todo model admin."""

    list_display = [
        "id",
        "user",
        "title",
        "description",
        "deadline",
        "status",
        "created_at",
        "updated_at",
        "is_in_progress",
    ]

    list_filter = [
        "user",
    ]


admin.site.register(Todo, TodoAdmin)
