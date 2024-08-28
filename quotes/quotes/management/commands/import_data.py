import json
from django.core.management.base import BaseCommand
from ...models import Author, Quote


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Load authors from the JSON file
        with open('authors.json', 'r', encoding='utf-8') as authors_file:
            authors_data = json.load(authors_file)
            for author_data in authors_data:
                author, created = Author.objects.get_or_create(
                    fullname=author_data['fullname'],
                    born_date=author_data['born_date'],
                    born_location=author_data['born_location'],
                    description=author_data['description']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added author: {author.fullname}'))

        # Load quotes from the JSON file
        with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
            quotes_data = json.load(quotes_file)
            for quote_data in quotes_data:
                try:
                    author = Author.objects.get(fullname=quote_data['author'])
                    Quote.objects.create(
                        author=author,
                        quote=quote_data['quote'],
                        tags=quote_data['tags']
                    )
                    self.stdout.write(self.style.SUCCESS(f'Successfully added quote by: {author.fullname}'))
                except Author.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Author not found: {quote_data["author"]}'))
