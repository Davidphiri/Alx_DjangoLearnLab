from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # String field to store the author's name

class Book(models.Model):
    title = models.CharField(max_length=255)  # String field for the book's title
    publication_year = models.IntegerField()  # Integer field for the publication year
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # ForeignKey linking to Author model


