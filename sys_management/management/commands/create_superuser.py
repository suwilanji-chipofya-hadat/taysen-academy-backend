import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from dotenv import load_dotenv

class Command(BaseCommand):
    help = 'Create a superuser with credentials from environment variables'

    def handle(self, *args, **options):
        # Load environment variables from .env file
        load_dotenv()

        # Get user details from environment variables
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', get_random_string(7))

        # Create the superuser
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))
