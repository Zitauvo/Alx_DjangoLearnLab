from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author  # Make sure Author is imported

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create a test author (for Book.author ForeignKey)
        self.author = Author.objects.create(name='John Doe')  # Adjust fields if your Author model differs

        # Create a test book
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2024
        )

        # URL for listing books
        self.list_url = reverse('book-list')

    def test_list_books(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'New Book',
            'author': self.author.pk,  # POST expects the PK of the ForeignKey
            'publication_year': 2025
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        data = {
            'title': 'Unauthorized Book',
            'author': self.author.pk,
            'publication_year': 2025
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)

