from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly  # Importing required permissions
from .models import Book
from .serializers import BookSerializer

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow unauthenticated access for reading, but authenticated for writing

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  # Retrieve a specific book by ID
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow unauthenticated access for reading

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # Use the Book model to save data
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # Retrieve the book to update
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # Delete a specific book
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
