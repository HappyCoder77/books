from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
