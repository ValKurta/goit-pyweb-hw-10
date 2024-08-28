from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255)
    born_location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    author = models.ForeignKey(Author, related_name='quotes', on_delete=models.CASCADE)
    quote = models.TextField()
    tags = models.JSONField()

    def __str__(self):
        return self.quote[:50]
