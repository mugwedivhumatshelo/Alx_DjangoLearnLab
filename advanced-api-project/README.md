# api/models.py
from django.db import models

# Define the Author model
class Author(models.Model):
    # Name field to store the author's name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Define the Book model
class Book(models.Model):
    # Title field to store the book's title
    title = models.CharField(max_length=255)
    # Publication year field to store the year the book was published
    publication_year = models.IntegerField()
    # Foreign key linking to the Author model
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



# api/serializers.py
from rest_framework import serializers
from .models import Book, Author

# Define the BookSerializer
class BookSerializer(serializers.ModelSerializer):
    # Define the meta class to specify the model and fields
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for the publication year
    def validate_publication_year(self, value):
        if value > 2024:  # assuming current year is 2024
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Define the AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to serialize related books
    books = BookSerializer(many=True, read_only=True)

    # Define the meta class to specify the model and fields
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

