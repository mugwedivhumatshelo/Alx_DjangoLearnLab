from django.core.management import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Query all books by a specific author
        author = Author.objects.get(name='John Doe')
        books_by_author = Book.objects.filter(author=author)
        print("Books by John Doe:")
        for book in books_by_author:
            print(book.title)

        # List all books in a library
        library = Library.objects.get(name='Public Library')
        books_in_library = library.books.all()
        print("\nBooks in Public Library:")
        for book in books_in_library:
            print(book.title)

        # Retrieve the librarian for a library
        librarian = Librarian.objects.get(library=library)
        print("\nLibrarian for Public Library:")
        print(librarian.name)
