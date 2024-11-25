from django.contrib import admin
from faqs.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    """Question model admin."""

    list_display = [
        "id",
        "user",
        "question",
        "deadline",
        "created_at",
        "updated_at",
    ]

    list_filter = ["user"]


class AnswerAdmin(admin.ModelAdmin):
    """Answer model admin."""

    list_display = [
        "id",
        "question",
        "answer",
        "created_at",
        "updated_at",
    ]

    list_filter = ["question"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
