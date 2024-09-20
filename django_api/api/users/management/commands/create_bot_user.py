from django.conf import settings
from django.core.management import BaseCommand
from rest_framework.authtoken.models import Token

from users.models import TodoUser

class Command(BaseCommand):


    def handle(self, *args, **options):

        TodoUser.objects.filter(username='bot').delete()

        user = TodoUser.objects.create_user(username='bot', password='bot')

        Token.objects.create(user=user, key=settings.BOT_TOKEN)