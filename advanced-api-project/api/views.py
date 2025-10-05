"""
Django REST Framework Custom Views and Generic Views for the Book Model

This module defines generic-based API views to handle CRUD operations
for the Book model efficiently.

Views:
- BookListView: Retrieve all books (public access)
- BookDetailView: Retrieve a specific book by ID (public access)
- BookCreateView: Create a new book (authenticated users only)
- BookUpdateView: Update an existing book (authenticated users only)
- BookDeleteView: Delete a book (authenticated users only)
"""
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books (anyone can view)
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Read-only access is allowed for everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve a single book by ID (anyone can view)
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a specific book using its ID.
    Read-only access is allowed for everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (only for authenticated users)
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to add a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book (only for authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update book details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (only for authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

