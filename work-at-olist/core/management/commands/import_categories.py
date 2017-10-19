import csv

from django.core.management.base import BaseCommand

from categories.models import Category
from channels.models import Channel


class Command(BaseCommand):
    help = 'Import categories from csv file from given channel'

    def add_arguments(self, parser):
        parser.add_argument('channel', help='Channel name')
        parser.add_argument('file', help='CSV file with categories tree')

    def handle(self, *args, **options):
        channel, created = Channel.objects.get_or_create(name=options['channel'])
        count = 0

        if created is False:
            self.stdout.write(f'\nDeleting categories from {channel.name}.\n\n')
            Category.objects.filter(channel=channel).delete()

        with open(options['file']) as file:
            csv_file = csv.reader(file)

            for row in csv_file:
                categories_list = row[0].split(' / ')
                count += Category.import_categories(channel, categories_list)

        self.stdout.write(f'\n{count} categories processed!')
