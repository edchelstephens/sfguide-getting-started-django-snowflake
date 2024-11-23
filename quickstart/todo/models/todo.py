from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Todo(models.Model):
    """Todo model."""

    class TodoStatus(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", _("In Progress")
        COMPLETED = "COMPLETED", _("Completed")
        CANCELLED = "CANCELLED", _("Cancelled")

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="todos"
    )
    title = models.TextField()
    description = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=30, choices=TodoStatus, default=TodoStatus.IN_PROGRESS
    )

    def __repr__(self):
        """Python object string representation."""
        return "Todo(user={}, title={}, description={})".format(
            self.user.email, self.title, self.description
        )

    def __str__(self):
        """Human readable object string representation."""
        return "{} - {}".format(self.title, self.description)

    @property
    def is_in_progress(self) -> bool:
        """Check if in progress"""
        return self.status == self.TodoStatus.IN_PROGRESS

    @property
    def is_completed(self) -> bool:
        """Check if completed"""
        return self.status == self.TodoStatus.COMPLETED

    @property
    def is_cancelled(self) -> bool:
        """Check if cancelled"""
        return self.status == self.TodoStatus.CANCELLED
