from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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

