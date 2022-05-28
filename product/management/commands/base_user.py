from decouple import config

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Command(BaseCommand):

    help = _("Generate Base User")

    def add_arguments(self, parser):
        parser.add_argument('--username', '-u', type=str, help='Username')
        parser.add_argument('--email', '-e', type=str, help='Email')
        parser.add_argument('--password', '-p', type=str, help='Password')

    def handle(self, *args, **kwargs):
        username = kwargs.get('username') or config('BASE_USERNAME')
        email = kwargs.get('email') or config('BASE_USER_EMAIL')
        password = kwargs.get('password') or config('BASE_PASSWORD')

        user = self.create_superuser(email, username, password)

        self.stdout.write(self.style.SUCCESS(f'User: {user.email} is created !!'))

    def create_superuser(self, email, username, password):

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
