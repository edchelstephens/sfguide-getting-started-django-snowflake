# Generated by Django 5.1 on 2024-11-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faqs", "0002_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="answer",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
