from django.db import models
from uuid import uuid4


class TimeStampedModel(models.Model):
    """Timestamped model."""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Question(TimeStampedModel):
    """Question model."""

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        """Human readable object string representation."""
        return self.question


class Answer(TimeStampedModel):
    """Answer model."""

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    question = models.ForeignKey("faqs.Question", on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        """Human readable object string representation."""
        return self.answer
