from django.contrib import admin
from .models import User, Exceptions

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=[
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'is_staff',
        'is_active',
    ]


@admin.register(Exceptions)
class ExceptionsAdmin(admin.ModelAdmin):
    list_display=[
        'url',
        'error',
    ]