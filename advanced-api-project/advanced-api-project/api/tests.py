from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    """
    Unit tests for the Book API endpoints:
    - Listing books
    - Creating books (authenticated and unauthenticated users)
    """

    def setUp(self):
        # Create a test user and one sample book
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.book = Book.objects.create(title="Test Book", author="John Doe", publication_year=2024)
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def test_list_books(self):
        """Ensure anyone can view the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a new book"""
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'New Book',
            'author': 'Jane Doe',
            'publication_year': 2025
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books"""
        data = {
            'title': 'Unauthorized Book',
            'author': 'Anon',
            'publication_year': 2025
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



