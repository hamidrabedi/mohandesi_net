from django.contrib import admin
from .models import User, Exceptions

admin.site.register(User)
admin.site.register(Exceptions)