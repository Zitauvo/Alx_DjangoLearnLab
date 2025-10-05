from django.urls import path
from . import views

urlpatterns = [
    # List all books and create a new book
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),

    # Retrieve details of a single book
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Update a specific book
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),

    # Delete a specific book
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]
