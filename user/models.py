from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    EmailValidator
)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
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
        unique = True, 
        blank=True,
        null=True
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
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []
    
    objects = UserManager()

class Exceptions(models.Model):
    url = models.CharField(
        _('Url'),
        max_length=500
    )
    error = models.CharField(
        'Error',
        max_length= 500
    )
    traceback = models.TextField(
        'Traceback',
    )

    def __str__(self):
        return self.error[:50]

    def __repr__(self):
        return self.error[:50]


