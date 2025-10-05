"""
Unit tests for the Book API endpoints.

Tests include:
- CRUD operations (Create, Retrieve, Update, Delete)
- Permissions for authenticated and unauthenticated users
- Filtering, Searching, and Ordering functionality
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITests(APITestCase):
    """Test suite for the Book API."""

    def setUp(self):
        """Create test users and initial book data."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2023)

        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        """Anyone can list all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Anyone can retrieve a specific book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        """Authenticated users can create a new book."""
        self.client.login(username='testuser', password='testpass123')
        data = {'title': 'New Book', 'author': 'Author C', 'publication_year': 2025}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a new book."""
        data = {'title': 'No Auth Book', 'author': 'Anon', 'publication_year': 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Authenticated users can update a book."""
        self.client.login(username='testuser', password='testpass123')
        data = {'title': 'Updated Title', 'author': 'Author A', 'publication_year': 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Users can filter books by author."""
        response = self.client.get(self.list_url, {'author': 'Author B'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author B')

    def test_search_books(self):
        """Users can search books by title."""
        response = self.client.get(self.list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books_by_title(self):
        """Users can order books by title."""
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))
