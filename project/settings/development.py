from .base import *
from .secure import *
from .packages import *
from decouple import config

DEBUG = True
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# ######################## #
#     DJANGO EXTENSIONS    #
# ######################## #

INSTALLED_APPS.append('django_extensions')

SHELL_PLUS_IMPORTS = [
    "from django.db import connection as c",
]