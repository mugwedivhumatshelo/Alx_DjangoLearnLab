from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List all books.

    * **URL:** `/books/`
    * **Method:** `GET`
    * **Permissions:** `IsAuthenticatedOrReadOnly`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a book by ID.

    * **URL:** `/books/<int:pk>/`
    * **Method:** `GET`
    * **Permissions:** `IsAuthenticatedOrReadOnly`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.

    * **URL:** `/books/create/`
    * **Method:** `POST`
    * **Permissions:** `IsAuthenticated`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.

    * **URL:** `/books/<int:pk>/update/`
    * **Method:** `PUT/PATCH`
    * **Permissions:** `IsAuthenticated`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.

    * **URL:** `/books/<int:pk>/delete/`
    * **Method:** `DELETE`
    * **Permissions:** `IsAuthenticated`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

