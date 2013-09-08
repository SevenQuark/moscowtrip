from apps.instagram_api.parser import add_places
from apps.main.models import Place
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = ''
    help = 'Adding places to base'

    def handle(self, *args, **options):
        all_places = Place.objects.all()
        add_places(all_places)
