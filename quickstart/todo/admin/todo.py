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
        "is_completed",
        "is_cancelled",
    ]

    list_filter = [
        "user",
    ]

    @admin.display(boolean=True)
    def is_in_progress(self, obj):
        """Check if in progress"""
        return obj.is_in_progress

    @admin.display(boolean=True)
    def is_completed(self, obj):
        """Check if completed"""
        return obj.is_completed

    @admin.display(boolean=True)
    def is_cancelled(self, obj):
        """Check if cancelled"""
        return obj.is_cancelled


admin.site.register(Todo, TodoAdmin)
