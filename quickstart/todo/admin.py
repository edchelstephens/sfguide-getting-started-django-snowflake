from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    """Todo model admin."""

    list_display = [
        "id",
        "title",
        "description",
        "user",
        "deadline",
        "created_at",
        "updated_at",
        "is_completed",
        "is_abandoned",
    ]

    list_filter = ["user", "is_completed", "is_abandoned"]


admin.site.register(Todo, TodoAdmin)
