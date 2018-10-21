from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Extra', {
                'fields': ('image', 'phone')
            },
        ),
    )

admin.site.register(Account, AccountAdmin)