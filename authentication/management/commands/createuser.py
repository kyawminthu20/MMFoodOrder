from django.core.management import BaseCommand, call_command
from authentication.models import Account

class Command(BaseCommand):

    def handle(self, *args, **options):
        a = Account(username='admin', is_superuser=True, user_type=['admin'])
        a.set_password('password')
        a.save()