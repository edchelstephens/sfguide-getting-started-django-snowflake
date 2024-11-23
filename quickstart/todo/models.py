from django.db import models
import uuid


class Todo(models.Model):
    """Todo model."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="todos"
    )
    title = models.TextField()
    description = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    is_abandoned = models.BooleanField(default=False)

    def __repr__(self):
        """Python object string representation."""
        return "Todo(user={}, title={}, description={})".format(
            self.user.email, self.title, self.description
        )

    def __str__(self):
        """Human readable object string representation."""
        return "{} - {}".format(self.title, self.description)
