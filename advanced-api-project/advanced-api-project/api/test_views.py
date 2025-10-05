from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class TestBookAPI(APITestCase):
    """API tests for the Book model"""

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book", author="John Doe", publication_year=2024
        )
        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def test_list_books(self):
        """Anyone can view the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.content))

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.login(username='testuser', password='testpass123')
        data = {'title': 'New Book', 'author': 'Jane Doe', 'publication_year': 2025}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        data = {'title': 'Unauthorized Book', 'author': 'Anon', 'publication_year': 2025}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)


