from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

class Command(BaseCommand):
    def handle(self, *args, **options):
        import environ
        env = environ.Env()
        User = get_user_model()
        username = env("DJANGO_SUPERUSER_USERNAME", default="admin")
        email = env("DJANGO_SUPERUSER_EMAIL", default="admin@example.com")
        password = env("DJANGO_SUPERUSER_PASSWORD", default="admin")

        try:
            User.objects.create_superuser(username, email, password)
            self.stdout.write(f'Superuser {username} created successfully')
        except IntegrityError:
            self.stdout.write(f'Superuser {username} already exists')