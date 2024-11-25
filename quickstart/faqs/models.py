from django.db import models
from uuid import uuid4


class Question(models.Model):
    """Question model."""

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    question = models.TextField()


class Answer(models.Model):
    """Answer model."""

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    question = models.ForeignKey("faqs.Question", on_delete=models.CASCADE)
    answer = models.TextField()
