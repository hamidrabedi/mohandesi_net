import trace
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    EmailValidator
)

class User(AbstractUser):
    email = models.EmailField(
        _('Email Address'),
        unique=True,
        validators=[
            EmailValidator
        ]
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=15,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(15),
        ],
        unique = True
    )
    first_name = models.CharField(
        _('First Name'),
        max_length=30,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(30),
        ]
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=30,
        blank=True,
        null=True,
    )
    date_joined = models.DateTimeField(
        _('Date Joined'), 
        auto_now_add=True
        )
    is_staff = models.BooleanField(
        _('is staff'), 
        default=False
        )
    is_active = models.BooleanField(
        _('is active'), 
        default=True
        )

class Exceptions(models.Model):
    url = models.CharField(
        _('Url'),
        max_length=500
    )
    error = models.CharField(
        'Error',
        max_length= 500
    )
    traceback = models.CharField(
        'Traceback',
        max_length= 1000
    )

    def __str__(self):
        return self.error[:50]

    def __repr__(self):
        return self.error[:50]