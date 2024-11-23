from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    """UserAdmin."""

    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_verified",
        "is_staff",
        "date_joined",
        "last_login",
    ]


admin.site.register(User, UserAdmin)
