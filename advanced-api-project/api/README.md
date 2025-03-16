# Book API

## Overview
This API provides endpoints for managing books.

## Endpoints
### GET /books/
* List all books

### GET /books/<int:pk>/
* Retrieve a book by ID

### POST /books/create/
* Create a new book

### PUT/PATCH /books/<int:pk>/update/
* Update an existing book

### DELETE /books/<int:pk>/delete/
* Delete a book by ID

## Permissions
* `AllowAny` for GET requests
* `IsAuthenticated` for POST, PUT/PATCH, and DELETE requests

# Filtering documentation
class BookListView(generics.ListAPIView):
    """
    List all books.

    Filtering:
        * title: Filter by book title
        * author: Filter by book author
        * publication_year: Filter by book publication year

    Searching:
        * search: Search for books by title or author

    Ordering:
        * ordering: Order books by title or publication year

    Example requests:
        * Filtering: GET http://localhost:8000/books/?title=Book+Title
        * Searching: GET http://localhost:8000/books/?search=Book+Title
        * Ordering: GET http://localhost:8000/books/?ordering=title
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
