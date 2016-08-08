import csv

from django.core.management.base import BaseCommand

from core.models import Category, Channel


class Command(BaseCommand):
    help = 'Imports one channel categories from csv file'

    def add_arguments(self, parser):
        parser.add_argument('channel', help='Channel name')
        parser.add_argument('file', help='CSV file containing categories path')

    def handle(self, *args, **options):
        channel, _ = Channel.objects.get_or_create(name=options['channel'])
        Category.objects.filter(channel=channel).delete()
        with open(options['file']) as categories_file:
            categories_reader = csv.reader(categories_file)
            next(categories_reader)
            for row in categories_reader:
                count = Category.create_channel_categories(channel, row[0].split(' / '))
                self.stdout.write('Processed {} Categories'.format(count))

        self.stdout.write(self.style.SUCCESS('Categories imported!'))
