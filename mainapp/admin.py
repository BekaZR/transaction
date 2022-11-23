from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from mainapp.models import Payment, User


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username",)}),
        (_("Personal info"), {"fields": ("balance",)}),
        
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

admin.site.register(User, UserAdmin)

admin.site.register(Payment)
