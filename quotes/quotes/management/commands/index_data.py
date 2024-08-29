from django.core.management.base import BaseCommand
from ...models import Quote
from ...search_indexes import QuoteIndex


class Command(BaseCommand):
    help = 'Elasticsearch'

    def handle(self, *args, **kwargs):
        for quote in Quote.objects.all():
            quote_index = QuoteIndex.from_django(quote)
            quote_index.save()
        self.stdout.write(self.style.SUCCESS('Successfully indexed all quotes.'))
