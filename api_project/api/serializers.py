from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Fields to serialize

    # Custom validation for publication_year to ensure it's not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer for books related to the author
    books = BookSerializer(many=True, read_only=True)  # Many books related to one author

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Fields to serialize

    