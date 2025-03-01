from django.core.management import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Query all books by a specific author
        author_name = 'John Doe'
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print("Books by {}:".format(author_name))
        for book in books_by_author:
            print(book.title)

        # List all books in a library
        library_name = 'Public Library'
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print("\nBooks in {}:".format(library_name))
        for book in books_in_library:
            print(book.title)

        # Retrieve the librarian for a library
        librarian = Librarian.objects.get(library=library)
        print("\nLibrarian for {}:".format(library_name))
        print(librarian.name)

