from elasticsearch_dsl import Document, Text, connections
from django.conf import settings
from .models import Quote

connections.create_connection(hosts=[settings.ELASTICSEARCH_DSL['default']['hosts']])


class QuoteIndex(Document):
    author = Text()
    quote = Text()
    tags = Text()

    class Index:
        name = 'quotes'

    @classmethod
    def from_django(cls, quote):
        return cls(
            meta={'id': quote.id},
            author=quote.author.fullname,
            quote=quote.quote,
            tags=','.join(quote.tags)
        )

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
