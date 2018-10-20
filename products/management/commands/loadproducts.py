from django.core.management.base import BaseCommand, CommandError
from products.models import Product
import json



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, required=True)

    def handle(self, *args, **options):
        try:
            with open('data.json', 'r') as file:

                for row in json.load(file):
                    Product.objects.create(**row)


        except Exception as err:
            raise CommandError(err)