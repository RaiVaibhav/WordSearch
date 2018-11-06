import csv

from django.core.management.base import BaseCommand
from wordsearch.models import Word

tsvfile= open('static/word_search.tsv')
reader = csv.reader(tsvfile, dialect='excel-tab')


class Command(BaseCommand):
    help = 'Import all the tsv data to database'

    def handle(self, *args, **options):
        for row in reader:
            word_object, created = Word.objects.get_or_create(
                name = row[0].strip(),
                frequency = int(row[1].strip())
            )