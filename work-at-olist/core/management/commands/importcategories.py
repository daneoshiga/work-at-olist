import csv

from django.core.management.base import BaseCommand
from core.models import Channel, Category


class Command(BaseCommand):
    # TODO: add error handling and help text usage
    help = 'Imports one channel categories from csv file'

    def add_arguments(self, parser):
        parser.add_argument('channel')
        parser.add_argument('file')

    def handle(self, *args, **options):
        channel, _ = Channel.objects.get_or_create(name=options['channel'])
        Category.objects.filter(channel=channel).delete()
        with open(options['file']) as categories_file:
            categories_reader = csv.reader(categories_file)
            next(categories_reader)
            for row in categories_reader:
                count = Category.create_channel_categories(channel.name, row[0].split(' / '))
                print(count)
