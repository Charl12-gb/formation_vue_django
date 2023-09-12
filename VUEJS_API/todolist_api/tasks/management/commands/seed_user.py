from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with a test user'

    def handle(self, *args, **options):
        username = 'testuser'
        email = 'testuser@example.com'
        password = 'testpassword'

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'User {username} already exists'))
